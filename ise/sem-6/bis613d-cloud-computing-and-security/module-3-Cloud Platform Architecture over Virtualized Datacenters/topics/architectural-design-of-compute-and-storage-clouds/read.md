# Module 3: Architectural Design of Compute and Storage Clouds


## Table of Contents

- [Module 3: Architectural Design of Compute and Storage Clouds](#module-3-architectural-design-of-compute-and-storage-clouds)
- [1. Introduction](#1-introduction)
- [2. Core Architectural Concepts](#2-core-architectural-concepts)
  - [The High-Level Layered Architecture](#the-high-level-layered-architecture)
  - [Architectural Design of Compute Clouds](#architectural-design-of-compute-clouds)
- [Example of scaling out with AWS EC2](#example-of-scaling-out-with-aws-ec2)
- [Launch additional instances](#launch-additional-instances)
  - [Architectural Design of Storage Clouds](#architectural-design-of-storage-clouds)
- [Example of uploading a file to AWS S3](#example-of-uploading-a-file-to-aws-s3)
- [Upload a file](#upload-a-file)
- [3. Key Points & Summary](#3-key-points--summary)
- [4. Exam Tips and Key Takeaways](#4-exam-tips-and-key-takeaways)

## 1. Introduction

Cloud computing's robust and scalable architecture is the backbone of its power. Unlike traditional monolithic systems, cloud architecture is designed as a collection of loosely coupled services that can be dynamically provisioned and managed. This module delves into the core architectural components that form the backbone of modern cloud platforms, primarily focusing on the separation and design of **Compute** and **Storage** resources.

## 2. Core Architectural Concepts

Cloud architecture is typically structured in layers, often visualized as a stack. The design principles ensure resources are pooled, scalable, and available over the network.

### The High-Level Layered Architecture

A generalized cloud architecture consists of four key layers:

1. **Hardware (Datacenter) Layer:** This is the physical foundation. It includes servers, routers, switches, power supplies, and cooling systems housed in massive, secure datacenters. This layer is fully abstracted away from the end-user.
2. **Infrastructure Layer (IaaS - Infrastructure as a Service):** This is where virtualization technology shines. A hypervisor (e.g., VMware, Xen, KVM) runs on the physical hardware to create and manage multiple Virtual Machines (VMs). This pool of abstracted compute, storage, and networking resources is what is delivered as a service (e.g., AWS EC2, Azure Virtual Machines).
3. **Platform Layer (PaaS - Platform as a Service):** This layer provides a development and deployment environment atop the infrastructure. It includes middleware, databases, development tools, and APIs (e.g., AWS Elastic Beanstalk, Google App Engine). Developers can build applications without managing the underlying OS or hardware.
4. **Application Layer (SaaS - Software as a Service):** This is the top layer, consisting of end-user applications accessible via a web browser or client interface (e.g., Gmail, Salesforce, Microsoft 365). The user is completely unaware of the underlying infrastructure.

### Architectural Design of Compute Clouds

The compute cloud is designed for processing. Its primary goal is to provide scalable and elastic computing power.

- **Core Component:** The **Virtual Machine (VM)** is the fundamental unit. A hypervisor on a physical server (often called a **host**) creates and runs these VMs (called **guests**).
- **Resource Pooling:** Compute resources (CPU, RAM) from numerous hosts are aggregated into a large pool. When a user requests a VM, the cloud management software (orchestrator) draws resources from this pool, deploys the VM, and manages its lifecycle.
- **Elasticity:** This is a key design feature. The architecture allows for automatic scaling. For example, an application experiencing high traffic can trigger rules to automatically launch additional VM instances to handle the load (`scale-out`). When demand decreases, instances can be terminated (`scale-in`) to save cost.

```python
# Example of scaling out with AWS EC2
import boto3

ec2 = boto3.client('ec2')

# Launch additional instances
response = ec2.run_instances(
    ImageId='ami-0c94855ba95c71c99',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=10
)

print(response)
```

- **Example:** Imagine an e-commerce website during a festival sale. The cloud architecture automatically spins up ten new web server VMs to handle the influx of users. After the sale, it scales back down to two VMs.

### Architectural Design of Storage Clouds

The storage cloud is designed for data persistence. Its architecture prioritizes durability, availability, and scalability over raw processing speed.

- **Core Components:** Cloud storage is not a single technology but a suite of services, each with a different architectural design:
  - **Object Storage:** (e.g., AWS S3, Azure Blob Storage) Data is stored as objects (file + metadata + unique ID) in a flat, non-hierarchical namespace (buckets/containers). It's highly scalable and durable, ideal for unstructured data like images, videos, and backups.
  - **Block Storage:** (e.g., AWS EBS, Azure Disk Storage) Provides raw storage volumes that can be attached to VMs, akin to a physical hard drive. The VM's OS can format it with a filesystem (NTFS, ext4). It's used for databases or applications needing low-latency storage.
  - **File Storage:** (e.g., AWS EFS, Azure Files) Provides shared file systems accessible by multiple VMs using standard protocols like NFS or SMB. It's ideal for shared content repositories.

```python
# Example of uploading a file to AWS S3
import boto3

s3 = boto3.client('s3')

# Upload a file
response = s3.upload_file(
    'local_file.txt',
    'my-bucket',
    'remote_file.txt'
)

print(response)
```

- **Design for Durability:** Data in object storage is typically **replicated** multiple times across different geographic zones or even different datacenters within a region. This protects against hardware failure or site disasters.

## 3. Key Points & Summary

| Aspect                | Compute Cloud                            | Storage Cloud                                       |
| :-------------------- | :--------------------------------------- | :-------------------------------------------------- |
| **Primary Goal**      | Processing Power & Execution             | Data Persistence & Durability                       |
| **Core Unit**         | Virtual Machine (VM)                     | Object, Block, or File                              |
| **Key Design Focus**  | Elasticity, Scalability (Scaling In/Out) | Durability (Replication), Availability, Scalability |
| **Abstraction Level** | Virtualized Hardware (CPU, RAM)          | Virtualized Disk/Storage Volume                     |
| **Example Services**  | AWS EC2, Azure VMs, GCP Compute Engine   | AWS S3 (Object), EBS (Block); Azure Blob, Disk      |

**Summary:** The architectural design of clouds separates compute and storage to allow them to scale independently. This decoupled, service-oriented architecture is the foundation for the core cloud characteristics of **on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service.** Mastering this architectural concept is crucial for designing and deploying efficient applications in the cloud.

## 4. Exam Tips and Key Takeaways

- Understand the four-layer cloud architecture and the role of each layer.
- Know the differences between compute and storage clouds, including their primary goals and design focuses.
- Be able to explain elasticity and scalability in the context of cloud computing.
- Familiarize yourself with the different types of storage (object, block, file) and their use cases.
- Practice designing and deploying applications in the cloud using services like AWS EC2, S3, and Azure VMs, Blob Storage.
