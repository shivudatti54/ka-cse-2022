# Disk Attachment and Storage Systems

## Introduction

Computers access secondary storage in three main ways: through **host-attached storage** (directly connected), **network-attached storage (NAS)** (via a data network), and **storage area networks (SAN)** (via a dedicated storage network). Understanding these attachment methods and their trade-offs is essential for designing efficient and reliable storage systems. Additionally, **RAID** (Redundant Array of Independent Disks) provides methods to improve both performance and reliability of disk storage.

## Host-Attached Storage (DAS - Direct Attached Storage)

Host-attached storage is accessed through local I/O ports on the host computer. The storage device is directly connected to the machine using a hardware interface/bus.

### Common Interfaces

| Interface | Full Name                        | Type     | Speed (typical)      | Notes                                             |
| :-------- | :------------------------------- | :------- | :------------------- | :------------------------------------------------ |
| **IDE**   | Integrated Drive Electronics     | Parallel | Up to 133 MB/s       | Legacy; max 2 devices per channel                 |
| **SATA**  | Serial ATA                       | Serial   | Up to 600 MB/s       | Most common in desktops/laptops                   |
| **SCSI**  | Small Computer Systems Interface | Parallel | Up to 640 MB/s       | Used in servers; supports 16 devices              |
| **SAS**   | Serial Attached SCSI             | Serial   | Up to 2.4 GB/s       | Enterprise servers; backward compatible with SATA |
| **NVMe**  | Non-Volatile Memory Express      | Serial   | Up to 7+ GB/s        | For SSDs; uses PCIe bus directly                  |
| **USB**   | Universal Serial Bus             | Serial   | Up to 20 Gbps (USB4) | External storage                                  |
| **FC**    | Fibre Channel                    | Serial   | Up to 128 Gbps       | SAN connectivity                                  |

### How Host-Attached Storage Works

```
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Host CPU │────→│ I/O Bus │────→│ Disk Drive │
│ │ │ (SATA/SAS/ │ │ (HDD or SSD) │
│ │ │ NVMe/SCSI) │ │ │
└──────────────┘ └──────────────┘ └──────────────┘
 │
 │ I/O commands sent via device driver
 │ Data transferred via DMA
```

**Advantages:**

- Fastest access (no network overhead)
- Simplest setup
- Lowest latency

**Disadvantages:**

- Storage is tied to one host (not easily shared)
- Limited by the number of I/O ports
- Scalability is limited

---

## Network-Attached Storage (NAS)

NAS provides file-level storage accessed over a standard **data network** (LAN/WAN). A NAS device is essentially a specialized computer that serves files to client machines over the network.

### Architecture

```
┌────────────┐ ┌──────────────────┐
│ Client 1 │──┐ │ NAS Device │
└────────────┘ │ ┌──────────────┐ │ ┌──────────────┐ │
 ├──→│ Network │─────→│ │ File System │ │
┌────────────┐ │ │ (LAN/WAN) │ │ │ Server │ │
│ Client 2 │──┤ │ TCP/IP │ │ ├──────────────┤ │
└────────────┘ │ └──────────────┘ │ │ RAID Storage │ │
 │ │ │ (disks) │ │
┌────────────┐ │ │ └──────────────┘ │
│ Client 3 │──┘ └──────────────────┘
└────────────┘
```

### Protocols Used

| Protocol | Full Name                   | OS Support     | Description                      |
| :------- | :-------------------------- | :------------- | :------------------------------- |
| **NFS**  | Network File System         | Unix/Linux     | Standard file sharing for Unix   |
| **CIFS** | Common Internet File System | Windows        | Windows file sharing (SMB-based) |
| **SMB**  | Server Message Block        | Cross-platform | Modern protocol for file sharing |

### How NAS Works

1. Client sends a file-level request (e.g., "read file X") over the network
2. Request travels via TCP/IP to the NAS device
3. NAS device's file system locates the file on its local disks
4. Data is sent back over the network to the client

**Advantages:**

- Easy file sharing among multiple clients
- Centralized storage management and backup
- Accessible from anywhere on the network
- Easy to add more storage (scalable)

**Disadvantages:**

- Slower than DAS (network overhead and latency)
- Network bandwidth becomes a bottleneck
- Not suitable for high-performance block-level I/O (like databases)

---

## Storage Area Network (SAN)

A SAN is a **dedicated, high-speed network** that connects servers to shared storage devices. Unlike NAS, a SAN provides **block-level access** -- the server sees the SAN storage as if it were a locally attached disk.

### Architecture

```
┌────────────┐ ┌──────────────────────────────┐ ┌──────────────┐
│ Server 1 │────→│ │────→│ Disk Array │
└────────────┘ │ SAN Fabric │ │ (RAID) │
 │ (Fibre Channel or │ └──────────────┘
┌────────────┐ │ iSCSI Network) │
│ Server 2 │────→│ │────→┌──────────────┐
└────────────┘ │ Dedicated high-speed │ │ Tape Library│
 │ storage network │ └──────────────┘
┌────────────┐ │ │
│ Server 3 │────→│ │────→┌──────────────┐
└────────────┘ └──────────────────────────────┘ │ SSD Array │
 └──────────────┘
```

### SAN Protocols

| Protocol               | Description                                                                                                      |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Fibre Channel (FC)** | Dedicated storage protocol; very high speed (up to 128 Gbps); uses special switches and HBAs (Host Bus Adapters) |
| **iSCSI**              | Encapsulates SCSI commands in TCP/IP packets; runs over standard Ethernet; cheaper than FC                       |
| **FCoE**               | Fibre Channel over Ethernet; combines FC and Ethernet                                                            |

### How SAN Works

1. Server sends block-level I/O commands (like read block 500)
2. Commands travel over the SAN fabric (FC switch or iSCSI network)
3. Storage device processes the block request
4. Data blocks are returned to the server
5. Server's OS sees the SAN disk as a local volume -- it can format it and create its own file system

**Advantages:**

- High performance (dedicated network, no data network contention)
- Block-level access (servers can format and use as local disks)
- Multiple servers can share storage pools
- Excellent for databases and high-performance workloads

**Disadvantages:**

- Expensive (specialized hardware: FC switches, HBAs)
- Complex to set up and manage
- Requires specialized knowledge

---

## Comparison: DAS vs NAS vs SAN

| Feature          | DAS                    | NAS                   | SAN                       |
| :--------------- | :--------------------- | :-------------------- | :------------------------ |
| **Connection**   | Direct (SATA/SAS/SCSI) | LAN/WAN (TCP/IP)      | Dedicated storage network |
| **Access level** | Block-level            | File-level            | Block-level               |
| **Protocol**     | SATA/SAS/NVMe          | NFS/CIFS/SMB          | FC/iSCSI                  |
| **Sharing**      | Single host            | Multiple clients      | Multiple servers          |
| **Performance**  | Highest                | Moderate              | High                      |
| **Cost**         | Low                    | Moderate              | High                      |
| **Scalability**  | Limited                | Good                  | Excellent                 |
| **Best for**     | Single-server, desktop | File sharing, backups | Databases, enterprise     |
| **Management**   | Simple                 | Moderate              | Complex                   |

---

## RAID (Redundant Array of Independent Disks)

RAID uses multiple disks together to improve **performance**, **reliability**, or both. Different RAID levels offer different trade-offs.

### RAID Levels Overview

| RAID Level  | Technique                     | Min Disks | Usable Capacity | Fault Tolerance     | Performance              |
| :---------- | :---------------------------- | :-------- | :-------------- | :------------------ | :----------------------- |
| **RAID 0**  | Striping                      | 2         | N disks (100%)  | None (0 disk loss)  | Best read/write          |
| **RAID 1**  | Mirroring                     | 2         | N/2 (50%)       | 1 disk failure      | Good read, normal write  |
| **RAID 5**  | Striping + Distributed Parity | 3         | (N-1) disks     | 1 disk failure      | Good read, slower write  |
| **RAID 6**  | Striping + Double Parity      | 4         | (N-2) disks     | 2 disk failures     | Good read, slowest write |
| **RAID 10** | Mirroring + Striping          | 4         | N/2 (50%)       | 1 per mirrored pair | Excellent read/write     |

### RAID 0 (Striping)

```
 Disk 0 Disk 1
 ┌──────────┐ ┌──────────┐
 │ Block 0 │ │ Block 1 │
 │ Block 2 │ │ Block 3 │
 │ Block 4 │ │ Block 5 │
 │ Block 6 │ │ Block 7 │
 └──────────┘ └──────────┘
```

- Data is split (striped) across disks
- **No redundancy** -- if one disk fails, all data is lost
- Best performance (parallel reads/writes)

### RAID 1 (Mirroring)

```
 Disk 0 Disk 1
 ┌──────────┐ ┌──────────┐
 │ Block 0 │ │ Block 0 │ ← Mirror
 │ Block 1 │ │ Block 1 │ ← Mirror
 │ Block 2 │ │ Block 2 │ ← Mirror
 │ Block 3 │ │ Block 3 │ ← Mirror
 └──────────┘ └──────────┘
```

- Every block is duplicated on a second disk
- Can survive one disk failure
- 50% storage overhead

### RAID 5 (Striping with Distributed Parity)

```
 Disk 0 Disk 1 Disk 2
 ┌──────────┐ ┌──────────┐ ┌──────────┐
 │ Block 0 │ │ Block 1 │ │ Parity01 │
 │ Block 2 │ │ Parity23 │ │ Block 3 │
 │ Parity45 │ │ Block 4 │ │ Block 5 │
 └──────────┘ └──────────┘ └──────────┘
```

- Parity is distributed across all disks (no single parity bottleneck)
- Can survive one disk failure (data reconstructed from parity)
- Good balance of performance, capacity, and reliability

### RAID 6 (Double Parity)

- Like RAID 5 but with two parity blocks per stripe
- Can survive **two** simultaneous disk failures
- Higher write penalty (two parity calculations)

### RAID 10 (1+0: Mirroring then Striping)

```
 Disk 0 Disk 1 Disk 2 Disk 3
 ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
 │ Block 0 │ │ Block 0 │ │ Block 1 │ │ Block 1 │
 │ Block 2 │ │ Block 2 │ │ Block 3 │ │ Block 3 │
 └─────────┘ └─────────┘ └─────────┘ └─────────┘
 ← Mirror → ← Mirror →
 ←────── Striped across pairs ──────→
```

- First mirrors, then stripes across mirrored pairs
- Excellent performance and fault tolerance
- 50% storage overhead

---

## Key Points Summary

| Concept | Key Idea                                                |
| :------ | :------------------------------------------------------ |
| DAS     | Direct connection; fastest; single host                 |
| NAS     | Network file sharing; NFS/CIFS; file-level access       |
| SAN     | Dedicated storage network; FC/iSCSI; block-level access |
| RAID 0  | Striping; best performance; no fault tolerance          |
| RAID 1  | Mirroring; survives 1 failure; 50% capacity             |
| RAID 5  | Distributed parity; survives 1 failure; good balance    |
| RAID 6  | Double parity; survives 2 failures                      |
| RAID 10 | Mirror + stripe; excellent performance + reliability    |

---

## Exam Tips

1. **DAS vs NAS vs SAN comparison table** is a very common exam question (5-10 marks). Know the differences in connection type, access level, protocols, and use cases.
2. **RAID levels** are frequently asked. Draw diagrams showing how data and parity are distributed. Know the minimum number of disks, usable capacity formula, and fault tolerance for each level.
3. **NAS protocols** (NFS for Unix, CIFS for Windows) are commonly asked in short-answer questions.
4. **SAN vs NAS** difference: SAN provides block-level access (like a local disk), NAS provides file-level access (like a shared folder). This distinction is critical.
5. **RAID 5 vs RAID 1** comparison is a classic question. RAID 5 is more space-efficient but has slower writes; RAID 1 is simpler but wastes 50% capacity.
6. Know that **iSCSI** runs SCSI over TCP/IP (cheaper alternative to Fibre Channel for SANs).
7. **Host-attached storage interfaces** (IDE, SATA, SCSI, SAS) may be asked as a list with brief descriptions.
8. Remember: RAID is about **reliability and performance**, not about replacing backups. RAID protects against disk failure, not against data corruption or accidental deletion.
