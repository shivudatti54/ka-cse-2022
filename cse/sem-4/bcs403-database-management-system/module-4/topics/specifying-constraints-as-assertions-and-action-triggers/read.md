# Specifying Constraints as Assertions and Action Triggers

## Introduction

Database Management Systems (DBMS) are designed to maintain data integrity and consistency. While primary keys, foreign keys, and check constraints provide basic integrity mechanisms, real-world applications often require more complex business rules that cannot be expressed through simple column-level or table-level constraints. This is where **Assertions** and **Triggers** come into play.

Assertions are general database-wide constraints that enforce complex business rules spanning multiple tables. They allow database designers to express conditions that must always be true, regardless of the operation being performed. For example, ensuring that no employee can earn more than their manager or that the total budget allocation across departments does not exceed the available funds.

Action Triggers, commonly known as triggers, are event-driven mechanisms that automatically execute specific actions in response to certain database operations like INSERT, UPDATE, or DELETE. Triggers enable automated enforcement of business rules, maintenance of audit trails, synchronization of related tables, and implementation of complex data validation that goes beyond what declarative constraints can achieve.

In the context of the university's BCS403 curriculum, understanding assertions and triggers is essential for designing robust database applications. These mechanisms represent the procedural approach to maintaining data integrity, complementing the declarative constraints covered in earlier modules.

## Key Concepts

### 1. Database Constraints: A Review

Before diving into assertions and triggers, it's important to understand the constraint hierarchy in SQL:

- **Domain Constraints**: Ensure values in a column belong to a specific domain (data types, formats)
- **Key Constraints**: Primary keys, unique keys ensure entity integrity
- **Referential Integrity**: Foreign keys maintain relationships between tables
- **Check Constraints**: Validate column values based on conditions

However, these traditional constraints have limitations:

- They operate on single tables or single columns
- They cannot enforce cross-table business rules
- They cannot perform cascading actions automatically
- They cannot maintain historical records or audit trails

### 2. Assertions

An **assertion** is a predicate expressing a condition that must always be true in the database. Unlike table-level check constraints, assertions are schema-level objects that can involve multiple tables and complex logic.

**Syntax for Creating Assertions (SQL Standard):**

```sql
CREATE ASSERTION assertion_name
CHECK (condition);
```

**Example 1: No Employee Earns More Than Manager**

```sql
CREATE ASSERTION no_employee_earns_more_than_manager
CHECK (NOT EXISTS (
 SELECT 1
 FROM employee e, employee m
 WHERE e.manager_id = m.emp_id
 AND e.salary > m.salary
));
```

**Example 2: Department Budget Limit**

```sql
CREATE ASSERTION department_budget_check
CHECK (
 (SELECT SUM(budget) FROM department) <=
 (SELECT total_budget FROM company_limits WHERE year = EXTRACT(YEAR FROM CURRENT_DATE))
);
```

**Example 3: At Least One Manager Per Department**

```sql
CREATE ASSERTION at_least_one_manager
CHECK (EXISTS (
 SELECT 1
 FROM department d
 WHERE d.manager_id IS NOT NULL
));
```

**Key Characteristics of Assertions:**

- Evaluated after every modification that could affect the asserted condition
- If any assertion evaluates to FALSE, the transaction is rolled back
- Supported in SQL standard but limited in commercial DBMS (Oracle, MySQL)
- PostgreSQL and some other systems provide partial support through triggers

### 3. Triggers (Action Triggers)

A **trigger** is a named database object that is automatically executed (fired) when specific events occur on a particular table or view. Triggers are used to enforce complex business rules, maintain audit trails, and automate database operations.

**Components of a Trigger:**

1. **Trigger Event**: INSERT, UPDATE, DELETE operations
2. **Trigger Timing**: BEFORE, AFTER, or INSTEAD OF
3. **Trigger Level**: STATEMENT-level or ROW-level
4. **Trigger Body**: The SQL statements to execute

**Basic Trigger Syntax (Oracle/PL/SQL):**

```sql
CREATE [OR REPLACE] TRIGGER trigger_name
{BEFORE | AFTER | INSTEAD OF}
{INSERT | UPDATE | DELETE} [OR {INSERT | UPDATE | DELETE}...]
ON table_name
[FOR EACH ROW [WHEN condition]]
DECLARE
 -- variable declarations
BEGIN
 -- trigger body (PL/SQL statements)
END;
```

**BEFORE vs AFTER Triggers:**

- **BEFORE triggers**: Execute before the triggering operation; used for data validation and modification
- **AFTER triggers**: Execute after the triggering operation; used for logging and audit trails

**ROW-level vs Statement-level:**

- **ROW-level**: Executes once for each affected row
- **Statement-level**: Executes once for the entire statement

### 4. Trigger Examples

**Example 1: Automatic Timestamp Update**

```sql
CREATE OR REPLACE TRIGGER update_timestamp
BEFORE UPDATE ON employee
FOR EACH ROW
BEGIN
 :NEW.last_modified := SYSDATE;
 :NEW.modified_by := USER;
END;
```

In this trigger:

- `:OLD` refers to the old row values before modification
- `:NEW` refers to the new row values after modification
- The trigger fires before each row update

**Example 2: Maintaining Audit Trail**

```sql
CREATE TABLE employee_audit (
 audit_id NUMBER PRIMARY KEY,
 emp_id NUMBER,
 action_type VARCHAR2(10),
 old_salary NUMBER,
 new_salary NUMBER,
 change_date DATE,
 changed_by VARCHAR2(50)
);

CREATE OR REPLACE TRIGGER audit_employee_salary
AFTER UPDATE OF salary ON employee
FOR EACH ROW
BEGIN
 INSERT INTO employee_audit
 VALUES (employee_audit_seq.NEXTVAL, :OLD.emp_id, 'SALARY_UPDATE',
 :OLD.salary, :NEW.salary, SYSDATE, USER);
END;
```

**Example 3: Enforcing Business Rule (No Salary Decrease)**

```sql
CREATE OR REPLACE TRIGGER prevent_salary_decrease
BEFORE UPDATE OF salary ON employee
FOR EACH ROW
BEGIN
 IF :NEW.salary < :OLD.salary THEN
 RAISE_APPLICATION_ERROR(-20001,
 'Salary cannot be decreased for employee ' || :OLD.emp_id);
 END IF;
END;
```

**Example 4: Cascading Updates**

```sql
CREATE OR REPLACE TRIGGER update_order_total
AFTER INSERT OR UPDATE OR DELETE ON order_items
FOR EACH ROW
BEGIN
 IF INSERTING OR UPDATING THEN
 UPDATE orders o
 SET o.total_amount = o.total_amount + :NEW.quantity * :NEW.unit_price
 WHERE o.order_id = :NEW.order_id;
 END IF;

 IF DELETING OR UPDATING THEN
 UPDATE orders o
 SET o.total_amount = o.total_amount - :OLD.quantity * :OLD.unit_price
 WHERE o.order_id = :OLD.order_id;
 END IF;
END;
```

### 5. INSTEAD OF Triggers

INSTEAD OF triggers are used on views (especially complex views that are not directly updatable) to enable DML operations.

```sql
CREATE OR REPLACE TRIGGER instead_of_insert_emp_view
INSTEAD OF INSERT ON emp_dept_view
FOR EACH ROW
BEGIN
 INSERT INTO department (dept_id, dept_name, location)
 VALUES (:NEW.dept_id, :NEW.dept_name, :NEW.location);

 INSERT INTO employee (emp_id, emp_name, dept_id, salary)
 VALUES (:NEW.emp_id, :NEW.emp_name, :NEW.dept_id, :NEW.salary);
END;
```

### 6. Differences Between Assertions and Triggers

| Aspect     | Assertions                      | Triggers                         |
| ---------- | ------------------------------- | -------------------------------- |
| Nature     | Declarative constraint          | Procedural code                  |
| Activation | Automatically checked after DML | Automatically executed on events |
| Purpose    | Enforce conditions              | Perform actions                  |
| Support    | Limited in commercial DBMS      | Widely supported                 |
| Complexity | Simpler check conditions        | Can execute complex logic        |
| Use Case   | Cross-table constraints         | Auditing, cascading, validation  |

## Examples

### Worked Example 1: Inventory Management System

**Scenario**: A warehouse needs to ensure that when an order is placed, the quantity requested does not exceed available stock. Also, automatically update the inventory when an order is confirmed.

**Solution Using Triggers:**

```sql
-- Table structure
CREATE TABLE products (
 product_id NUMBER PRIMARY KEY,
 product_name VARCHAR2(100),
 stock_quantity NUMBER,
 reorder_level NUMBER
);

CREATE TABLE orders (
 order_id NUMBER PRIMARY KEY,
 order_date DATE,
 status VARCHAR2(20)
);

CREATE TABLE order_items (
 order_item_id NUMBER PRIMARY KEY,
 order_id NUMBER REFERENCES orders(order_id),
 product_id NUMBER REFERENCES products(product_id),
 quantity NUMBER
);

-- Trigger to validate stock and update inventory
CREATE OR REPLACE TRIGGER validate_and_update_stock
AFTER INSERT ON order_items
FOR EACH ROW
DECLARE
 v_available_stock NUMBER;
BEGIN
 -- Check available stock
 SELECT stock_quantity INTO v_available_stock
 FROM products
 WHERE product_id = :NEW.product_id;

 IF v_available_stock < :NEW.quantity THEN
 RAISE_APPLICATION_ERROR(-20001,
 'Insufficient stock for product ' || :NEW.product_id ||
 '. Available: ' || v_available_stock || ', Requested: ' || :NEW.quantity);
 END IF;

 -- Update stock
 UPDATE products
 SET stock_quantity = stock_quantity - :NEW.quantity
 WHERE product_id = :NEW.product_id;

 -- Check for reorder
 IF (stock_quantity - :NEW.quantity) <= reorder_level THEN
 DBMS_OUTPUT.PUT_LINE('Warning: Product ' || :NEW.product_id ||
 ' has reached reorder level!');
 END IF;
END;
```

### Worked Example 2: University Course Enrollment

**Scenario**: Implement business rules for course enrollment:

- Maximum 40 students per course
- A student cannot enroll in two courses at the same time slot
- Automatically maintain enrollment count

**Solution:**

```sql
CREATE TABLE courses (
 course_id NUMBER PRIMARY KEY,
 course_name VARCHAR2(50),
 max_students NUMBER DEFAULT 40,
 current_enrollment NUMBER DEFAULT 0
);

CREATE TABLE time_slots (
 slot_id NUMBER PRIMARY KEY,
 day VARCHAR2(10),
 start_time VARCHAR2(5),
 end_time VARCHAR2(5)
);

CREATE TABLE enrollments (
 enrollment_id NUMBER PRIMARY KEY,
 student_id NUMBER,
 course_id NUMBER REFERENCES courses(course_id),
 slot_id NUMBER REFERENCES time_slots(slot_id),
 enrollment_date DATE
);

-- Trigger to check course capacity
CREATE OR REPLACE TRIGGER check_course_capacity
BEFORE INSERT ON enrollments
FOR EACH ROW
DECLARE
 v_current NUMBER;
 v_max NUMBER;
BEGIN
 SELECT current_enrollment, max_students
 INTO v_current, v_max
 FROM courses
 WHERE course_id = :NEW.course_id;

 IF v_current >= v_max THEN
 RAISE_APPLICATION_ERROR(-20002,
 'Course ' || :NEW.course_id || ' is full!');
 END IF;

 -- Update enrollment count
 UPDATE courses
 SET current_enrollment = current_enrollment + 1
 WHERE course_id = :NEW.course_id;
END;

-- Trigger to check time slot conflict
CREATE OR REPLACE TRIGGER check_time_conflict
BEFORE INSERT ON enrollments
FOR EACH ROW
DECLARE
 v_conflict_count NUMBER;
BEGIN
 SELECT COUNT(*) INTO v_conflict_count
 FROM enrollments e
 WHERE e.student_id = :NEW.student_id
 AND e.slot_id = :NEW.slot_id
 AND e.enrollment_id != :NEW.enrollment_id;

 IF v_conflict_count > 0 THEN
 RAISE_APPLICATION_ERROR(-20003,
 'Time slot conflict! Student already enrolled in another course at this time.');
 END IF;
END;
```

## Exam Tips

1. **Understand the difference**: Assertions are declarative constraints checked automatically, while triggers are procedural code executed on specific events.

2. **Trigger timing matters**: Remember that BEFORE triggers modify data before insertion, while AFTER triggers are used for logging and auditing.

3. **Use OLD and NEW references**: In row-level triggers, use :OLD.column_name for existing values and :NEW.column_name for new values. Note: :NEW is null for DELETE operations, :OLD is null for INSERT.

4. **RAISE_APPLICATION_ERROR**: Know how to use this to raise user-defined error messages in Oracle triggers.

5. **INSTEAD OF triggers**: These are specifically for making complex views updatable.

6. **Mutating table problem**: Be aware that row-level triggers cannot query or modify the same table that triggered them. This is a common source of errors.

7. **Assertion syntax**: Remember the SQL standard syntax: CREATE ASSERTION name CHECK (condition).

8. **Transaction behavior**: Both assertions and triggers cause automatic rollback when constraints are violated or errors are raised.

9. **Trigger names**: Must be unique within a schema and follow naming conventions.

10. **WHEN clause**: Optional clause in triggers to specify conditions under which the trigger should fire.
