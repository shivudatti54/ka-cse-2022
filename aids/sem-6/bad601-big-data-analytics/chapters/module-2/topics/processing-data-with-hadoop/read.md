# Processing Data with Hadoop

## Introduction

For  engineering students, understanding how to process vast amounts of data is a cornerstone of Big Data Analytics. Traditional systems often fail to handle the **Volume** and **Velocity** of big data. Hadoop emerges as a powerful, open-source framework designed to process and store massive datasets across clusters of commodity hardware in a distributed, scalable, and fault-tolerant manner. This module delves into the core components and processes that enable this capability.

## Core Concepts of Hadoop Data Processing

Hadoop's approach to data processing is fundamentally different from traditional systems. Its power lies in its core components: the Hadoop Distributed File System (HDFS) for storage and the MapReduce programming model for processing.

### 1. Hadoop Distributed File System (HDFS)

HDFS is the storage layer of Hadoop. It is designed to store very large files reliably across multiple machines.

*   **Master/Slave Architecture:** HDFS follows a master-slave architecture.
    *   **NameNode (Master):** Manages the file system namespace (metadata) and regulates access to files by clients. It knows which blocks of data belong to which file and on which DataNode they are stored.
    *   **DataNode (Slave):** Stores the actual data blocks and serves read/write requests from clients. There are multiple DataNodes in a cluster.
*   **Data Storage:** Files are broken down into large blocks (typically 128 MB or 256 MB). These blocks are replicated across multiple DataNodes (default replication factor is 3) to ensure fault tolerance. This means if one machine fails, the data is still available on others.
*   **Example:** A 1 GB file is split into 8 blocks (if block size is 128MB). Each block is replicated three times and stored on different DataNodes across the cluster. The NameNode keeps the metadata for this entire operation.

### 2. MapReduce: The Processing Engine

MapReduce is a programming model and an associated implementation for processing and generating large datasets. It works on the principle of **"Divide and Conquer."** A processing job is divided into two main phases: the **Map** phase and the **Reduce** phase.

*   **Map Phase (`Mapper`):**
    *   **Function:** Processes input data. The input data is split and each split is processed by a separate Map task.
    *   **Works on:** A single HDFS block at a time.
    *   **Output:** Key-Value pairs. e.g., `(word, 1)`.
*   **Shuffle and Sort Phase:** This is an intermediate, automatic phase where the framework collects all the key-value pairs from all Mappers, groups them by key, and sorts the values. It then sends these sorted lists to the Reducers.
*   **Reduce Phase (`Reducer`):**
    *   **Function:** Aggregates the results from the Map phase.
    *   **Input:** A key and a list of all values for that key from all Mappers. e.g., `(word, [1, 1, 1])`.
    *   **Output:** Aggregated result. e.g., `(word, 3)`.

#### Example: Word Count Problem

The "Hello World" of MapReduce. The goal is to count the frequency of each word in a large collection of documents.

1.  **Input Splitting:** The large text file is split into logical splits (e.g., by line).
2.  **Mapping:** Each Mapper processes one split.
    *   Input: (Line number, "hello world hello")
    *   Map function outputs: `('hello', 1), ('world', 1), ('hello', 1)`
3.  **Shuffling and Sorting:** The framework groups all values by key.
    *   It creates: `('hello', [1, 1])` and `('world', [1])`
4.  **Reducing:** A Reducer receives each grouped key-list pair.
    *   For `('hello', [1, 1])`, the Reduce function sums the list: outputs `('hello', 2)`
    *   For `('world', [1])`, it outputs `('world', 1)`

### 3. Yet Another Resource Negotiator (YARN)

YARN is the resource management and job scheduling layer of Hadoop (introduced in Hadoop 2.x). It separates the resource management and processing components, making Hadoop more efficient and scalable.

*   **ResourceManager (RM):** The master daemon. It manages the global assignment of compute resources (CPU, memory) to applications.
*   **NodeManager (NM):** The slave daemon on each machine. It manages resources and containers on a single node.
*   **ApplicationMaster (AM):** Manages the lifecycle of a *single application* (e.g., a MapReduce job). It negotiates resources from the RM and works with the NMs to execute and monitor the tasks.

YARN allows Hadoop to run diverse workloads (like Spark, Tez) beyond just MapReduce, making it a truly multi-purpose data processing platform.

## Key Points & Summary

*   **Hadoop** is a framework for distributed storage and processing of big data.
*   **HDFS** provides reliable, scalable storage using a NameNode (master for metadata) and DataNodes (slaves for data storage).
*   **MapReduce** is a programming model for parallel data processing. It involves:
    *   **Map:** Processes data to generate key-value pairs.
    *   **Shuffle & Sort:** Groups intermediate data by key.
    *   **Reduce:** Aggregates the grouped data.
*   **YARN** is the resource manager that allocates resources (CPU, memory) to various applications running on the Hadoop cluster, enabling it to support multiple processing paradigms.
*   The entire process is designed to be **fault-tolerant** (via data replication and task retries) and to **move computation to the data** (processing happens on the node where the data resides, minimizing network traffic).