python
import pandas as pd

# Read the first sheet of an Excel file
df = pd.read_excel('data.xlsx')
print(df.head())