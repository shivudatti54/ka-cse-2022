# fchdir() and getcwd() Functions, Device Special Files - Summary

## Key Definitions and Concepts

- **Working Directory**: The directory associated with a process that serves as the reference point for resolving relative pathnames.

- **fchdir()**: System call that changes the current working directory to the directory referenced by an open file descriptor. Prototype: `int fchdir(int fd)`.

- **getcwd()**: Function that returns the absolute pathname of the current working directory. Prototype: `char *getcwd(char *buf, size_t size)`.

- **Device Special Files**: Special files in Unix/Linux that provide an interface between user programs and hardware devices.

- **Character Device**: Device accessed character-by-character without buffering (e.g., keyboard, terminal).

- **Block Device**: Device accessed in fixed-size blocks with buffering (e.g., hard disk, CD-ROM).

## Important Formulas and Theorems

- Device number encoding: `dev_t dev = makedev(major, minor)`
- Extracting device numbers: `major(dev)` and `minor(dev)`
- Character device file type: `S_IFCHR` (or `S_ISCHR(st.st_mode)`)
- Block device file type: `S_IFBLK` (or `S_ISBLK(st.st_mode)`)

## Key Points

- fchdir() requires an open file descriptor pointing to a directory; it fails with ENOTDIR if applied to a regular file.

- getcwd() returns NULL on failure with errno set to ERANGE if buffer is too small, or EINVAL if buf is NULL.

- The get_current_dir_name() function dynamically allocates memory and should be freed after use.

- Character devices transfer data one byte at a time; block devices use fixed-size blocks.

- Major device number identifies the device driver; minor number identifies the specific device instance.

- Device special files are created using mknod() with appropriate file type flags (S_IFCHR or S_IFBLK).

- In ls -l output, character devices show 'c' and block devices show 'b' as the first character of permissions.

- The dirfd() function returns the file descriptor associated with a DIR\* stream.

## Common Mistakes to Avoid

1. **Passing regular file descriptor to fchdir()**: Remember fchdir() only works with directory file descriptors; it will fail with ENOTDIR otherwise.

2. **Buffer size issues with getcwd()**: Not allocating sufficient buffer size leads to ERANGE errors; use PATH_MAX from `<limits.h>`.

3. **Confusing device types**: Not distinguishing between character and block devices, which have different I/O characteristics.

4. **Forgetting to close directories**: After using fchdir(), the directory file descriptor remains open and must be closed separately.

5. **Permission issues**: Creating device files requires appropriate privileges; regular users cannot create device files in /dev.

## Revision Tips

1. Practice writing code using both fchdir() and getcwd() together to understand their relationship.

2. Remember that fchdir() is useful when you already have a directory open (e.g., from opendir()).

3. Review the difference between absolute paths (resolved from root) and relative paths (resolved from current working directory).

4. Use `ls -l /dev` to see examples of character (c) and block (b) device files in a Unix system.

5. Remember that device files in /dev are typically created by the system or with root privileges using mknod or appropriate device management tools.
