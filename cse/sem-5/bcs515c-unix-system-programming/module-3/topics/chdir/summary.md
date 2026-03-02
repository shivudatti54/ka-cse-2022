# Change Directory (chdir) - Summary

## Key Definitions and Concepts

- **Current Working Directory (CWD)**: The directory from which relative paths are resolved. Every Unix process has a CWD inherited from its parent.

- **chdir() System Call**: A Unix system call that changes the current working directory of a process to a specified path.

- **Relative Path**: A path that is resolved relative to the current working directory (e.g., "docs/file.txt").

- **Absolute Path**: A complete path starting from root directory (e.g., "/home/user/docs").

## Important Formulas and Theorems

```c
int chdir(const char *path);  // Returns 0 on success, -1 on failure

int fchdir(int fd);           // Change directory using file descriptor

char *getcwd(char *buf, size_t size);  // Get current working directory
```

## Key Points

- chdir() is declared in `<unistd.h>` header file
- Returns 0 for success and -1 for failure, with errno set on error
- Accepts both absolute and relative path arguments
- fchdir() is more efficient when you already have a directory open
- getcwd() can allocate memory dynamically when passed NULL as first argument
- Process needs execute permission on target directory
- Common errors: EACCES (permission denied), ENOENT (directory doesn't exist), ENOTDIR (path component not a directory)
- Child processes inherit parent's CWD at fork() time
- Symbolic links are followed by chdir()

## Common Mistakes to Avoid

1. **Not checking return value**: Always verify chdir() succeeds before assuming the directory changed

2. **Confusing chdir with cd command**: chdir() is a system call, not a shell command—it's used in programs

3. **Memory leaks with getcwd()**: When using getcwd(NULL, 0), remember to free() the allocated memory

4. **Thread safety**: Remember all threads share the same CWD in a process

## Revision Tips

1. Practice writing simple C programs that change directories and verify with getcwd()

2. Remember the header file: <unistd.h> is required for chdir() and getcwd()

3. Understand that chdir() affects only the calling process, not the parent or sibling processes

4. Know the error return convention: always check for -1, not just non-zero values

5. Review the relationship between chdir and file operations—relative file paths depend on CWD
