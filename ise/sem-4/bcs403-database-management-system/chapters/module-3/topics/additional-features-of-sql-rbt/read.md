sql
-- Find all students who are either in the 'CSE' department OR have a CPI > 9.0
SELECT name FROM Students WHERE dept = 'CSE'
UNION
SELECT name FROM Students WHERE cpi > 9.0;
