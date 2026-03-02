# Examples of Dimensional Modelling

## Introduction

Dimensional modelling is the foundation of data warehouse design, transforming complex business requirements into structured, query-optimized databases. This topic provides comprehensive worked examples that demonstrate how to apply dimensional modelling principles to real-world business scenarios. Through these examples, you will learn how to translate business questions into fact and dimension tables, design effective star schemas, and create meaningful analysis structures that support business intelligence operations.

Understanding dimensional modelling through practical examples is essential for anyone designing data warehouses or business intelligence systems. The examples in this section progress from simple scenarios to more complex implementations, helping you build confidence in applying these techniques to any business domain. Each example includes detailed step-by-step reasoning, showing exactly how business requirements translate into physical database designs.

## Key Concepts

### Example 1: Retail Sales Analysis System

Consider a retail chain that wants to analyze daily sales transactions across multiple stores. The business stakeholders need to answer questions like: "What was the total revenue by product category last month?" or "Which store performed best in the last quarter?"

**Step 1: Identify the Business Process**

The core business process is the retail sales transaction. Each sale represents a measurable event that the business wants to analyze.

**Step 2: Identify the Grain**

The grain (granularity) of the fact table is individual sales transaction line items. This means each row in the fact table represents one product sold in one transaction at one store at a specific time.

**Step 3: Identify Dimensions**

From the business requirements, we identify the following dimensions:

- Product Dimension: Contains product information including SKU, name, category, subcategory, brand, and unit price
- Store Dimension: Contains store information including store ID, name, address, city, region, and store type
- Date Dimension: Contains date attributes including date, day of week, month, quarter, year, and holiday indicators
- Customer Dimension: Contains customer information including customer ID, name, segment, and demographics

**Step 4: Identify Facts**

The measurable metrics (facts) for this process include:

- Sales Amount: The total revenue from the sale (quantity × unit price)
- Quantity Sold: Number of units sold
- Cost: The cost of goods sold
- Discount Amount: Any discount applied

**Step 5: Design the Star Schema**

The resulting star schema has one fact table (fact_sales) surrounded by four dimension tables. The fact table contains foreign keys to each dimension table along with the fact columns.

```
fact_sales
----------
sale_key (PK)
date_key (FK) → dim_date
product_key (FK) → dim_product
store_key (FK) → dim_store
customer_key (FK) → dim_customer
sales_amount DECIMAL(10,2)
quantity_sold INTEGER
cost_amount DECIMAL(10,2)
discount_amount DECIMAL(10,2)

dim_product
-----------
product_key (PK)
product_sku VARCHAR(20)
product_name VARCHAR(100)
category VARCHAR(50)
subcategory VARCHAR(50)
brand VARCHAR(50)
unit_price DECIMAL(10,2)

dim_store
---------
store_key (PK)
store_id INTEGER
store_name VARCHAR(100)
address VARCHAR(200)
city VARCHAR(50)
region VARCHAR(50)
store_type VARCHAR(20)

dim_date
--------
date_key (PK) - format YYYYMMDD
full_date DATE
day_of_week INTEGER
day_name VARCHAR(10)
month INTEGER
month_name VARCHAR(10)
quarter INTEGER
year INTEGER
is_holiday BOOLEAN
is_weekend BOOLEAN

dim_customer
------------
customer_key (PK)
customer_id INTEGER
customer_name VARCHAR(100)
customer_segment VARCHAR(20)
city VARCHAR(50)
state VARCHAR(50)
```

### Example 2: Library Book Lending System

A university library wants to track book borrowing patterns to understand usage and optimize inventory management.

**Business Process:** Book lending/borrowing transactions

**Grain:** Individual book checkout record

**Dimensions:** Book, Member (student/faculty), Date, Library Branch

**Facts:** Number of books borrowed, days overdue, late fees collected

**Star Schema Design:**

```
fact_book_lending
-----------------
lending_key (PK)
date_key (FK) → dim_date
book_key (FK) → dim_book
member_key (FK) → dim_member
branch_key (FK) → dim_branch
borrow_date DATE
return_date DATE
due_date DATE
days_borrowed INTEGER
is_returned BOOLEAN
late_fee DECIMAL(8,2)

dim_book
--------
book_key (PK)
isbn VARCHAR(13)
title VARCHAR(200)
author VARCHAR(100)
genre VARCHAR(50)
publisher VARCHAR(100)
publication_year INTEGER
category VARCHAR(50)

dim_member
----------
member_key (PK)
member_id VARCHAR(20)
member_name VARCHAR(100)
member_type VARCHAR(20) -- Student/Faculty/Staff
department VARCHAR(50)
enrollment_year INTEGER

dim_branch
----------
branch_key (PK)
branch_id INTEGER
branch_name VARCHAR(100)
location VARCHAR(100)
branch_type VARCHAR(20)
```

### Example 3: Healthcare Patient Visits

A hospital network wants to analyze patient visit patterns and billing information.

**Business Process:** Patient visits to hospital facilities

**Grain:** Individual patient visit per department per day

**Dimensions:** Patient, Date, Hospital/Department, Physician, Insurance

**Facts:** Visit duration, billing amount, tests ordered, medications prescribed

```
fact_patient_visits
--------------------
visit_key (PK)
visit_date_key (FK) → dim_date
patient_key (FK) → dim_patient
hospital_key (FK) → dim_hospital
department_key (FK) → dim_department
physician_key (FK) → dim_physician
insurance_key (FK) → dim_insurance
visit_duration_minutes INTEGER
billing_amount DECIMAL(12,2)
tests_ordered INTEGER
medications_prescribed INTEGER
admission_type VARCHAR(20) -- Emergency/Scheduled/Transfer
```

### Handling Slow Changing Dimensions (SCD)

In Example 1 (Retail Sales), what happens when a product's category changes or a store's region is reorganized? This demonstrates the importance of SCD handling.

**Type 1 (Overwrite):** Simply update the existing dimension record. Historical analysis shows the new value for all historical records. Suitable when historical accuracy is not critical.

**Type 2 (Add New Row):** Create a new dimension record with a new surrogate key and effective dates. This preserves full history but increases table size.

**Example of Type 2 Implementation:**

```
dim_product (with SCD Type 2)
-----------------------------
product_key (PK)
product_sku VARCHAR(20)
product_name VARCHAR(100)
category VARCHAR(50)
effective_start_date DATE
effective_end_date DATE
is_current BOOLEAN
version_number INTEGER
```

When the category for "Product A" changes from "Electronics" to "Computers" on March 15, 2024, a new row is inserted with updated category, and the previous row's effective_end_date is updated to March 14, 2024, and is_current is set to FALSE.

## Examples

### Worked Example 1: Creating a Date Dimension

The date dimension is unique because it exists in every data warehouse and is essential for time-based analysis.

**Requirement:** Create a date dimension for a sales data warehouse covering 2020-2025.

**Solution:**

```sql
-- Generate date dimension data
DECLARE @StartDate DATE = '2020-01-01';
DECLARE @EndDate DATE = '2025-12-31';

WITH DateSequence AS (
    SELECT @StartDate AS DateValue
    UNION ALL
    SELECT DATEADD(DAY, 1, DateValue)
    FROM DateSequence
    WHERE DateValue < @EndDate
)
SELECT 
    CAST(FORMAT(DateValue, 'yyyyMMdd') AS INTEGER) AS date_key,
    DateValue AS full_date,
    DATEPART(DAY, DateValue) AS day_of_month,
    DATEPART(WEEKDAY, DateValue) AS day_of_week,
    DATENAME(WEEKDAY, DateValue) AS day_name,
    DATEPART(MONTH, DateValue) AS month,
    DATENAME(MONTH, DateValue) AS month_name,
    DATEPART(QUARTER, DateValue) AS quarter,
    DATEPART(YEAR, DateValue) AS year,
    CASE WHEN DATEPART(MONTH, DateValue) IN (4, 6, 9, 11) THEN 30
         WHEN DATEPART(MONTH, DateValue) = 2 THEN 
             CASE WHEN (DATEPART(YEAR, DateValue) % 4 = 0 AND 
                       DATEPART(YEAR, DateValue) % 100 <> 0) OR 
                       DATEPART(YEAR, DateValue) % 400 = 0 THEN 29 ELSE 28 END
         ELSE 31 END AS days_in_month,
    CASE WHEN DATENAME(WEEKDAY, DateValue) IN ('Saturday', 'Sunday') 
         THEN 1 ELSE 0 END AS is_weekend
FROM DateSequence
OPTION (MAXRECURSION 2000);
```

### Worked Example 2: Querying the Star Schema

Using Example 1 (Retail Sales), answer: "Show quarterly sales by store region and product category for the current year."

```sql
SELECT 
    d.year,
    d.quarter,
    st.region AS store_region,
    p.category AS product_category,
    SUM(f.sales_amount) AS total_sales,
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
JOIN dim_store st ON f.store_key = st.store_key
JOIN dim_product p ON f.product_key = p.product_key
WHERE d.year = YEAR(GETDATE())
GROUP BY d.year, d.quarter, st.region, p.category
ORDER BY d.year, d.quarter, st.region, p.category;
```

This query demonstrates how the star schema enables simple joins between fact and dimension tables, making complex analytical queries straightforward to write and efficient to execute.

### Worked Example 3: Converting to Snowflake Schema

From Example 1, normalize the product dimension to third normal form:

```
dim_product (now normalized)
--------------------------
product_key (PK)
product_sku VARCHAR(20)
product_name VARCHAR(100)
brand_key (FK) → dim_brand
category_key (FK) → dim_category

dim_brand
---------
brand_key (PK)
brand_name VARCHAR(50)
brand_manufacturer VARCHAR(100)

dim_category
------------
category_key (PK)
category_name VARCHAR(50)
category_department VARCHAR(50)
```

This snowflake schema reduces data redundancy but increases query complexity. The choice between star and snowflake depends on your specific requirements for storage efficiency versus query simplicity.

## Exam Tips

1. ALWAYS identify the business process first before designing any dimensional model. The grain must be clearly defined before dimension selection.

2. REMEMBER that fact tables contain measurable business metrics (facts) while dimension tables contain descriptive attributes for filtering and grouping.

3. SURROGATE KEYS are mandatory in dimension tables - never use natural keys as primary keys in dimensional models.

4. The DATE DIMENSION is the most important and universal dimension - every data warehouse needs one regardless of the business domain.

5. For exam questions requiring star schema design, always start by identifying: What happened? (Fact), When? (Date dimension), Where? (Location dimension), Who? (Customer/Person dimension), What product/item? (Product dimension).

6. SLOWLY CHANGING DIMENSIONS (SCD) are frequently tested. Know the differences between Type 1 (overwrite), Type 2 (add row), and Type 3 (add column) with clear use cases for each.

7. The STAR SCHEMA is preferred over snowflake for reporting because it has fewer joins and better query performance, even though it may have some data redundancy.

8. FACTS can be additive (sales amount), semi-additive (account balance - cannot sum across time), or non-additive (ratios/percentages). This classification is important for accurate analysis.

9. When asked to compare star and snowflake schemas, emphasize that star provides better query performance while snowflake provides better storage efficiency through normalization.

10. CONFORMED DIMENSIONS are dimensions that can be used across multiple fact tables in different business processes, ensuring consistent analysis across the enterprise.