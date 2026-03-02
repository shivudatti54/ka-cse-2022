# File System Mounting - Summary

## Key Definitions and Concepts

- **File System Mounting**: The process of attaching a file system to a specific location in the directory tree, making it accessible to users and applications

- **Mount Point**: A directory in the existing file system hierarchy where a new file system is attached. Access to this directory redirects to the mounted file system

- **Mount Table**: A kernel data structure that maintains records of all currently mounted file systems, including device, mount point, file system type, and options

- **Root File System**: The primary file system mounted at "/" during boot, from which all other file systems are accessible

- **Static Mounting**: File systems automatically mounted at boot time based on configuration files like /etc/fstab

- **Dynamic Mounting**: File systems mounted on-demand during system operation, typically for removable media or network shares

- **Unmount**: The operation that detaches a file system from the mount point, flushing pending writes and releasing resources

## Important Commands and Syntax

- **Unix mount command**: mount -t type device mount_point
- **Unix unmount command**: umount device_or_mount_point
- **View mount table**: cat /proc/mounts or mount command
- **/etc/fstab fields**: device, mount_point, type, options, dump, fsck

## Key Points

- File system mounting enables multiple storage devices to appear as a unified directory tree

- The mount operation validates the file system, updates the mount table, and establishes driver connection

- The Virtual File System (VFS) layer provides a common interface that allows different file system types to coexist

- Root file system is the first file system mounted and contains essential system directories

- Removable media are typically dynamically mounted when inserted, removed when ejected

- Unmount can fail if files are open or processes have working directories in the mounted file system

- Each mounted file system appears as a subtree in the global directory hierarchy

## Common Mistakes to Avoid

- Confusing mount point (directory) with device (physical storage) - these are distinct entities

- Forgetting to unmount before removing removable media, which can cause data loss

- Assuming mounting always succeeds - file system must be valid and mount point must exist

- Confusing file system type with partition - a partition is the storage space, file system is the organization method

## Revision Tips

- Draw the hierarchy showing how multiple file systems connect to the root

- Memorize the mount command syntax with its components: type, device, mount_point

- Practice reading /etc/fstab entries to understand static mounting configuration

- Review the boot sequence to understand when and how root file system is mounted first