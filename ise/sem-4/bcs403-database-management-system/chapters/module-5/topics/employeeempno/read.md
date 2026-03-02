# **Employee (EMPNO) Study Material**

## **Introduction**

In a database management system, an employee table is used to store information about employees in an organization. The EMPNO (Employee Number) field is a unique identifier for each employee and is used to track and manage employee data.

## **Definitions and Concepts**

- **EMPNO (Employee Number)**: A unique identifier assigned to each employee in the organization.
- **Primary Key**: A field or set of fields that uniquely identify each record in a table.
- **Foreign Key**: A field or set of fields that references the primary key of another table.

## **Employee Table Structure**

| Field Name  | Data Type      | Description                          |
| ----------- | -------------- | ------------------------------------ |
| EMPNO       | int            | Unique identifier for each employee  |
| EMPNAME     | varchar(50)    | Employee name                        |
| DEPARTMENT  | varchar(50)    | Department where the employee works  |
| SALARY      | decimal(10, 2) | Employee's salary                    |
| HIREDATE    | date           | Date when the employee was hired     |
| LASTPAYDATE | date           | Date when the employee was last paid |
| JOBTITLE    | varchar(50)    | Employee's job title                 |

## **Employee Table Relationships**

- **Primary Key**: EMPNO is the primary key of the employee table, uniquely identifying each employee.
- **Foreign Key**: There are no foreign keys in this table.

## **Key Concepts**

- **Normalization**: Normalization is the process of organizing data in a database to minimize data redundancy and dependency.
- **Denormalization**: Denormalization is the process of increasing data redundancy and dependency to improve query performance.
- **Indexing**: Indexing is the process of creating a data structure that improves query performance by allowing the database to quickly locate specific data.

## **Example Use Cases**

- **Employee Data Management**: The employee table is used to store information about employees in an organization, such as their name, department, salary, and hire date.
- **Salary Calculation**: The salary column is used to calculate employee salaries based on their job title and hire date.
- **Reporting and Analysis**: The employee table is used to generate reports and analyze employee data, such as employee turnover rates and salary trends.

## **SQL Queries**

- **SELECT**: `SELECT * FROM employee WHERE EMPNO = 'EMP001';` Retrieves all columns for an employee with EMPNO 'EMP001'.
- **INSERT**: `INSERT INTO employee (EMPNO, EMPNAME, DEPARTMENT, SALARY, HIREDATE, LASTPAYDATE, JOBTITLE) VALUES ('EMP002', 'John Doe', 'Sales', 50000.00, '2020-01-01', '2022-01-01', 'Sales Representative');` Inserts a new employee into the employee table.
- **UPDATE**: `UPDATE employee SET SALARY = 60000.00 WHERE EMPNO = 'EMP001';` Updates the salary of an employee with EMPNO 'EMP001'.
- **DELETE**: `DELETE FROM employee WHERE EMPNO = 'EMP002';` Deletes an employee with EMPNO 'EMP002'.
