# Programming on AWS and Azure


## Table of Contents

- [Programming on AWS and Azure](#programming-on-aws-and-azure)
- [1. Introduction to Cloud Programming Paradigms](#1-introduction-to-cloud-programming-paradigms)
- [2. Core Concepts of AWS and Azure Programming](#2-core-concepts-of-aws-and-azure-programming)
  - [2.1. The Shared Responsibility Model](#21-the-shared-responsibility-model)
  - [2.2. Infrastructure as Code (IaC)](#22-infrastructure-as-code-iac)
  - [2.3. Event-Driven Architecture](#23-event-driven-architecture)
- [3. Programming on Amazon Web Services (AWS)](#3-programming-on-amazon-web-services-aws)
  - [3.1. Key AWS Services for Developers](#31-key-aws-services-for-developers)
  - [3.2. Example: Using the AWS SDK for Python (Boto3)](#32-example-using-the-aws-sdk-for-python-boto3)
- [Create an S3 client using default credentials](#create-an-s3-client-using-default-credentials)
- [(Credentials are typically from IAM roles or ~/.aws/credentials)](#credentials-are-typically-from-iam-roles-or-awscredentials)
- [Call the list_buckets API method](#call-the-listbuckets-api-method)
- [Print the bucket names](#print-the-bucket-names)
- [4. Programming on Microsoft Azure](#4-programming-on-microsoft-azure)
  - [4.1. Key Azure Services for Developers](#41-key-azure-services-for-developers)
  - [4.2. Example: Using the Azure SDK for Python](#42-example-using-the-azure-sdk-for-python)
- [Authenticate using DefaultAzureCredential (supports multiple auth methods)](#authenticate-using-defaultazurecredential-supports-multiple-auth-methods)
- [This will work on Azure App Service, VMs, and locally with Azure CLI login](#this-will-work-on-azure-app-service-vms-and-locally-with-azure-cli-login)
- [Create a BlobServiceClient using the credential and account URL](#create-a-blobserviceclient-using-the-credential-and-account-url)
- [List all containers in the storage account](#list-all-containers-in-the-storage-account)
- [5. Comparison of Programming Models: AWS vs. Azure](#5-comparison-of-programming-models-aws-vs-azure)
- [6. Best Practices for Cloud Programming](#6-best-practices-for-cloud-programming)
- [Exam Tips](#exam-tips)

## 1. Introduction to Cloud Programming Paradigms

Cloud programming represents a fundamental shift from traditional software development. Instead of managing physical hardware and complex infrastructure, developers leverage vast, scalable, and managed services provided by cloud providers like Amazon Web Services (AWS) and Microsoft Azure. This paradigm enables a focus on business logic and application code, while the cloud platform handles provisioning, scaling, and maintenance.

The programming model in the cloud is inherently **service-oriented** and often **event-driven**. Applications are built by composing various cloud services—such as compute, storage, databases, and AI—via well-defined APIs. This approach promotes modularity, scalability, and resilience.

```
+-----------------------------+
| Application Code          |
| (Your Business Logic)     |
+-----------------------------+
         |
         | API Calls / SDKs
         v
+-----------------------------------------------+
| Cloud Platform                              |
| +---------+ +--------+ +-----------------+ |
| | Compute | | Storage| | Databases     | |
| | (e.g.,  | | (e.g., | | (e.g., RDS,  | |
| | Lambda, | | S3)    | | Cosmos DB)   | |
| | App     | |        | |               | |
| | Service)| |        | |               | |
| +---------+ +--------+ +-----------------+ |
+-----------------------------------------------+
```

## 2. Core Concepts of AWS and Azure Programming

### 2.1. The Shared Responsibility Model

A critical concept for cloud developers is the **Shared Responsibility Model**. The cloud provider is responsible for the security _of_ the cloud (the infrastructure), while the customer is responsible for security _in_ the cloud (their data, access management, and application security). This directly impacts how you program and configure your services.

### 2.2. Infrastructure as Code (IaC)

Instead of manually clicking buttons in a web console to create resources, cloud programming emphasizes **Infrastructure as Code (IaC)**. You write code (in JSON, YAML, or a domain-specific language) to define your infrastructure. This code can be version-controlled, shared, and reused, ensuring consistent and repeatable environments.

- **AWS:** AWS CloudFormation
- **Azure:** Azure Resource Manager (ARM) Templates, Bicep

### 2.3. Event-Driven Architecture

Both platforms are built around events. An event—such as a file being uploaded, a message arriving in a queue, or a scheduled time being reached—can trigger a piece of code to execute. This is the foundation of serverless computing.

- **Example Event Flow on AWS:**
  1. A user uploads an image to an Amazon S3 bucket (`s3:ObjectCreated` event).
  2. This event automatically triggers an AWS Lambda function.
  3. The Lambda function code runs, perhaps creating a thumbnail of the image.
  4. The thumbnail is saved back to another S3 bucket.

```
User -> [S3 Bucket] (Upload Image)
[S3 Bucket] -> (Event) -> [AWS Lambda] (Trigger Function)
[AWS Lambda] -> (Process) -> [S3 Bucket] (Save Thumbnail)
```

## 3. Programming on Amazon Web Services (AWS)

AWS offers a vast array of services, and programming for AWS typically involves using the AWS SDKs (Software Development Kits) available for various languages like Python, JavaScript, Java, and .NET.

### 3.1. Key AWS Services for Developers

| Service Category   | AWS Service        | Description                      | Common Use Case                                  |
| :----------------- | :----------------- | :------------------------------- | :----------------------------------------------- |
| **Compute**        | AWS Lambda         | Serverless function-as-a-service | Event-driven processing, API backends            |
|                    | Amazon EC2         | Virtual servers in the cloud     | Traditional web hosting, long-running processes  |
| **Storage**        | Amazon S3          | Scalable object storage          | File storage, static website hosting, data lakes |
|                    | Amazon EBS         | Block storage for EC2            | Boot volumes, databases                          |
| **Databases**      | Amazon DynamoDB    | Managed NoSQL database           | High-scale, low-latency applications             |
|                    | Amazon RDS         | Managed relational database      | Traditional SQL applications (PostgreSQL, MySQL) |
| **Integration**    | Amazon SQS         | Message queue service            | Decoupling application components                |
|                    | Amazon SNS         | Pub/Sub messaging service        | Sending notifications, fan-out messages          |
| **API Management** | Amazon API Gateway | Create, publish, and manage APIs | Building RESTful APIs that trigger Lambda        |

### 3.2. Example: Using the AWS SDK for Python (Boto3)

To interact with AWS services programmatically, you use the SDK. Below is a simple Python example using Boto3 to list all S3 buckets.

```python
import boto3

# Create an S3 client using default credentials
# (Credentials are typically from IAM roles or ~/.aws/credentials)
s3_client = boto3.client('s3')

# Call the list_buckets API method
response = s3_client.list_buckets()

# Print the bucket names
print("Your S3 buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")
```

## 4. Programming on Microsoft Azure

Azure provides a comparable set of services with deep integration with the Microsoft ecosystem (.NET, Windows, SQL Server). Programming is done using Azure SDKs for languages like C#, Python, Java, and JavaScript.

### 4.1. Key Azure Services for Developers

| Service Category   | Azure Service        | Description                               | Common Use Case                                                   |
| :----------------- | :------------------- | :---------------------------------------- | :---------------------------------------------------------------- |
| **Compute**        | Azure Functions      | Serverless function-as-a-service          | Event-driven processing, API backends                             |
|                    | Azure App Service    | Platform for web apps and APIs            | Web application hosting (support for .NET, Node.js, Python, etc.) |
| **Storage**        | Azure Blob Storage   | Scalable object storage                   | File storage, static websites, data lakes                         |
|                    | Azure Disk Storage   | Block storage for VMs                     | Boot volumes, databases                                           |
| **Databases**      | Azure Cosmos DB      | Globally distributed multi-model database | High-scale, low-latency apps, NoSQL                               |
|                    | Azure SQL Database   | Managed relational SQL database           | Traditional SQL applications                                      |
| **Integration**    | Azure Queue Storage  | Message queuing service                   | Decoupling application components                                 |
|                    | Azure Service Bus    | Advanced messaging service                | Enterprise messaging, publish-subscribe                           |
| **API Management** | Azure API Management | Publish, manage, and secure APIs          | Building and managing APIs                                        |

### 4.2. Example: Using the Azure SDK for Python

This example uses the Azure Storage Blobs client library for Python to list containers in a storage account.

```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Authenticate using DefaultAzureCredential (supports multiple auth methods)
# This will work on Azure App Service, VMs, and locally with Azure CLI login
credential = DefaultAzureCredential()

# Create a BlobServiceClient using the credential and account URL
blob_service_client = BlobServiceClient(
    account_url="https://<your-storage-account>.blob.core.windows.net/",
    credential=credential
)

# List all containers in the storage account
containers = blob_service_client.list_containers()
print("Your Blob Storage containers:")
for container in containers:
    print(f" - {container['name']}")
```

## 5. Comparison of Programming Models: AWS vs. Azure

| Feature                    | AWS                                      | Azure                                     |
| :------------------------- | :--------------------------------------- | :---------------------------------------- |
| **Primary SDK Languages**  | Python, JavaScript, Java, Go, .NET       | **.NET**, Python, Java, JavaScript, Go    |
| **Serverless Compute**     | AWS Lambda                               | Azure Functions                           |
| **Primary Object Storage** | Amazon S3                                | Azure Blob Storage                        |
| **Managed SQL Database**   | Amazon RDS                               | Azure SQL Database                        |
| **Primary NoSQL Database** | Amazon DynamoDB                          | Azure Cosmos DB                           |
| **Primary IaC Tool**       | AWS CloudFormation                       | ARM Templates / Bicep                     |
| **Identity & Access Mgmt** | AWS IAM (Identity and Access Management) | Azure AD (Active Directory)               |
| **CLI Tool**               | AWS CLI                                  | Azure CLI                                 |
| **Key Differentiator**     | Extensive service breadth and maturity   | Deep integration with Microsoft ecosystem |

## 6. Best Practices for Cloud Programming

1. **Design for Failure:** Assume any component can fail. Implement retry logic, timeouts, and fallback mechanisms.
2. **Leverage Managed Services:** Use databases, queues, and other managed services to reduce operational overhead.
3. **Implement Security Early:** Follow the principle of least privilege in IAM roles and policies. Keep secrets in managed services (AWS Secrets Manager, Azure Key Vault), not in code.
4. **Optimize for Cost:** Be aware of the cost model of services you use (e.g., Lambda execution time vs. EC2 hourly cost). Use auto-scaling to match capacity with demand.
5. **Monitor and Log:** Integrate monitoring (Amazon CloudWatch, Azure Monitor) and centralized logging from the start to gain visibility into application behavior.

## Exam Tips

- **Understand the Shared Responsibility Model:** Be clear on what you are responsible for vs. what the cloud provider handles. This is a frequent exam topic.
- **Know the Core Services:** Focus on the primary compute, storage, and database services for both AWS and Azure. Understand their use cases and basic configuration.
- **IaC is Key:** You will almost certainly be tested on the concept of Infrastructure as Code and the tools used for it (CloudFormation, ARM Templates).
- **Event-Driven Patterns:** Be prepared to identify scenarios where an event-driven, serverless architecture (using Lambda or Azure Functions) is the most appropriate solution.
- **Compare and Contrast:** Exams often ask for the Azure equivalent of an AWS service, or vice-versa. Use the comparison table above as a study guide.
