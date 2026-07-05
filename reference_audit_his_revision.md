# Reference Audit for HIS Revision

This audit applies to `paper_his_revision.tex`, which uses an inline
`thebibliography` list. The legacy `references.bib` file is not the source of
truth for this revision.

## Current Rule

Do not use arXiv preprints as references for this revision. Reviewer-mentioned
systems should still be discussed when they are directly relevant to Reviewer
1's requested positioning. Public product pages and GitHub repositories are
used only as related-system evidence, not as empirical validation.

## References Used in `paper_his_revision.tex`

| Key | Source type | Use in manuscript | Note |
| --- | --- | --- | --- |
| `verkruysse2008` | Peer-reviewed OA journal article | Classic ambient-light rPPG background | Optics Express, DOI: `10.1364/OE.16.021434` |
| `poh_ica` | Peer-reviewed OA journal article | Classic blind-source video rPPG background | Optics Express, DOI: `10.1364/OE.18.010762` |
| `deepphys` | Open-access conference repository | Deep-learning rPPG estimator and degradation context | ECCV 2018, CVF Open Access |
| `ayesha_web_vital` | Conference/LNCS entry supplied for reviewer positioning | Web application for remote vital-sign measurement | Used to acknowledge existing web-rPPG systems |
| `gupta_privacy` | IEEE conference entry supplied for reviewer positioning | Privacy-oriented remote heart-rate estimation | Used to avoid claiming privacy-oriented processing as Camerala novelty |
| `rhythmedge` | IEEE conference demo entry supplied for reviewer positioning | Edge-based contactless heart-rate estimation | Used to acknowledge edge rPPG systems |
| `di_lernia_rppg_wild` | Behavior Research Methods entry supplied for reviewer positioning | Online webcam/in-the-wild rPPG degradation context | Used to acknowledge known uncontrolled-webcam issues |
| `labvanced_rppg` | Official public system page | Browser/web-deployable rPPG functionality | Related-system evidence only |
| `facephys_demo` | Public GitHub repository | Browser-based rPPG demo | Related-system evidence only |

## Explicit Limits

- No arXiv entries are used in the manuscript.
- Labvanced and FacePhys-Demo are not used as empirical validation sources.
- Camerala does not claim novelty in browser rPPG, local rPPG processing, edge
  rPPG, or privacy-oriented heart-rate estimation alone.
