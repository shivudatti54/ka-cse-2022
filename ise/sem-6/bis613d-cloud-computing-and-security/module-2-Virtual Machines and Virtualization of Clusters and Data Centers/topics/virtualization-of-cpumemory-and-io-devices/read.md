# Module 2: Virtualization of CPU/Memory and I/O Devices


## Table of Contents

- [Module 2: Virtualization of CPU/Memory and I/O Devices](#module-2-virtualization-of-cpumemory-and-io-devices)
- [Introduction](#introduction)
- [Core Concepts and Techniques](#core-concepts-and-techniques)
  - [1. CPU Virtualization](#1-cpu-virtualization)
  - [2. Memory Virtualization](#2-memory-virtualization)
  - [3. I/O Device Virtualization](#3-io-device-virtualization)
- [Comparison of Virtualization Techniques](#comparison-of-virtualization-techniques)
- [Exam Tips and Key Takeaways](#exam-tips-and-key-takeaways)

## Introduction

Virtualization is the foundational technology that makes cloud computing possible. It involves creating a virtual (rather than actual) version of a computer's hardware components, such as the CPU, memory, storage, and network interfaces. This allows a single physical machine, called the **host**, to run multiple isolated virtual machines (VMs), known as **guests**. Each VM operates with its own operating system and applications as if it were running on its own dedicated hardware. This module explores the core techniques used to virtualize the three critical hardware resources: the CPU, Memory, and I/O devices.

## Core Concepts and Techniques

### 1. CPU Virtualization

The CPU is the brain of the computer, and its virtualization is crucial. The challenge is to allow multiple guest operating systems to share a single physical CPU without interfering with each other. This is primarily managed by a software layer called the **hypervisor** (or Virtual Machine Monitor - VMM).

#### Types of CPU Virtualization

- **Full Virtualization (Binary Translation):** The hypervisor translates and traps all privileged instructions (e.g., those that attempt to change the CPU state) executed by the guest OS. These instructions are translated into safe instructions that can be executed on the physical hardware. The guest OS is unaware it is being virtualized. This method requires no modification to the guest OS but can incur performance overhead.
- **Para-virtualization:** The guest operating system is modified ("hypervisor-aware") to know it is running on a virtualized platform. It makes explicit calls (hypercalls) to the hypervisor for privileged operations. This reduces overhead and improves performance compared to full virtualization but requires modifying the guest OS kernel.
- **Hardware-Assisted Virtualization:** Modern CPUs (Intel VT-x, AMD-V) include built-in features that facilitate virtualization. They introduce a new CPU execution mode (root vs. non-root) that allows the hypervisor to run in a privileged mode while guest OSes run in a less privileged mode. Privileged instructions from the guest automatically trap to the hypervisor, making virtualization more efficient and eliminating the need for binary translation or OS modification.

#### Examples

- VMware ESXi uses full virtualization for legacy systems.
- The Xen hypervisor is a classic example of para-virtualization.
- Most modern hypervisors like KVM, VMware, and Hyper-V leverage hardware-assisted virtualization.

### 2. Memory Virtualization

Each VM requires its own isolated view of a contiguous physical memory space. Memory virtualization maps the physical memory of the host machine to the virtual/physical memory of each guest VM.

#### The Role of the Hypervisor

- The hypervisor maintains a shadow page table for each VM. The guest OS manages its own virtual-to-physical memory mapping (its page table), but this "physical" address is actually a pseudo-physical address. The hypervisor's shadow page table then maps these pseudo-physical addresses to the actual machine addresses.

#### Hardware Support

- Modern processors offer features like **Nested Page Tables (NPT)** from AMD and **Extended Page Tables (EPT)** from Intel. These features hardware-accelerate the two-level address translation (guest virtual -> guest physical -> host physical), significantly reducing the performance penalty associated with software-based shadow page tables.

### 3. I/O Device Virtualization

Virtualizing Input/Output devices (like network cards, storage controllers, and GPUs) is complex due to their diversity and high performance requirements.

#### Types of I/O Virtualization

- **Full Device Emulation:** The hypervisor emulates a well-known, generic hardware device (e.g., an Intel E1000 network card). The guest OS uses its standard driver for this emulated device. The hypervisor then translates the guest's requests and forwards them to the actual physical device. This offers high compatibility but can be inefficient due to the emulation overhead and numerous context switches between the guest and hypervisor.
- **Para-virtualized I/O:** Instead of emulating a real hardware device, the hypervisor provides a simplified, abstract device interface. The guest OS uses special paravirtualized drivers that are aware of the virtualization layer. These drivers communicate directly with the hypervisor via efficient mechanisms, drastically reducing overhead.
- **Direct I/O Passthrough (SR-IOV):** This method bypasses the hypervisor entirely for maximum performance. A physical I/O device, such as a network interface card (NIC) supporting **Single Root I/O Virtualization (SR-IOV)**, can present itself as multiple independent "virtual functions." Each virtual function can be assigned directly to a specific VM. The VM then gets dedicated, direct access to a share of the physical hardware.

#### Examples

- The **Virtio** framework is a standard for paravirtualized I/O in Linux-based hypervisors like KVM. It provides front-end drivers for the guest and back-end drivers on the host, leading to near-native performance.
- Essential for high-performance applications like network packet processing or GPU acceleration in virtualized environments.

## Comparison of Virtualization Techniques

| Aspect                    | Key Technique                         | Description                                                           | Advantage                                                 |
| ------------------------- | ------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------- |
| **CPU Virtualization**    | Hardware-Assisted (Intel VT-x/AMD-V)  | Uses CPU extensions to trap privileged instructions.                  | High performance, no OS modification needed.              |
| **Memory Virtualization** | Nested/Extended Page Tables (NPT/EPT) | Hardware-accelerated translation of guest-to-host physical addresses. | Reduces memory management overhead significantly.         |
| **I/O Virtualization**    | Para-virtualization (e.g., Virtio)    | Uses hypervisor-aware drivers for efficient communication.            | Excellent balance of performance and flexibility.         |
| **I/O Virtualization**    | Direct Passthrough (SR-IOV)           | Assigns a virtual function of a physical device directly to a VM.     | Near-native performance, ideal for high-throughput tasks. |

## Exam Tips and Key Takeaways

- Understand the trade-offs between full virtualization, para-virtualization, and hardware-assisted approaches.
- Remember that modern cloud platforms primarily use hardware-assisted virtualization.
- Know the specific examples: VMware ESXi (full), Xen (para), KVM (hardware-assisted), Virtio (I/O).
- Focus on how virtualization decouples software from hardware enabling cloud computing characteristics.

**In essence, virtualization decouples software from hardware, enabling the resource pooling, on-demand access, and multi-tenancy that are the hallmarks of cloud computing.**
