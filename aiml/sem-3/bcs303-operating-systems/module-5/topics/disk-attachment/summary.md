# Disk Attachment - Summary

## Key Definitions

- **Disk Attachment**: Methods and interfaces used to connect storage devices to a computer system
- **DAS (Direct Attached Storage)**: Storage physically connected to the host system via internal or external interfaces
- **NAS (Network Attached Storage)**: File-level storage accessed over a TCP/IP network using protocols like SMB/CIFS or NFS
- **SAN (Storage Area Network)**: High-speed network dedicated to block-level storage access using protocols like Fibre Channel or iSCSI
- **AHCI**: Advanced Host Controller Interface, the standard interface for SATA controllers
- **LUN (Logical Unit Number)**: Identifier used to address devices in SCSI and SAN environments
- **Hot Swapping**: Ability to add or remove storage devices while the system is running

## Important Formulas

- **Effective Transfer Rate**: Actual throughput considering protocol overhead (e.g., SATA 6 Gbps ≈ 600 MB/s raw, ~550 MB/s effective)
- **IOPS (Input/Output Operations Per Second)**: Measure of storage performance, often more important than raw throughput for random access workloads
- **Latency**: Time from I/O request initiation to completion, determined by seek time, rotational delay, and controller overhead

## Key Points

1. SATA has replaced PATA/IDE as the dominant consumer storage interface, offering higher speeds, hot swapping, and thinner cables.

2. SCSI continues to be relevant in enterprise environments due to its reliability, command queuing, and support for many devices per bus.

3. SAS combines SCSI reliability with SATA's serial architecture, offering dual-port connectivity for high availability.

4. DAS provides lowest latency and simplest management but lacks scalability and multi-host sharing capabilities.

5. NAS excels at file sharing across heterogeneous clients but introduces network latency and bandwidth limitations.

6. SAN delivers highest performance for block storage but requires specialized infrastructure and expertise.

7. Device drivers provide abstraction between the operating system and storage hardware, enabling support for multiple interface types.

8. Modern systems often combine multiple storage types: fast SSDs via SATA/NVMe for boot and applications, NAS for file sharing, and SAN for enterprise databases.

## Common Mistakes

1. **Confusing NAS with SAN**: NAS provides file-level access over standard networks; SAN provides block-level access over dedicated high-speed networks.

2. **Ignoring controller limitations**: A fast SSD connected to a SATA II controller is limited to 300 MB/s regardless of the drive's capabilities.

3. **Overlooking the need for RAID**: In enterprise environments, single disks are rarely acceptable due to failure risk; RAID configurations require proper controller support.

4. **Underestimating latency differences**: Network storage (NAS/SAN) introduces milliseconds of latency compared to sub-millisecond local storage, which matters for latency-sensitive applications.

5. **Hot swapping without proper support**: Attempting to remove disks without hot-swap capability can cause data corruption and hardware damage.