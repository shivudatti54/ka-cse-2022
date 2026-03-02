python
import pandas as pd

# Define two Series with different but overlapping indices
series_a = pd.Series([10, 20, 30], index=['a', 'b', 'c']) # Indices: a, b, c
series_b = pd.Series([5, 15, 25], index=['b', 'c', 'd']) # Indices: b, c, d

result = series_a + series_b
print(result)
# a     NaN  (because 'a' is only in series_a)
# b    25.0  (20 + 5)
# c    45.0  (30 + 15)
# d     NaN  (because 'd' is only in series_b)
# dtype: float64