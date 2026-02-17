
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from scipy import stats

def annotate_significance(ax, data, x, y, hue, pair_conds):
    """
    Annotate significance between two conditions (pair_conds) within each x-category.
    """
    contexts = data[x].unique()
    
    # Y-offset for annotations
    y_max = data[y].max()
    h = y_max * 0.05
    
    for i, context in enumerate(sorted(contexts, reverse=True)): # University first if desc, but seaborn order matters.
        # Get data
        d1 = data[(data[x] == context) & (data[hue] == pair_conds[0])][y].dropna()
        d2 = data[(data[x] == context) & (data[hue] == pair_conds[1])][y].dropna()
        
        n1 = len(d1)
        n2 = len(d2)
        
        # T-test
        if n1 > 1 and n2 > 1:
            t, p = stats.ttest_ind(d1, d2, equal_var=False)
            
            # Format p-value
            if p < 0.001:
                sig_symbol = "***"
            elif p < 0.01:
                sig_symbol = "**"
            elif p < 0.05:
                sig_symbol = "*"
            else:
                sig_symbol = "n.s."
            
            # Draw line and text
            # Approximate x-coords for hue bars. 
            # Seaborn dodge: width=0.8. 3 bars. centers at -0.27, 0, 0.27 roughly?
            # THREAT (red) vs CHALLENGE (blue)
            # hue_order was THREAT, CHALLENGE, NEUTRAL
            # THREAT is index 0, CHALLENGE is index 1.
            
            # Context-centers: 0, 1. Univ is usually 1 (alphabetical H, U? No. Home, Univ).
            # Let's dynamically find centers if possible, or assume seaborn default.
            # Default order: Home (0), University (1)
            
            x_center = i 
            bar_width = 0.26 # Approx
            x1 = x_center - epsilon
            x2 = x_center
            
            # Hardcoded offset for hue_order=['THREAT', 'CHALLENGE', 'NEUTRAL']
            # THREAT is 1st (-0.26), CHALLENGE is 2nd (0), NEUTRAL is 3rd (+0.26)
            x_threat = x_center - 0.26
            x_chal = x_center
            
            y1 = data[(data[x] == context)][y].mean() + data[(data[x] == context)][y].std() # Just above bar? No, above max.
            # Find max of the two comparison bars
            y_curr_max = max(d1.mean() + d1.std(), d2.mean() + d2.std())
            y_curr_max = max(d1.max(), d2.max()) # safer for raw data points
            
            # Draw
            line_y = y_curr_max + h
            ax.plot([x_threat, x_threat, x_chal, x_chal], [line_y, line_y+h, line_y+h, line_y], lw=1.5, c='k')
            ax.text((x_threat+x_chal)/2, line_y+h, f"{sig_symbol}\n(p={p:.3f})", ha='center', va='bottom', fontsize=10)
            
            # Add N
            ax.text(x_center, 0, f"n={n1+n2}", ha='center', va='bottom', fontsize=8, color='black', fontweight='bold')

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
    hue_order = ['THREAT', 'CHALLENGE', 'NEUTRAL']
    context_order = ['University', 'Home']
    
    # A. Physiology (Motion)
    # Filter out outliers specifically for plotting? or keep raw? Keep raw.
    
    sns.barplot(data=windows, x='context', y='mean_motion', hue='condition', 
                hue_order=hue_order, order=context_order,
                palette={'THREAT': '#ff4d4d', 'CHALLENGE': '#4d79ff', 'NEUTRAL': '#999999'},
                errorbar='se', ax=axes[0], capsize=.1)
    
    axes[0].set_title('A. Physiological Freezing (Motion)', fontweight='bold')
    axes[0].set_ylabel('Head Motion (L2 Norm)')
    axes[0].set_xlabel('Context')
    axes[0].legend(title='Condition')
    
    # Custom Annotation for Motion
    # We compare THREAT vs CHALLENGE
    # University (Index 0)
    # Home (Index 1)
    
    # Manually annotate for control
    # University
    u_th = windows[(windows['context']=='University') & (windows['condition']=='THREAT')]['mean_motion'].dropna()
    u_ch = windows[(windows['context']=='University') & (windows['condition']=='CHALLENGE')]['mean_motion'].dropna()
    t_u, p_u = stats.ttest_ind(u_th, u_ch, equal_var=False)
    
    # Home
    h_th = windows[(windows['context']=='Home') & (windows['condition']=='THREAT')]['mean_motion'].dropna()
    h_ch = windows[(windows['context']=='Home') & (windows['condition']=='CHALLENGE')]['mean_motion'].dropna()
    t_h, p_h = stats.ttest_ind(h_th, h_ch, equal_var=False)

    # Draw Univ
    y_max = windows['mean_motion'].max()
    h = y_max * 0.05
    x_u = 0 # Univ is index 0
    # THREAT(-0.27), CHAL(0)
    axes[0].plot([-0.27, -0.27, 0, 0], [1.3e-3, 1.35e-3, 1.35e-3, 1.3e-3], lw=1.5, c='k') # Hardcoded Y for neatness
    sig_u = "***" if p_u < 0.001 else "**" if p_u < 0.01 else "*" if p_u < 0.05 else "n.s."
    axes[0].text(-0.135, 1.35e-3, f"{sig_u}\n(p={p_u:.3f})", ha='center', va='bottom')
    axes[0].text(0, 0, f"n(win)={len(u_th)+len(u_ch)}", ha='center', va='bottom', fontsize=9)

    # Draw Home
    x_h = 1 # Home is index 1
    axes[0].plot([1-0.27, 1-0.27, 1, 1], [1.3e-3, 1.35e-3, 1.35e-3, 1.3e-3], lw=1.5, c='k')
    sig_h = "***" if p_h < 0.001 else "**" if p_h < 0.01 else "*" if p_h < 0.05 else "n.s."
    axes[0].text(1-0.135, 1.35e-3, f"{sig_h}\n(p={p_h:.3f})", ha='center', va='bottom')
    axes[0].text(1, 0, f"n(win)={len(h_th)+len(h_ch)}", ha='center', va='bottom', fontsize=9)


    # B. Behavior (RT)
    sns.barplot(data=trials, x='context', y='rt', hue='condition',
                hue_order=hue_order, order=context_order,
                palette={'THREAT': '#ff4d4d', 'CHALLENGE': '#4d79ff', 'NEUTRAL': '#999999'},
                errorbar='se', ax=axes[1], capsize=.1)
    
    axes[1].set_title('B. Behavioral Response (RT)', fontweight='bold')
    axes[1].set_ylabel('Reaction Time (ms)')
    axes[1].set_xlabel('Context')
    try:
        axes[1].get_legend().remove() # Unified legend
    except:
        pass
        
    # Stats for RT
    # University
    u_th_rt = trials[(trials['context']=='University') & (trials['condition']=='THREAT')]['rt'].dropna()
    u_ch_rt = trials[(trials['context']=='University') & (trials['condition']=='CHALLENGE')]['rt'].dropna()
    t_u_rt, p_u_rt = stats.ttest_ind(u_th_rt, u_ch_rt, equal_var=False)

    y_max_rt = trials['rt'].max() # approx 3500? No avg is 1000.
    y_line = 1300 # manual
    axes[1].plot([-0.27, -0.27, 0, 0], [y_line, y_line+50, y_line+50, y_line], lw=1.5, c='k')
    sig_u_rt = "***" if p_u_rt < 0.001 else "**" if p_u_rt < 0.01 else "*" if p_u_rt < 0.05 else "n.s."
    axes[1].text(-0.135, y_line+50, f"{sig_u_rt}\n(p={p_u_rt:.3f})", ha='center', va='bottom')
    axes[1].text(0, 0, f"n(trial)={len(u_th_rt)+len(u_ch_rt)}", ha='center', va='bottom', fontsize=9)

    # Home
    h_th_rt = trials[(trials['context']=='Home') & (trials['condition']=='THREAT')]['rt'].dropna()
    h_ch_rt = trials[(trials['context']=='Home') & (trials['condition']=='CHALLENGE')]['rt'].dropna()
    t_h_rt, p_h_rt = stats.ttest_ind(h_th_rt, h_ch_rt, equal_var=False)
    
    axes[1].plot([1-0.27, 1-0.27, 1, 1], [y_line, y_line+50, y_line+50, y_line], lw=1.5, c='k')
    sig_h_rt = "***" if p_h_rt < 0.001 else "**" if p_h_rt < 0.01 else "*" if p_h_rt < 0.05 else "n.s."
    axes[1].text(1-0.135, y_line+50, f"{sig_h_rt}\n(p={p_h_rt:.3f})", ha='center', va='bottom')
    axes[1].text(1, 0, f"n(trial)={len(h_th_rt)+len(h_ch_rt)}", ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(f"{out_dir}/Figure3_Interaction.png", dpi=300)
    print("Generated Figure 3: Interaction Effect with Stats")

    # --- FIGURE 2: Data Quality (Ecological Validity) ---
    plt.figure(figsize=(6, 5))
    sns.boxplot(data=windows, x='context', y='mean_exposure_fluc', hue='context', palette="Set2", legend=False)
    plt.title('B. Environment Signal Quality', fontweight='bold')
    plt.ylabel('Exposure Fluctuation (Noise Level)')
    
    # Add N
    n_u = len(windows[windows['context']=='University'])
    n_h = len(windows[windows['context']=='Home'])
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
    sns.lineplot(data=windows, x='global_index', y='mean_motion', hue='condition', 
                 palette={'THREAT': '#ff4d4d', 'CHALLENGE': '#4d79ff', 'NEUTRAL': '#999999'},
                 alpha=0.5, linewidth=1, legend=False)
    
    sns.scatterplot(data=windows, x='global_index', y='mean_motion', hue='condition', style='context',
                    palette={'THREAT': '#ff4d4d', 'CHALLENGE': '#4d79ff', 'NEUTRAL': '#999999'},
                    s=60, alpha=0.9)
    
    # Add vertical line data separating Univ/Home
    # Find index where Home starts
    home_start_idx = windows[windows['context']=='Home'].index.min()
    # Windows index might not be contiguous if we filtered? 
    # global_index is contiguous range.
    home_start_global = windows[windows['context']=='Home']['global_index'].min()
    
    if not np.isnan(home_start_global):
        plt.axvline(x=home_start_global - 0.5, color='black', linestyle='--', linewidth=2)
        plt.text(home_start_global/2, windows['mean_motion'].max()*0.9, "University (Lab)", ha='center', fontsize=12, fontweight='bold')
        plt.text(home_start_global + (windows['global_index'].max() - home_start_global)/2, windows['mean_motion'].max()*0.9, "Home (Natural)", ha='center', fontsize=12, fontweight='bold')

    plt.title('C. Longitudinal Dynamics (SCED): Threat Response Dampening', fontweight='bold')
    plt.ylabel('Head Motion (Freezing)')
    plt.xlabel('Time (Blocks over 10 Sessions)')
    
    plt.tight_layout()
    plt.savefig(f"{out_dir}/Figure4_Longitudinal.png", dpi=300)
    print("Generated Figure 4: Longitudinal Time Series")


if __name__ == "__main__":
    generate_paper_figures()
