# Partition And Mounting - Summary

## Key Definitions

- **Partition**: A logical division of a physical disk into independent sections, each functioning as a separate disk.
- **Mount Point**: A directory in the existing file system hierarchy where a new file system is attached.
- **Mounting**: The process of making a file system available at a specific location in the directory tree.
- **Master Boot Record (MBR)**: The first sector of a storage device containing the partition table and boot loader code.
- **GUID Partition Table (GPT)**: Modern partition scheme supporting larger disks and more partitions than MBR.
- **File System**: The method and data structure used by the operating system to control how data is stored and retrieved.

## Important Formulas

- **Maximum Partitions (MBR)**: 4 primary partitions OR 3 primary + 1 extended (containing unlimited logical partitions)
- **Maximum Partition Size (MBR)**: 2 TB (due to 32-bit addressing with 512-byte sectors)
- **Boot Process Sequence**: BIOS/UEFI → MBR/GPT → Boot Loader → Kernel → Mount Root FS → Init Process

## Key Points

1. Partitioning enables multiple operating systems and file systems on a single physical disk.

2. The boot sector contains critical code for system startup and partition table information.

3. Different file systems (NTFS, ext4, FAT32) offer varying features like journaling, compression, and access control.

4. Mounting integrates file systems into the unified directory tree, hiding physical storage details from users.

5. The `/etc/fstab` file in Unix systems configures automatic mounting of file systems at boot time.

6. Unmounting requires all files to be closed and no processes accessing the mounted file system.

7. Modern systems use GPT for disks larger than 2TB and support for UEFI booting.

8. Virtual file systems (VFS) provide abstraction allowing different file system types to coexist.

## Common Mistakes

1. **Confusing Partition with File System**: A partition is storage space; a file system is the method of organizing data within that partition.

2. **Forgetting to Create Mount Point**: Attempting to mount without an existing directory causes mount failure.

3. **Not Unmounting Before Removal**: Removing mounted removable media without unmounting can cause data loss.

4. **Incorrect fstab Configuration**: Syntax errors in `/etc/fstab` can prevent system from booting properly.

5. **Overlooking Swap Partition**: Failing to configure swap can cause memory exhaustion issues in systems with limited RAM.