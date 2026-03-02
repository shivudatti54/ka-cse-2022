# Public Cloud Platforms: GAE, AWS and Azure

## Overview

Public cloud platforms provide on-demand computing resources over the internet, operated by third-party providers. The three major platforms are Google App Engine (GAE) as PaaS, Amazon Web Services (AWS) as comprehensive IaaS/PaaS/SaaS, and Microsoft Azure with strong hybrid cloud and enterprise integration capabilities.

## Key Points

- **Google App Engine (GAE)**: Fully managed PaaS with automatic scaling, built-in services (Datastore, Memcache, Task Queues); supports Python, Java, Go, PHP, Node.js, Ruby; two environments - Standard (sandboxed, fast) and Flexible (Docker containers, more customization)
- **AWS (Amazon Web Services)**: Market leader launched 2006 with broadest service portfolio (200+ services); flagship services include EC2 (IaaS VMs), Lambda (serverless), S3 (object storage), RDS (managed databases), DynamoDB (NoSQL)
- **Microsoft Azure**: Second-largest platform launched 2010; hybrid cloud leader with Azure Arc; deep integration with Microsoft ecosystem (Active Directory, Windows Server, .NET, Office 365); strong PaaS with Azure App Service
- **GAE Auto-Scaling**: Automatically scales instances based on traffic and can scale to zero when no traffic, reducing costs
- **GAE Built-in Services**: Datastore (NoSQL), Memcache (caching), Task Queues (async processing), URL Fetch (HTTP client), Blobstore (large files), Users API (authentication)
- **AWS Global Infrastructure**: Largest number of Regions and Availability Zones worldwide for low-latency access and disaster recovery
- **Azure Hybrid Strength**: Seamless integration between on-premises and cloud resources using Azure ExpressRoute and Azure Arc

## Important Concepts

- GAE is PaaS (no server management, deploy code only) vs. AWS EC2 is IaaS (full OS control, SSH access)
- Service equivalents: GAE Datastore ~ AWS DynamoDB ~ Azure Cosmos DB; S3 ~ Blob Storage ~ Cloud Storage
- Deployment lifecycle for GAE: Develop with SDK → Test locally → Configure (app.yaml) → Deploy (gcloud) → Auto-scaling in production
- Three-tier architecture matters: Access Layer (ToR switches) → Aggregation Layer → Core Layer for understanding cloud infrastructure
- Pay-as-you-go pricing models: AWS per-second/hour, Azure per-minute, GAE per instance-hour plus API calls

## Notes

- Remember GAE is PaaS, not IaaS - developers deploy code not VMs (key distinction from AWS EC2)
- Know GAE's key built-in services and their purposes for exam questions
- Understand Standard vs. Flexible environments: Standard is sandboxed with fast startup, Flexible uses Docker with more freedom
- AWS is market leader with broadest services; Azure excels at hybrid cloud and Microsoft integration
- Be able to map equivalent services across platforms (EC2 = Azure VMs, S3 = Blob Storage, Lambda = Azure Functions)
- Comparison questions are frequent: be ready to contrast PaaS (GAE) vs. IaaS (EC2) characteristics
