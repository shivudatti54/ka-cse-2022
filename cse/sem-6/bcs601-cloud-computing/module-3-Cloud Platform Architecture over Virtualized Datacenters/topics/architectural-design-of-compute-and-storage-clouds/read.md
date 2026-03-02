# Module 3: Architectural Design of Compute and Storage Clouds

## 1. Introduction

Cloud computing's robust and scalable architecture serves as the fundamental backbone enabling modern distributed systems. Unlike traditional monolithic architectures characterized by tight coupling and static resource allocation, cloud architecture employs a collection of loosely coupled, independently scalable services that can be dynamically provisioned, configured, and managed according to workload demands. This modular approach to system design facilitates elasticity, fault tolerance, and multi-tenancy—core principles distinguishing cloud platforms from conventional data center deployments.

This module examines the core architectural components constituting modern cloud platforms, with particular emphasis on the fundamental separation and independent design of **Compute** and **Storage** resources. Understanding this architectural separation is essential for cloud architects and engineers tasked with designing systems that meet specific performance, durability, and scalability requirements.

## 2. Core Architectural Concepts

Cloud architecture adheres to a layered service model that abstracts underlying complexity while providing well-defined interfaces for resource consumption. The design principles underlying this architecture—resource pooling, elasticity, on-demand self-service, and measured service—ensure that infrastructure components can be efficiently utilized across multiple tenants while maintaining Quality of Service (QoS) guarantees.

### 2.1 The High-Level Layered Architecture

A generalized cloud architecture comprises four distinct layers, each providing specific abstractions and services to the layer above:

**Definition 2.1 (Cloud Service Model):** A cloud service model defines the level of abstraction and management responsibility transferred from the cloud provider to the consumer. Formally, let **S** represent the set of managed resources, **C** the consumer's management responsibilities, and **P** the provider's management responsibilities. For a service model **M**, we have **C(M) ∪ P(M) = S** where **C(M) ∩ P(M) = ∅**.

1. **Hardware (Datacenter) Layer:** The physical foundation encompassing servers, network switches, routers, power distribution units, and cooling systems housed in geographically distributed, secure datacenters. This layer implements physical redundancy (dual-powered servers, RAID storage, redundant network paths) and is fully abstracted from end-users. The provider maintains complete operational control over this layer.

2. **Infrastructure Layer (IaaS - Infrastructure as a Service):** This layer introduces virtualization technology, enabling the logical partitioning of physical resources. A **hypervisor** (e.g., VMware ESXi, Xen, KVM) executes on physical hardware to create and manage multiple Virtual Machines (VMs), each operating as an independent guest system. The aggregated pool of virtualized compute (CPU, RAM), storage, and networking resources constitutes the IaaS offering (e.g., Amazon EC2, Azure Virtual Machines, GCP Compute Engine). Consumers retain responsibility for operating system installation, middleware configuration, and application deployment.

3. **Platform Layer (PaaS - Platform as a Service):** This layer provides a managed execution environment for application development and deployment. It abstracts infrastructure complexity by offering pre-configured middleware, runtime environments, databases, and development tools. Consumers develop applications using provided APIs without managing underlying OS or hardware. Examples include AWS Elastic Beanstalk, Google App Engine, and Azure App Service.

4. **Application Layer (SaaS - Software as a Service):** The consumer-facing layer delivering complete applications over the network. Users access functionality through web browsers or thin clients without visibility into or control over the underlying infrastructure, platform, or application stack. Examples include Gmail, Salesforce, Microsoft 365, and Google Workspace.

### 2.2 Architectural Design of Compute Clouds

The compute cloud architecture is specifically designed for processing workloads. Its primary architectural objectives are providing scalable computing power, maintaining sub-second VM provisioning times, and ensuring efficient resource utilization through intelligent scheduling.

**Definition 2.2 (Compute Cloud):** A compute cloud is a distributed system that provides on-demand provisioning of virtualized computational resources (CPU, RAM) to consumers via network access. Formally, a compute cloud **CC** can be defined as a tuple **CC = (H, V, O, S)** where **H** represents the physical host pool, **V** the virtual machine instances, **O** the cloud orchestrator, and **S** the scheduling algorithm mapping **V → H**.

#### 2.2.1 Core Components and Resource Pooling

The **Virtual Machine (VM)** constitutes the fundamental computational unit in cloud infrastructure. A hypervisor operating on physical servers (hosts) creates and manages these VMs (guests). Resource pooling aggregates compute resources (CPU cycles, memory) from multiple physical hosts into a unified logical pool. When a consumer requests VM provisioning, the cloud management software (orchestrator) allocates resources from this pool according to specified constraints (instance type, availability zone, placement groups).

**Theorem 2.1 (Resource Utilization Bound):** For a compute cloud with **N** homogeneous hosts, each providing capacity **C** compute units, and a VM demand **D** compute units, the maximum utilization **U_max** achievable without violating SLA guarantees is bounded by:

**U_max ≤ (N × C) / D**

_Proof:_ The scheduling algorithm must allocate at most **C** compute units per host. To guarantee SLA compliance, total demand **D** must not exceed total capacity **N × C**. Therefore, utilization cannot exceed this ratio without risk of resource contention. ∎

#### 2.2.2 Elasticity and Auto-Scaling

Elasticity represents a defining characteristic of cloud compute architecture, enabling dynamic adjustment of resource capacity in response to workload variations. Cloud platforms implement elasticity through **auto-scaling groups** that automatically launch or terminate VM instances based on defined scaling policies.

**Definition 2.3 (Elasticity):** Elasticity is the degree to which a system automatically adjusts its resource allocation to match changing demand. Formally, elasticity **E** can be measured as:

**E = (ΔR / R) / (ΔD / D)**

where **R** represents allocated resources, **D** represents demand, and **Δ** denotes the change over time. Perfect elasticity yields **E = 1**.

Elastic scaling operates in two modes:

- **Scale-Out (Horizontal Expansion):** Adding VM instances to increase capacity when demand exceeds threshold (e.g., CPU utilization > 70%)
- **Scale-In (Horizontal Contraction):** Removing VM instances to reduce capacity when demand falls below threshold (e.g., CPU utilization < 30%)

This approach follows a **reactive elasticity model** triggered by observed metrics. Advanced implementations employ **predictive elasticity** using time-series analysis and machine learning to forecast demand spikes.

```python
# Example: AWS Auto Scaling policy configuration
import boto3

autoscaling = boto3.client('autoscaling')

# Define scaling policy
response = autoscaling.put_scaling_policy(
 AutoScalingGroupName='web-server-group',
 PolicyName='scale-out-policy',
 AdjustmentType='PercentChangeInCapacity',
 ScalingAdjustment=50, # Increase capacity by 50%
 Cooldown=300 # Wait 5 minutes before next scaling action
)

# Define CloudWatch metric alarm for trigger
cloudwatch = boto3.client('cloudwatch')
cloudwatch.put_metric_alarm(
 AlarmName='high-cpu-alarm',
 MetricName='CPUUtilization',
 Namespace='AWS/EC2',
 Statistic='Average',
 Period=300,
 EvaluationPeriods=2,
 Threshold=70,
 ComparisonOperator='GreaterThanThreshold',
 Dimensions=[{'Name': 'AutoScalingGroupName', 'Value': 'web-server-group'}],
 AlarmActions=[response['PolicyARN']]
)
```

### 2.3 Architectural Design of Storage Clouds

The storage cloud architecture addresses data persistence requirements with emphasis on durability, availability, and scalability. Unlike compute resources that are ephemeral, storage resources must maintain data integrity across hardware failures, software updates, and potential site disasters.

**Definition 2.4 (Storage Cloud):** A storage cloud is a distributed system providing persistent data storage with characteristics including durability, availability, and scalability. It can be formally represented as **SC = (D, R, C, P)** where **D** represents the data storage backend, **R** the replication strategy, **C** the consistency model, and **P** the data placement algorithm.

#### 2.3.1 Storage Service Models

Cloud providers offer multiple storage service models, each optimized for specific access patterns and use cases:

**Object Storage:** Stores data as objects within a flat namespace (buckets/containers). Each object comprises the data file, metadata, and a unique identifier. This architecture eliminates the hierarchical directory structure of traditional file systems, enabling massive scalability. Object storage employs **RESTful APIs** for access and achieves high durability through distributed replication.

_Example Services:_ Amazon S3, Azure Blob Storage, Google Cloud Storage

_Durability Model:_ Object storage typically guarantees **eleven 9s** (99.999999999%) annual durability by replicating data across multiple geographically separated availability zones. For data volume **V**, the probability of data loss **P_loss** over time **T** is:

**P_loss(T) ≤ (1 - 0.99999999999)^T**

**Block Storage:** Provides raw storage volumes presented as virtualized disks to compute instances. The guest operating system formats the volume with a filesystem (NTFS, ext4, XFS). Block storage prioritizes low latency and high IOPS (Input/Output Operations Per Second), making it suitable for database systems, enterprise applications, and boot volumes.

_Example Services:_ Amazon EBS, Azure Disk Storage, Google Persistent Disk

**File Storage:** Offers managed network file systems accessible to multiple compute instances simultaneously using standard protocols (NFSv4, SMB/CIFS). This architecture supports shared read-write access to common file repositories, enabling lift-and-shift migration of legacy applications.

_Example Services:_ Amazon EFS, Azure Files, Google Cloud Filestore

#### 2.3.2 Data Replication and Durability Strategies

Storage cloud architects must address data durability through replication and redundancy mechanisms. Two primary strategies are employed:

**Synchronous Replication:** Data is written to multiple storage locations before acknowledging write completion. This approach ensures strong consistency but introduces latency proportional to the number of replicas. For **n** replicas, write latency **L_write** is:

**L_write = max(L_1, L_2, ..., L_n)**

where **L_i** represents latency to replica **i**.

**Asynchronous Replication:** Write acknowledgment occurs after persisting to primary storage, with replication to secondary locations occurring subsequently. This approach minimizes write latency but introduces a **replication lag** window during which data loss is possible if primary storage fails.

**Erasure Coding:** Advanced storage systems employ erasure coding (similar to RAID) to achieve durability while reducing storage overhead compared to full replication. Data is split into **k** data chunks and **m** parity chunks, allowing reconstruction from any **k** chunks out of **k+m** total. The durability model for erasure coding with **n** total chunks and **m** parity chunks provides **n-m** fault tolerance:

**Storage Overhead = (k + m) / k**
**Durability = 1 - Σ(i=0 to n-m) C(n, i) × p^i × (1-p)^(n-i)**

where **p** represents the per-chunk failure probability.

#### 2.3.3 Consistency Models

Storage cloud architectures must balance consistency guarantees with availability, fundamentally addressing the **CAP Theorem** trade-off:

**Theorem 2.2 (CAP Theorem):** A distributed storage system can guarantee only two of three properties simultaneously: **Consistency** (all nodes see the same data simultaneously), **Availability** (every request receives a response), and **Partition tolerance** (system continues operation despite network failures). Formally:

**CAP(C, A, P) = True ⇒ Only 2 of {C, A, P} can be simultaneously guaranteed**

Cloud storage systems typically implement one of two consistency models:

1. **Strong Consistency:** All replicas must agree on the latest write before any read returns a value. This model is essential for transactional systems but introduces latency. Achieved through consensus protocols like Paxos or Raft.

2. **Eventual Consistency:** Reads may return stale data temporarily, but all replicas will eventually converge to the same value given no further writes. This model optimizes for availability and partition tolerance, suitable for web applications, caching, and analytics workloads. The convergence time **T_conv** follows:

**T_conv ≤ T_network × log(n)**

where **n** is the number of replicas.

## 3. Key Points & Summary

| Aspect                | Compute Cloud                            | Storage Cloud                                          |
| :-------------------- | :--------------------------------------- | :----------------------------------------------------- |
| **Primary Goal**      | Processing Power & Execution             | Data Persistence & Durability                          |
| **Core Unit**         | Virtual Machine (VM)                     | Object, Block, or File                                 |
| **Key Design Focus**  | Elasticity, Scalability (Scaling In/Out) | Durability (Replication, Erasure Coding), Availability |
| **Abstraction Level** | Virtualized Hardware (CPU, RAM)          | Virtualized Disk/Storage Volume                        |
| **Consistency Model** | N/A (Stateless Computation)              | Strong or Eventual                                     |
| **Example Services**  | AWS EC2, Azure VMs, GCP Compute Engine   | AWS S3 (Object), EBS (Block); Azure Blob, Disk         |

**Summary:** The architectural design of clouds separates compute and storage into independently scalable subsystems, enabling optimized resource allocation based on workload characteristics. Compute clouds implement virtualization for resource pooling and elasticity through auto-scaling mechanisms. Storage clouds employ distributed replication strategies and configurable consistency models to achieve durability and availability guarantees. Understanding the trade-offs between consistency, availability, and partition tolerance (CAP theorem) is essential for designing cloud-native applications that leverage these architectural patterns effectively.

## 4. Assessment Questions

### Question 1 (Hard - Numerical)

A cloud provider operates a compute cluster with 1000 homogeneous servers, each providing 100 vCPUs. The auto-scaling policy triggers when CPU utilization exceeds 80%. Currently, 750 servers are active with average utilization of 75%. If a new application deployment requires 5000 additional vCPUs and the scaling policy adds capacity in increments of 100 servers, how many additional servers will be launched before the policy reaches equilibrium? Show your reasoning.

### Question 2 (Hard - Application)

A financial trading application requires strong consistency for transaction records but experiences peak write loads of 10,000 transactions per second. Design a storage architecture that addresses the CAP theorem trade-offs. Justify your choice of storage service type, consistency model, and replication strategy, including estimated write latency implications.

### Question 3 (Hard - Analysis)

Compare synchronous vs. asynchronous replication in cloud storage systems. Given a storage system with 3 replicas where the network latency between data centers is 10ms, calculate the write completion time for each replication strategy. Under what circumstances would you choose eventual consistency over strong consistency? Justify your answer with reference to the CAP theorem.
