# Programming on AWS and Azure

## 1. Introduction to Cloud Computing Platforms

Cloud computing has fundamentally transformed software development paradigms by providing on-demand access to scalable computational resources. **Amazon Web Services (AWS)** and **Microsoft Azure** represent the two dominant cloud platforms, collectively serving millions of organizations worldwide. Understanding the programming models, service offerings, and architectural patterns of these platforms is essential for modern software engineers.

### 1.1. Cloud Service Models

Cloud computing operates on three fundamental service models that define the scope of management responsibilities:

- **Infrastructure as a Service (IaaS)**: Provides virtualized computing resources. Users manage operating systems, middleware, and runtime while the cloud provider handles physical infrastructure.
- **Platform as a Service (PaaS)**: Offers a complete development and deployment environment. Users focus on application code while the provider manages underlying infrastructure.
- **Software as a Service (SaaS)**: Delivers complete applications over the internet. Users interact with the application without managing any infrastructure.

### 1.2. Shared Responsibility Model

The **Shared Responsibility Model** delineates security obligations between cloud providers and customers. AWS and Azure implement similar frameworks:

| Responsibility            | AWS                                                         | Azure                                                         |
| ------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------- |
| Security **OF** the Cloud | Physical infrastructure, hypervisor, network infrastructure | Physical datacenters, host infrastructure, network controls   |
| Security **IN** the Cloud | Customer data, access management, application security      | Customer data, identity management, application configuration |

This model directly impacts programming decisions, particularly regarding data encryption, access control implementation, and application security configurations.

## 2. Core AWS Services and Programming

### 2.1. Compute Services

**Amazon Elastic Compute Cloud (EC2)** provides resizable virtual servers. Programming with EC2 involves instance selection, security group configuration, and user data scripts for initialization.

```python
# AWS SDK for Python (Boto3) - Launching an EC2 Instance
import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')

response = ec2_client.run_instances(
 ImageId='ami-0c55b159cbfafe1f0', # Amazon Linux 2 AMI
 InstanceType='t3.micro',
 MinCount=1,
 MaxCount=1,
 KeyName='my-key-pair',
 SecurityGroupIds=['sg-0123456789abcdef0'],
 UserData='''#!/bin/bash
 yum update -y
 yum install -y httpd
 systemctl start httpd
 echo "<h1>Hello from EC2</h1>" > /var/www/html/index.html'''
)

print(f"Instance ID: {response['Instances'][0]['InstanceId']}")
```

**AWS Lambda** enables serverless computing where code executes in response to events without provisioning servers. Azure Functions provides equivalent functionality on the Microsoft platform.

```python
# AWS Lambda Function - Image Thumbnail Generator
import boto3
import io
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
 # Get bucket name and file key from event
 bucket = event['Records'][0]['s3']['bucket']['name']
 key = event['Records'][0]['s3']['object']['key']

 # Download image from S3
 file_byte_string = s3.get_object(Bucket=bucket, Key=key)['Body'].read()
 image = Image.open(io.BytesIO(file_byte_string))

 # Create thumbnail (128x128)
 image.thumbnail((128, 128))

 # Save thumbnail to destination bucket
 buffer = io.BytesIO()
 image.save(buffer, "JPEG")
 buffer.seek(0)

 dest_bucket = bucket.replace('source', 'thumbnail')
 s3.put_object(Bucket=dest_bucket, Key=f"thumb_{key}", Body=buffer)

 return {
 'statusCode': 200,
 'body': f'Thumbnail created for {key}'
 }
```

### 2.2. Storage Services

**Amazon Simple Storage Service (S3)** provides scalable object storage with built-in versioning, lifecycle policies, and access controls.

| Feature    | Description                   | Programming Interface               |
| ---------- | ----------------------------- | ----------------------------------- |
| Buckets    | Container for objects         | `create_bucket()`, `list_buckets()` |
| Objects    | Files stored with metadata    | `put_object()`, `get_object()`      |
| Versioning | Object version control        | `put_object_versioning()`           |
| Lifecycle  | Automated transition policies | `put_bucket_lifecycle()`            |

```python
# Boto3 - S3 Object Operations
import boto3

s3 = boto3.resource('s3')

# Upload a file
s3.Bucket('my-bucket').upload_file('local.txt', 'remote.txt')

# Download a file
s3.Bucket('my-bucket').download_file('remote.txt', 'local_copy.txt')

# List objects with prefix
for obj in s3.Bucket('my-bucket').objects.filter(Prefix='images/'):
 print(obj.key)
```

### 2.3. Database Services

**Amazon DynamoDB** is a fully managed NoSQL database providing single-digit millisecond latency at any scale.

```python
# DynamoDB Table Operations with Boto3
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Users')

# Insert item
table.put_item(
 Item={
 'user_id': 'USR001',
 'name': 'John Doe',
 'email': 'john@example.com',
 'age': 28
 }
)

# Query with partition key
response = table.query(
 KeyConditionExpression=Key('user_id').eq('USR001')
)

# Scan with filter
response = table.scan(
 FilterExpression=Attr('age').gte(25)
)
```

**Amazon Relational Database Service (RDS)** supports MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB with automated backups and failover.

## 3. Core Azure Services and Programming

### 3.1. Compute Services

**Azure Virtual Machines** provide IaaS-level compute with Windows and Linux support. The Azure SDK enables programmatic management.

```python
# Azure SDK for Python - Azure Virtual Machine Management
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

subscription_id = "your-subscription-id"
credential = DefaultAzureCredential()

compute_client = ComputeManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)

# Create VM operation would require prior network setup
# This demonstrates the SDK structure
async_vm_creation = compute_client.virtual_machines.begin_create_or_update(
 'resource_group_name',
 'vm_name',
 {
 'location': 'eastus',
 'storage_profile': {
 'image_reference': {
 'publisher': 'Canonical',
 'offer': 'UbuntuServer',
 'sku': '18.04-LTS',
 'version': 'latest'
 }
 },
 'hardware_profile': {
 'vm_size': 'Standard_DS1_v2'
 }
 }
)
```

**Azure Functions** is Microsoft's serverless compute service, compatible with AWS Lambda.

```python
# Azure Function - HTTP Trigger (Python)
import azure.functions as func
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
 logging.info('Python HTTP trigger function processed a request.')

 name = req.params.get('name')
 if not name:
 try:
 req_body = req.get_json()
 except ValueError:
 pass
 else:
 name = req_body.get('name')

 if name:
 return func.HttpResponse(
 f"Hello, {name}. This HTTP triggered function executed successfully.",
 status_code=200
 )
 else:
 return func.HttpResponse(
 "This HTTP triggered function executed. Pass a name in the query string.",
 status_code=400
 )
```

### 3.2. Storage Services

**Azure Blob Storage** provides massively scalable object storage for unstructured data.

```python
# Azure SDK - Blob Storage Operations
from azure.storage.blob import BlobServiceClient, ContainerClient

connection_string = "your-connection-string"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create container
container_client = blob_service_client.get_container_client("mycontainer")
container_client.create_container()

# Upload blob
blob_client = blob_service_client.get_blob_client("mycontainer", "myfile.txt")
blob_client.upload_blob("Hello Azure!", overwrite=True)

# Download blob
downloaded = blob_client.download_blob()
content = downloaded.readall()
```

### 3.3. Azure Database Services

| Service                       | Type                | Use Case                 | Programming Interface |
| ----------------------------- | ------------------- | ------------------------ | --------------------- |
| Azure SQL                     | Relational          | Enterprise applications  | pyodbc, pymssql       |
| Cosmos DB                     | NoSQL (Multi-model) | Global distribution      | azure-cosmos SDK      |
| Azure Database for PostgreSQL | Relational          | Open source applications | psycopg2              |
| Azure Cache for Redis         | In-memory cache     | Session storage, caching | redis-py              |

## 4. Infrastructure as Code (IaC)

### 4.1. AWS CloudFormation

CloudFormation uses JSON or YAML templates to define infrastructure.

```yaml
# CloudFormation Template - S3 Bucket with Website Configuration
AWSTemplateFormatVersion: '2010-09-09'
Description: 'S3 Static Website Hosting'

Resources:
 WebsiteBucket:
 Type: 'AWS::S3::Bucket'
 Properties:
 BucketName: 'my-static-website-bucket'
 WebsiteConfiguration:
 IndexDocument: 'index.html'
 ErrorDocument: 'error.html'
 PublicAccessBlockConfiguration:
 BlockPublicAcls: false
 BlockPublicPolicy: false
 IgnorePublicAcls: false
 RestrictPublicBuckets: false

 BucketPolicy:
 Type: 'AWS::S3::BucketPolicy'
 Properties:
 Bucket: !Ref WebsiteBucket
 PolicyDocument:
 Version: '2012-10-17'
 Statement:
 - Effect: Allow
 Principal: '*'
 Action: 's3:GetObject'
 Resource: !Sub 'arn:aws:s3:::${WebsiteBucket}/*'
```

### 4.2. Azure Resource Manager (ARM) Templates

ARM templates use JSON to define Azure resources.

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2021-04-01",
      "name": "mystorageaccount",
      "location": "eastus",
      "sku": {
        "name": "Standard_LRS"
      },
      "kind": "StorageV2",
      "properties": {
        "supportsHttpsTrafficOnly": true
      }
    }
  ]
}
```

## 5. AWS vs Azure: Service Comparison

| Category           | AWS Service | Azure Service      | Key Difference                                              |
| ------------------ | ----------- | ------------------ | ----------------------------------------------------------- |
| **Compute**        | EC2         | Virtual Machines   | Azure offers tighter Visual Studio integration              |
| **Serverless**     | Lambda      | Azure Functions    | Both support similar triggers; Azure has Durable Functions  |
| **Object Storage** | S3          | Blob Storage       | S3 has broader ecosystem integration                        |
| **NoSQL**          | DynamoDB    | Cosmos DB          | Cosmos DB offers multi-model (SQL, MongoDB, Cassandra APIs) |
| **Relational**     | RDS         | Azure SQL Database | Azure SQL has hybrid license mobility                       |
| **Container**      | ECS/EKS     | AKS                | EKS and AKS are both Kubernetes-managed services            |
| **Identity**       | IAM         | Azure AD           | Azure AD provides enterprise identity federation            |
| **CDN**            | CloudFront  | Azure CDN          | Both offer global edge locations                            |

## 6. Authentication and Access Management

### 6.1. AWS Identity and Access Management (IAM)

```python
# Creating IAM User and Attaching Policy with Boto3
import boto3

iam = boto3.client('iam')

# Create user
iam.create_user(UserName='developer')

# Create access key
key_response = iam.create_access_key(UserName='developer')
access_key = key_response['AccessKey']['AccessKeyId']
secret_key = key_response['AccessKey']['SecretAccessKey']

# Attach policy
iam.attach_user_policy(
 UserName='developer',
 PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)
```

### 6.2. Azure Active Directory Authentication

```python
# Azure - Authenticating with DefaultAzureCredential
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(
 account_url="https://mystorageaccount.blob.core.windows.net",
 credential=credential
)
```

---

## Assessment Questions

### Multiple Choice Questions

**Question 1**: A company needs to process uploaded images to create thumbnails automatically. Which AWS architecture provides the most cost-effective solution for variable workload?

A) EC2 instance running 24/7 with image processing script
B) Lambda function triggered by S3 ObjectCreated event
C) ECS container with auto-scaling
D) Lightsail instance with scheduled tasks

**Answer**: B) Lambda function triggered by S3 ObjectCreated event. Lambda provides event-driven execution with pay-per-invocation pricing, making it cost-effective for variable workloads. You only pay for compute time when the function executes.

---

**Question 2**: In Azure, you need to deploy a web application that must maintain session state across multiple instances. Which Azure service combination is MOST appropriate?

A) Azure Functions + Cosmos DB
B) App Service + Azure Cache for Redis
C) Virtual Machines + Azure SQL
D) AKS + Azure Files

**Answer**: B) App Service + Azure Cache for Redis. Azure App Service provides the web hosting platform while Azure Cache for Redis stores session state in-memory, enabling fast retrieval across multiple instances.

---

**Question 3**: When implementing Infrastructure as Code, what is the PRIMARY advantage of using Azure Resource Manager templates over manual portal configuration?

A) Lower direct costs for resource deployment
B) Idempotent and repeatable deployments with version control
C) Automatic security patching of resources
D) Real-time monitoring integration

**Answer**: B) Idempotent and repeatable deployments with version control. ARM templates ensure consistent infrastructure deployment, can be stored in version control systems, and enable automated deployment pipelines.

---

**Question 4**: A multinational application requires sub-10ms latency for users across three continents. Which database configuration BEST meets this requirement?

A) Single RDS instance in us-east-1
B) DynamoDB with global tables
C) Single Cosmos DB account with single region write
D) ElastiCache Redis in one region

**Answer**: B) DynamoDB with global tables. DynamoDB global tables provide multi-region replication with automatic failover, enabling low-latency access for distributed users.

---

### Short Answer Questions

**Question 1**: Explain the difference between AWS S3 eventual consistency and strong consistency. How does this affect application design?

**Answer**: S3 provides read-after-write consistency for new object writes (strong consistency), meaning newly uploaded objects are immediately readable. However, for overwrite PUTs and DELETEs, S3 offers eventual consistency—changes may take time to propagate across replicas. Application designers must implement retry logic for read operations after updates and consider using versioning to maintain data integrity during the consistency window.

---

**Question 2**: Compare AWS IAM roles with Azure Managed Identities. How do they simplify resource access management?

**Answer**: Both eliminate the need to store credentials in code. AWS IAM roles are assumed by EC2 instances, Lambda functions, and other services, with temporary credentials automatically rotated. Azure Managed Identities provide similar functionality for Azure resources, automatically generating service principal credentials that can be used to authenticate to Azure services. Both approaches follow the principle of least privilege and eliminate credential leakage risks.

---

### Numerical Problem

**Question**: Calculate the monthly cost for an AWS Lambda function that executes 10 million times per month, with each execution lasting 200ms and using 256MB of memory. Given Lambda pricing: $0.20 per 1 million requests, $0.0000166667 per GB-second.

**Solution**:

- Request charges: (10,000,000 / 1,000,000) × $0.20 = $2.00
- Compute charges:
- Duration per execution = 200ms = 0.2 seconds
- Memory = 256MB = 0.25GB
- GB-seconds per execution = 0.25 × 0.2 = 0.05 GB-s
- Total GB-seconds = 10,000,000 × 0.05 = 500,000 GB-s
- Compute cost = 500,000 × $0.0000166667 = $8.33
- **Total monthly cost = $2.00 + $8.33 = $10.33**
