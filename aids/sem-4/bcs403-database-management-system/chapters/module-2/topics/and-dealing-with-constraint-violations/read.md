# Handling Constraint Violations in DBMS

## Introduction

In a Database Management System (DBMS), **integrity constraints** are rules enforced on database tables to ensure the accuracy, consistency, and reliability of the data. They are fundamental to maintaining data integrity. However, during standard database operations like `INSERT`, `UPDATE`, or `DELETE`, these rules can be broken, leading to **constraint violations**. Understanding what these violations are and how the DBMS deals with them is crucial for any developer or database administrator. This module explores the common types of constraint violations and the mechanisms, primarily **transaction control**, used to handle them.

## Core Concepts: Types of Constraints and Their Violations

Constraints are defined during table creation (using `CREATE TABLE`) or alteration (using `ALTER TABLE`). When a user operation attempts to modify the database in a way that breaks one of these rules, the DBMS raises an error and prevents the operation from succeeding. This is a constraint violation.

The most common constraints and their potential violations are:

### 1. `NOT NULL` Constraint
*   **Rule:** A column cannot have a `NULL` value.
*   **Violation Example:** Attempting to `INSERT` a new record without providing a value for a column defined as `NOT NULL`.