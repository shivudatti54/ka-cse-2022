# **TB1: Ch 5: 5.1- Big Data Analytics**

## **5.1 Introduction to Hadoop**

### What is Hadoop?

Hadoop is an open-source, distributed computing framework that enables the processing and storage of large amounts of data in a scalable and fault-tolerant manner. It was created by Doug Cutting and Mike Cafarella in 2005.

### Why Hadoop?

- **Scalability:** Hadoop can handle large amounts of data by distributing it across a cluster of nodes, making it suitable for big data analytics.
- **Flexibility:** Hadoop supports various data formats and can be used with different programming languages.
- **Cost-effectiveness:** Hadoop is open-source and can be run on commodity hardware, making it a cost-effective solution.

### Why Not RDBMS?

Relational Database Management Systems (RDBMS) are designed for structured data and are not suitable for big data analytics due to their:

- **Scalability limitations:** RDBMS can become bottlenecked as the volume of data increases.
- **Data schema limitations:** RDBMS require a predefined schema, which can be inflexible for unstructured or semi-structured data.

### RDBMS vs Hadoop

| **Characteristics** | **RDBMS**           | **Hadoop**                        |
| ------------------- | ------------------- | --------------------------------- |
| **Data structure**  | Structured data     | Unstructured/semi-structured data |
| **Scalability**     | Limited scalability | Scalable                          |
| **Data schema**     | Predefined schema   | No predefined schema              |
| **Cost**            | Commercial licenses | Open-source                       |

**5.1.1 History of Hadoop**

- **2005:** Doug Cutting and Mike Cafarella created Hadoop.
- **2006:** Google, Yahoo!, and Amazon joined the Apache Hadoop project.
- **2009:** Hadoop 0.9 was released.
- **2010:** Hadoop 1.0 was released.
- **2011:** Hadoop 2.0 was released.

## Key Concepts

- **Distributed computing:** Hadoop's distributed architecture allows it to process large amounts of data in parallel.
- **MapReduce:** A programming model used for processing data in Hadoop.
- **Data processing pipeline:** A series of data processing tasks that are executed in sequence.
