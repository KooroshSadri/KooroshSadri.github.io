(function () {
  'use strict';

  var viewer = document.querySelector('[data-document-viewer]');
  if (!viewer) return;

  var fieldset = viewer.querySelector('.document-switch');
  var options = viewer.querySelectorAll('input[name="document"]');
  var frame = viewer.querySelector('[data-document-frame]');
  var heading = viewer.querySelector('#document-title');
  var openLink = viewer.querySelector('[data-document-open]');
  var downloadLink = viewer.querySelector('[data-document-download]');
  var status = viewer.querySelector('[data-document-status]');
  var current = 'cv';

  function selectDocument(value, updateAddress, announce) {
    var selected = null;
    for (var i = 0; i < options.length; i += 1) {
      if (options[i].value === value) selected = options[i];
    }
    if (!selected) return;

    selected.checked = true;
    var title = selected.getAttribute('data-title');
    var url = selected.getAttribute('data-pdf');
    if (value !== current) {
      frame.src = url + '#view=FitH&navpanes=0';
    }
    current = value;
    heading.textContent = title;
    frame.title = 'Koorosh Sadri - ' + title + ' PDF';
    openLink.href = url;
    openLink.setAttribute('aria-label', 'Open ' + title + ' PDF in a new tab');
    downloadLink.href = url;
    downloadLink.setAttribute('download', selected.getAttribute('data-download'));
    downloadLink.setAttribute('aria-label', 'Download ' + title + ' PDF');

    if (announce) status.textContent = title + ' selected.';
    if (updateAddress && window.history && window.history.replaceState) {
      try {
        window.history.replaceState(null, '', window.location.pathname + window.location.search + '#' + value);
      } catch (error) {
        // The document controls still work if the browser restricts history.
      }
    }
  }

  function selectFromAddress() {
    selectDocument(window.location.hash.toLowerCase() === '#resume' ? 'resume' : 'cv', false, false);
  }

  for (var i = 0; i < options.length; i += 1) {
    options[i].addEventListener('change', function () {
      if (this.checked) selectDocument(this.value, true, true);
    });
  }
  window.addEventListener('hashchange', selectFromAddress);
  selectFromAddress();
  fieldset.hidden = false;
}());
