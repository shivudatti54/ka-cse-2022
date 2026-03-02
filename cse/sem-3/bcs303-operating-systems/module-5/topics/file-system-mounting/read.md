# File System Mounting

## Introduction

A file system must be **mounted** before it can be accessed by processes. Mounting is the process of making a file system available at a specific location in the directory tree. Just as a program must be loaded into memory before it can execute, a file system stored on a disk partition must be mounted before files on it can be accessed.

This topic corresponds to **Section 11.5** of Silberschatz (Operating System Concepts).

## What is Mounting?

When the OS mounts a file system, it:

1. Verifies the file system on the device is valid (checks the format and metadata)
2. Records in its data structures that a file system is mounted at a specific **mount point**
3. Makes the files and directories of that file system accessible through the mount point

The **mount point** is an empty directory in the existing directory tree where the new file system is attached.

```
Before Mounting:

 / (root file system on disk 1)
 ├── bin/
 ├── home/
 │ └── alice/
 ├── tmp/
 └── mnt/ ← empty directory (mount point)

 USB drive (disk 2) has its own file system:
 photos/
 ├── vacation.jpg
 └── family.jpg
 documents/
 └── resume.pdf

After Mounting USB at /mnt:

 / (root file system)
 ├── bin/
 ├── home/
 │ └── alice/
 ├── tmp/
 └── mnt/ ← mount point
 ├── photos/
 │ ├── vacation.jpg
 │ └── family.jpg
 └── documents/
 └── resume.pdf
```

After mounting, accessing `/mnt/photos/vacation.jpg` reads from the USB drive's file system.

## The Mount Table

The OS maintains a **mount table** that records information about each mounted file system:

| Field                | Description                                                    |
| :------------------- | :------------------------------------------------------------- |
| **Device**           | The storage device (disk partition) containing the file system |
| **File system type** | The format of the file system (ext4, NTFS, FAT32, etc.)        |
| **Mount point**      | The directory where the file system is attached                |
| **Mount options**    | Flags such as read-only, no-exec, etc.                         |

```
Mount Table Example:

| Device | Type | Mount Point | Options |
|------------|-------|-------------|------------|
| /dev/sda1 | ext4 | / | rw |
| /dev/sda2 | ext4 | /home | rw |
| /dev/sdb1 | vfat | /mnt/usb | rw,noexec |
| /dev/sr0 | iso9660| /media/cdrom| ro |
```

## Mount Process

### Step 1: Verify the File System

The OS reads the **superblock** (or equivalent metadata) from the device to determine the file system type and verify its integrity.

### Step 2: Check the Mount Point

The mount point must be an existing directory, typically an empty one. If the directory is not empty, its existing contents become **hidden** (inaccessible) until the file system is unmounted.

### Step 3: Update the Mount Table

The OS adds an entry to its mount table, recording the device-to-mount-point mapping.

### Step 4: Enable Access

The OS links the root of the mounted file system to the mount point directory. Any path traversal that reaches the mount point is redirected to the mounted file system.

## Mounting in Different Operating Systems

### UNIX/Linux

In UNIX/Linux, all file systems are mounted into a **single unified directory tree** rooted at `/`. There are no drive letters.

```bash
# Mount a USB drive
mount /dev/sdb1 /mnt/usb

# Mount with specific file system type
mount -t ntfs /dev/sdc1 /mnt/windows

# Mount as read-only
mount -o ro /dev/sr0 /media/cdrom

# View all mounted file systems
mount
# or
df -h

# Unmount a file system
umount /mnt/usb
```

The file `/etc/fstab` contains entries for file systems that should be mounted automatically at boot:

```
# /etc/fstab
# device mount-point type options dump pass
/dev/sda1 / ext4 defaults 0 1
/dev/sda2 /home ext4 defaults 0 2
/dev/sda3 swap swap defaults 0 0
```

### Windows

Windows uses **drive letters** (C:, D:, E:, etc.) instead of mount points. Each partition is assigned a letter. However, Windows also supports mounting volumes at NTFS directory mount points (similar to UNIX).

```
C:\ → Primary partition (Windows OS)
D:\ → Second partition or CD-ROM
E:\ → USB drive
```

### macOS

macOS automatically mounts removable devices under `/Volumes/`:

```
/Volumes/USB_DRIVE/
/Volumes/External_HD/
```

## Boot Mounting

At boot time, the **root file system** is mounted first. The boot loader identifies the root partition, and the kernel mounts it at `/`. Other file systems listed in `/etc/fstab` (or equivalent) are then mounted at their designated mount points during the boot process.

```
Boot Sequence:
1. BIOS/UEFI loads boot loader
2. Boot loader loads kernel from boot partition
3. Kernel mounts root file system at /
4. Kernel starts init process
5. Init reads /etc/fstab and mounts remaining file systems
```

## Unmounting

**Unmounting** detaches a file system from the directory tree. Before unmounting, the OS must ensure:

1. **No files are open** on that file system
2. **No process** has its current working directory within that file system
3. All **buffered writes** are flushed to disk

If any of these conditions are not met, the unmount fails (the file system is "busy").

```
$ umount /mnt/usb
umount: /mnt/usb: target is busy.
# A process still has files open on the USB drive
```

## Virtual File System (VFS) and Mounting

The **Virtual File System (VFS)** layer in UNIX/Linux provides a uniform interface for all file systems, regardless of their type. When a file system is mounted, the VFS:

1. Reads the file system's superblock
2. Creates a VFS superblock object in memory
3. Links the mounted file system's root inode to the mount point
4. Routes all subsequent file operations through the appropriate file system driver

```
Application
 |
 v
 VFS Layer (uniform interface)
 |
 +----------+----------+----------+
 | | | |
 ext4 NTFS FAT32 NFS
 driver driver driver driver
 | | | |
 /dev/sda1 /dev/sdb1 /dev/sdc1 network
```

## Summary

| Concept      | Key Point                                                            |
| :----------- | :------------------------------------------------------------------- |
| Mounting     | Attaching a file system to a directory in the existing tree          |
| Mount point  | Directory where the file system becomes accessible                   |
| Mount table  | OS data structure tracking all mounted file systems                  |
| `/etc/fstab` | Configuration file for automatic mounting at boot (UNIX/Linux)       |
| Root mount   | Root file system is the first to be mounted during boot              |
| Unmounting   | Detach file system; fails if files are open or directory is in use   |
| VFS          | Uniform interface that supports mounting different file system types |

## Exam Tips

1. **Explain the mount process** — Be able to describe the steps: verify file system, check mount point, update mount table, enable access.
2. **Draw before/after mounting diagrams** — Show how a separate file system becomes part of the directory tree at the mount point. This is a common diagram question.
3. **UNIX vs Windows** — Know that UNIX uses a single directory tree with mount points, while Windows uses drive letters. may ask for a comparison.
4. **Boot mounting** — Know that the root file system is mounted first, and `/etc/fstab` handles the rest.
5. **Why unmount can fail** — "Target is busy" — open files or processes with current directory on that file system.
6. **VFS** — Mention that the Virtual File System layer makes mounting different file system types possible through a uniform interface.
