python
    import pandas as pd

    # Creating a Series from a list
    student_marks = pd.Series([85, 92, 78, 90], index=['Alice', 'Bob', 'Charlie', 'Diana'])
    print(student_marks)
    # Output:
    # Alice       85
    # Bob         92
    # Charlie     78
    # Diana       90
    # dtype: int64