# Benefits and Limitations of Cloud Computing

## A Comprehensive Study Material for BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Cloud computing has emerged as one of the most transformative technologies in the modern digital landscape, fundamentally changing how organizations and individuals deploy, manage, and pay for computing resources. According to the Delhi University syllabus for BSc (Hons) Computer Science under NEP 2024 UGCF, cloud computing is a core topic that students must understand thoroughly, as it forms the backbone of modern IT infrastructure and business operations.

In simple terms, cloud computing refers to the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet ("the cloud") to offer faster innovation, flexible resources, and economies of scale. Instead of owning their own computing infrastructure or data centers, organizations can rent access to these resources from cloud service providers like Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP).

The relevance of this technology extends far beyond the classroom. As of 2024, the global cloud computing market is valued at over $600 billion, with adoption rates increasing exponentially across industries. From startups launching their first applications to enterprises running mission-critical workloads, cloud computing has become ubiquitous. Understanding both its benefits and limitations is crucial for any computer science professional, as this knowledge enables informed decision-making when designing, deploying, and managing cloud-based solutions.

This study material provides comprehensive coverage of the benefits and limitations of cloud computing, aligned with the Delhi University curriculum requirements. We will explore each concept in detail, provide practical examples with code demonstrations, and include assessment items of varying difficulty levels to prepare students effectively for semester examinations.

---

## 2. Benefits of Cloud Computing

Cloud computing offers numerous advantages that have driven its widespread adoption. This section provides an exhaustive exploration of these benefits, supported by real-world examples and code demonstrations where applicable.

### 2.1 Cost Efficiency

One of the most compelling benefits of cloud computing is its cost efficiency. Traditional IT infrastructure requires significant capital expenditure (CapEx) for purchasing hardware, setting up data centers, and maintaining physical facilities. Cloud computing transforms these capital expenses into operational expenses (OpEx) through a pay-as-you-go model.

**Key Cost-Related Advantages:**

- **No Initial Hardware Investment**: Organizations can provision computing resources instantly without purchasing physical servers
- **Pay-per-use Pricing**: Users only pay for the resources they consume
- **Reduced Maintenance Costs**: The cloud provider handles hardware maintenance, updates, and repairs
- **Lower Energy Costs**: No need to power and cool in-house data centers
- **Elastic Cost Scaling**: Costs automatically adjust based on demand

**Example: Cost Comparison**

Consider a startup that needs to deploy a web application. Traditionally, they would need to:

- Purchase servers (approximately ₹2-5 lakhs)
- Set up networking infrastructure (approximately ₹50,000-1 lakh)
- Pay for data center space and power (approximately ₹1-2 lakhs annually)
- Hire system administrators (approximately ₹5-8 lakhs annually)

With cloud computing, the same startup can start with a minimal monthly cost (approximately ₹5,000-15,000) and scale as their business grows.

### 2.2 Scalability and Elasticity

Cloud computing provides unparalleled scalability and elasticity—two critical capabilities that differentiate it from traditional infrastructure.

- **Scalability** refers to the ability to increase resources to handle growing workloads
- **Elasticity** refers to the ability to automatically scale up or down based on demand

**Real-World Example:**

An e-commerce website experiences significantly higher traffic during sale seasons (Diwali, Black Friday, etc.). With traditional infrastructure, the company would need to either over-provision resources (wasting money during normal periods) or under-provision (risking website crashes during peak periods). Cloud computing solves this problem through automatic scaling.

**Code Example: Auto-Scaling Configuration in AWS**

```yaml
# AWS Auto Scaling Group Configuration
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Auto Scaling Group for Web Application'

Resources:
  WebServerGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
        - !Ref PublicSubnet1
        - !Ref PublicSubnet2
      LaunchConfigurationName: !Ref LaunchConfig
      MinSize: '2'
      MaxSize: '10'
      DesiredCapacity: '2'
      TargetGroupARNs:
        - !Ref ALBTargetGroup
      MetricsCollection:
        - - GroupMinSize
          - - MetricCollection
        - - GroupMaxSize
        - - MetricCollection

  # Scaling Policy
  ScaleUpPolicy:
    Type: AWS::AutoScaling::ScalingPolicy
    Properties:
      AutoScalingGroupName: !Ref WebServerGroup
      PolicyType: TargetTrackingScaling
      TargetTrackingConfiguration:
        PredefinedMetricSpecification:
          PredefinedMetricType: ASGAverageCPUUtilization
        TargetValue: 70
```

This configuration automatically scales the number of EC2 instances between 2 and 10 based on CPU utilization, ensuring optimal performance while controlling costs.

### 2.3 Flexibility and Accessibility

Cloud computing provides remarkable flexibility in terms of how, when, and where users can access resources and services.

**Key Flexibility Benefits:**

- **Remote Access**: Users can access cloud resources from anywhere with an internet connection
- **Multi-device Support**: Works seamlessly across desktops, laptops, tablets, and smartphones
- **Platform Independence**: Users are not locked into specific hardware or operating systems
- **Service Variety**: Choose from Infrastructure as a Service (IaaS), Platform as a Service (PaaS), or Software as a Service (SaaS)
- **Rapid Deployment**: Deploy applications in minutes rather than weeks or months

**Example: Deploying a Python Flask Application to Cloud**

```python
# Simple Flask application
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Cloud Computing Demo',
        'status': 'Running on cloud infrastructure',
        'environment': os.environ.get('ENVIRONMENT', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

```dockerfile
# Dockerfile for containerizing the application
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000
ENV ENVIRONMENT=production

EXPOSE 5000

CMD ["python", "app.py"]
```

This application can be deployed to any cloud platform (AWS ECS, Azure Container Instances, Google Cloud Run) with minimal configuration changes.

### 2.4 Reliability and Performance

Cloud service providers invest billions of dollars in building robust, reliable infrastructure that would be impossible for most individual organizations to replicate.

**Reliability Features:**

- **High Availability**: Data centers are distributed across multiple geographic regions
- **Redundancy**: Critical components are replicated to eliminate single points of failure
- **99.9% Uptime SLA**: Most major providers guarantee high availability
- **Disaster Recovery**: Built-in backup and recovery mechanisms
- **Load Balancing**: Distributes traffic across multiple servers for optimal performance

**Example: Multi-Region Deployment Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                    Global Load Balancer                     │
└─────────────────────────────────────────────────────────────┘
          │                    │                    │
          ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Asia Pacific   │  │   Europe West   │  │  US East        │
│  (Mumbai)       │  │  (Frankfurt)    │  │  (Virginia)     │
├─────────────────┤  ├─────────────────┤  ├─────────────────┤
│ • Primary DB    │  │ • Secondary DB  │  │ • Secondary DB  │
│ • App Servers   │  │ • App Servers   │  │ • App Servers   │
│ • CDN Edge      │  │ • CDN Edge      │  │ • CDN Edge      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### 2.5 Automatic Updates and Maintenance

Cloud providers continuously update their platforms with new features, security patches, and performance improvements, eliminating the burden of manual updates from users.

**Update-Related Benefits:**

- **Security Patches**: Automatic application of critical security updates
- **New Features**: Regular introduction of new services and capabilities
- **No Downtime for Updates**: Rolling updates ensure continuous availability
- **Compliance Updates**: Automatic adherence to evolving regulatory requirements

### 2.6 Enhanced Collaboration

Cloud computing transforms how teams collaborate by providing shared access to files, applications, and development environments.

**Collaboration Benefits:**

- **Real-time Document Editing**: Multiple users can work on the same document simultaneously (e.g., Google Docs, Microsoft 365)
- **Version Control Integration**: Seamless integration with Git, GitHub, GitLab
- **Shared Development Environments**: Teams can share development environments and configurations
- **Unified Communication**: Integration of email, messaging, video conferencing, and file sharing

---

## 3. Limitations of Cloud Computing

While cloud computing offers numerous benefits, it is essential to understand its limitations and challenges. A comprehensive understanding of both advantages and disadvantages is crucial for making informed architectural decisions.

### 3.1 Security and Privacy Concerns

Despite significant advancements in cloud security, concerns about data security and privacy remain among the most cited limitations.

**Security Challenges:**

- **Data Breaches**: Cloud environments can be targets for cyberattacks
- **Shared Responsibility Model**: Security is a shared responsibility between provider and user
- **Insider Threats**: Malicious insiders at the cloud provider level
- **API Vulnerabilities**: Insecure APIs can expose vulnerabilities
- **Multi-tenancy Risks**: Data isolation between tenants sharing physical resources

**Privacy Concerns:**

- **Data Location**: Uncertainty about where data is physically stored
- **Data Access**: Potential for unauthorized access by cloud provider staff
- **Data Sovereignty**: Legal implications of data stored in different jurisdictions
- **Compliance**: Ensuring cloud services meet industry-specific regulations

**Example: Security Best Practices Implementation**

```python
# Cloud Security Configuration Example
import boto3
from botocore.config import Config

# Configure secure S3 bucket settings
class CloudSecurityManager:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.iam_client = boto3.client('iam')
    
    def setup_secure_bucket(self, bucket_name):
        """Configure secure S3 bucket with encryption and access controls"""
        
        # Enable default encryption
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
        
        # Enable versioning for backup
        self.s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'Status': 'Enabled'
            }
        )
        
        # Block public access
        self.s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'BlockPublicPolicy': True,
                'IgnorePublicAcls': True,
                'RestrictPublicBuckets': True
            }
        )
        
        print(f"Secure configuration applied to bucket: {bucket_name}")
    
    def create_iam_role_with_mfa(self, role_name):
        """Create IAM role requiring MFA for sensitive operations"""
        
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "arn:aws:iam::123456789012:root"},
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "Bool": {"aws:MultiFactorAuthPresent": "true"}
                    }
                }
            ]
        }
        
        self.iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=str(trust_policy)
        )
        
        print(f"Created IAM role with MFA requirement: {role_name}")

# Usage
security_manager = CloudSecurityManager()
security_manager.setup_secure_bucket("my-secure-bucket")
security_manager.create_iam_role_with_mfa("AdminRoleWithMFA")
```

### 3.2 Downtime and Connectivity Issues

Cloud services depend on internet connectivity, and any disruption can impact access to critical resources.

**Downtime Concerns:**

- **Internet Dependency**: Requires stable internet connection for access
- **Provider Downtime**: Cloud providers occasionally experience outages
- **Regional Outages**: Natural disasters or infrastructure failures can affect entire regions
- **Latency Issues**: Physical distance from data centers can cause performance degradation

**Historical Examples:**

- In 2021, a major AWS outage affected thousands of websites and applications for several hours
- In 2020, a Google Cloud outage impacted multiple services globally
- Azure has experienced several regional outages affecting business continuity

**Mitigation Strategies:**

- Implement multi-region architectures
- Use edge computing for critical applications
- Maintain offline backup capabilities
- Design for graceful degradation

### 3.3 Limited Control and Flexibility

When using cloud services, organizations surrender a degree of control over their infrastructure and applications.

**Control Limitations:**

- **Infrastructure Control**: Limited access to underlying hardware and network infrastructure
- **Software Restrictions**: Cannot modify certain system software or configurations
- **Vendor-imposed Limits**: Resource quotas and throttling limits
- **Customization Constraints**: May not be able to customize the environment as needed
- **Exit Challenges**: Difficulty in migrating away from the cloud provider

**Example: Vendor Lock-in Challenges**

```python
# Example demonstrating migration complexity between cloud providers
# AWS to Azure migration considerations

# AWS-specific configurations
aws_config = {
    'service': 'aws',
    'compute': 'ec2',
    'storage': 's3',
    'database': 'rds',
    'networking': 'vpc',
    'authentication': 'iam',
    'monitoring': 'cloudwatch'
}

# Corresponding Azure configurations
azure_config = {
    'service': 'azure',
    'compute': 'virtual_machines',
    'storage': 'blob_storage',
    'database': 'sql_database',
    'networking': 'virtual_network',
    'authentication': 'azure_ad',
    'monitoring': 'azure_monitor'
}

# Code that works on AWS (requires significant rework for Azure)
class AWSStorageService:
    def __init__(self, bucket_name):
        self.bucket = bucket_name
        self.s3 = boto3.client('s3')
    
    def upload_file(self, file_path, key):
        self.s3.upload_file(file_path, self.bucket, key)
    
    def download_file(self, key, download_path):
        self.s3.download_file(self.bucket, key, download_path)

# Migrating to Azure requires entirely different code
class AzureStorageService:
    def __init__(self, container_name):
        self.container = container_name
        self.blob_service = BlockBlobService(
            account_name='your_account',
            account_key='your_key'
        )
    
    def upload_file(self, file_path, blob_name):
        self.blob_service.create_blob_from_path(
            self.container, blob_name, file_path
        )
    
    def download_file(self, blob_name, download_path):
        self.blob_service.get_blob_to_path(
            self.container, blob_name, download_path
        )
```

This example illustrates how cloud-specific code creates vendor lock-in, making migrations costly and time-consuming.

### 3.4 Cost Management Challenges

While cloud computing can reduce costs, improper management can lead to unexpected and often higher expenses.

**Cost-Related Challenges:**

- **Unpredictable Bills**: Usage-based pricing can lead to variable monthly costs
- **Hidden Costs**: Data transfer fees, API calls, and storage costs can accumulate
- **Idle Resources**: Forgotten resources continue to incur charges
- **Over-provisioning**: Allocating more resources than necessary
- **Complex Pricing Models**: Different pricing tiers, reserved instances, and spot pricing can be confusing

**Example: Cost Monitoring and Optimization**

```python
# Cloud Cost Monitoring and Optimization Script
import boto3
from datetime import datetime, timedelta

class CostOptimizer:
    def __init__(self):
        self.ce_client = boto3.client('ce')  # Cost Explorer
        self.ec2_client = boto3.client('ec2')
    
    def get_monthly_costs(self):
        """Get detailed cost breakdown for the current month"""
        
        response = self.ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': datetime.today().replace(day=1).strftime('%Y-%m-%d'),
                'End': datetime.today().strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost', 'BlendedCost'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Dimension': 'SERVICE'}
            ]
        )
        
        print("\n=== Monthly Cost Breakdown ===")
        for result in response['ResultsByTime']:
            for group in result['Groups']:
                service = group['Keys'][0]
                cost = float(group['Metrics']['UnblendedCost']['Amount'])
                if cost > 0:
                    print(f"{service}: ${cost:.2f}")
    
    def find_idle_instances(self, idle_threshold=5):
        """Find EC2 instances with low CPU utilization"""
        
        # Get all running instances
        reservations = self.ec2_client.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )['Reservations']
        
        print(f"\n=== Idle Instance Report (CPU < {idle_threshold}%) ===")
        
        for reservation in reservations:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_type = instance['InstanceType']
                
                # Get CPU metrics (simplified)
                # In production, use CloudWatch metrics
                print(f"Instance: {instance_id} ({instance_type})")
                print(f"  Consider: Resize or terminate if unused")
    
    def suggest_savings(self):
        """Suggest cost optimization opportunities"""
        
        print("\n=== Cost Optimization Suggestions ===")
        print("1. Use Reserved Instances for steady-state workloads")
        print("2. Implement auto-scaling for variable workloads")
        print("3. Use Spot Instances for fault-tolerant batch jobs")
        print("4. Enable S3 Intelligent-Tiering for variable access patterns")
        print("5. Set up cost alerts and budgets")
        print("6. Schedule non-production instances to stop during off-hours")

# Usage
optimizer = CostOptimizer()
optimizer.get_monthly_costs()
optimizer.find_idle_instances()
optimizer.suggest_savings()
```

### 3.5 Compliance and Legal Issues

Organizations operating in regulated industries face significant compliance challenges when adopting cloud computing.

**Compliance Challenges:**

- **Data Protection Regulations**: GDPR, HIPAA, PCI-DSS compliance
- **Industry-Specific Requirements**: Financial, healthcare, government regulations
- **Audit Requirements**: Demonstrating compliance to auditors
- **Data Residency**: Legal requirements for data storage locations
- **Third-party Risk**: Compliance responsibilities extend to cloud providers

**Key Considerations:**

- Understand the shared responsibility model
- Review provider compliance certifications (SOC 2, ISO 27001, etc.)
- Ensure data processing agreements are in place
- Maintain documentation for compliance audits

### 3.6 Performance Limitations

While cloud computing generally offers excellent performance, certain use cases may experience limitations.

**Performance Challenges:**

- **Latency**: Not ideal for real-time applications requiring sub-millisecond latency
- **Bandwidth Costs**: High data transfer costs can impact application design
- **Shared Resources**: Noisy neighbor issues in multi-tenant environments
- **Network Dependency**: Performance limited by network conditions

---

## 4. Comparative Summary: Benefits vs Limitations

| Aspect | Benefits | Limitations |
|--------|----------|-------------|
| **Cost** | Pay-as-you-go, reduced CapEx | Unpredictable bills, hidden costs |
| **Scalability** | Instant scaling, elastic resources | Vendor limits and throttling |
| **Security** | Enterprise-grade security | Data breaches, shared responsibility |
| **Accessibility** | Access from anywhere | Internet dependency |
| **Maintenance** | Automatic updates | Limited control over environment |
| **Reliability** | 99.9%+ uptime guarantees | Potential provider downtime |
| **Compliance** | Certified data centers | Complex compliance requirements |

---

## 5. Key Takeaways

1. **Cost Efficiency**: Cloud computing transforms capital expenses to operational expenses through pay-as-you-go pricing, eliminating large upfront investments in hardware and infrastructure.

2. **Scalability and Elasticity**: Cloud resources can be automatically scaled up or down based on demand, ensuring optimal performance while controlling costs.

3. **Accessibility and Flexibility**: Users can access cloud resources from anywhere, using any device, with minimal configuration requirements.

4. **Security is a Shared Responsibility**: While cloud providers secure the infrastructure, users are responsible for securing their data, applications, and access controls.

5. **Vendor Lock-in is Real**: Migrating between cloud providers is complex and costly due to proprietary services and APIs.

6. **Cost Management Requires Vigilance**: Continuous monitoring is essential to avoid unexpected charges from idle resources or hidden fees.

7. **Connectivity is Critical**: Cloud services require reliable internet connectivity; downtime can significantly impact business operations.

8. **Compliance Must Be Addressed**: Organizations must ensure their cloud implementations meet industry-specific regulatory requirements.

9. **Hybrid and Multi-cloud Strategies**: Many organizations adopt hybrid or multi-cloud approaches to balance benefits while mitigating limitations.

10. **Strategic Decision-Making**: Understanding both benefits and limitations enables informed decisions about when to use cloud services and when traditional infrastructure might be more appropriate.

---

## 6. Assessment Questions

### Multiple Choice Questions (MCQs)

#### Easy Level

**Question 1:** Which of the following is NOT a benefit of cloud computing?
- (a) Cost efficiency
- (b) Scalability
- (c) Unlimited control over hardware
- (d) Automatic updates

**Answer:** (c) Unlimited control over hardware

---

**Question 2:** What type of cloud computing service provides virtual machines, storage, and networking?
- (a) SaaS
- (b) PaaS
- (c) IaaS
- (d) All of the above

**Answer:** (c) IaaS

---

#### Medium Level

**Question 3:** In the cloud computing shared responsibility model, which of the following is the customer's responsibility?
- (a) Physical security of data centers
- (b) Network infrastructure
- (c) Application code and data
- (d) Hypervisor security

**Answer:** (c) Application code and data

---

**Question 4:** Which cloud deployment model provides services to multiple organizations but isolates resources logically?
- (a) Public Cloud
- (b) Private Cloud
- (c) Community Cloud
- (d) Hybrid Cloud

**Answer:** (a) Public Cloud

---

**Question 5:** What is the primary challenge associated with vendor lock-in in cloud computing?
- (a) Security vulnerabilities
- (b) Difficulty migrating between providers
- (c) Higher costs
- (d) Compliance issues

**Answer:** (b) Difficulty migrating between providers

---

#### Difficult Level

**Question 6:** Which of the following strategies helps mitigate the risk of cloud provider downtime?
- (a) Using a single data center
- (b) Implementing multi-region deployment
- (c) Depending on a single availability zone
- (d) Avoiding auto-scaling

**Answer:** (b) Implementing multi-region deployment

---

**Question 7:** In cloud cost optimization, what does the term "idle resources" refer to?
- (a) Resources that are turned off
- (b) Resources provisioned but underutilized, incurring costs
- (c) Resources that have reached their maximum capacity
- (d) Resources that are being attacked

**Answer:** (b) Resources provisioned but underutilized, incurring costs

---

**Question 8:** Which AWS feature automatically adjusts compute capacity based on CPU utilization?
- (a) AWS Lambda
- (b) Amazon S3
- (c) Auto Scaling Groups
- (d) Amazon RDS

**Answer:** (c) Auto Scaling Groups

---

**Question 9:** What is the main concern regarding data privacy in cloud computing?
- (a) Faster data access
- (b) Uncertainty about data location and jurisdiction
- (c) Reduced storage costs
- (d) Automatic software updates

**Answer:** (b) Uncertainty about data location and jurisdiction

---

**Question 10:** Which of the following is a characteristic of SaaS (Software as a Service)?
- (a) Users manage virtual machines
- (b) Users deploy their own applications
- (c) Applications are delivered over the internet
- (d) Users control the underlying infrastructure

**Answer:** (c) Applications are delivered over the internet

---

### Short Answer Questions

**Question 1:** Explain the concept of "pay-as-you-go" pricing in cloud computing and how it benefits startups. (3 marks)

**Answer:** Pay-as-you-go pricing in cloud computing allows users to pay only for the computing resources they consume, without any upfront capital investment. For startups, this means they can launch applications with minimal initial capital, scale resources as their business grows, and avoid over-provisioning infrastructure. This model converts capital expenses (CapEx) into operational expenses (OpEx), improving cash flow and reducing financial risk.

---

**Question 2:** Discuss two security concerns associated with cloud computing and their mitigation strategies. (4 marks)

**Answer:** Two major security concerns in cloud computing are:

1. **Data Breaches**: Mitigation involves implementing strong encryption (both at rest and in transit), proper access control through IAM, regular security audits, and multi-factor authentication.

2. **Shared Responsibility Confusion**: Organizations must clearly understand which security aspects are handled by the provider versus the customer. This includes proper configuration of cloud services, regular vulnerability assessments, and maintaining compliance.

---

**Question 3:** What is vendor lock-in? Explain one strategy to minimize its impact. (3 marks)

**Answer:** Vendor lock-in refers to the difficulty and cost associated with migrating from one cloud provider to another due to proprietary services, APIs, and data formats.

**Strategy to minimize:** Use containerization (Docker/Kubernetes) and cloud-agnostic architectures that abstract cloud-specific services, enabling easier migration between providers.

---

### Long Answer Questions

**Question 1:** "Cloud computing offers significant benefits but also presents notable limitations." Discuss this statement with reference to at least FOUR benefits and FOUR limitations of cloud computing. (10 marks)

**Answer:** Cloud computing has revolutionized IT infrastructure, but it is essential to understand both its advantages and disadvantages:

**Benefits:**

1. **Cost Efficiency**: Eliminates capital expenditure through pay-as-you-go pricing
2. **Scalability**: Provides instant provisioning and elastic scaling capabilities
3. **Accessibility**: Enables access to resources from anywhere with internet connectivity
4. **Reliability**: Offers 99.9%+ uptime with built-in redundancy and disaster recovery

**Limitations:**

1. **Security Concerns**: Data breaches and shared responsibility challenges
2. **Downtime Risk**: Internet dependency and potential provider outages
3. **Limited Control**: Reduced control over infrastructure and configuration
4. **Vendor Lock-in**: Difficulty migrating between cloud providers
5. **Cost Management**: Unpredictable bills and hidden fees
6. **Compliance**: Complex regulatory and legal requirements

A balanced approach considering both aspects is essential for successful cloud adoption.

---

**Question 2:** Explain the concept of scalability and elasticity in cloud computing with the help of a practical example. How do auto-scaling groups help achieve these goals? (8 marks)

**Answer:** **Scalability** refers to the ability to increase capacity to handle growing workloads, while **elasticity** is the automatic adjustment of resources based on demand.

**Practical Example:** An e-commerce website during a sale event may experience traffic increase from 1,000 to 100,000 visitors per hour. Without cloud computing, the company would need to either maintain servers for peak traffic (wasting resources) or risk crashes during high traffic.

**Auto-Scaling Groups** address this by:
- Monitoring metrics like CPU utilization
- Automatically adding instances when demand increases
- Removing instances when demand decreases
- Maintaining desired capacity with predefined minimum and maximum limits
- Distributing traffic across instances using load balancers

This ensures optimal performance at minimum cost.

---

### True/False Questions

**Question 1:** In cloud computing, the customer is responsible for physical security of data centers. (True/False)

**Answer:** False - Physical security is the responsibility of the cloud provider.

---

**Question 2:** Serverless computing eliminates the need for servers entirely. (True/False)

**Answer:** False - Serverless computing abstracts server management but still runs on servers managed by the cloud provider.

---

**Question 3:** Multi-cloud strategies can help mitigate vendor lock-in risks. (True/False)

**Answer:** True - Using multiple cloud providers reduces dependency on a single vendor.

---

**Question 4:** Cloud computing always reduces IT costs compared to on-premises infrastructure. (True/False)

**Answer:** False - While cloud can reduce costs, improper management can lead to higher expenses.

---

**Question 5:** Data stored in the cloud is always more secure than on-premises data. (True/False)

**Answer:** False - Security depends on implementation; both cloud and on-premises can be secure or vulnerable based on practices.

---

## 7. References and Further Reading

1. Delhi University BSc (Hons) Computer Science Syllabus - NEP 2024 UGCF
2. AWS Documentation: https://docs.aws.amazon.com
3. Microsoft Azure Documentation: https://docs.microsoft.com/azure
4. Google Cloud Documentation: https://cloud.google.com/docs
5. "Cloud Computing: Concepts, Technology & Architecture" by Thomas Erl
6. NIST Special Publication 800-145 - Definition of Cloud Computing

---

*This study material has been prepared in accordance with the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF guidelines.*