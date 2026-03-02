# Virtualization Structure, Tools and Mechanisms

## Overview

Virtualization structure involves a Virtual Machine Monitor (VMM) or hypervisor that manages and allocates hardware resources to multiple Virtual Machines. The core components include the host machine (physical hardware), hypervisor (management layer), guest operating systems, and virtual machines that operate in isolated environments.

## Key Points

- **Type 1 (Bare-Metal) Hypervisor**: Installed directly on physical hardware offering better performance and security; does not rely on host OS (e.g., VMware ESXi, Microsoft Hyper-V, Xen, KVM)
- **Type 2 (Hosted) Hypervisor**: Runs as application on top of host operating system; easier to set up but has performance overhead (e.g., VMware Workstation, Oracle VirtualBox, Parallels Desktop)
- **Full Virtualization**: Complete hardware simulation using binary translation for sensitive instructions; allows unmodified guest OS to run (e.g., VMware Workstation)
- **Paravirtualization**: Guest OS is modified to be aware of virtualization with hypercalls to hypervisor for better performance; requires modified guest kernel (e.g., Xen in paravirtualization mode)
- **Hardware-Assisted Virtualization**: Uses CPU extensions (Intel VT-x, AMD-V) to improve performance by reducing hypervisor overhead; supported by most modern processors
- **Memory Virtualization Techniques**: Shadow page tables maintain guest-to-host physical memory mapping; Extended Page Tables (EPT/Intel) and memory overcommitment for optimization
- **I/O Device Virtualization**: Full emulation (compatible but slower), paravirtualized drivers (better performance), direct I/O passthrough using SR-IOV (maximum performance)

## Important Concepts

- Type 1 hypervisors run directly on hardware for production environments while Type 2 run on host OS for development/testing
- CPU virtualization schedules physical CPU time across multiple VMs presenting virtual CPUs (vCPUs)
- Orchestration platforms like OpenStack, VMware vRealize, and Kubernetes manage virtualized environments
- Containerization (Docker) provides application isolation but is not full virtualization - shares host OS kernel

## Notes

- Be able to identify and differentiate Type 1 vs Type 2 hypervisors with examples
- Remember hardware-assisted virtualization improves performance by reducing hypervisor overhead
- Understand trade-offs between performance, cost, and features when comparing technologies
- Know that EPT is hardware-assisted memory virtualization offering better performance than shadow page tables
- Focus on how virtualization enables data center automation and cloud computing characteristics
