import pandas as pd

file_path = "assignment1/scripts/ev_dataset.csv"  
df = pd.read_csv(file_path)

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values[missing_values > 0])

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nUnique values in '{col}': {df[col].nunique()}")

print("\nFirst 5 rows of the dataset:")
print(df.head())
