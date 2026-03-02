# Partition And Mounting

## Introduction

Partition and mounting are fundamental concepts in operating system file management that enable efficient organization and access to secondary storage. A partition is a logical division of a physical storage device (typically a hard disk) into separate sections, each of which can be treated as an independent disk. Each partition can contain a different file system, allowing multiple operating systems to coexist on the same physical device or enabling logical organization of data.

Mounting is the process by which the operating system makes a file system available to users and applications at a specific location in the directory tree. When a file system is mounted, its root directory is attached to a mount point—a directory in the currently accessible directory hierarchy. This mechanism allows users to access files without needing to know the physical details of where the data is stored. The combination of partitioning and mounting provides flexibility, security, and efficient resource utilization in modern computing environments.

## Key Concepts

### Disk Partitioning

A disk partition is a logical slice of physical disk storage. The Master Boot Record (MBR) or GUID Partition Table (GPT) contains partition information at the beginning of the disk. There are three main types of partitions:

1. **Primary Partition**: A bootable partition that can contain an operating system. MBR supports up to four primary partitions. One primary partition can be designated as the active (boot) partition.

2. **Extended Partition**: A special primary partition that serves as a container for logical partitions. Only one extended partition is allowed per disk in MBR scheme. It solves the limitation of four primary partitions by allowing creation of multiple logical partitions.

3. **Logical Partition**: Partitions created within the extended partition. An unlimited number of logical partitions can be created, providing flexibility for multiple file systems and operating systems.

### File System Types

Different operating systems support various file systems, each with distinct characteristics:

- **FAT (File Allocation Table)**: Simple file system used in early systems and removable media. Versions include FAT12, FAT16, and FAT32 with increasing partition size limits.
- **NTFS (New Technology File System)**: Windows NT-based file system supporting compression, encryption, journaling, and access control lists.
- **ext (Extended File System)**: Linux file systems (ext2, ext3, ext4) with journaling support, journaling features in ext3/ext4, and extent-based allocation in ext4.
- **UNIX File Systems**: UFS, ZFS, and other specialized file systems with advanced features like snapshots and data integrity checking.

### Mounting Process

The mounting operation involves several critical steps:

1. **Mount Point Selection**: A directory in the existing directory tree serves as the attachment point. Common mount points include `/mnt`, `/media`, or user-specified directories.

2. **File System Identification**: The kernel identifies the file system type through magic numbers in the superblock or by explicit specification.

3. **Superblock Reading**: The kernel reads the superblock to obtain file system metadata including block size, free blocks, inode information, and file system state.

4. **Mount Data Structure Creation**: A mount table entry is created storing the file system device, mount point, mount options, and file system-specific data.

5. **Directory Entry Integration**: The root directory of the new file system is linked to the mount point, making all files accessible through the directory tree.

### Mount Types

- **Bind Mount**: Mounts a directory or file at another location, maintaining the same underlying data.
- **Remote Mount**: Network-based mounting using protocols like NFS (Network File System) or SMB/CIFS.
- **Loop Mount**: Mounting an image file as if it were a block device, useful for ISO images and virtual disks.

### Unmounting

Unmounting safely disconnects a file system from the directory tree. The `umount` command in Unix-like systems performs this operation. The kernel ensures all pending writes are completed and no processes are using files in the mounted file system before completion.

## Examples

### Example 1: Linux Disk Partitioning Scenario

Consider a 500 GB hard disk to be partitioned for a dual-boot system:

```
Partition Table:
/dev/sda1 - 100 GB - Windows (NTFS) - Primary, Bootable
/dev/sda2 - 100 GB - Linux /boot (ext4) - Primary
/dev/sda3 - Extended Partition - Remaining 300 GB
/dev/sda5 - 150 GB - Linux / (ext4) - Logical
/dev/sda6 - 100 GB - Linux /home (ext4) - Logical
/dev/sda7 - 50 GB - Swap Space - Logical
```

Commands to create and mount:
```bash
# Create file system
mkfs.ext4 /dev/sda5
mkfs.ext4 /dev/sda6
mkswap /dev/sda7

# Mount file systems
mount /dev/sda5 /mnt/root
mount /dev/sda6 /mnt/home

# Add to /etc/fstab for automatic mounting
/dev/sda5 / ext4 defaults 0 1
/dev/sda6 /home ext4 defaults 0 2
```

### Example 2: Mounting ISO Image

Mounting an ISO image as a loop device:
```bash
# Create mount point
mkdir -p /mnt/iso

# Mount ISO image
mount -o loop /path/to/image.iso /mnt/iso

# Verify mounting
ls -la /mnt/iso/

# Unmount when done
umount /mnt/iso
```

### Example 3: Windows Drive Letter Assignment

In Windows, partitions are assigned drive letters:
- `C:` typically represents the primary partition with the operating system
- Additional partitions receive subsequent letters (D:, E:, etc.)
- Removable media receive letters dynamically based on insertion order
- Mount points can be created using Disk Management to assign partitions to empty folders

## Exam Tips

1. **Understand MBR vs GPT**: Remember MBR supports maximum 2TB partitions and 4 primary partitions, while GPT supports up to 256 primary partitions and partitions larger than 2TB.

2. **Mount Point Concept**: The mount point must be an existing directory. The original contents become invisible until unmounting, not deleted.

3. **Boot Process Connection**: The boot loader reads the partition table to locate the bootable partition, then mounts the root file system to begin the operating system loading process.

4. ** journaling File Systems**: Modern file systems like ext3, ext4, NTFS use journaling to ensure file system consistency after crashes, recording transactions before execution.

5. **Swap vs Mount**: Swap space is not a mounted file system but a raw partition used for virtual memory, managed by the memory manager rather than the file system.

6. **Mount Options**: Remember common mount options like `ro` (read-only), `rw` (read-write), `noexec` (no binary execution), and `nosuid` (ignore setuid bits).

7. **File System Mount Sequence**: During boot, the root filesystem is mounted first (initially as read-only), then checked by fsck, and remounted as read-write before switching to multi-user mode.