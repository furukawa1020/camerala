
import pandas as pd
from scipy import stats
import os

def verify_stats():
    base_path = r"c:\Users\hatake\OneDrive\画像\デスクトップ\.vscode\camerala\src\assets"
    
    # Load Data
    all_windows = []
    all_trials = []
    
    for i in range(1, 11):
        context = 'University' if i <= 5 else 'Home'
        
        # Windows
        w_path = os.path.join(base_path, f"data{i}", "windows.csv")
        if os.path.exists(w_path):
            df = pd.read_csv(w_path)
            df['context'] = context
            df['mean_motion'] = pd.to_numeric(df['mean_motion'], errors='coerce')
            all_windows.append(df)
            
        # Trials
        t_path = os.path.join(base_path, f"data{i}", "trials.csv")
        if os.path.exists(t_path):
            df_t = pd.read_csv(t_path)
            df_t['context'] = context
            df_t['rt'] = pd.to_numeric(df_t['rt'], errors='coerce')
            all_trials.append(df_t)

    windows = pd.concat(all_windows, ignore_index=True)
    trials = pd.concat(all_trials, ignore_index=True)

    print("=== STATISTICAL VERIFICATION (Raw Output) ===")
    
    # 1. Physiology (Motion)
    print("\n[Physiology: Head Motion]")
    for context in ['University', 'Home']:
        th = windows[(windows['context']==context) & (windows['condition']=='THREAT')]['mean_motion'].dropna()
        ch = windows[(windows['context']==context) & (windows['condition']=='CHALLENGE')]['mean_motion'].dropna()
        
        t, p = stats.ttest_ind(th, ch, equal_var=False)
        print(f"  Context: {context}")
        print(f"    Threat (n={len(th)}): mean={th.mean():.6f}")
        print(f"    Chall  (n={len(ch)}): mean={ch.mean():.6f}")
        print(f"    T-test: t={t:.4f}, p={p:.10f}")
        if p < 0.05:
            print("    -> SIGNIFICANT")
        else:
            print("    -> NOT SIGNIFICANT")

    # 2. Behavior (RT)
    print("\n[Behavior: Reaction Time]")
    for context in ['University', 'Home']:
        th = trials[(trials['context']==context) & (trials['condition']=='THREAT')]['rt'].dropna()
        ch = trials[(trials['context']==context) & (trials['condition']=='CHALLENGE')]['rt'].dropna()
        
        t, p = stats.ttest_ind(th, ch, equal_var=False)
        print(f"  Context: {context}")
        print(f"    Threat (n={len(th)}): mean={th.mean():.2f}ms")
        print(f"    Chall  (n={len(ch)}): mean={ch.mean():.2f}ms")
        print(f"    T-test: t={t:.4f}, p={p:.10f}")
        if p < 0.05:
            print("    -> SIGNIFICANT")
        else:
            print("    -> NOT SIGNIFICANT")

if __name__ == "__main__":
    verify_stats()
