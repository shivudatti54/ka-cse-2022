# Public Cloud Platforms: GAE, AWS and Azure


## Table of Contents

- [Public Cloud Platforms: GAE, AWS and Azure](#public-cloud-platforms-gae-aws-and-azure)
- [Introduction to Public Cloud Platforms](#introduction-to-public-cloud-platforms)
- [Google App Engine (GAE)](#google-app-engine-gae)
  - [Overview](#overview)
  - [Key Characteristics of GAE](#key-characteristics-of-gae)
  - [GAE Architecture](#gae-architecture)
  - [GAE Built-in Services](#gae-built-in-services)
  - [GAE Application Lifecycle](#gae-application-lifecycle)
  - [Example `app.yaml` Configuration](#example-appyaml-configuration)
- [Amazon Web Services (AWS)](#amazon-web-services-aws)
  - [Overview](#overview)
  - [Key Characteristics](#key-characteristics)
  - [AWS Architecture Example (Web Application)](#aws-architecture-example-web-application)
  - [Core AWS Services](#core-aws-services)
- [Microsoft Azure](#microsoft-azure)
  - [Overview](#overview)
  - [Key Characteristics](#key-characteristics)
  - [Azure Architecture Example (Hybrid)](#azure-architecture-example-hybrid)
  - [Core Azure Services](#core-azure-services)
- [Comparative Analysis: GAE vs AWS vs Azure](#comparative-analysis-gae-vs-aws-vs-azure)
- [Key Differences: PaaS (GAE) vs IaaS (AWS EC2)](#key-differences-paas-gae-vs-iaas-aws-ec2)
- [Exam Tips](#exam-tips)

## Introduction to Public Cloud Platforms

Public Cloud Platforms provide on-demand computing resources and services over the internet, operated by third-party providers. They represent the practical implementation of cloud computing concepts, offering massive scalability, reliability, and a pay-as-you-go economic model. The three major platforms discussed in this context are **Google App Engine (GAE)**, **Amazon Web Services (AWS)**, and **Microsoft Azure**. These platforms allow businesses and developers to build, deploy, and manage applications without the capital expense of owning and maintaining physical hardware.

## Google App Engine (GAE)

### Overview

Google App Engine (GAE) is a **Platform as a Service (PaaS)** offering from Google that allows developers to build and deploy web applications on Google's infrastructure. Launched in 2008, it was one of the earliest cloud platforms. GAE completely abstracts away the underlying infrastructure — developers do not manage servers, virtual machines, or operating system patches. They simply upload their application code, and GAE handles everything else, including provisioning, scaling, load balancing, and health management.

### Key Characteristics of GAE

- **Fully Managed PaaS:** No server management. Developers focus only on code.
- **Automatic Scaling:** GAE automatically scales the number of application instances up or down based on incoming traffic. It can scale down to zero when there is no traffic, reducing costs.
- **Built-in Services:** Provides integrated access to Google services like Datastore, Memcache, Task Queues, and URL Fetch.
- **Language Support:** Supports multiple runtime environments including Python, Java, Go, PHP, Node.js, and Ruby.
- **Two Environments:**
  - **Standard Environment:** Applications run in a sandboxed environment with fast scale-up, automatic scaling to zero, and millisecond startup times. More restrictive but highly optimized.
  - **Flexible Environment:** Applications run in Docker containers on Google Compute Engine VMs, offering more customization (any language, any library, SSH access) but with slightly longer startup times.

### GAE Architecture

```
Developer --> Deploys App (via SDK / gcloud CLI)
| v
+----------------------------------+
| Google App Engine (PaaS) |
| +----------------------------+ |
| | Frontend (HTTP Server) | |
| +----------------------------+ |
| | | | |
| | App | | App | | App |
| | Inst.1 | | Inst.2 | | Inst.N | <- Auto-scaled
| +--------+ +--------+ +--------+ |
| | | | |
| +----------------------------+ |
| | Built-in Services | |
| | Datastore | Memcache |Task |
| | Queues | URL Fetch | Mail |
| +----------------------------+ |
+----------------------------------+
```

### GAE Built-in Services

| Service          | Description                                               | Purpose                                                                                     |
| :--------------- | :-------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **Datastore**    | Schemaless NoSQL database (now Cloud Datastore/Firestore) | Persistent data storage with automatic sharding and replication                             |
| **Memcache**     | Distributed in-memory cache                               | Speed up data retrieval and reduce Datastore reads                                          |
| **Task Queues**  | Asynchronous task execution                               | Offload long-running work (e.g., sending emails, image processing) outside of user requests |
| **URL Fetch**    | HTTP client service                                       | Make outbound HTTP/HTTPS requests to external services                                      |
| **Blobstore**    | Large file storage service                                | Store and serve large objects like images and videos                                        |
| **Users API**    | Authentication service                                    | Integrate with Google Accounts for user login                                               |
| **Mail API**     | Email sending service                                     | Send emails from the application                                                            |
| **Cron Service** | Scheduled task execution                                  | Run tasks at regular intervals (e.g., cleanup jobs, report generation)                      |

### GAE Application Lifecycle

1. **Develop:** Write application code using the App Engine SDK in a supported language (Python, Java, Go, etc.).
2. **Test Locally:** Use the App Engine development server to test the application on the local machine.
3. **Configure:** Define application settings in `app.yaml` (Python/Go) or `appengine-web.xml` (Java), including runtime, URL routing, scaling parameters, and service configurations.
4. **Deploy:** Upload the application to GAE using the `gcloud app deploy` command (or the older `appcfg.py`).
5. **Run and Scale:** GAE automatically handles incoming requests, distributes load across instances, and scales the number of instances based on traffic.

### Example `app.yaml` Configuration

```yml
runtime: python39
entrypoint: gunicorn -b :$PORT main:app
instance_class: F2
automatic_scaling:
  target_cpu_utilization: 0.65
  min_instances: 1
  max_instances: 10
  min_pending_latency: 30ms
  max_pending_latency: automatic
```

## Amazon Web Services (AWS)

### Overview

AWS, launched in 2006, is the market leader and most mature public cloud platform. Unlike GAE's PaaS focus, AWS offers a comprehensive suite spanning **IaaS, PaaS, and SaaS** with over 200 services.

### Key Characteristics

- **Broadest Service Portfolio:** Compute (EC2, Lambda), Storage (S3, EBS), Databases (RDS, DynamoDB), Networking (VPC, CloudFront), AI/ML (SageMaker), and many more.
- **Global Infrastructure:** Largest number of Regions and Availability Zones worldwide, enabling low-latency access and disaster recovery.
- **Pay-as-you-go:** Billing by the second/hour depending on service, with reserved and spot instance pricing for cost optimization.
- **Elastic Compute Cloud (EC2):** The flagship IaaS service providing virtual servers with full OS control.
- **AWS Lambda:** Serverless compute that runs code in response to events without managing servers.

### AWS Architecture Example (Web Application)

```
Client --> Route 53 (DNS) --> CloudFront (CDN)
| v
Application Load Balancer (ALB)
| |
EC2 (AZ-1) EC2 (AZ-2)
| |
Amazon RDS (Multi-AZ) | Amazon S3 (Static Assets)
```

### Core AWS Services

| Category       | Service           | Description                        |
| :------------- | :---------------- | :--------------------------------- |
| **Compute**    | EC2               | Virtual servers (IaaS)             |
| **Compute**    | Lambda            | Serverless functions (FaaS)        |
| **Compute**    | Elastic Beanstalk | PaaS for web apps (similar to GAE) |
| **Storage**    | S3                | Scalable object storage            |
| **Database**   | RDS               | Managed relational databases       |
| **Database**   | DynamoDB          | Managed NoSQL database             |
| **Networking** | VPC               | Isolated virtual network           |

## Microsoft Azure

### Overview

Microsoft Azure, launched in 2010, is the second-largest cloud platform. It is deeply integrated with the Microsoft enterprise ecosystem, making it a natural choice for organizations using Windows Server, Active Directory, .NET, and Office 365.

### Key Characteristics

- **Hybrid Cloud Leader:** Azure Arc enables management of on-premises, multi-cloud, and edge resources from a single control plane.
- **Enterprise Integration:** Seamless integration with Active Directory, Windows Server, SQL Server, and the .NET framework.
- **PaaS Strength:** Azure App Service provides managed hosting for web applications similar to GAE.
- **Global Reach:** Extensive network of data center regions worldwide.

### Azure Architecture Example (Hybrid)

```
On-Premises Data Center
| +--> Azure ExpressRoute (Private Link)
| v
Azure Virtual Network
| | |
Azure SQL Azure App Azure Blob
Database Service Storage
| Azure Traffic Manager |
(Routes users globally)
```

### Core Azure Services

| Category       | Service            | Description                        |
| :------------- | :----------------- | :--------------------------------- |
| **Compute**    | Virtual Machines   | Virtual servers (IaaS)             |
| **Compute**    | Azure Functions    | Serverless functions (FaaS)        |
| **Compute**    | App Service        | PaaS for web apps (similar to GAE) |
| **Storage**    | Blob Storage       | Scalable object storage            |
| **Database**   | Azure SQL Database | Managed relational database        |
| **Database**   | Cosmos DB          | Globally distributed NoSQL         |
| **Networking** | VNet               | Isolated virtual network           |

## Comparative Analysis: GAE vs AWS vs Azure

| Feature               | GAE                                           | AWS                                           | Azure                                              |
| :-------------------- | :-------------------------------------------- | :-------------------------------------------- | :------------------------------------------------- |
| **Type**              | PaaS (primarily)                              | IaaS + PaaS + SaaS                            | IaaS + PaaS + SaaS                                 |
| **Launched**          | 2008                                          | 2006                                          | 2010                                               |
| **Core Strength**     | Auto-scaling web apps, zero server management | Broadest services, market leader              | Hybrid cloud, enterprise integration               |
| **Server Management** | None (fully managed)                          | Full control (EC2) or managed (Lambda)        | Full control (VMs) or managed (App Service)        |
| **Scaling**           | Automatic, scales to zero                     | Manual (EC2) or automatic (Lambda, Beanstalk) | Manual (VMs) or automatic (Functions, App Service) |
| **Built-in Services** | Datastore, Memcache, Task Queues              | S3, SQS, SNS, DynamoDB                        | Blob Storage, Queue Storage, Cosmos DB             |
| **Equivalent PaaS**   | App Engine                                    | Elastic Beanstalk                             | App Service                                        |
| **Pricing**           | Pay per instance-hour + API calls             | Per-second/hour (varies by service)           | Per-minute billing                                 |
| **Best For**          | Rapid web app deployment, startups            | Large-scale enterprise, diverse workloads     | Microsoft-centric enterprises, hybrid setups       |

## Key Differences: PaaS (GAE) vs IaaS (AWS EC2)

Understanding the difference between GAE's PaaS model and AWS EC2's IaaS model is fundamental:

| Aspect              | GAE (PaaS)                         | AWS EC2 (IaaS)                              |
| :------------------ | :--------------------------------- | :------------------------------------------ |
| **What you manage** | Application code only              | OS, middleware, runtime, and code           |
| **Server access**   | No SSH, no OS access (Standard)    | Full root/admin SSH access                  |
| **Scaling**         | Fully automatic                    | Manual or configured auto-scaling           |
| **Deployment**      | Upload code, platform handles rest | Launch VM, install software, deploy         |
| **Flexibility**     | Limited to supported runtimes      | Any OS, any software                        |
| **Maintenance**     | Zero (platform handles patches)    | You patch OS and dependencies               |
| **Use case**        | Web apps, APIs, microservices      | Custom workloads, legacy apps, full control |

## Exam Tips

1. **GAE is PaaS, not IaaS:** Remember that Google App Engine is a Platform as a Service. Developers deploy code, not virtual machines. This is a key distinction from AWS EC2.
2. **GAE Auto-Scaling:** GAE automatically scales instances based on traffic and can scale to zero. This is a frequently tested concept.
3. **GAE Built-in Services:** Know the key services — Datastore (NoSQL), Memcache (caching), Task Queues (async processing), URL Fetch (HTTP client).
4. **Standard vs Flexible:** Standard Environment is sandboxed with fast startup; Flexible runs in Docker containers with more freedom.
5. **Compare PaaS offerings:** GAE, AWS Elastic Beanstalk, and Azure App Service are all PaaS platforms — know their similarities and differences.
6. **AWS is the market leader** with the broadest service portfolio and most Regions/AZs.
7. **Azure excels at hybrid cloud** with Azure Arc and deep Microsoft ecosystem integration.
8. **Service Mapping:** Be able to map equivalent services: GAE Datastore ~ DynamoDB ~ Cosmos DB; S3 ~ Blob Storage ~ Cloud Storage.
