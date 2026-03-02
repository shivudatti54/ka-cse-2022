python
import pandas as pd

# Create a sample DataFrame
data = {'Name': [' alice cooper  ', 'bOb Marley', 'Charlie Brown', 'diana@prince'],
        'Email': ['ALICE@.EDU', 'bob.marley@email.com', 'charlie.brown@.edu', None]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)