sql
-- Find the name of the employee who has the highest salary.
SELECT ename FROM Emp
WHERE sal = (SELECT MAX(sal) FROM Emp);
