# Image brief

The site has nine photo placements across its two pages, filled by six photographs.
Every one is still a placeholder, plus the founder portrait is worth replacing. The
placeholders render as tinted panels tagged **Photo 01** through **Photo 06**, so you
can see at a glance which shot fills which slot.

## Specs

| Slot | Where | Ratio | Export | Filename |
|---|---|---|---|---|
| ~~**Photo 01**~~ | **Class page "Save a seat" — DONE** | 2:3 vertical | 1000 × 1500px, JPEG, 298KB | `assets/table-set.jpg` ✅ |
| ~~**Photo 08**~~ | **Home hero — DONE** | 4:5 vertical | 1200 × 1500px, JPEG, 294KB | `assets/home-hero.jpg` ✅ |
| ~~**Photo 07**~~ | **Class page "More Craft Nights" — DONE** | 3:2 horizontal | 1400 × 933px, JPEG, 272KB | `assets/ladies-night.jpg` ✅ |
| ~~**Photo 02**~~ | **Class page hero — DONE** | 2:3 vertical | 1000 × 1500px, JPEG, 262KB | `assets/craft-night.jpg` ✅ |
| ~~**Photo 09**~~ | **Home needlepoint card — DONE** | 6:4 horizontal | 958 × 639px, JPEG, 163KB | `assets/needlepoint-card.jpg` ✅ |
| ~~**Photo 03**~~ | **Home ornaments card (6:4) + class page "Coming soon" (4:3) — DONE** | 4:3 native | 1200 × 857px, JPEG, 226KB | `assets/ornament-kit.jpg` ✅ |
| **Photo 04** | Home About section | 1:1 square | 1200 × 1200px, JPEG, <250KB | `assets/rachel.jpg` (replace) |
| ~~**Photo 05**~~ | **Class page hero inset — DONE** | 4:5 vertical | 960 × 1200px, JPEG, 261KB | `assets/kit.jpg` ✅ |
| ~~**Photo 06**~~ | **Class page "Coming soon" — DONE** | 4:3 horizontal | 1200 × 900px, JPEG, 309KB | `assets/intermediate.jpg` ✅ |

Nine placements, six files. Photos 01, 02 and 03 each appear more than once, and that's
deliberate — reusing them ties the two pages together as one site and saves you three
shoots.

**Palette to hold across all six** — this is what makes them read as one set rather
than six stock photos:

- deep olive `#374936`
- cream `#F6F2EB`
- soft blush `#E8C9C0`
- brass `#B08A57`

Warm, slightly underexposed, natural window light throughout. No cool tones, no hard
flash, no blue-white daylight bulbs.


### Already in place

`assets/craft-night.jpg` — four women around a sunlit table, each with a hoop — fills the
**class page hero**.

`assets/table-set.jpg` — the table laid out before anyone arrives, canvases on stands at
every place — fills **"Save me a seat"** on the class page.

Untouched originals sit beside each one as `*-original.png`. Don't delete those; they're
what you re-crop from if a slot ever changes shape.

Both also match slots on the **home page** that are still empty — `craft-night.jpg` is
almost word-for-word Photo 01's brief for the home hero, and `table-set.jpg` would serve
"More craft nights". Reusing them there was always the plan; say the word.

`assets/kit.jpg` — the branded kit on marble: printed tulip canvas, banded skeins, stork
scissors, pouch and card — fills the **hero inset** on the class page. It gets a cream mat
and a soft shadow there, because without one the two photos run together where they
overlap.

`assets/ornament-kit.jpg` — the branded wood ornament painting kit, box open with paints,
brushes and three finished ornaments — fills the **Ornament Painting** card in the class
page's "Coming soon" row. It reads at 335px wide, where the kit photo in the hero inset
does not, because the subject is fewer, larger objects.

`assets/intermediate.jpg` — a finished blue hydrangea canvas with pincushion, stork
scissors and books — fills the **Intermediate Needlepoint** card.

`assets/ladies-night.jpg` — six women laughing around a table on a winter evening, wine
and a chalkboard — fills **More Craft Nights**. It was shot in the evening where the hero
is daytime, which is what separates a ladies' night from the beginner class at a glance.

**The Needlepoint page is fully photographed. Zero placeholders remain on it.**

`assets/home-hero.jpg` — the same evening gathering as `ladies-night.jpg`, shot wider in
the sitting room — fills the **home hero**. It leads on the social side of a craft night
rather than the crafting, which is the right call now that the About copy is about rest
and taking a night off.

`ornament-kit.jpg` is reused on the **home Ornament Painting card**, where it renders
around 330px wide and reads far better than it does in the class page's smaller trio.

`assets/needlepoint-card.jpg` — women holding up finished canvases (a daisy, a bow, a
hydrangea) over a table of wool bobbins — fills the **home Needlepoint card**. Cropped
from below the supplied image's title block, which tightened the framing as a bonus: it
now shows the canvases close enough to read at card size, which a wide room shot would
not have.

## Every slot on the site is filled

Both pages, nine placements, nine photographs. Nothing below is outstanding — it's kept
as the record of what each slot wants, for when something gets reshot.

Originals for every supplied image sit beside their web copies in `assets/` as
`*-original.png`. Those are what you re-crop from if a slot ever changes shape — don't
delete them.

### Card ratios

The two cards under *Pick up something new* are **6:4** (`aspect-ratio: 3/2` on
`.card .slot`). The "Coming soon" tiles on the class page stay 4:3 — they're narrower
columns, and a 6:4 tile there would be too short to read.

Shoot anything destined for the home cards at **6:4 or wider**. Wider is safe: the slot
crops to fill from the centre, so extra width is headroom, while a tall photo loses its
top and bottom.

### If you reshoot, shoot these

 a **close** needlepoint shot for the home page's Needlepoint card
(a hoop and hands, not a whole room — a wide shot won't read at card size), plus Photos
03, 05 and 06.

### Keep marketing text out of the photos

The version supplied for Photo 06 had *Intermediate Needlepoint · SKILLS | CREATIVITY |
COMMUNITY* and the logo set into the image itself. The card underneath already carries
that heading, so on the page the title appeared twice, once as a graphic and once as live
text — and baked-in type doesn't scale with the layout, can't be selected or read aloud,
and breaks the set with the other cards, which are photographs.

So the file in `assets/` is cropped to the canvas and tools, text excluded. The uncropped
version is kept at `assets/intermediate-original.png` if it's wanted for Instagram or a
flyer, where a titled graphic is exactly right.

The same applies to anything generated from here: ask for the scene, not the poster. The
`CR DESIGN CO.` printed on the canvas binding is different — that's branding on a real
product, and it belongs.

### The kit photo deserves a bigger slot

The hero inset renders at **189 × 236px** on desktop and **114 × 142px** on phones. At that
size the composition reads — you can tell it's a kit — but none of the branding does: the
logo on the box, the `CR DESIGN CO.` printed down the canvas border, and the
*A Brighter Day Stitches Here* card are all below legible size.

That's the most thoroughly branded asset in the set being used as a texture accent. The
home page's **Needlepoint card** is still empty and renders around 480px wide, which would
show all of it. Worth moving, or worth shooting a second, simpler still life for the inset
and giving the kit its own moment.

### A note on the table photo

At full resolution the book spines in the centre of the table read `HEDLEPORE` over
`NEEDLEPOINT` — the top one is garbled, which is the usual giveaway that an image was
generated rather than shot. In the 4:5 crop the site uses it lands small and reads as
texture, so it very likely passes unnoticed. Worth knowing it's there: if it bothers you,
regenerate with *no books on the table*, or paint the spine out in any photo editor.

---

## Before you generate Photo 02 — read this

**Don't use AI for the needlepoint close-up.** Image models are specifically bad at two
things: hands, and the physical logic of thread. You will get six fingers, stitches that
don't connect to anything, and thread that passes through itself. Needlepointers spot it
instantly, and they are exactly the audience you're trying to win.

Shoot it on your phone. Portrait mode, near a window, midday, no flash. Ten minutes of
real stitching beats any prompt.

The same caution applies loosely to Photo 01 — multiple people means multiple sets of
hands. If you can photograph one real craft night, do that and skip the prompts entirely.

---

## Prompts

Written for ChatGPT / DALL·E, Midjourney, or Gemini. For Midjourney, append the `--ar`
flag noted under each.

### Photo 01 — Hero

```
Four women in their thirties and forties seated around a long light oak
table in a bright home dining room, mid-conversation, one laughing,
crafting supplies spread between them — embroidery hoops, wound spools
of thread, small scissors, mugs of tea. Shot from a slightly elevated
three-quarter angle so the table leads into the frame. Soft diffused
afternoon light from a large window on the left, warm and slightly
underexposed. Color palette of cream, olive green, soft blush pink and
warm brass. Linen and natural wood textures. Shallow depth of field,
85mm lens look, film grain. Warm documentary feel, candid not posed.
Vertical composition with open space in the upper third.
```

`--ar 4:5`

Avoid: *text, logos, watermarks, harsh flash, cool blue tones, close-up hands, visible
faces in sharp focus*

> Ask for faces slightly turned or soft-focused. It sidesteps the uncanny-face problem
> and reads as a genuine candid rather than a stock photo.

### Photo 02 — Needlepoint *(shoot this one for real)*

If you must generate it, frame so hands are small or cropped out entirely:

```
Still life of a needlepoint project in progress on a light oak table:
a wooden embroidery hoop holding cream canvas with a partially finished
botanical design in olive green and blush pink wool, surrounded by
neatly wound thread spools, small gold embroidery scissors, and a
thimble. Overhead flat-lay composition. Soft diffused window light from
the upper left, warm tone, gentle shadows. Cream, olive green, blush and
brass palette. Linen tablecloth texture. Shallow depth of field,
macro lens look, film grain.
```

`--ar 5:4`

Avoid: *hands, fingers, people, text, watermarks, cool tones, cluttered background*

**Real-shoot version:** canvas in hoop on a linen cloth, window to your left, thread and
scissors arranged loosely around it. Shoot from directly above — stand on a chair. Take
twenty, keep one.

### Photo 03 — Ornament Painting

```
Six hand-painted glass ball ornaments in cream, sage green and soft
blush, drying on a light oak table beside small paint pots and fine
brushes resting on a folded linen cloth. Some ornaments finished with
delicate botanical brushwork, one still wet and glistening. Soft
diffused window light from the left, warm and slightly underexposed,
gentle highlights on the glass. Cream, olive green, blush and brass
palette. Shallow depth of field, 50mm lens look, film grain.
Horizontal composition, quiet and unhurried.
```

`--ar 5:4`

Avoid: *hands, people, Christmas trees, red and gold holiday cliché, text, glitter,
harsh specular highlights*

> Steer away from traditional red-and-green Christmas. Your brand is sage and blush —
> holding that makes the ornament night look like *yours*, not like every other seasonal
> craft workshop in town.

### Photo 04 — Founder portrait (replacement)

The current portrait is styled for a different business: white blazer, office patio,
LinkedIn energy. It's the one image on the page that doesn't feel like the rest of it.
Worth reshooting.

```
Natural portrait of a woman in her late thirties with shoulder-length
wavy light brown hair, seated at a craft table beside a sunlit window,
turned toward the camera with a warm relaxed smile. Wearing a soft
cream linen shirt or an oatmeal knit sweater. An embroidery hoop and
thread spools rest on the table in soft foreground blur. Interior of a
warm home studio, olive green and cream tones, dried botanicals out of
focus behind her. Soft diffused window light, warm and slightly
underexposed. Shallow depth of field, 85mm lens look, film grain.
Square composition.
```

`--ar 1:1`

Avoid: *blazer, office setting, corporate headshot lighting, white seamless backdrop,
harsh flash, cool tones*

**Or — five minutes, real:** sit at your craft table near a window. Someone shoots on
portrait mode from slightly above eye level. Hoop in your hands or on the table. Look at
the camera, not the work. Cream or oatmeal top.

> For a business where people will walk in and meet you, the photo on the site has to
> match the person at the door. That matters more than how polished it is.


### Photo 05 — Threads & tools (class page hero inset)

This one sits small — about 230px wide — overlapping the big hero photo on a blush
panel. Keep it simple; detail will be lost at that size.

```
Tight overhead still life of needlepoint supplies on a folded cream
linen cloth: three or four neatly wound skeins of wool in olive green,
blush pink and cream, small gold embroidery scissors, and a few needles.
Nothing else in frame. Soft diffused window light from the upper left,
warm and slightly underexposed, gentle shadows. Cream, olive green,
blush and brass palette. Shallow depth of field, macro lens look,
film grain. Vertical composition, generous empty space around the
objects.
```

`--ar 4:5`

Avoid: *hands, people, clutter, text, watermarks, cool tones, busy background*

> Shoot this one for real if you can — it's just objects on a cloth, no hands involved,
> so it's the easiest of the six and AI has no advantage.

### Photo 06 — Intermediate needlepoint (coming soon)

```
A finished needlepoint piece with more intricate botanical detail
resting on a light oak table, in cream, olive green and blush wool on
canvas, with a few thread skeins and small scissors at the edge of the
frame. Soft diffused window light from the left, warm and slightly
underexposed. Cream, olive green, blush and brass palette. Shallow
depth of field, 50mm lens look, film grain. Horizontal composition,
quiet and unhurried.
```

`--ar 4:3`

Avoid: *hands, fingers, people, text, watermarks, cool tones, cluttered background*

> Same caution as Photo 02 — AI renders stitches that don't make physical sense. If you
> have a finished intermediate piece, photograph it. That's a two-minute job and it will
> look better.

---

## Wiring a finished photo in

1. Drop the file in `assets/` using the filename from the specs table.
2. In `index.html`, find the matching `<div class="slot">` block and replace the whole
   block with:

   ```html
   <img src="assets/hero.jpg" alt="Friends gathered around the craft table">
   ```

   Keep the `hero-slot` / `card` sizing classes on a wrapper if you want the aspect
   ratio locked:

   ```html
   <div class="hero-slot"><img src="assets/hero.jpg" alt="..."></div>
   ```

3. Write a real `alt` description — it's what screen readers announce and what shows if
   the image fails to load.
4. Re-run the build:

   ```bash
   python3 build.py
   ```

### Compressing before you add it

Phone photos are 3–5MB. That's far too heavy for a web page. From this folder:

```bash
sips -Z 1600 ~/Downloads/YOUR-PHOTO.jpg --out assets/hero.jpg && sips -s format jpeg -s formatOptions 72 assets/hero.jpg --out assets/hero.jpg
```

`-Z 1600` caps the long edge at 1600px; `formatOptions 72` sets JPEG quality. Check the
result is under 400KB with `ls -la assets/`.
