# Virtual Clusters and Resource Management

## Overview

Virtual Clusters are collections of interconnected virtual machines deployed and managed as a unified resource pool to execute distributed applications. Unlike physical clusters, virtual clusters are dynamically constructed using virtualization technology, enabling multiple isolated clusters to coexist on the same physical hardware with improved resource utilization and flexibility.

## Key Points

- **Building Blocks**: Virtual Machines (computation units), Virtual Network (interconnects VMs), Virtual Storage (abstracted storage resources), Cluster Manager (provisioning and monitoring software like Kubernetes, Mesos, vSphere)
- **Dynamic Provisioning**: Cluster scales resources (VMs, CPU, memory, storage) up or down based on demand; process includes request, scheduling, deployment, configuration, and integration completed in minutes
- **Resource Allocation**: Deciding how physical resources (CPU cycles, memory pages, I/O bandwidth) are distributed among competing VMs using static or dynamic allocation policies
- **Load Balancing**: Distributing workload evenly across physical hosts to prevent hotspots and ensure no single host is overwhelmed
- **Server Consolidation**: Combining workloads from multiple underutilized hosts onto fewer hosts to power down idle servers and save energy
- **Live Migration**: Moving running VM from one physical host to another with minimal downtime using pre-copy (iterative memory copying), stop-and-copy (final delta and state), and switchover phases
- **High Availability (HA)**: Automatically restarts VMs on healthy hosts after physical host failure with brief service interruption
- **Fault Tolerance (FT)**: Maintains continuously updated secondary VM on different host for instant takeover with zero downtime and no state loss

## Important Concepts

- Layered architecture: Virtual Cluster → Virtualization Layer (Hypervisors) → Physical Infrastructure (Servers, Network, Storage)
- Resource management policies: Allocation (static vs. dynamic), Scheduling (packing vs. spreading), Scaling (horizontal vs. vertical)
- Live migration is cornerstone for load balancing, proactive maintenance, and energy savings with millisecond pause duration
- Virtual clusters enable multi-tenancy, allowing cloud providers to multiplex physical resources among multiple isolated tenants

## Notes

- Clearly articulate difference between physical and virtual clusters highlighting advantages (flexibility, multi-tenancy, efficiency)
- Know the three steps of live migration: pre-copy, stop-and-copy, switchover and their importance
- Differentiate resource management policies (what to achieve) from mechanisms (how to implement)
- Compare HA vs. FT: HA has brief interruption, FT has zero downtime but higher resource overhead
- Ultimate goal is meeting performance and availability SLAs while minimizing operational costs
