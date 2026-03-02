# Views and ODBC - Summary

## Key Definitions and Concepts

- **View**: A virtual table defined by a SELECT query; does not store data physically (except materialized views)
- **Simple View**: Created from a single table without aggregates; typically updatable
- **Complex View**: Created from multiple tables with JOINs, aggregates, or GROUP BY; often not updatable
- **Materialized View**: Stores query results physically on disk; requires periodic refresh
- **ODBC**: Open Database Connectivity—a standard API for applications to access database management systems
- **DSN (Data Source Name)**: Configuration storing database connection details
- **ODBC Driver**: Database-specific library translating ODBC calls to native DB API

## Important Formulas and Theorems

- **View Creation**: `CREATE VIEW view_name AS SELECT ... FROM table WHERE condition`
- **View Deletion**: `DROP VIEW view_name`
- **View Updatability Criteria**: Single base table, no aggregates, no GROUP BY/HAVING, no DISTINCT/UNION, all NOT NULL columns included

## Key Points

- Views provide data abstraction, security, and query simplification without duplicating data
- Materialized views improve performance in data warehousing but require storage space and refresh logic
- ODBC enables database interoperability across different DBMS platforms
- ODBC architecture consists of Application, Driver Manager, ODBC Driver, and Data Source layers
- Views can implement column-level security by exposing only specific attributes to users
- Complex views with JOINs are not automatically updatable—DBMS may restrict INSERT/UPDATE operations
- DSN can be User DSN (user-specific), System DSN (machine-wide), or File DSN (portable)
- ODBC drivers are database-specific; MySQL, Oracle, PostgreSQL each have separate drivers

## Common Mistakes to Avoid

- Assuming all views are updatable—complex views with joins/aggregates may not support DML operations
- Confusing materialized views with regular views—they store actual data physically
- Believing ODBC is programming language-specific—it works with C, C++, Python, PHP, and more
- Forgetting that views reflect current data in base tables (except materialized views)

## Revision Tips

1. Practice creating different types of views and testing their updatability
2. Configure an ODBC data source on your system and establish a test connection
3. Draw the ODBC architecture diagram and label all four layers
4. Write SQL queries using views to reinforce understanding of virtual tables
5. Review previous year DU exam questions on views and ODBC for pattern familiarity