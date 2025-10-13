import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load dataset
iris = sns.load_dataset('iris')  # built-in in seaborn

# 2. Basic inspection
print("Shape:", iris.shape)
print("\nFirst 5 rows:")
print(iris.head())
print("\nInfo:")
print(iris.info())
print("\nAny missing values per column:")
print(iris.isnull().sum())

# 3. Summary statistics
print("\nSummary statistics (numeric columns):")
print(iris.describe())

# Also statistics by species
print("\nSummary by species:")
print(iris.groupby('species').agg(['mean', 'median', 'std']))

# 4. Data cleaning (if needed)
# Check duplicates
duplicates = iris.duplicated()
print("\nNumber of duplicate rows:", duplicates.sum())
# If duplicates exist, can drop them
iris_clean = iris.drop_duplicates()

# No missing values in Iris, so no fill/drop needed in this case

# 5. Visualizations

# a) Histogram of all numeric features
iris_clean.hist(bins=15, figsize=(12, 8))
plt.suptitle("Histograms of Iris features")
plt.show()

# b) Pairplot (scatter plots + distributions) colored by species
sns.pairplot(iris_clean, hue='species', diag_kind='kde')
plt.suptitle("Pairplot of Iris features by species", y=1.02)
plt.show()

# c) Boxplots for each feature by species
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
plt.figure(figsize=(14, 10))
for i, feature in enumerate(features, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x='species', y=feature, data=iris_clean, palette='Set2')
    plt.title(f'Boxplot of {feature} by species')
    plt.xlabel('Species')
    plt.ylabel(feature)
plt.tight_layout()
plt.show()

# d) Correlation heatmap
plt.figure(figsize=(8, 6))
corr = iris_clean.drop('species', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation between numeric features")
plt.show()
