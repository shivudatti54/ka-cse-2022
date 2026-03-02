# **Word Count Program in Hadoop and Spark**

### Overview

- Implementing a word count program in Hadoop and Spark is a fundamental step in big data analytics.
- This summary provides key points and formulas for revising the topic.

### Key Concepts

- **Hadoop**: Distributed computing framework for processing large data sets.
- **Spark**: In-memory data processing engine for Hadoop.
- **Word Count Program**: A program that reads input data, tokenizes words, and counts their occurrences.
- **MapReduce**: A programming model for processing data in parallel across a cluster of nodes.
- **RDD (Resilient Distributed Dataset)**: A Spark object that represents a distributed collection of data.

### Hadoop Implementation

- **MapReduce Steps**:
  - Map: Tokenizes words and generates key-value pairs (word, 1).
  - Reduce: Combines key-value pairs to produce the final word count.
- **Map programming**: Uses a mapper function to process input data.
- **Reduce programming**: Uses a reducer function to combine key-value pairs.

### Spark Implementation

- **RDD API**: Creates an RDD from an input source (e.g., text file).
- **Map**: Applies a transformation function to an RDD.
- **Reduce**: Combines key-value pairs using a combiner function.
- **Spark Core**: Provides the foundation for building Spark applications.

### Important Formulas and Definitions

- **MapReduce Formula**:
  - `Output = (Map \* Reduce) / Map`
- **RDD Formula**:
  - `RDD = map + flatMap + filter + reduce`
- **Key-Value Pair**: A pair consisting of a key and a value.

### Theorems

- **Hadoop's Fault-Tolerant Property**: Ensures that data is not lost in case of node failures.
- **Spark's In-Memory Property**: Enables fast data processing by storing data in memory.

### Quick Revision Tips

- Understand the basic concepts of Hadoop and Spark.
- Familiarize yourself with MapReduce and RDD APIs.
- Practice implementing word count programs in both Hadoop and Spark.
