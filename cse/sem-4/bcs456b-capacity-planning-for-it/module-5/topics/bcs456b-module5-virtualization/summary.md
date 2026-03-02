# Virtualization in IT Capacity Planning - Summary

## Key Definitions and Concepts

- **Virtualization**: Creating software-based representations of physical IT resources (servers, storage, networks) to enable multiple virtual instances on a single physical platform
- **Hypervisor**: Software layer that enables virtualization by allowing multiple VMs to share physical hardware resources
- **Virtual Machine (VM)**: Isolated software container with its own virtual CPU, memory, storage, and network interface
- **vCPU**: Virtual CPU assigned to a VM, scheduled by the hypervisor on physical cores

## Important Formulas and Techniques

- **Resource Utilization Improvement**: Virtualization typically improves CPU utilization from 5-15% (physical servers) to 60-80% (virtualized servers)
- **Server Consolidation Ratio**: Number of physical servers reduced = Original servers × Average utilization / Target utilization
- **Memory Overcommitment**: Total VM memory allocation can exceed physical RAM through techniques like ballooning and page sharing

## Key Points

1. Virtualization originated in the 1960s but became mainstream in the early 2000s with x86 virtualization solutions
2. Five main types: Server (most common), Desktop (VDI), Network (SDN), Storage (SAN/NAS abstraction), and Application virtualization
3. Type 1 hypervisors (VMware ESXi, Hyper-V) run directly on hardware; Type 2 hypervisors (VirtualBox, VMware Workstation) run on host OS
4. Live migration enables moving running VMs between hosts without downtime for maintenance and load balancing
5. Virtualization reduces capital expenditure (hardware costs) and operational expenditure (power, cooling, space)
6. VM sprawl (uncontrolled VM proliferation) is a common management challenge requiring governance policies
7. Virtualization is the foundational technology for cloud computing—IAAS, PAAS, and SAAS all rely on virtualization
8. Disaster recovery is significantly improved through VM replication and rapid failover capabilities

## Common Mistakes to Avoid

- Confusing virtualization with cloud computing—virtualization is the technology, cloud is the service delivery model
- Oversubscribing resources without considering performance requirements and peak load scenarios
- Neglecting security considerations in virtualized environments—VM isolation can be compromised if not properly configured
- Underestimating the importance of VM sprawl management and proper capacity forecasting

## Revision Tips

1. Focus on memorizing all five types of virtualization with one example for each
2. Remember the key difference between Type 1 and Type 2 hypervisors
3. Know the typical utilization improvement percentages from virtualization
4. Understand how virtualization enables elastic capacity in cloud environments
5. Review the advantages and disadvantages table to be prepared for comparative questions
