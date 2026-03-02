# Hive Data Types

## Introduction

Apache Hive is a data warehouse infrastructure built on top of Hadoop that provides SQL-like query capabilities for analyzing large datasets. Understanding Hive data types is fundamental to effectively working with Hive tables and writing efficient HQL (Hive Query Language) queries. Data types define the kind of values that columns can store in Hive tables, and choosing the appropriate data type is crucial for data storage optimization, query performance, and maintaining data integrity.

In the context of Big Data processing, Hive serves as a critical bridge between structured query language (SQL) and the distributed computing environment of Hadoop. The data types in Hive are designed to accommodate various data formats encountered in enterprise data ecosystems, ranging from simple numeric values to complex nested structures. For students preparing for DU semester examinations, a thorough understanding of Hive data types enables them to design efficient table schemas and write optimized queries that perform well on large-scale data.

This topic explores the complete spectrum of data types supported by Hive, including primitive types that form the building blocks of data representation and complex types that enable modeling of sophisticated data structures. We will examine each data type category with practical examples, discuss type conversion mechanisms, and highlight important considerations for real-world Hive implementations.

## Key Concepts

### Primitive Data Types

Primitive data types in Hive represent the most fundamental data representations. They are categorized into several groups based on the nature of data they store.

#### Numeric Types

Hive provides a comprehensive set of numeric types to handle various computational requirements:

**Integer Types:**
- TINYINT: 1-byte signed integer, range from -128 to 127
- SMALLINT: 2-byte signed integer, range from -32,768 to 32,767
- INT: 4-byte signed integer, range from -2,147,483,648 to 2,147,483,647 (this is the default integer type in Hive)
- BIGINT: 8-byte signed integer, range from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

When creating tables, it is important to note that Hive treats integer literals as INT by default. For example, if you assign the value 100 to a TINYINT column, you must explicitly cast it as TINYINT(100) or the value will be treated as INT.

**Floating-Point Types:**
- FLOAT: 4-byte single-precision floating-point number
- DOUBLE: 8-byte double-precision floating-point number (this is the default for decimal literals)
- DECIMAL: Introduced in Hive 0.11.0, provides arbitrary precision for numeric values

The DECIMAL type is particularly important for financial applications where precision is critical. It allows specification of total digits and fractional digits, for example, DECIMAL(10,2) represents a number with up to 10 total digits and 2 decimal places.

#### String Types

**STRING:** Variable-length character string with no defined maximum length. It can store Unicode characters and handles large text data effectively. STRING in Hive can store strings up to 2GB in size.

**VARCHAR:** Variable-length character string with a defined maximum length between 1 and 65535. If the assigned value exceeds the defined length, it will be truncated or cause an error depending on configuration.

**CHAR:** Fixed-length character string with maximum length of 255. Values shorter than the defined length are padded with spaces.

For most text processing scenarios, STRING is preferred due to its flexibility and minimal storage overhead when compared to fixed-length types.

#### Date and Time Types

**DATE:** Represents a date value in the format YYYY-YYYY-MM-DD, ranging from 0000-01-01 to 9999-12-31.

**TIMESTAMP:** Represents a point in time with nanosecond precision, stored as the number of nanoseconds since the Unix epoch (January 1, 1970). The format is YYYY-MM-DD HH:MM:SS.frac.

**INTERVAL:** Used for interval arithmetic, allowing date and time arithmetic operations.

Hive 3.1.0 and later versions provide additional temporal types including INTERVAL_YEAR_MONTH and INTERVAL_DAY_TIME for more granular time span representations.

#### Boolean Type

**BOOLEAN:** Stores true or false values. This is the simplest data type in Hive, used extensively in filtering conditions and logical operations.

#### Binary Type

**BINARY:** Stores variable-length binary data. This type is essential for storing serialized objects, compressed data, or any binary content that cannot be represented as text. Unlike other types, BINARY data is not displayed in human-readable format in Hive outputs.

### Complex Data Types

Complex data types enable modeling of sophisticated data structures that go beyond simple scalar values. These types are particularly valuable when working with semi-structured data like JSON or nested enterprise data.

#### ARRAY

ARRAY is an ordered collection of elements of the same data type. Arrays in Hive are zero-indexed, meaning the first element is accessed using index 0. The syntax for defining an ARRAY column is ARRAY<data_type>.

Consider an example where we want to store a list of skills for each employee:

```sql
CREATE TABLE employee_skills (
    employee_id INT,
    name STRING,
    skills ARRAY<STRING>
);
```

To insert data:

```sql
INSERT INTO employee_skills VALUES 
(101, 'Amit', ARRAY('Java', 'Python', 'Hive')),
(102, 'Priya', ARRAY('SQL', 'Scala', 'Spark'));
```

To query array elements, use bracket notation with the index:

```sql
SELECT name, skills[0] AS first_skill 
FROM employee_skills;
```

To access all elements, use EXPLODE function which transforms each array element into a separate row:

```sql
SELECT name, skill 
FROM employee_skills 
LATERAL VIEW EXPLODE(skills) AS skill;
```

#### MAP

MAP is a collection of key-value pairs where keys must be primitive types and values can be any data type. Each key in a map must be unique. The syntax is MAP<key_type, value_type>.

Example table with MAP type:

```sql
CREATE TABLE product_details (
    product_id INT,
    product_name STRING,
    attributes MAP<STRING, STRING>
);
```

Inserting data:

```sql
INSERT INTO product_details VALUES 
(1001, 'Laptop', MAP('color', 'Silver', 'warranty', '2 years', 'weight', '2.5kg')),
(1002, 'Mouse', MAP('color', 'Black', 'warranty', '1 year'));
```

Accessing map values using bracket notation:

```sql
SELECT product_name, attributes['color'] AS color 
FROM product_details;
```

Using map keys function to retrieve all keys:

```sql
SELECT product_name, MAP_KEYS(attributes) AS all_attributes 
FROM product_details;
```

#### STRUCT

STRUCT is similar to a record in traditional databases or a class in object-oriented programming. It groups together related fields that can be of different data types. Each field within a struct has a name and a data type. The syntax is STRUCT<field_name1:data_type1, field_name2:data_type2, ...>.

Example representing address as a struct:

```sql
CREATE TABLE employee_address (
    employee_id INT,
    name STRING,
    address STRUCT<street:STRING, city:STRING, state:STRING, pincode:STRING>
);
```

Inserting data:

```sql
INSERT INTO employee_address VALUES 
(101, 'Rahul', STRUCT('123 MG Road', 'Delhi', 'Delhi', '110001')),
(102, 'Sunita', STRUCT('456 Park Avenue', 'Mumbai', 'Maharashtra', '400001'));
```

Accessing struct fields using dot notation:

```sql
SELECT name, address.city AS city, address.pincode AS pincode 
FROM employee_address;
```

#### UNIONTYPE

UNIONTYPE represents a value that can be one of several data types, but only one at a time. This is useful for handling schema evolution or representing optional fields with different possible types. The syntax is UNIONTYPE<type1, type2, ...>.

Creating a table with UNIONTYPE:

```sql
CREATE TABLE variable_data (
    id INT,
    value UNIONTYPE<STRING, INT, DOUBLE>
);
```

When inserting data into UNIONTYPE columns, you must specify which type using the syntax:

```sql
INSERT INTO variable_data VALUES 
(1, CAST('hello' AS UNIONTYPE<STRING, INT, DOUBLE>)),
(2, CAST(42 AS UNIONTYPE<STRING, INT, DOUBLE>));
```

### Type Conversion

Hive supports both implicit and explicit type conversion. Understanding type conversion rules is essential for writing correct queries and avoiding unexpected results.

#### Implicit Conversion

Hive automatically converts smaller numeric types to larger ones. The numeric type promotion hierarchy is: TINYINT → SMALLINT → INT → BIGINT → FLOAT → DOUBLE. Additionally, STRING can be implicitly converted to DOUBLE in numeric contexts.

#### Explicit Conversion (Casting)

The CAST function performs explicit type conversion with the syntax: CAST(expression AS target_type).

Examples:

```sql
-- Convert string to integer
SELECT CAST('100' AS INT);

-- Convert double to integer (truncates decimal part)
SELECT CAST(12.78 AS INT);  -- Returns 12

-- Convert string to date
SELECT CAST('2024-01-15' AS DATE);

-- Convert timestamp to string
SELECT CAST(CAST('2024-01-15 10:30:00' AS TIMESTAMP) AS STRING);
```

Failed casts return NULL rather than throwing an error, which is important behavior to remember during debugging.

#### Special Conversion Functions

Hive provides additional conversion functions beyond CAST:
- CONVERT: Alternative conversion function
- TO_DATE: Extracts date part from timestamp or string
- UNIX_TIMESTAMP: Converts date/time to Unix timestamp
- FROM_UNIXTIME: Converts Unix timestamp to string

### Type Comparison and Operators

When comparing values of different types, Hive follows specific rules. Comparisons between numeric types follow the implicit conversion rules. String comparisons are case-sensitive by default. Dates and timestamps can be compared directly. Complex types (ARRAY, MAP, STRUCT) support equality comparison only.

## Examples

### Example 1: Creating a Table with Multiple Data Types

Design a Hive table to store student examination records with the following requirements: student ID, name, date of birth, marks in different subjects, contact phone numbers, and personal details including email and alternate contact.

```sql
CREATE TABLE student_records (
    student_id INT,
    name STRING,
    date_of_birth DATE,
    marks MAP<STRING, INT>,
    phone_numbers ARRAY<STRING>,
    contact STRUCT<email:STRING, alternate_phone:STRING>,
    is_active BOOLEAN
);
```

Insert sample data:

```sql
INSERT INTO student_records VALUES 
(1001, 'Ananya Gupta', '2003-05-15', 
 MAP('Mathematics', 92, 'Physics', 88, 'Chemistry', 95),
 ARRAY('9876543210', '9876543211'),
 STRUCT('ananya.gupta@email.com', '9876543212'),
 true);
```

Query to find students with marks above 90 in Mathematics:

```sql
SELECT student_id, name, marks['Mathematics'] AS math_marks 
FROM student_records 
WHERE marks['Mathematics'] > 90;
```

### Example 2: Working with Nested Complex Types

Create a table to store department information where each department has multiple projects, and each project has team members with their roles.

```sql
CREATE TABLE department_info (
    dept_id INT,
    dept_name STRING,
    projects ARRAY<STRUCT<
        project_id:INT,
        project_name:STRING,
        team_members:ARRAY<STRUCT<member_name:STRING, role:STRING>>
    >>
);
```

Query to find all team members working on specific projects:

```sql
SELECT dept_name, project.project_name, member.member_name, member.role
FROM department_info
LATERAL VIEW EXPLODE(projects) AS project
LATERAL VIEW EXPLODE(project.team_members) AS member
WHERE project.project_name LIKE '%Analytics%';
```

### Example 3: Type Conversion in Queries

Demonstrate various type conversion scenarios:

```sql
-- Create table with string dates
CREATE TABLE sales_data (
    sale_id INT,
    sale_date STRING,
    amount STRING
);

-- Insert sample data
INSERT INTO sales_data VALUES 
(1, '2024-01-15', '1500.75'),
(2, '2024-01-16', '2300.50');

-- Convert strings to appropriate types for calculations
SELECT 
    sale_id,
    CAST(sale_date AS DATE) AS date,
    CAST(amount AS DOUBLE) * 1.18 AS tax_included
FROM sales_data;

-- Convert date to string with different format
SELECT 
    sale_id,
    FROM_UNIXTIME(UNIX_TIMESTAMP(sale_date, 'yyyy-MM-dd'), 'dd/MM/yyyy') AS formatted_date
FROM sales_data;
```

## Exam Tips

1. Remember the integer type hierarchy: TINYINT (1 byte) < SMALLINT (2 bytes) < INT (4 bytes) < BIGINT (8 bytes). INT is the default integer type in Hive.

2. For floating-point operations, use DOUBLE for general calculations. For financial applications requiring exact precision, use DECIMAL type.

3. STRING is the most flexible string type with no length constraints, making it the default choice for text data.

4. ARRAY, MAP, and STRUCT are the three main complex types. ARRAY stores ordered elements, MAP stores key-value pairs, and STRUCT stores named fields of different types.

5. Access ARRAY elements using index notation (array[index]), MAP values using key notation (map['key']), and STRUCT fields using dot notation (struct.field).

6. The LATERAL VIEW clause is essential when querying complex types. Use EXPLODE with LATERAL VIEW to transform ARRAY and MAP elements into separate rows.

7. Remember that failed CAST operations return NULL rather than throwing errors. Always validate data before type conversion in production queries.

8. For date operations, remember that DATE stores only date (YYYY-MM-DD) while TIMESTAMP stores date with time including nanoseconds.

9. Complex types can be nested. For example, you can have ARRAY<MAP<STRING, STRUCT<>>> for highly complex data structures.

10. UNIONTYPE is less commonly used but important for schema evolution scenarios where a column might hold different types of values at different times.