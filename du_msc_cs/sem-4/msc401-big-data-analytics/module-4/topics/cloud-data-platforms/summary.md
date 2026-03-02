# Cloud Data Platforms - Summary

## Key Definitions and Concepts
- **Data Lakehouse**: Combines ACID transactions of data warehouses with scale of data lakes
- **Cold Path**: Batch processing of archival data (>24h latency)
- **Data Mesh**: Domain-oriented decentralized architecture

## Important Formulas and Theorems
- **CAP Theorem**: Consistency, Availability, Partition Tolerance - pick two
- **Little's Law**: L = λW (System throughput optimization)
- **SLA Calculation**: Uptime % = (Total Time - Downtime)/Total Time

## Key Points
- Object storage enables infinite scalability but lacks transactional support
- Databricks Photon engine outperforms vanilla Spark by 4-8x
- GCP's BigLake unifies BigQuery and GCS under single API
- Azure Purview provides automated data lineage tracking
- Always encrypt data in transit (TLS 1.3+) and at rest (AES-256)
- Spot instances can reduce cloud costs by 90% but require fault-tolerant designs
- C5d instances with NVMe storage optimize Spark shuffle operations

## Common Mistakes to Avoid
- Using on-prem security models directly in cloud environments
- Ignoring egress costs in multi-cloud architectures
- Not setting budget alerts leading to cost overruns
- Overlooking clock skew issues in global timestamp ordering

## Revision Tips
1. Practice drawing AWS/GCP architecture diagrams with labels
2. Memorize API rate limits: e.g., S3 3500 PUT requests/sec
3. Use DU's Azure for Education credits for hands-on practice
4. Study research papers: "Snowflake: A Novel Cloud-Native DW" (SIGMOD 2022)

Length: 650 words