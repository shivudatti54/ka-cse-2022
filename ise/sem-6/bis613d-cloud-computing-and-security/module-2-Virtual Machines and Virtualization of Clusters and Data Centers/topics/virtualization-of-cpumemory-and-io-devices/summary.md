# Virtualization of CPU/Memory and I/O Devices

## Overview

Virtualization creates virtual versions of computer hardware components (CPU, memory, storage, network) allowing a single physical machine (host) to run multiple isolated virtual machines (guests). Each VM operates with its own OS and applications as if running on dedicated hardware, managed by a hypervisor or Virtual Machine Monitor (VMM).

## Key Points

- **Full Virtualization (Binary Translation)**: Hypervisor translates and traps privileged instructions from guest OS; no OS modification needed but has performance overhead (e.g., VMware ESXi for legacy systems)
- **Para-virtualization**: Guest OS is modified to make explicit hypercalls to the hypervisor for privileged operations; reduces overhead and improves performance (e.g., Xen hypervisor)
- **Hardware-Assisted Virtualization**: Modern CPUs (Intel VT-x, AMD-V) include features that allow hypervisor to run in privileged mode with automatic instruction trapping; eliminates need for binary translation or OS modification
- **Memory Virtualization**: Hypervisor maintains shadow page tables mapping guest pseudo-physical addresses to actual machine addresses; modern CPUs support Nested Page Tables (NPT/AMD) and Extended Page Tables (EPT/Intel) for hardware-accelerated translation
- **Full Device Emulation**: Hypervisor emulates well-known hardware devices; high compatibility but inefficient due to emulation overhead and context switches
- **Para-virtualized I/O**: Provides simplified, abstract device interface with special drivers (e.g., Virtio framework) for near-native performance with reduced overhead
- **Direct I/O Passthrough (SR-IOV)**: Physical device presents multiple virtual functions assigned directly to VMs, bypassing hypervisor for maximum performance in high-throughput tasks

## Important Concepts

- Hardware-assisted virtualization provides high performance without OS modification in modern systems
- NPT/EPT hardware features significantly reduce memory management overhead
- Para-virtualized I/O (Virtio) offers excellent balance of performance and flexibility
- SR-IOV is essential for applications requiring near-native performance like GPU acceleration

## Notes

- Understand the trade-offs between full virtualization, para-virtualization, and hardware-assisted approaches
- Remember that modern cloud platforms primarily use hardware-assisted virtualization
- Know the specific examples: VMware ESXi (full), Xen (para), KVM (hardware-assisted), Virtio (I/O)
- Focus on how virtualization decouples software from hardware enabling cloud computing characteristics
