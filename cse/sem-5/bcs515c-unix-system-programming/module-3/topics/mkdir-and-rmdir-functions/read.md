# mkdir() and rmdir() Functions in UNIX/Linux

## Introduction

The mkdir() and rmdir() functions are fundamental system calls in UNIX/Linux operating systems that enable processes to create and remove directories. These functions are essential components of file system management and are extensively used in system programming, application development, and shell scripting. Understanding these functions is crucial for any computer science engineering student, as they form the backbone of file system operations in UNIX-like operating systems.

The mkdir() system call creates a new empty directory, while rmdir() removes an empty directory. These operations are atomic and provide proper error handling mechanisms essential for robust application development. In the context of 's Operating Systems syllabus, these functions demonstrate important concepts like system calls, file system structure, process interaction with the kernel, and error handling in operating systems.

## Key Concepts

### 1. mkdir() - Create Directory

The mkdir() function creates a new directory with the specified pathname. It is declared in the `<sys/stat.h>` header file and requires appropriate permissions to create a directory.

**Function Prototype:**

```c
#include <sys/stat.h>

int mkdir(const char *pathname, mode_t mode);
```

**Parameters:**

- `pathname`: Pointer to a string containing the path name of the directory to be created
- `mode`: Specifies the permissions to be set on the new directory

**Return Value:**

- Returns 0 on success
- Returns -1 on error, and errno is set appropriately

**Common errno values:**

- EEXIST: Pathname already exists (but may be a file)
- EACCES: Write permission denied for the parent directory
- ENOENT: A component of the path prefix does not exist
- ENOTDIR: A component of the path prefix is not a directory
- EROFS: The parent directory is on a read-only file system

### 2. rmdir() - Remove Directory

The rmdir() function removes an empty directory. The directory must be empty (containing only '.' and '..' entries) before it can be removed.

**Function Prototype:**

```c
#include <unistd.h>

int rmdir(const char *pathname);
```

**Parameters:**

- `pathname`: Pointer to a string containing the path name of the directory to be removed

**Return Value:**

- Returns 0 on success
- Returns -1 on error, and errno is set appropriately

**Common errno values:**

- ENOENT: The pathname does not exist
- EBUSY: The directory is in use by some process
- ENOTDIR: A component of the path is not a directory
- ENOTEMPTY: The directory is not empty
- EACCES: Write permission is denied on the parent directory
- EPERM: The file system does not allow directory removal

### 3. Directory Permissions and umask

When creating a directory with mkdir(), the mode argument specifies the permissions. However, the actual permissions are affected by the process's umask (user file creation mask). The final permissions are calculated as:

```
final_permissions = mode & ~umask
```

Common default umask values are 022, which means:

- If mode is 0777, final permissions become 0755 (rwxr-xr-x)

### 4. Special Directory Entries

Every newly created directory automatically contains two special entries:

- "." - refers to the directory itself
- ".." - refers to the parent directory

These entries are automatically created by the mkdir() system call and are essential for directory traversal.

### 5. Path Resolution

Both mkdir() and rmdir() can work with:

- Absolute paths (starting from root "/")
- Relative paths (from current working directory)
- Symbolic links (they operate on the target directory)

## Examples

### Example 1: Creating a Simple Directory

```c
#include <stdio.h>
#include <sys/stat.h>
#include <errno.h>
#include <string.h>

int main() {
 const char *dirpath = "/home/student/mynewdir";

 // Create directory with rwxr-xr-x permissions
 if (mkdir(dirpath, 0755) == 0) {
 printf("Directory created successfully: %s\n", dirpath);
 } else {
 fprintf(stderr, "Error creating directory: %s\n", strerror(errno));
 return 1;
 }

 return 0;
}
```

**Step-by-step explanation:**

1. Include necessary header files for system calls and error handling
2. Define the directory path as a string constant
3. Call mkdir() with path and permissions (0755 = rwxr-xr-x)
4. Check return value for success (0) or failure (-1)
5. Use strerror() to convert errno to human-readable message

### Example 2: Creating Nested Directories

```c
#include <stdio.h>
#include <sys/stat.h>
#include <errno.h>
#include <string.h>
#include <libgen.h>

int create_nested_dirs(const char *path) {
 char *path_copy = strdup(path);
 char *p = path_copy;

 // Skip leading '/' if present
 if (*p == '/') {
 p++;
 }

 // Create each component of the path
 while (p != NULL && *p != '\0') {
 char *next = strchr(p, '/');
 if (next != NULL) {
 *next = '\0'; // Temporarily terminate string
 }

 // Try to create this component
 if (mkdir(path_copy, 0755) == -1) {
 if (errno != EEXIST) {
 fprintf(stderr, "Error creating %s: %s\n",
 path_copy, strerror(errno));
 free(path_copy);
 return -1;
 }
 }

 if (next != NULL) {
 *next = '/'; // Restore the '/'
 p = next + 1;
 } else {
 break;
 }
 }

 free(path_copy);
 return 0;
}

int main() {
 const char *nested_path = "/home/student/projects/test/src";

 if (create_nested_dirs(nested_path) == 0) {
 printf("Nested directories created successfully\n");
 } else {
 printf("Failed to create nested directories\n");
 }

 return 0;
}
```

**Step-by-step explanation:**

1. Create a copy of the path to avoid modifying the original
2. Parse the path component by component
3. For each component, attempt to create the directory
4. Handle the case where directory already exists (EEXIST)
5. Continue creating remaining components

### Example 3: Removing a Directory with Verification

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>
#include <errno.h>
#include <string.h>

int safe_rmdir(const char *path) {
 struct stat st;

 // Check if path exists
 if (stat(path, &st) == -1) {
 if (errno == ENOENT) {
 printf("Directory does not exist: %s\n", path);
 return 0; // Not an error if it doesn't exist
 }
 fprintf(stderr, "Error checking path: %s\n", strerror(errno));
 return -1;
 }

 // Check if it's a directory
 if (!S_ISDIR(st.st_mode)) {
 fprintf(stderr, "Error: %s is not a directory\n", path);
 return -1;
 }

 // Attempt to remove the directory
 if (rmdir(path) == -1) {
 if (errno == ENOTEMPTY) {
 fprintf(stderr, "Error: Directory is not empty: %s\n", path);
 } else {
 fprintf(stderr, "Error removing directory: %s\n", strerror(errno));
 }
 return -1;
 }

 printf("Directory removed successfully: %s\n", path);
 return 0;
}

int main() {
 const char *dirpath = "/home/student/mynewdir";

 // First create the directory
 if (mkdir(dirpath, 0755) == 0) {
 printf("Created: %s\n", dirpath);
 }

 // Then remove it
 safe_rmdir(dirpath);

 return 0;
}
```

**Step-by-step explanation:**

1. Use stat() to verify the path exists
2. Check if the path points to a directory using S_ISDIR macro
3. Attempt to remove the directory using rmdir()
4. Handle specific error cases like ENOTEMPTY
5. Provide meaningful error messages

## Exam Tips

1. **Remember function headers**: mkdir() is in `<sys/stat.h>` while rmdir() is in `<unistd.h>`. This distinction is frequently tested in exams.

2. **Permission calculation**: Understand how umask affects directory permissions. Final permissions = mode & ~umask.

3. **rmdir() requirement**: Remember that rmdir() only works on empty directories. This is a common trick question.

4. **Return values**: Both functions return 0 on success and -1 on failure. Never confuse this with file operations that return positive values.

5. **Special entries**: Every directory automatically contains '.' and '..' entries after creation.

6. **errno handling**: Study common errno values like EEXIST, EACCES, ENOENT, ENOTEMPTY for both functions.

7. **Path types**: Know that both functions work with both absolute and relative paths.

8. **Atomic operations**: mkdir() and rmdir() are atomic operations, meaning they either complete entirely or fail entirely.
