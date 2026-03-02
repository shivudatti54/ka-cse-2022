python
import pandas as pd

# Fetch and parse all tables from a Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
tables = pd.read_html(url)  # Returns a list of DataFrames

# The first table on the page is often the one we need
gdp_table = tables[0]
print(gdp_table.head())