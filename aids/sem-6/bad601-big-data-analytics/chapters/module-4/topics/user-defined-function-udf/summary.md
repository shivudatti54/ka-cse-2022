# User Defined Function (UDF) Revision Notes

==============================================

## What is a User Defined Function (UDF) in Hive?

- A UDF is a custom function that can be used in Hive queries to perform specific tasks.
- It allows users to write and use their own functions in Hive queries.

## Characteristics of UDFs

- UDFs are stored in the `hive::udf` directory in the Hive metastore.
- They can take arguments and return a value.
- UDFs can be used in Hive queries to perform complex calculations.

## Types of UDFs

- **Native UDFs**: written in Java or C++.
- **Pseudo UDFs**: written in a pseudo-language (e.g., SQL).

## Important Formulas and Definitions

- **UDF Registration**: `CREATE FUNCTION function_name (argument_list) RETURNS return_type;`
- **UDF Implementation**: `public class UDFClassName implements CallableInterface { public Object call(TableInput input, TableOutput output, Context context) throws IOException, InterruptedException; }`

## Important Theorems

- **The UDF Theorem**: A UDF can be used in a Hive query to perform any calculation that can be performed using Java.

## Key Features

- **Argument Handling**: UDFs can handle various data types, including strings, integers, and dates.
- **Return Type**: UDFs can return various data types, including integers, strings, and arrays.
- **Error Handling**: UDFs can handle errors and exceptions.

## Quick Revision Tips

- Use native UDFs for complex calculations.
- Use pseudo UDFs for simple calculations.
- Register UDFs before using them in Hive queries.
- Document UDFs to make them reusable.
