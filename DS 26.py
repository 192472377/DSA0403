import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Synthetic dataset
control = np.random.normal(loc=50, scale=5, size=30)   # placebo group
treatment = np.random.normal(loc=55, scale=5, size=30) # drug group

# Hypothesis test (t-test)
t_stat, p_value = stats.ttest_ind(control, treatment)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Visualization (fixed keyword)
plt.boxplot([control, treatment], tick_labels=["Placebo", "Treatment"])
plt.title(f"Clinical Trial Results (p-value={p_value:.4f})")
plt.ylabel("Response Value")
plt.show()
