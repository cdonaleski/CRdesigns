# CR Design Co. — Website

A two-page site for CR Design Co. Craft nights, the beginner needlepoint class, host
sign-up and newsletter. **Hosted on GoHighLevel** — see
[`docs/GHL-DEPLOY.md`](docs/GHL-DEPLOY.md).

Live preview: https://claude.ai/artifact/DArQPYRkuTek7WycLTGfzi

---

## Still to fill in

One placeholder is highlighted in brass on the pages so they're impossible to miss.
Grep both pages for the bracketed text:

```bash
grep -n "\[" index.html needlepoint.html assets/forms.js
```


| Placeholder | Where | What it needs |
|---|---|---|
| `[CONTACT EMAIL]` | Both footers, all four forms | Your business email. Set it **once** — the `CONTACT` variable at the top of `assets/forms.js`. |
| Shop link | Header + footer nav, both pages | Currently a non-clickable `<span class="nav-soon">Shop<span class="chip">Soon</span></span>`. When the shop is live, replace that span with `<a href="YOUR-URL">Shop</a>` in both pages. |


Remove the `class="fill"` wrapper from each once it's real, so the brass highlight goes away.

Six photographs are still placeholders too — specs, AI prompts and shooting notes are in
[`docs/IMAGE-BRIEF.md`](docs/IMAGE-BRIEF.md).

---

## Files

```
index.html                  Home page.
needlepoint.html            The beginner class: details, host sign-up, save-a-seat.
assets/
  site.css                  All styling for both pages. One stylesheet, shared.
  forms.js                  Form handling + the contact email. Shared.
  logo-mark.png             CR monogram, cropped from your logo. Header + favicon.
  logo-full.png             Full logo lockup. Cream band above the footer.
  rachel.jpg                Founder portrait, About section. 900px, compressed.
  logo-original.webp        Untouched logo you supplied. Keep — source of truth.
  rachel-original.png       Untouched portrait, 1254px. Keep.
build.py                    Builds both deployment targets.
dist/standalone/            Complete single-file pages, for any normal web host.
dist/ghl/                   Paste-ready blocks for GoHighLevel. Not edited by hand.
docs/GHL-DEPLOY.md          How to get it onto GHL, and the forms decision.
docs/IMAGE-BRIEF.md         Specs and AI prompts for the six photos still needed.
```

The two HTML pages plus `assets/` are the project. Everything else is convenience.

Both pages share `assets/site.css` and `assets/forms.js`, so a change to colors, type or
form behavior lands on both at once. That's the main reason to edit the stylesheet rather
than adding inline styles to a page.

---

## Working on it

Run every command below from the project folder.

**Preview locally.** Don't just double-click `index.html` — the fonts and layout
behave better over a real server:

```bash
python3 -m http.server 8421
```

Then open http://localhost:8421. Ctrl-C to stop. (Port 8421 rather than the usual 8000
because you already have something running there.)

If a style change doesn't show up, it's the browser caching `site.css` — hard-reload with
Cmd-Shift-R.

**Swapping a photo.** Drop the new file in `assets/`, replace the matching
`<div class="slot">` block with an `<img>` — the exact steps are at the end of
[`docs/IMAGE-BRIEF.md`](docs/IMAGE-BRIEF.md) — then re-run the build. Check both pages:
Photos 01, 02 and 03 each appear more than once.

```bash
python3 build.py
```

**Publishing.** `python3 build.py` writes both targets:

- `dist/ghl/` — the blocks you paste into GoHighLevel. Every CSS rule is scoped to a
  `.crd` wrapper so the site's styles and GHL's can't reach into each other, with a
  defensive reset on top. Full instructions in [`docs/GHL-DEPLOY.md`](docs/GHL-DEPLOY.md).
- `dist/standalone/` — complete single-file pages. Keep the two together in a folder and
  the link between them works. For emailing, a USB stick, or any ordinary web host.

Never hand-edit anything in `dist/` — it's overwritten on every build.

---

## Design notes

Decisions worth knowing before you change things.

**Two pages, not three.** The mockups had Home / Needlepoint / Ornaments. Needlepoint
earned its own page — it carries the class spec and two distinct forms (host a night vs.
attend one), which are different asks from different people. Ornaments did not: it's one
"coming soon" line with no dates, so it lives as a card on the home page and a tile on the
class page. Give it a page when it has a date and a price.

**The host offer is the strongest thing you have.** "Gather ten guests and your seat is
free" turns one customer into eleven, and it's the only thing on the site that recruits
on your behalf. That's why it gets a full dark-green band on the class page and its own
form, rather than a line in a paragraph.

**Palette** — pulled from the logo, not invented:

| Token | Hex | Used for |
|---|---|---|
| `--ink` | `#374936` | The logo green. Headings, buttons, footer. |
| `--cream` | `#F6F2EB` | Page ground |
| `--sand` | `#EFE9DF` | Craft Nights band |
| `--blush` | `#E8C9C0` | Newsletter band |
| `--brass` | `#B08A57` | The rule under the logo. Hairlines, accents, highlights. |

**Type.** Cinzel for the wordmark only — it matches the engraved caps in the logo.
Cormorant Garamond for headings. Jost for body and UI. Loaded from Google Fonts with
real fallback stacks, so nothing collapses if the CDN is slow.

**The logo images use `mix-blend-mode: multiply`.** Your logo files are dark green on
solid white. Multiply makes the white disappear against the cream ground without needing
a transparent PNG. This works on light backgrounds only — that's why the footer uses the
wordmark set in Cinzel rather than the image.

**The nav is identical on both pages.** Same markup, same order, byte for byte — links
are written page-qualified (`index.html#about`, `needlepoint.html#host`) so the same
markup works from either page, and a same-page target still jumps without a reload. There
is deliberately no "current page" highlight; add one and the menu changes between pages
again.

**The header row is full at phone width.** `Home`, `About`, `Host a Night` and `Shop`
carry `.hide-sm` and drop out below 820px, leaving the logo, `Needlepoint` and the
`Newsletter` button — which is exactly as much as fits in 375px. All of them remain in
the footer nav. Adding a seventh item means building a proper mobile menu rather than
hiding more.

**Single theme, on purpose.** No dark mode. This is a cream-and-olive brand identity;
flipping it to dark would break it. Every color is painted explicitly so it holds
regardless of the viewer's system setting.

**All four forms open the visitor's email app**, pre-addressed to you with every field
they filled in written into the body. No backend, no signup, no monthly fee, works today.
`assets/forms.js` reads each field's own label to build that message, so if you add a
field to a form it shows up in the email automatically — nothing else to change.

The tradeoff is real and worth knowing: a mailto form loses people who use webmail
without a configured mail app, and nothing is stored anywhere but your inbox. When
bookings get steady enough that this stings, get a free Flodesk or Mailchimp account and
replace a `<form>` block with their embed code. The surrounding layout will hold.

---

## Hosting

**GoHighLevel** is the plan — full walkthrough in
[`docs/GHL-DEPLOY.md`](docs/GHL-DEPLOY.md). The short version: GHL has no file hosting, so
each page goes into a Custom Code element as one self-contained block, and
`python3 build.py` produces those blocks.

Read the **forms** section of that doc before launching. The forms currently open the
visitor's email app, which works but creates no GHL contact and triggers no workflow —
which is most of the reason to be on GHL at all.

If GHL ever stops being the right home, `dist/standalone/` drops onto Netlify, Cloudflare
Pages or GitHub Pages as-is. In that case, update the `og:image` meta tag in both source
pages to the full URL (`https://yourdomain.com/assets/logo-full.png`) so link previews
work when the site is shared.
