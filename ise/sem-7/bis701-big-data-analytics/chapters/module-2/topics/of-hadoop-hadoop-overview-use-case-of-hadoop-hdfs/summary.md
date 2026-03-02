# **Hadoop Overview and Revision Notes**

### Key Points

- **What is Hadoop?**
  - A distributed computing framework for processing large data sets
  - Open-source, Java-based framework
- **Why Hadoop?**
  - Handles large data volumes and high scalability
  - Cost-effective and flexible
- **Why not RDBMS?**
  - Not designed for big data analytics
  - Limited scalability and capacity
- **RDBMS vs Hadoop**
  - Relational databases (RDBMS) vs Hadoop (NoSQL)
  - RDBMS: designed for structured data, limited scalability
  - Hadoop: designed for unstructured and semi-structured data, high scalability

### Hadoop Use Cases

- **Data Warehousing**: storing and managing large volumes of data
- **Data Mining**: processing and analyzing large datasets
- **Data Integration**: combining data from various sources
- **Data Security**: protecting sensitive data

### HDFS (Hadoop Distributed File System)

- **Definition**: a distributed file system for storing and retrieving large data sets
- **Key Features**:
  - Scalable and fault-tolerant
  - Distributed architecture
  - Supports large data sets
- **Components**:
  - NameNode (NN)
  - DataNode (DN)
  - BlockManager (BM)

### Processing Data with Hadoop

- **MapReduce**: a programming model for processing data in parallel
- **Steps**:
  1.  Map stage: split data into smaller chunks
  2.  Reduce stage: combine data from multiple maps
- **Example**: word count program
- **Formula**: T = (m \* r) / (s \* c)

### Managing Resources and Applications

- **Resource Management**: managing node resources and application resources
- **Key Concepts**:
  - JobTracker (JT)
  - TaskTracker (TT)
  - ApplicationMaster (AM)
- **Formulas**:
  - (m \* r) / (s \* c) = T
  - (s \* c) / (m \* r) = s

### Important Definitions and Theorems

- **Big Data**: large volumes of data
- **Hadoop Core**: core components of Hadoop
- **Hadoop Ecosystem**: ecosystem of Hadoop components and tools
- **Scalability**: ability to handle large data volumes
- **Fault-Tolerance**: ability to handle node failures
