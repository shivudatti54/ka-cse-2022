# Virtual Machines


## Table of Contents

- [Virtual Machines](#virtual-machines)
- [Introduction](#introduction)
- [Concept of Virtualization](#concept-of-virtualization)
  - [Key Terminology](#key-terminology)
- [Types of Hypervisors](#types-of-hypervisors)
  - [Type 1: Bare-Metal Hypervisor](#type-1-bare-metal-hypervisor)
  - [Type 2: Hosted Hypervisor](#type-2-hosted-hypervisor)
  - [Comparison: Type 1 vs Type 2](#comparison-type-1-vs-type-2)
- [Benefits of Virtual Machines](#benefits-of-virtual-machines)
  - [1. Isolation](#1-isolation)
  - [2. Server Consolidation](#2-server-consolidation)
  - [3. Testing and Development](#3-testing-and-development)
  - [4. Security and Sandboxing](#4-security-and-sandboxing)
  - [5. OS Research and Education](#5-os-research-and-education)
  - [6. Snapshots and Recovery](#6-snapshots-and-recovery)
  - [7. Live Migration](#7-live-migration)
- [Java Virtual Machine (JVM) - Application-Level VM](#java-virtual-machine-jvm---application-level-vm)
  - [JVM vs System VM](#jvm-vs-system-vm)
- [Para-Virtualization](#para-virtualization)
  - [Advantages of Para-Virtualization](#advantages-of-para-virtualization)
  - [Disadvantages](#disadvantages)
- [Hardware-Assisted Virtualization](#hardware-assisted-virtualization)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

A **Virtual Machine (VM)** is a software-based emulation of a physical computer. Virtualization technology allows a single physical machine (host) to run multiple virtual machines, each with its own operating system, as if they were separate physical computers.

> **Definition:** A virtual machine provides an interface that is identical to the underlying bare hardware. The operating system running in a VM believes it has its own dedicated hardware, but the hardware is actually shared with other VMs.

The fundamental idea is to abstract the hardware of a single computer (CPU, memory, disk, network) into several different execution environments, thereby creating the illusion that each environment has its own private computer.

## Concept of Virtualization

```
Traditional System: Virtualized System:
+------------------+ +------+ +------+ +------+
| Applications | | App | | App | | App |
+------------------+ +------+ +------+ +------+
| Operating | | OS 1 | | OS 2 | | OS 3 |
| System | |(Linux)|(Win) |(macOS)|
+------------------+ +------+ +------+ +------+
| Hardware | | Hypervisor |
+------------------+ +-------------------------+
 | Hardware |
 +-------------------------+
```

### Key Terminology

| Term           | Definition                                                                                           |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| **Host**       | The underlying physical machine and its OS                                                           |
| **Guest**      | The virtual machine and its OS                                                                       |
| **Hypervisor** | Software layer that creates and manages virtual machines (also called Virtual Machine Monitor - VMM) |
| **Host OS**    | The operating system running on the physical machine                                                 |
| **Guest OS**   | The operating system running inside a virtual machine                                                |

## Types of Hypervisors

### Type 1: Bare-Metal Hypervisor

The hypervisor runs **directly on the hardware** (no host OS). It has direct access to hardware resources and provides maximum performance and security.

```
+------+ +------+ +------+
| VM 1 | | VM 2 | | VM 3 |
|(Linux)|(Win) |(Ubuntu)|
+------+ +------+ +------+
+---------------------------+
| Type 1 Hypervisor |
| (runs on bare metal) |
+---------------------------+
| Hardware |
+---------------------------+
```

**Examples:**
| Hypervisor | Vendor | Use Case |
|-----------|--------|----------|
| **VMware ESXi** | VMware | Enterprise data centers |
| **Microsoft Hyper-V** | Microsoft | Windows Server virtualization |
| **Xen** | Open source | Cloud computing (Amazon AWS uses Xen/Nitro) |
| **KVM** | Open source (Linux) | Linux-based virtualization |
| **Oracle VM Server** | Oracle | Enterprise virtualization |

**Characteristics:**

- Higher performance (no host OS overhead)
- Better security (smaller attack surface)
- Used in data centers and cloud computing
- Requires dedicated hardware

### Type 2: Hosted Hypervisor

The hypervisor runs **on top of a host operating system** as an application. It is easier to set up but has more overhead since it goes through the host OS.

```
+------+ +------+ +------+
| VM 1 | | VM 2 | | VM 3 |
|(Linux)|(Win) |(Ubuntu)|
+------+ +------+ +------+
+---------------------------+
| Type 2 Hypervisor |
| (runs on host OS) |
+---------------------------+
| Host Operating System |
| (Windows/Linux/macOS) |
+---------------------------+
| Hardware |
+---------------------------+
```

**Examples:**
| Hypervisor | Vendor | Use Case |
|-----------|--------|----------|
| **Oracle VirtualBox** | Oracle | Personal/educational use |
| **VMware Workstation** | VMware | Development and testing |
| **VMware Fusion** | VMware | macOS virtualization |
| **Parallels Desktop** | Parallels | macOS users running Windows |
| **QEMU** | Open source | Emulation and virtualization |

**Characteristics:**

- Easier to install (just an application)
- Lower performance (host OS overhead)
- Good for development, testing, and learning
- Runs on standard desktop operating systems

### Comparison: Type 1 vs Type 2

| Feature         | Type 1 (Bare-Metal)         | Type 2 (Hosted)                |
| --------------- | --------------------------- | ------------------------------ |
| **Runs on**     | Directly on hardware        | On top of host OS              |
| **Performance** | Higher                      | Lower (host OS overhead)       |
| **Security**    | Better                      | Dependent on host OS security  |
| **Use case**    | Data centers, cloud         | Desktop, development, testing  |
| **Setup**       | Requires dedicated hardware | Easy, install like any app     |
| **Examples**    | VMware ESXi, Hyper-V, Xen   | VirtualBox, VMware Workstation |

## Benefits of Virtual Machines

### 1. Isolation

Each VM is completely isolated from other VMs. A crash or virus in one VM does not affect others.

```
+------+ +------+ +------+
| VM 1 | | VM 2 | | VM 3 |
| OK | |CRASH | | OK |
+------+ +------+ +------+
 VM 2 crash does NOT
 affect VM 1 or VM 3
```

### 2. Server Consolidation

Multiple underutilized physical servers can be consolidated into VMs on a single powerful server, reducing hardware costs.

```
Before: After:
[Server 1: 10% CPU] [Single Server: 70% CPU]
[Server 2: 15% CPU] --> +------+------+------+
[Server 3: 20% CPU] |VM 1 |VM 2 |VM 3 |
 +------+------+------+
Waste: 3 servers Savings: 2 servers
```

### 3. Testing and Development

Developers can test software on multiple OS environments without needing separate physical machines.

### 4. Security and Sandboxing

Suspicious software can be run inside a VM (sandbox). If it is malicious, it cannot escape the VM to harm the host.

### 5. OS Research and Education

Researchers can develop and test new operating systems inside VMs without risking physical hardware.

### 6. Snapshots and Recovery

VMs can be snapshotted (saved at a point in time) and restored instantly -- useful for backup and disaster recovery.

### 7. Live Migration

Running VMs can be moved from one physical host to another without downtime -- used in cloud computing for load balancing and maintenance.

## Java Virtual Machine (JVM) - Application-Level VM

The **Java Virtual Machine (JVM)** is not a system-level VM but an **application-level virtual machine**. It executes Java bytecode, providing platform independence.

```
+------------------+
| Java Program |
| (Source: .java) |
+------------------+
 |
 javac (compiler)
 |
+------------------+
| Java Bytecode |
| (.class file) |
+------------------+
 |
+------------------+
| JVM |
| (Interprets or |
| JIT compiles |
| bytecode) |
+------------------+
 |
+------------------+
| Host OS + HW |
+------------------+
```

### JVM vs System VM

| Feature                 | JVM (Application VM)           | System VM (VMware, etc.)          |
| ----------------------- | ------------------------------ | --------------------------------- |
| **What it virtualizes** | A runtime environment          | Entire hardware                   |
| **Runs**                | Java bytecode only             | Complete OS + apps                |
| **Purpose**             | Platform independence for Java | Multiple OS on one machine        |
| **Performance**         | JIT compilation for speed      | Near-native with hardware support |

## Para-Virtualization

In **para-virtualization**, the guest OS is **modified** to be aware that it is running in a virtual machine. Instead of trying to execute privileged instructions directly (which would be trapped by the hypervisor), the guest OS makes explicit calls (hypercalls) to the hypervisor.

```
Full Virtualization: Para-Virtualization:
+--------+ +--------+
|Guest OS| |Modified|
|(unmod.)| |Guest OS|
+---+----+ +---+----+
 | |
 Privileged Hypercall
 instruction (direct call
 TRAPPED by to hypervisor)
 hypervisor |
 | |
+---+------+ +---+------+
|Hypervisor| |Hypervisor|
+----------+ +----------+
```

### Advantages of Para-Virtualization

- **Better performance** than full virtualization (no trap-and-emulate overhead)
- More efficient communication between guest and hypervisor

### Disadvantages

- Guest OS must be **modified** (source code access required)
- Cannot run unmodified proprietary OSes (like Windows) without modification
- **Example:** Xen supports para-virtualization

## Hardware-Assisted Virtualization

Modern CPUs provide hardware support for virtualization:

| Technology     | Vendor | Feature                                        |
| -------------- | ------ | ---------------------------------------------- |
| **Intel VT-x** | Intel  | Hardware virtualization extensions             |
| **AMD-V**      | AMD    | AMD virtualization technology                  |
| **Intel EPT**  | Intel  | Extended Page Tables for memory virtualization |
| **Intel VT-d** | Intel  | Direct I/O virtualization                      |

These technologies allow the hypervisor to run guest OS code directly on the CPU in a special mode, reducing the performance overhead of virtualization significantly.

## Summary

```
+--------------------------------------------------+
| Virtual Machines Summary |
+--------------------------------------------------+
| |
| Hypervisor Types: |
| Type 1 (Bare-metal): ESXi, Hyper-V, Xen |
| Type 2 (Hosted): VirtualBox, VMware Workstation|
| |
| Benefits: Isolation, Consolidation, Testing, |
| Security, Snapshots, Live Migration |
| |
| JVM: Application-level VM for Java bytecode |
| |
| Para-virtualization: Modified guest OS, |
| hypercalls for better performance |
| |
| Hardware support: Intel VT-x, AMD-V |
+--------------------------------------------------+
```

## Exam Tips

1. **Type 1 vs Type 2 hypervisors** is a very common question. Know the differences, examples, and diagrams for both.
2. **Benefits of VMs:** Memorize at least 5 benefits -- isolation, consolidation, testing, security, snapshots. Be ready to explain each briefly.
3. **Draw diagrams:** Practice drawing the architecture diagrams for Type 1 and Type 2 hypervisors.
4. **JVM as application-level VM:** Understand that JVM virtualizes a runtime (not hardware). It provides "write once, run anywhere" for Java.
5. **Para-virtualization vs full virtualization:** Know that para-virtualization requires guest OS modification but offers better performance. Xen is the standard example.
6. **Hardware virtualization support:** Mention Intel VT-x and AMD-V to show awareness of modern hardware support.
7. ** commonly asks:** "Explain virtual machines with a neat diagram" or "Compare Type 1 and Type 2 hypervisors."
8. **Server consolidation** is a key business benefit -- multiple underutilized servers consolidated into one, saving hardware and energy costs.
