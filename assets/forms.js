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
})();
