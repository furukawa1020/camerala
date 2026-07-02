# Reference Audit for HIS Revision

This audit applies to `paper_his_revision.tex`, which uses an inline
`thebibliography` list. The legacy `references.bib` file is not the source of
truth for this revision.

## Rule

Use only open-access and reliable references. Do not cite commercial pages,
marketing pages, informal web pages, or unverified public demos as
bibliographic evidence. Do not use arXiv preprints as references for this
revision. If a source is available only as an arXiv preprint or public demo, do
not cite it as bibliographic evidence.

## References Used in `paper_his_revision.tex`

| Key | OA source | Use in manuscript | Reliability note |
| --- | --- | --- | --- |
| `verkruysse2008` | Optics Express, DOI: `10.1364/OE.16.021434` | Classic ambient-light rPPG background | Peer-reviewed open-access journal |
| `poh_ica` | Optics Express, DOI: `10.1364/OE.18.010762` | Classic blind-source video rPPG background | Peer-reviewed open-access journal |
| `deepphys` | CVF Open Access: `https://openaccess.thecvf.com/content_ECCV_2018/html/Weixuan_Chen_DeepPhys_Video-Based_Physiological_ECCV_2018_paper.html` | Recent deep-learning rPPG estimator and sensitivity context | ECCV 2018 paper; CVF page states this open version is identical to the published LNCS version |

## Explicitly Not Used as Bibliographic Evidence

- LabVanced and FacePhys-Demo: mentioned only in the response letter as
  reviewer-mentioned public tools/demos, not cited as scholarly evidence.
- Ayesha et al., RhythmEdge, Gupta and Etemad, and MediaPipe arXiv papers:
  removed because arXiv references are not allowed for this revision.
- `di_lernia_rppg_wild`: removed from the revised manuscript because an
  open-access primary source was not confirmed during this pass.
- Legacy non-OA or paywalled references in `references.bib`: not used for
  `paper_his_revision.tex`.
