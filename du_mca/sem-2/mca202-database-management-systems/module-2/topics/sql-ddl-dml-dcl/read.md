# SQL DDL, DML, DCL

## Introduction
SQL (Structured Query Language) forms the backbone of modern database management systems. This topic covers three fundamental components: Data Definition Language (DDL), Data Manipulation Language (DML), and Data Control Language (DCL). These components enable database administrators and developers to structure databases, manipulate data, and control access permissions.

DDL focuses on schema creation/modification (CREATE, ALTER, DROP). DML handles data operations (INSERT, UPDATE, DELETE, SELECT). DCL manages security through GRANT/REVOKE commands. Mastery of these concepts is critical for building enterprise applications like banking systems, e-commerce platforms, and inventory management systems where data integrity and security are paramount.

In DU's MCA program, this topic bridges theoretical database design concepts with practical implementation. With 75% weightage in semester exams, students must demonstrate command syntax precision and real-world problem-solving abilities.

## Key Concepts
**1. Data Definition Language (DDL)**
- Schema Creation: `CREATE TABLE` with constraints (PRIMARY KEY, FOREIGN KEY, CHECK)
- Schema Modification: `ALTER TABLE` (add/drop columns, modify constraints)
- Schema Deletion: `DROP TABLE` (cascading vs restrict options)
- Transactional DDL: Oracle's AUTOCOMMIT vs MySQL's implicit commits

**2. Data Manipulation Language (DML)**
- CRUD Operations: `INSERT INTO`, `UPDATE ... SET`, `DELETE FROM`
- Querying: `SELECT` with JOINs (INNER, LEFT, RIGHT), WHERE clauses, and aggregation
- Bulk Operations: `INSERT INTO ... SELECT` for data migration
- Transaction Control: Implicit vs explicit COMMIT/ROLLBACK (often grouped with TCL)

**3. Data Control Language (DCL)**
- Privilege Management: `GRANT SELECT ON employees TO hr_role`
- Revocation: `REVOKE DELETE ON salaries FROM auditor`
- Role-Based Access: Creating roles and inheritance hierarchies
- Security Best Practices: Principle of least privilege implementation

## Examples
**Example 1: DDL for E-Commerce Database**
```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) CHECK (price > 0),
    category_id INT REFERENCES categories(category_id)
);

ALTER TABLE products ADD COLUMN stock INT DEFAULT 0;
```

**Example 2: Complex DML Query**
```sql
-- Find total sales per category in Q1 2024
SELECT c.category_name, SUM(oi.quantity * oi.unit_price) AS total_sales
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
WHERE oi.order_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY c.category_name
HAVING SUM(oi.quantity * oi.unit_price) > 10000;
```

**Example 3: DCL for Banking System**
```sql
CREATE ROLE loan_officer;
GRANT SELECT, UPDATE ON loans TO loan_officer;
GRANT loan_officer TO user_ashok;

REVOKE UPDATE ON loans FROM loan_officer;
```

## Exam Tips
1. Memorize exact syntax for CONSTRAINT definitions (PK, FK, CHECK)
2. Practice writing JOINs with 3+ tables – common in 8-mark questions
3. Understand GRANT hierarchy: System > Database > Table > Column-level privileges
4. Always specify CASCADE/RESTRICT when using DROP to avoid schema inconsistencies
5. For UPDATE/DELETE, write WHERE conditions carefully – missing WHERE = catastrophic data loss
6. Know differences between TRUNCATE (DDL) vs DELETE (DML) – auto-commit behavior
7. Use SQL:1999 vs SQL:2003 standards in answers when discussing features like window functions