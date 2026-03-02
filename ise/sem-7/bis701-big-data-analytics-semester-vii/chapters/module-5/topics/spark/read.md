# Spark SQL: Unified Data Processing in Apache Spark

## Introduction to Spark SQL

Spark SQL is a core module of Apache Spark that provides structured data processing capabilities. It bridges the gap between the relational world (SQL) and the procedural world (RDDs), enabling users to run SQL queries alongside complex analytics algorithms. Spark SQL allows you to work with structured and semi-structured data using either SQL or the DataFrame API.

**Key Advantages:**
- Unified data access across various formats (JSON, Parquet, Avro, ORC, etc.)
- Integration with Hive metastore and existing Hive data warehouses
- Standard connectivity through JDBC/ODBC
- Optimized execution through Catalyst optimizer
- Support for both batch and interactive processing

## Core Concepts

### DataFrames and Datasets

Spark SQL introduces two main abstractions: DataFrames and Datasets.

**DataFrame**: A distributed collection of data organized into named columns, equivalent to a table in a relational database. DataFrames are built on top of RDDs but with a schema and optimized execution plan.

```
+----------+--------+-------+
|   name   |  age   | city  |
+----------+--------+-------+
|  Alice   |   25   |  NYC  |
|   Bob    |   30   |  SF   |
| Charlie  |   35   |  LA   |
+----------+--------+-------+
```

**Dataset**: A strongly-typed extension of DataFrames that provides compile-time type safety. Datasets combine the benefits of RDDs (strong typing, functional programming) with the optimizations of Spark SQL.

### SparkSession

The entry point to all Spark SQL functionality is the SparkSession. It replaces the old SQLContext and HiveContext.

```python
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("SparkSQLExample") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
```

## Architecture and Components

### Catalyst Optimizer

Catalyst is Spark SQL's query optimization engine that performs various transformations to optimize logical plans:

```
+---------------------+       +---------------------+       +---------------------+
|   Unresolved        |       |   Analyzed          |       |   Optimized         |
|   Logical Plan      | -->   |   Logical Plan      | -->   |   Logical Plan      |
+---------------------+       +---------------------+       +---------------------+
         |                            |                            |
         V                            V                            V
+---------------------+       +---------------------+       +---------------------+
|   Physical Plans    | -->   |   Code Generation   | -->   |   Execution         |
+---------------------+       +---------------------+       +---------------------+
```

**Optimization Techniques:**
- Predicate pushdown
- Constant folding
- Projection pruning
- Join reordering
- Null propagation

### Tungsten Execution Engine

Tungsten improves Spark's execution performance by:
- Off-heap memory management
- Cache-aware computation
- Code generation

## Working with Data Sources

Spark SQL supports numerous data formats:

| Format | Description | Advantages |
|--------|-------------|------------|
| Parquet | Columnar storage | Efficient compression, predicate pushdown |
| JSON | Semi-structured data | Human-readable, widely used |
| CSV | Tabular data | Simple, compatible with many tools |
| Avro | Row-based format | Schema evolution, compact binary format |
| ORC | Optimized columnar | Better compression than Parquet for some workloads |

**Reading Data Example:**
```python
# Read JSON file
df_json = spark.read.json("data.json")

# Read Parquet file
df_parquet = spark.read.parquet("data.parquet")

# Read CSV with options
df_csv = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("data.csv")
```

## SQL Operations

### Basic SQL Queries

You can register DataFrames as temporary views and run SQL queries:

```python
# Create DataFrame
df = spark.read.json("employees.json")

# Register as temporary view
df.createOrReplaceTempView("employees")

# Run SQL query
result = spark.sql("SELECT name, department FROM employees WHERE salary > 50000")
result.show()
```

### Built-in Functions

Spark SQL provides numerous built-in functions for data manipulation:

**String Functions:** `concat`, `substring`, `lower`, `upper`, `trim`
**Date Functions:** `current_date`, `date_add`, `date_sub`, `datediff`
**Math Functions:** `round`, `ceil`, `floor`, `abs`
**Aggregate Functions:** `count`, `sum`, `avg`, `min`, `max`

```python
from pyspark.sql.functions import col, avg, count

# Aggregate operations
df.groupBy("department") \
  .agg(avg("salary").alias("avg_salary"), 
       count("id").alias("employee_count")) \
  .show()
```

### Window Functions

Window functions perform calculations across related rows without collapsing them:

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, desc

windowSpec = Window.partitionBy("department").orderBy(desc("salary"))

df.withColumn("rank", rank().over(windowSpec)) \
  .filter(col("rank") <= 3) \
  .show()
```

## Performance Optimization

### Caching and Persistence

```python
# Cache DataFrame in memory
df.cache()

# Persist with specific storage level
from pyspark.storagelevel import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK)
```

### Partitioning and Bucketing

**Partitioning:** Divides data based on column values
**Bucketing:** Groups data into fixed number of buckets

```python
# Write with partitioning
df.write.partitionBy("department", "year").parquet("partitioned_data")

# Write with bucketing
df.write.bucketBy(10, "department").saveAsTable("bucketed_table")
```

### Broadcast Joins

For joining large with small tables, use broadcast joins:

```python
from pyspark.sql.functions import broadcast

# Broadcast the smaller DataFrame
result = large_df.join(broadcast(small_df), "join_key")
```

## Integration with Other Spark Components

### Spark Streaming Integration

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Define schema for streaming data
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

# Read streaming data
streaming_df = spark.readStream \
    .schema(schema) \
    .json("streaming_data/")

# Process with SQL
streaming_df.createOrReplaceTempView("streaming_table")
result = spark.sql("SELECT city, AVG(age) FROM streaming_table GROUP BY city")
```

### MLlib Integration

```python
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Prepare features using SQL transformations
feature_df = spark.sql("""
    SELECT age, experience, education_level, salary 
    FROM employee_data 
    WHERE salary IS NOT NULL
""")

# Use with MLlib
assembler = VectorAssembler(
    inputCols=["age", "experience", "education_level"],
    outputCol="features"
)

lr = LinearRegression(featuresCol="features", labelCol="salary")
```

## Hive Integration

Spark SQL provides complete compatibility with Apache Hive:

```python
# Enable Hive support
spark = SparkSession.builder \
    .appName("HiveExample") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

# Query Hive tables
spark.sql("SELECT * FROM hive_table").show()
```

## Advanced Features

### User-Defined Functions (UDFs)

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define UDF
def categorize_age(age):
    if age < 30: return "Young"
    elif age < 50: return "Middle-aged"
    else: return "Senior"

# Register UDF
categorize_age_udf = udf(categorize_age, StringType())

# Use UDF
df.withColumn("age_category", categorize_age_udf(col("age"))).show()
```

### Structured Streaming with Spark SQL

```python
# Read streaming data
streaming_df = spark.readStream.json("streams/")

# Create temporary view
streaming_df.createOrReplaceTempView("streaming_events")

# Run continuous SQL query
result = spark.sql("""
    SELECT window.time, COUNT(*) as event_count
    FROM streaming_events
    GROUP BY window(timestamp, '1 hour')
""")

# Write output stream
query = result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()
```

## Best Practices

1. **Use Schema Inference Carefully**: For production code, define explicit schemas
2. **Leverage Catalyst Optimizer**: Write queries that can be optimized (avoid UDFs when possible)
3. **Monitor Query Plans**: Use `df.explain()` to understand execution plans
4. **Choose Appropriate Storage Format**: Use columnar formats (Parquet, ORC) for analytical workloads
5. **Manage Memory Efficiently**: Use appropriate persistence levels and monitor memory usage

## Exam Tips

1. **Remember the Hierarchy**: SparkSession → DataFrame/Dataset → Logical Plan → Physical Plan
2. **Understand Lazy Evaluation**: Operations are only executed when an action is called
3. **Know the Difference**: DataFrames (untyped) vs Datasets (typed)
4. **Catalyst Optimizer**: Be familiar with its optimization techniques
5. **Integration Points**: Understand how Spark SQL works with Streaming, MLlib, and Hive
6. **Performance Tuning**: Know when to use caching, partitioning, and broadcast joins
7. **SQL Syntax**: Practice common SQL patterns and window functions
8. **Error Handling**: Understand common errors like schema mismatches and type conversions