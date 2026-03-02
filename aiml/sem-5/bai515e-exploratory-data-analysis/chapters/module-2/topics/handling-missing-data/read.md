python
# Check for missing values
df.isnull().sum()

# Get total missing values per column
print(df.isnull().sum())

# Calculate percentage of missing values
print((df.isnull().sum() / len(df)) * 100)