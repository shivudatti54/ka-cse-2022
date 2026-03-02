# Introduction to Hadoop Study Material

=====================================

## Table of Contents

1. [Of Hadoop](#of-hadoop)
2. [Hadoop Overview](#hadoop-overview)
3. [Use Case of Hadoop](#use-case-of-hadoop)
4. [HDFS (Hadoop Distributed File System)](#hdfs-hadoop-distributed-file-system)
5. [Processing Data with Hadoop](#processing-data-with-hadoop)
6. [Managing Resources and Applications](#managing-resources-and-applications)

## Of Hadoop

---

### What is Hadoop?

Hadoop is an open-source, distributed computing framework that enables the processing and analysis of large data sets across a cluster of computers. It was created by Doug Cutting and Mike Cafarella and is now maintained by the Apache Software Foundation.

### Why Hadoop?

Hadoop is used for big data processing due to its ability to handle massive amounts of data and scale horizontally. It is particularly useful for processing unstructured and semi-structured data, such as logs, images, and videos.

### Why not RDBMS?

RDBMS (Relational Database Management System) is not suitable for big data processing because it is designed for structured data and has limitations in handling large amounts of unstructured data. Hadoop is more flexible and can handle a wide range of data types.

### RDBMS Vs Hadoop

|                    | RDBMS      | Hadoop                       |
| ------------------ | ---------- | ---------------------------- |
| **Data Structure** | Relational | Distributed                  |
| **Data Type**      | Structured | Unstructured/Semi-structured |
| **Scalability**    | Limited    | Horizontal                   |
| **Cost**           | High       | Low                          |

## Hadoop Overview

---

### Key Components

- **Node**: A single computer in the cluster
- **Cluster**: A group of nodes working together
- **Master**: The node that manages the cluster
- **Slave**: The nodes that perform tasks

### Hadoop Architecture

- **HDFS (Hadoop Distributed File System)**: Stores data across multiple nodes
- **MapReduce**: Processes data in parallel across multiple nodes
- **YARN (Yet Another Resource Negotiator)**: Manages resources and applications

## Use Case of Hadoop

---

### Applications

- **Data Warehousing**: Stores and analyzes large amounts of data
- **Data Mining**: Extracts valuable insights from data
- **Machine Learning**: Trains models on large datasets
- **Real-time Analytics**: Processes data in real-time

### Industries

- **Finance**: Analyzes transaction data and market trends
- **Healthcare**: Analyzes medical records and patient data
- **Retail**: Analyzes customer behavior and sales data

## HDFS (Hadoop Distributed File System)

---

### How it Works

- **Data is split into chunks**: Each chunk is stored on multiple nodes
- **Nodes are identified by their IP address**: Data is stored in a distributed manner
- **Data is replicated**: Multiple copies of each chunk are stored for redundancy

### Benefits

- **Scalability**: HDFS can handle massive amounts of data
- **Availability**: Data is available even if some nodes fail
- **Fault tolerance**: Data is replicated for redundancy

## Processing Data with Hadoop

---

### MapReduce

- **Map phase**: Data is split into chunks and processed in parallel
- **Reduce phase**: Results are aggregated and processed in parallel

### Key Concepts

- **Mapper**: Processes data and produces key-value pairs
- **Reducer**: Processes key-value pairs and produces output

### Example

- **Input**: Log data from web servers
- **Mapper**: Extracts relevant data from log files
- **Reducer**: Aggregates data and produces summary statistics

## Managing Resources and Applications

---

### YARN

- **Resource management**: Manages resources such as memory and CPU
- **Application management**: Manages applications and their resources

### Key Concepts

- **ApplicationMaster**: Manages application resources
- **ResourceManager**: Manages resources and applications

### Example

- **Input**: Job submission with resource requirements
- **YARN**: Allocates resources and manages job execution

Note: This study material is a comprehensive overview of the topic and covers key concepts, definitions, and examples. It is intended to serve as a starting point for further learning and exploration of Hadoop and big data analytics.
