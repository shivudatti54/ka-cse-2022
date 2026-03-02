python
import pandas as pd
import numpy as np

# From a list (default integer index: 0, 1, 2...)
data_list = [10, 20, 30, 40]
s1 = pd.Series(data_list)
print(s1)
# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# From a dictionary (keys become the index)
data_dict = {'a': 10, 'b': 20, 'c': 30}
s2 = pd.Series(data_dict)
print(s2)
# Output:
# a    10
# b    20
# c    30
# dtype: int64