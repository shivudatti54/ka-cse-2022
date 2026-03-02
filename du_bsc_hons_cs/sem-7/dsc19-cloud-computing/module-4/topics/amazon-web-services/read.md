# Amazon Web Services (AWS) — Comprehensive Study Material

## Cloud Computing (BSc Hons Computer Science — NEP 2024 UGCF)

---

## 1. Introduction to Cloud Computing and AWS

### 1.1 Context: Cloud Computing in Modern Computing

Cloud computing has revolutionized how organizations deploy, manage, and scale their applications. According to the Delhi University syllabus under NEP 2024 UGCF, cloud computing represents a fundamental shift from traditional on-premises infrastructure to on-demand, pay-as-you-go services delivered over the internet.

**Cloud Computing Definition (NIST):** A model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.

### 1.2 What is Amazon Web Services?

**Amazon Web Services (AWS)** is the world's most comprehensive and widely adopted cloud platform, offering over 200 fully featured services from data centers globally. Launched in 2006, AWS was the first major cloud provider and continues to lead the market with approximately 32% of the cloud infrastructure market share.

**Real-World Relevance:**
- **Netflix** streams content to 200+ million subscribers using AWS
- **Airbnb** manages millions of listings on AWS infrastructure
- **NASA** uses AWS for Mars rover data processing
- **Startups** like Uber, Airbnb, and Spotify began on AWS

For Delhi University CS students, understanding AWS is essential because:
1. **Industry Demand:** 90% of cloud job postings require AWS skills
2. **Career Opportunities:** AWS Solutions Architect is among the highest-paying IT certifications
3. **Practical Application:** Direct alignment with NEP 2024 emphasis on industry-relevant skills

---

## 2. AWS Global Infrastructure

### 2.1 Regions and Availability Zones

AWS operates in **Geographic Regions** worldwide. Each region is a physical location containing multiple **Availability Zones (AZs)**.

| Component | Description |
|-----------|-------------|
| **Region** | Geographic area (e.g., us-east-1, ap-south-1) |
| **Availability Zone** | Isolated data center within a region |
| **Edge Location** | CDN endpoints for CloudFront caching |

**Key Concepts:**
- **High Availability:** Deploy applications across multiple AZs
- **Low Latency:** Choose regions closest to users
- **Data Sovereigncy:** Some data must remain in specific countries

**Example:** The `ap-south-1` (Mumbai) region serves Indian customers with lower latency. A production deployment should span at least 2 AZs (e.g., `ap-south-1a` and `ap-south-1b`).

### 2.2 Content Delivery Network (CDN)

**Amazon CloudFront** is AWS's CDN service that delivers content globally with low latency through edge locations.

---

## 3. Core AWS Services

### 3.1 Compute Services

#### 3.1.1 Amazon EC2 (Elastic Compute Cloud)

**EC2** provides resizable compute capacity in the cloud. It's the foundational service for running applications.

**Key Features:**
- **Instance Types:** General purpose (t3, m5), Compute optimized (c5), Memory optimized (r5), GPU instances (p4)
- **Pricing Models:**
  - **On-Demand:** Pay per hour/second, no commitment
  - **Reserved Instances:** 1-3 year commitment, up to 72% discount
  - **Spot Instances:** Bid for unused capacity, up to 90% discount
  - **Savings Plans:** Flexible pricing based on usage commitment
- **Scaling:** Auto Scaling Groups (ASG) for automatic scaling

**Security Best Practice:** Never expose SSH keys publicly; use Security Groups and Key Pairs properly.

#### 3.1.2 AWS Lambda (Serverless Computing)

**Lambda** is a serverless compute service that runs code in response to events without provisioning servers.

**Characteristics:**
- Pay only for compute time consumed
- Automatic scaling from 0 to thousands of requests
- Maximum execution time: 900 seconds (15 minutes)
- Supported runtimes: Node.js, Python, Java, Go, .NET, Ruby

**Use Cases:**
- Real-time file processing (S3 triggers)
- API backends (API Gateway integration)
- Data processing pipelines
- IoT backend processing

#### 3.1.3 Container Services

| Service | Description | Use Case |
|---------|-------------|----------|
| **Amazon ECS** | Elastic Container Service | Container orchestration (Docker) |
| **Amazon EKS** | Elastic Kubernetes Service | Kubernetes on AWS |
| **Amazon ECR** | Elastic Container Registry | Docker container registry |

---

### 3.2 Storage Services

#### 3.2.1 Amazon S3 (Simple Storage Service)

**S3** is object storage built to store and retrieve any amount of data from anywhere.

**Key Concepts:**
- **Buckets:** Containers for objects (globally unique names)
- **Objects:** Files with key (filename) and value (data)
- **Storage Classes:**
  - **S3 Standard:** Frequent access (high durability, low latency)
  - **S3 Intelligent-Tiering:** Auto-tiering based on access patterns
  - **S3 Standard-IA:** Infrequent access (lower retrieval fee)
  - **S3 Glacier:** Archival (retrieval in minutes to hours)
  - **S3 Glacier Deep Archive:** Long-term archive (12+ hours retrieval)

**Key Features:**
- **Versioning:** Track changes to objects
- **Lifecycle Policies:** Automate transitions between storage classes
- **Replication:** Cross-region replication (CRR) for disaster recovery
- **Access Control:** Bucket policies, ACLs, IAM policies

**Security:**
- **Block Public Access:** Prevent accidental exposure
- **Encryption:** SSE-S3, SSE-KMS, SSE-C, client-side encryption
- **Access Logging:** Track all access requests

#### 3.2.2 Other Storage Services

| Service | Type | Use Case |
|---------|------|----------|
| **EBS** | Block storage | EC2 persistent storage |
| **EFS** | File storage | Shared file system across instances |
| **FSx** | Managed file systems | Windows/Lustre file systems |
| **Glacier** | Archive storage | Long-term backup |

---

### 3.3 Database Services

#### 3.3.1 Amazon RDS (Relational Database Service)

**RDS** manages relational databases with automated patching, backups, and scaling.

**Supported Engines:**
- Amazon Aurora (MySQL/PostgreSQL compatible)
- MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

**Key Features:**
- **Automated Backups:** Point-in-time recovery
- **Read Replicas:** For read scaling (up to 5)
- **Multi-AZ Deployment:** High availability with automatic failover
- **Encryption:** At rest (KMS) and in transit (SSL)

**Example: Creating an RDS Instance (AWS Console or CLI)**

```bash
# AWS CLI command to create RDS MySQL instance
aws rds create-db-instance \
    --db-instance-identifier mydatabase \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --allocated-storage 20 \
    --master-username admin \
    --master-user-password YourSecurePassword123 \
    --region ap-south-1
```

#### 3.3.2 Amazon DynamoDB (NoSQL)

**DynamoDB** is a fully managed NoSQL database with single-digit millisecond latency.

**Key Concepts:**
- **Tables, Items, Attributes:** No fixed schema
- **Primary Keys:** Partition key (required) + Sort key (optional)
- **DAX (DynamoDB Accelerator):** In-memory cache for microsecond latency
- **Global Tables:** Multi-region replication

**Use Cases:** Gaming, IoT, mobile backends, real-time bidding platforms

#### 3.3.3 Other Database Services

| Service | Type | Use Case |
|---------|------|----------|
| **ElastiCache** | In-memory | Redis/Memcached caching |
| **Redshift** | Data Warehouse | Analytics and BI |
| **DocumentDB** | Document | MongoDB compatible |
| **Neptune** | Graph | Social networks, fraud detection |

---

### 3.4 Networking Services

#### 3.4.1 Amazon VPC (Virtual Private Cloud)

**VPC** is an isolated virtual network within AWS cloud.

**Components:**
- **Subnets:** Divide VPC into public and private subnets
- **Route Tables:** Control traffic routing
- **Internet Gateway (IGW):** Connect VPC to internet
- **NAT Gateway:** Allow private subnet instances to access internet
- **Security Groups:** Instance-level firewall (stateful)
- **NACLs:** Subnet-level firewall (stateless)

**Architecture Example:**

```
┌─────────────────────────────────────────────────┐
│                    VPC (10.0.0.0/16)            │
│  ┌──────────────────┐  ┌──────────────────┐   │
│  │ Public Subnet    │  │ Private Subnet   │   │
│  │ 10.0.1.0/24      │  │ 10.0.2.0/24      │   │
│  │                  │  │                  │   │
│  │ ┌──────────────┐ │  │ ┌──────────────┐ │   │
│  │ │  ALB         │ │  │ │ EC2 Instance │ │   │
│  │ └──────────────┘ │  │ └──────────────┘ │   │
│  └────────┬─────────┘  └────────┬─────────┘   │
│           │                     │              │
│           └──────────┬──────────┘              │
│                      │                         │
│              ┌───────┴───────┐                 │
│              │  Internet GW  │                 │
│              └───────────────┘                 │
└─────────────────────────────────────────────────┘
```

#### 3.4.2 Route 53 (DNS Service)

- **Hosted Zones:** Container for DNS records
- **Record Types:** A, AAAA, CNAME, MX, TXT, NS
- **Routing Policies:** Simple, Weighted, Latency-based, Geolocation, Failover

#### 3.4.3 API Gateway

- Create, maintain, and secure APIs at any scale
- Supports RESTful and WebSocket APIs
- Integration with Lambda for serverless backends

---

### 3.5 Security & Identity Services

#### 3.5.1 IAM (Identity and Access Management)

**IAM** enables secure management of access to AWS services and resources.

**Key Concepts:**
- **Users:** Individual authentication (long-term credentials)
- **Groups:** Collection of users with shared permissions
- **Roles:** Temporary credentials for services/applications
- **Policies:** JSON documents defining permissions

**IAM Policy Structure:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ]
    }
  ]
}
```

**Best Practices:**
- Enable MFA for root account
- Use IAM roles instead of access keys
- Follow principle of least privilege
- Enable CloudTrail for audit logging

#### 3.5.2 Other Security Services

| Service | Purpose |
|---------|---------|
| **Cognito** | User identity and access management for apps |
| **KMS** | Key management and encryption |
| **Secrets Manager** | Rotate and manage secrets |
| **Security Groups** | Instance-level firewall rules |
| **WAF** | Web application firewall |
| **Shield** | DDoS protection |

---

## 4. AWS Pricing Models

Understanding AWS pricing is critical for cost optimization.

### 4.1 Pricing Pillars

1. **Compute:** Based on instance hours,Lambda execution time
2. **Storage:** GB per month consumed
3. **Data Transfer:** Outbound transfer (inbound is free)
4. **Request Pricing:** Number of API requests (S3, Lambda)

### 4.2 Cost Optimization Strategies

| Strategy | Description |
|----------|-------------|
| **Right-sizing** | Match instance sizes to actual needs |
| **Reserved Instances** | Commit for 1-3 years for discounts |
| **Spot Instances** | Use for fault-tolerant workloads |
| **S3 Lifecycle Policies** | Move data to cheaper storage classes |
| **AWS Budgets** | Set alerts for spending limits |
| **Cost Explorer** | Analyze spending patterns |

---

## 5. AWS Well-Architected Framework

AWS provides best practices through five pillars:

### 5.1 Operational Excellence
- Infrastructure as Code (CloudFormation, Terraform)
- Automated responses to events
- Continuous improvement through feedback

### 5.2 Security
- Strong identity foundation (IAM)
- Enable traceability (CloudTrail)
- Apply security at all layers
- Protect data in transit and at rest

### 5.3 Reliability
- Automatically recover from failures
- Scale horizontally to increase availability
- Stop guessing capacity

### 5.4 Performance Efficiency
- Use serverless architectures
- Experiment more often
- Consider mechanical sympathy

### 5.5 Cost Optimization
- Implement cloud financial management
- Adopt consumption model
- Analyze and attribute expenditure

---

## 6. Hands-On Examples

### 6.1 Example 1: Hosting a Static Website on S3 with CloudFront

**Step 1: Create S3 Bucket and Upload Content**

```bash
# Create bucket (bucket name must be globally unique)
aws s3 mb s3://my-website-bucket-2024 --region ap-south-1

# Enable static website hosting
aws s3 website s3://my-website-bucket-2024 \
    --index-document index.html \
    --error-document error.html

# Upload website files
aws s3 sync ./website-files s3://my-website-bucket-2024

# Set bucket policy for public read access
aws s3api put-bucket-policy --bucket my-website-bucket-2024 \
    --policy '{
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-website-bucket-2024/*"
        }]
    }'
```

**Step 2: Configure CloudFront Distribution**

```bash
aws cloudfront create-distribution \
    --origin-domain-name my-website-bucket-2024.s3.amazonaws.com \
    --default-root-object index.html
```

### 6.2 Example 2: Serverless Image Processing with Lambda and S3

This example demonstrates a common pattern: when an image is uploaded to S3, Lambda automatically processes it (creates a thumbnail).

**Step 1: Create Lambda Function**

```python
import boto3
import os
from PIL import Image
import io

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket name and file key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download image from S3
    response = s3_client.get_object(Bucket=bucket, Key=key)
    image_content = response['Body'].read()
    
    # Open image and create thumbnail
    image = Image.open(io.BytesIO(image_content))
    image.thumbnail((128, 128))
    
    # Save thumbnail to buffer
    buffer = io.BytesIO()
    image.save(buffer, "JPEG")
    buffer.seek(0)
    
    # Upload thumbnail to destination bucket
    dest_bucket = f"{bucket}-thumbnails"
    dest_key = f"thumbnails/{key}"
    
    s3_client.put_object(
        Bucket=dest_bucket,
        Key=dest_key,
        Body=buffer,
        ContentType='image/jpeg'
    )
    
    return {
        'statusCode': 200,
        'body': f'Thumbnail created for {key}'
    }
```

**Step 2: Add S3 Trigger to Lambda**

```bash
aws lambda add-permission \
    --function-name image-thumbnail-function \
    --principal s3.amazonaws.com \
    --action lambda:InvokeFunction \
    --statement-id s3-trigger \
    --source-arn arn:aws:s3:::source-bucket

aws s3api put-bucket-notification-configuration \
    --bucket source-bucket \
    --notification-configuration '{
        "LambdaFunctionConfigurations": [{
            "LambdaFunctionArn": "arn:aws:lambda:ap-south-1:123456789012:function:image-thumbnail-function",
            "Events": ["s3:ObjectCreated:Put"]
        }]
    }'
```

**Step 3: Deployment Package (requirements.txt)**

```
boto3
Pillow
```

---

## 7. Challenging MCQs (Application-Based)

### Section A: Multiple Choice Questions

**Q1. A company needs to store customer data for 7 years for regulatory compliance. Which S3 storage class is MOST cost-effective?**
- A) S3 Standard
- B) S3 Standard-IA
- C) S3 Glacier
- D) S3 Glacier Deep Archive

**Answer: D** — S3 Glacier Deep Archive is designed for long-term archive with retrieval times of 12+ hours and is the most cost-effective for data retention beyond 1 year.

---

**Q2. An application requires sub-millisecond latency for database queries. Which AWS service should be implemented?**
- A) RDS with Read Replicas
- B) ElastiCache with Redis
- C) DynamoDB with DAX
- D) Aurora Serverless

**Answer: C** — DynamoDB Accelerator (DAX) provides in-memory caching with microsecond latency, ideal for sub-millisecond requirements.

---

**Q3. A startup wants to deploy a Node.js API that handles 1000 requests/day but expects growth to 1 million/day within 6 months. Which architecture is MOST appropriate?**
- A) EC2 instance with Auto Scaling
- B) ECS containers with Load Balancer
- C) Lambda with API Gateway
- D) Elastic Beanstalk

**Answer: C** — Lambda with API Gateway provides serverless scaling from 0 to handle millions of requests without infrastructure management, perfect for unpredictable growth.

---

**Q4. Which IAM principal should be used by an application running on EC2 to access S3 buckets securely?**
- A) IAM User with Access Keys
- B) IAM Group
- C) IAM Role attached to EC2 instance
- D) Root account credentials

**Answer: C** — IAM Roles provide temporary credentials and should be attached to EC2 instances following the principle of least privilege.

---

**Q5. A company needs to ensure high availability across two geographically distant data centers in Mumbai region. Which configuration is CORRECT?**
- A) Single EC2 instance in us-east-1
- B) Two EC2 instances in different VPCs in ap-south-1
- C) Two EC2 instances in different AZs in ap-south-1
- D) Single RDS instance with Multi-AZ enabled

**Answer: C** — Deploying across different Availability Zones within the same region provides high availability while maintaining low latency.

---

**Q6. A user reports they cannot access their S3 bucket from their VPC endpoint. What could be the cause?**
- A) S3 bucket policy denies the VPC endpoint
- B) Internet Gateway is not attached
- C) NAT Gateway is misconfigured
- D) Security Group blocks port 443

**Answer: A** — S3 bucket policies can explicitly allow or deny access from specific VPC endpoints.

---

**Q7. Which AWS service provides managed Kubernetes clusters?**
- A) ECS
- B) EKS
- C) Fargate
- D) Lightsail

**Answer: B** — Amazon EKS (Elastic Kubernetes Service) provides managed Kubernetes clusters.

---

**Q8. For disaster recovery, a company needs to replicate data to a different region with RPO (Recovery Point Objective) of 15 minutes. Which S3 feature meets this requirement?**
- A) S3 Standard-IA
- B) S3 Cross-Region Replication (CRR)
- C) S3 Versioning
- D) S3 Lifecycle Policies

**Answer: B** — S3 Cross-Region Replication automatically replicates objects to a different region, meeting the RPO requirement.

---

### Section B: True/False Questions

**Q9. AWS Lambda functions can run for up to 24 hours.**
- A) True
- B) False

**Answer: B** — Lambda functions have a maximum execution timeout of 900 seconds (15 minutes).

---

**Q10. Security Groups in AWS are stateful, meaning return traffic is automatically allowed.**
- A) True
- B) False

**Answer: A** — Security Groups are stateful, so if inbound traffic is allowed, the response traffic is automatically permitted regardless of outbound rules.

---

### Section C: Fill in the Blanks

**Q11. The AWS service that provides a logically isolated virtual network is called __________.**

**Answer:** Amazon VPC (Virtual Private Cloud)

---

**Q12. AWS __________ is a managed service that provides Domain Name System (DNS) web service.**

**Answer:** Amazon Route 53

---

## 8. Key Takeaways

1. **AWS Dominance:** AWS is the leading cloud platform with 200+ services; understanding it is essential for modern CS careers.

2. **Global Infrastructure:** AWS operates in geographic Regions, each containing multiple Availability Zones for high availability and fault tolerance.

3. **Core Services:**
   - **Compute:** EC2 (virtual servers), Lambda (serverless), ECS/EKS (containers)
   - **Storage:** S3 (object storage), EBS (block), EFS (file)
   - **Database:** RDS (relational), DynamoDB (NoSQL), ElastiCache (caching)
   - **Networking:** VPC (isolated network), Route 53 (DNS), CloudFront (CDN)
   - **Security:** IAM (access management), KMS (encryption), Security Groups

4. **Pricing Model:** Pay-as-you-go for compute, storage, and data transfer; use Reserved Instances and Savings Plans for cost optimization.

5. **Serverless Revolution:** Lambda enables event-driven architectures without server management, scaling automatically.

6. **Security First:** Follow the principle of least privilege, enable MFA, use IAM roles, encrypt data at rest and in transit.

7. **Well-Architected Framework:** Design for operational excellence, security, reliability, performance efficiency, and cost optimization.

8. **Hands-On Skills:** Practical experience with S3, Lambda, VPC, and IAM is crucial—use the AWS Free Tier for practice.

---

## References and Further Reading

1. **AWS Official Documentation:** https://docs.aws.amazon.com
2. **AWS Well-Architected Framework:** https://aws.amazon.com/architecture/well-architected
3. **AWS Free Tier:** https://aws.amazon.com/free
4. **Delhi University NEP 2024 UGCF Syllabus:** Cloud Computing Module

---

*This study material is designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum. For practical exposure, students are encouraged to create a free AWS account and complete the AWS Cloud Practitioner Essentials digital course.*