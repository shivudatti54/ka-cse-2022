# **TB1: Ch 5: 5.1- Big Data Analytics**

### 5.1 Introduction to Hadoop

## **What is Hadoop?**

Hadoop is an open-source, distributed computing framework designed to process large amounts of data across a cluster of computers. It is written in Java and provides a scalable and fault-tolerant way to process big data.

## **History of Hadoop**

Hadoop was first developed in 2004 by Doug Cutting and Mike Cafarella at the University of California, Berkeley. It was initially called "Nutch," a web crawler, and was later renamed to Hadoop. The first public release of Hadoop was in 2006.

## **Why Hadoop?**

- **Scalability**: Hadoop is designed to handle large amounts of data and scale horizontally, making it suitable for big data analytics.
- **Flexibility**: Hadoop supports a wide range of data formats, including text, image, audio, and video.
- **Cost-effectiveness**: Hadoop is free and open-source, making it an affordable solution for big data analytics.
- **Easy to use**: Hadoop provides a simple and intuitive API, making it easy to use for developers and non-technical users.

### 5.1.1 Key Components of Hadoop

#### 1. Distributed File System (HDFS)

- **Distributed storage**: HDFS stores data across a cluster of computers, making it highly scalable and fault-tolerant.
- **Block-based storage**: HDFS stores data in fixed-size blocks, making it efficient for large data sets.

#### 2. MapReduce

- **Processing framework**: MapReduce is a programming model used to process data in parallel across a cluster of computers.
- **Map phase**: The map phase reads data from HDFS, applies a program to each record, and outputs a set of key-value pairs.
- **Reduce phase**: The reduce phase aggregates the output from the map phase and produces the final output.

#### 3. YARN (Yet Another Resource Negotiator)

- **Resource management**: YARN manages resources, such as CPU and memory, across the Hadoop cluster.
- **Application-level resource management**: YARN provides a secure way to manage resources for MapReduce jobs.

#### 4. Pig

- **High-level data processing**: Pig is a high-level data processing language that allows users to write data processing scripts.
- **Data transformation**: Pig provides a simple and intuitive way to transform and manipulate data.

### 5.1.2 Why Not RDBMS?

---

RDBMS (Relational Database Management System) is a traditional database management system that is not suitable for big data analytics.

- **Scalability**: RDBMS is designed for small to medium-sized data sets and can become sluggish with large data sets.
- **Data format**: RDBMS is optimized for structured data, which is not suitable for big data analytics.
- **Cost-effectiveness**: RDBMS can be expensive to maintain and scale.

### 5.1.3 RDBMS vs Hadoop

---

| Feature                | RDBMS       | Hadoop                           |
| ---------------------- | ----------- | -------------------------------- |
| **Scalability**        | Limited     | Highly scalable                  |
| **Data format**        | Structured  | Unstructured and semi-structured |
| **Cost-effectiveness** | Expensive   | Affordable                       |
| **Data processing**    | Query-based | Data-intensive                   |

### Key Concepts

- **Big data**: Data that is too large to be processed by traditional methods.
- **Hadoop ecosystem**: The set of tools and technologies that make up the Hadoop platform.
- **Distributed computing**: A computing paradigm that spreads tasks across multiple computers.
- **MapReduce**: A programming model used to process data in parallel across a cluster of computers.
- **YARN**: A resource management system that provides application-level resource management for MapReduce jobs.
