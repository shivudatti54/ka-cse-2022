# Architectural Design of Compute and Storage Clouds

## Overview

Cloud architecture is structured as loosely coupled services that can be dynamically provisioned and managed. The design separates Compute (processing) and Storage (data persistence) resources to allow independent scaling, forming the foundation for achieving elasticity, reliability, and on-demand service delivery in modern cloud platforms.

## Key Points

- **Four-Layer Cloud Architecture**: Hardware/Datacenter Layer (physical foundation) → Infrastructure Layer/IaaS (virtualization with hypervisors creating VMs) → Platform Layer/PaaS (middleware, databases, development tools) → Application Layer/SaaS (end-user applications via browser)
- **Compute Cloud Design**: Virtual Machine (VM) is fundamental unit; resources (CPU, RAM) from numerous hosts aggregated into pools; elasticity allows automatic scaling (scale-out for high traffic, scale-in for low demand)
- **Storage Cloud Design**: Object Storage (AWS S3, Azure Blob - flat namespace for unstructured data), Block Storage (AWS EBS, Azure Disk - raw volumes attached to VMs for databases), File Storage (AWS EFS, Azure Files - shared file systems using NFS/SMB)
- **Compute Elasticity Example**: E-commerce website automatically spins up ten new web server VMs during festival sale, scales back down to two VMs afterward
- **Storage Durability**: Data in object storage replicated multiple times across different geographic zones or datacenters within region, protecting against hardware failure or disasters
- **Resource Pooling**: Cloud management software (orchestrator) draws resources from pools when users request VMs, deploys them, and manages their lifecycle
- **Decoupled Architecture**: Separating compute and storage allows each to scale independently based on specific needs

## Important Concepts

- Compute cloud focuses on processing power with elasticity and scalability as key design features
- Storage cloud prioritizes durability (through replication), availability, and scalability over raw processing speed
- Hypervisor creates VMs (guests) on physical servers (hosts), providing isolation and abstraction
- Storage types serve different purposes: Object for unstructured data (images, videos), Block for low-latency applications (databases), File for shared access (content repositories)
- Architecture enables core cloud characteristics: on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service

## Notes

- Understand why compute and storage are separated architecturally (independent scaling)
- Remember the four-layer cloud architecture and what each layer provides
- Know the three storage types (Object, Block, File) with examples and appropriate use cases
- Be able to explain elasticity with real-world examples like e-commerce peak traffic handling
- Focus on how durability is achieved through geographic replication in storage clouds
- Connect architectural concepts to service models: IaaS (VMs), PaaS (managed platform), SaaS (complete applications)
