from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parent
ASSET_DIR = ROOT / "src" / "assets"
OUT_DIR = ROOT / "paper_figures"

CONDITION_LABELS = {
    "NEUTRAL": "neutral instruction",
    "THREAT": "negative instruction",
    "CHALLENGE": "positive instruction",
}

CONTEXT_LABELS = {
    "University": "laboratory",
    "Home": "home",
}

PALETTE = {
    "neutral instruction": "#6b7280",
    "negative instruction": "#b91c1c",
    "positive instruction": "#1d4ed8",
}


def load_data():
    all_windows = []
    all_trials = []

    for session in range(1, 11):
        context = "University" if session <= 5 else "Home"
        session_dir = ASSET_DIR / f"data{session}"

        windows_path = session_dir / "windows.csv"
        if windows_path.exists():
            windows = pd.read_csv(windows_path)
            windows["context"] = context
            windows["session"] = session
            all_windows.append(windows)

        trials_path = session_dir / "trials.csv"
        if trials_path.exists():
            trials = pd.read_csv(trials_path)
            trials["context"] = context
            trials["session"] = session
            all_trials.append(trials)

    if not all_windows or not all_trials:
        raise RuntimeError("Expected window and trial CSV files under src/assets/data1..data10.")

    windows = pd.concat(all_windows, ignore_index=True)
    trials = pd.concat(all_trials, ignore_index=True)

    for column in ["mean_motion", "mean_exposure_fluc"]:
        windows[column] = pd.to_numeric(windows[column], errors="coerce")
    trials["rt"] = pd.to_numeric(trials["rt"], errors="coerce")

    valid_conditions = set(CONDITION_LABELS)
    windows = windows[windows["condition"].isin(valid_conditions)].copy()
    trials = trials[trials["condition"].isin(valid_conditions)].copy()

    windows["instruction"] = windows["condition"].map(CONDITION_LABELS)
    trials["instruction"] = trials["condition"].map(CONDITION_LABELS)
    windows["deployment context"] = windows["context"].map(CONTEXT_LABELS)
    trials["deployment context"] = trials["context"].map(CONTEXT_LABELS)

    windows = windows.sort_values(["session", "start_time"]).reset_index(drop=True)
    windows["window index"] = range(len(windows))

    return windows, trials


def generate_figures():
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.15)
    OUT_DIR.mkdir(exist_ok=True)

    windows, trials = load_data()
    instruction_order = [
        "neutral instruction",
        "negative instruction",
        "positive instruction",
    ]
    context_order = ["laboratory", "home"]

    # Figure 2: measurement-quality indicator
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    sns.boxplot(
        data=windows,
        x="deployment context",
        y="mean_exposure_fluc",
        order=context_order,
        color="#cbd5e1",
        ax=ax,
    )
    sns.stripplot(
        data=windows,
        x="deployment context",
        y="mean_exposure_fluc",
        order=context_order,
        color="#334155",
        alpha=0.35,
        size=2.5,
        ax=ax,
    )
    ax.set_title("Exposure fluctuation by deployment context")
    ax.set_xlabel("")
    ax.set_ylabel("Exposure fluctuation")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "Figure2_Quality.png", dpi=300)
    plt.close(fig)

    # Figure 3: task-event and sensor-derived summaries
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.2))
    sns.barplot(
        data=windows,
        x="deployment context",
        y="mean_motion",
        hue="instruction",
        order=context_order,
        hue_order=instruction_order,
        palette=PALETTE,
        errorbar="se",
        capsize=0.08,
        ax=axes[0],
    )
    axes[0].set_title("A. Head-motion estimates")
    axes[0].set_xlabel("")
    axes[0].set_ylabel("Head-motion estimate")
    axes[0].legend(title="Instruction", frameon=True)

    sns.barplot(
        data=trials,
        x="deployment context",
        y="rt",
        hue="instruction",
        order=context_order,
        hue_order=instruction_order,
        palette=PALETTE,
        errorbar="se",
        capsize=0.08,
        ax=axes[1],
    )
    axes[1].set_title("B. Reaction time")
    axes[1].set_xlabel("")
    axes[1].set_ylabel("Reaction time (ms)")
    axes[1].get_legend().remove()

    fig.tight_layout()
    fig.savefig(OUT_DIR / "Figure3_Interaction.png", dpi=300)
    plt.close(fig)

    # Figure 4: longitudinal descriptive view
    fig, ax = plt.subplots(figsize=(13.5, 5.2))
    sns.lineplot(
        data=windows,
        x="window index",
        y="mean_motion",
        hue="instruction",
        hue_order=instruction_order,
        palette=PALETTE,
        alpha=0.35,
        linewidth=1.0,
        legend=False,
        ax=ax,
    )
    sns.scatterplot(
        data=windows,
        x="window index",
        y="mean_motion",
        hue="instruction",
        hue_order=instruction_order,
        style="deployment context",
        palette=PALETTE,
        s=42,
        alpha=0.85,
        ax=ax,
    )

    home_start = windows.loc[windows["deployment context"] == "home", "window index"].min()
    if pd.notna(home_start):
        ax.axvline(home_start - 0.5, color="#0f172a", linestyle="--", linewidth=1.5)
        ymax = windows["mean_motion"].max()
        ax.text((home_start - 0.5) / 2, ymax * 0.94, "laboratory", ha="center")
        ax.text(
            home_start + (windows["window index"].max() - home_start) / 2,
            ymax * 0.94,
            "home",
            ha="center",
        )

    ax.set_title("Descriptive longitudinal view of head-motion estimates")
    ax.set_xlabel("Window order over 10 sessions")
    ax.set_ylabel("Head-motion estimate")
    ax.legend(title="", ncol=2, frameon=True)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "Figure4_Longitudinal.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    generate_figures()
