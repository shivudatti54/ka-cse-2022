# Module 2: Introducing Hadoop

## 1. Introduction

In the era of Big Data, traditional systems like RDBMS face significant challenges in storing and processing massive volumes of unstructured or semi-structured data. They are often expensive, scale vertically (which has a limit), and are not designed for distributed data processing. **Hadoop** emerged as a groundbreaking open-source framework from the Apache Software Foundation, specifically designed to overcome these exact challenges. It provides a cost-effective, scalable, and fault-tolerant platform for distributed storage and processing of vast datasets across clusters of commodity hardware.

## 2. Core Concepts of Hadoop

Hadoop's power lies in its core components and its fundamental approach to data processing.

### 2.1 Hadoop Ecosystem

Hadoop is not a single tool but an ecosystem of interrelated components. The two most fundamental components are:

*   **HDFS (Hadoop Distributed File System):** This is Hadoop's storage layer. It is designed to store very large files reliably across multiple machines.
    *   **How it works:** A large file is broken down into smaller blocks (typically 128 MB or 256 MB). These blocks are distributed and replicated across different nodes in the cluster (default replication factor is 3). This ensures both high throughput access and fault tolerance—if one node fails, data is not lost as copies exist elsewhere.
    *   **Architecture:** It follows a master/slave architecture.
        *   **Namenode (Master):** Manages the filesystem namespace (e.g., the directory tree) and regulates access to files. It stores metadata (like which blocks belong to which file and where they are located).
        *   **Datanode (Slave):** Stores the actual data blocks and serves read/write requests from clients.

*   **MapReduce:** This is Hadoop's processing layer. It is a programming model for processing large datasets in parallel by dividing the work into a set of independent tasks.
    *   **How it works:** Processing happens in two main phases:
        1.  **Map Phase:** The input data is split and processed by "Mapper" tasks. Each Mapper processes a single split and produces a set of intermediate key-value pairs.
        2.  **Reduce Phase:** The intermediate key-value pairs are shuffled, sorted, and then processed by "Reducer" tasks. Each Reducer works on a set of values for a specific key, aggregating or summarizing them to produce the final output.
    *   **Example:** To count the frequency of all words in a large collection of text files:
        *   **Mapper:** Reads a line of text, splits it into words, and emits `(word, 1)` for each word.
        *   **Reducer:** Receives a `(key, list_of_values)` pair, e.g., `("the", [1, 1, 1, 1])`, and sums the values, emitting `("the", 4)`.

### 2.2 YARN (Yet Another Resource Negotiator)

As Hadoop evolved, MapReduce was recognized as being tightly coupled with the resource management functionality. **YARN** was introduced to separate these concerns, acting as the operating system for Hadoop. It is the cluster resource management layer.

*   **Function:** YARN manages and schedules resources (CPU, memory) across the cluster and arbitrates them among various competing applications (not just MapReduce, but also Spark, Tez, etc.).
*   **Architecture:**
    *   **ResourceManager (Master):** The ultimate authority that allocates resources to all running applications.
    *   **NodeManager (Slave):** Runs on each machine in the cluster and is responsible for managing resources (containers) on that single node.
    *   **ApplicationMaster:** Manages the lifecycle of a single application (e.g., a specific MapReduce job), negotiating resources from the ResourceManager and working with NodeManagers to execute and monitor tasks.

## 3. Key Hadoop Daemons (Services)

A typical Hadoop cluster runs the following daemons:
*   **Namenode:** Master daemon for HDFS.
*   **Secondary Namenode:** Helper daemon for the primary Namenode (not a backup).
*   **Datanode:** Slave daemon for HDFS on each worker node.
*   **ResourceManager:** Master daemon for YARN.
*   **NodeManager:** Slave daemon for YARN on each worker node.

## 4. Key Advantages of Hadoop

1.  **Scalability:** Scales *horizontally* by simply adding more commodity machines to the cluster. This is more cost-effective and flexible than vertical scaling.
2.  **Fault Tolerance:** Data is automatically replicated across the cluster. If a node fails, processing is redirected to another node containing a copy of the data, and the work continues without significant interruption.
3.  **Cost-Effective:** Built to run on cheap, commodity hardware rather than expensive, specialized mainframes.
4.  **Flexibility:** Can store and process diverse data (structured, unstructured, log files, social media data, etc.) without needing a predefined schema.

## 5. Summary

| Key Point | Description |
| :--- | :--- |
| **What it is** | An open-source framework for distributed storage and processing of big data. |
| **Core Components** | **HDFS** (storage) and **MapReduce/YARN** (processing & resource management). |
| **Architecture** | Master/Slave architecture (Namenode/Datanode, ResourceManager/NodeManager). |
| **Data Handling** | Breaks data into blocks, distributes, and replicates them across a cluster. |
| **Processing Model** | Uses MapReduce for parallel processing of data where it is stored (data locality). |
| **Key Advantages** | Scalability, Fault Tolerance, Cost-Effectiveness, and Flexibility. |

Hadoop provides the foundational layer upon which the entire modern Big Data ecosystem is built, enabling the analysis of datasets that were previously too large or complex to handle.