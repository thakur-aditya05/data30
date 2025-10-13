import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the tips dataset
tips = sns.load_dataset("tips")

# 2. Inspect the data  
print(tips.head())
print(tips.info())

#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   total_bill  244 non-null    float64
#  1   tip         244 non-null    float64
#  2   sex         244 non-null    category
#  3   smoker      244 non-null    category
#  4   day         244 non-null    category
#  5   time        244 non-null    category
#  6   size        244 non-null    int64
# dtypes: category(4), float64(2), int64(1)
# memory usage: 7.4 KB
# None





# 3. Create the boxplot: tip amount by day
plt.figure(figsize=(8, 6))
sns.boxplot(x="day", y="tip", data=tips, palette="Set3")

# 4. Customize title and axis labels
plt.title("Distribution of Tips by Day", fontsize=16)
plt.xlabel("Day of Week", fontsize=14)
plt.ylabel("Tip Amount ($)", fontsize=14)

# 5. Optionally rotate x-ticks if needed
plt.xticks(rotation=0)

# 6. Show grid (if desired)
plt.grid(True, linestyle='--', alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
# 7. Optionally, save the plot
plt.savefig("tips_boxplot.png", dpi=300)