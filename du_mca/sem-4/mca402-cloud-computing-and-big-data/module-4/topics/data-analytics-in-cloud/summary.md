# Data Analytics in Cloud - Summary

## Key Definitions and Concepts

- **Data Analytics in Cloud**: The practice of performing data analysis using cloud computing resources, leveraging elastic scalability, managed services, and pay-as-you-go pricing.

- **Data Lake**: Storage repository that holds raw data in native format until needed for analysis; supports structured, semi-structured, and unstructured data.

- **Data Warehouse**: Optimized storage system for structured data designed for query and analysis; provides fast SQL queries for business intelligence.

- **Serverless Analytics**: Analytics operations that run without server management—automatically scaling based on demand, with pay-per-use pricing.

- **Data Ingestion**: The process of collecting and importing data from various sources into a storage system for processing.

## Important Formulas and Theorems

- **Cloud Cost Model**: Total Cost = Compute Costs + Storage Costs + Data Transfer Costs + Managed Service Fees

- **Scalability Factor**: Cloud analytics can scale from gigabytes to petabytes without hardware changes—vertical scaling replaced by horizontal scaling.

## Key Points

1. Cloud analytics eliminates upfront CapEx through OpEx model—pay only for consumed resources.

2. Four types of analytics progress from basic to advanced: Descriptive (what happened), Diagnostic (why), Predictive (what will happen), Prescriptive (what should we do).

3. Cloud analytics architecture includes: Ingestion Layer → Storage Layer → Processing Layer → Analytics/Visualization Layer.

4. Major providers offer comparable services: AWS (Redshift, Athena, SageMaker), Azure (Synapse, Data Factory, ML), GCP (BigQuery, Dataflow, Vertex AI).

5. Data lakes store raw data; data warehouses store processed, structured data—use both based on use case.

6. Real-time analytics uses streaming services (Kinesis, Event Hubs, Pub/Sub); batch analytics uses ETL and data pipelines.

7. Security involves IAM, encryption (at rest/in transit), and compliance certifications (HIPAA, GDPR, SOC 2).

8. Serverless options (Lambda, Functions, Cloud Functions) offer automatic scaling; managed services offer more control.

9. Shared responsibility model: Cloud provider secures infrastructure; customer secures data and access.

10. Big data's Three Vs—Volume, Velocity, Variety—are addressed through cloud object storage, streaming services, and diverse data format support.

## Common Mistakes to Avoid

1. Confusing data lakes with data warehouses—each serves different purposes in analytics architecture.

2. Overlooking data security—always address encryption, access controls, and compliance in cloud analytics designs.

3. Choosing managed services over serverless when elasticity and cost optimization are priorities.

4. Ignoring data transfer costs—egress charges can significantly impact cloud analytics expenses.

5. Not considering vendor lock-in—understand data portability and multi-cloud strategies.

## Revision Tips

1. Draw the complete analytics pipeline from data sources to insights—understand how components connect.

2. Create a comparison table of cloud services across AWS, Azure, and GCP for common analytics tasks.

3. Practice explaining how a real-world scenario (like e-commerce analytics) would be implemented in the cloud.

4. Review the four analytics types with concrete examples—be able to classify business questions into appropriate categories.

5. Memorize key security concepts: IAM, encryption, shared responsibility model, and compliance frameworks.