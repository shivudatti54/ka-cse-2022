# Virtual Machines


## Table of Contents

- [Virtual Machines](#virtual-machines)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Classification of Virtual Machines](#definition-and-classification-of-virtual-machines)
  - [Virtual Machine Monitor and Hypervisors](#virtual-machine-monitor-and-hypervisors)
  - [Virtualization of CPU and Memory](#virtualization-of-cpu-and-memory)
  - [Virtual Storage and Networking](#virtual-storage-and-networking)
  - [Containers and Lightweight Virtualization](#containers-and-lightweight-virtualization)
- [Examples](#examples)
  - [Example 1: Creating a Virtual Machine with Type 2 Hypervisor](#example-1-creating-a-virtual-machine-with-type-2-hypervisor)
  - [Example 2: CPU Virtualization and Context Switching](#example-2-cpu-virtualization-and-context-switching)
  - [Example 3: Memory Overcommitment Scenario](#example-3-memory-overcommitment-scenario)
- [Exam Tips](#exam-tips)

## Introduction

Virtual machines represent one of the most significant advances in computer science and information technology infrastructure over the past two decades. A virtual machine (VM) is a software implementation of a physical computer that executes programs like a real machine. In the context of operating systems, virtual machines provide an abstraction layer that allows multiple operating systems to run concurrently on a single physical hardware platform, each believing they have exclusive access to the underlying resources.

The concept of virtual machines emerged from the need to maximize hardware utilization and provide isolation between different computing environments. Modern data centers and cloud computing platforms rely heavily on virtualization technology to deliver scalable, flexible, and cost-effective computing services. Understanding virtual machines is essential for any computer science professional, as virtualization has become the backbone of enterprise IT infrastructure, enabling concepts like cloud computing, containerization, and software-defined networking. For students preparing for operating systems examinations, virtual machines represent a critical topic that bridges theoretical concepts with practical industry applications.

## Key Concepts

### Definition and Classification of Virtual Machines

A virtual machine is created when a software layer, known as a virtual machine monitor (VMM) or hypervisor, partitions the resources of a physical computer to create isolated environments. Each virtual machine contains its own virtual hardware including CPU, memory, storage, and network interfaces. The operating system installed on a virtual machine is called the guest operating system, while the operating system running on the physical hardware is called the host operating system (in Type 2 hypervisors) or simply the underlying platform (in Type 1 hypervisors).

Virtual machines are classified into two fundamental categories: process virtual machines and system virtual machines. Process virtual machines are designed to execute a single program or process in isolation, providing a platform-independent runtime environment. Examples include the Java Virtual Machine (JVM) and .NET Common Language Runtime (CLR), which compile code into bytecode that runs on the virtual machine regardless of the underlying hardware and operating system. System virtual machines, on the other hand, provide complete system-level virtualization where an entire operating system can run on virtual hardware. VMware Workstation, VirtualBox, and enterprise hypervisors like VMware ESXi are examples of system virtual machine implementations.

### Virtual Machine Monitor and Hypervisors

The virtual machine monitor is the core component responsible for creating and managing virtual machines. The VMM sits between the hardware and the guest operating systems, intercepting and handling privileged instructions that would normally require direct hardware access. When a guest operating system attempts to perform operations that require supervisor privileges, the VMM intervenes and emulates these operations on behalf of the virtual machine, maintaining isolation and security.

Hypervisors are categorized into two types based on their architecture. Type 1 hypervisors, also known as bare-metal hypervisors, run directly on the physical hardware without requiring a host operating system. Examples include VMware ESXi, Microsoft Hyper-V, and Xen. These hypervisors provide superior performance and are typically used in enterprise data centers. Type 2 hypervisors, also called hosted hypervisors, run as application software on top of a host operating system. VirtualBox, VMware Workstation, and QEMU are examples of Type 2 hypervisors. While easier to install and use, Type 2 hypervisors incur additional overhead from the host operating system.

### Virtualization of CPU and Memory

CPU virtualization involves creating the illusion of multiple independent CPUs, each with its own register set and execution state. The VMM maintains a virtual CPU (vCPU) for each virtual machine and schedules physical CPU time to these virtual CPUs. Modern processors include hardware assistance for virtualization, such as Intel VT-x and AMD-V, which allow the VMM to run guest operating systems in a more efficient manner by providing separate execution modes for the hypervisor and guest operating systems.

Memory virtualization is more complex because the guest operating system expects to see contiguous physical memory starting from address zero. The VMM maintains a mapping between the guest physical addresses used by the virtual machine and the real physical addresses on the host machine. This两层 addressing scheme requires translation lookaside buffers (TLBs) and can introduce performance overhead. Techniques like memory overcommitment, where the total memory allocated to virtual machines exceeds the physical RAM available, allow for more efficient utilization but require careful management to avoid performance degradation.

### Virtual Storage and Networking

Virtual storage virtualization creates virtual disks that appear to guest operating systems as physical hard drives. These virtual disks are typically stored as files on the host filesystem, allowing for easy backup, migration, and provisioning. Virtual storage can be implemented through various mechanisms including file-based images, logical volume management, and storage area network (SAN) virtualization.

Virtual networking enables virtual machines to communicate with each other and with external networks. Virtual switches, which can be software-based or hardware-assisted, connect virtual network adapters to physical network interfaces. Virtual LANs (VLANs) can be configured within virtual environments to segment network traffic. Virtual networking also supports advanced features like load balancing, port mirroring, and network isolation for security purposes.

### Containers and Lightweight Virtualization

Containerization represents a lightweight alternative to traditional virtual machines. Unlike full virtual machines that virtualize the entire hardware stack, containers share the host operating system kernel while providing process-level isolation. Docker and Kubernetes have popularized container technology in modern DevOps and cloud-native applications. Containers offer faster startup times, lower memory overhead, and more efficient resource utilization compared to virtual machines, though they provide less isolation and cannot run different operating systems than the host.

## Examples

### Example 1: Creating a Virtual Machine with Type 2 Hypervisor

Consider a scenario where a student needs to run Linux on a Windows machine for an operating systems laboratory assignment. Using VirtualBox (a Type 2 hypervisor), the process involves several steps. First, the student installs VirtualBox on the Windows host operating system. Then, they create a new virtual machine specifying the guest operating system type (Linux) and version (Ubuntu). The wizard allocates virtual resources: 2 GB of RAM, 2 CPU cores, and a 50 GB virtual hard disk stored as a VDI file. After creating the VM, they mount an Ubuntu ISO image to the virtual optical drive and start the VM. The VirtualBox hypervisor intercepts boot requests, presents the Ubuntu installer as if running on physical hardware, and manages the installation process. Once Ubuntu is installed, the VMM handles all interactions between the guest OS and host resources, providing seamless operation.

### Example 2: CPU Virtualization and Context Switching

Suppose a physical server with 8 CPU cores hosts four virtual machines, each configured with 2 virtual CPUs. The hypervisor's scheduler must allocate physical CPU time to 8 virtual CPUs. When VM1's vCPU0 needs to execute, the hypervisor performs a context switch, saving the current host state and loading VM1's saved state. If VM1 attempts to execute a privileged instruction like modifying page tables, the CPU generates a trap that the hypervisor catches. The hypervisor then emulates the instruction's effect on the virtual CPU state, simulating what would have happened on real hardware. This process, called virtualization trapping, ensures isolation between virtual machines while maintaining the illusion of exclusive hardware access.

### Example 3: Memory Overcommitment Scenario

A data center operator has a server with 64 GB of RAM and needs to host 10 virtual machines, each requiring 8 GB. Without memory overcommitment, only 8 VMs would fit. With overcommitment, the operator creates all 10 VMs allocating 8 GB each (80 GB virtual memory). The hypervisor uses techniques like transparent page sharing, where identical memory pages across VMs are merged into a single copy, and ballooning, where a balloon driver in the guest OS inflates to reclaim unused memory. If all VMs actively use their allocated memory and demand exceeds physical capacity, the hypervisor performs swapping, moving least-recently-used pages to disk. This demonstrates how virtualization achieves high utilization while maintaining isolation, though administrators must monitor performance carefully.

## Exam Tips

1. UNDERSTAND THE DIFFERENCE BETWEEN TYPE 1 AND TYPE 2 HYPERVISORS: Type 1 hypervisors run directly on hardware (bare-metal) and are used in data centers, while Type 2 hypervisors run as applications on a host OS. Know examples of each type.

2. DISTINGUISH BETWEEN PROCESS VM AND SYSTEM VM: Process VMs (JVM, CLR) execute single programs and are platform-independent; System VMs virtualize entire computer systems to run multiple OS instances.

3. MEMORIZE THE ROLE OF VMM: The Virtual Machine Monitor creates and manages VMs, handles privileged instructions, provides isolation, and performs resource allocation between virtual machines.

4. KNOW HARDWARE VIRTUALIZATION TECHNOLOGIES: Intel VT-x and AMD-V are CPU extensions that assist virtualization by providing separate execution modes, improving performance significantly.

5. UNDERSTAND MEMORY VIRTUALIZATION CONCEPTS: Guest physical addresses and host physical addresses require translation; techniques include page sharing, ballooning, and swapping.

6. CONTAINERS VS VIRTUAL MACHINES: Remember that containers share the host OS kernel and provide process isolation, while VMs provide full hardware virtualization and can run different OS types.

7. ADVANTAGES OF VIRTUALIZATION: Resource utilization, isolation, portability, snapshot/backup capabilities, and rapid provisioning are key benefits frequently asked in exams.

8. VIRTUAL NETWORKING COMPONENTS: Virtual switches connect virtual network adapters to physical networks; understand concepts like virtual LANs and network isolation.

9. PERFORMANCE CONSIDERATIONS: Virtualization introduces overhead due to resource scheduling, emulation, and translation; hardware-assisted virtualization reduces this overhead significantly.

10. LIVE MIGRATION: Advanced feature allowing VMs to move between physical hosts without service interruption, important for load balancing and maintenance in data centers.