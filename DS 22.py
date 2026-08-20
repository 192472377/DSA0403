import numpy as np
import scipy.stats as stats

drug = np.random.normal(10, 2, 50)
placebo = np.random.normal(5, 2, 50)

ci_drug = stats.t.interval(0.95, len(drug)-1, loc=np.mean(drug), scale=stats.sem(drug))
ci_placebo = stats.t.interval(0.95, len(placebo)-1, loc=np.mean(placebo), scale=stats.sem(placebo))

print("95% CI Drug:", ci_drug)
print("95% CI Placebo:", ci_placebo)
