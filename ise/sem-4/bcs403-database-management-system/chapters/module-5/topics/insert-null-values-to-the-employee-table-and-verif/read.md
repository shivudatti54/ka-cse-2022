# **Insert Null Values to the Employee Table and Verify the Result**

## **Introduction**

In a database management system, null values are used to represent missing or unknown data. In this topic, we will learn how to insert null values into the employee table and verify the result.

## **What are Null Values?**

- Null values are represented by a special symbol (NULL) in a database.
- Null values indicate that a particular field or attribute does not contain any valid data.
- Null values are used to represent missing or unknown data.

## **Types of Null Values**

- **Not Null**: This type of null value is used to indicate that a field or attribute cannot contain null values.
- **Nullable**: This type of null value is used to indicate that a field or attribute can contain null values.
- **Defined**: This type of null value is used to indicate that a field or attribute has a specific value assigned to it, even if it is null.

## **Inserting Null Values into the Employee Table**

### Using the INSERT Statement

To insert null values into the employee table, we can use the following SQL statement:

```sql
INSERT INTO employee (name, age, salary)
VALUES ('John Doe', NULL, NULL);
```

In this statement, we are inserting a new record into the employee table with null values for the name and age fields, and a null value for the salary field.

### Using the SET NULL Statement

Alternatively, we can use the SET NULL statement to insert null values into the employee table:

```sql
SET employee.name = NULL;
SET employee.age = NULL;
SET employee.salary = NULL;
```

This statement sets the values of the name, age, and salary fields to null.

## **Verifying the Result**

To verify the result of inserting null values into the employee table, we can use the following SQL statement:

```sql
SELECT * FROM employee;
```

This statement returns all the records in the employee table, including the null values we inserted earlier.

## **Example Use Case**

Suppose we have an employee table with the following columns: name, age, salary, and department. We want to insert a new record for an employee named John Doe who is 25 years old and earns a salary of $50000 per year. However, we are not sure what department John works in. In this case, we can insert the following null values:

```sql
INSERT INTO employee (name, age, salary, department)
VALUES ('John Doe', 25, 50000, NULL);
```

This statement inserts a new record into the employee table with null values for the department field.

## **Best Practices**

- Use the SET NULL statement instead of the INSERT statement to insert null values into the employee table.
- Use the NOT NULL constraint to specify that a field or attribute cannot contain null values.
- Use the NULL data type to indicate that a field or attribute can contain null values.

## **Conclusion**

In this topic, we learned how to insert null values into the employee table and verify the result. We also discussed the different types of null values, including not null, nullable, and defined null values. Additionally, we provided best practices for inserting null values into the employee table.
