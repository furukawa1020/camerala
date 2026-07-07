from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
ASSET_DIR = ROOT / "src" / "assets"
OUT_MD = ROOT / "analysis_recomputed_results.md"
OUT_CSV = ROOT / "analysis_recomputed_results.csv"

VALID_CONDITIONS = {"NEUTRAL", "THREAT", "CHALLENGE"}
RT_MIN_MS = 100.0
RT_MAX_MS = 1500.0


def context_for_session(session: int) -> str:
    return "Laboratory" if session <= 5 else "Home"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def csv_columns(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        return next(reader)


def to_float(value: str | int | float | None) -> float:
    if value is None or value == "":
        return math.nan
    return float(value)


def mean(values: Iterable[float]) -> float:
    vals = [v for v in values if not math.isnan(v)]
    if not vals:
        return math.nan
    return sum(vals) / len(vals)


def sample_sd(values: Iterable[float]) -> float:
    vals = [v for v in values if not math.isnan(v)]
    if len(vals) < 2:
        return math.nan
    m = mean(vals)
    return math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))


def fmt(value: float | int | str | None, digits: int = 3) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, int):
        return str(value)
    if math.isnan(value):
        return ""
    return f"{value:.{digits}f}"


def summarize_values(values: list[float]) -> tuple[int, float, float]:
    clean = [v for v in values if not math.isnan(v)]
    return len(clean), mean(clean), sample_sd(clean)


def add_result(
    rows: list[dict[str, str]],
    metric: str,
    source_csv: str,
    source_columns: str,
    filter_desc: str,
    context: str,
    condition: str,
    n: int | None = None,
    mean_value: float | None = None,
    sd_value: float | None = None,
    proportion: float | None = None,
    value: str | None = None,
    note: str = "",
) -> None:
    rows.append(
        {
            "metric": metric,
            "source_csv": source_csv,
            "source_columns": source_columns,
            "filter": filter_desc,
            "context": context,
            "condition": condition,
            "n": "" if n is None else str(n),
            "mean": "" if mean_value is None else fmt(mean_value, 4),
            "sd": "" if sd_value is None else fmt(sd_value, 4),
            "proportion": "" if proportion is None else fmt(proportion, 4),
            "value": "" if value is None else value,
            "note": note,
        }
    )


def load_all() -> tuple[list[dict], list[dict], list[dict], list[dict], list[dict], list[dict]]:
    trials: list[dict] = []
    windows: list[dict] = []
    features: list[dict] = []
    blocks: list[dict] = []
    subjective: list[dict] = []
    metadata: list[dict] = []

    for session in range(1, 11):
        session_dir = ASSET_DIR / f"data{session}"
        context = context_for_session(session)

        for row in read_csv(session_dir / "trials.csv"):
            row["session"] = session
            row["context"] = context
            row["rt_num"] = to_float(row.get("rt"))
            row["correct_bool"] = str(row.get("correct", "")).lower() == "true"
            trials.append(row)

        for row in read_csv(session_dir / "windows.csv"):
            row["session"] = session
            row["context"] = context
            row["mean_roival_num"] = to_float(row.get("mean_roival"))
            row["mean_motion_num"] = to_float(row.get("mean_motion"))
            row["mean_exposure_fluc_num"] = to_float(row.get("mean_exposure_fluc"))
            row["mean_quality_num"] = to_float(row.get("mean_quality"))
            row["frame_count_num"] = to_float(row.get("frame_count"))
            row["start_time_num"] = to_float(row.get("start_time"))
            row["end_time_num"] = to_float(row.get("end_time"))
            duration_s = (row["end_time_num"] - row["start_time_num"]) / 1000.0
            row["fps_proxy_num"] = row["frame_count_num"] / duration_s if duration_s > 0 else math.nan
            windows.append(row)

        for row in read_csv(session_dir / "features_raw.csv"):
            row["session"] = session
            row["context"] = context
            row["quality_num"] = to_float(row.get("quality"))
            row["exposure_fluc_num"] = to_float(row.get("exposure_fluc"))
            row["roival_num"] = to_float(row.get("roival"))
            row["motion_num"] = to_float(row.get("motion"))
            features.append(row)

        for row in read_csv(session_dir / "blocks.csv"):
            row["session"] = session
            row["context"] = context
            blocks.append(row)

        for row in read_csv(session_dir / "subjective.csv"):
            row["session"] = session
            row["context"] = context
            subjective.append(row)

        with (session_dir / "metadata.json").open("r", encoding="utf-8") as f:
            item = json.load(f)
            item["session"] = session
            item["context"] = context
            metadata.append(item)

    return trials, windows, features, blocks, subjective, metadata


def inventory() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for session in range(1, 11):
        session_dir = ASSET_DIR / f"data{session}"
        context = context_for_session(session)
        for name in ["trials.csv", "features_raw.csv", "windows.csv", "blocks.csv", "subjective.csv"]:
            path = session_dir / name
            data = read_csv(path)
            cols = csv_columns(path)
            condition_col = "condition" if "condition" in cols else ("c" if "c" in cols else "")
            block_col = "blockId" if "blockId" in cols else ("block_id" if "block_id" in cols else ("b" if "b" in cols else ""))
            trial_col = "id" if "id" in cols and name == "trials.csv" else ""
            timestamp_cols = [c for c in ["t", "time", "startTime", "start_time", "end_time"] if c in cols]
            rows.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "rows": str(len(data)),
                    "columns": ", ".join(cols),
                    "context_rule": f"data{session} -> {context}",
                    "condition_column": condition_col,
                    "block_id_column": block_col,
                    "trial_id_column": trial_col,
                    "timestamp_columns": ", ".join(timestamp_cols),
                }
            )
        meta_path = session_dir / "metadata.json"
        with meta_path.open("r", encoding="utf-8") as f:
            meta = json.load(f)
        rows.append(
            {
                "path": str(meta_path.relative_to(ROOT)),
                "rows": "1 JSON object",
                "columns": ", ".join(sorted(meta.keys())),
                "context_rule": f"data{session} -> {context}",
                "condition_column": "blockPlan",
                "block_id_column": "",
                "trial_id_column": "",
                "timestamp_columns": "startTime",
            }
        )
    return rows


def build_results() -> tuple[list[dict[str, str]], dict[str, object]]:
    trials, windows, features, blocks, subjective, metadata = load_all()
    result_rows: list[dict[str, str]] = []

    valid_trials = [r for r in trials if RT_MIN_MS <= r["rt_num"] <= RT_MAX_MS]

    for context in ["Laboratory", "Home", "Total"]:
        all_ctx = trials if context == "Total" else [r for r in trials if r["context"] == context]
        valid_ctx = valid_trials if context == "Total" else [r for r in valid_trials if r["context"] == context]
        retention = len(valid_ctx) / len(all_ctx) if all_ctx else math.nan
        add_result(
            result_rows,
            "Retained trials after RT exclusion",
            "trials.csv",
            "rt",
            "100 <= rt <= 1500 ms",
            context,
            "All",
            n=len(valid_ctx),
            proportion=retention,
            value=f"{len(valid_ctx)}/{len(all_ctx)} ({retention * 100:.1f}%)",
            note="RT-only retention; no Conf < 0.8 filtering was applied.",
        )

        rt_vals = [r["rt_num"] for r in valid_ctx]
        _, rt_m, rt_sd = summarize_values(rt_vals)
        add_result(
            result_rows,
            "Mean RT after RT exclusion",
            "trials.csv",
            "rt",
            "100 <= rt <= 1500 ms",
            context,
            "All",
            n=len(rt_vals),
            mean_value=rt_m,
            sd_value=rt_sd,
            note="Milliseconds.",
        )

        if valid_ctx:
            accuracy = sum(1 for r in valid_ctx if r["correct_bool"]) / len(valid_ctx)
        else:
            accuracy = math.nan
        add_result(
            result_rows,
            "Accuracy after RT exclusion",
            "trials.csv",
            "correct, rt",
            "100 <= rt <= 1500 ms",
            context,
            "All",
            n=len(valid_ctx),
            proportion=accuracy,
            value=f"{accuracy * 100:.1f}%" if not math.isnan(accuracy) else "",
        )

    for context in ["Laboratory", "Home", "Total"]:
        for condition in sorted(VALID_CONDITIONS):
            all_ctx = [
                r
                for r in trials
                if (context == "Total" or r["context"] == context) and r["condition"] == condition
            ]
            valid_ctx = [
                r
                for r in valid_trials
                if (context == "Total" or r["context"] == context) and r["condition"] == condition
            ]
            if not all_ctx:
                continue
            retention = len(valid_ctx) / len(all_ctx)
            add_result(
                result_rows,
                "Condition-level RT retention",
                "trials.csv",
                "condition, rt",
                "100 <= rt <= 1500 ms",
                context,
                condition,
                n=len(valid_ctx),
                proportion=retention,
                value=f"{len(valid_ctx)}/{len(all_ctx)} ({retention * 100:.1f}%)",
            )

    metric_map = [
        ("rPPG-oriented ROI green-channel value", "mean_roival_num", "mean_roival", "windows.csv"),
        ("Motion estimate", "mean_motion_num", "mean_motion", "windows.csv"),
        (
            "Frame-to-frame green-channel brightness-change indicator",
            "mean_exposure_fluc_num",
            "mean_exposure_fluc",
            "windows.csv",
        ),
        ("Window FPS proxy", "fps_proxy_num", "frame_count, start_time, end_time", "windows.csv"),
    ]
    valid_windows = [r for r in windows if r.get("condition") in VALID_CONDITIONS]
    for label, key, cols, source in metric_map:
        for context in ["Laboratory", "Home", "Total"]:
            ctx_rows = valid_windows if context == "Total" else [r for r in valid_windows if r["context"] == context]
            vals = [r[key] for r in ctx_rows]
            n, m, sd = summarize_values(vals)
            add_result(
                result_rows,
                label,
                source,
                cols,
                "condition in NEUTRAL/THREAT/CHALLENGE",
                context,
                "All",
                n=n,
                mean_value=m,
                sd_value=sd,
                note="Use only if manuscript states this metric is computed from window logs.",
            )

    feature_quality_counts = Counter(str(r.get("quality", "")) for r in features)
    window_quality_counts = Counter(str(r.get("mean_quality", "")) for r in windows)
    add_result(
        result_rows,
        "features_raw quality unique values",
        "features_raw.csv",
        "quality",
        "all saved frame records",
        "Total",
        "All",
        n=len(features),
        value="; ".join(f"{k}: {v}" for k, v in sorted(feature_quality_counts.items())),
        note="All saved frame records have quality=1; this is not continuous tracking confidence.",
    )
    add_result(
        result_rows,
        "windows mean_quality unique values",
        "windows.csv",
        "mean_quality",
        "all saved window records",
        "Total",
        "All",
        n=len(windows),
        value="; ".join(f"{k}: {v}" for k, v in sorted(window_quality_counts.items())),
        note="All saved windows have mean_quality=1; do not report as tracking availability.",
    )

    extras: dict[str, object] = {
        "trials": trials,
        "valid_trials": valid_trials,
        "windows": windows,
        "valid_windows": valid_windows,
        "features": features,
        "blocks": blocks,
        "subjective": subjective,
        "metadata": metadata,
        "feature_quality_counts": feature_quality_counts,
        "window_quality_counts": window_quality_counts,
    }
    return result_rows, extras


def result_lookup(rows: list[dict[str, str]], metric: str, context: str) -> dict[str, str]:
    for row in rows:
        if row["metric"] == metric and row["context"] == context and row["condition"] == "All":
            return row
    raise KeyError((metric, context))


def make_markdown(rows: list[dict[str, str]], inv: list[dict[str, str]], extras: dict[str, object]) -> str:
    current_table_comparison = [
        (
            "582/600 retained trials",
            "541/600 (90.2%) with RT 100--1500 ms only",
            "Not reproducible",
            "No continuous confidence column or Conf < 0.8 filtering code was found.",
        ),
        (
            "Laboratory 292 / Home 290",
            "Laboratory 256 / Home 285 with RT 100--1500 ms only",
            "Not reproducible",
            "Current retained-trial counts differ from the manuscript values.",
        ),
        (
            "Measured processing FPS 59.8 / 58.2",
            "Window FPS proxy: Laboratory 41.43 +/- 3.87, Home 47.14 +/- 7.68",
            "Not reproducible as written",
            "No direct measured processing FPS log column was found.",
        ),
        (
            "Face size",
            "No face-size/IOD column found",
            "Delete",
            "Cannot reproduce from current exported CSV files.",
        ),
        (
            "Camera-derived brightness range 105--114 / 102--111",
            "Not present as a current CSV column",
            "Separate author-confirmed information",
            "Keep only in environment/setup table if retained.",
        ),
        (
            "Exposure fluctuation 0.03 / 0.09",
            "mean_exposure_fluc: Laboratory 0.0504 +/- 0.0509, Home 0.0707 +/- 0.0337",
            "Rename and update if used",
            "Use frame-to-frame green-channel brightness-change indicator.",
        ),
        (
            "Face-tracking availability 99.1% / 96.5%",
            "quality=1 for all saved frames; mean_quality=1 for all windows",
            "Delete",
            "Saved logs do not contain failed-detection frames or continuous confidence.",
        ),
    ]

    new_table_rows = [
        (
            "Retained trials after RT exclusion",
            result_lookup(rows, "Retained trials after RT exclusion", "Laboratory")["value"],
            result_lookup(rows, "Retained trials after RT exclusion", "Home")["value"],
            "Recomputed from trials.csv using 100 <= rt <= 1500 ms.",
        ),
        (
            "Mean RT after RT exclusion",
            f"{float(result_lookup(rows, 'Mean RT after RT exclusion', 'Laboratory')['mean']):.1f} +/- {float(result_lookup(rows, 'Mean RT after RT exclusion', 'Laboratory')['sd']):.1f} ms",
            f"{float(result_lookup(rows, 'Mean RT after RT exclusion', 'Home')['mean']):.1f} +/- {float(result_lookup(rows, 'Mean RT after RT exclusion', 'Home')['sd']):.1f} ms",
            "RT-only trial filter.",
        ),
        (
            "Accuracy after RT exclusion",
            result_lookup(rows, "Accuracy after RT exclusion", "Laboratory")["value"],
            result_lookup(rows, "Accuracy after RT exclusion", "Home")["value"],
            "Correct responses among retained trials.",
        ),
        (
            "rPPG-oriented ROI green-channel value",
            f"{float(result_lookup(rows, 'rPPG-oriented ROI green-channel value', 'Laboratory')['mean']):.2f} +/- {float(result_lookup(rows, 'rPPG-oriented ROI green-channel value', 'Laboratory')['sd']):.2f}",
            f"{float(result_lookup(rows, 'rPPG-oriented ROI green-channel value', 'Home')['mean']):.2f} +/- {float(result_lookup(rows, 'rPPG-oriented ROI green-channel value', 'Home')['sd']):.2f}",
            "Recomputed from windows.csv mean_roival.",
        ),
        (
            "Motion estimate",
            f"{float(result_lookup(rows, 'Motion estimate', 'Laboratory')['mean']):.4f} +/- {float(result_lookup(rows, 'Motion estimate', 'Laboratory')['sd']):.4f}",
            f"{float(result_lookup(rows, 'Motion estimate', 'Home')['mean']):.4f} +/- {float(result_lookup(rows, 'Motion estimate', 'Home')['sd']):.4f}",
            "Recomputed from windows.csv mean_motion.",
        ),
        (
            "Frame-to-frame green-channel brightness-change indicator",
            f"{float(result_lookup(rows, 'Frame-to-frame green-channel brightness-change indicator', 'Laboratory')['mean']):.4f} +/- {float(result_lookup(rows, 'Frame-to-frame green-channel brightness-change indicator', 'Laboratory')['sd']):.4f}",
            f"{float(result_lookup(rows, 'Frame-to-frame green-channel brightness-change indicator', 'Home')['mean']):.4f} +/- {float(result_lookup(rows, 'Frame-to-frame green-channel brightness-change indicator', 'Home')['sd']):.4f}",
            "Replaces exposure fluctuation terminology.",
        ),
    ]

    lines: list[str] = []
    lines.append("# Recomputed Analysis Results")
    lines.append("")
    lines.append("Generated by `analysis_recompute_tables.py`.")
    lines.append("")
    lines.append("Important exclusions from the manuscript interpretation:")
    lines.append("- No continuous `conf` or `confidence` column was found in the current exported logs.")
    lines.append("- No `Conf < 0.8` filtering is applied in this recomputation.")
    lines.append("- `quality` is not treated as continuous tracking confidence.")
    lines.append("- `exposure fluctuation` should be renamed if retained.")
    lines.append("")
    lines.append("## 1. CSV / JSON Inventory")
    lines.append("")
    lines.append("| Path | Rows | Context rule | Condition column | Block ID | Trial ID | Timestamp columns | Columns |")
    lines.append("|---|---:|---|---|---|---|---|---|")
    for item in inv:
        lines.append(
            f"| `{item['path']}` | {item['rows']} | {item['context_rule']} | "
            f"{item['condition_column']} | {item['block_id_column']} | {item['trial_id_column']} | "
            f"{item['timestamp_columns']} | {item['columns']} |"
        )
    lines.append("")
    lines.append("## 2. Recomputed Metrics")
    lines.append("")
    lines.append("| Metric | Context | Condition | N | Mean | SD | Proportion | Value | Notes |")
    lines.append("|---|---|---|---:|---:|---:|---:|---|---|")
    for row in rows:
        lines.append(
            f"| {row['metric']} | {row['context']} | {row['condition']} | {row['n']} | "
            f"{row['mean']} | {row['sd']} | {row['proportion']} | {row['value']} | {row['note']} |"
        )
    lines.append("")
    lines.append("## 3. Current Table 4 Comparison")
    lines.append("")
    lines.append("| Current manuscript value | Recomputed / checked value | Decision | Reason |")
    lines.append("|---|---|---|---|")
    for item, recomputed, decision, reason in current_table_comparison:
        lines.append(f"| {item} | {recomputed} | {decision} | {reason} |")
    lines.append("")
    lines.append("## 4. Proposed New Table 4")
    lines.append("")
    lines.append("| Metric | Laboratory | Home | Notes |")
    lines.append("|---|---:|---:|---|")
    for metric, lab, home, notes in new_table_rows:
        lines.append(f"| {metric} | {lab} | {home} | {notes} |")
    lines.append("")
    lines.append("## 5. Environment Table Handling")
    lines.append("")
    lines.append(
        "`Camera-derived brightness range 105--114 / 102--111` is not reproduced from the "
        "current CSV columns. If retained, it should remain in the environment/setup table as "
        "author-confirmed setup/check information, not in the results table as a recomputed log statistic."
    )
    lines.append("")
    lines.append("## 6. Values Suitable for Manuscript Use")
    lines.append("")
    lines.append("- RT-only retained trials: 541/600 (90.2%), with Laboratory 256/300 and Home 285/300.")
    lines.append("- Mean RT and accuracy after the RT filter.")
    lines.append("- Window-level mean_roival, mean_motion, and mean_exposure_fluc after renaming.")
    lines.append("")
    lines.append("## 7. Values to Remove from Results Table")
    lines.append("")
    lines.append("- 582/600 and 97.0% retention.")
    lines.append("- Laboratory 292 / Home 290 retained trials.")
    lines.append("- 99.1% / 96.5% face-tracking availability.")
    lines.append("- `Conf < 0.8` filtering.")
    lines.append("- Face size, because no face-size/IOD column exists in the current CSV logs.")
    lines.append("- Measured processing FPS, unless a separate reproducible FPS log source is identified.")
    lines.append("")
    lines.append("## 8. Method / Limitation Notes")
    lines.append("")
    lines.append(
        "The current logs save landmark-available frame records, but they do not store continuous "
        "face-detection or tracking-confidence values for all frames. Failed landmark detections "
        "are not recoverable as explicit frame records from the current logs. Future versions should "
        "log continuous confidence values for all frames, including failed detections, so that a "
        "pre-specified operational threshold can be applied."
    )
    lines.append("")
    return "\n".join(lines) + "\n"


def write_csv(rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "metric",
        "source_csv",
        "source_columns",
        "filter",
        "context",
        "condition",
        "n",
        "mean",
        "sd",
        "proportion",
        "value",
        "note",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    inv = inventory()
    rows, extras = build_results()
    write_csv(rows)
    OUT_MD.write_text(make_markdown(rows, inv, extras), encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print(f"Wrote {OUT_CSV}")


if __name__ == "__main__":
    main()
