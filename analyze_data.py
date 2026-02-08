
import os
import pandas as pd
import json
import glob
import numpy as np

def analyze_all_data():
    all_windows = []
    all_subjective = []
    
    # Path to assets
    base_path = r"c:\Users\hatake\OneDrive\画像\デスクトップ\.vscode\camerala\src\assets"
    
    # Iterate through data1 to data10
    for i in range(1, 11):
        folder = os.path.join(base_path, f"data{i}")
        win_path = os.path.join(folder, "windows.csv")
        sub_path = os.path.join(folder, "subjective.csv")
        
        context = 'University' if i <= 5 else 'Home'

        if os.path.exists(win_path):
            df_w = pd.read_csv(win_path)
            df_w['session'] = i
            df_w['context'] = context
            all_windows.append(df_w)
            
        if os.path.exists(sub_path):
            df_s = pd.read_csv(sub_path)
            df_s['session'] = i
            df_s['context'] = context
            all_subjective.append(df_s)

    if not all_windows:
        print("No data found.")
        return

    # Combine
    windows = pd.concat(all_windows, ignore_index=True)
    subjective = pd.concat(all_subjective, ignore_index=True)

    print(f"Total Windows: {len(windows)}")
    print(f"Total Subjective Ratings: {len(subjective)}")
    print(f"Sessions: {sorted(windows['session'].unique())}")

    # --- 0. Context Comparison (Ecological Validity) ---
    print("\n[Ecological Validity] Home vs University (Baseline Features):")
    print(windows.groupby('context')[['mean_roival', 'mean_motion', 'mean_exposure_fluc', 'mean_quality']].mean())

    # --- 1. Signal Quality Check (Exposure Fluctuation) ---
    # Low means good quality.
    mean_exp_fluc = windows['mean_exposure_fluc'].mean()
    print(f"\n[Quality] Mean Exposure Fluctuation: {mean_exp_fluc:.4f} (Lower is better)")

    # --- 2. Physiological Differentiation (Threat vs Challenge) ---
    # We hypothesize meaningful diffs in 'mean_motion' or 'mean_roival' (brightness) or 'mean_ear'
    print("\n[Physiology] Condition Differences (Mean +/- Std):")
    
    for metric in ['mean_roival', 'mean_motion', 'mean_ear']:
        print(f"\n-- {metric} --")
        stats = windows.groupby('condition')[metric].agg(['mean', 'std', 'count'])
        print(stats)
        
        # Simple Cohen's d (Threat vs Challenge)
        try:
            m1 = stats.loc['THREAT', 'mean']
            s1 = stats.loc['THREAT', 'std']
            n1 = stats.loc['THREAT', 'count']
            
            m2 = stats.loc['CHALLENGE', 'mean']
            s2 = stats.loc['CHALLENGE', 'std']
            n2 = stats.loc['CHALLENGE', 'count']
            
            # Pooled SD
            sp = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
            d = (m1 - m2) / sp
            
            print(f"Effect Size (Threat vs Challenge) Cohen's d: {d:.3f}")
        except:
            print("Could not calc effect size (missing conditions?)")

    # --- 3. Behavioral Differentiation ---
    # Accuracy / RT
    print("\n[Behavior] Condition Differences:")
    for metric in ['mean_rt', 'accuracy']:
        print(f"\n-- {metric} --")
        # rt might be null, dropna
        stats = windows.dropna(subset=[metric]).groupby('condition')[metric].agg(['mean', 'std', 'count'])
        print(stats)

    # --- 4. Subjective Check ---
    print("\n[Subjective] Ratings:")
    print(subjective.groupby('condition')[['appraisal', 'valence', 'utility']].mean())

if __name__ == "__main__":
    analyze_all_data()
