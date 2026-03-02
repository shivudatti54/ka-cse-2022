python
# Traditional Boolean Indexing (becomes messy)
filtered_df = df[(df['marks'] > 75) & (df['attendance'] > 80) & (df['department'] == 'CS')]

# Using query() (clean and readable)
filtered_df = df.query('marks > 75 and attendance > 80 and department == "CS"')