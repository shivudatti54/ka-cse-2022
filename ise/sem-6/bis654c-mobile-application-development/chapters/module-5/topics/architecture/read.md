# Virtual Machine Architecture

## What is a Virtual Machine?

A **Virtual Machine (VM)** is a software-based emulation of a physical computer. It runs an operating system and applications just like a physical machine, but shares the underlying hardware with other VMs through a hypervisor.

## VM Components

### 1. Virtual CPU (vCPU)

The vCPU represents processing power allocated to a VM.

```
Physical CPU (8 cores)
├── VM1: 2 vCPUs
├── VM2: 4 vCPUs
├── VM3: 2 vCPUs
└── VM4: 2 vCPUs (oversubscribed)
```

**Key Concepts:**
- **vCPU**: Virtual processor allocated to a VM
- **CPU Affinity**: Binding vCPUs to specific physical cores
- **CPU Oversubscription**: More vCPUs than physical cores
- **CPU Scheduling**: How hypervisor allocates CPU time

### 2. Virtual Memory

Memory allocation and management for VMs.

**Memory Allocation:**
- **Static Allocation**: Fixed amount of RAM assigned
- **Dynamic Memory**: RAM adjusts based on demand
- **Memory Overcommitment**: Total VM RAM > physical RAM

**Memory Optimization Techniques:**
- **Memory Ballooning**: Reclaim unused memory from VMs
- **Transparent Page Sharing (TPS)**: Deduplicate identical pages
- **Memory Compression**: Compress pages before swapping
- **Swap to Disk**: Use disk when RAM is exhausted

### 3. Virtual Storage

```
Virtual Disk Types:
┌─────────────────────────────────────────────┐
│ Thick Provisioned (Eager Zeroed)            │
│ - Full space allocated immediately          │
│ - Best performance                          │
│ - No growth overhead                        │
├─────────────────────────────────────────────┤
│ Thick Provisioned (Lazy Zeroed)             │
│ - Full space allocated                      │
│ - Zeroed on first write                     │
│ - Good performance                          │
├─────────────────────────────────────────────┤
│ Thin Provisioned                            │
│ - Grows as data is written                  │
│ - Storage efficient                         │
│ - Slight performance overhead               │
└─────────────────────────────────────────────┘
```

**Virtual Disk Formats:**
| Format | Platform | Description |
|--------|----------|-------------|
| VMDK | VMware | Virtual Machine Disk |
| VHD/VHDX | Microsoft | Virtual Hard Disk |
| QCOW2 | KVM/QEMU | QEMU Copy-On-Write |
| VDI | VirtualBox | VirtualBox Disk Image |
| RAW | Multiple | Unformatted disk image |

### 4. Virtual Network

```
VM Network Architecture:
┌──────────┐     ┌──────────┐     ┌──────────┐
│   VM1    │     │   VM2    │     │   VM3    │
│  vNIC    │     │  vNIC    │     │  vNIC    │
└────┬─────┘     └────┬─────┘     └────┬─────┘
     │               │                │
     └───────────────┼────────────────┘
                     ▼
          ┌──────────────────┐
          │  Virtual Switch  │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │  Physical NIC    │
          └──────────────────┘
```

**Network Components:**
- **vNIC (Virtual Network Interface Card)**: Emulated network adapter
- **Virtual Switch**: Software switch connecting VMs
- **Port Groups**: Logical grouping for network policies
- **VLAN Tagging**: Network segmentation

## VM Configuration Files

### VMware (.vmx, .vmdk)
```
# Example .vmx configuration
config.version = "8"
virtualHW.version = "19"
displayName = "WebServer"
guestOS = "ubuntu-64"
memSize = "4096"
numvcpus = "2"
scsi0.virtualDev = "lsilogic"
scsi0:0.fileName = "WebServer.vmdk"
ethernet0.virtualDev = "vmxnet3"
ethernet0.networkName = "VM Network"
```

### Hyper-V Configuration
- `.xml` - VM configuration
- `.vhdx` - Virtual hard disk
- `.avhdx` - Differencing disk (snapshots)

### KVM/libvirt (XML)
```xml
<domain type='kvm'>
  <name>webserver</name>
  <memory unit='GiB'>4</memory>
  <vcpu>2</vcpu>
  <os>
    <type arch='x86_64'>hvm</type>
  </os>
  <devices>
    <disk type='file' device='disk'>
      <source file='/var/lib/libvirt/images/webserver.qcow2'/>
      <target dev='vda' bus='virtio'/>
    </disk>
  </devices>
</domain>
```

## VM Lifecycle States

```
           ┌─────────────┐
           │   Created   │
           └──────┬──────┘
                  ▼
           ┌─────────────┐
    ┌──────│   Powered   │──────┐
    │      │     Off     │      │
    │      └──────┬──────┘      │
    │             ▼             │
    │      ┌─────────────┐      │
    │      │   Running   │◄─────┤
    │      └──────┬──────┘      │
    │             ▼             │
    │      ┌─────────────┐      │
    │      │  Suspended  │──────┘
    │      └─────────────┘
    ▼
┌─────────────┐
│   Deleted   │
└─────────────┘
```

**States:**
- **Created**: VM defined but never started
- **Powered Off**: VM exists but not running
- **Running**: VM actively executing
- **Suspended**: VM state saved to disk (paused)

## VM Migration

### Live Migration (vMotion, Live Migration)
Moving a running VM between hosts without downtime.

**Requirements:**
- Shared storage between hosts
- Compatible CPUs
- Network connectivity
- Sufficient resources on destination

### Cold Migration
Moving a powered-off VM between hosts or storage.

### Storage Migration
Moving VM disk files between datastores while running.

## Snapshots

```
Snapshot Chain:
┌────────────────┐
│  Base Disk     │
│  (Original)    │
└───────┬────────┘
        ▼
┌────────────────┐
│  Snapshot 1    │
│  (Delta 1)     │
└───────┬────────┘
        ▼
┌────────────────┐
│  Snapshot 2    │
│  (Delta 2)     │
└───────┬────────┘
        ▼
┌────────────────┐
│  Current State │
│  (Active)      │
└────────────────┘
```

**Snapshot Contents:**
- Memory state (optional)
- Disk state (delta/differencing disk)
- VM configuration

**Best Practices:**
- Use for short-term purposes (testing, updates)
- Don't use as backup solution
- Limit snapshot chain depth
- Delete snapshots after use

## Summary

- VMs consist of virtual CPU, memory, storage, and network components
- Virtual disks can be thick or thin provisioned
- VM states include created, powered off, running, and suspended
- Live migration enables moving VMs without downtime
- Snapshots capture point-in-time VM state for recovery
