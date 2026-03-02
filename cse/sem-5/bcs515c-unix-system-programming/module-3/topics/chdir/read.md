# Change Directory (chdir) System Call

## Introduction

The **chdir** (change directory) system call is a fundamental operating system function that modifies the current working directory of a process. In Unix-like operating systems, every process maintains a concept of a "current working directory" (CWD), which serves as the default directory for relative path name resolution. When a process starts, it typically inherits the working directory from its parent process. The chdir system call allows processes to change this working directory during execution, enabling flexible navigation through the file system hierarchy.

Understanding chdir is crucial for system programming and shell implementation because it directly impacts how file paths are interpreted throughout the process lifetime. Without the ability to change directories, processes would be restricted to accessing files only from their initial working directory, severely limiting their functionality. The chdir system call is essential for implementing interactive shells, file management utilities, and any application that needs to operate on different parts of the file system.

In the context of 's Operating Systems syllabus (22CS34), chdir is covered under process management and file I/O operations, emphasizing its role in process environment management and file system navigation.

## Key Concepts

### Current Working Directory (CWD)

The current working directory is a fundamental attribute of each process in Unix-like systems. It represents the directory from which relative paths are resolved. When a process attempts to open a file using a relative path (e.g., "data.txt" instead of "/home/user/data.txt"), the operating system searches for the file relative to the current working directory. The CWD is inherited from the parent process during fork(), and the initial CWD for login shells is typically the user's home directory.

### The chdir() System Call

The chdir system call has the following prototype:

```c
#include <unistd.h>
int chdir(const char *path);
```

The function takes a single argument: a path to the new working directory. This path can be either absolute (starting with '/') or relative to the current working directory. On success, chdir returns 0, and on failure, it returns -1 with errno set to indicate the specific error.

### Difference Between chdir and fchdir

Unix provides two variants for changing directories:

- **chdir()**: Takes a pathname as argument
- **fchdir()**: Takes a file descriptor as argument

```c
#include <unistd.h>
int fchdir(int fd);
```

The fchdir() function is particularly useful when you already have a directory open (e.g., from a previous opendir() call), as it allows changing to that directory without re-opening it by name. This can be more efficient in certain scenarios and avoids race conditions in multi-threaded programs.

### getcwd() - Complementary Function

The getcwd() function retrieves the current working directory, serving as the inverse of chdir():

```c
#include <unistd.h>
char *getcwd(char *buf, size_t size);
char *getcwd(char *buf, size_t size);
```

This function is useful for saving the current directory before changing it, allowing the process to restore its original location later.

### Path Resolution and chdir

When chdir() is called with a relative path, the path is resolved relative to the current working directory at the time of the call. After changing directories, all subsequent relative path operations use the new directory as the base. It's important to note that symbolic links in the path are resolved by chdir(), and the final directory becomes the actual working directory.

### Error Conditions

The chdir() system call can fail due to several reasons:

- **EACCES**: Permission denied for the directory
- **ENOENT**: The specified directory does not exist
- **ENOTDIR**: A component of the path prefix is not a directory
- **EFAULT**: The path points outside the accessible address space
- **ENOMEM**: Insufficient kernel memory

## Examples

### Example 1: Basic chdir Usage

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>

int main() {
 char cwd[256];

 // Get initial working directory
 if (getcwd(cwd, sizeof(cwd)) != NULL) {
 printf("Initial directory: %s\n", cwd);
 }

 // Change to /tmp directory
 if (chdir("/tmp") == 0) {
 printf("Successfully changed to /tmp\n");

 // Verify the change
 if (getcwd(cwd, sizeof(cwd)) != NULL) {
 printf("Current directory now: %s\n", cwd);
 }
 } else {
 perror("chdir failed");
 return EXIT_FAILURE;
 }

 return EXIT_SUCCESS;
}
```

**Step-by-step execution:**

1. First, getcwd() retrieves and prints the initial working directory
2. chdir("/tmp") attempts to change to /tmp directory
3. If successful, getcwd() is called again to verify the new directory
4. If chdir fails, perror() prints the error message with descriptive text

### Example 2: Changing to a Relative Path

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
 char cwd[256];

 printf("Starting in: %s\n", getcwd(cwd, sizeof(cwd)));

 // Change to subdirectory "documents" relative to current
 if (chdir("documents") == 0) {
 printf("Changed to: %s\n", getcwd(cwd, sizeof(cwd)));

 // Now change to "reports" subdirectory within documents
 if (chdir("reports") == 0) {
 printf("Now in: %s\n", getcwd(cwd, sizeof(cwd)));
 }
 } else {
 perror("chdir failed");
 return EXIT_FAILURE;
 }

 return EXIT_SUCCESS;
}
```

**Step-by-step execution:**

1. The program starts in some initial directory
2. chdir("documents") changes to a subdirectory named "documents" relative to current directory
3. chdir("reports") changes to "reports" subdirectory within documents
4. Each change is verified using getcwd()

### Example 3: Save and Restore Working Directory

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main() {
 char *original_dir;
 char cwd[1024];

 // Allocate memory for original directory path
 original_dir = getcwd(NULL, 0);
 if (original_dir == NULL) {
 perror("getcwd");
 return EXIT_FAILURE;
 }

 printf("Original: %s\n", original_dir);

 // Perform operations in /tmp
 if (chdir("/tmp") != 0) {
 perror("chdir to /tmp");
 free(original_dir);
 return EXIT_FAILURE;
 }

 printf("Changed to: %s\n", getcwd(cwd, sizeof(cwd)));


 // ... perform operations in /tmp ...

 // Restore original directory
 if (chdir(original_dir) != 0) {
 perror("chdir back to original");
 free(original_dir);
 return EXIT_FAILURE;
 }

 printf("Restored to: %s\n", getcwd(cwd, sizeof(cwd)));

 free(original_dir);
 return EXIT_SUCCESS;
}
```

**Step-by-step execution:**

1. getcwd(NULL, 0) dynamically allocates memory for the path string
2. The original directory path is saved in original_dir
3. Change to /tmp and perform operations
4. Finally, use chdir(original_dir) to return to the original directory
5. Free the allocated memory

## Exam Tips

1. **Remember the function prototype**: chdir() is declared in `<unistd.h>` and takes a `const char *path` argument, returning an integer (0 for success, -1 for failure).

2. **Understand the difference between absolute and relative paths**: chdir accepts both absolute paths (starting with '/') and relative paths (resolved from current directory).

3. **Know the complementary functions**: getcwd() retrieves the current directory, while fchdir() uses a file descriptor instead of a pathname.

4. **Remember error handling**: Always check the return value of chdir() and use perror() or strerror() to handle errors appropriately in exam programs.

5. **Thread safety considerations**: Each thread in a process shares the same working directory, so chdir() affects all threads—keep this in mind for multi-threaded programs.

6. **Child process inheritance**: When a process calls fork(), the child process inherits the parent's working directory at the time of fork, but subsequent changes in one process do not affect the other.

7. **Symbolic link handling**: chdir() follows symbolic links, so chdir("/tmp") where /tmp is a symlink will change to the target directory.

8. **Permission requirements**: The process needs execute (search) permission on the directory to change into it.
