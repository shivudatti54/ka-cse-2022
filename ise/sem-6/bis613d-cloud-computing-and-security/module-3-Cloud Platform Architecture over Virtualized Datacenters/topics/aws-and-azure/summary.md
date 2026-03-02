# Programming on AWS and Azure

## Overview

Cloud programming represents a shift from traditional development by leveraging scalable, managed services from cloud providers. The programming model is service-oriented and event-driven, where applications are built by composing cloud services via APIs, promoting modularity, scalability, and resilience while focusing on business logic rather than infrastructure management.

## Key Points

- **Shared Responsibility Model**: Cloud provider responsible for security of the cloud (infrastructure); customer responsible for security in the cloud (data, access management, application security)
- **Infrastructure as Code (IaC)**: Write code (JSON, YAML, DSL) to define infrastructure ensuring consistency and repeatability; AWS uses CloudFormation, Azure uses ARM Templates/Bicep
- **Event-Driven Architecture**: Events (file upload, message arrival, scheduled time) trigger code execution; foundation of serverless computing (e.g., S3 upload event triggers Lambda function)
- **AWS Core Services**: Lambda (serverless FaaS), EC2 (virtual servers IaaS), S3 (object storage), EBS (block storage), DynamoDB (NoSQL), RDS (relational database), SQS (message queue), API Gateway (API management)
- **Azure Core Services**: Azure Functions (serverless FaaS), App Service (PaaS web apps), Blob Storage (object storage), Disk Storage (block storage), Cosmos DB (globally distributed NoSQL), Azure SQL Database (relational), Queue Storage (messaging), API Management
- **AWS SDK (Boto3)**: Python SDK for programmatic AWS interaction using default credentials from IAM roles or ~/.aws/credentials
- **Azure SDK**: Python SDK using DefaultAzureCredential supporting multiple auth methods (works on App Service, VMs, locally with Azure CLI)
- **Service Equivalents**: Lambda ↔ Azure Functions, EC2 ↔ Azure VMs, S3 ↔ Blob Storage, DynamoDB ↔ Cosmos DB, RDS ↔ Azure SQL Database

## Important Concepts

- Best practices: Design for failure (retry logic, timeouts), leverage managed services, implement security early (least privilege, secrets management), optimize for cost (auto-scaling), monitor and log from start
- AWS offers extensive service breadth and maturity with most Regions/AZs; Azure excels at Microsoft ecosystem integration and hybrid cloud
- Event-driven pattern example: User uploads image to S3 → S3 ObjectCreated event → Lambda function triggered → Process image → Save thumbnail to another S3 bucket
- IaC enables version control for infrastructure, ensuring reproducible environments across development, staging, and production
- Primary SDK languages: AWS supports Python, JavaScript, Java, Go, .NET; Azure emphasizes .NET, Python, Java, JavaScript, Go

## Notes

- Understand the Shared Responsibility Model clearly - frequently tested on what customer vs. provider manages
- Know core compute, storage, and database services for both platforms with use cases and basic configuration
- IaC is key exam topic - understand CloudFormation and ARM Templates concepts
- Be prepared to identify event-driven serverless architecture scenarios (Lambda/Azure Functions most appropriate)
- Practice mapping AWS services to Azure equivalents and vice versa using comparison tables
- Remember best practices: design for failure, use managed services, implement security early, optimize costs
