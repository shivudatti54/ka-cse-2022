# File System Mounting - Summary

## Key Definitions

- **Mount Point**: A directory in the existing file system hierarchy where a new file system is attached, making its contents accessible from that location

- **Mounting**: The process of attaching a file system to a specific point in the directory tree, enabling access to files stored on a physical or logical device

- **Virtual File System (VFS)**: An abstraction layer in the kernel that provides a uniform interface for different file system types, allowing them to coexist and be accessed through common operations

- **Unmounting**: The process of detaching a mounted file system from the directory hierarchy after ensuring all pending operations are complete

- **Mount Options**: Parameters that modify the behavior of a mounted file system, such as read-only access or disabling execution of binaries

## Important Formulas

- **Mount Command Syntax** (Unix-like systems):

```
mount -t filesystem_type device mount_point [options]
```

- **fstab Entry Format**:

```
device mount_point filesystem_type options dump fsck
```

## Key Points

1. File system mounting integrates storage devices into the system's directory hierarchy, presenting a unified view of all files regardless of physical location

2. Mount points are typically empty directories (commonly `/mnt`, `/media`, or `/home`) where new file systems become attached

3. The Virtual File System (VFS) layer abstracts file system differences, enabling simultaneous support for multiple file system types (ext4, NTFS, FAT32, NFS, etc.)

4. Automatic mounting detects removable media and mounts them without user intervention, common in modern desktop environments

5. Boot-time mounting is configured through `/etc/fstab`, ensuring critical file systems are available before user processes start

6. Mount options like `ro`, `rw`, `noexec`, `nosuid`, and `noatime` control file system behavior and enhance security

7. Unmounting requires that no processes have open files or working directories within the mounted file system; otherwise, it fails with "device busy"

8. Network file systems (NFS, CIFS) extend mounting concepts to remote file systems, making remote files appear as local directories

## Common Mistakes

1. **Assuming mount point contents are deleted**: The original contents of a mount point are not deleted but become hidden and reappear after unmounting

2. **Ignoring unmount requirements**: Attempting to unmount while processes are using files leads to failures; always check for open files first

3. **Confusing file system with device**: A single device may contain multiple partitions, each with its own file system requiring separate mount operations

4. **Forgetting mount options for security**: Using default mount options without considering security implications (noexec, nosuid) can introduce vulnerabilities
