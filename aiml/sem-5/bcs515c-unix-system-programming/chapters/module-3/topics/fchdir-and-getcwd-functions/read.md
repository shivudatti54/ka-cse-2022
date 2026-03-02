# Directory Functions in Unix System Programming

## Introduction to Directory Functions

Directory functions in Unix provide the essential tools for navigating and manipulating the directory structure of the filesystem. These functions allow programs to create, remove, and change directories, as well as obtain information about the current working directory. Understanding these functions is crucial for system programming as they form the foundation for file system navigation and organization.

Directory operations are built upon the fundamental file I/O concepts but operate at a higher level of abstraction, dealing with directory entries rather than raw file data.

## Key Directory Functions

### mkdir() - Creating Directories

The `mkdir()` function creates a new directory with the specified pathname.

**Function Prototype:**

```c
#include <sys/stat.h>
#include <sys/types.h>

int mkdir(const char *pathname, mode_t mode);
```

**Parameters:**

- `pathname`: The path of the directory to create
- `mode`: The permission bits for the new directory

**Return Value:**

- Returns 0 on success
- Returns -1 on error and sets errno

**Example:**

```c
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

int main() {
    if (mkdir("/tmp/mydir", 0755) == -1) {
        perror("mkdir");
        return 1;
    }
    printf("Directory created successfully\n");
    return 0;
}
```

The mode argument specifies the permissions using the same bit pattern as the `chmod` command. Common permission values include:

- 0755: rwxr-xr-x (read, write, execute for owner; read and execute for group and others)
- 0777: rwxrwxrwx (full permissions for all)

### rmdir() - Removing Directories

The `rmdir()` function removes an empty directory.

**Function Prototype:**

```c
#include <unistd.h>

int rmdir(const char *pathname);
```

**Parameters:**

- `pathname`: The path of the directory to remove

**Return Value:**

- Returns 0 on success
- Returns -1 on error and sets errno

**Example:**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    if (rmdir("/tmp/mydir") == -1) {
        perror("rmdir");
        return 1;
    }
    printf("Directory removed successfully\n");
    return 0;
}
```

**Important:** The directory must be empty before it can be removed. If the directory contains files or subdirectories, `rmdir()` will fail with errno set to ENOTEMPTY.

### chdir() and fchdir() - Changing Directories

The `chdir()` function changes the current working directory of the calling process.

**Function Prototype:**

```c
#include <unistd.h>

int chdir(const char *path);
int fchdir(int fd);
```

**Parameters:**

- `chdir()`: Takes a pathname as argument
- `fchdir()`: Takes a file descriptor of an open directory

**Return Value:**

- Returns 0 on success
- Returns -1 on error and sets errno

**Example:**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    if (chdir("/tmp") == -1) {
        perror("chdir");
        return 1;
    }
    printf("Current directory changed to /tmp\n");
    return 0;
}
```

The current working directory is a process attribute, meaning that changing it affects only the process that calls `chdir()`, not the shell from which the program was executed.

### getcwd() - Getting Current Working Directory

The `getcwd()` function retrieves the absolute pathname of the current working directory.

**Function Prototype:**

```c
#include <unistd.h>

char *getcwd(char *buf, size_t size);
```

**Parameters:**

- `buf`: Buffer to store the pathname
- `size`: Size of the buffer

**Return Value:**

- Returns pointer to buf on success
- Returns NULL on error and sets errno

**Example:**

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    char cwd[1024];

    if (getcwd(cwd, sizeof(cwd)) == NULL) {
        perror("getcwd");
        return 1;
    }

    printf("Current working directory: %s\n", cwd);
    return 0;
}
```

It's important to allocate a sufficiently large buffer for `getcwd()`. If the buffer is too small, the function will return NULL with errno set to ERANGE.

## Directory Navigation and Path Resolution

### Absolute vs Relative Paths

Unix systems support two types of pathnames:

**Absolute Pathnames:**

- Begin with a forward slash (/)
- Specify the complete path from the root directory
- Example: `/home/user/documents/file.txt`

**Relative Pathnames:**

- Do not begin with a forward slash
- Interpreted relative to the current working directory
- Example: `documents/file.txt` (if current directory is `/home/user`)

### The Directory Structure

```
Root Directory (/)
├── bin/          (Essential system binaries)
├── etc/          (System configuration files)
├── home/         (User home directories)
│   ├── user1/
│   ├── user2/
│   └── user3/
├── tmp/          (Temporary files)
├── usr/          (User programs and data)
└── var/          (Variable data like logs)
```

## Directory Reading Functions

While not part of the basic directory functions covered in this module, it's important to mention the functions used to read directory contents:

- `opendir()`: Opens a directory stream
- `readdir()`: Reads the next directory entry
- `closedir()`: Closes a directory stream
- `rewinddir()`: Resets the directory stream to the beginning

These functions are typically covered in more advanced file I/O topics.

## Error Handling with Directory Functions

Proper error handling is essential when working with directory functions. Common errors include:

| Error Code | Description               | Common Causes                              |
| ---------- | ------------------------- | ------------------------------------------ |
| EACCES     | Permission denied         | Insufficient permissions for the operation |
| EEXIST     | File exists               | Directory already exists (mkdir)           |
| ENOENT     | No such file or directory | Path component doesn't exist               |
| ENOTDIR    | Not a directory           | Path component is not a directory          |
| ENOTEMPTY  | Directory not empty       | Trying to remove non-empty directory       |

**Example with comprehensive error handling:**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

int main() {
    if (chdir("/nonexistent") == -1) {
        fprintf(stderr, "Error changing directory: %s\n", strerror(errno));

        switch(errno) {
            case EACCES:
                fprintf(stderr, "Permission denied to access the directory\n");
                break;
            case ENOENT:
                fprintf(stderr, "The directory does not exist\n");
                break;
            case ENOTDIR:
                fprintf(stderr, "A component of the path is not a directory\n");
                break;
            default:
                fprintf(stderr, "Unknown error occurred\n");
        }
        return 1;
    }
    return 0;
}
```

## Practical Examples and Use Cases

### Creating a Directory Hierarchy

```c
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

int create_directory_hierarchy() {
    // Create multiple directories
    if (mkdir("/tmp/app", 0755) == -1) {
        perror("Failed to create /tmp/app");
        return 1;
    }

    if (mkdir("/tmp/app/logs", 0755) == -1) {
        perror("Failed to create /tmp/app/logs");
        return 1;
    }

    if (mkdir("/tmp/app/data", 0755) == -1) {
        perror("Failed to create /tmp/app/data");
        return 1;
    }

    printf("Directory hierarchy created successfully\n");
    return 0;
}
```

### Directory Navigation Program

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char cwd[1024];

    // Get current directory
    if (getcwd(cwd, sizeof(cwd)) == NULL) {
        perror("getcwd");
        return 1;
    }
    printf("Current directory: %s\n", cwd);

    // Change to specified directory or home
    const char *target = (argc > 1) ? argv[1] : getenv("HOME");
    if (chdir(target) == -1) {
        perror("chdir");
        return 1;
    }

    // Get new current directory
    if (getcwd(cwd, sizeof(cwd)) == NULL) {
        perror("getcwd");
        return 1;
    }
    printf("New directory: %s\n", cwd);

    return 0;
}
```

## Relationship with File Descriptors

Directory functions work alongside file descriptor-based functions. The `fchdir()` function is particularly interesting as it uses a file descriptor to change directories:

```c
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd;
    char cwd[1024];

    // Open current directory
    fd = open(".", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }

    // Change to another directory
    if (chdir("/tmp") == -1) {
        perror("chdir");
        close(fd);
        return 1;
    }

    getcwd(cwd, sizeof(cwd));
    printf("Current directory: %s\n", cwd);

    // Return to original directory using file descriptor
    if (fchdir(fd) == -1) {
        perror("fchdir");
        close(fd);
        return 1;
    }

    getcwd(cwd, sizeof(cwd));
    printf("Back to original: %s\n", cwd);

    close(fd);
    return 0;
}
```

## Exam Tips

1. **Remember the header files**: `mkdir()` requires `<sys/stat.h>` and `<sys/types.h>`, while `chdir()`, `fchdir()`, `rmdir()`, and `getcwd()` require `<unistd.h>`.

2. **Error handling is crucial**: Always check return values and handle errors appropriately using `perror()` or `strerror(errno)`.

3. **Understand the process scope**: Directory changes affect only the current process, not the parent shell.

4. **Buffer size matters**: For `getcwd()`, ensure the buffer is large enough (PATH_MAX constant can be used).

5. **Permission bits**: Remember that directory permissions work differently than file permissions. Execute permission on a directory means search permission.

6. **Empty requirement**: `rmdir()` only works on empty directories. You must remove all contents first.

7. **File descriptors**: `fchdir()` uses a file descriptor obtained by opening a directory with `open()`.

8. **Common errors**: Memorize common errno values (EACCES, EEXIST, ENOENT, ENOTDIR, ENOTEMPTY) and what they mean.
