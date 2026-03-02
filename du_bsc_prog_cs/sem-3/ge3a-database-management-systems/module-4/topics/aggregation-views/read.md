# Aggregation Views: Comprehensive Study Material

## Database Management Systems (Ge3A) — BSc Physical Science (CS), Delhi University

---

## 1. Introduction

In the modern era of data-driven decision making, organizations generate massive amounts of data stored in relational databases. However, querying raw transactional data for analytical purposes can be extremely inefficient, especially when calculations involve thousands or millions of rows. **Aggregation Views** provide an elegant solution to this problem by pre-computing and storing summarized data, making complex analytical queries execute faster and more efficiently.

### What Are Aggregation Views?

An **Aggregation View** (also known as a summarized or materialized view in some contexts) is a virtual table defined by a SQL query that performs aggregate functions such as `SUM()`, `AVG()`, `COUNT()`, `MAX()`, and `MIN()` on one or more base tables. Unlike regular views that simply store query definitions, aggregation views can either store the computed results (materialized) or compute results on-the-fly when queried (virtual).

### Real-World Relevance

Consider a retail chain like **Reliance Fresh** or **Big Bazaar** with thousands of transactions daily. A manager wanting to know total sales for the current month would need to scan millions of transaction records if querying the raw `sales` table directly. With an aggregation view pre-computing monthly sales figures, this query returns instantly—demonstrating the critical importance of aggregation views in business intelligence and reporting systems.

For Delhi University students, understanding aggregation views is essential because:
- They are a fundamental concept in database management systems
- They frequently appear in university examinations
- They are extensively used in industry for reporting and analytics
- They demonstrate advanced SQL querying skills

---

## 2. Understanding Database Views

Before diving into aggregation views, let's establish the foundation with regular database views.

### 2.1 What is a View?

A **View** is a virtual table based on the result set of a SQL query. It does not store data physically but references data from one or more base tables. Views provide:

- **Data abstraction**: Simplify complex queries
- **Security**: Restrict access to specific columns or rows
- **Logical data independence**: Applications remain unaffected by table structure changes

### 2.2 Types of Views

| Type | Description | Data Storage |
|------|-------------|--------------|
| Simple View | Derived from single table, no aggregate functions | Not stored |
| Complex View | Derived from multiple tables with aggregates | Not stored |
| Materialized View | Stores physical copy of query results | Physically stored |

---

## 3. Aggregation Views: Deep Dive

### 3.1 Definition

An **Aggregation View** is a database object that defines a query containing one or more aggregate functions (`GROUP BY`, `HAVING`, etc.) to compute and present summarized data from one or more base tables.

### 3.2 Key Characteristics

1. **Pre-computation**: Aggregations are computed either at view creation time or query time
2. **Virtual Nature**: Most aggregation views (non-materialized) do not store data physically
3. **Dynamic Results**: Always reflect current data in base tables
4. **Query Simplification**: Complex aggregation queries become simple `SELECT *` operations

### 3.3 Components of an Aggregation View

```sql
CREATE VIEW view_name AS
SELECT 
    column1,
    column2,
    aggregate_function(column3) AS alias_name
FROM 
    table_name
WHERE 
    condition
GROUP BY 
    column1, column2
HAVING 
    condition;
```

**Key Components:**
- **SELECT clause**: Contains aggregate functions
- **GROUP BY clause**: Defines how data is grouped
- **HAVING clause**: Filters grouped data
- **WHERE clause**: Filters rows before aggregation

---

## 4. Why Use Aggregation Views?

### 4.1 Performance Benefits

- **Reduced Query Execution Time**: Pre-computed aggregations eliminate repetitive calculations
- **Lower I/O Operations**: Fewer rows need to be scanned
- **Optimized Resource Usage**: Less CPU and memory consumption

### 4.2 Development Benefits

- **Simplified Application Code**: Complex queries replaced by simple view queries
- **Reusability**: Same aggregation logic used across multiple reports
- **Maintainability**: Changes needed in one place (the view)

### 4.3 Business Benefits

- **Faster Decision Making**: Real-time access to summarized data
- **Consistent Reporting**: Everyone uses the same aggregation logic
- **Support for Analytics**: Enable business intelligence applications

---

## 5. Creating Aggregation Views: SQL Syntax and Examples

### 5.1 Basic Syntax

```sql
CREATE [OR REPLACE] VIEW view_name AS
SELECT 
    [DISTINCT] column_list
    aggregate_function(column) AS new_column
FROM 
    table_name
[WHERE conditions]
[GROUP BY group_columns]
[HAVING group_conditions];
```

### 5.2 Example 1: Sales Summary View

Consider a **Sales Management System** for a company. We have the following base tables:

```sql
-- Base Table: sales
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    quantity INT,
    unit_price DECIMAL(10,2),
    region VARCHAR(50)
);

-- Sample Data
INSERT INTO sales VALUES 
(1, 101, '2024-01-15', 10, 500.00, 'North'),
(2, 102, '2024-01-16', 5, 1200.00, 'South'),
(3, 101, '2024-01-17', 8, 500.00, 'North'),
(4, 103, '2024-01-18', 15, 250.00, 'East'),
(5, 102, '2024-01-19', 3, 1200.00, 'West'),
(6, 101, '2024-02-10', 12, 550.00, 'North');
```

**Creating an Aggregation View for Monthly Sales by Product:**

```sql
-- Aggregation View 1: Monthly Product Sales Summary
CREATE VIEW monthly_product_sales AS
SELECT 
    EXTRACT(YEAR FROM sale_date) AS year,
    EXTRACT(MONTH FROM sale_date) AS month,
    product_id,
    SUM(quantity * unit_price) AS total_revenue,
    SUM(quantity) AS total_quantity,
    COUNT(*) AS transaction_count,
    AVG(quantity * unit_price) AS avg_transaction_value
FROM 
    sales
GROUP BY 
    EXTRACT(YEAR FROM sale_date),
    EXTRACT(MONTH FROM sale_date),
    product_id
ORDER BY 
    year, month, product_id;
```

**Querying the View:**

```sql
-- Get sales summary for January 2024
SELECT * FROM monthly_product_sales 
WHERE year = 2024 AND month = 1;
```

**Result:**

| year | month | product_id | total_revenue | total_quantity | transaction_count | avg_transaction_value |
|------|-------|------------|---------------|----------------|-------------------|----------------------|
| 2024 | 1     | 101        | 9000.00       | 18             | 2                 | 4500.00              |
| 2024 | 1     | 102        | 6000.00       | 5              | 1                 | 6000.00              |
| 2024 | 1     | 103        | 3750.00       | 15             | 1                 | 3750.00              |

### 5.3 Example 2: Employee Performance Aggregation View

For a **Human Resources Management System**:

```sql
-- Base Table: employees
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

-- Base Table: performance_records
CREATE TABLE performance_records (
    record_id INT PRIMARY KEY,
    emp_id INT,
    review_date DATE,
    performance_score DECIMAL(5,2),
    bonus_amount DECIMAL(10,2)
);

-- Aggregation View: Department-wise Employee Statistics
CREATE VIEW dept_employee_stats AS
SELECT 
    e.department,
    COUNT(e.emp_id) AS total_employees,
    AVG(e.salary) AS avg_salary,
    MIN(e.salary) AS min_salary,
    MAX(e.salary) AS max_salary,
    SUM(e.salary) AS total_salary_expense,
    AVG(p.performance_score) AS avg_performance,
    SUM(p.bonus_amount) AS total_bonus_paid
FROM 
    employees e
LEFT JOIN 
    performance_records p ON e.emp_id = p.emp_id
GROUP BY 
    e.department
ORDER BY 
    e.department;
```

**Querying the View:**

```sql
-- Get department with highest average performance
SELECT department, avg_performance 
FROM dept_employee_stats 
ORDER BY avg_performance DESC 
LIMIT 1;
```

---

## 6. Materialized vs Virtual Aggregation Views

### 6.1 Virtual Aggregation Views (Non-Materialized)

- Query is executed each time the view is accessed
- Always returns current data from base tables
- No storage overhead
- Suitable when base data changes frequently

### 6.2 Materialized Aggregation Views

- Stores physical copy of aggregated results
- Requires refresh mechanism to update data
- Provides extremely fast query performance
- Suitable for data that doesn't change in real-time

**Note for Delhi University Students:** Most academic databases (MySQL, PostgreSQL) implement virtual views. Materialized views are an advanced feature available in Oracle, SQL Server, and some PostgreSQL extensions.

---

## 7. Implementation Details

### 7.1 How DBMS Processes Aggregation Views

When a query is executed against an aggregation view, the Database Management System:

1. **Parses the View Query**: Breaks down the aggregation view definition
2. **Optimizes the Query**: Uses query optimization techniques
3. **Executes Aggregations**: Computes SUM, COUNT, AVG, etc.
4. **Returns Results**: Presents the aggregated data

### 7.2 View Maintenance

**Automatic Maintenance**: Most modern DBMS systems automatically maintain views when base table data changes.

**Refresh Options for Materialized Views:**
- `ON DEMAND`: Manually refreshed when needed
- `ON COMMIT`: Automatically refreshed when base table changes
- `ON SCHEDULE`: Refreshed at specified intervals

### 7.3 Query Optimization

Database optimizers can:
- Recognize when a view query matches the aggregation view definition
- Rewrite user queries to use the pre-computed aggregation
- Combine multiple table joins with aggregations efficiently

---

## 8. Updating Aggregation Views

### 8.1 Updatable Aggregation Views

Aggregation views are generally **not directly updatable** because:
- Multiple rows are aggregated into single results
- Aggregate functions lose information about individual rows
- Updates would be ambiguous

### 8.2 Workaround: INSTEAD OF Triggers

```sql
-- Create an updatable view
CREATE VIEW product_sales_summary AS
SELECT 
    product_id,
    SUM(quantity) AS total_sold,
    MAX(sale_date) AS last_sale_date
FROM 
    sales
GROUP BY 
    product_id;

-- Create INSTEAD OF trigger for INSERT
CREATE OR REPLACE TRIGGER ins_product_sales
INSTEAD OF INSERT ON product_sales_summary
FOR EACH ROW
BEGIN
    INSERT INTO sales (product_id, quantity, sale_date)
    VALUES (:NEW.product_id, :NEW.total_sold, :NEW.last_sale_date);
END;
```

---

## 9. Practical Use Cases

### 9.1 E-Commerce Applications

- **Daily Sales Summary**: Pre-computed daily revenue, orders, customers
- **Product Category Analytics**: Sales by category, region, time period
- **Customer Lifetime Value**: Aggregated purchase history

### 9.2 Banking Systems

- **Account Balance Summaries**: Total deposits, withdrawals, interest
- **Branch Performance**: Transactions per branch, customer counts
- **Loan Analytics**: Approved loans, default rates by category

### 9.3 Educational Institutions (DU Context)

- **Student Performance**: Average marks per course, pass rates
- **Attendance Summaries**: Present/absent counts by class
- **Fee Collection**: Monthly collection reports by department

---

## 10. Limitations and Considerations

1. **Storage Overhead**: Materialized views consume disk space
2. **Refresh Latency**: Data may be stale between refreshes
3. **Not Always Updatable**: Complex aggregations cannot be directly updated
4. **Performance Trade-offs**: View maintenance adds write overhead
5. **Query Complexity**: Some aggregations cannot be expressed in views

---

## 11. Key Takeaways

1. **Aggregation Views** are virtual tables that store query definitions with aggregate functions (SUM, AVG, COUNT, MAX, MIN)

2. They **simplify complex queries** by pre-computing aggregations and presenting them as simple SELECT statements

3. **Performance benefits** include reduced query execution time, lower I/O operations, and optimized resource usage

4. **Two main types**: Virtual (non-materialized) views compute results on-the-fly, while Materialized views store physical copies

5. Aggregation views use **GROUP BY** clause to organize data and can include **HAVING** for filtered aggregations

6. They are **not directly updatable**; INSTEAD OF triggers can be used for write operations

7. Common in **business intelligence**, reporting systems, and analytical applications

8. Essential for **Delhi University examinations** - understand both syntax and practical implementation

---

## 12. Assessment Items

### Multiple Choice Questions (MCQs)

**Question 1:** What is an aggregation view?
- (a) A physical table storing aggregated data
- (b) A virtual table defined by a query containing aggregate functions
- (c) A temporary table created during query execution
- (d) A backup of the database

**Question 2:** Which of the following aggregate functions can be used in an aggregation view?
- (a) SUM() and AVG()
- (b) CONCAT() and SUBSTRING()
- (c) UPPER() and LOWER()
- (d) Both (a) and (c)

**Question 3:** What is the main advantage of using aggregation views?
- (a) They consume less storage space
- (b) They simplify complex queries and improve performance
- (c) They allow direct updates to base tables
- (d) They automatically create indexes

**Question 4:** In an aggregation view, which clause is essential for grouping aggregated data?
- (a) WHERE
- (b) GROUP BY
- (c) ORDER BY
- (d) HAVING

**Question 5:** What is the difference between a virtual view and a materialized view?
- (a) Virtual views are faster than materialized views
- (b) Materialized views store physical data while virtual views do not
- (c) Virtual views can be updated directly, materialized views cannot
- (d) There is no difference

**Question 6:** Which of the following is TRUE about aggregation views?
- (a) They always store data physically
- (b) They cannot contain WHERE clauses
- (c) They always reflect current data in base tables
- (d) They cannot be queried using SELECT

**Question 7:** What does the COUNT(*) aggregate function return?
- (a) Sum of all values in a column
- (b) Average of all values in a column
- (c) Number of rows in a group
- (d) Maximum value in a column

**Question 8:** Which trigger is used to make an aggregation view updatable?
- (a) BEFORE trigger
- (b) AFTER trigger
- (c) INSTEAD OF trigger
- (d) FOR EACH ROW trigger

**Question 9:** In a university database, which of the following would be suitable for an aggregation view?
- (a) Student login history
- (b) Total marks obtained by each student per semester
- (c) Individual student fee transactions
- (d) Raw examination answers

**Question 10:** What happens when you query a virtual aggregation view?
- (a) It returns pre-stored results
- (b) It executes the underlying query each time
- (c) It returns an error
- (d) It returns cached results from last week

---

### Flashcards

**Flashcard 1:**
> **Term:** Aggregation View
> **Definition:** A virtual table defined by a SQL query that contains aggregate functions (SUM, AVG, COUNT, MAX, MIN) to compute summarized data from one or more base tables.

**Flashcard 2:**
> **Term:** GROUP BY Clause
> **Definition:** A SQL clause that groups rows with the same values into summary rows, essential for creating aggregation views.

**Flashcard 3:**
> **Term:** Materialized View
> **Definition:** A database object that stores the physical results of a query, providing fast access but requiring refresh to update data.

**Flashcard 4:**
> **Term:** Virtual View
> **Definition:** A view that does not store data physically; the query is executed each time the view is accessed, always returning current data.

**Flashcard 5:**
> **Term:** HAVING Clause
> **Definition:** A SQL clause that filters groups after the GROUP BY aggregation, similar to WHERE but for grouped data.

**Flashcard 6:**
> **Term:** INSTEAD OF Trigger
> **Definition:** A trigger defined on a view that allows INSERT, UPDATE, or DELETE operations by intercepting the operation and executing custom logic.

**Flashcard 7:**
> **Term:** Aggregate Function
> **Definition:** A function that performs a calculation on a set of values and returns a single value; examples include SUM, AVG, COUNT, MAX, MIN.

**Flashcard 8:**
> **Term:** Query Rewrite Optimization
> **Definition:** A database optimization technique where the query optimizer automatically redirects queries to use existing aggregation views for better performance.

**Flashcard 9:**
> **Term:** Base Table
> **Definition:** The original table in a database from which an aggregation view derives its data through a query.

**Flashcard 10:**
> **Term:** View Maintenance
> **Definition:** The process of keeping views synchronized with base table data; automatic in virtual views, requires explicit refresh in materialized views.

---

## References and Further Reading

1. **Delhi University Syllabus (NEP 2024)**: Ge3A Database Management Systems - Unit III: Advanced SQL and Database Objects
2. **Textbook**: "Database System Concepts" by Silberschatz, Korth, Sudarshan
3. **Reference**: "SQL Fundamentals" by Date, C.J.
4. **Practice**: MySQL, PostgreSQL, and Oracle documentation on Views

---

*This study material is designed specifically for BSc Physical Science (CS) students at Delhi University under NEP 2024, covering all essential concepts of Aggregation Views with practical examples and comprehensive assessment items.*