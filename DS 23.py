from scipy import stats

design_A = [0.12,0.15,0.14,0.13,0.16]
design_B = [0.18,0.20,0.19,0.21,0.22]

t_stat, p_val = stats.ttest_ind(design_A, design_B)
print("T-statistic:", t_stat, "P-value:", p_val)
