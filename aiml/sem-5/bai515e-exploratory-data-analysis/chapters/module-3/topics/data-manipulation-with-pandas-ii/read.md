python
# Fill missing values with the mean of the column
df.fillna(df.mean(), inplace=True)