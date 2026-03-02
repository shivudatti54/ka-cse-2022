python
import pandas as pd

def normalize_series(s):
    """
    Normalizes a pandas Series to a 0-1 range using min-max scaling.
    Formula: (s - s.min()) / (s.max() - s.min())
    """
    if s.empty:
        raise ValueError("Series cannot be empty.")
    if s.max() == s.min():
        return pd.Series([0.5] * len(s)) # Handle case where all values are identical
    return (s - s.min()) / (s.max() - s.min())