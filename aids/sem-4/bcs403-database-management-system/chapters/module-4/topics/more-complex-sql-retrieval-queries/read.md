sql
    SELECT Students.name, Grades.grade
    FROM Students
    INNER JOIN Grades ON Students.id = Grades.student_id;