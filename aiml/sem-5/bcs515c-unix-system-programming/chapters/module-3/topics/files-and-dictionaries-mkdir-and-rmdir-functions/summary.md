# **Files and Dictionaries: mkdir and rmdir Functions**

## **Key Points:**

### Introduction

- `mkdir` and `rmdir` functions are used to manage files and directories in Unix systems.
- These functions are essential for file system organization and management.

### mkdir Function

- Creates a new directory with the specified name.
- Returns 0 if the directory is created successfully.
- Returns non-zero if the directory cannot be created (e.g., due to permission errors).

### rmdir Function

- Deletes an empty directory with the specified name.
- Returns 0 if the directory is deleted successfully.
- Returns non-zero if the directory cannot be deleted (e.g., due to permission errors or if the directory is not empty).

### Important Formulas and Definitions:

- **Pathname**: A string that specifies the location of a file or directory in the file system.

### Important Theorems:

- **Directory Existence Theorem**: A directory can only be deleted if it is empty and has not been modified recently.
- **File System Consistency Theorem**: The `mkdir` and `rmdir` functions ensure that the file system remains consistent and valid after their execution.

### Quick Revision Tips:

- Use `mkdir` to create new directories and `rmdir` to delete empty directories.
- Be aware of permission errors when using `mkdir` and `rmdir`.
- Verify directory existence before attempting to delete it with `rmdir`.

By mastering the `mkdir` and `rmdir` functions, you can effectively manage files and directories in Unix systems, ensuring a stable and organized file system.
