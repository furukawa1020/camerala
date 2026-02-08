
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
    base_path = r"c:\Users\hatake\OneDrive\画像\デスクトップ\.vscode\camerala\src\assets"
    
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
    
    # OUTPUT DIR
    out_dir = "paper_figures"
    os.makedirs(out_dir, exist_ok=True)

    # --- FIGURE 3: Interaction Effect (The "Safe Haven" Effect) ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # A. Physiology (Motion)
    # Ensure numeric
    windows['mean_motion'] = pd.to_numeric(windows['mean_motion'], errors='coerce')
    
    sns.barplot(data=windows, x='context', y='mean_motion', hue='condition', 
                palette={'THREAT': '#ff4d4d', 'CHALLENGE': '#4d79ff', 'NEUTRAL': '#999999'},
                errorbar='se', ax=axes[0], capsize=.1)
    
    axes[0].set_title('A. Physiological Freezing (Motion)', fontweight='bold')
    axes[0].set_ylabel('Head Motion (L2 Norm)')
    axes[0].set_xlabel('Context')
    axes[0].legend(title='Condition')
    
    # B. Behavior (RT)
    trials['rt'] = pd.to_numeric(trials['rt'], errors='coerce')
    
    sns.barplot(data=trials, x='context', y='rt', hue='condition',
                palette={'THREAT': '#ff4d4d', 'CHALLENGE': '#4d79ff', 'NEUTRAL': '#999999'},
                errorbar='se', ax=axes[1], capsize=.1)
    
    axes[1].set_title('B. Behavioral Response (RT)', fontweight='bold')
    axes[1].set_ylabel('Reaction Time (ms)')
    axes[1].set_xlabel('Context')
    try:
        axes[1].get_legend().remove() # Unified legend
    except:
        pass
    
    plt.tight_layout()
    plt.savefig(f"{out_dir}/Figure3_Interaction.png", dpi=300)
    # plt.savefig(f"{out_dir}/Figure3_Interaction.pdf") # PDF might fail on windows without backend
    print("Generated Figure 3: Interaction Effect")

    # --- FIGURE 2: Data Quality (Ecological Validity) ---
    plt.figure(figsize=(6, 5))
    windows['mean_exposure_fluc'] = pd.to_numeric(windows['mean_exposure_fluc'], errors='coerce')
    sns.boxplot(data=windows, x='context', y='mean_exposure_fluc', hue='context', palette="Set2", legend=False)
    plt.title('B. Environment Signal Quality', fontweight='bold')
    plt.ylabel('Exposure Fluctuation (Noise Level)')
    plt.tight_layout()
    plt.savefig(f"{out_dir}/Figure2_Quality.png", dpi=300)
    print("Generated Figure 2: Quality")

if __name__ == "__main__":
    generate_paper_figures()
