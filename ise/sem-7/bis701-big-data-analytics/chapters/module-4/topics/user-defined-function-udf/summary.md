# **User Defined Function (UDF)**

## **Introduction**

- A User Defined Function (UDF) is a custom-written function that can be used in Hive queries.
- UDFs are stored in the Hive repository and can be used like regular Hive functions.

## **Key Points**

- **Types of UDFs**:
  - Java-based UDFs
  - Python-based UDFs (introduced in Hive 0.13)
  - C-based UDFs
- **UDF Registration**:
  - Register UDFs using `CREATE TEMPORARY FUNCTION` or `CREATE FUNCTION`
  - Specify UDF jar file or directory
- **UDF Syntax**:
  - `SELECT function_name(column1, column2, ...) FROM table_name;`
- **UDF Parameters**:
  - Can be of any data type (e.g., string, integer, date)
  - Can be used in Hive queries, such as filtering, grouping, and aggregating data

## **Important Formulas and Definitions**

- **Function**: A set of instructions that takes input values and produces output values.
- **UDF**: A custom-written function that can be used in Hive queries.
- **Java-based UDF**: A UDF written in Java, compiled into a JAR file, and stored in the Hive repository.

## **Important Theorems**

- **Hive's UDF Ecosystem**: Hive's UDF ecosystem allows developers to create custom functions that can be used in Hive queries.

## **Revision Notes**

- UDFs are stored in the Hive repository and can be used like regular Hive functions.
- UDFs can be registered using `CREATE TEMPORARY FUNCTION` or `CREATE FUNCTION`.
- UDFs can be used in Hive queries, such as filtering, grouping, and aggregating data.
