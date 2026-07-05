# Reference Audit for HIS Revision

This audit applies to `paper_his_revision.tex`, which uses an inline
`thebibliography` list. The legacy `references.bib` file is not the source of
truth for this revision.

## Current Rule

Do not cite arXiv when a peer-reviewed conference or journal version exists.
Use the peer-reviewed versions for DeepPhys, Ayesha et al., Gupta and Etemad,
RhythmEdge, Di Lernia et al., Verkruysse et al., and Poh et al. Use arXiv only
when no peer-reviewed version is available and the citation is needed as a
technical software/framework reference. The only current arXiv citation is
MediaPipe, which is used as a technical implementation reference for a tool used
by Camerala, not as peer-reviewed empirical evidence. Public product pages and
GitHub repositories are used only as related-system/public-tool evidence, not
as empirical validation.

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
| `labvanced_rppg` | Official public system page | Browser/web-deployable rPPG functionality | Public-tool evidence only; not a peer-reviewed study |
| `facephys_demo` | Public GitHub repository | Browser-based rPPG demo | Public-demo evidence only; not a peer-reviewed study |
| `jspsych` | Peer-reviewed journal article | Browser-based task execution background | Behavior Research Methods, DOI: `10.3758/s13428-014-0458-y` |
| `psychopy2` | Peer-reviewed journal article | PsychoPy/PsychoJS/Pavlovia experiment-runtime background | Behavior Research Methods, DOI: `10.3758/s13428-018-01193-y` |
| `mediapipe_framework` | Open-access technical preprint | MediaPipe implementation-framework citation | Technical reference only; not empirical evidence |

## Explicit Limits

- When a peer-reviewed version exists, the manuscript cites that version rather
  than an arXiv preprint.
- The only arXiv entry is MediaPipe, used only as a technical implementation
  reference.
- Labvanced and FacePhys-Demo are not used as empirical validation sources.
- AI tools are not cited as references.
- Camerala does not claim novelty in browser rPPG, local rPPG processing, edge
  rPPG, or privacy-oriented heart-rate estimation alone.
