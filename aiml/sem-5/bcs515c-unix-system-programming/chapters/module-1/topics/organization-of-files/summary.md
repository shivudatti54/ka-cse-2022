# Organization of Files

## UNIX SYSTEM PROGRAMMING

### Revision Notes

### Key Features

- Files are organized using a hierarchical structure
- Each file is identified by a unique name (filename)
- There are two types of files: regular files and special files
- Regular files contain data and can be accessed using the `cat`, `echo`, and `cp` commands

### File System Hierarchy

- File system consists of:
  - Root directory (/)
  - Directories (subdirectories)
  - Files
- Each directory has a parent-child relationship
- Files can be created, deleted, and renamed using various commands

### File Types

- **Regular Files**
  - Contain data (e.g., text, images, programs)
  - Can be accessed using `cat`, `echo`, and `cp`
- **Special Files**
  - Represent devices or processes
  - Can be accessed using system calls (e.g., `open`, `close`)

### File Permissions

- Files can be accessed by different users with different permissions
- Permissions are controlled using the `chmod` command
- Three types of permissions:
  - Read (r)
  - Write (w)
  - Execute (x)

### Important Formulas and Definitions

- **File Path**: The sequence of directories and filenames that lead to a file (e.g., `/home/user/file.txt`)
- **File Descriptor**: A unique integer used to identify a file (e.g., `fd = open("file.txt", O_RDONLY)`)

Note: The above summary is a concise revision guide and is not intended to be a comprehensive study material.
