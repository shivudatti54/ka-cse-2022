# HDFS (Hadoop Distributed File System)

## Introduction to HDFS

The Hadoop Distributed File System (HDFS) is the primary storage system used by the Hadoop ecosystem. It is a distributed, scalable, and fault-tolerant file system designed to run on commodity hardware. HDFS is optimized for storing very large files (terabytes to petabytes) and providing high-throughput access to data, making it ideal for batch processing workloads typical in big data analytics.

HDFS is based on the **Google File System (GFS)** paper and embodies a "write-once, read-many" model. This means data is written to the cluster once and then read many times for analysis, which simplifies data coherency and enables high throughput.

## Core Architecture

HDFS follows a master-slave architecture. The two main types of daemons (background processes) are the **NameNode** (master) and the **DataNode** (slave).

### NameNode (The Master)

The NameNode is the central controller and manager of the HDFS cluster. It does not store the actual file data; instead, it manages the file system's metadata and namespace.

**Key Responsibilities:**
*   **Metadata Management:** Stores the entire filesystem tree (directory hierarchy) and the metadata (like file names, permissions, ownership) for all files and directories.
*   **Namespace Operations:** Manages operations like opening, closing, and renaming files and directories.
*   **Block Mapping:** Keeps a record of which blocks (pieces of a file) are stored on which DataNodes. This mapping is stored in memory for fast access.
*   **Client Coordination:** Clients communicate with the NameNode to get the location of data blocks before reading or writing files.

The NameNode is a **single point of failure** in a basic HDFS setup. Its metadata is critical. To ensure resilience, the metadata is persistently stored on the local disk in two forms:
1.  `fsimage`: A checkpoint of the entire filesystem namespace.
2.  `edits`: A transaction log that records all changes to the filesystem since the last `fsimage` was created.

A secondary NameNode (often misunderstood as a backup) periodically merges the `fsimage` and `edits` log to prevent the log from becoming too large, but it does not provide failover capability. For high availability (HA), an Active/Standby NameNode configuration with a Quorum Journal Manager (QJM) is used.

### DataNode (The Slaves)

DataNodes are the workhorses of the cluster. There are typically many DataNodes, one per node in the cluster.

**Key Responsibilities:**
*   **Data Storage:** Store and retrieve actual file data blocks.
*   **Block Operations:** Perform operations like creating, deleting, and replicating blocks upon instruction from the NameNode.
*   **Heartbeats:** Send periodic heartbeats (every 3 seconds by default) to the NameNode to report their health and availability.
*   **Block Reports:** Periodically send a full list of all blocks they are storing to the NameNode.

If a DataNode fails to send a heartbeat, the NameNode marks it as dead and initiates replication of its blocks to other healthy DataNodes to maintain the desired replication factor.

## Data Organization: Blocks and Replication

### Blocks
Unlike traditional file systems that use small block sizes (e.g., 4KB), HDFS uses very large block sizes, typically **128MB** or **256MB**. This design has significant advantages:
*   **Reduces Metadata Overhead:** Fewer blocks mean less metadata for the NameNode to manage, allowing it to scale to manage billions of files.
*   **Improves Data Transfer:** Large blocks minimize the seek time overhead compared to the time spent transferring data, leading to higher overall throughput.

A file larger than the block size is split into multiple 128MB blocks. The last block of a file will often be smaller.

```
+----------------------+  File (e.g., 500MB)
|      Block 1         |  --> 128MB
+----------------------+
|      Block 2         |  --> 128MB
+----------------------+
|      Block 3         |  --> 128MB
+----------------------+
|      Block 4         |  --> 116MB (Remaining data)
+----------------------+
```

### Replication
HDFS is fault-tolerant because it replicates data blocks across multiple DataNodes. The **replication factor** (default is 3) is configurable per file.

**Replication Strategy:**
The NameNode makes replication decisions based on a policy to maximize reliability and availability while optimizing network bandwidth.

1.  **First Replica:** Placed on the node where the write request originated (the client node).
2.  **Second Replica:** Placed on a node in a different **rack** than the first replica.
3.  **Third Replica:** Placed on a different node within the **same rack** as the second replica.
4.  **Additional Replicas:** Placed on random nodes, with a strict limit of one replica per node.

This strategy provides a good balance:
*   **Write Optimization:** Writes only traverse one inter-rack switch (from client rack to another rack).
*   **Fault Tolerance:** Data survives the loss of an entire rack.
*   **Read Performance:** Reads can be served from multiple racks, improving bandwidth.

```
Rack 1                          Rack 2
+------------+  +------------+  +------------+
| DataNode A |  | DataNode B |  | DataNode C |
| Block: B1R1|  | Block: B1R3|  | Block: B1R2|
+------------+  +------------+  +------------+
      |                 |               |
      +-----------------+---------------+
                Switch / Network
```

*Diagram: Replication of a block (B1) across two racks. R1, R2, R3 represent replicas.*

## HDFS Read/Write Operations

### Writing a File
1.  The client contacts the NameNode to request a file write.
2.  The NameNode checks permissions and creates an entry in the filesystem metadata. It then provides the client with a list of DataNodes (a pipeline) to write the data to.
3.  The client starts writing data to the first DataNode in the pipeline.
4.  The first DataNode receives the data, stores it, and forwards it to the second DataNode.
5.  The second DataNode does the same, forwarding it to the third, and so on, until all replicas are written.
6.  The pipeline is acknowledged back to the client. The client then closes the file, notifying the NameNode that the write is complete.

```
Client -> NameNode: "I want to write file.log"
NameNode -> Client: "Ok, write to DN1, DN2, DN3"
Client -> DN1: (Sends data packet)
DN1 -> DN2: (Forwards data packet)
DN2 -> DN3: (Forwards data packet)
DN3 -> DN2: (Ack)
DN2 -> DN1: (Ack)
DN1 -> Client: (Ack)
Client -> NameNode: "Write is finished"
```

### Reading a File
1.  The client contacts the NameNode, requesting the locations of the blocks for a specific file.
2.  The NameNode returns the addresses of the DataNodes (typically multiple per block) that hold the requested blocks, sorted by network proximity to the client.
3.  The client connects directly to the closest DataNode and begins reading data sequentially.
4.  After reading a block, the client closes the connection to that DataNode and finds the best DataNode for the next block.

This design allows HDFS to scale read throughput by the number of DataNodes in the cluster.

## Key Features and Characteristics

| Feature | Description | Benefit |
| :--- | :--- | :--- |
| **Fault Tolerance** | Automatic detection of node failures and re-replication of data from healthy nodes. | High availability and data durability. |
| **Scalability** | Scale out by adding more DataNodes to the cluster. NameNode scales vertically (more RAM). | Handles petabytes of data across thousands of nodes. |
| **High Throughput** | Optimized for large, sequential reads and writes rather than low-latency access. | Ideal for MapReduce, Spark, and other batch processing frameworks. |
| **Data Locality** | Computation is moved to the data rather than moving data to the computation. | Reduces network congestion and increases throughput. |
| **Portability** | Written in Java, HDFS can be deployed on a wide range of hardware and operating systems. | Runs on commodity hardware, reducing cost. |

## HDFS Federation and High Availability

### Federation
As a cluster grows, the single NameNode's memory becomes a limiting factor. **HDFS Federation** introduces multiple independent NameNodes/namespaces that manage different parts of the filesystem. These NameNodes are federated; they are independent and don't coordinate with each other. All DataNodes store blocks for all NameNodes. This allows horizontal scaling of the namespace.

### High Availability (HA)
In a basic setup, the NameNode is a single point of failure. **HDFS High Availability** eliminates this by allowing two NameNodes in an active-standby configuration. The Standby NameNode has an up-to-date copy of the metadata. If the Active NameNode fails, the Standby quickly (in tens of seconds) takes over its responsibilities. This requires a shared storage (like NFS or QJM) for the `edits` log and a ZooKeeper ensemble for coordination.

## HDFS Commands
HDFS can be interacted with via a command-line interface similar to Linux shell commands.

```bash
# Basic File Operations
hdfs dfs -ls /user/data          # List files
hdfs dfs -mkdir /user/newdir     # Create directory
hdfs dfs -put localfile.txt /user/data/ # Copy from local to HDFS
hdfs dfs -get /user/data/file.txt .     # Copy from HDFS to local
hdfs dfs -cat /user/data/file.txt       # Display file content

# Administrative Commands
hdfs dfsadmin -report           # Get a cluster status report
hdfs fsck /path -files -blocks # Check the health of files and blocks
```

## HDFS in the Big Data Ecosystem
HDFS is the foundational layer for many other tools in the Hadoop ecosystem:
*   **MapReduce/Spark:** Read input data from and write output data to HDFS.
*   **Apache Hive:** Stores its data warehouses (tables) as files in HDFS.
*   **Apache HBase:** Can use HDFS as its underlying durable storage layer.
*   **Apache Flume/Kafka:** Often used to ingest data streams into HDFS for batch analysis.

## Exam Tips
1.  **Memorize the Roles:** Be crystal clear on the distinct responsibilities of the NameNode (metadata manager) vs. DataNode (data storage). This is a common source of exam questions.
2.  **Understand Replication:** Know the default replication factor (3) and the logic behind the placement strategy (one on local node, one on different rack, one on same rack as second). Be able to explain *why* this strategy is used.
3.  **Block Size Reasoning:** Be prepared to explain why HDFS uses such large block sizes (reduces metadata, improves throughput) compared to traditional filesystems.
4.  **Single Point of Failure:** Remember that the basic NameNode is a SPOF. Understand the concepts of Federation (scaling namespace) and HA (providing failover) as solutions.
5.  **Write-Once Model:** HDFS is optimized for appending to files but not for arbitrary, low-latency updates. This is a key design trade-off.