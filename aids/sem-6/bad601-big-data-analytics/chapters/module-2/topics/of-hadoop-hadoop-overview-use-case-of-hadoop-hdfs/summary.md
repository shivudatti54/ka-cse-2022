# Summary and Revision Notes: Hadoop

=====================================

### Introduction to Hadoop

- Hadoop is an open-source, distributed computing framework used for processing large datasets.
- It is designed to handle massive amounts of data across a cluster of computers.
- Hadoop is the perfect solution for big data analytics tasks.

### Why Hadoop?

- Hadoop is chosen over RDBMS for several reasons:
  - Handles large amounts of data that don't fit in traditional databases.
  - Can process data in real-time.
  - Provides high scalability and fault tolerance.

### Why Not RDBMS?

- RDBMS (Relational Database Management System) is not suitable for big data analytics due to:
  - Limited storage capacity and scalability.
  - Lack of support for parallel processing.

### Hadoop Overview

- Hadoop consists of:
  - HDFS (Hadoop Distributed File System): a distributed storage system.
  - MapReduce: a programming model and software framework.
  - YARN (Yet Another Resource Negotiator): a resource management layer.

### Use Cases of Hadoop

- Hadoop is used in various industries, including:
  - Data warehousing and business intelligence.
  - Real-time analytics and reporting.
  - Machine learning and predictive analytics.

### HDFS (Hadoop Distributed File System)

- HDFS is a distributed file system that:
  - Allows for the storage and retrieval of large amounts of data.
  - Provides high availability and fault tolerance.

### Formulas and Definitions

- **Data Ingestion Rate**: The rate at which data is ingested into HDFS.
- **Data Storage Capacity**: The amount of data that can be stored in HDFS.
- **MapReduce**: A programming model and software framework for processing data in parallel.

### Processing Data with Hadoop

- Hadoop uses the MapReduce programming model to process data in parallel.
- MapReduce consists of two stages:
  - Map: breaks down data into smaller chunks.
  - Reduce: combines the output from the Map stage.

### Managing Resources and Applications

- Hadoop uses the YARN resource management layer to manage resources.
- YARN provides:
  - Resource allocation and deallocation.
  - Job scheduling and monitoring.

### Important Theorems

- **MapReduce Theorem**: The output of the Map stage is equivalent to the input of the Reduce stage.
- **Data Processing Theorem**: Hadoop can process large amounts of data in parallel using the MapReduce programming model.
