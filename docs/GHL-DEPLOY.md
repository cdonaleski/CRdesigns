# Deploying to GoHighLevel

GHL has no file hosting — you can't upload a folder of HTML, CSS and images the way
you would with a normal web host. What it does have is a **Custom Code / HTML element**
you can drop into a page, and that's where the site goes: one block per page, with the
stylesheet, script and images already folded in.

`python3 build.py` produces those blocks in `dist/ghl/`.

> GHL renames menu items fairly often. The steps below describe what you're looking for
> by function rather than quoting exact labels, so find the nearest match in your account.

---

## Which file to paste

The build makes two versions of each page. They render identically — the difference is
where the photos live.

| File | Size | Photos | Use when |
|---|---|---|---|
| `home-media.html` · `needlepoint-media.html` | ~30KB | GHL Media Library URLs | **Recommended.** Faster pages, editor stays responsive |
| `home.html` · `needlepoint.html` | ~430KB | Baked into the HTML | You want it live in ten minutes with no uploads |

The baked-in versions are 430KB of text going into a browser code editor. That works, but
the editor gets sluggish and GHL has been known to choke on very large pastes. Start with
the `-media` versions unless you're in a hurry.

---

## First: upload the images

Skip this if you're using the baked-in version.

1. Open GHL's **Media Library**.
2. Upload everything from `assets/` **except** `site.css`, `forms.js` and the two
   `*-original.*` files:
   - `logo-mark.png`
   - `logo-full.png`
   - `rachel.jpg`
   - plus any photos you've added since (`hero.jpg`, `needlepoint.jpg`, …)
3. Copy each file's public URL.
4. Open `dist/ghl/home-media.html` in any text editor and find-and-replace:

   | Find | Replace with |
   |---|---|
   | `MEDIA_URL/logo-mark.png` | the Media Library URL for that file |
   | `MEDIA_URL/logo-full.png` | …and so on for each |

   Do the same in `needlepoint-media.html`. Searching for `MEDIA_URL` finds every one.

---

## Build the two pages

### 1. Create a Website (not a Funnel)

Sites → Websites → new site. A funnel works too, but a website gives you cleaner page
paths, and this is a site rather than a linear sales flow.

### 2. Set the page paths

This matters — the links in the block are already written to match:

| Page | Path must be |
|---|---|
| Home | `/` |
| Needlepoint | `needlepoint` |

If you name the second page something else, open the block and change every
`href="/needlepoint"` to your path before pasting.

### 3. Paste each block

On each page:

1. Delete whatever starter section GHL put there. You want an empty page.
2. Add a **Row**, then a **Custom Code / HTML** element inside it.
3. Paste the entire contents of the matching file — the opening `<!-- comment -->` through
   the final `</script>`. All of it.
4. Set the containing **Section and Row to full width**, and set their padding and margin
   to **0**. GHL defaults to a boxed container with generous padding; leave it and the
   design sits in a letterbox with a stripe of GHL's background down each side.

Repeat for the Needlepoint page with its own file.

### 4. Fonts (optional but worth it)

Each block carries its own Google Fonts `<link>`, so the fonts load either way. If you'd
rather load them once for the whole site, move these two lines into the site's
**Head Tracking Code** and delete them from both blocks:

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500&display=swap">
```

### 5. Check it on a phone

Use the builder's mobile preview, then look at the real published URL on your actual
phone. GHL's mobile preview is not always honest about what ships.

---

## Why the CSS is written the way it is

Open one of the files and you'll see every rule starts with `.crd`. That's deliberate and
it solves a real problem in both directions.

**Styles leaking out.** The site styles bare elements — `section`, `form`, `input`, `a`,
`p`. Pasted raw into a GHL page, those rules would hit GHL's own elements: every form on
the site gets cream inputs, every section gets 120px of padding. Scoping every rule under
`.crd` keeps them inside this block.

**Styles leaking in.** GHL themes also style bare elements, and those rules reach *into*
your block wherever the design doesn't set the same property. Tested against a deliberately
aggressive theme, the host's section borders and background bled straight through the
middle of the page. The build now emits a defensive reset at the top of the block that
neutralizes every element this markup uses, so the design re-asserts everything it needs.

**Don't hand-edit the files in `dist/ghl/`.** Edit `index.html`, `needlepoint.html` or
`assets/site.css` and re-run `python3 build.py`. The scoping is applied at build time;
hand-edits are lost on the next build and are easy to get subtly wrong.

---

## The forms — read this before you launch

The four forms currently open the visitor's email app with their answers pre-filled. That
works anywhere and costs nothing, **but on GHL it throws away the main reason to be on
GHL.** A mailto form creates no contact, starts no workflow, triggers no follow-up. You
get an email in your inbox and everything after that is manual.

The host sign-up is the one that hurts most. Someone offering to gather ten guests is the
most valuable lead this site produces, and it should land in your CRM with an automation
behind it.

### What to do instead

Rebuild each form as a **GHL form**, then swap it in:

1. Sites → Forms → build a form with the matching fields:

   | Replaces | Fields |
   |---|---|
   | Newsletter (both pages) | First name, Email |
   | Save me a seat | First name, Last name, Email, Phone, checkbox: *Also tell me about intermediate classes and new craft nights* |
   | Host sign-up | First name, Last name, Email, Phone, City/neighborhood, dropdown: *Expected guests* (10–12 / 13–15 / 16+), Preferred dates |

2. Style each form in GHL's form builder to match:

   | | Value |
   |---|---|
   | Button / heading green | `#374936` |
   | Page background | `#F6F2EB` |
   | Newsletter band background | `#E8C9C0` |
   | Input background | `#FBF4F1` (newsletter) · `#FFFDF9` (host form) |
   | Input border | `#CFAFA5` (newsletter) · `#C7BEAF` (host form) |
   | Accent / hairline | `#B08A57` |
   | Heading font | Cormorant Garamond |
   | Body & button font | Jost |

3. In the pasted block, find the `<form ...>` … `</form>` you're replacing and swap the
   whole thing for GHL's embed code. The surrounding layout is a grid cell — it will hold
   whatever you put in it.

4. Attach a workflow to each: an instant auto-reply at minimum, and for the host form, a
   task to call them.

Until you do that, the mailto forms work and nobody is blocked. This is the upgrade, not
a prerequisite.

---

## After any change to the site

```bash
python3 build.py
```

Then re-paste the affected block. There's no partial update — the block is one unit, so
changing one headline means replacing the whole thing. Because of that, make your edits in
the source files, build once, and paste once, rather than tweaking directly in GHL.

If you've already swapped in GHL forms, you'll need to re-do those swaps after a rebuild.
Keep a copy of each embed snippet somewhere handy so it's a paste rather than a rebuild.

---

## Known quirks

**The header doesn't stick.** In the GHL build it's deliberately static. GHL wraps custom
code in containers that often carry a `transform` or `overflow` rule, either of which
silently kills `position: sticky` — a sticky header that sometimes works is worse than a
static one that always does. If it behaves on your funnel, find this line near the end of
the `<style>` block and change `static` back to `sticky`:

```css
.crd .site-head{position:static; ...}
```

**The logo needs a light background.** Your logo files are dark green on solid white, and
the build uses `mix-blend-mode: multiply` to make that white disappear against the cream.
It only works over a light color. If you ever put the block on a dark GHL section, remove
the `mix-blend-mode` line and use a transparent PNG instead.

**Anchor links.** `#host`, `#newsletter` and friends scroll within a page. They work, but
if GHL's own sticky nav is enabled it will cover the top of the target section. Either
turn GHL's nav off (this site brings its own header) or add scroll padding.

**Placeholders still show.** The brass-highlighted `[YOUR CITY]`, `[CONTACT EMAIL]`,
`[WHAT'S INCLUDED]`, `[DATE]` and `[LOCATION]` are live on the page. Fill them in the
source files before you paste, or you'll publish them.
