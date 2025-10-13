import numpy as np
from scipy import stats




# Sample data
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([12, 24, 33, 47, 54, 66, 75, 89])

# 1. Compute Pearson correlation coefficient (r) using NumPy
corr_matrix = np.corrcoef(x, y)
r_np = corr_matrix[0, 1]
print("Pearson r (NumPy):", r_np)

# 2. Use SciPy’s pearsonr to get both r and p-value
r_scipy, p_value = stats.pearsonr(x, y)
print("Pearson r (SciPy):", r_scipy)
print("p-value:", p_value)

# 3. Interpret results
alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis: significant correlation.")
else:
    print("Fail to reject null hypothesis: correlation not significant.")
print("Strength of correlation:", end=" ") 