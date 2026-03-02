# File System Architecture

## Layered Design

Modern file systems employ a **layered (or hierarchical) architecture** that separates concerns and provides clear interfaces between components. This design principle enables modularity, portability, and maintainability.

### Layer Hierarchy

```
┌─────────────────────────────────────┐
│ Application Programs │
├─────────────────────────────────────┤
│ Logical File System (Interface) │
├─────────────────────────────────────┤
│ File Organization Module │
├─────────────────────────────────────┤
│ Basic File System (Device Drivers)│
├─────────────────────────────────────┤
│ I/O Control (Device Controllers) │
├─────────────────────────────────────┤
│ Physical Devices │
└─────────────────────────────────────┘
```

## Layer Responsibilities

### Logical File System Layer

The **Logical File System** provides the user-visible file system interface, managing:

- File naming and directory management
- Metadata operations (getattr, setattr)
- Directory structure maintenance
- Protection and security enforcement

This layer maintains the **File Control Block (FCB)**, a data structure containing file attributes, permissions, and pointers to file data blocks. In Unix systems, the FCB corresponds to the **inode** structure.

### File Organization Module Layer

This layer implements logical-to-physical block mapping:

- Translates logical file offsets to physical disk blocks
- Manages free space allocation
- Implements file allocation methods (contiguous, linked, indexed)
- Handles free block tracking via bitmaps or free lists

### Basic File System Layer

The **Basic File System** issues generic I/O commands:

- Read/write logical blocks
- Buffer management
- Block allocation requests
- Interfaces with device drivers

This layer is device-independent, abstracting hardware specifics.

### I/O Control Layer

The **I/O Control** layer comprises:

- Device drivers specific to hardware controllers
- Interrupt handling routines
- DMA (Direct Memory Access) management
- Device-specific command translation

## Critical Data Structures

### File Control Block (FCB)/Inode

The FCB contains:

- File type and permissions (mode)
- Owner and group identifiers
- File size in bytes
- Timestamps (access, modification, creation)
- Block pointers (direct, indirect, double-indirect)
- Reference count

### Boot Control Block

Contains bootstrap loader code and information required to boot the operating system from the volume. Located at a fixed position (first sector in many systems).

### Volume Control Block (Superblock)

Maintains file system metadata:

- Total block count and free block count
- Inode count and free inode list
- Block size and allocation unit
- File system state and integrity information

## Implementation Considerations

The layered architecture provides several benefits:

- **Abstraction**: Each layer hides implementation details from layers above
- **Modularity**: Layers can be modified independently
- **Portability**: Device-independent interfaces simplify cross-platform development
- **Maintainability**: Bugs can be isolated to specific layers

Key implementation decisions include:

- Allocation strategy selection (contiguous, linked, indexed)
- Directory implementation (linear list, hash table, B-tree)
- Free space management approach
- Caching and buffering policies
