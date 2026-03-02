# **Database Management System Study Material**

## **Topic:** Creating a Table in a Database

### Introduction

---

In this topic, we will learn how to create a table in a database. A table is a fundamental concept in database management systems, and it is used to store and manage data. In this study material, we will focus on creating a table called "Employee" that contains the attribute "EMPNO".

### What is a Table?

---

A table is a collection of related data that is organized into rows and columns. Each row represents a single record, and each column represents a field or attribute of that record. Tables are used to store and manage data in a database.

### Table Attributes

---

A table attribute, also known as a field or column, is a single column in a table that contains data. Each attribute has a unique name, and it is used to store a specific type of data. Attributes are used to define the characteristics of a table and to organize the data in a meaningful way.

### Creating a Table

---

To create a table, you need to define the attributes of the table and specify the data type of each attribute. The following steps outline the process of creating a table:

1. **Define the table name**: The table name is the name given to the table.
2. **Define the attributes**: Define the attributes of the table, including the name, data type, and any other relevant information.
3. **Specify the data type**: Specify the data type of each attribute, such as integer, string, or date.
4. **Create the table**: Create the table in the database using the defined attributes and data types.

### Creating the Employee Table

---

Let's create an example table called "Employee" that contains the attribute "EMPNO". The following is an example of how to create this table:

| Attribute | Data Type | Description            |
| --------- | --------- | ---------------------- |
| EMPNO     | Integer   | Unique employee number |
| EMPNAME   | String    | Employee name          |
| JOBTITLE  | String    | Employee job title     |
| DEPTNO    | Integer   | Department number      |

**SQL Code**

```sql
CREATE TABLE Employee (
  EMPNO Integer PRIMARY KEY,
  EMPNAME String NOT NULL,
  JOBTITLE String NOT NULL,
  DEPTNO Integer NOT NULL
);
```

**Explanation**

- The `CREATE TABLE` statement is used to create a new table in the database.
- The `Employee` table is defined with four attributes: `EMPNO`, `EMPNAME`, `JOBTITLE`, and `DEPTNO`.
- The `INTEGER PRIMARY KEY` constraint is used to define the `EMPNO` attribute as the primary key of the table.
- The `NOT NULL` constraint is used to ensure that the `EMPNAME`, `JOBTITLE`, and `DEPTNO` attributes cannot be null.

### Key Concepts

---

- **Table**: A collection of related data organized into rows and columns.
- **Attribute**: A single column in a table that contains data.
- **Data type**: The type of data that an attribute can store, such as integer, string, or date.
- **Primary key**: A unique attribute that identifies each record in a table.

### Best Practices

---

- **Use meaningful table and attribute names**: Use clear and descriptive names for tables and attributes to make it easier to understand the data.
- **Use data types consistently**: Use consistent data types for similar attributes to avoid confusion.
- **Include indexes**: Include indexes on frequently queried attributes to improve query performance.

### Conclusion

---

In this study material, we learned how to create a table in a database and the importance of attributes and data types in defining the characteristics of a table. We also covered key concepts and best practices for creating effective tables. By applying the concepts and techniques learned in this study material, you can create well-designed tables that efficiently store and manage data.
