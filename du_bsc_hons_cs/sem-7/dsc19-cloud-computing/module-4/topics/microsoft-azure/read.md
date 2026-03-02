# Microsoft Azure - Comprehensive Study Material

## Cloud Computing (BSc Hons Computer Science - NEP 2024 UGCF)
### Delhi University

---

## Table of Contents
1. [Introduction to Cloud Computing and Microsoft Azure](#1-introduction-to-cloud-computing-and-microsoft-azure)
2. [Azure Core Concepts and Architecture](#2-azure-core-concepts-and-architecture)
3. [Azure Compute Services](#3-azure-compute-services)
4. [Azure Networking](#4-azure-networking)
5. [Azure Storage Services](#5-azure-storage-services)
6. [Azure Database Services](#6-azure-database-services)
7. [Azure Security and Identity Management](#7-azure-security-and-identity-management)
8. [Azure Serverless Computing](#8-azure-serverless-computing)
9. [Azure DevOps Services](#9-azure-devops-services)
10. [Azure AI and Machine Learning Services](#10-azure-ai-and-machine-learning-services)
11. [Practical Examples with Code](#11-practical-examples-with-code)
12. [Multiple Choice Questions](#12-multiple-choice-questions)
13. [Flashcards](#13-flashcards)
14. [Key Takeaways](#14-key-takeaways)
15. [References and Syllabus Context](#15-references-and-syllabus-context)

---

## 1. Introduction to Cloud Computing and Microsoft Azure

### 1.1 What is Cloud Computing?

Cloud computing is the delivery of computing services over the internet ("the cloud"), enabling on-demand access to resources like servers, storage, databases, networking, software, analytics, and intelligence. Instead of owning and maintaining physical data centers, organizations can rent these resources from cloud service providers on a pay-as-you-go basis.

**Key Characteristics of Cloud Computing:**
- **On-demand self-service**: Users can provision resources automatically without human intervention
- **Broad network access**: Services are available over the network through standard mechanisms
- **Resource pooling**: Multiple customers share pooled resources (multi-tenant model)
- **Elasticity**: Resources can be scaled up or down rapidly based on demand
- **Measured service**: Usage is monitored, controlled, and reported for transparency

### 1.2 What is Microsoft Azure?

Microsoft Azure (formerly Windows Azure) is a comprehensive cloud computing platform and online portal that allows you to access and manage cloud services and resources provided by Microsoft. Launched in 2010, Azure provides a wide array of cloud-based services including computing, analytics, storage, networking, and AI/ML capabilities.

**Why Microsoft Azure?**

| Factor | Description |
|--------|-------------|
| **Market Position** | Second-largest cloud provider after AWS |
| **Enterprise Trust** | Used by 95% of Fortune 500 companies |
| **Hybrid Capabilities** | Strong support for hybrid cloud scenarios |
| **Integration** | Seamless integration with Microsoft ecosystem |
| **Compliance** | Offers 90+ compliance certifications |

### 1.3 Real-World Relevance

Azure powers numerous global applications and services:

- **Netflix**: Uses Azure for content delivery and streaming infrastructure
- **Adobe**: Runs its Creative Cloud on Azure
- **Walmart**: Leverages Azure for e-commerce and inventory management
- **BMW**: Connected car platform built on Azure IoT
- **Microsoft Teams**: Powers communication for millions of organizations

---

## 2. Azure Core Concepts and Architecture

### 2.1 Azure Regions and Availability Zones

**Azure Regions** are geographic data centers located around the world. Each region contains multiple data centers equipped with independent power, cooling, and networking.

**Key Points:**
- Azure has 60+ regions worldwide
- Some services are region-specific
- Customers can choose regions for data residency and compliance

**Availability Zones** are physically separated data centers within a region, connected with low-latency networking. They provide redundancy and high availability.

```
Region Example: Central India (centralindia)
├── Availability Zone 1
├── Availability Zone 2  
└── Availability Zone 3
```

**Availability Sets** group VMs to protect against hardware failures within a single data center using:
- **Fault Domains**: Hardware groups that share power/network
- **Update Domains**: Groups for planned maintenance

### 2.2 Azure Resource Manager (ARM)

ARM is the deployment and management service for Azure, providing a management layer for creating, updating, and deleting resources in your Azure subscription.

**ARM Benefits:**
- Declarative templates for infrastructure as code
- Role-based access control (RBAC)
- Tagging for resource organization
- Cost management and tracking

### 2.3 Resource Groups

A **Resource Group** is a logical container for Azure resources. It helps organize resources that share the same lifecycle, permissions, and management.

**Best Practices:**
- Group resources by environment (dev, staging, prod)
- Group by application or workload
- Consider resource location and access requirements

### 2.4 Azure Subscriptions and Management Groups

- **Subscription**: Logical container for billing and resource management
- **Management Groups**: Organize subscriptions hierarchically for governance

---

## 3. Azure Compute Services

### 3.1 Azure Virtual Machines (IaaS)

Azure Virtual Machines provide on-demand, scalable computing resources. You have control over the operating system, configuration, and installed software.

**VM Types by Workload:**

| Category | Series | Use Case |
|----------|--------|----------|
| General Purpose | B, D, DSv2 | Development, testing, small databases |
| Compute Optimized | F, Fs | Batch processing, web servers |
| Memory Optimized | Esv3, M | Large databases, in-memory caching |
| GPU | NC, ND | Deep learning, graphics rendering |
| High Performance | H | HPC, parallel computing |

**Example: Creating a VM using Azure CLI**
```bash
# Create a resource group
az group create --name myResourceGroup --location eastus

# Create a virtual machine
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --generate-ssh-keys

# Open port 80 for web server
az vm open-port --port 80 --resource-group myResourceGroup --name myVM
```

### 3.2 Azure App Service (PaaS)

Azure App Service is a fully managed platform for building, deploying, and scaling web apps. It supports multiple languages including .NET, .NET Core, Java, Node.js, Python, and PHP.

**App Service Plan Tiers:**
- **Free**: For testing/learning (1 GB RAM, 60 min/day)
- **Shared**: For development ($0.013/hour)
- **Basic**: For production (custom domain, manual scaling)
- **Standard**: For production apps (auto-scaling)
- **Premium**: For enterprise (VNet integration, enhanced performance)

**Key Features:**
- Auto-scaling
- Deployment slots (staging/production)
- Custom domains and SSL
- Continuous deployment from GitHub, Azure DevOps

### 3.3 Azure Container Instances (ACI)

ACI provides the fastest and simplest way to run containers in Azure without managing virtual machines.

```yaml
# azuredeploy.yaml for Container Instance
apiVersion: 2019-12-01
location: eastus
name: mycontainer
properties:
  containers:
  - name: mycontainer
    properties:
      image: mcr.microsoft.com/azuredocs/aci-helloworld:latest
      ports:
      - protocol: TCP
        port: 80
      resources:
        requests:
          cpu: 1.0
          memoryInGB: 1.5
  osType: Linux
  ipAddress:
    type: Public
    ports:
    - protocol: TCP
      port: '80'
type: Microsoft.ContainerInstance/containerGroups
```

### 3.4 Azure Kubernetes Service (AKS)

AKS is a managed Kubernetes service for deploying, managing, and scaling containerized applications.

**Key Concepts:**
- **Node**: Azure VM running Kubernetes
- **Pod**: Smallest deployable unit (one or more containers)
- **Service**: Stable IP address for pod access
- **Ingress**: HTTP/HTTPS routing to services

### 3.5 Azure Functions (Serverless)

Azure Functions is an event-driven serverless compute service that runs code in response to events without managing infrastructure.

**Pricing Model:**
- **Consumption Plan**: Pay only for execution time
- **Premium Plan**: Pre-warmed instances, VNet connectivity
- **App Service Plan**: Dedicated VMs for always-on apps

---

## 4. Azure Networking

### 4.1 Azure Virtual Network (VNet)

VNet enables Azure resources to communicate with each other, the internet, and on-premises networks.

**Components:**
- **Address Space**: CIDR block (e.g., 10.0.0.0/16)
- **Subnets**: Segments of VNet address space
- **Network Security Groups (NSG)**: Filter network traffic
- **Route Tables**: Define network traffic paths

### 4.2 Azure Load Balancer

Load Balancer distributes incoming traffic across healthy VMs using Layer 4 (TCP/UDP).

**Types:**
- **Public Load Balancer**: Internet-facing traffic
- **Internal Load Balancer**: Traffic within VNet

```json
{
  "frontendIPConfigurations": [
    {
      "name": "myFrontEnd",
      "properties": {
        "publicIPAddress": {
          "id": "/subscriptions/.../publicIPAddresses/myPublicIP"
        }
      }
    }
  ],
  "backendAddressPools": [
    {
      "name": "myBackEndPool"
    }
  ],
  "loadBalancingRules": [
    {
      "name": "myHTTPRule",
      "properties": {
        "frontendIPConfiguration": {"id": "..."},
        "backendAddressPool": {"id": "..."},
        "protocol": "Tcp",
        "frontendPort": 80,
        "backendPort": 80
      }
    }
  ]
}
```

### 4.3 Azure VPN Gateway

VPN Gateway connects on-premises networks to Azure through Site-to-Site or Point-to-Site VPNs.

**Types:**
- **Policy-based**: Static routing, one connection per gateway
- **Route-based**: Dynamic routing, supports multiple tunnels

### 4.4 Azure Content Delivery Network (CDN)

Azure CDN caches static content at edge locations worldwide for fast delivery.

**Features:**
- Global edge network
- Dynamic site acceleration
- Custom domain support
- HTTPS support

### 4.5 Azure Application Gateway

Application Gateway is a Layer 7 load balancer with web application firewall (WAF) capabilities.

---

## 5. Azure Storage Services

### 5.1 Azure Storage Account

A storage account provides a unique namespace in Azure for all storage data objects.

**Storage Account Types:**
- **Standard**: General-purpose v2 (HDD)
- **Premium**: Block blobs, page blobs, files (SSD)

**Redundancy Options:**
- LRS (Locally Redundant Storage) - 3 copies in one facility
- ZRS (Zone Redundant Storage) - 3 copies across availability zones
- GRS (Geo-Redundant Storage) - 3 copies locally + 3 in secondary region
- GZRS (Geo-Zone Redundant Storage) - ZRS locally + GRS secondary

### 5.2 Azure Blob Storage

Blob storage stores unstructured data (text, binary, audio, video).

**Blob Types:**
- **Block Blobs**: Text, media files (up to 4.75 TB)
- **Page Blobs**: Random access files, VHDs (up to 8 TB)
- **Append Blobs**: Log files, streaming data

**Access Tiers:**
- **Hot**: Frequently accessed data
- **Cool**: Infrequently accessed (>30 days)
- **Archive**: Rarely accessed (>180 days)

**Example: Upload blob using Python SDK**
```python
from azure.storage.blob import BlobServiceClient, BlobClient

# Connection string from Azure Portal
connection_string = "DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=mykey;EndpointSuffix=core.windows.net"

# Create blob service client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get container client
container_client = blob_service_client.get_container_client("mycontainer")

# Upload a file
with open("example.txt", "rb") as data:
    container_client.upload_blob(name="example.txt", data=data)

print("File uploaded successfully!")
```

### 5.3 Azure Files

Azure Files provides fully managed file shares in the cloud accessible via SMB protocol.

**Use Cases:**
- Lift-and-shift applications
- Configuration files
- Log files
- Development/debugging tools

### 5.4 Azure Queue Storage

Queue storage provides messaging between application components.

**Components:**
- **Queue**: Container of messages
- **Message**: Up to 64 KB text string

### 5.5 Azure Disk Storage

Managed disks provide high-performance block storage for Azure VMs.

**Disk Types:**
- **Standard HDD**: Low-cost, development/test
- **Standard SSD**: Production workloads
- **Premium SSD**: Mission-critical, high IOPS
- **Ultra Disk**: Highest performance, large workloads

---

## 6. Azure Database Services

### 6.1 Azure SQL Database

Fully managed relational database as a service (DBaaS) built on SQL Server.

**Deployment Options:**
- **Single Database**: Isolated database
- **Elastic Pool**: Shared resources across databases
- **Managed Instance**: Near-full SQL Server compatibility

**Scaling Options:**
- DTU-based purchasing (Basic, Standard, Premium)
- vCore-based purchasing (General Purpose, Business Critical)

**Example: Connect to Azure SQL using Python**
```python
import pyodbc

server = 'myserver.database.windows.net'
database = 'mydatabase'
username = 'myusername'
password = 'mypassword'

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    # Execute query
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print(f"SQL Server version: {row[0]}")
    
    conn.close()
except Exception as e:
    print(f"Error: {e}")
```

### 6.2 Azure Cosmos DB

Globally distributed, multi-model database service with single-digit millisecond latency.

**Data Models:**
- SQL API (document)
- MongoDB API
- Cassandra API
- Gremlin API (graph)
- Table API (key-value)

**Consistency Levels:**
- Strong
- Bounded staleness
- Session
- Consistent prefix
- Eventual

### 6.3 Azure Redis Cache

In-memory data store for fast data access.

**Use Cases:**
- Session caching
- Application caching
- Message broker
- Real-time analytics

### 6.4 Azure Database for MySQL/PostgreSQL

Fully managed MySQL and PostgreSQL databases.

**Features:**
- Automatic backups
- Automatic patching
- High availability
- Scalability

---

## 7. Azure Security and Identity Management

### 7.1 Azure Active Directory (Azure AD)

Azure AD is Microsoft's cloud-based identity and access management service.

**Editions:**
- Free
- Office 365 Apps
- Premium P1
- Premium P2

**Key Concepts:**
- **Tenants**: Single Azure AD organization
- **Users**: Individual identities
- **Groups**: Collection of users
- **Applications**: SaaS apps using SSO

### 7.2 Role-Based Access Control (RBAC)

RBAC provides fine-grained access management to Azure resources.

**Built-in Roles:**
- **Owner**: Full access, can delegate
- **Contributor**: Manage resources, no access
- **Reader**: View resources only
- **User Access Administrator**: Manage user access

```json
{
  "roleDefinitionId": "/subscriptions/.../providers/Microsoft.Authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c",
  "principalId": "user-object-id",
  "principalType": "User",
  "scope": "/subscriptions/.../resourceGroups/myResourceGroup"
}
```

### 7.3 Azure Security Center

Unified security management and threat protection.

**Features:**
- Continuous security assessment
- Security recommendations
- Threat protection
- Just-in-time VM access

### 7.4 Azure Key Vault

Centralized secrets, keys, and certificate management.

**Use Cases:**
- Store connection strings
- Store API keys
- Manage SSL/TLS certificates
- Encrypt data with keys

### 7.5 Azure Firewall

Managed, cloud-based network security service.

**Features:**
- Built-in high availability
- Threat-based filtering
- Outbound SNAT
- Application FQDN tags

---

## 8. Azure Serverless Computing

### 8.1 Azure Functions

Event-driven serverless compute that executes code in response to events.

**Supported Triggers:**
- HTTP Trigger (Web API)
- Timer Trigger (Scheduled jobs)
- Blob Trigger (File processing)
- Queue Trigger (Message processing)
- Cosmos DB Trigger (Database changes)

**Example: Azure Function with HTTP Trigger**
```python
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
        return func.HttpResponse(f"Hello, {name}!")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string",
            status_code=400
        )
```

### 8.2 Azure Logic Apps

Visual workflow automation service for building enterprise integration solutions.

**Key Components:**
- **Triggers**: Start workflows
- **Actions**: Steps in workflow
- **Connectors**: Integration with services
- **Conditions**: Branch logic

---

## 9. Azure DevOps Services

### 9.1 Azure Pipelines

Continuous integration and continuous delivery (CI/CD) platform.

**Components:**
- **Pipelines**: Define build and release process
- **Agents**: Run build/deployment jobs
- **Stages**: Deployment phases
- **Jobs**: Collection of tasks

**Example: Azure Pipeline YAML**
```yaml
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

stages:
  - stage: Build
    jobs:
      - job: BuildJob
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '3.8'
          
          - script: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt
            displayName: 'Install dependencies'
          
          - script: |
              python -m pytest tests/
            displayName: 'Run tests'
          
          - task: PublishTestResults@2
            inputs:
              testResultsFiles: '**/test-results.xml'
              testRunTitle: 'Python Tests'

  - stage: Deploy
    jobs:
      - deployment: DeployWebApp
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'AzureServiceConnection'
                    appName: 'mywebapp'
                    package: '$(Pipeline.Workspace)/drop/**/*.zip'
```

### 9.2 Azure Repos

Git repositories for source code management.

**Features:**
- Unlimited private repos
- Branch policies
- Pull requests
- Code review

### 9.3 Azure Boards

Work item tracking and Agile project management.

**Work Item Types:**
- Epic
- Feature
- User Story
- Bug
- Task

### 9.4 Azure Artifacts

Package management for Maven, npm, NuGet, and Python packages.

---

## 10. Azure AI and Machine Learning Services

### 10.1 Azure Cognitive Services

Pre-built AI APIs for vision, speech, language, and decision making.

**Service Categories:**
- **Vision**: Computer Vision, Face API, Form Recognizer
- **Speech**: Speech to Text, Text to Speech, Translator
- **Language**: Text Analytics, LUIS, QnA Maker
- **Decision**: Anomaly Detector, Content Moderator

### 10.2 Azure Machine Learning

End-to-end ML platform for building, training, and deploying models.

**Features:**
- Automated ML
- Designer (drag-and-drop)
- Python SDK
- Model management
- MLOps integration

**Example: Create and train a model**
```python
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# Connect to workspace
ml_client = MLClient(
    subscription_id="your-subscription-id",
    resource_group_name="your-resource-group",
    workspace_name="your-workspace"
)

# Create a compute cluster
from azure.ai.ml.entities import AmlCompute
compute = AmlCompute(
    name="cpu-cluster",
    type="amlcompute",
    size="Standard_DS3_v2",
    min_instances=0,
    max_instances=4
)
ml_client.compute.begin_create_or_update(compute)

# Define training job
from azure.ai.ml import command
job = command(
    code="./src",
    command="python train.py --data ${{inputs.data}}",
    inputs={
        "data": Input(type=AssetTypes.URI_FOLDER, path="azureml://datastores/workspaceblobstore/paths/data")
    },
    environment="AzureML-sklearn-1.0-gnu@latest",
    compute="cpu-cluster"
)

# Submit job
returned_job = ml_client.jobs.create_or_update(job)
```

### 10.3 Azure Bot Service

Build, test, and deploy intelligent bots.

**Features:**
- Virtual Assistant template
- Integration with channels (Teams, Slack, etc.)
- QnA Maker integration
- Language Understanding (LUIS)

---

## 11. Practical Examples with Code

### Example 1: Deploying a Web App to Azure App Service

**Step 1: Create the App Service Plan**
```bash
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku FREE
```

**Step 2: Create the Web App**
```bash
az webapp create --name mywebapp123 --resource-group myResourceGroup --plan myAppServicePlan
```

**Step 3: Configure Deployment from GitHub**
```bash
az webapp deployment source config-local-git --name mywebapp123 --resource-group myResourceGroup
```

**Step 4: Add deployment credentials**
```bash
az webapp deployment user set --user-name myusername --password mypassword
```

**Step 5: Push code from local Git**
```bash
git remote add azure <deployment-local-git-url>
git push azure master
```

### Example 2: Serverless Image Processing with Azure Functions and Blob Storage

**function.json**
```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "myblob",
      "type": "blobTrigger",
      "direction": "in",
      "path": "images/{name}",
      "connection": "AzureWebJobsStorage"
    },
    {
      "name": "outputBlob",
      "type": "blob",
      "direction": "out",
      "path": "processed/{name}",
      "connection": "AzureWebJobsStorage"
    }
  ]
}
```

**__init__.py**
```python
import logging
from azure.functions import BlobStreamIOBinaryReader

def main(myblob: func.InputStream, outputBlob: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # Read the input blob
    input_data = myblob.read()
    
    # Process the image (example: convert to grayscale)
    # In production, use PIL or OpenCV
    processed_data = input_data  # Placeholder
    
    # Write to output blob
    outputBlob.set(processed_data)
```

---

## 12. Multiple Choice Questions

### Easy Level

1. **Which Azure service provides virtual machines in the cloud?**
   - A) Azure App Service
   - B) Azure Virtual Machines
   - C) Azure Functions
   - D) Azure Container Instances
   - **Answer: B**

2. **What is the minimum unit of billing in Azure Functions??**
   - A) Hour
   - B) Minute
   - C) Second
   - D) Millisecond
   - **Answer: C**

3. **Which storage service is best for storing unstructured data like images and videos?**
   - A) Azure Files
   - B) Azure Queue Storage
   - C) Azure Blob Storage
   - D) Azure Table Storage
   - **Answer: C**

4. **What does PaaS stand for in cloud computing?**
   - A) Platform as a Service
   - B) Platform and as a Service
   - C) Private as a Service
   - D) Processing as a Service
   - **Answer: A**

5. **Which Azure service provides a globally distributed database?**
   - A) Azure SQL Database
   - B) Azure Cosmos DB
   - C) Azure Redis Cache
   - D) Azure Database for MySQL
   - **Answer: B**

### Medium Level

6. **What is the purpose of Azure Load Balancer?**
   - A) Encrypt network traffic
   - B) Distribute traffic across multiple VMs
   - C) Cache static content
   - D) Manage SSL certificates
   - **Answer: B**

7. **Which Azure AD feature enables Single Sign-On (SSO)?**
   - A) Conditional Access
   - B) Application Proxy
   - C) Enterprise Applications
   - D) Multi-Factor Authentication
   - **Answer: C**

8. **What type of redundancy does ZRS provide?**
   - A) Single data center redundancy
   - B) Availability zone redundancy
   - C) Geographic redundancy
   - D) No redundancy
   - **Answer: B**

9. **Which service is used for container orchestration in Azure?**
   - A) Azure Container Instances
   - B) Azure Kubernetes Service
   - C) Azure Service Fabric
   - D) Azure Batch
   - **Answer: B**

10. **What is the maximum message size in Azure Queue Storage?**
    - A) 16 KB
    - B) 32 KB
    - C) 64 KB
    - D) 128 KB
    - **Answer: C**

11. **Which Azure service provides serverless workflow automation?**
    - A) Azure Functions
    - B) Azure Logic Apps
    - C) Azure Event Grid
    - D) Azure Service Bus
    - **Answer: B**

12. **What is the purpose of Azure CDN?**
    - A) Store databases
    - B) Cache content globally
    - C) Manage DNS
    - D) Deploy web apps
    - **Answer: B**

### Hard Level

13. **Which consistency model in Azure Cosmos DB provides the strongest guarantee?**
    - A) Eventual
    - B) Session
    - C) Consistent Prefix
    - D) Strong
    - **Answer: D**

14. **What Azure RBAC role has full access to manage resources but cannot grant access?**
    - A) Owner
    - B) Contributor
    - C) Reader
    - D) User Access Administrator
    - **Answer: B**

15. **Which trigger type is NOT supported by Azure Functions?**
    - A) HTTP Trigger
    - B) Timer Trigger
    - C) SMTP Trigger
    - D) Queue Trigger
    - **Answer: C**

16. **What is the purpose of Azure Virtual Network?**
    - A) Provide CDN services
    - B) Enable DNS resolution
    - C) Create isolated network environment
    - D) Manage SSL certificates
    - **Answer: C**

17. **Which Azure service is used for secrets management?**
    - A) Azure Key Vault
    - B) Azure Security Center
    - C) Azure Sentinel
    - D) Azure Firewall
    - **Answer: A**

18. **In Azure DevOps, which service is used for CI/CD pipelines?**
    - A) Azure Repos
    - B) Azure Boards
    - C) Azure Pipelines
    - D) Azure Artifacts
    - **Answer: C**

19. **What is the purpose of Availability Zones in Azure?**
    - A) Backup data
    - B) Provide high availability within a region
    - C) Connect to on-premises networks
    - D) Cache content
    - **Answer: B**

20. **Which Azure ML component provides drag-and-drop model building?**
    - A) Automated ML
    - B) Designer
    - C) Python SDK
    - D) CLI
    - **Answer: B**

---

## 13. Flashcards

| # | Term | Definition |
|---|------|------------|
| 1 | Azure Region | Geographic location containing Azure data centers |
| 2 | Virtual Machine | IaaS offering for on-demand compute resources |
| 3 | Azure Blob Storage | Object storage for unstructured data |
| 4 | Azure AD | Microsoft's cloud-based identity and access management |
| 5 | RBAC | Role-Based Access Control for resource authorization |
| 6 | Azure Functions | Serverless compute service for event-driven code |
| 7 | VNet | Virtual Network for private Azure resource communication |
| 8 | Azure SQL Database | Managed relational database as a service |
| 9 | Cosmos DB | Globally distributed multi-model database service |
| 10 | Load Balancer | Distributes traffic across multiple servers |
| 11 | App Service | PaaS for building and hosting web applications |
| 12 | AKS | Azure Kubernetes Service for container orchestration |
| 13 | Azure CDN | Content Delivery Network for global caching |
| 14 | Azure Key Vault | Service for secrets, keys, and certificate management |
| 15 | Azure DevOps | Set of development tools for CI/CD and project management |
| 16 | Logic Apps | Serverless workflow automation service |
| 17 | Azure Cognitive Services | Pre-built AI APIs for vision, speech, language |
| 18 | Azure ML | Platform for building and deploying ML models |
| 19 | Resource Group | Logical container for Azure resources |
| 20 | Availability Set | Grouping of VMs for redundancy against failures |

---

## 14. Key Takeaways

### Core Concepts
- **Azure** is Microsoft's comprehensive cloud platform offering IaaS, PaaS, and SaaS services
- Understanding regions, availability zones, and resource groups is fundamental to Azure architecture

### Compute Services
- **Virtual Machines** provide full control but require manual management (IaaS)
- **App Service** is the go-to for web applications without infrastructure management (PaaS)
- **Azure Functions** enables serverless computing with event-driven architecture

### Storage Services
- **Blob Storage** is ideal for unstructured data (images, videos, backups)
- **Azure Files** provides SMB file shares for cloud file systems
- **Queue Storage** enables reliable messaging between application components

### Database Services
- **Azure SQL Database** for traditional relational database needs
- **Cosmos DB** for globally distributed, low-latency applications
- **Redis Cache** for high-performance in-memory caching

### Networking
- **VNet** creates isolated network environments
- **Load Balancer** distributes traffic for high availability
- **VPN Gateway** connects on-premises networks to Azure

### Security
- **Azure AD** provides identity and access management
- **RBAC** enables fine-grained permission management
- **Key Vault** secures sensitive information

### DevOps & AI
- **Azure DevOps** provides comprehensive CI/CD tooling
- **Azure Functions** and **Logic Apps** enable serverless architectures
- **Cognitive Services** and **Azure ML** bring AI capabilities to applications

---

## 15. References and Syllabus Context

### Delhi University NEP 2024 UGCF Syllabus Alignment

This study material covers the following topics as per the Delhi University BSc (Hons) Computer Science syllabus under Cloud Computing:

| Unit | Topic | Coverage in this Material |
|------|-------|--------------------------|
| Unit 1 | Introduction to Cloud Computing | ✓ Complete |
| Unit 2 | Microsoft Azure Overview | ✓ Complete |
| Unit 3 | Azure Compute Services | ✓ Complete |
| Unit 4 | Azure Storage Services | ✓ Complete |
| Unit 5 | Azure Networking | ✓ Complete |
| Unit 6 | Azure Database Services | ✓ Complete |
| Unit 7 | Azure Security & Identity | ✓ Complete |
| Unit 8 | Azure DevOps | ✓ Complete |
| Unit 9 | Serverless Computing | ✓ Complete |
| Unit 10 | Azure AI/ML Services | ✓ Complete |

### Recommended References

1. **Microsoft Learn**: Official Azure tutorials and documentation
2. **Azure Portal**: hands-on experience with Azure services
3. **Microsoft Certified: Azure Fundamentals**: Entry-level certification
4. **"Microsoft Azure: The Complete Guide"** - Various publishers
5. **Azure Documentation**: docs.microsoft.com/azure

### Hands-On Practice

Students are encouraged to:
- Create a free Azure account (₹15,000 credit for new users)
- Complete Microsoft Learn modules for Azure
- Practice with Azure CLI and Azure Portal
- Build sample projects integrating multiple Azure services

---

**Document Prepared for**: BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)
**Subject**: Cloud Computing
**Topic**: Microsoft Azure
**Word Count**: ~3,500 words