# S-28-4-002 A1 minor-revision fact audit

Audit date: 2026-08-14

This document records the pre-edit factual audit requested for the A1
administrative inquiry. No conclusion marked `UNRESOLVED` may be inserted into
the manuscript by inference.

## 1. A1-submitted baseline

The A1-submitted July revision was identified by its title:

`Camerala: An Edge-Side, Browser-Native Framework for Remote Psychophysiological Experiments with rPPG Sensing`

Protected copies were made before any A1 manuscript editing:

| Artifact | Protected copy | SHA-256 |
|---|---|---|
| Manuscript TeX | `paper_his_a1_submitted.tex` | `20FEF90AD65609ABE4308E28B1BAC4B1EB894FCBDC20E3CB36C795658D77D115` |
| Manuscript PDF | `paper_his_a1_submitted.pdf` | `A1D210FFE3F7FC2FB53C69AE0A44632637F9906C9A3E815B2FC0C2CF18A10ADB` |
| Response TeX | `response_to_reviewers_a1_submitted.tex` | `1715FEB636885D591BC3B4FC0F41F80E2CF18757C6A6BDF947B036FFBBA2785D` |
| Response PDF | `response_to_reviewers_a1_submitted.pdf` | `326C882319D85EF722B1E5365B11D8EC127CD39289EFACAD0CDCF869B10242AA` |

These hashes match the corresponding files in
`提出用LaTeXソース一式20260716`. The protected copies must not be edited. The
A1 difference manuscript must use `paper_his_a1_submitted.tex` as its baseline,
not the April original submission.

## 2.1 Session and trial structure

Status: **VERIFIED BY CODE/LOG STRUCTURE AND AUTHOR CONFIRMATION**

### Verified structure

- Blocks per session: 6
- Trials per block: 10
- Trial rows per exported session folder: 60
- Rows across the ten folders named `data1` through `data10`: 600

Evidence:

- `src/logic/SessionManager.js:13-14` sets `numBlocks: 6` and
  `trialsPerBlock: 10`.
- `src/logic/SessionManager.js:42-59` iterates through all generated blocks and
  runs ten trials in each block.
- The collection-time version in Git commit
  `2128eb604c4538da389f1100c1e8f28c7d4829d9` (2026-02-03) has the same 6 x 10
  configuration.
- Every `src/assets/data1`--`data10/trials.csv` contains 60 rows with block IDs
  0--5 and exactly 10 rows per block.
- Every corresponding `blocks.csv` contains 12 rows: START and END records for
  each of six blocks.
- Every corresponding `metadata.json` contains a six-entry `blockPlan`.

Therefore, the supported per-session procedure is **6 blocks x 10 trials = 60
trials**, not 3 blocks x 20 trials.

### Repository duplicate and author confirmation

`src/assets/data2` and `src/assets/data3` are byte-for-byte duplicates in the
current repository and therefore are not two independently archived session
exports:

- Both have session ID `45f6e5c7-6868-44dd-b300-fe5f48daa7c8`.
- Both have start time `2026-02-03T03:02:53.409Z`.
- `metadata.json`, `trials.csv`, `blocks.csv`, `subjective.csv`,
  `features_raw.csv`, and `windows.csv` have identical SHA-256 hashes across the
  two directories.
- Git commit `4ec51a4c44d102d88c7abd6cd8b64837c654eaa0` added both copies in this state.

Repository-audit consequences:

- The repository currently contains 600 trial rows but only 540 distinct trial
  rows across nine distinct session IDs.
- The reported `541/600` RT-range count is reproduced only when the duplicated
  session is counted twice.
- Excluding the duplicate `data3` leaves 490/540 trials in the 100--1500 ms
  range; this is an audit diagnostic, not a replacement manuscript result.
- The current repository copy alone cannot independently reproduce the original
  ten-session aggregate because one archived folder is a duplicate.

On 2026-08-14, the author explicitly confirmed all of the following:

- Ten independent sessions were actually conducted.
- The deployment therefore comprised 600 completed trials.
- `data3` is an erroneous repository copy of `data2`, not evidence that only
  nine sessions were conducted.
- The submitted `541/600` value was calculated from the original ten-session
  dataset, not from the duplicated repository copy currently present here.

Accordingly, **10 sessions, 600 completed trials, and 541/600 may remain as
author-confirmed experimental facts**. The current `data1`--`data10` repository
copy must not be represented as a complete independently reproducible archive
of the ten original sessions, and its duplicated folder must not be used to
replace or recalculate the submitted aggregate.

## 2.2 Display conditions

Status: **RESOLVED BY AUTHOR CONFIRMATION**

Conflicting manuscript/history statements are present:

- April submission: a standard 13.5-inch display at approximately 60 Hz
  (`paper_his_original_submitted.tex:284`).
- A1-submitted revision: mouse Computer G-Tune P517G60ZO21CNHWT, built-in
  15.6-inch 2560 x 1440 display, 165 Hz
  (`paper_his_a1_submitted.tex:335-341`).

`AUTHOR_FACTS_NEEDED.md:8-16` and a prior author handoff describe the latter as
author-confirmed. The repository contains no deployment-time purchase record,
hardware screenshot, OS display record, or metadata field that independently
identifies the machine or refresh rate, so explicit reconfirmation was sought.

On 2026-08-14, the author confirmed that the reported deployment used:

- PC: mouse Computer G-Tune P517G60ZO21CNHWT
- Display: built-in 15.6-inch display
- Resolution: 2560 x 1440 pixels
- Nominal refresh rate: 165 Hz

The old 13.5-inch / approximately 60 Hz description is incorrect and must not
remain in the final manuscript.

## 2.3 External illuminance meter

Status: **RESOLVED FROM AVAILABLE EVIDENCE: NO EXTERNAL MEASUREMENT**

The April submission states that a digital lux meter was used
(`paper_his_original_submitted.tex:285-288`), but no supporting equipment list,
photo, meter export, measurement log, code path, or contemporaneous record was
found. The current A1 revision and author-fact memo instead state that external
light-meter values were not used.

Following the A1 instruction for absence of supporting evidence, the manuscript
must state:

`No external illuminance measurement was performed.`

Camera-image-derived values must not be called lux or ambient illuminance.

## 2.4 Camera-derived brightness ranges 105--114 / 102--111

Status: **NOT REPRODUCIBLE; DELETE THE RANGES**

What the implementation actually computes:

- `src/logic/FeatureExtractor.js:81-96` downsamples the whole video frame to
  64 x 48 pixels and computes the mean green-channel value as `frameAvg`.
- `src/logic/FeatureExtractor.js:98-119` computes `roiLimit` as the green-channel
  mean over a 3 x 3 forehead landmark region.
- `src/logic/FeatureExtractor.js:40-55` exports `roiLimit` as `roival` and
  exports only the absolute frame-to-frame change in `frameAvg` as
  `exposure_fluc`.
- `src/logic/DataLogger.js:75` aggregates `roival`, `motion`, `ear`, `quality`,
  and `exposure_fluc`; it does not persist or aggregate raw `frameAvg`.

No saved CSV column, source image set, setup/check log, or aggregation procedure
reproduces laboratory 105--114 and home 102--111. The image region, aggregation
level, and provenance of those ranges therefore cannot be established. They
must be removed rather than redefined by guesswork.

## 2.5 `mean_quality`

Status: **IMPLEMENTATION UNDERSTOOD; NUMERIC RESULT MUST BE REMOVED**

Implementation facts:

- `src/logic/FeatureExtractor.js:13-14` can return `quality: 0` when no landmarks
  are present, and `src/logic/FeatureExtractor.js:55` returns `quality: 1` when
  landmarks are present.
- In the actual callback path, `src/logic/CameraManager.js:66-69` invokes the
  downstream callback only when landmarks are present. Therefore no-landmark
  camera results are not passed to the normal frame logger.
- All 68,845 saved `features_raw.csv` rows have `quality = 1`, and all 299 saved
  `windows.csv` rows have `mean_quality = 1`.

Numeric or evaluative uses in the A1-submitted manuscript/response:

- `paper_his_a1_submitted.tex:421`: definition of `mean_quality`
- `paper_his_a1_submitted.tex:435`: all 299 windows had `mean_quality = 1.0`
- `paper_his_a1_submitted.tex:496`: landmark availability listed among relevant
  indicators
- `response_to_reviewers_a1_submitted.tex:265`: says it is not primary evidence
- `response_to_reviewers_a1_submitted.tex:270-271`: describes the value and its
  logging-path limitation

The numeric `299` / `1.0` result and any success/quality interpretation must be
removed. At most one concise structural limitation may remain:

`The normal export path stored frame records only when FaceMesh landmarks were returned; therefore, the saved records cannot be used to estimate an overall landmark-detection success rate across all camera frames.`

## 2.6 Publication-information commands

Status: **COMMANDS IDENTIFIED**

`ehis.cls` defines the following formal commands:

- `\YEAR{...}` at `ehis.cls:914`
- `\VOL{...}` at `ehis.cls:964`
- `\NO{...}` at `ehis.cls:970`
- `\received{year}{month}{day}` at `ehis.cls:1442`
- `\revised{year}{month}{day}` at `ehis.cls:1444`

The corresponding values requested for the final manuscript are:

```tex
\YEAR{2026}
\VOL{28}
\NO{4}
\received{2026}{April}{26}
\revised{2026}{July}{17}
```

The current A1 manuscript leaves `\YEAR{}`, `\VOL{}`, and `\NO{}` empty and does
not call `\received` or `\revised`. No acceptance date will be invented.

The class prints the received/revised string through `\@uketsuke` in its
biography machinery (`ehis.cls:1374,1439-1449`). Placement and rendering must be
verified by compiling the final publication-layout source after the factual
blockers are resolved.

## 2.7 Author portrait

Status: **RESOLVED; AUTHOR FILE SUPPLIED**

On 2026-08-14, the author supplied `古川耕太郎顔写真.jpg`. The file was opened
and visually checked as a portrait of the author. It is a 731x981, 24-bit JPEG
with SHA-256
`A8EFB90887F0B8E6B6B14753D68AB6CF9F7292041A52A9AAE0C6D120EEFB4A6B`.
The original file was not altered.

`paper_figures/author.png` is not an author photograph. Visual inspection shows
that it is an obsolete Camerala flowchart containing old labels, including an
exposure-fluctuation threshold and window rejection. It must not be reused as a
portrait. No image was embedded in `Kotaro furukawa.docx`.

The portrait was copied to the explicit submission name
`S-28-4-002_古川耕太郎_顔写真.jpg` and included both as a standalone deliverable
and in `S-28-4-002_LaTeXソース一式.zip`. The copies have the same SHA-256 as the
author-supplied original. The class file draws a biography photo box but does
not provide an image-inclusion argument in `\profile`; separate image delivery
therefore follows the editorial-office request.

## 3. Same-browser-clock verification

Status: **VERIFIED WITH A SCOPE LIMITATION**

- Trial timestamps and RT calculations use `performance.now()` in
  `src/logic/TaskEngine.js:36,50,54`.
- Exported frame timestamps use `performance.now()` in
  `src/logic/DataLogger.js:31`.
- Block records use the same API in `src/logic/DataLogger.js:117,121,126`.
- These components run in the same client-side browser runtime.

It is therefore supportable to say that task-event and face-image-derived
records use the same browser clock domain. The logs do not support a claim that
every face frame was assigned to an independently stored physical
stimulus-onset-to-response interval, and physical display onset was not
externally verified.

## 4. Stop conditions and required author input

The experimental-fact blockers have now been resolved through code/log evidence
and explicit author confirmation. Manuscript editing may proceed using only the
facts recorded above.

No factual or external-file blocker remains. The author portrait has been
supplied and checked, and the manuscript, response, difference PDF, source ZIP,
and standalone portrait can be treated as a complete A1 submission set after
the final hash and archive checks recorded in the delivery report.
