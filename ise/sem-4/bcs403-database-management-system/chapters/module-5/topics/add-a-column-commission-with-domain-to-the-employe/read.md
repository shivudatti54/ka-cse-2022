# **Add a Column Commission with Domain to the Employee Table**

## **Introduction**

In this module, we will be learning about how to add a new column to an existing table in a database. Specifically, we will be adding a column called "Commission" to the "Employee" table. This column will have a domain that defines its data type and constraints.

## **What is a Domain?**

A domain is a set of values that a column can take on. It defines the data type and constraints of a column, such as its length, precision, and scale. Domains are used to enforce data integrity and consistency in a database.

## **Why Add a Commission Column to the Employee Table?**

Adding a commission column to the employee table can help us track the amount of commission an employee earns for each sale. This can be useful for calculating an employee's total earnings and for auditing sales data.

## **Step-by-Step Guide to Adding a Commission Column**

### Step 1: Identify the Existing Table and Column

Before we can add a new column to the employee table, we need to identify the existing table and column. In this case, we will be adding a new column called "Commission" to the "Employee" table.

### Step 2: Define the Domain for the Commission Column

To define the domain for the commission column, we need to decide on its data type and constraints. For example, we might decide that the commission column should be a decimal value with a maximum length of 10 digits. We can use the following SQL command to define the domain:

```sql
CREATE DOMAIN commission_domain AS DECIMAL(10, 2);
```

### Step 3: Add the Commission Column to the Employee Table

Once we have defined the domain for the commission column, we can add it to the employee table using the following SQL command:

```sql
ALTER TABLE employees ADD COLUMN commission commission_domain;
```

### Step 4: Populate the Commission Column

After adding the commission column to the employee table, we need to populate it with data. We can use the following SQL command to insert data into the commission column:

```sql
UPDATE employees SET commission = 0.10 * sales_amount;
```

## **Key Concepts**

- **Domain**: A set of values that a column can take on. Defines the data type and constraints of a column.
- **Decimal**: A numerical data type that can store decimal values.
- **ALTER TABLE**: A SQL command used to modify the structure of an existing table.
- **CREATE DOMAIN**: A SQL command used to define a domain for a column.
- **UPDATE**: A SQL command used to modify existing data in a table.

## **Example Use Cases**

- Tracking employee commission based on sales data
- Calculating employee earnings based on commission rates
- Auditing sales data to ensure accuracy and consistency

## **Best Practices**

- Define domains carefully to ensure data integrity and consistency
- Use meaningful and descriptive column names
- Use SQL commands to modify table structures and data
- Test and verify data after modifying tables or columns.
