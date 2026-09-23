/* CR Design Co. — form handling and footer contact link.
 *
 * There's no server behind this site, so every form composes an email to you
 * and opens the visitor's mail app with it pre-filled. They press send; you get
 * a message with all their answers in the body.
 *
 * To switch a form over to Flodesk/Mailchimp later, replace that <form> block
 * with their embed code. This script ignores any form it doesn't recognize.
 */
(function () {
  'use strict';

  /* ---- The only thing you need to edit ---- */
  var CONTACT = '[CONTACT EMAIL]';

  /* Subject line per form id. A form not listed here is left alone. */
  var SUBJECTS = {
    'seat-form': 'Save me a seat — needlepoint class'
  };

  /* ---- Footer contact link ---- */
  var mail = document.getElementById('foot-mail');
  if (mail) {
    mail.textContent = CONTACT;
    mail.href = 'mailto:' + CONTACT;
  }

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- A control's own label text ----
   * Controls sit inside their <label>, so label.textContent would swallow the
   * control's own text too — every <option> of a <select>, for instance. Clone
   * the label, strip the controls out, and read what's left.
   */
  function labelFor(form, el) {
    var label = form.querySelector('label[for="' + el.id + '"]');
    if (!label) return el.name || el.id;

    var clone = label.cloneNode(true);
    var nested = clone.querySelectorAll('input, select, textarea');
    for (var i = 0; i < nested.length; i++) {
      nested[i].parentNode.removeChild(nested[i]);
    }
    return clone.textContent.replace(/\s+/g, ' ').trim() || el.name || el.id;
  }

  /* ---- Read a form into "Label: value" lines ---- */
  function readFields(form) {
    var lines = [];
    var controls = form.querySelectorAll('input, select, textarea');

    for (var i = 0; i < controls.length; i++) {
      var el = controls[i];
      if (el.type === 'submit' || el.type === 'button') continue;

      var name = labelFor(form, el);

      if (el.type === 'checkbox') {
        lines.push(name + ': ' + (el.checked ? 'Yes' : 'No'));
        continue;
      }

      var value = (el.value || '').trim();
      if (value) lines.push(name + ': ' + value);
    }
    return lines;
  }

  /* ---- Wire up each known form ---- */
  Object.keys(SUBJECTS).forEach(function (id) {
    var form = document.getElementById(id);
    if (!form) return;

    var note = form.querySelector('.form-note');
    var emailField = form.querySelector('input[type="email"]');

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var email = emailField ? emailField.value.trim() : '';
      if (!email || email.indexOf('@') < 1) {
        if (note) note.textContent = 'Please add an email address so we know where to write.';
        if (emailField) emailField.focus();
        return;
      }

      var body = readFields(form).join('\n');

      if (note) note.textContent = 'Opening your email app — press send and you’re all set.';

      window.location.href =
        'mailto:' + CONTACT +
        '?subject=' + encodeURIComponent(SUBJECTS[id]) +
        '&body=' + encodeURIComponent(body);
    });
  });
})();
