# Apache Hadoop

=====================================

### Overview

Apache Hadoop is an open-source distributed computing framework designed to store and process massive datasets across clusters of commodity hardware. It provides the infrastructure for scalable, fault-tolerant big data processing essential for IoT analytics.

### Key Points

- **Core Components:** HDFS (distributed storage), YARN (resource management), MapReduce (processing model), and Hadoop Common (utilities)
- **HDFS Architecture:** NameNode (master) manages metadata and namespace; DataNodes (workers) store actual data blocks
- **Block Storage:** Files split into 128MB blocks by default, replicated 3 times across DataNodes for fault tolerance
- **YARN Components:** ResourceManager (global scheduler), NodeManager (per-node agent), ApplicationMaster (per-app coordinator), Container (resource unit)
- **Rack Awareness:** HDFS places 2 replicas on the same rack and 1 on a different rack for optimal fault tolerance
- **Key Advantages:** Horizontal scalability, fault tolerance via replication, cost-effectiveness with commodity hardware, data locality optimization
- **Key Limitations:** High latency (batch only), small files problem (NameNode memory), no real-time processing, programming complexity

### Important Concepts

- NameNode stores file-to-block mapping and metadata; DataNodes send heartbeats every 3 seconds
- HDFS follows write-once-read-many model optimized for streaming reads
- YARN separates resource management from processing, enabling multiple frameworks on one cluster
- Schema-on-read approach allows flexible storage of structured, semi-structured, and unstructured data

### Notes

- HDFS NameNode vs DataNode responsibilities are a common exam question; know their distinct roles clearly
- Understand the YARN workflow: Client submits to ResourceManager, ApplicationMaster negotiates resources, tasks execute in Containers
- Hadoop vs Traditional RDBMS comparison (schema-on-read vs schema-on-write, horizontal vs vertical scaling) is frequently tested
