# Virtual Machines - Summary

## Key Definitions and Concepts

A VIRTUAL MACHINE is a software implementation of a physical computer that executes programs like a real machine, created by partitioning physical resources through a virtual machine monitor. A HYPERVISOR or VMM is the software layer that creates and manages virtual machines, intercepting privileged instructions and allocating physical resources. PROCESS VIRTUAL MACHINES execute single programs and provide platform independence, exemplified by JVM and .NET CLR. SYSTEM VIRTUAL MACHINES virtualize entire computer systems to run multiple operating systems concurrently. TYPE 1 HYPERVISORS run directly on bare metal without a host OS (VMware ESXi, Hyper-V), while TYPE 2 HYPERVISORS run as applications on a host OS (VirtualBox, VMware Workstation).

## Important Formulas and Techniques

CPU VIRTUALIZATION involves time-sharing physical CPUs among virtual CPUs through scheduling. MEMORY VIRTUALIZATION uses translation between guest physical addresses and host physical addresses, with techniques like page sharing and ballooning for efficiency. VIRTUAL STORAGE creates virtual disks as files or logical volumes, supporting thin provisioning and snapshots. LIVE MIGRATION moves running VMs between physical hosts without downtime using memory pre-copy mechanisms.

## Key Points

- Virtual machines provide hardware abstraction, enabling multiple OS instances on single physical hardware
- Type 1 hypervisors offer better performance and are used in enterprise data centers
- Type 2 hypervisors are easier to set up but have higher overhead
- Hardware virtualization extensions (Intel VT-x, AMD-V) significantly improve VM performance
- Memory overcommitment allows allocating more virtual memory than physical RAM available
- Containers share the host OS kernel, providing lightweight virtualization
- Virtual networking uses virtual switches to connect VMs to physical networks
- Virtualization enables important features like live migration, high availability, and disaster recovery

## Common Mistakes to Avoid

CONFUSING PROCESS VMS WITH SYSTEM VMS is a common error; remember process VMs run programs while system VMs run entire operating systems. IGNORING THE DIFFERENCE BETWEEN HYPERVISOR TYPES leads to incorrect architecture understanding; Type 1 is bare-metal, Type 2 is hosted. UNDERESTIMATING VIRTUALIZATION OVERHEAD is incorrect; virtual machines do introduce performance penalties compared to bare-metal deployment. BELIEVING CONTAINERS ARE THE SAME AS VMS is wrong; containers share the kernel and provide less isolation.

## Revision Tips

CREATE COMPARISON TABLES between hypervisor types, VM types, and virtualization approaches to clarify distinctions. PRACTICE DRAWING VIRTUALIZATION ARCHITECTURE DIAGRAMS showing the relationship between hardware, VMM, and guest operating systems. UNDERSTAND THE EXECUTION FLOW when a guest OS makes a system call or executes privileged instructions to grasp VMM functionality. REVIEW CURRENT INDUSTRY TRENDS in virtualization and containerization as examination questions often relate concepts to practical applications.