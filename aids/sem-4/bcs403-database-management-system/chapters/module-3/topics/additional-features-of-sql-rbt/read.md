sql
-- Find all unique student names across both departments
SELECT student_name FROM Students_CSE
UNION
SELECT student_name FROM Students_ECE;

-- Find students who are enrolled in both CSE and ECE (e.g., a double major)
SELECT student_name FROM Students_CSE
INTERSECT
SELECT student_name FROM Students_ECE;

-- Find students who are only in CSE, not in ECE
SELECT student_name FROM Students_CSE
EXCEPT
SELECT student_name FROM Students_ECE;