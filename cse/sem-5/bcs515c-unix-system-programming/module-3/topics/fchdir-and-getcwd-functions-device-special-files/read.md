# fchdir() and getcwd() Functions, Device Special Files

## Introduction

In Unix/Linux system programming, managing the current working directory is a fundamental operation that every programmer must understand. The working directory is the directory in which a process currently operates, and it serves as the reference point for relative path resolution. This topic covers two important system calls for directory management: `fchdir()` and `getcwd()`, along with an essential understanding of device special files in the Unix filesystem.

The `fchdir()` function provides an alternative method to change the working directory using a file descriptor, while `getcwd()` retrieves the absolute path of the current working directory. These functions are particularly useful in file manipulation programs, shell implementations, and system utilities. Additionally, device special files represent an important concept in Unix/Linux that allows programs to interact with hardware devices through the filesystem interface, making device I/O operations similar to regular file operations.

Understanding these concepts is crucial for CSE students as they form the foundation for system-level programming and operating system concepts covered in their curriculum.

## Key Concepts

### The Working Directory Concept

The current working directory (CWD) is a fundamental property of each process in Unix/Linux. Every process has a working directory that serves as the base for resolving relative pathnames. When a process starts, it typically inherits the working directory of its parent process (usually the shell). The working directory can be changed using the `chdir()` system call, and programs can query the current working directory using `getcwd()`.

### fchdir() Function

The `fchdir()` system call changes the current working directory to the directory referenced by an open file descriptor.

**Function Prototype:**

```c
#include <unistd.h>
int fchdir(int fd);
```

**Parameters:**

- `fd`: A file descriptor referring to a directory that must be open

**Return Value:**

- Returns 0 on success
- Returns -1 on error, and `errno` is set appropriately

**Key Points:**

1. The file descriptor must refer to a directory; if it refers to a regular file, the call will fail with `ENOTDIR`
2. Unlike `chdir()` which takes a pathname, `fchdir()` works with an already open directory descriptor
3. This function is particularly useful when you have a directory open (e.g., from `opendir()` or `open()`) and want to change to that directory without knowing its pathname
4. The directory remains open after `fchdir()` completes; you must close it separately when done
5. Common error codes include `EBADF` (invalid fd), `ENOTDIR` (fd doesn't refer to a directory), and `EACCES` (permission denied)

### getcwd() Function

The `getcwd()` function returns a pointer to a string containing the absolute pathname of the current working directory.

**Function Prototype:**

```c
#include <unistd.h>
char *getcwd(char *buf, size_t size);
char *getwd(char *buf); /* Deprecated, for backward compatibility */
char *get_current_dir_name(void); /* Dynamically allocated */
```

**Parameters:**

- `buf`: A pointer to a buffer where the pathname will be stored
- `size`: The size of the buffer in bytes

**Return Value:**

- Returns a pointer to `buf` on success
- Returns NULL on error, and `errno` is set appropriately

**Key Points:**

1. The buffer must be large enough to hold the pathname plus a terminating null character
2. If the buffer is too small, the function fails with `ERANGE`
3. The `get_current_dir_name()` function is a GNU extension that allocates memory using `malloc()`
4. The returned path is an absolute path starting from root (`/`)
5. On success, the returned pointer is the same as the `buf` argument

### Device Special Files

Device special files are a fundamental concept in Unix/Linux filesystems that provide an interface between user programs and hardware devices. They appear as files in the filesystem but represent hardware devices rather than regular data files.

**Types of Device Special Files:**

1. **Character Device Files:**

- Device access is on a character-by-character basis
- Examples: keyboards, mice, terminals, serial ports
- No buffering; data is transferred one character at a time
- Created using `mknod()` with type `S_IFCHR`
- Listed with 'c' in `ls -l` output

2. **Block Device Files:**

- Device access is in fixed-size blocks
- Examples: hard disks, CD-ROM drives, tape drives
- Buffered I/O operations
- Created using `mknod()` with type `S_IFBLK`
- Listed with 'b' in `ls -l` output

**Device Numbers:**

- Each device special file has a major number and minor number
- Major number: identifies the device driver
- Minor number: identifies the specific device or partition
- Retrieved using `major()` and `minor()` macros from `<sys/types.h>`

**Creating Device Files:**

```c
#include <sys/types.h>
#include <sys/stat.h>

int mknod(const char *pathname, mode_t mode, dev_t dev);
```

The `mode` argument specifies the file type and permissions. For character devices, use `S_IFCHR | mode`; for block devices, use `S_IFBLK | mode`. The `dev` argument encodes the major and minor numbers.

## Examples

### Example 1: Using fchdir() with dirfd()

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

int main() {
 DIR *dir;
 int dir_fd;
 char cwd[PATH_MAX];

 /* Open the /tmp directory */
 dir = opendir("/tmp");
 if (dir == NULL) {
 perror("opendir");
 exit(EXIT_FAILURE);
 }

 /* Get file descriptor from directory stream */
 dir_fd = dirfd(dir);
 if (dir_fd == -1) {
 perror("dirfd");
 closedir(dir);
 exit(EXIT_FAILURE);
 }

 printf("Before fchdir: ");
 if (getcwd(cwd, sizeof(cwd)) != NULL)
 printf("%s\n", cwd);

 /* Change to /tmp using file descriptor */
 if (fchdir(dir_fd) == -1) {
 perror("fchdir");
 closedir(dir);
 exit(EXIT_FAILURE);
 }

 printf("After fchdir: ");
 if (getcwd(cwd, sizeof(cwd)) != NULL)
 printf("%s\n", cwd);

 /* Cleanup */
 closedir(dir);

 return 0;
}
```

**Output:**

```
Before fchdir: /home/user
After fchdir: /tmp
```

### Example 2: getcwd() with error handling

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <limits.h>

int main() {
 char *cwd;
 char buffer[PATH_MAX];

 /* Method 1: Using a user-provided buffer */
 if (getcwd(buffer, sizeof(buffer)) != NULL) {
 printf("Current directory (buffer): %s\n", buffer);
 } else {
 perror("getcwd buffer version");
 }

 /* Method 2: Using dynamically allocated memory */
 cwd = get_current_dir_name();
 if (cwd != NULL) {
 printf("Current directory (allocated): %s\n", cwd);
 free(cwd);
 } else {
 perror("get_current_dir_name");
 }

 return 0;
}
```

### Example 3: Creating a device special file programmatically

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
 /* Create a character device file with major number 5, minor number 1 */
 /* Major 5, minor 1 is typically /dev/tty */
 dev_t dev = makedev(5, 1);
 mode_t mode = S_IFCHR | 0666; /* Character device with rw-rw-rw- */

 if (mknod("/tmp/mydevice", mode, dev) == -1) {
 perror("mknod");
 exit(EXIT_FAILURE);
 }

 printf("Device file created successfully\n");

 /* Verify using stat */
 struct stat st;
 if (stat("/tmp/mydevice", &st) == 0) {
 printf("Device type: %s\n", S_ISCHR(st.st_mode) ? "Character" : "Block");
 printf("Major number: %lu\n", (unsigned long)major(st.st_rdev));
 printf("Minor number: %lu\n", (unsigned long)minor(st.st_rdev));
 }

 /* Cleanup */
 unlink("/tmp/mydevice");

 return 0;
}
```

## Exam Tips

1. **Remember the function signatures:** `int fchdir(int fd)` and `char *getcwd(char *buf, size_t size)` are frequently asked in exams.

2. **Key difference between chdir() and fchdir():** chdir() takes a pathname argument, while fchdir() takes an open file descriptor.

3. **Device file types:** Character devices use 'c' in ls -l output (unbuffered, byte-oriented), while block devices use 'b' (buffered, block-oriented).

4. **Error handling:** Remember that fchdir() fails with ENOTDIR if the file descriptor doesn't refer to a directory, and getcwd() fails with ERANGE if the buffer is too small.

5. **Device numbers:** Each device has major (identifies driver) and minor (identifies specific device) numbers, retrievable using major() and minor() macros.

6. **mknod() usage:** Remember that mknod() requires root privileges for creating device special files in system directories like /dev.

7. **Path_MAX constant:** This constant from `<limits.h>` defines the maximum length of a pathname.

8. **dirfd() function:** This returns the file descriptor associated with a directory stream, which can be used with fchdir().

9. **S_IFCHR and S_IFBLK:** These are the file type flags for character and block device files respectively.

10. **get_current_dir_name():** This is a GNU extension that allocates memory dynamically for the current working directory string.

11. **Process inheritance:** Child processes inherit the parent's working directory, but subsequent changes in child don't affect parent and vice versa.

12. **Symbolic links and working directory:** If the current directory is a symbolic link, getcwd() returns the resolved path, not the symbolic link path.
