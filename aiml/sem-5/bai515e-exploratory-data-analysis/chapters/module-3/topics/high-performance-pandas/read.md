python
# Check current memory usage
df.info(memory_usage='deep')

# Optimize a specific column
df['department'] = df['department'].astype('category') # From 'object' to 'category'

# Optimize all numeric columns
df_int = df.select_dtypes(include=['int64'])
converted_int = df_int.apply(pd.to_numeric, downcast='integer')
df_float = df.select_dtypes(include=['float64'])
converted_float = df_float.apply(pd.to_numeric, downcast='float')

# Replace original columns with optimized ones
df[converted_int.columns] = converted_int
df[converted_float.columns] = converted_float

# Check memory usage after optimization
df.info(memory_usage='deep')