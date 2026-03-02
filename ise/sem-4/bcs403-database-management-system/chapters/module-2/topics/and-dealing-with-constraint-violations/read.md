# Handling Constraint Violations in DBMS

## Introduction

In a Database Management System (DBMS), constraints are rules enforced on data columns to ensure the **integrity, accuracy, and reliability** of the data within a table. They are fundamental to the relational model. However, when a database operation (like `INSERT`, `UPDATE`, or `DELETE`) attempts to violate these predefined rules, the DBMS raises an error and prevents the operation from completing. This event is known as a **constraint violation**. Understanding how to identify, handle, and resolve these violations is a critical skill for any developer or database administrator.

## Core Concepts of Constraint Violations

A constraint violation occurs when an SQL operation tries to modify the database state in a way that breaks one or more of its integrity constraints. The DBMS is designed to be the ultimate guardian of these rules; it will **always reject** any transaction that causes a violation, ensuring the database remains in a consistent state.

Common types of constraints and their potential violations include:

### 1. PRIMARY KEY Constraint
*   **Rule:** Ensures a column (or set of columns) has a unique, non-`NULL` value for every row in the table.
*   **Violation Scenario:**
    *   **Duplicate Value:** Trying to `INSERT` a new row with a primary key value that already exists in the table.
    *   **Null Value:** Attempting to `INSERT` a row with a `NULL` value in the primary key column.

**Example:**