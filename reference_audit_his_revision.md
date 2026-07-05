# Reference Audit for HIS Revision

This audit applies to `paper_his_revision.tex`, which uses an inline
`thebibliography` list. The legacy `references.bib` file is not the source of
truth for this revision.

## Current Rule

Use peer-reviewed open-access sources for the manuscript's scholarly related
work whenever possible. Do not cite arXiv when a peer-reviewed conference or
journal version exists. Use arXiv only when no peer-reviewed version is
available and the citation is needed as a technical software/framework
reference. The only current arXiv citation is MediaPipe, which is used as a
technical implementation reference for a tool used by Camerala, not as
peer-reviewed empirical evidence.

Reviewer 1 explicitly identified several related studies and systems. All
reviewer-specified items are retained in the manuscript body and reference list:
Gupta and Etemad, Ayesha et al., LabVanced rPPG, FacePhys-Demo, RhythmEdge, and
Di Lernia et al. LabVanced and FacePhys-Demo are treated only as public
tools/demonstrations, not as peer-reviewed empirical studies or validation
evidence. Additional peer-reviewed open-access sources provide supporting
context but do not replace the reviewer-specified items.

## References Used in `paper_his_revision.tex`

| Key | Source type | Use in manuscript | Note |
| --- | --- | --- | --- |
| `verkruysse2008` | Peer-reviewed OA journal article | Classic ambient-light rPPG background | Optics Express, DOI: `10.1364/OE.16.021434` |
| `poh_ica` | Peer-reviewed OA journal article | Classic blind-source video rPPG background | Optics Express, DOI: `10.1364/OE.18.010762` |
| `deepphys` | Open-access conference repository | Deep-learning rPPG estimator and degradation context | ECCV 2018, CVF Open Access |
| `ayesha_web_vital` | Peer-reviewed conference/book chapter | Web application for remote measurement of vital signs | Reviewer-specified scholarly related work, DOI: `10.1007/978-3-031-21047-1_21` |
| `labvanced_rppg` | Public tool/system page | Online experiment platform with remote heart-rate detection/rPPG functionality | Reviewer-specified public tool/demonstration; not empirical validation evidence |
| `facephys_demo` | Public web demo/repository | Browser-based rPPG monitoring with local inference | Reviewer-specified public tool/demonstration; not empirical validation evidence |
| `rhythmedge` | Peer-reviewed conference demo paper | Contactless heart-rate estimation on edge devices | Reviewer-specified scholarly related work |
| `gupta_privacy` | Peer-reviewed conference paper | Privacy-preserving remote heart-rate estimation from facial videos | Reviewer-specified scholarly related work, DOI: `10.1109/SMC53992.2023.10394350` |
| `kooij_naber_open_rppg` | Peer-reviewed OA journal article | Open-source remote heart-rate imaging | Behavior Research Methods, DOI: `10.3758/s13428-019-01256-8` |
| `efficientphys` | Peer-reviewed open-access conference repository | Efficient camera-based cardiac measurement | WACV 2023, CVF Open Access |
| `mobilephys` | Peer-reviewed journal/proceedings article | Mobile camera-based contactless physiological sensing | IMWUT 2022, DOI: `10.1145/3517225` |
| `di_lernia_rppg_wild` | Peer-reviewed OA journal article | Online webcam/in-the-wild rPPG degradation context | Behavior Research Methods, DOI: `10.3758/s13428-024-02398-0` |
| `rppg_toolbox` | Peer-reviewed open-access proceedings article | rPPG implementation and benchmarking toolbox | NeurIPS 2023 Datasets and Benchmarks Track |
| `bhutani_privacy_rppg` | Peer-reviewed OA journal article | Privacy-related remote physiological signal removal | Communications Engineering, DOI: `10.1038/s44172-025-00363-z` |
| `jspsych_joss` | Peer-reviewed OA software article | Browser-based task execution background | Journal of Open Source Software, DOI: `10.21105/joss.05351` |
| `psychopy2` | Peer-reviewed OA journal article | PsychoPy/PsychoJS/Pavlovia experiment-runtime background | Behavior Research Methods, DOI: `10.3758/s13428-018-01193-y` |
| `mediapipe_framework` | Open-access technical preprint | MediaPipe implementation-framework citation | Technical reference only; not empirical evidence |

## Explicit Limits

- When a peer-reviewed version exists, the manuscript cites that version rather
  than an arXiv preprint.
- The only arXiv entry is MediaPipe, used only as a technical implementation
  reference.
- The reviewer-specified items remain in the manuscript and reference list.
- LabVanced and FacePhys-Demo are cited only as public tools/demonstrations,
  not as peer-reviewed studies or empirical validation evidence.
- AI tools are not cited as references.
- Camerala does not claim novelty in browser rPPG, local rPPG processing,
  open-source rPPG implementations, edge/mobile camera-based physiological
  sensing, or privacy-oriented processing alone.
