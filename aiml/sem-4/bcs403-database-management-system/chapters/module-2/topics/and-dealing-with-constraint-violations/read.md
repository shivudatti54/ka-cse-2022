sql
    CREATE TABLE Students (
        student_id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL -- 'name' cannot be NULL
    );

    -- This will cause a NOT NULL constraint violation:
    INSERT INTO Students (student_id) VALUES (101);