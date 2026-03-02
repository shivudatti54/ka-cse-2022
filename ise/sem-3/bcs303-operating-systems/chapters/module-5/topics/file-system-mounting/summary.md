# File System Mounting - Summary

## Key Definitions and Concepts

- **File System Mounting**: The process of attaching a file system to a specific location (mount point) in the operating system's directory tree, making it accessible to users and applications.

- **Mount Point**: A directory in the existing file system hierarchy where a new file system is attached. When mounted, the original contents of this directory become temporarily hidden.

- **Virtual File System (VFS)**: A kernel layer that provides a unified interface allowing different file system types (ext4, NTFS, FAT, NFS) to be accessed through standard system calls.

- **Unmounting**: The reverse operation of mounting that flushes data buffers and detaches the file system from the directory tree.

## Important Formulas and Commands

- Linux mount command: `mount -t type device mount_point`
- Linux unmount command: `umount mount_point` or `umount device`
- fstab entry format: `device mount_point type options dump fsck`

## Key Points

- File system mounting enables multiple storage devices to appear as a unified directory tree to users.

- The root file system is mounted by the kernel during boot; all other file systems mount afterward.

- Automatic mounting occurs via /etc/fstab configuration or desktop environment auto-mount features.

- Mount options like 'ro' (read-only) and 'rw' (read-write) control access permissions.

- Proper unmounting is critical to prevent data loss from unwritten buffers.

- Virtual File Systems abstract underlying file system differences, allowing diverse storage types to coexist.

- Network file systems (NFS, SMB) require mounting just like local physical devices.

## Common Mistakes to Avoid

- Attempting to unmount while files are still open can cause data corruption.

- Forgetting that mounting hides existing mount point contents (a common exam trick question).

- Confusing device names (like /dev/sda1) with mount points (like /mnt/data).

- Not understanding that mount operations require appropriate privileges (root or sudo in Linux).

## Revision Tips

- Practice reading and creating /etc/fstab entries as this is commonly tested in practical exams.

- Understand the sequence of boot process related to file system mounting.

- Remember that mounting is logical (software) rather than physical connection.

- Review differences between how Windows (drive letters) and Linux (directory-based) handle file system organization.