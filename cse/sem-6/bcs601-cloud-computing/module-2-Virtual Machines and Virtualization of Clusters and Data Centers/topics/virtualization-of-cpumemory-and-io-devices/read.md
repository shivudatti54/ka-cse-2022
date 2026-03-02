# Module 2: Virtualization of CPU/Memory and I/O Devices

## Introduction

Virtualization constitutes the foundational technology enabling cloud computing paradigms. It involves creating a virtual representation of a computer's hardware platform—including the central processing unit (CPU), main memory, storage subsystems, and network interfaces—rather than providing direct physical hardware to each workload. This abstraction layer permits a single physical machine, termed the **host**, to execute multiple isolated virtual machines (VMs), each designated as a **guest**. Each guest VM operates with its own operating system and application stack, maintaining the illusion of exclusive hardware ownership despite sharing physical resources. This module provides an in-depth examination of the core techniques employed to virtualize three critical hardware resources: the CPU, memory, and I/O devices.

## 1. CPU Virtualization

CPU virtualization addresses the fundamental challenge of enabling multiple guest operating systems to share a single physical processor without mutual interference. The CPU executes instructions in different privilege levels (rings in x86 architecture), where privileged instructions that affect hardware control must be restricted to the most privileged level (ring 0). Guest operating systems expect to execute at this highest privilege level, creating a core virtualization problem.

### 1.1 The Trap-and-Emulate Strategy

The classical approach to CPU virtualization employs **trap-and-emulate**: when a guest OS executes a privileged instruction, the CPU traps (generates a fault) to the hypervisor, which then emulates the intended behavior. This technique requires that all privileged instructions generate traps, a property termed **sensitive instruction** behavior. The x86 architecture historically contained instructions that failed to trap (non-trapping sensitive instructions), necessitating additional techniques.

### 1.2 Virtualization Techniques

**Full Virtualization (Binary Translation):** The hypervisor employs binary translation to convert guest OS instructions before execution. Non-privileged instructions execute directly for performance, while privileged instructions are replaced with calls to hypervisor routines. The guest OS remains unmodified, preserving binary compatibility. However, this approach incurs significant performance overhead due to translation complexity and cache pollution.

**Para-virtualization:** The guest operating system is modified to recognize its virtualized environment, replacing privileged operations with explicit **hypercalls** to the hypervisor. This technique eliminates the need for binary translation, reducing overhead substantially. However, it requires OS kernel modifications, limiting compatibility. The Xen hypervisor pioneered this approach.

**Hardware-Assisted Virtualization:** Modern processors incorporate virtualization extensions—Intel VT-x and AMD-V—that introduce additional CPU execution modes. These extensions provide a **root mode** for the hypervisor and a **non-root mode** for guest VMs. When guests execute privileged instructions, the CPU automatically traps to the hypervisor, eliminating the need for binary translation or para-virtualization. This approach provides near-native performance while maintaining guest OS compatibility.

### 1.3 Performance Analysis

The overhead of CPU virtualization depends on the frequency of privileged operations and trap handling latency. Hardware-assisted virtualization typically incurs 1-3% overhead for compute-intensive workloads, while binary translation may introduce 5-15% overhead due to translation and caching costs.

## 2. Memory Virtualization

Memory virtualization must provide each VM with an isolated, contiguous address space while the physical host memory is fragmented and shared. This requires a three-level address translation hierarchy.

### 2.1 Memory Virtualization Fundamentals

Guest software operates using **virtual addresses** (GVA), which the guest OS translates to **guest physical addresses** (GPA). However, GPA is not the actual hardware address; it is a pseudo-physical address that the hypervisor must map to **machine addresses** (MA) representing actual hardware memory. This creates a two-stage translation requirement: GVA → GPA → MA.

### 2.2 Shadow Page Tables

Initially, hypervisors implemented memory virtualization through **shadow page tables**. The hypervisor maintains shadow page tables that directly map GVA to MA, bypassing the guest's page tables. When guest page tables are modified, the hypervisor intercepts the operation and updates the shadow tables accordingly. This technique maintains isolation but introduces significant overhead due to page table synchronization and additional memory consumption.

### 2.3 Hardware-Assisted Memory Virtualization

Modern processors provide **Nested Page Tables (NPT)** (AMD) or **Extended Page Tables (EPT)** (Intel), enabling hardware-accelerated two-stage address translation. The CPU traverses both the guest page table and the host's nested page table automatically, reducing hypervisor involvement. This approach improves performance by 5-10% for memory-intensive workloads and eliminates the complexity of shadow page table management.

**Mathematical Model:** The effective memory access time with nested paging is:

T_effective = T_base × (1 + F × (T_L1 + T_L2))

Where T_base represents base memory access time, F is the page fault rate, and T_L1, T_L2 represent L1 and L2 page table lookup times respectively.

## 3. I/O Device Virtualization

I/O device virtualization presents unique challenges due to device diversity, high performance requirements, and the complexity of device driver ecosystems. Multiple virtualization models exist, each balancing compatibility, performance, and isolation.

### 3.1 Full Device Emulation

The hypervisor emulates a well-known hardware device (e.g., Intel E1000 network adapter). Guest OSes use standard device drivers designed for the emulated hardware. The hypervisor intercepts I/O operations and translates them to actual device operations. This approach provides excellent compatibility but introduces substantial overhead due to emulation complexity and frequent context switches. Performance typically reaches 30-50% of native I/O throughput.

### 3.2 Para-virtualized I/O

Para-virtualized I/O replaces hardware emulation with optimized shared memory buffers and notification mechanisms. The **Virtio** standard exemplifies this approach, defining a paravirtualization framework with front-end drivers in the guest and back-end drivers in the host. Communication occurs through shared memory rings, minimizing data copying. Performance approaches 70-90% of native throughput.

The **vhost** kernel module further optimizes Virtio by allowing the host kernel to directly access guest memory for I/O operations, reducing hypervisor involvement and improving latency.

### 3.3 Direct I/O Passthrough

For maximum performance, **SR-IOV (Single Root I/O Virtualization)** enables physical devices to present multiple independent virtual functions (VFs). Each VF can be directly assigned to a guest VM, bypassing the hypervisor entirely. The VM interacts with the device using native drivers, achieving 95-98% of native performance. However, this approach sacrifices hypervisor-mediated isolation and complicates live migration.

## 4. Comparative Analysis

| Technique | Performance | Isolation | Compatibility | Use Case |
|-----------|-------------|-----------|---------------|----------|
| Binary Translation | Low-Medium | High | Guest unmodified | Legacy systems |
| Para-virtualization | Medium-High | High | OS modification required | Linux/Unix VMs |
| Hardware-Assisted | High | High | Guest unmodified | General purpose |
| Virtio Para-virtual I/O | High | Medium | Driver support needed | Cloud workloads |
| SR-IOV Passthrough | Near-native | Lower | Hardware support required | HPC, NFV |

## 5. Conclusion

CPU, memory, and I/O device virtualization employ distinct techniques optimized for each resource's characteristics. Hardware-assisted virtualization has become dominant for CPU and memory, while I/O virtualization continues to balance compatibility (emulation), performance (Virtio), and maximum throughput (SR-IOV) based on workload requirements.