"""
Advanced Statistical Analysis for IEEE ToAC Paper
Performs:
1. 2-way ANOVA (Context x Condition)
2. Effect Size Comparison (Cohen's d)
3. Habituation Effect (Session correlation)
4. Bayesian Analysis (Bayes Factor)
5. Mixed-Effects Model
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import pearsonr
import os

# For ANOVA
try:
    import statsmodels.api as sm
    from statsmodels.formula.api import ols, mixedlm
    HAS_STATSMODELS = True
except ImportError:
    HAS_STATSMODELS = False
    print("Warning: statsmodels not available, skipping ANOVA and Mixed-Effects")

# For Bayesian
try:
    from scipy.stats import ttest_ind
    # We'll use BIC approximation for Bayes Factor
    HAS_BAYESIAN = True
except ImportError:
    HAS_BAYESIAN = False

def cohens_d(group1, group2):
    """Calculate Cohen's d effect size"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std if pooled_std > 0 else 0

def bayes_factor_ttest(group1, group2):
    """
    Approximate Bayes Factor using BIC approximation
    BF10 > 3: Evidence for alternative
    BF10 < 1/3: Evidence for null
    """
    n1, n2 = len(group1), len(group2)
    t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False)
    
    # BIC approximation
    n = n1 + n2
    bic_alt = n * np.log(1 - (t_stat**2 / (t_stat**2 + n - 2)))
    bic_null = 0
    bf10 = np.exp((bic_null - bic_alt) / 2)
    
    return bf10, p_val

def run_all_analyses():
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
            df['session'] = i
            df['mean_motion'] = pd.to_numeric(df['mean_motion'], errors='coerce')
            all_windows.append(df)
            
        # Trials
        t_path = os.path.join(base_path, f"data{i}", "trials.csv")
        if os.path.exists(t_path):
            df_t = pd.read_csv(t_path)
            df_t['context'] = context
            df_t['session'] = i
            df_t['rt'] = pd.to_numeric(df_t['rt'], errors='coerce')
            all_trials.append(df_t)

    windows = pd.concat(all_windows, ignore_index=True)
    trials = pd.concat(all_trials, ignore_index=True)
    
    # Filter for main conditions
    windows_main = windows[windows['condition'].isin(['THREAT', 'CHALLENGE'])].copy()
    trials_main = trials[trials['condition'].isin(['THREAT', 'CHALLENGE'])].copy()

    print("="*80)
    print("ADVANCED STATISTICAL ANALYSIS")
    print("="*80)
    
    # ========================================================================
    # 1. TWO-WAY ANOVA (Context × Condition)
    # ========================================================================
    print("\n[1] TWO-WAY ANOVA (Context × Condition Interaction)")
    print("-" * 80)
    
    if HAS_STATSMODELS:
        # Physiology (Motion)
        print("\nA. Physiological Response (Head Motion)")
        windows_clean = windows_main.dropna(subset=['mean_motion'])
        formula = 'mean_motion ~ C(context) + C(condition) + C(context):C(condition)'
        model = ols(formula, data=windows_clean).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        print(anova_table)
        
        interaction_p = anova_table.loc['C(context):C(condition)', 'PR(>F)']
        print(f"\n*** Interaction Effect: F={anova_table.loc['C(context):C(condition)', 'F']:.3f}, p={interaction_p:.4f} ***")
        
        # Behavior (RT)
        print("\n\nB. Behavioral Response (Reaction Time)")
        trials_clean = trials_main.dropna(subset=['rt'])
        formula_rt = 'rt ~ C(context) + C(condition) + C(context):C(condition)'
        model_rt = ols(formula_rt, data=trials_clean).fit()
        anova_table_rt = sm.stats.anova_lm(model_rt, typ=2)
        print(anova_table_rt)
        
        interaction_p_rt = anova_table_rt.loc['C(context):C(condition)', 'PR(>F)']
        print(f"\n*** Interaction Effect: F={anova_table_rt.loc['C(context):C(condition)', 'F']:.3f}, p={interaction_p_rt:.4f} ***")
    else:
        print("(Skipped - statsmodels not available)")
    
    # ========================================================================
    # 2. EFFECT SIZE COMPARISON TABLE
    # ========================================================================
    print("\n\n[2] EFFECT SIZE COMPARISON (Cohen's d)")
    print("-" * 80)
    
    results_table = []
    
    for measure, data, col in [('Motion', windows_main, 'mean_motion'), ('RT', trials_main, 'rt')]:
        print(f"\n{measure}:")
        for context in ['University', 'Home']:
            threat = data[(data['context']==context) & (data['condition']=='THREAT')][col].dropna()
            challenge = data[(data['context']==context) & (data['condition']=='CHALLENGE')][col].dropna()
            
            d = cohens_d(threat, challenge)
            t, p = stats.ttest_ind(threat, challenge, equal_var=False)
            
            # Interpretation
            if abs(d) < 0.2:
                interp = "Negligible"
            elif abs(d) < 0.5:
                interp = "Small"
            elif abs(d) < 0.8:
                interp = "Medium"
            else:
                interp = "Large"
            
            print(f"  {context:12s}: d={d:+.3f} ({interp:10s}), t={t:.3f}, p={p:.4f}")
            results_table.append({
                'Measure': measure,
                'Context': context,
                "Cohen's d": d,
                't-statistic': t,
                'p-value': p,
                'Interpretation': interp
            })
    
    results_df = pd.DataFrame(results_table)
    print("\n\nSummary Table:")
    print(results_df.to_string(index=False))
    
    # ========================================================================
    # 3. HABITUATION EFFECT (Session Trend)
    # ========================================================================
    print("\n\n[3] HABITUATION EFFECT (Session × Physiological Response)")
    print("-" * 80)
    
    # Aggregate by session
    session_motion = windows.groupby('session')['mean_motion'].mean()
    session_nums = session_motion.index.values
    motion_vals = session_motion.values
    
    r, p = pearsonr(session_nums, motion_vals)
    print(f"\nPearson Correlation (Session vs Motion): r={r:.3f}, p={p:.4f}")
    
    if p < 0.05:
        print("*** SIGNIFICANT habituation effect detected ***")
        print(f"As sessions progressed, motion {'decreased' if r < 0 else 'increased'} systematically.")
    else:
        print("(No significant habituation trend)")
    
    # ========================================================================
    # 4. BAYESIAN ANALYSIS
    # ========================================================================
    print("\n\n[4] BAYESIAN ANALYSIS (Bayes Factor)")
    print("-" * 80)
    print("BF10 Interpretation: >3 = Evidence for H1, <1/3 = Evidence for H0\n")
    
    for measure, data, col in [('Motion', windows_main, 'mean_motion'), ('RT', trials_main, 'rt')]:
        print(f"{measure}:")
        for context in ['University', 'Home']:
            threat = data[(data['context']==context) & (data['condition']=='THREAT')][col].dropna()
            challenge = data[(data['context']==context) & (data['condition']=='CHALLENGE')][col].dropna()
            
            bf, p = bayes_factor_ttest(threat, challenge)
            
            if bf > 3:
                evidence = "Moderate-to-Strong evidence FOR difference"
            elif bf < 1/3:
                evidence = "Moderate-to-Strong evidence AGAINST difference (null)"
            else:
                evidence = "Inconclusive"
            
            print(f"  {context:12s}: BF10={bf:.3f} ({evidence})")
    
    # ========================================================================
    # 5. MIXED-EFFECTS MODEL (Advanced)
    # ========================================================================
    print("\n\n[5] MIXED-EFFECTS MODEL (Session as Random Effect)")
    print("-" * 80)
    
    if HAS_STATSMODELS:
        # Physiology
        print("\nA. Physiological Response (Motion)")
        windows_clean = windows_main.dropna(subset=['mean_motion'])
        
        try:
            # Random intercept for session
            formula_lme = 'mean_motion ~ C(context) * C(condition)'
            model_lme = mixedlm(formula_lme, windows_clean, groups=windows_clean['session']).fit()
            print(model_lme.summary())
        except Exception as e:
            print(f"(Could not fit mixed model: {e})")
        
        # Behavior
        print("\n\nB. Behavioral Response (RT)")
        trials_clean = trials_main.dropna(subset=['rt'])
        
        try:
            formula_lme_rt = 'rt ~ C(context) * C(condition)'
            model_lme_rt = mixedlm(formula_lme_rt, trials_clean, groups=trials_clean['session']).fit()
            print(model_lme_rt.summary())
        except Exception as e:
            print(f"(Could not fit mixed model: {e})")
    else:
        print("(Skipped - statsmodels not available)")
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    
    # Save summary to file
    with open('advanced_analysis_summary.txt', 'w', encoding='utf-8') as f:
        f.write("ADVANCED STATISTICAL ANALYSIS SUMMARY\n")
        f.write("="*80 + "\n\n")
        f.write("1. TWO-WAY ANOVA\n")
        if HAS_STATSMODELS:
            f.write(f"   Motion Interaction: p={interaction_p:.4f}\n")
            f.write(f"   RT Interaction: p={interaction_p_rt:.4f}\n\n")
        f.write("2. EFFECT SIZE TABLE\n")
        f.write(results_df.to_string(index=False))
        f.write(f"\n\n3. HABITUATION\n")
        f.write(f"   r={r:.3f}, p={p:.4f}\n")
    
    print("\nSummary saved to: advanced_analysis_summary.txt")

if __name__ == "__main__":
    run_all_analyses()
