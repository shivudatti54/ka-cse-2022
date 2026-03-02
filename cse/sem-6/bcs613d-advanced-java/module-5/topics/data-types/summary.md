# Data Types in JDBC - Summary

## Key Definitions

- **JDBC Type Mapping**: The systematic conversion between Java data types and SQL data types performed by the JDBC driver during database operations
- **java.sql.Types**: A class defining integer constants (such as INTEGER, VARCHAR, DATE) representing standard SQL data types
- **BLOB (Binary Large Object)**: SQL data type for storing binary data such as images, audio, or video files
- **CLOB (Character Large Object)**: SQL data type for storing large text data, particularly useful for character sets exceeding VARCHAR limits
- **TIMESTAMP**: SQL data type storing both date and time with nanosecond precision

## Important Formulas

- Type-safe setter: `pstmt.set<Type>(parameterIndex, value)` where Type matches Java data type
- Type-safe getter: `rs.get<Type>(columnLabel)` or `rs.get<Type>(columnIndex)`
- Null check: `if (rs.wasNull())` - must be called immediately after getter that might return NULL
- Date conversion: `new Date(java.util.Date.getTime())` converts util.Date to sql.Date

## Key Points

1. JDBC drivers handle automatic conversion between Java and SQL types based on standard mappings defined in the specification

2. The `java.sql.Date` class only contains date information; time portion is truncated when storing in DATE columns

3. `java.sql.Timestamp` extends `java.util.Date` and provides nanosecond precision for both storage and retrieval

4. When retrieving NULL values into primitive types, JDBC returns zero values; use `wasNull()` to distinguish NULL from actual zero

5. The `PreparedStatement` interface provides type-specific setter methods that ensure proper type conversion and prevent SQL injection

6. Binary data can be handled through `setBinaryStream()`, `setBytes()`, or `setBlob()` methods depending on data size and source

7. Different database vendors may support different SQL type names, but the JDBC driver normalizes these to standard `java.sql.Types` constants

8. Batch operations with `addBatch()` and `executeBatch()` maintain type information across multiple parameter sets

## Common Mistakes

1. **Using java.util.Date with setDate()**: The `setDate()` method requires `java.sql.Date`, not `java.util.Date`. Forgetting this causes compilation or runtime errors.

2. **Confusing TIME and TIMESTAMP**: Storing a timestamp value into a TIME column loses the date portion entirely, and storing only time into TIMESTAMP defaults the date to 1970-01-01.

3. **Not checking wasNull() after primitive getters**: This is the most common error when NULL values are possible; the code cannot distinguish between NULL and zero without this check.

4. **Ignoring character encoding for CLOBs**: When handling international characters, failing to specify proper encoding results in data corruption or truncation.

5. **Attempting to store large files entirely in memory**: For very large BLOBs, always use streams rather than byte arrays to avoid `OutOfMemoryError`.