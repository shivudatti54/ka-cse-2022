# **DATABASE MANAGEMENT SYSTEM**

## **Module: Creating Tables**

### 2. Create a Table called Employee that contain attributes EMPNO

In this section, we will discuss the importance of creating a table in a database management system (DBMS) and how to design a table called Employee with the attribute EMPNO.

## **What is a Table?**

In a DBMS, a table is a collection of related data stored in rows and columns. Each column represents a field or attribute of the data, and each row represents a single record or entry. Tables are the fundamental structure of a database, and they serve as the basis for storing, managing, and retrieving data.

## **Designing a Table**

When designing a table, it is essential to consider the following factors:

- **Attributes**: What fields or columns do we need to store data in the table?
- **Data Types**: What type of data will be stored in each attribute?
- **Relationships**: How do the attributes relate to each other?
- **Constraints**: What rules or conditions must be met for data to be valid or consistent?

## **Creating a Table called Employee with attribute EMPNO**

In this example, we will create a table called Employee with the attribute EMPNO. The EMPNO attribute represents the employee number, which is a unique identifier for each employee.

## **Table Structure**

Here is an example of the table structure for the Employee table:

| Column Name | Data Type     | Description                         |
| ----------- | ------------- | ----------------------------------- |
| EMPNO       | INT           | Employee Number (unique identifier) |
| NAME        | VARCHAR(50)   | Employee Name                       |
| DEPARTMENT  | VARCHAR(50)   | Department of Employment            |
| SALARY      | DECIMAL(10,2) | Employee Salary                     |
| HIRE_DATE   | DATE          | Date of Hire                        |

## **Explanation of Attributes**

- **EMPNO**: The EMPNO attribute represents the employee number, which is a unique identifier for each employee. The data type for EMPNO is INT, which means it can store integer values.
- **NAME**: The NAME attribute represents the employee name. The data type for NAME is VARCHAR(50), which means it can store strings of up to 50 characters.
- **DEPARTMENT**: The DEPARTMENT attribute represents the department of employment. The data type for DEPARTMENT is VARCHAR(50), which means it can store strings of up to 50 characters.
- **SALARY**: The SALARY attribute represents the employee salary. The data type for SALARY is DECIMAL(10,2), which means it can store decimal values with a maximum of 10 digits and 2 decimal places.
- **HIRE_DATE**: The HIRE_DATE attribute represents the date of hire. The data type for HIRE_DATE is DATE, which means it can store dates.

## **Constraints**

To ensure data consistency and integrity, we need to define constraints for the table. In this example, we need to define the following constraints:

- **Primary Key**: The EMPNO attribute must be a primary key, which means it must be unique and not null.
- **Unique Constraint**: The NAME attribute must be unique, which means no two employees can have the same name.

## **SQL Code**

Here is an example of the SQL code to create the Employee table with the specified attributes and constraints:

```sql
CREATE TABLE Employee (
  EMPNO INT PRIMARY KEY,
  NAME VARCHAR(50) NOT NULL UNIQUE,
  DEPARTMENT VARCHAR(50),
  SALARY DECIMAL(10,2),
  HIRE_DATE DATE
);
```

## **Further Reading**

- [Database Management Systems](https://en.wikipedia.org/wiki/Database_management_system)
- [SQL Tutorial](https://www.w3schools.com/sql/sql_intro.asp)
- [Database Design Principles](https://www.tutorialspoint.com/database_design/database_design_principles.htm)

## **Case Study**

Suppose we want to create an Employee Management System that allows users to create, read, update, and delete employee records. We can use the Employee table we created earlier as the foundation for our system.

Here is an example of how we can design the system:

- **User Interface**: Create a user interface that allows users to interact with the system, such as a web application or a desktop application.
- **Database Connection**: Establish a connection to the database and create a query to retrieve employee data.
- ** CRUD Operations**: Implement create, read, update, and delete operations to manage employee data.

## **Applications**

The Employee table and the DBMS concepts discussed in this topic have numerous applications in various industries, including:

- **Human Resources**: Employee management systems are essential for human resources departments to manage employee data and perform tasks such as payroll, benefits, and performance evaluations.
- **HRIS Systems**: Human Resource Information Systems (HRIS) are used to manage employee data and perform tasks such as payroll, benefits, and performance evaluations.
- **Database Administration**: Database administrators use DBMS concepts to design, implement, and maintain databases for various applications.

In conclusion, creating a table called Employee with the attribute EMPNO is an essential part of database management system design. By understanding the attributes, data types, relationships, and constraints, we can design a table that meets the needs of our application and ensures data consistency and integrity.
