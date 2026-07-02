# Reference Audit for HIS Revision

This audit applies to `paper_his_revision.tex`, which uses an inline
`thebibliography` list. The legacy `references.bib` file is not the source of
truth for this revision.

## Rule

Use only open-access and reliable references. Do not cite commercial pages,
marketing pages, informal web pages, or unverified public demos as
bibliographic evidence. ArXiv-only demo/preprint papers may be retained only as
narrow technical or system-context examples, not as support for central
empirical claims.

## References Used in `paper_his_revision.tex`

| Key | OA source | Use in manuscript | Reliability note |
| --- | --- | --- | --- |
| `verkruysse2008` | Optics Express, DOI: `10.1364/OE.16.021434` | Classic ambient-light rPPG background | Peer-reviewed open-access journal |
| `poh_ica` | Optics Express, DOI: `10.1364/OE.18.010762` | Classic blind-source video rPPG background | Peer-reviewed open-access journal |
| `deepphys` | arXiv: `https://arxiv.org/abs/1805.07888` | Recent deep-learning rPPG estimator and sensitivity context | Accepted at ECCV 2018, open arXiv version |
| `ayesha_web_vital` | arXiv: `https://arxiv.org/abs/2208.09916` | Web-rPPG system context and cautious mention of illumination/motion sensitivity | Open arXiv paper; use cautiously, not as a central validation source |
| `rhythmedge` | arXiv: `https://arxiv.org/abs/2208.06572` | Edge-rPPG system context | Open arXiv demo paper; use only as system-context evidence |
| `gupta_privacy` | arXiv: `https://arxiv.org/abs/2306.01141` | Privacy-oriented rPPG positioning | Accepted at IEEE SMC 2023, open arXiv version |
| `mediapipe_paper` | arXiv: `https://arxiv.org/abs/1906.08172` | MediaPipe/FaceMesh implementation basis | Official open technical paper |

## Explicitly Not Used as Bibliographic Evidence

- LabVanced and FacePhys-Demo: mentioned only in the response letter as
  reviewer-mentioned public tools/demos, not cited as scholarly evidence.
- `di_lernia_rppg_wild`: removed from the revised manuscript because an
  open-access primary source was not confirmed during this pass.
- Legacy non-OA or paywalled references in `references.bib`: not used for
  `paper_his_revision.tex`.
