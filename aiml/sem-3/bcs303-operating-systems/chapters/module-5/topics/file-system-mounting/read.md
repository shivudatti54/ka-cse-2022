# File System Mounting

## Introduction

File system mounting is a fundamental operating system concept that enables the operating system to make various storage devices and their file systems accessible to users and applications. When you connect a USB drive, insert a CD, or start your computer, the operating system performs mounting operations behind the scenes to integrate these storage resources into the unified file system hierarchy. Without mounting, each storage device would exist in isolation, making it impossible to access files across different drives and partitions through a consistent interface.

The mount operation essentially tells the operating system that a particular file system is ready to be accessed and should be attached to the existing directory tree at a specified location called the mount point. This process is crucial for maintaining the illusion of a single, seamless file system even when multiple physical and logical storage devices are present. Modern operating systems support various file system types including FAT32, NTFS, ext4, XFS, and many others, each with its own internal structure and organization. The mounting mechanism provides an abstraction layer that allows the OS to handle these diverse file systems transparently, enabling users to interact with files regardless of where they are physically stored.

In the context of the University of Delhi's Computer Science curriculum, understanding file system mounting is essential for comprehending how operating systems manage secondary storage and provide file access capabilities. This knowledge forms the foundation for advanced topics in system administration, storage management, and operating system design. The concepts learned here directly apply to real-world scenarios that students will encounter in their professional careers, from configuring servers to troubleshooting system issues.

## Key Concepts

### Mount Point

A mount point is a directory in the existing file system hierarchy where a new file system is attached or "mounted." When a file system is mounted at a particular directory, any access to that directory or its subdirectories will be redirected to the mounted file system. In Unix-like systems, the root directory "/" is the mount point for the root file system, while other file systems are typically mounted under directories like /mnt, /media, or /home. For example, when you insert a USB drive in Linux, it might be automatically mounted at /media/username/usb-drive.

The mount point directory typically exists in the parent file system before mounting occurs. If the mount point directory contains any files or subdirectories, they become hidden and inaccessible as long as the new file system is mounted at that point. This behavior is important to understand because it means mounting can effectively "overlay" existing directory contents. In Windows, mount points work differently as each partition gets its own drive letter (C:, D:, E:), though modern Windows also supports directory-based mount points through the mountvol command or disk management utilities.

### Mount Operation

The mount operation is the system call or command that attaches a file system to a specific mount point. In Unix-like systems, the mount command follows the syntax: mount -t type device mount_point. For example, mounting a USB drive formatted with FAT32 would require: mount -t vfat /dev/sdb1 /mnt/usb. The operating system performs several critical steps during mounting: it validates the file system by reading its superblock, verifies the file system is compatible and not already mounted, updates the mount table (or mount hash table in Unix), and establishes the connection between the file system driver and the physical storage device.

The mount system call takes several parameters including the device name (representing the physical or logical storage device), the mount point directory path, the file system type, and optional flags that specify mounting behavior such as read-only (O_RDONLY) or read-write (O_RDWR). Modern operating systems also support bind mounts, which allow mounting a directory to multiple locations, and loop devices, which enable mounting image files as if they were physical devices. These advanced mounting techniques are particularly useful in containerization and virtualization environments.

### Mount Table

The mount table, also known as the mount table or vfstable in different operating systems, is a kernel data structure that maintains records of all currently mounted file systems. Each entry in the mount table contains essential information including the mounted device, the mount point path, the file system type, mount options, and the time of mounting. The kernel uses this table to translate file system operations from virtual file system layer to the appropriate file system-specific implementation.

In Linux, the /proc/mounts or /etc/mtab file provides a view of the current mount table, allowing administrators to see all mounted file systems and their properties. The mount table is crucial for the virtual file system (VFS) layer, which provides a unified interface for file operations regardless of the underlying file system type. When a process attempts to access a file, the VFS layer consults the mount table to determine which file system driver should handle the request. This abstraction is what enables Linux and other Unix-like systems to support numerous file system types simultaneously.

### Root File System

The root file system is the primary file system that is mounted at the "/" directory during system boot. All other file systems are mounted relative to this root file system, either directly or through mount points within it. The root file system must contain essential system directories and files needed for the operating system to function, including /bin, /etc, /lib, /usr, and /sbin. Without a properly mounted root file system, the system cannot boot or provide any meaningful services.

In systems with multiple partitions or storage devices, the root file system is typically specified in the bootloader configuration (such as GRUB in Linux) through its device identifier. The root file system can also be mounted in different modes: read-write for normal operation or read-only for recovery and maintenance tasks. When troubleshooting system issues, mounting the root file system as read-only can prevent further damage while allowing examination of system files. Embedded systems often use a minimal root file system (initramfs) loaded into memory during boot, which then mounts the actual root file system from storage.

### Unmount Operation

The unmount operation is the reverse of mounting and detaches a file system from the mount point, making it inaccessible to processes. In Unix-like systems, the umount command is used: umount /mnt/usb or umount /dev/sdb1. The unmount operation is critical for ensuring data integrity, as it forces the file system to flush any pending writes to storage and update metadata. Before unmounting, the operating system ensures that no processes are actively using files on that file system.

Unmounting can fail if files on the file system are still open or if processes have their working directories within the mounted file system. The lazy unmount option (umount -l) detaches the file system from the hierarchy immediately but cleans up references only when they are no longer in use. This is useful for safely removing external drives without waiting for all processes to close files. Windows uses the "Safely Remove Hardware" feature to ensure data is written before disconnecting storage devices, similar in purpose to the unmount operation.

### Dynamic and Static Mounting

Static mounting refers to file systems that are automatically mounted at system boot time based on configuration files like /etc/fstab in Linux or the Registry in Windows. These configurations specify which file systems should be mounted, at which mount points, and with what options. Static mounting ensures that essential file systems like /home, /boot, and swap partitions are available when the system starts. The /etc/fstab file contains fields for the device, mount point, file system type, options, dump frequency, and fsck order.

Dynamic mounting occurs when file systems are mounted and unmounted during system operation, typically in response to user actions or automated scripts. Removable media like USB drives and memory cards are usually dynamically mounted when inserted, using desktop environment tools or the udev subsystem in Linux. Network file systems such as NFS and CIFS are also dynamically mounted when needed, often through automount daemons that mount shares on-demand. This approach conserves system resources and network bandwidth by only connecting to file systems when they are actually accessed.

## Examples

### Example 1: Mounting a USB Drive in Linux

Consider a scenario where you have a USB drive with device name /dev/sdb1 formatted with the ext4 file system, and you want to access its contents at /mnt/usb.

Step 1: Create the mount point directory if it doesn't exist:
mkdir -p /mnt/usb

Step 2: Mount the file system:
mount /dev/sdb1 /mnt/usb

Step 3: Verify the mount was successful:
df -h | grep sdb1
mount | grep sdb1

Step 4: Access the files:
ls -la /mnt/usb

Step 5: After use, unmount the file system:
umount /mnt/usb

The df command shows the file system usage, and mount | grep filters for our specific device. The unmount operation flushes all buffered data and releases the device, allowing safe physical removal.

### Example 2: Configuring Static Mount in /etc/fstab

Suppose you have an additional hard drive at /dev/sda2 that should be mounted at /data whenever the system boots. You would add the following line to /etc/fstab:

/dev/sda2    /data    ext4    defaults    0    2

The six fields in /etc/fstab are:
- Device: /dev/sda2 (the partition to mount)
- Mount point: /data (where to attach it)
- File system type: ext4
- Options: defaults (rw, suid, dev, exec, auto, nouser, async)
- Dump: 0 (not backed up by dump utility)
- Fsck: 2 (check after root file system)

After saving the file, you can test the configuration with: mount -a (mounts all file systems mentioned in fstab that are not already mounted).

### Example 3: Windows Drive Mounting

In Windows, mounting a new volume is simpler but conceptually similar. When you connect a new hard drive:

1. Open Disk Management (diskmgmt.msc)
2. Right-click on the unallocated space
3. Select "New Simple Volume"
4. Follow the wizard to assign a drive letter (e.g., E:) or mount it as a folder path

If mounting as a folder path, you choose an existing NTFS volume and specify an empty folder as the mount point. This creates a directory junction rather than a traditional mount, but serves the same purpose of integrating another volume into the file system hierarchy.

## Exam Tips

For DU semester examinations, focus on the following key areas:

1. Understand the difference between mount point and device - the mount point is the directory while the device is the storage medium. This distinction frequently appears in exam questions.

2. Know the sequence of operations during mount: validate file system → check permissions → update mount table → establish driver connection. Understanding this flow demonstrates conceptual clarity.

3. Remember that the root file system is mounted first during boot, and all other file systems are mounted relative to it. This hierarchical relationship is crucial for understanding file system architecture.

4. The mount table is the kernel data structure that maintains information about all mounted file systems - be able to explain what information it contains.

5. Difference between static mounting (via /etc/fstab) and dynamic mounting (on-demand) is important - know examples of each.

6. Unmount can fail if files are open - this is a practical consideration that may appear in troubleshooting scenarios.

7. Virtual File System (VFS) layer concept is essential - it provides the abstraction that allows different file systems to coexist through a common interface.

8. Practice drawing diagrams showing the relationship between user applications, system calls, VFS, file system drivers, and physical devices.

9. Know common file system types (FAT, NTFS, ext4) and their characteristics, as file system type is a parameter in mounting.

10. The mount command syntax in Unix-like systems is frequently tested: mount -t type device mount_point. Memorize this format.