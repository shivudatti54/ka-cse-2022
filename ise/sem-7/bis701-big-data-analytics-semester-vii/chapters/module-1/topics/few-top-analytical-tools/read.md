sql
SELECT department, AVG(salary)
FROM employee_data
GROUP BY department;