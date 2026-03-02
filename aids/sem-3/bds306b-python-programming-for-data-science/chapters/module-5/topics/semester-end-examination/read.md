python
        import pandas as pd
        df = pd.DataFrame({'Dept': ['IT', 'HR', 'IT', 'Sales'], 'Salary': [70000, 50000, 80000, 60000]})
        avg_salary = df.groupby('Dept')['Salary'].mean()
        print(avg_salary)