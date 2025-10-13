import pandas as pd

# 1. Read CSV with missing values
df = pd.read_csv('students_marks_missing.csv')

# 2. Inspect missing data
print("Missing values per column:")
print(df.isnull().sum())
print()

# 3. Choose a way to handle missing values
# Option A: Drop rows where the column we care about is missing
# Suppose we want to compute the average of 'science' grouped by 'class'
df2 = df.dropna(subset=['science'])

# Option B: Fill missing values with something reasonable: e.g. mean of that column
df2 = df.copy()
science_mean = df2['science'].mean()
df2['science'] = df2['science'].fillna(science_mean)

# 4. Group by a column and compute average of another column
grouped = df2.groupby('class')['science'].mean().reset_index()


# Average science marks by class (after cleaning):
print("Average science marks by class (after cleaning):")
print(grouped)
