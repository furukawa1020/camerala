
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

    # --- 2. Advanced Statistical Analysis ---
    import matplotlib.pyplot as plt
    try:
        from sklearn.cluster import KMeans
        from sklearn.preprocessing import StandardScaler
        import seaborn as sns
        from scipy import stats
    except ImportError:
        print("Skipping advanced stats (sklearn/scipy/seaborn not found)")
        return

    # A. Correlation Matrix
    print("\n[Correlation] Physiological & Context Features:")
    # Create dummy for Context (Home=1, Univ=0)
    windows['is_home'] = (windows['context'] == 'Home').astype(int)
    corr_cols = ['mean_roival', 'mean_motion', 'mean_ear', 'mean_exposure_fluc', 'mean_quality', 'is_home']
    corr = windows[corr_cols].corr()
    print(corr)

    # B. Clustering (Unsupervised Learning)
    # Can we find "Physiological States" without knowing the condition?
    # Features: Motion, EAR, ROI
    features = windows[['mean_motion', 'mean_ear', 'mean_roival']].dropna()
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    windows.loc[features.index, 'cluster'] = kmeans.fit_predict(scaled_features)
    
    print("\n[Clustering] Cluster Centers (Scaled):")
    # Inverse transform to see real values
    centers = scaler.inverse_transform(kmeans.cluster_centers_)
    df_centers = pd.DataFrame(centers, columns=['Motion', 'EAR', 'ROI'])
    
    # --- 3. Behavioral Differentiation (Using Trials Data) ---
    # Load all trials
    all_trials = []
    for i in range(1, 11):
        t_path = os.path.join(base_path, f"data{i}", "trials.csv")
        context = 'University' if i <= 5 else 'Home'
        if os.path.exists(t_path):
            df_t = pd.read_csv(t_path)
            df_t['session'] = i
            df_t['context'] = context
            all_trials.append(df_t)
    
    if all_trials:
        trials = pd.concat(all_trials, ignore_index=True)
        print("\n[Behavior] Condition Differences (from Trials):")
        # RT (ms)
        print("-- Reaction Time (ms) --")
        print(trials.groupby('condition')['rt'].agg(['mean', 'std', 'count']))
        
        # Accuracy
        print("\n-- Accuracy --")
        # correct is boolean, convert to int
        trials['correct_int'] = trials['correct'].astype(int)
        print(trials.groupby('condition')['correct_int'].agg(['mean', 'count']))
        
        # Framing Effect Check: Efficiency (Accuracy / RT) ?
        # Or just Context x Condition for RT
        print("\n[Interaction] RT by Condition x Context:")
        print(trials.groupby(['context', 'condition'])['rt'].mean())

    # D. Time series trend (Fatigue effect?)
    # Correlation between Session Index and Baseline Motion
    # Fix: use stats.pearsonr correctly
    clean_win = windows.dropna(subset=['mean_motion', 'session'])
    r, p = stats.pearsonr(clean_win['session'], clean_win['mean_motion'])
    print(f"\n[Trend] Session vs Motion: r={r:.3f}, p={p:.3f}")


if __name__ == "__main__":
    analyze_all_data()
