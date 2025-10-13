import pandas as pd

# 1. Read the CSV file 
df = pd.read_csv('students_marks.csv')

# 2. Display basic information (number of rows, columns, data types, non-null counts, etc.)
print("===== Basic Information =====")
df.info()

# 3. Display the first 5 rows
print("\n===== Top 5 Rows =====")
print(df.head())

# 4. Display summary statistics (numeric columns)
print("\n===== Summary Statistics (numeric columns) =====")
print(df.describe())

# 5 Summary including non-numeric columns 
print("\n===== Summary (all columns) =====")
print(df.describe(include='all'))
