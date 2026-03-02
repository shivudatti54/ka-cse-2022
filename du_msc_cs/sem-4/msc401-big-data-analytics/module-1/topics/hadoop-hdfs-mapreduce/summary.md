# Hadoop HDFS & MapReduce - Summary

## Key Definitions and Concepts
- **HDFS Block**: Basic storage unit (128MB) replicated across DataNodes
- **MapReduce**: Programming model with map (filter/sort) and reduce (summary) operations
- **YARN**: Resource negotiator separating processing engine from resource management
- **Rack Awareness**: Strategy placing replica blocks in different physical racks

## Important Formulas and Theorems
- **MapReduce Data Flow**: Input → Map → (Combine) → Shuffle → Reduce → Output
- **Replication Storage**: Total = Original Size × Replication Factor
- **CAP Theorem**: HDFS prioritizes Availability & Partition Tolerance (AP system)
- **Data Locality Probability**: P = min(1, (Nodes_with_Data / Total_Nodes))

## Key Points
- HDFS NameNode stores metadata; DataNodes store actual blocks
- MapReduce's shuffle phase is most network-intensive
- YARN allows multiple processing engines (Spark, Tez) on same cluster
- Erasure coding in Hadoop 3 reduces storage overhead by 50%
- Optimal block size balances disk seeks and parallelism
- Speculative execution duplicates slow tasks across nodes
- HDFS federation scales metadata management horizontally

## Common Mistakes to Avoid
- Using MapReduce for real-time processing (instead use Spark Streaming)
- Setting replication factor >5 (causes unnecessary network traffic)
- Ignoring combiner optimization for additive operations
- Not configuring rack awareness in large clusters
- Using TextInputFormat for binary files

## Revision Tips
1. Practice drawing HDFS write pipeline with 3 DataNodes
2. Memorize MapReduce phase order using "IMSCRO" acronym (Input-Map-Shuffle-Combine-Reduce-Output)
3. Compare HDFS with AWS S3 in terms of consistency models
4. Solve previous years' DU questions on calculating storage needs with varying replication factors

Length: 720 words