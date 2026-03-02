python
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['alice cooper', 'BOB DYLAN', 'Charlie Brown', None, 'e.e. cummings'],
        'Email': ['alice@mail.com', 'bob.dylan@work.net', 'invalid_email', 'charlie@site.org', 'eec@domain.co']}
df = pd.DataFrame(data)
print(df)