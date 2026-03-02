sql
    -- Find all cities where either a student or a professor lives
    SELECT city FROM Student
    UNION
    SELECT city FROM Professor;