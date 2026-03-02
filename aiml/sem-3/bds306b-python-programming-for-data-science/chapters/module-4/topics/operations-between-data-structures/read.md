python
    import pandas as pd
    import numpy as np

    # Create a DataFrame of scores
    df_scores = pd.DataFrame({
        'Math': [85, 70, 93],
        'Physics': [78, 82, 88],
        'Chemistry': [92, 75, 80]
    }, index=['Alice', 'Bob', 'Charlie'])  # Row index

    # Calculate the mean for each student (each row)
    mean_scores = df_scores.mean(axis=1)  # This creates a Series with student names as index
    print("Mean Scores:\n", mean_scores)

    # Subtract the mean from each subject (column) for each student (row)
    standardized_scores = df_scores.sub(mean_scores, axis='index')
    print("\nStandardized Scores (Score - Mean):\n", standardized_scores)