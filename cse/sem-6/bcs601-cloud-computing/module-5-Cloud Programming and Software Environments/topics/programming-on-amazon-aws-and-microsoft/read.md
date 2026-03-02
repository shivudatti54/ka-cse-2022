# Programming on AWS and Azure

## 1. Introduction to Cloud Programming Paradigms

Cloud computing has fundamentally transformed software development paradigms by abstracting infrastructure management and enabling developers to focus on business logic. Unlike traditional on-premises development where organizations maintain physical servers, networking equipment, and storage arrays, cloud platforms provide **managed services** that scale elastically according to demand. This shift represents a transition from **capacity planning** to **consumption-based billing**, where organizations pay only for compute, storage, and network resources actually utilized.

The programming model in cloud environments is inherently **service-oriented** and increasingly **event-driven**. Applications are constructed by composing discrete cloud services—compute instances, object storage, managed databases, machine learning APIs, and queueing systems—through well-defined REST APIs or language-specific SDKs. This compositional approach promotes **loose coupling**, **horizontal scalability**, and **resilience through redundancy**.

```
┌─────────────────────────────────────────────────────────────────┐
│ Cloud Application │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ Business Logic Layer │ │
│ │ (Your Application Code / Functions) │ │
│ └──────────────────────────────────────────────────────────┘ │
│ │ │
│ API Calls / SDKs │
│ ▼ │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ Cloud Platform Layer │ │
│ │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │ │
│ │ │ Compute │ │ Storage │ │Database │ │ AI/ML │ │ │
│ │ │ Lambda, │ │ S3, │ │ DynamoDB,│ │ Sage- │ │ │
│ │ │ ECS, VM │ │ Blob │ │ Cosmos │ │ maker │ │ │
│ │ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │ │
│ └──────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## 2. Core Architectural Concepts

### 2.1. The Shared Responsibility Model

The **Shared Responsibility Model** constitutes the foundational security paradigm in cloud computing. This model delineates security obligations between the cloud service provider (CSP) and the customer through a division that varies by service model:

- **Provider Responsibility (Security OF the cloud)**: Physical security of data centers, hardware infrastructure, network infrastructure, and virtualization layer.
- **Customer Responsibility (Security IN the cloud)**: Data classification, identity and access management, application-level security, network configuration, and encryption implementation.

| Responsibility Area     | IaaS Responsibility | PaaS Responsibility | SaaS Responsibility |
| :---------------------- | :------------------ | :------------------ | :------------------ |
| Data Protection         | Customer            | Customer            | Customer            |
| Identity Management     | Customer            | Customer            | Customer            |
| Application Security    | Customer            | Customer            | Customer (limited)  |
| Network Configuration   | Customer            | Customer            | Provider            |
| OS/Patches              | Customer            | Provider            | Provider            |
| Physical Infrastructure | Provider            | Provider            | Provider            |

### 2.2. Infrastructure as Code (IaC)

**Infrastructure as Code** represents the practice of defining infrastructure through declarative configuration files that can be version-controlled, tested, and automated. IaC eliminates manual provisioning, ensures environment consistency, and enables **immutable infrastructure** patterns.

**AWS CloudFormation Example (EC2 Instance with S3 Access):**

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'IaC Example: EC2 with IAM Role for S3 Access'

Resources:
 EC2Instance:
 Type: 'AWS::EC2::Instance'
 Properties:
 ImageId: 'ami-0c55b159cbfafe1f0'
 InstanceType: 't3.micro'
 IamInstanceProfile: !Ref InstanceProfile
 UserData:
 Fn::Base64: !Sub |
 #!/bin/bash
 yum update -y
 yum install -y python3

 S3AccessRole:
 Type: 'AWS::IAM::Role'
 Properties:
 AssumeRolePolicyDocument:
 Version: '2012-10-17'
 Statement:
 - Effect: Allow
 Principal:
 Service: 'ec2.amazonaws.com'
 Action: 'sts:AssumeRole'
 ManagedPolicyArns:
 - 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'

 InstanceProfile:
 Type: 'AWS::IAM::InstanceProfile'
 Properties:
 Roles: [!Ref S3AccessRole]
```

**Azure ARM Template Example (Virtual Machine with Managed Identity):**

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2021-03-01",
      "name": "myVM",
      "location": "[resourceGroup().location]",
      "identity": {
        "type": "SystemAssigned"
      },
      "properties": {
        "hardwareProfile": {
          "vmSize": "Standard_DS1_v2"
        },
        "osProfile": {
          "computerName": "myVM",
          "adminUsername": "adminuser",
          "adminPassword": "SecurePassword123!"
        },
        "storageProfile": {
          "imageReference": {
            "publisher": "Canonical",
            "offer": "UbuntuServer",
            "sku": "18.04-LTS",
            "version": "latest"
          }
        }
      }
    },
    {
      "type": "Microsoft.Authorization/roleAssignments",
      "apiVersion": "2020-04-01-preview",
      "name": "[guid(resourceGroup().id, 'storageBlobReader')]",
      "properties": {
        "roleDefinitionId": "[concat('/subscriptions/', subscription().subscriptionId, '/providers/Microsoft.Authorization/roleDefinitions/', '2a2b9908-6ea1-4ae3-8e65-b1e2e3dfe')]",
        "principalId": "[reference(resourceId('Microsoft.Compute/virtualMachines', 'myVM'), '2021-03-01', 'Full').identity.principalId]"
      }
    }
  ]
}
```

### 2.3. Event-Driven Architecture and Serverless Computing

Event-driven architectures decouple producers from consumers through asynchronous message passing. This pattern is fundamental to **serverless computing**, where function-as-a-service (FaaS) platforms execute code in response to events without requiring explicit server management.

#### AWS Lambda Execution Model

When a Lambda function is invoked, AWS provisions a runtime environment, executes the handler function, and terminates the environment after execution. The billing model charges based on **invocation count**, **execution duration** (rounded to 1ms), and **memory allocation**.

**AWS Lambda Function (Python - Image Thumbnail Generation):**

```python
import boto3
import os
from PIL import Image

s3_client = boto3.client('s3')

def lambda_handler(event, context):
 """
 Lambda handler for S3 object creation event.
 Creates a thumbnail for uploaded images.
 """
 # Extract bucket name and object key from event
 bucket = event['Records'][0]['s3']['bucket']['name']
 key = event['Records'][0]['s3']['object']['key']

 # Define thumbnail dimensions
 THUMBNAIL_SIZE = (128, 128)
 output_bucket = f"{bucket}-thumbnails"

 try:
 # Download the original image to /tmp (ephemeral storage)
 download_path = f'/tmp/{key}'
 s3_client.download_file(bucket, key, download_path)

 # Generate thumbnail
 with Image.open(download_path) as img:
 img.thumbnail(THUMBNAIL_SIZE)
 thumbnail_key = f"thumbnails/{key}"
 img.save(download_path)

 # Upload thumbnail to output bucket
 s3_client.upload_file(download_path, output_bucket, thumbnail_key)

 return {
 'statusCode': 200,
 'body': f'Successfully created thumbnail for {key}'
 }

 except Exception as e:
 print(f"Error processing {key}: {str(e)}")
 raise
```

#### Azure Functions Execution Model

Azure Functions provides similar serverless capabilities with additional integration options within the Microsoft ecosystem. The **Consumption Plan** provides automatic scaling, while **Premium Plan** offers pre-warmed instances to mitigate cold-start latency.

**Azure Function (C# - Queue Trigger with Blob Output):**

```csharp
using System;
using System.IO;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Extensions.Logging;

public class ImageProcessor
{
 [FunctionName("ResizeImage")]
 public void Run(
 [QueueTrigger("image-queue", Connection = "AzureWebJobsStorage")]string imageId,
 [Blob("images/{queueTrigger}", FileAccess.Read)] Stream inputBlob,
 [Blob("thumbnails/{queueTrigger}", FileAccess.Write)] Stream outputBlob,
 ILogger log)
 {
 log.LogInformation($"Processing image: {imageId}");

 // Image processing would go here
 // Using ImageSharp, System.Drawing, or similar library

 inputBlob.CopyTo(outputBlob);

 log.LogInformation($"Thumbnail created for: {imageId}");
 }
}
```

## 3. AWS Programming: SDKs and Service Integration

### 3.1. AWS SDK for Python (Boto3) Programming Patterns

The AWS SDK for Python (Boto3) provides programmatic access to AWS services. Understanding **resource** versus **client** objects is essential for effective SDK usage.

```python
import boto3
from botocore.exceptions import ClientError
import json

class S3Operations:
 """Demonstrates comprehensive S3 operations using Boto3"""

 def __init__(self, region_name='us-east-1'):
 # Client provides low-level service access
 self.s3_client = boto3.client('s3', region_name=region_name)

 # Resource provides higher-level, object-oriented access
 self.s3_resource = boto3.resource('s3')

 def create_bucket_with_encryption(self, bucket_name, region='us-east-1'):
 """Create S3 bucket with server-side encryption"""
 try:
 if region == 'us-east-1':
 response = self.s3_client.create_bucket(Bucket=bucket_name)
 else:
 response = self.s3_client.create_bucket(
 Bucket=bucket_name,
 CreateBucketConfiguration={
 'LocationConstraint': region
 }
 )

 # Enable encryption
 self.s3_client.put_bucket_encryption(
 Bucket=bucket_name,
 ServerSideEncryptionConfiguration={
 'Rules': [
 {
 'ApplyServerSideEncryptionByDefault': {
 'SSEAlgorithm': 'AES256'
 }
 }
 ]
 }
 )

 # Enable versioning
 self.s3_client.put_bucket_versioning(
 Bucket=bucket_name,
 VersioningConfiguration={
 'Status': 'Enabled'
 }
 )

 return response

 except ClientError as e:
 print(f"Error creating bucket: {e}")
 raise

 def upload_file_with_metadata(self, file_path, bucket, key, metadata):
 """Upload file with custom metadata"""
 try:
 response = self.s3_client.upload_file(
 file_path,
 bucket,
 key,
 ExtraArgs={
 'Metadata': metadata,
 'ContentType': 'application/octet-stream'
 }
 )
 return response
 except ClientError as e:
 print(f"Upload failed: {e}")
 raise

 def generate_presigned_url(self, bucket, key, expiration=3600):
 """Generate pre-signed URL for temporary access"""
 try:
 url = self.s3_client.generate_presigned_url(
 'get_object',
 Params={
 'Bucket': bucket,
 'Key': key
 },
 ExpiresIn=expiration
 )
 return url
 except ClientError as e:
 print(f"Error generating URL: {e}")
 raise
```

### 3.2. DynamoDB Programming with Boto3

**DynamoDB** is a fully managed NoSQL database providing single-digit millisecond latency at any scale. Understanding **partition keys**, **sort keys**, and **GSI/LSI** is critical for efficient data modeling.

```python
import boto3
from boto3.dynamodb.conditions import Key, Attr

class DynamoDBOperations:
 """DynamoDB CRUD operations demonstrating key patterns"""

 def __init__(self, table_name='Products'):
 self.dynamodb = boto3.resource('dynamodb')
 self.table = self.dynamodb.Table(table_name)

 def put_item_with_conditions(self, item):
 """
 Conditional write to prevent overwrites
 """
 try:
 response = self.table.put_item(
 Item=item,
 ConditionExpression='attribute_not_exists(PK) AND attribute_not_exists(SK)'
 )
 return response
 except self.dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
 print("Item already exists - conditional write failed")
 raise

 def query_with_partition_and_sort(self, pk_value, sk_range=None):
 """
 Query with partition key and optional sort key range
 """
 if sk_range:
 key_condition = Key('PK').eq(pk_value) & Key('SK').between(sk_range[0], sk_range[1])
 else:
 key_condition = Key('PK').eq(pk_value)

 response = self.table.query(
 KeyConditionExpression=key_condition,
 ScanIndexForward=True # Ascending order by sort key
 )

 return response['Items']

 def batch_operations(self, items):
 """
 Batch write for efficient bulk operations
 DynamoDB batch write limit: 25 items
 """
 with self.table.batch_writer() as batch:
 for item in items:
 batch.put_item(Item=item)

 def update_item_with_return_values(self, pk, sk, update_expression, expression_values):
 """
 Update item and return new/old values
 """
 response = self.table.update_item(
 Key={'PK': pk, 'SK': sk},
 UpdateExpression=update_expression,
 ExpressionAttributeValues=expression_values,
 ReturnValues='ALL_NEW'
 )
 return response['Attributes']
```

## 4. Azure Programming: SDKs and Service Integration

### 4.1. Azure SDK for .NET Programming

The Azure SDK for .NET provides consistent patterns for interacting with Azure services. The **Azure.Identity** library simplifies authentication through various credential types.

```csharp
using Azure;
using Azure.Storage.Blobs;
using Azure.Storage.Queues;
using Azure.Data.Tables;
using Azure.Identity;

public class AzureStorageService
{
 private readonly string _connectionString;
 private readonly DefaultAzureCredential _credential;

 public AzureStorageService()
 {
 _connectionString = Environment.GetEnvironmentVariable("AZURE_STORAGE_CONNECTION_STRING");
 _credential = new DefaultAzureCredential();
 }

 /// <summary>
 /// Upload blob using connection string (simple auth)
 /// </summary>
 public async Task<string> UploadBlobAsync(
 string containerName,
 string blobName,
 Stream content)
 {
 var blobServiceClient = new BlobServiceClient(_connectionString);
 var containerClient = blobServiceClient.GetBlobContainerClient(containerName);
 await containerClient.CreateIfNotExistsAsync();

 var blobClient = containerClient.GetBlobClient(blobName);
 await blobClient.UploadAsync(content, overwrite: true);

 return blobClient.Uri.ToString();
 }

 /// <summary>
 /// Upload blob using Managed Identity (recommended for production)
 /// </summary>
 public async Task<string> UploadBlobWithMIAsync(
 string accountName,
 string containerName,
 string blobName,
 Stream content)
 {
 var blobServiceClient = new BlobServiceClient(
 new Uri($"https://{accountName}.blob.core.windows.net"),
 _credential);

 var containerClient = blobServiceClient.GetBlobContainerClient(containerName);
 await containerClient.CreateIfNotExistsAsync();

 var blobClient = containerClient.GetBlobClient(blobName);
 await blobClient.UploadAsync(content, overwrite: true);

 return blobClient.Uri.ToString();
 }

 /// <summary>
 /// Process messages from queue
 /// </summary>
 public async Task ProcessQueueMessagesAsync(string queueName)
 {
 var queueServiceClient = new QueueServiceClient(_connectionString);
 var queueClient = queueServiceClient.GetQueueClient(queueName);

 await foreach (var message in queueClient.ReceiveMessagesAsync(maxMessages: 10))
 {
 foreach (var msg in message.Value)
 {
 Console.WriteLine($"Processing: {msg.Body}");

 // Process message logic here

 // Delete after processing
 await queueClient.DeleteMessageAsync(msg.MessageId, msg.PopReceipt);
 }
 }
 }
}
```

### 4.2. Azure Cosmos DB Programming

Cosmos DB is a globally distributed, multi-model database service. The **SQL API** provides familiar SQL-like querying with JSON documents.

```csharp
using Microsoft.Azure.Cosmos;
using System.Linq;
using System.Threading.Tasks;

public class CosmosDBService
{
 private readonly CosmosClient _client;
 private readonly Container _container;

 public CosmosDBService(string connectionString, string databaseName, string containerName)
 {
 _client = new CosmosClient(connectionString);
 _container = _client.GetDatabase(databaseName)
 .GetContainer(containerName);
 }

 /// <summary>
 /// Create item with automatic ID generation
 /// </summary>
 public async Task<ItemResponse<Product>> CreateProductAsync(Product product)
 {
 return await _container.CreateItemAsync(
 product,
 new PartitionKey(product.CategoryId));
 }

 /// <summary>
 /// Query with parameterized SQL
 /// </summary>
 public async Task<IEnumerable<Product>> QueryProductsByCategoryAsync(string categoryId)
 {
 var query = new QueryDefinition(
 "SELECT * FROM Products p WHERE p.categoryId = @categoryId AND p.price > @minPrice")
 .WithParameter("@categoryId", categoryId)
 .WithParameter("@minPrice", 100);

 var results = new List<Product>();

 using var iterator = _container.GetItemQueryIterator<Product>(query);

 while (iterator.HasMoreResults)
 {
 var response = await iterator.ReadNextAsync();
 results.AddRange(response);
 }

 return results;
 }

 /// <summary>
 /// Optimistic concurrency with ETag
 /// </summary>
 public async Task<ItemResponse<Product>> UpdateProductAsync(Product product)
 {
 var options = new ItemRequestOptions
 {
 IfMatchEtag = product.ETag
 };

 return await _container.ReplaceItemAsync(
 product,
 product.Id,
 new PartitionKey(product.CategoryId),
 options);
 }
}

public class Product
{
 public string Id { get; set; }
 public string Name { get; set; }
 public decimal Price { get; set; }
 public string CategoryId { get; set; }
 public string ETag { get; set; }
}
```

## 5. Comparative Analysis: AWS vs Azure Programming Models

### 5.1. Serverless Computing Comparison

| Feature             | AWS Lambda                            | Azure Functions                                     |
| :------------------ | :------------------------------------ | :-------------------------------------------------- |
| **Runtime Support** | Python, Node.js, Java, Go, Ruby, .NET | C#, JavaScript, Java, Python, PowerShell, Go        |
| **Timeout Limit**   | 15 minutes (configurable)             | 10 minutes (default), 60 minutes (premium)          |
| **Memory Range**    | 128 MB - 10 GB                        | 128 MB - 1.5 GB (Consumption), up to 8 GB (Premium) |
| **Cold Start**      | 100ms - 10s                           | 200ms - 10s (Consumption), faster with Premium      |
| **Concurrency**     | 1000 (default), configurable          | 200 (default), expandable                           |
| **Pricing**         | Invocations × duration                | Invocations × duration + execution time             |

### 5.2. Storage Services Comparison

| AWS Service | Azure Service         | Key Differences                                             |
| :---------- | :-------------------- | :---------------------------------------------------------- |
| S3          | Azure Blob Storage    | S3: eventual consistency; Azure: strong consistency for LRS |
| EBS         | Azure Managed Disks   | EBS: tied to EC2; Azure: standalone management              |
| EFS         | Azure Files           | EFS: NFS; Azure Files: SMB 3.0 + NFS                        |
| S3 Glacier  | Azure Archive Storage | Similar tiered archival, pricing differs                    |

### 5.3. Database Services Comparison

| AWS Service | Azure Service           | Programming Implications                                           |
| :---------- | :---------------------- | :----------------------------------------------------------------- |
| DynamoDB    | Cosmos DB               | DynamoDB: partition key design critical; Cosmos DB: richer SQL API |
| RDS         | Azure SQL / Managed SQL | RDS: more AWS integration; Azure SQL: familiar T-SQL               |
| ElastiCache | Azure Cache for Redis   | Similar patterns, Azure offers more tier options                   |

## 6. Serverless Patterns and Best Practices

### 6.1. Lambda@Edge and Azure Functions Premium Patterns

**AWS Lambda@Edge** allows running Lambda functions at CloudFront edge locations for latency-sensitive operations like request/response transformation.

```python
# Lambda@Edge: Modify request headers
def handler(event, context):
 request = event['Records'][0]['cf']['request']

 # Add security headers
 request['headers']['x-custom-header'] = [{'key': 'X-Custom-Header', 'value': 'value'}]
 request['headers']['strict-transport-security'] = [{
 'key': 'Strict-Transport-Security',
 'value': 'max-age=31536000; includeSubDomains'
 }]

 return request
```

### 6.2. Durable Functions (Azure)

Azure Durable Functions extend Azure Functions with **stateful workflows**, enabling complex orchestration scenarios.

```csharp
[FunctionName("Orchestrator")]
public static async Task<List<string>> RunOrchestrator(
 [OrchestrationTrigger] DurableOrchestrationContext context)
{
 var outputs = new List<string>();

 // Function chaining pattern
 outputs.Add(await context.CallActivityAsync<string>("FunctionA", "input"));
 outputs.Add(await context.CallActivityAsync<string>("FunctionB", "input"));

 // Fan-out/fan-in pattern
 var tasks = new List<Task<string>>();
 for (int i = 0; i < 10; i++)
 {
 tasks.Add(context.CallActivityAsync<string>("ProcessItem", i));
 }

 outputs.AddRange(await Task.WhenAll(tasks));

 return outputs;
}
```

## 7. Security Programming: IAM and Azure AD Integration

### 7.1. AWS IAM Policy Programming

```python
import boto3
import json

class IAMPolicyManager:
 """Programmatic IAM policy management"""

 def __init__(self):
 self.iam = boto3.client('iam')

 def create_lambda_execution_role(self, role_name, s3_bucket_arn):
 """Create IAM role for Lambda with S3 access"""
 trust_policy = {
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {"Service": "lambda.amazonaws.com"},
 "Action": "sts:AssumeRole"
 }
 ]
 }

 role = self.iam.create_role(
 RoleName=role_name,
 AssumeRolePolicyDocument=json.dumps(trust_policy),
 Description='Lambda execution role'
 )

 # Attach managed policies
 self.iam.attach_role_policy(
 RoleName=role_name,
 PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
 )

 # Inline policy for S3 access
 s3_policy = {
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": f"{s3_bucket_arn}/*"
 }
 ]
 }

 self.iam.put_role_policy(
 RoleName=role_name,
 PolicyName='S3AccessPolicy',
 PolicyDocument=json.dumps(s3_policy)
 )

 return role['Role']['Arn']
```

### 7.2. Azure RBAC Programming

```csharp
using Azure.Identity;
using Microsoft.Azure.Management.Authorization;
using Microsoft.Azure.Management.ResourceManager;
using System.Threading.Tasks;

public class AzureRBACService
{
 private readonly AuthorizationManagementClient _authClient;
 private readonly string _subscriptionId;

 public AzureRBACService()
 {
 var credential = new DefaultAzureCredential();
 _subscriptionId = Environment.GetEnvironmentVariable("AZURE_SUBSCRIPTION_ID");

 _authClient = new AuthorizationManagementClient(
 new Uri("https://management.azure.com/"),
 credential);
 _authClient.SubscriptionId = _subscriptionId;
 }

 /// <summary>
 /// Assign Reader role to a managed identity
 /// </summary>
 public async Task<string> AssignRoleAsync(
 string resourceGroupName,
 string principalId,
 string roleDefinitionName = "Reader")
 {
 var roleDefinitions = await _authClient.RoleDefinitions.ListAsync(
 scope: $"/subscriptions/{_subscriptionId}/resourceGroups/{resourceGroupName}",
 filter: $"roleName eq '{roleDefinitionName}'");

 var roleDefinitionId = roleDefinitions.Value.First().Id;

 var roleAssignment = new RoleAssignmentProperties
 {
 PrincipalId = principalId,
 RoleDefinitionId = roleDefinitionId,
 PrincipalType = "ServicePrincipal"
 };

 var result = await _authClient.RoleAssignments.CreateAsync(
 scope: $"/subscriptions/{_subscriptionId}/resourceGroups/{resourceGroupName}",
 roleAssignmentName: System.Guid.NewGuid().ToString(),
 parameters: roleAssignment);

 return result.Value.Id;
 }
}
```

---

## 8. Assessment: Hard Analytical Questions

### Question 1: Multi-Service Architecture Design

A fintech company needs to process credit card transactions in real-time. The architecture must:

1. Receive transactions via REST API
2. Validate each transaction against a fraud detection model
3. Store approved transactions in a database
4. Send notifications to users via SMS/Email
5. Process payments through a third-party payment gateway
6. Maintain audit logs for compliance

**Analyze the AWS architecture:**

```python
# Given: Lambda function receives transaction
# Lambda memory: 512 MB, execution time: 800ms
# Function invoked 1 million times per day
# S3 stores audit logs: 10KB per transaction
```

**Question**: Calculate the daily AWS costs for the transaction processing assuming:

- Lambda pricing: $0.20 per 1M requests, $0.0000166667 per GB-second
- S3 pricing: $0.023 per GB stored, $0.005 per 10,000 GET requests
- Data transfer: $0.09 per GB

Show all calculations and recommend cost optimization strategies.

### Question 2: DynamoDB Data Model Design

**Scenario**: An e-commerce platform needs to store orders with the following access patterns:

1. Get all orders for a customer (Query by CustomerID)
2. Get all orders for a customer within a date range
3. Get order details by OrderID (global lookup)
4. Get all orders with status "PENDING" across all customers

**Question**: Design a DynamoDB table schema with appropriate primary key, sort key, and GSIs. Write Boto3 code to execute each access pattern efficiently.

### Question 3: Azure Functions Cold Start Analysis

**Given**: Azure Function running on Consumption Plan

- Average execution time: 200ms
- Function runs every 5 minutes during business hours (8 hours/day)
- Memory allocation: 512 MB

**Question**:

a) Calculate the number of cold starts expected per day if the function has 60% utilization rate.

b) If each cold start adds 3 seconds latency, calculate the effective total execution time.

c) Compare costs with Premium Plan (always warm) where execution time is consistently 200ms.

### Question 4: IAM Policy Debugging

The following IAM policy is not allowing a Lambda function to access an S3 bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::mybucket/*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::mybucket"
    }
  ]
}
```

The Lambda execution role has this policy attached, but S3 operations fail with Access Denied.

**Question**: Identify at least 3 potential issues and provide solutions for each.

---
