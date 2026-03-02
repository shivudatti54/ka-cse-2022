# What is Hive - Summary

## Key Definitions and Concepts

- Apache Hive is an open-source data warehousing and analytics platform built on top of Apache Hadoop
- HiveQL is the SQL-like query language that gets translated into MapReduce, Tez, or Spark jobs
- The Metastore stores metadata about tables, partitions, and schemas separately from actual data
- SerDe (Serializer/Deserializer) handles data format conversion between rows and files

## Important Formulas and Theorems

- Hive translates HiveQL → Abstract Syntax Tree → Logical Plan → Optimized Plan → MapReduce/Tez/Spark jobs
- Partition pruning reduces data scanned by filtering on partition columns
- Bucket join optimization uses the number of buckets to efficiently join large tables

## Key Points

- Hive was originally developed by Facebook and later open-sourced to Apache
- It provides a familiar SQL-like interface for Big Data analysis
- Managed tables are controlled by Hive (data deleted on DROP); external tables reference existing data
- Common file formats: TextFile (default), SequenceFile, RCFile, ORC (optimized row columnar), Parquet (columnar)
- Partitioning organizes data by column values (e.g., date, region) for faster queries
- Bucketing divides data into clusters within partitions using hash functions
- Hive integrates with the broader Hadoop ecosystem including HDFS, YARN, and MapReduce

## Common Mistakes to Avoid

- Confusing managed and external tables—dropping a managed table deletes both metadata and data
- Assuming Hive supports all SQL features—some operations have different semantics
- Not considering file format impact on query performance—columnar formats like ORC/Parquet are better for analytics
- Ignoring partition pruning—queries should filter on partition columns when possible

## Revision Tips

- Draw the Hive architecture diagram showing CLI, Driver, Compiler, Optimizer, and Execution Engine
- Practice writing CREATE TABLE statements with different options (partitioned, external, file formats)
- Remember the query execution flow: Query submission through job execution on Hadoop
- Compare different file formats—know when to use text vs. columnar formats
- Review the distinction between metadata (schema, partitions) and actual data storage