# **Database Management System**

**Module:** No. of Hours: 08
**Topic:** Add Primary Key Constraint and Not Null Constraint to the Employee Table

---

## **Introduction**

In this topic, we will explore the importance of primary key and not null constraints in a database. These constraints are essential in ensuring data integrity and preventing data anomalies. We will also discuss how to add these constraints to the employee table and provide examples and case studies to illustrate the concepts.

## **What is a Primary Key?**

A primary key is a unique identifier for each record in a table. It is a column or set of columns that uniquely identifies each row in a table. The primary key is used to establish the relationships between tables in a database.

## **Why do we need Primary Key?**

A primary key is necessary to:

- Prevent duplicate entries
- Identify each record uniquely
- Provide a unique identifier for each row
- Establish relationships between tables

## **What is a Not Null Constraint?**

A not null constraint is a constraint that specifies that a column cannot contain null values. Null values are used to indicate missing or unknown data.

## **Why do we need Not Null Constraint?**

A not null constraint is necessary to:

- Prevent null values from being entered in a column
- Ensure that each record has a valid value in a column
- Prevent errors caused by null values

## **Adding Primary Key Constraint to the Employee Table**

To add a primary key constraint to the employee table, we need to:

1.  Create a new column that will serve as the primary key.
2.  Define the primary key constraint on the new column.
3.  Ensure that the primary key column is unique and non-null.

Here is an example of how to add a primary key constraint to the employee table:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Department VARCHAR(50) NOT NULL
);
```

In the example above, the EmployeeID column is defined as the primary key and cannot contain null values.

## **Adding Not Null Constraint to the Employee Table**

To add a not null constraint to the employee table, we need to:

1.  Select the columns that require a not null constraint.
2.  Apply the not null constraint to the selected columns.

Here is an example of how to add a not null constraint to the employee table:

```sql
ALTER TABLE Employees
ADD CONSTRAINT NotNullFirstName CHECK (FirstName IS NOT NULL),
ADD CONSTRAINT NotNullLastName CHECK (LastName IS NOT NULL),
ADD CONSTRAINT NotNullEmail CHECK (Email IS NOT NULL);
```

In the example above, the FirstName, LastName, and Email columns are defined with a not null constraint.

## **Case Study: Employee Database**

Suppose we are working on an employee database that stores information about employees, including their names, addresses, and job titles. We need to design the database schema to ensure that each record is unique and has valid data.

Here is an example of how to design the database schema:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Department VARCHAR(50) NOT NULL
);

CREATE TABLE Addresses (
    AddressID INT PRIMARY KEY,
    Street VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL
);

CREATE TABLE JobTitles (
    JobTitleID INT PRIMARY KEY,
    JobTitle VARCHAR(50) NOT NULL
);

CREATE TABLE EmployeeAddresses (
    EmployeeID INT NOT NULL,
    AddressID INT NOT NULL,
    PRIMARY KEY (EmployeeID, AddressID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (AddressID) REFERENCES Addresses(AddressID)
);

CREATE TABLE EmployeeJobTitles (
    EmployeeID INT NOT NULL,
    JobTitleID INT NOT NULL,
    PRIMARY KEY (EmployeeID, JobTitleID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (JobTitleID) REFERENCES JobTitles(JobTitleID)
);
```

In the example above, we have defined the Employees, Addresses, JobTitles, EmployeeAddresses, and EmployeeJobTitles tables. We have also established relationships between the tables using foreign keys.

## **Application: Employee Payroll System**

An employee payroll system is a software application that manages employee salaries, deductions, and benefits. The system requires a database to store employee information and payroll data.

To design a database for an employee payroll system, we would need to:

1.  Define the employee table with columns for employee ID, name, address, and job title.
2.  Define the payroll table with columns for payroll ID, employee ID, salary, and deductions.
3.  Establish relationships between the tables using foreign keys.

Here is an example of how to design the database schema:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Department VARCHAR(50) NOT NULL
);

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY,
    EmployeeID INT NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    Deductions DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE TaxDeductions (
    TaxDeductionID INT PRIMARY KEY,
    PayrollID INT NOT NULL,
    TaxType VARCHAR(50) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (PayrollID) REFERENCES Payroll(PayrollID)
);
```

In the example above, we have defined the Employees, Payroll, and TaxDeductions tables. We have also established relationships between the tables using foreign keys.

## **Conclusion**

In this topic, we have explored the importance of primary key and not null constraints in a database. We have discussed how to add these constraints to the employee table and provided examples and case studies to illustrate the concepts. We have also discussed the application of these constraints in an employee database and payroll system.

## **Further Reading**

- "Database Systems: The Complete Book" by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- "Database Systems: A Practical Approach" by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- "Database Systems: Concepts and Software" by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- "Database Systems: The Complete Book" by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza (second edition)
- "Database Systems: A Practical Approach" by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza (second edition)
