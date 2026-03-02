python
import pandas as pd

# Read all tables from a local HTML file
tables = pd.read_html('financial_report.html')

# The 'tables' variable is a list of DataFrames
print(f"Number of tables found: {len(tables)}")

# Access the first table
df = tables[0]
print(df.head())