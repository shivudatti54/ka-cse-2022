# History and Cloud Service Providers
## Cloud Computing - BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Cloud Computing has revolutionized the way organizations deploy, manage, and scale their IT infrastructure. From streaming movies on Netflix to running complex machine learning models, cloud services power the digital world we live in today. This chapter explores the historical evolution of cloud computing and examines the major cloud service providers that dominate the industry today.

**Real-World Relevance:**
- Netflix runs entirely on AWS, streaming to over 230 million subscribers
- Uber uses AWS and GCP for real-time ride matching
- Banks like Capital One have migrated completely to AWS
- Startups can now launch globally without investing in physical infrastructure

This study material aligns with the Delhi University NEP 2024 UGCF syllabus for Cloud Computing, covering all essential topics including history, virtualization, service models, deployment models, and cloud providers.

---

## 2. History of Cloud Computing

### 2.1 Early Foundations (1950s-1970s)

The concept of cloud computing traces its roots to the **1950s** when mainframes were expensive shared resources:

- **Time-Sharing (1960s):** Multiple users could access a single mainframe computer simultaneously. This was the first instance of resource sharing and virtualization concepts.
- **ARPANET (1969):** The precursor to the internet laid the groundwork for networked computing and remote access.

### 2.2 Grid Computing (1990s)

Grid computing emerged in the late 1990s as a way to combine distributed computing resources for solving large-scale computational problems.

**Key Characteristics of Grid Computing:**
- Distributed resources across geographic locations
- Resource sharing and coordination
- Used in scientific research (e.g., CERN's Large Hadron Collider)
- No centralized management

**Grid vs. Cloud Computing:**

| Feature | Grid Computing | Cloud Computing |
|---------|---------------|-----------------|
| Resource Allocation | Static, job-based | Dynamic, on-demand |
| Management | Decentralized | Centralized |
| Billing | Not usage-based | Pay-as-you-go |
| Example | SETI@Home | AWS EC2 |

Grid computing laid the foundation for modern cloud services by proving that distributed resources could work together. However, it lacked the elasticity and commercial service models that define cloud computing today.

### 2.3 Utility Computing (Early 2000s)

The concept of **utility computing** treated computing resources like electricity—users pay only for what they use. This model combined:

- **On-demand resource provisioning**
- **Pay-per-use pricing**
- **Service-level agreements (SLAs)**

Companies like IBM and HP offered utility computing solutions, but the technology wasn't mature enough for widespread adoption.

### 2.4 Birth of Modern Cloud Computing (2006-Present)

**Key Milestones:**

| Year | Event |
|------|-------|
| 2002 | Amazon launches AWS (initial services) |
| 2006 | Amazon Elastic Compute Cloud (EC2) goes live |
| 2008 | Google App Engine launched |
| 2009 | Microsoft Azure released |
| 2010 | Rackspace launches OpenStack |
| 2011-2024 | Explosive growth with GCP, Azure, IBM, Oracle |

**Salesforce.com (1999)** is often credited as the first true "cloud" company, offering Software as a Service (SaaS) for customer relationship management.

---

## 3. Virtualization - The Foundation of Cloud Computing

Virtualization is the **core technology** that enables cloud computing. It allows multiple virtual machines to run on a single physical server, maximizing resource utilization.

### 3.1 What is Virtualization?

Virtualization creates a software-based representation of physical hardware resources—servers, storage, or network devices. This abstraction layer enables:

- **Hardware independence:** Virtual machines can run on any compatible hardware
- **Isolation:** Each VM operates independently
- **Efficiency:** Better utilization of physical resources
- **Cost savings:** Reduced hardware costs and energy consumption

### 3.2 Types of Virtualization

1. **Server Virtualization:** Divides a physical server into multiple isolated virtual servers
2. **Network Virtualization:** Creates virtual network switches, routers, and firewalls
3. **Storage Virtualization:** Pools multiple physical storage devices into a single logical unit
4. **Desktop Virtualization:** Runs desktop environments on central servers (VDI - Virtual Desktop Infrastructure)

### 3.3 Hypervisors

A **hypervisor** is software that creates and runs virtual machines. There are two types:

**Type 1 (Bare-Metal):**
- Runs directly on hardware
- Examples: VMware ESXi, Microsoft Hyper-V, Xen
- Used in enterprise data centers

**Type 2 (Hosted):**
- Runs as an application on a host OS
- Examples: VMware Workstation, VirtualBox, Parallels
- Used for testing and development

**Example: Using VirtualBox (Type 2 Hypervisor)**

```bash
# Create a virtual machine using VBoxManage command line
VBoxManage createvm --name "CloudLabVM" --ostype "Ubuntu_64" --register

# Configure resources
VBoxManage modifyvm "CloudLabVM" --memory 2048 --cpus 2

# Create virtual hard disk
VBoxManage createhd --filename "CloudLabVM.vdi" --size 20480 --format VDI

# Attach storage controller
VBoxManage storagectl "CloudLabVM" --name "SATA Controller" --add sata

# Attach disk and ISO
VBoxManage storageattach "CloudLabVM" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "CloudLabVM.vdi"
VBoxManage storageattach "CloudLabVM" --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium "ubuntu-22.04.iso"
```

---

## 4. Cloud Service Models

Cloud computing offers three primary service models, each providing different levels of control and management.

### 4.1 Infrastructure as a Service (IaaS)

IaaS provides virtualized computing resources over the internet. Users manage:
- Operating systems
- Applications
- Data

The provider manages:
- Physical infrastructure
- Hardware virtualization
- Networking
- Storage

**Examples:** AWS EC2, Google Compute Engine, Microsoft Azure Virtual Machines, DigitalOcean

**Use Cases:**
- Website hosting
- Development and testing environments
- Disaster recovery

**Example: Launching an AWS EC2 Instance**

```python
import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Launch an instance
response = ec2.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Ubuntu AMI
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='my-key-pair',
    SecurityGroups=['launch-wizard-1']
)

print(f"Instance ID: {response['Instances'][0]['InstanceId']}")
```

### 4.2 Platform as a Service (PaaS)

PaaS provides a complete development and deployment environment. Users manage:
- Applications
- Data

The provider manages:
- Operating systems
- Middleware
- Runtime
- Infrastructure

**Examples:** AWS Elastic Beanstalk, Google App Engine, Microsoft Azure App Service, Heroku

**Use Cases:**
- Application development and deployment
- API development
- Business intelligence applications

**Example: Deploying to Google App Engine (Python)**

```yaml
# app.yaml configuration
runtime: python39
entrypoint: gunicorn -b :$PORT main:app

handlers:
- url: /
  static_files: static/index.html
  upload: static/index.html

- url: /api/*
  script: auto
```

```python
# main.py - Simple Flask application
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Cloud Computing!',
        'service': 'Google App Engine'
    })

@app.route('/api/status')
def status():
    return jsonify({'status': 'running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```

### 4.3 Software as a Service (SaaS)

SaaS delivers software applications over the internet. Users access the application; the provider manages everything.

**What the provider manages:**
- Everything (infrastructure, applications, data, security)

**What the user manages:**
- User settings and preferences
- Some data management

**Examples:** Google Workspace, Microsoft 365, Salesforce, Netflix, Dropbox

**Use Cases:**
- Email services (Gmail)
- Customer relationship management (Salesforce)
- Collaboration tools (Microsoft Teams)
- Entertainment (Netflix, Spotify)

---

## 5. Cloud Deployment Models

### 5.1 Public Cloud

Services are delivered over the public internet and shared across multiple organizations.

**Characteristics:**
- Owned by cloud service providers
- Pay-as-you-go pricing
- Scalability on demand
- Examples: AWS, Azure, GCP

**Advantages:**
- Lower capital costs
- No maintenance burden
- Global accessibility

### 5.2 Private Cloud

Dedicated cloud infrastructure for a single organization.

**Characteristics:**
- Can be on-premises or hosted
- Enhanced security and control
- Customizable resources

**Use Cases:**
- Financial institutions
- Government organizations
- Healthcare (for HIPAA compliance)

### 5.3 Hybrid Cloud

Combines public and private cloud infrastructure, allowing data and applications to move between them.

**Characteristics:**
- Flexible workload placement
- Data portability
- Bursting to public cloud during peak demand

**Example Use Case:**
- Bank stores sensitive customer data in private cloud
- Uses public cloud for analytics and marketing campaigns

### 5.4 Community Cloud

Shared infrastructure for specific communities (e.g., government agencies, universities).

**Characteristics:**
- Shared by organizations with common requirements
- Cost-effective for community members
- Can be managed internally or by third parties

---

## 6. Major Cloud Service Providers

### 6.1 Amazon Web Services (AWS)

**Founded:** 2006 (first major cloud provider)

**Market Share:** ~32% (as of 2024)

**Key Services:**

| Category | Services |
|----------|----------|
| Compute | EC2, Lambda, ECS, EKS |
| Storage | S3, EBS, Glacier |
| Database | RDS, DynamoDB, ElastiCache |
| Networking | VPC, Route 53, CloudFront |
| AI/ML | SageMaker, Rekognition |

**Notable Features:**
- Largest ecosystem of services
- 33 Availability Zones globally
- Extensive certification programs

**Example: Simple S3 Bucket Operation**

```python
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Upload a file to S3
s3.upload_file(
    Bucket='my-university-notes',
    Key='cloud-computing/lecture1.pdf',
    Filename='./lecture1.pdf',
    ExtraArgs={'Metadata': {'subject': 'Cloud Computing'}}
)

# Generate presigned URL for download
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': 'my-university-notes', 'Key': 'cloud-computing/lecture1.pdf'},
    ExpiresIn=3600
)

print(f"Download URL: {url}")
```

### 6.2 Microsoft Azure

**Founded:** 2010 (released publicly)

**Market Share:** ~23% (as of 2024)

**Key Services:**

| Category | Services |
|----------|----------|
| Compute | Virtual Machines, Azure Functions, AKS |
| Storage | Blob Storage, Azure Files, Disk Storage |
| Database | Azure SQL, Cosmos DB, Azure Database |
| Networking | Virtual Network, Azure CDN, Load Balancer |
| Enterprise | Active Directory, Microsoft 365 integration |

**Notable Features:**
- Strong enterprise presence
- Seamless integration with Windows Server
- Hybrid cloud capabilities (Azure Arc)

### 6.3 Google Cloud Platform (GCP)

**Founded:** 2008 (Google App Engine)

**Market Share:** ~11% (as of 2024)

**Key Services:**

| Category | Services |
|----------|----------|
| Compute | Compute Engine, Cloud Functions, GKE |
| Storage | Cloud Storage, Filestore, Persistent Disk |
| Database | Cloud SQL, Firestore, Bigtable |
| Big Data | BigQuery, Dataflow, Dataproc |
| AI/ML | Vertex AI, TensorFlow, AutoML |

**Notable Features:**
- Leading in data analytics and ML
- Strong open-source contributions (Kubernetes)
- Global fiber network

**Example: Using Google BigQuery**

```python
from google.cloud import bigquery

# Initialize client
client = bigquery.Client()

# Query public dataset
query = """
    SELECT 
        name,
        SUM(number) as total_speakers
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'CA'
    GROUP BY name
    ORDER BY total_speakers DESC
    LIMIT 10
"""

# Execute query
query_job = client.query(query)

# Print results
print("Top 10 names in California:")
for row in query_job.result():
    print(f"{row.name}: {row.total_speakers}")
```

### 6.4 Other Major Providers

**IBM Cloud:**
- Strong in enterprise and hybrid cloud
- Watson AI services
- Focus on regulated industries

**Oracle Cloud:**
- Database-focused offerings
- Enterprise applications
- Strong in ERP and CRM

**Alibaba Cloud:**
- Leading provider in China
- Strong in Asian markets
- Competitive pricing

---

## 7. Key Characteristics of Cloud Computing

### 7.1 Essential Characteristics (NIST Model)

1. **On-Demand Self-Service:** Users can provision resources automatically without human intervention
2. **Broad Network Access:** Services available over the network through standard mechanisms
3. **Resource Pooling:** Provider's resources are pooled to serve multiple customers
4. **Elasticity:** Resources can be scaled up or down automatically
5. **Measured Service:** Usage is monitored and billed transparently

### 7.2 Advantages of Cloud Computing

- **Cost Efficiency:** Pay-as-you-go reduces capital expenditure
- **Scalability:** Handle varying workloads easily
- **Reliability:** Multiple data centers ensure high availability
- **Accessibility:** Access from anywhere with internet
- **Automatic Updates:** Providers handle infrastructure updates

### 7.3 Challenges and Considerations

- **Security and Privacy:** Data breaches, compliance issues
- **Downtime:** Service outages can impact business
- **Vendor Lock-in:** Difficult to migrate between providers
- **Latency:** Physical distance can affect performance
- **Cost Management:** Unmonitored usage can lead to high bills

---

## 8. Key Takeaways

1. **Historical Evolution:** Cloud computing evolved from mainframe time-sharing (1950s) → Grid computing (1990s) → Utility computing (2000s) → Modern cloud (2006-present)

2. **Virtualization:** The foundational technology enabling cloud computing, allowing multiple virtual machines on physical hardware through hypervisors

3. **Service Models:**
   - **IaaS:** Infrastructure (AWS EC2, Azure VMs)
   - **PaaS:** Platform (AWS Elastic Beanstalk, Google App Engine)
   - **SaaS:** Software (Salesforce, Microsoft 365)

4. **Deployment Models:**
   - Public Cloud (shared, pay-per-use)
   - Private Cloud (dedicated, enhanced control)
   - Hybrid Cloud (combined flexibility)
   - Community Cloud (shared by specific groups)

5. **Major Providers:** AWS (market leader), Azure (enterprise strength), GCP (data/ML focus), IBM Cloud (enterprise), Oracle Cloud (database)

6. **Key Characteristics:** On-demand self-service, broad network access, resource pooling, elasticity, measured service

7. **Real-World Impact:** Cloud computing enables global-scale applications, reduces IT costs, and powers modern digital services

---

## 9. Multiple Choice Questions (MCQs)

### Question 1
**Which of the following is considered the first true "cloud" company that offered SaaS?**

a) Amazon Web Services  
b) Salesforce.com  
c) Google  
d) Microsoft Azure

**Answer:** b) Salesforce.com  
**Explanation:** Salesforce.com, launched in 1999, is widely recognized as the first company to offer software as a service (SaaS) for customer relationship management, predating modern cloud computing by several years.

---

### Question 2
**Which cloud service model gives users the most control over the underlying infrastructure?**

a) SaaS  
b) PaaS  
c) IaaS  
d) FaaS

**Answer:** c) IaaS  
**Explanation:** Infrastructure as a Service (IaaS) provides virtualized computing resources where users manage operating systems, applications, and data, while the provider handles physical infrastructure and virtualization.

---

### Question 3
**What type of hypervisor runs directly on the hardware without a host operating system?**

a) Type 1 (Bare-Metal)  
b) Type 2 (Hosted)  
c) Type 3  
d) Type 4

**Answer:** a) Type 1 (Bare-Metal)  
**Explanation:** Type 1 hypervisors (e.g., VMware ESXi, Hyper-V) run directly on hardware, providing better performance and are commonly used in enterprise data centers.

---

### Question 4
**Which AWS service is an example of IaaS?**

a) S3  
b) Lambda  
c) EC2  
d) SageMaker

**Answer:** c) EC2  
**Explanation:** Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud, representing the IaaS model where users manage virtual machines.

---

### Question 5
**In a hybrid cloud deployment, which component typically stores sensitive data?**

a) Public Cloud  
b) Private Cloud  
c) Community Cloud  
d) Edge Cloud

**Answer:** b) Private Cloud  
**Explanation:** Sensitive data is typically stored in a private cloud for enhanced security and compliance, while the public cloud handles less sensitive workloads like analytics.

---

### Question 6
**Which Google Cloud service is primarily used for big data analytics?**

a) Cloud Functions  
b) BigQuery  
c) Compute Engine  
d) Cloud Storage

**Answer:** b) BigQuery  
**Explanation:** BigQuery is Google's fully managed, serverless data warehouse designed for big data analytics with SQL-like queries.

---

### Question 7
**Grid computing differs from cloud computing primarily in:**

a) Use of virtualization  
b) Billing model  
c) Geographic distribution  
d) Network protocols

**Answer:** b) Billing model  
**Explanation:** Grid computing typically doesn't use usage-based billing, while cloud computing operates on a pay-as-you-go utility model.

---

### Question 8
**Which of the following is NOT one of the five essential characteristics of cloud computing (NIST)?**

a) On-Demand Self-Service  
b) Resource Pooling  
c) Multi-tenancy  
d) Measured Service

**Answer:** c) Multi-tenancy  
**Explanation:** The five NIST characteristics are: on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service. Multi-tenancy is a feature but not listed as an essential characteristic.

---

### Question 9
**What is the primary function of a hypervisor?**

a) Network security  
b) Creating and managing virtual machines  
c) Database management  
d) Load balancing

**Answer:** b) Creating and managing virtual machines  
**Explanation:** A hypervisor is software that creates and runs virtual machines, allowing multiple operating systems to run on a single physical server.

---

### Question 10
**Which deployment model is best suited for an organization requiring compliance with specific regulations like HIPAA?**

a) Public Cloud  
b) Private Cloud  
c) Hybrid Cloud  
d) Community Cloud

**Answer:** b) Private Cloud or d) Community Cloud  
**Explanation:** For strict compliance requirements like HIPAA in healthcare, organizations often use private clouds (dedicated infrastructure) or community clouds shared with other regulated entities.

---

## 10. Flashcards

### Flashcard 1
**Front:** What is virtualization in cloud computing?

**Back:** Virtualization is the process of creating a software-based representation of physical hardware resources (servers, storage, network). It enables multiple virtual machines to run on a single physical server, maximizing resource utilization and providing hardware independence.

---

### Flashcard 2
**Front:** Define IaaS (Infrastructure as a Service)

**Back:** IaaS is a cloud service model that provides virtualized computing resources (servers, storage, networking) over the internet. Users manage operating systems, applications, and data, while the provider manages physical infrastructure and virtualization. Examples: AWS EC2, Azure Virtual Machines, Google Compute Engine.

---

### Flashcard 3
**Front:** What is the difference between Type 1 and Type 2 hypervisors?

**Back:** Type 1 (Bare-Metal) hypervisors run directly on hardware without a host OS, providing better performance and used in data centers (VMware ESXi, Hyper-V). Type 2 (Hosted) hypervisors run as applications on a host OS, used for testing and development (VirtualBox, VMware Workstation).

---

### Flashcard 4
**Front:** List the five essential characteristics of cloud computing (NIST model)

**Back:**
1. On-Demand Self-Service
2. Broad Network Access
3. Resource Pooling
4. Rapid Elasticity
5. Measured Service

---

### Flashcard 5
**Front:** What is vendor lock-in in cloud computing?

**Back:** Vendor lock-in occurs when a customer becomes dependent on a specific cloud provider's services and technologies, making it difficult and costly to switch to another provider. This can happen due to proprietary APIs, unique services, or significant data migration challenges.

---

### Flashcard 6
**Front:** What is the main advantage of a hybrid cloud deployment?

**Back:** Hybrid cloud combines public and private cloud infrastructure, allowing organizations to keep sensitive data in a private cloud while using the public cloud for scalable, cost-effective resources. This provides flexibility, better security for critical data, and the ability to handle peak workloads.

---

### Flashcard 7
**Front:** How does SaaS differ from PaaS?

**Back:** SaaS (Software as a Service) delivers complete applications over the internet; users only manage settings and data (e.g., Gmail, Salesforce). PaaS (Platform as a Service) provides a development and deployment environment; users manage applications and data while the provider handles OS, middleware, and runtime (e.g., Google App Engine, Heroku).

---

### Flashcard 8
**Front:** What was the significance of AWS EC2 in 2006?

**Back:** Amazon EC2 (Elastic Compute Cloud), launched in 2006, was the first commercial IaaS product that allowed users to rent virtual servers on demand. It revolutionized cloud computing by enabling businesses to provision computing resources quickly without investing in physical hardware.

---

### Flashcard 9
**Front:** Name three major cloud service providers and their market focus

**Back:**
- **AWS:** Largest ecosystem, general-purpose cloud
- **Microsoft Azure:** Enterprise solutions, Windows integration
- **Google Cloud Platform:** Data analytics, machine learning, Kubernetes

---

### Flashcard 10
**Front:** What is the concept of "pay-as-you-go" in cloud computing?

**Back:** Pay-as-you-go is a pricing model where users pay only for the computing resources they consume, without upfront capital investment. It enables cost optimization, as organizations can scale resources up or down based on demand, similar to paying for electricity or water utility services.

---

*This study material is prepared for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF) - Cloud Computing Course.*