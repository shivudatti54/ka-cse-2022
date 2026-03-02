python
import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40]
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)