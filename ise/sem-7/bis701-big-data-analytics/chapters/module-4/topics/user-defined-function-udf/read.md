# User Defined Function (UDF) in Hive

=====================================================

## Overview

---

In Hive, a User Defined Function (UDF) is a custom function that can be used to perform complex data transformations and calculations on data stored in Hive tables. UDFs provide a way to leverage external programming languages such as Java, Python, and Scala to extend the functionality of Hive.

## What are UDFs?

---

- A User Defined Function (UDF) is a custom function that can be used to perform complex data transformations and calculations on data stored in Hive tables.
- UDFs are stored in external jars and can be used to perform various tasks such as date calculations, string manipulation, and mathematical calculations.

## Characteristics of UDFs

---

- UDFs are stored in external jars and can be used to perform various tasks such as date calculations, string manipulation, and mathematical calculations.
- UDFs can take input parameters and return output values.
- UDFs can be used with various Hive data types such as INT, STRING, DATE, etc.

## Benefits of UDFs

---

- UDFs provide a way to leverage external programming languages to perform complex data transformations and calculations.
- UDFs can be reused across multiple Hive queries.
- UDFs can be used to perform tasks that are not possible with built-in Hive functions.

## Types of UDFs

---

- **Java UDFs**: Java UDFs are the most commonly used type of UDF. They are stored in external jars and can be used to perform complex data transformations and calculations.
- **Python UDFs**: Python UDFs are used to perform tasks such as data cleaning and data transformation.
- **Scala UDFs**: Scala UDFs are used to perform tasks such as data aggregation and data grouping.

## Examples of UDFs

---

### Java UDF Example

Here is an example of a simple Java UDF that calculates the sum of two numbers:

```java
public class SumUDF extends org.apache.hadoop.hive.ql.udf.UdfDriver {
    public Object invoke(Map<String, Object> args) throws Exception {
        int num1 = (int) args.get("num1");
        int num2 = (int) args.get("num2");
        return num1 + num2;
    }
}
```

### Python UDF Example

Here is an example of a simple Python UDF that calculates the sum of two numbers:

```python
from org.apache.hadoop.hive.ql.udf.generic.GenericUDF import GenericUDF
from org.apache.hadoop.io.ints import IntWritable

class SumUDF(GenericUDF):
    def evaluate(self, x, y):
        return x + y
```

## Registering UDFs

---

To use a UDF in Hive, you need to register it first. You can register a UDF by creating a JAR file and including the UDF class in it.

### Registering Java UDF

Here is an example of how to register a Java UDF:

```bash
jar -cvf myudf.jar myudf.class
hadoop fs -put myudf.jar /user/hive/udf
```

### Registering Python UDF

Here is an example of how to register a Python UDF:

```bash
python setup.py bdist_wheel
hadoop fs -put myudf-1.0-SNAPSHOT-jar-with-dependencies.whl /user/hive/udf
```

## Using UDFs

---

Once you have registered a UDF, you can use it in your Hive queries.

### Using Java UDF

Here is an example of how to use a Java UDF:

```sql
CREATE EXTERNAL FUNCTION my_sum(num1 INT, num2 INT)
RETURNS INT
LANGUAGE Java
CLASSPATH myudf.jar;

SELECT my_sum(1, 2) FROM my_table;
```

### Using Python UDF

Here is an example of how to use a Python UDF:

```sql
CREATE EXTERNAL FUNCTION my_sum(x INT, y INT)
RETURNS INT
LANGUAGE Python
LOCATION '/user/hive/udf/myudf-1.0-SNAPSHOT-jar-with-dependencies.whl';

SELECT my_sum(1, 2) FROM my_table;
```

## Conclusion

---

In this study material, we have covered the basics of User Defined Functions (UDFs) in Hive. We have explained what UDFs are, their characteristics, benefits, and types. We have also provided examples of how to register and use Java and Python UDFs in Hive queries.
