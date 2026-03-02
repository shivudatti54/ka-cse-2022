# Cloud Platform Architecture over Virtualized Datacenters

## Overview

Cloud computing architecture is built atop massive physical datacenters using virtualization as the core enabling technology. The architecture abstracts, pools, and automates physical resources to deliver scalable, on-demand services, transforming static physical datacenters into dynamic, flexible environments delivering utility-like computing services.

## Key Points

- **Hypervisor (VMM)**: Software layer creating and running virtual machines; sits between physical hardware and VMs, abstracting resources (CPU, RAM, Storage, Network) and allocating them to isolated VMs (examples: VMware vSphere, Microsoft Hyper-V, KVM)
- **Physical Layer**: Foundation consisting of actual hardware (server racks, storage arrays, networking switches/routers, power supplies, cooling systems)
- **Virtualization/Abstraction Layer**: Hypervisor abstracts hardware into unified resource pool, partitions into multiple isolated execution environments (VMs), emulates hardware for guest VMs
- **Resource Pooling and Automation Layer**: CPU cycles, storage, and bandwidth pooled together for dynamic assignment in multi-tenant model; orchestration tools (Kubernetes, OpenStack) automate provisioning, deployment, scaling, and management
- **Service Delivery Layer**: Top layer where consumers interact via web portals and APIs; delivers IaaS (raw compute/storage/networking as VMs), PaaS (managed platform for development), SaaS (complete running applications)
- **Multi-Tenancy**: Architecture allows extreme hardware utilization where resources are shared efficiently among numerous consumers securely
- **Automated Provisioning**: User requests trigger automated sequences selecting hosts, creating VMs, configuring networks, and deploying OS without human intervention

## Important Concepts

- Layered architecture: Physical Hardware → Virtualization/Abstraction → Resource Pooling/Automation → Service Delivery
- Virtual Machines provide complete isolation with own guest OS and applications, secured from other VMs on same host
- Orchestration software automates resource provisioning enabling self-service and rapid elasticity characteristics
- Example flow: User request → Cloud management software → Resource pool check → Host selection → VM instantiation → Network configuration → Credential delivery
- Efficiency and multi-tenancy transform rigid physical datacenters into dynamic, flexible cloud environments

## Notes

- Understand how virtualization is the cornerstone technology making cloud computing possible
- Remember the four-layer cloud datacenter architecture from bottom to top
- Focus on how resource pooling and automation enable the cloud's on-demand characteristics
- Be able to trace the complete flow of provisioning a web server from user request to deployment
- Explain how multi-tenancy improves hardware utilization while maintaining security and isolation
- Connect this architecture to the three service models (IaaS, PaaS, SaaS) and their delivery
