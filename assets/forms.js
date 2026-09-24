/* CR Design Co. — footer contact link and copyright year.
 *
 * All four forms (newsletter on both pages, save-a-seat, host sign-up) are now
 * GoHighLevel embeds, so submissions create a contact and can trigger a
 * workflow. Nothing here touches them — an iframe is a separate document and
 * this script cannot reach inside it. Style those in GHL itself; see
 * docs/GHL-FORMS.md.
 */
(function () {
  'use strict';

  /* The only thing you need to edit. */
  var CONTACT = 'hello@crdesignco.com';

  var mail = document.getElementById('foot-mail');
  if (mail) {
    mail.textContent = CONTACT;
    mail.href = 'mailto:' + CONTACT;
  }

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- Mobile menu ----
   * The header row cannot hold six items at phone width, so below 820px the
   * nav is replaced by this panel. Visibility is toggled with the `hidden`
   * attribute rather than inline styles, so CSS stays in charge of layout.
   */
  var toggle = document.getElementById('nav-toggle');
  var panel = document.getElementById('mobile-nav');

  if (toggle && panel) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      panel.hidden = !open;
      document.body.classList.toggle('nav-open', open);
    };

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    /* Following a link closes the panel. Same-page anchors need handling:
       the body is still scroll-locked when the browser tries to jump, so the
       scroll is swallowed and you land on a closed menu at the same position.
       Close first, then scroll ourselves — offset by the sticky header so the
       heading is not hidden underneath it. */
    panel.addEventListener('click', function (e) {
      var link = e.target.closest('a');
      if (!link) return;

      var href = link.getAttribute('href') || '';
      setOpen(false);

      if (href.charAt(0) !== '#' || href.length < 2) return;
      var target = document.getElementById(href.slice(1));
      if (!target) return;

      e.preventDefault();
      var head = document.querySelector('.site-head');
      var offset = head ? head.getBoundingClientRect().height : 0;
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      requestAnimationFrame(function () {
        window.scrollTo({
          top: Math.max(0, target.offsetTop - offset),
          behavior: reduce ? 'auto' : 'smooth'
        });
        if (history.replaceState) history.replaceState(null, '', href);
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });

    /* Rotating to landscape can cross the breakpoint with the panel open,
       which would leave the body scroll-locked on a desktop-width layout. */
    window.addEventListener('resize', function () {
      if (window.innerWidth > 820) setOpen(false);
    });
  }
})();
