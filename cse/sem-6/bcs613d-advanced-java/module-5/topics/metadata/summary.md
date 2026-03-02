# Database Metadata in JDBC

## Overview

JDBC metadata provides information about database structure, capabilities, and result sets. DatabaseMetaData describes database properties and schema, while ResultSetMetaData provides details about result set columns including names, types, and properties.

## Key Points

- **DatabaseMetaData**: Obtained via connection.getMetaData(), describes database features
- **ResultSetMetaData**: Obtained via resultSet.getMetaData(), describes result columns
- **getColumnCount()**: Returns number of columns in ResultSet
- **getColumnName()**: Returns column name by index
- **getColumnType()**: Returns SQL type code for column
- **getTableName()**: Returns table name for column
- **getTables()**: Get list of tables in database
- **getColumns()**: Get list of columns for specific table

## Important Concepts

- Metadata useful for generic database tools and frameworks
- DatabaseMetaData reveals database capabilities and limits
- ResultSetMetaData enables dynamic result processing
- Column indices start at 1, not 0
- Use metadata to write database-independent code

## Notes

- Remember two types: DatabaseMetaData (database info) and ResultSetMetaData (result info)
- For exams, know how to get column count, names, and types from ResultSetMetaData
- Practice using getColumnCount() and getColumnName() in loops
