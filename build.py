#!/usr/bin/env python3
"""
Build deployable copies of the site.

index.html and needlepoint.html are the source: ordinary HTML pages that
reference assets/ alongside them. Two things get built from them.

  dist/standalone/   Complete pages with the stylesheet, script and images
                     baked in. One file each. Email them, open them from a USB
                     stick, or drop the folder on any normal web host.

  dist/ghl/          Paste-ready blocks for GoHighLevel. No <html>/<head>/<body>
                     — GHL supplies those. Everything is wrapped in a single
                     .crd element and every CSS rule is scoped to it, so the
                     site's styles cannot leak out into GHL's page chrome and
                     GHL's styles have a harder time leaking in.

    python3 build.py

Re-run it after any change to a page, the stylesheet, the script, or a photo.
See docs/GHL-DEPLOY.md for what to do with dist/ghl/.
"""

import base64
import mimetypes
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
PAGES = {"index.html": "home.html", "needlepoint.html": "needlepoint.html"}

SCOPE = ".crd"

STYLESHEET = re.compile(r'<link[^>]+rel="stylesheet"[^>]+href="(assets/[^"]+\.css)"[^>]*>')
SCRIPT = re.compile(r'<script[^>]+src="(assets/[^"]+\.js)"[^>]*>\s*</script>')
ASSET = re.compile(r'(?P<attr>src|href)="(?P<path>assets/[^"]+)"')
FONT_LINK = re.compile(r'<link[^>]+fonts\.(?:googleapis|gstatic)[^>]*>')


# --------------------------------------------------------------------------
# shared helpers
# --------------------------------------------------------------------------

def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def inline_images(html: str, missing: list, label: str) -> str:
    def swap(m):
        target = ROOT / m.group("path")
        if not target.exists():
            missing.append(f"{label}: {m.group('path')}")
            return m.group(0)
        return f'{m.group("attr")}="{data_uri(target)}"'
    return ASSET.sub(swap, html)


# --------------------------------------------------------------------------
# CSS scoping
# --------------------------------------------------------------------------

def split_rules(css: str):
    """Yield (prelude, body, is_block) for each top-level rule."""
    i, start, depth = 0, 0, 0
    n = len(css)
    while i < n:
        c = css[i]
        if c == "{":
            if depth == 0:
                prelude = css[start:i]
                depth, body_start = 1, i + 1
                i += 1
                while i < n and depth:
                    if css[i] == "{":
                        depth += 1
                    elif css[i] == "}":
                        depth -= 1
                    i += 1
                yield prelude, css[body_start:i - 1], True
                start = i
                continue
        elif c == ";" and depth == 0:
            # a statement like @import / @charset
            yield css[start:i + 1], "", False
            start = i + 1
        i += 1
    tail = css[start:]
    if tail.strip():
        yield tail, "", False


def scope_selector(sel: str) -> str:
    sel = sel.strip()
    if not sel:
        return sel
    # tokens carry the page's design tokens — they have to land on the wrapper
    if sel in (":root", "body", ":root:not([data-theme='light'])"):
        return SCOPE
    # html rules stay global: scroll-behavior and reduced-motion only work there
    if sel == "html" or sel.startswith("html "):
        return sel
    if sel.startswith("*"):
        return f"{SCOPE} {sel}"
    return f"{SCOPE} {sel}"


def scope_css(css: str) -> str:
    out = []
    for prelude, body, is_block in split_rules(css):
        head = prelude.strip()
        if not is_block:
            if head:
                out.append(head)
            continue

        if head.startswith("@"):
            name = head.split()[0].lower()
            if name in ("@media", "@supports", "@layer", "@container"):
                # recurse: the rules inside still need scoping
                out.append(f"{head}{{\n{scope_css(body)}\n}}")
            else:
                # @font-face, @keyframes, @page — leave completely alone
                out.append(f"{head}{{{body}}}")
            continue

        # strip comments from the selector list before splitting on commas
        clean = re.sub(r"/\*.*?\*/", "", head, flags=re.S)
        selectors = [scope_selector(s) for s in clean.split(",") if s.strip()]
        if selectors:
            out.append(",\n".join(selectors) + "{" + body.strip() + "}")
    return "\n".join(out)


# --------------------------------------------------------------------------
# targets
# --------------------------------------------------------------------------

def build_standalone(src: str, out_name: str, missing: list) -> Path:
    html = (ROOT / src).read_text(encoding="utf-8")

    def css(m):
        p = ROOT / m.group(1)
        if not p.exists():
            missing.append(f"{src}: {m.group(1)}")
            return m.group(0)
        return "<style>\n" + p.read_text(encoding="utf-8") + "\n</style>"

    def js(m):
        p = ROOT / m.group(1)
        if not p.exists():
            missing.append(f"{src}: {m.group(1)}")
            return m.group(0)
        return "<script>\n" + p.read_text(encoding="utf-8") + "\n</script>"

    html = STYLESHEET.sub(css, html)
    html = SCRIPT.sub(js, html)
    html = inline_images(html, missing, src)

    # standalone pages link to each other by their source filenames
    dest = OUT / "standalone" / src
    dest.write_text(html, encoding="utf-8")
    return dest


GHL_RESET = """
/* ---- Defensive reset (added by build.py) ----
 * A GHL theme styles bare elements — section, form, p, li, input — and those
 * rules reach inside this block wherever the site's own CSS doesn't set the
 * same property. A host border, background or padding then shows up in the
 * middle of the design.
 *
 * So: neutralize every element this markup uses, then let the scoped site CSS
 * below re-assert what it actually wants. This block must come FIRST — it is
 * the same specificity as most of the site's own rules, and later wins.
 */
.crd,.crd *,.crd *::before,.crd *::after{box-sizing:border-box}
.crd header,.crd nav,.crd main,.crd section,.crd footer,.crd article,.crd div,
.crd h1,.crd h2,.crd h3,.crd h4,.crd p,.crd span,.crd a,.crd small,.crd b,.crd i,
.crd em,.crd strong,.crd img,.crd svg,.crd hr,.crd figure,.crd blockquote,
.crd form,.crd label,.crd fieldset,.crd legend,
.crd ol,.crd ul,.crd li,.crd dl,.crd dt,.crd dd{
  margin:0;padding:0;border:0;background:transparent;
  font-family:inherit;font-size:inherit;font-weight:inherit;font-style:inherit;
  line-height:inherit;letter-spacing:inherit;text-transform:none;
  color:inherit;text-align:inherit;text-decoration:none;
  list-style:none;box-shadow:none;border-radius:0;
}
.crd input,.crd select,.crd textarea,.crd button{
  margin:0;font-family:inherit;font-size:inherit;line-height:normal;
  letter-spacing:inherit;text-transform:none;border-radius:0;box-shadow:none;
}
.crd img,.crd svg{max-width:100%;display:block;height:auto}
.crd a{text-decoration:none}
"""

GHL_OVERRIDES = """
/* ---- GoHighLevel overrides (added by build.py) ----
 * GHL drops this block inside its own containers. Those containers often carry
 * a transform or overflow rule, either of which silently disables position:
 * sticky — so the header is static here. If it sticks fine on your funnel,
 * change position:static back to position:sticky below.
 */
.crd .site-head{position:static;backdrop-filter:none;-webkit-backdrop-filter:none}
/* the logo images are dark-on-white and rely on multiply against a light
   ground; if GHL's section sits on a dark color, drop these two lines */
.crd .brand img,.crd .logo-band img{mix-blend-mode:multiply}
"""


def build_ghl(src: str, out_name: str, missing: list, media: bool = False) -> Path:
    html = (ROOT / src).read_text(encoding="utf-8")

    fonts = FONT_LINK.findall(html)

    css_match = STYLESHEET.search(html)
    css_text = ""
    if css_match:
        p = ROOT / css_match.group(1)
        if p.exists():
            css_text = p.read_text(encoding="utf-8")
        else:
            missing.append(f"{src}: {css_match.group(1)}")

    js_match = SCRIPT.search(html)
    js_text = ""
    if js_match:
        p = ROOT / js_match.group(1)
        if p.exists():
            js_text = p.read_text(encoding="utf-8")
        else:
            missing.append(f"{src}: {js_match.group(1)}")

    body = re.search(r"<body>(.*)</body>", html, re.S)
    inner = body.group(1).strip() if body else html
    inner = STYLESHEET.sub("", inner)
    inner = SCRIPT.sub("", inner)
    if media:
        # leave filenames behind for a find-and-replace against GHL's Media Library
        inner = ASSET.sub(
            lambda m: f'{m.group("attr")}="MEDIA_URL/{Path(m.group("path")).name}"', inner)
    else:
        inner = inline_images(inner, missing, src)

    # links between pages become GHL page paths
    inner = inner.replace('href="index.html"', 'href="/"')
    inner = inner.replace('href="needlepoint.html"', 'href="/needlepoint"')

    parts = []
    parts.append("<!-- CR Design Co. — paste this whole block into a GoHighLevel")
    parts.append(f"     Custom Code / HTML element. Source: {src}")
    parts.append("     Built by build.py — edit the source, not this file.")
    if media:
        parts.append("")
        parts.append("     BEFORE PASTING: upload the files from assets/ to GHL's Media")
        parts.append("     Library, then find-and-replace every MEDIA_URL/<name> below")
        parts.append("     with that file's Media Library URL. See docs/GHL-DEPLOY.md. -->")
    else:
        parts.append("     Images are baked in as data URIs — nothing else to upload. -->")
    parts.extend(fonts)
    parts.append("<style>")
    parts.append(GHL_RESET.strip())
    parts.append(scope_css(css_text))
    parts.append(GHL_OVERRIDES.strip())
    parts.append("</style>")
    parts.append(f'<div class="crd">')
    parts.append(inner)
    parts.append("</div>")
    parts.append("<script>")
    parts.append(js_text)
    parts.append("</script>")

    stem = Path(out_name).stem
    dest = OUT / "ghl" / (f"{stem}-media.html" if media else out_name)
    dest.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return dest


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "standalone").mkdir(parents=True)
    (OUT / "ghl").mkdir(parents=True)

    missing: list = []

    print("standalone — complete pages, for any normal web host")
    for src, ghl_name in PAGES.items():
        if not (ROOT / src).exists():
            print(f"  skipped (no such page): {src}")
            continue
        d = build_standalone(src, ghl_name, missing)
        print(f"  {src:20} -> dist/standalone/{src}  ({d.stat().st_size:,} bytes)")

    print("\nghl — paste-ready blocks, CSS scoped to .crd")
    for src, ghl_name in PAGES.items():
        if not (ROOT / src).exists():
            continue
        d = build_ghl(src, ghl_name, missing)
        print(f"  {src:20} -> dist/ghl/{d.name:24} ({d.stat().st_size:>9,} bytes)  images baked in")
        m = build_ghl(src, ghl_name, missing, media=True)
        print(f"  {'':20} -> dist/ghl/{m.name:24} ({m.stat().st_size:>9,} bytes)  Media Library URLs")

    for item in missing:
        print(f"\n  missing: {item}")

    print("\nNext: docs/GHL-DEPLOY.md")


if __name__ == "__main__":
    main()
