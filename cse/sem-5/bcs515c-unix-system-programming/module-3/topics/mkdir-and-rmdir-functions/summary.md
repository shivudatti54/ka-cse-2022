# mkdir() and rmdir() Functions - Summary

## Key Definitions and Concepts

- **mkdir()**: UNIX system call that creates a new empty directory with specified pathname and permissions
- **rmdir()**: UNIX system call that removes an empty directory from the file system
- **umask**: User file creation mask that modifies the permissions of newly created files and directories
- **errno**: A variable that stores error codes when system calls fail

## Important Formulas and Theorems

```
final_permissions = mode & ~umask
```

- mkdir() prototype: `int mkdir(const char *pathname, mode_t mode);`
- rmdir() prototype: `int rmdir(const char *pathname);`
- Both return 0 on success, -1 on failure

## Key Points

- mkdir() requires `<sys/stat.h>` header file
- rmdir() requires `<unistd.h>` header file
- rmdir() only removes empty directories (only '.' and '..' entries)
- Every new directory automatically contains '.' (self) and '..' (parent) entries
- Common errno values for mkdir(): EEXIST, EACCES, ENOENT, ENOTDIR
- Common errno values for rmdir(): ENOTEMPTY, ENOENT, EBUSY, EACCES
- Both absolute and relative paths can be used
- Permissions are affected by the process umask value

## Common Mistakes to Avoid

- Confusing header files: mkdir() uses sys/stat.h, not unistd.h
- Forgetting that rmdir() fails on non-empty directories
- Not checking return values for error handling
- Assuming mkdir() will succeed without error checking
- Ignoring umask when calculating final permissions

## Revision Tips

1. Memorize the exact function prototypes with their header files
2. Practice writing small C programs to create and remove directories
3. Remember the list of errno values for both functions
4. Understand how umask affects permission bits
5. Remember that rmdir() is specifically for directories, not files
