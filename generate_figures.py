
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

def generate_paper_figures():
    # Setup style
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.4)
    try:
        plt.rcParams['font.family'] = 'sans-serif'
    except:
        pass

    # Load data
    base_path = "src/assets"

    all_windows = []
    all_trials = []

    for i in range(1, 11):
        # Context Logic
        if i <= 5:
            context = 'University'
        else:
            context = 'Home'

        # Windows
        w_path = os.path.join(base_path, f"data{i}", "windows.csv")
        if os.path.exists(w_path):
            df = pd.read_csv(w_path)
            df['context'] = context
            df['session'] = i
            all_windows.append(df)

        # Trials
        t_path = os.path.join(base_path, f"data{i}", "trials.csv")
        if os.path.exists(t_path):
            df_t = pd.read_csv(t_path)
            df_t['context'] = context
            df_t['session'] = i
            # Condition check
            if 'condition' in df_t.columns:
                all_trials.append(df_t)

    windows = pd.concat(all_windows, ignore_index=True)
    trials = pd.concat(all_trials, ignore_index=True)

    # Filter valid conditions
    valid_conds = ['THREAT', 'CHALLENGE', 'NEUTRAL']
    windows = windows[windows['condition'].isin(valid_conds)]
    trials = trials[trials['condition'].isin(valid_conds)]
    label_map = {'THREAT': 'negative instruction', 'CHALLENGE': 'positive instruction', 'NEUTRAL': 'neutral instruction'}
    context_map = {'University': 'laboratory', 'Home': 'home'}
    windows['condition_label'] = windows['condition'].map(label_map)
    trials['condition_label'] = trials['condition'].map(label_map)
    windows['context_label'] = windows['context'].map(context_map)
    trials['context_label'] = trials['context'].map(context_map)

    # Cleanup data types
    windows['mean_motion'] = pd.to_numeric(windows['mean_motion'], errors='coerce')
    trials['rt'] = pd.to_numeric(trials['rt'], errors='coerce')
    windows['mean_exposure_fluc'] = pd.to_numeric(windows['mean_exposure_fluc'], errors='coerce')

    # OUTPUT DIR
    out_dir = "paper_figures"
    os.makedirs(out_dir, exist_ok=True)

    # --- FIGURE 3: Interaction Effect (The "Safe Haven" Effect) ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Define Order
    hue_order = ['negative instruction', 'positive instruction', 'neutral instruction']
    context_order = ['laboratory', 'home']

    # A. Physiology (Motion)
    # Filter out outliers specifically for plotting? or keep raw? Keep raw.

    sns.barplot(data=windows, x='context_label', y='mean_motion', hue='condition_label',
                hue_order=hue_order, order=context_order,
                palette={'negative instruction': '#ff4d4d', 'positive instruction': '#4d79ff', 'neutral instruction': '#999999'},
                errorbar='se', ax=axes[0], capsize=.1)

    axes[0].set_title('A. Head-motion estimates', fontweight='bold')
    axes[0].set_ylabel('Head motion estimate (L2 norm)')
    axes[0].set_xlabel('Deployment context')
    axes[0].legend(title='Instructional task context')

    # B. Behavior (RT)
    sns.barplot(data=trials, x='context_label', y='rt', hue='condition_label',
                hue_order=hue_order, order=context_order,
                palette={'negative instruction': '#ff4d4d', 'positive instruction': '#4d79ff', 'neutral instruction': '#999999'},
                errorbar='se', ax=axes[1], capsize=.1)

    axes[1].set_title('B. Reaction time', fontweight='bold')
    axes[1].set_ylabel('Reaction Time (ms)')
    axes[1].set_xlabel('Deployment context')
    try:
        axes[1].get_legend().remove() # Unified legend
    except:
        pass

    plt.tight_layout()
    plt.savefig(f"{out_dir}/Figure3_Interaction.png", dpi=300)
    print("Generated Figure 3: Descriptive summaries")

    # --- FIGURE 2: Data Quality (Ecological Validity) ---
    plt.figure(figsize=(6, 5))
    sns.boxplot(data=windows, x='context_label', y='mean_exposure_fluc', hue='context_label', palette="Set2", legend=False)
    plt.title('Exposure fluctuation by context', fontweight='bold')
    plt.ylabel('Exposure fluctuation')

    # Add N
    n_u = len(windows[windows['context_label']=='laboratory'])
    n_h = len(windows[windows['context_label']=='home'])
    plt.text(0, windows['mean_exposure_fluc'].max(), f"n={n_u}", ha='center', va='bottom')
    plt.text(1, windows['mean_exposure_fluc'].max(), f"n={n_h}", ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(f"{out_dir}/Figure2_Quality.png", dpi=300)
    print("Generated Figure 2: Quality")

    # --- FIGURE 4: Longitudinal SCED Dynamics (Time Series) ---
    plt.figure(figsize=(14, 6))

    # We need a continuous time axis or just block index
    # Sort by session then block_id (assuming blocks 0,1,2...)
    # windows has block_id.

    # Create a unique block index: (session-1)*3 + block_id
    # Wait, block_id resets? Let's check data. Usually block_id is 0..N per session.
    # In DataLogger, block_id is 0,1,2...
    # Let's assume 6 blocks per session? Or variable.
    # We can just plot by "Session-Block"

    # Assign a global order
    windows = windows.sort_values(by=['session', 'start_time'])
    windows['global_index'] = range(len(windows))

    # Plot
    # University (Session 1-5)
    sns.lineplot(data=windows, x='global_index', y='mean_motion', hue='condition_label',
                 palette={'negative instruction': '#ff4d4d', 'positive instruction': '#4d79ff', 'neutral instruction': '#999999'},
                 alpha=0.5, linewidth=1, legend=False)

    sns.scatterplot(data=windows, x='global_index', y='mean_motion', hue='condition_label', style='context_label',
                    palette={'negative instruction': '#ff4d4d', 'positive instruction': '#4d79ff', 'neutral instruction': '#999999'},
                    s=60, alpha=0.9)

    # Add vertical line data separating Univ/Home
    # Find index where Home starts
    home_start_idx = windows[windows['context_label']=='home'].index.min()
    # Windows index might not be contiguous if we filtered?
    # global_index is contiguous range.
    home_start_global = windows[windows['context_label']=='home']['global_index'].min()

    if not np.isnan(home_start_global):
        plt.axvline(x=home_start_global - 0.5, color='black', linestyle='--', linewidth=2)
        plt.text(home_start_global/2, windows['mean_motion'].max()*0.9, "laboratory", ha='center', fontsize=12, fontweight='bold')
        plt.text(home_start_global + (windows['global_index'].max() - home_start_global)/2, windows['mean_motion'].max()*0.9, "home", ha='center', fontsize=12, fontweight='bold')

    plt.title('Descriptive longitudinal view of head-motion estimates', fontweight='bold')
    plt.ylabel('Head-motion estimate')
    plt.xlabel('Window order over 10 sessions')

    plt.tight_layout()
    plt.savefig(f"{out_dir}/Figure4_Longitudinal.png", dpi=300)
    print("Generated Figure 4: Longitudinal Time Series")


if __name__ == "__main__":
    generate_paper_figures()
