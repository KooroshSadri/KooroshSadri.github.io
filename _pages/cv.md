---
layout: archive
title: "CV / Résumé"
excerpt: "Curriculum vitae and résumé of Koorosh Sadri."
permalink: /cv/
author_profile: true
document_viewer: true
---

<section class="documents" data-document-viewer aria-label="CV and résumé documents">
  <p class="documents__notice">These are placeholder documents. Updated versions will be added here.</p>

  <fieldset class="document-switch" hidden>
    <legend class="documents__sr-only">Choose a document</legend>
    <label class="document-switch__option">
      <input id="cv" type="radio" name="document" value="cv" checked
        data-pdf="{{ '/files/cv.pdf' | relative_url }}"
        data-title="Curriculum vitae" data-download="Koorosh_Sadri_CV.pdf">
      <span>CV</span>
    </label>
    <label class="document-switch__option">
      <input id="resume" type="radio" name="document" value="resume"
        data-pdf="{{ '/files/resume.pdf' | relative_url }}"
        data-title="Résumé" data-download="Koorosh_Sadri_Resume.pdf">
      <span>Résumé</span>
    </label>
  </fieldset>

  <div class="document-toolbar">
    <h2 class="document-toolbar__title" id="document-title">Curriculum vitae</h2>
    <div class="document-toolbar__links">
      <a data-document-open href="{{ '/files/cv.pdf' | relative_url }}" target="_blank" rel="noopener" aria-label="Open curriculum vitae PDF in a new tab">Open PDF</a>
      <a data-document-download href="{{ '/files/cv.pdf' | relative_url }}" download="Koorosh_Sadri_CV.pdf" aria-label="Download curriculum vitae PDF">Download</a>
    </div>
  </div>

  <iframe class="document-frame fitvidsignore" data-document-frame
    src="{{ '/files/cv.pdf' | relative_url }}#view=FitH&amp;navpanes=0"
    title="Koorosh Sadri - curriculum vitae PDF"
    aria-describedby="document-help"></iframe>

  <p class="documents__help" id="document-help">If the preview does not appear, open the PDF directly:
    <a href="{{ '/files/cv.pdf' | relative_url }}" target="_blank" rel="noopener">CV</a>
    <span aria-hidden="true"> · </span>
    <a href="{{ '/files/resume.pdf' | relative_url }}" target="_blank" rel="noopener">Résumé</a>.
  </p>
  <p class="documents__sr-only" data-document-status aria-live="polite" aria-atomic="true"></p>
</section>
