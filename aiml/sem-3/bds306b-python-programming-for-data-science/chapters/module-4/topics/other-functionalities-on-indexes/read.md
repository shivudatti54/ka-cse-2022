python
    import pandas as pd

    # Create a sample DataFrame
    df = pd.DataFrame({
        'student_id': [101, 102, 103],
        'name': ['Alice', 'Bob', 'Charlie'],
        'grade': ['A', 'B', 'A+']
    })
    print("Original DataFrame:")
    print(df)

    # Set 'student_id' as the index
    df_indexed = df.set_index('student_id')
    print("\nDataFrame with 'student_id' as index:")
    print(df_indexed)