# **Profile**

### Key Points

- **Definition**: The profile of a file is a set of attributes that describe the file, including its name, permissions, ownership, and timestamps.
- **Components**:
  - **User ID (UID)**: The user ID of the owner of the file.
  - **Group ID (GID)**: The group ID of the file.
  - **Permissions**: The access rights of the owner, group, and others (read, write, execute).
- **UNIX Operating System**:
  - The profile of a file is stored in the inode table.
  - The inode table contains information about the file's attributes, such as its permissions and timestamps.

### Important Formulas and Definitions

- **File Permissions**: A set of three permissions (read, write, execute) that determine access rights for the owner, group, and others.
  - `rwx`: read, write, execute
  - `rw-`: read, write
  - `r-x`: read, execute
- **File Types**: Regular files (e.g., `file.txt`), directories (e.g., `dir`), symbolic links (e.g., `link`), special files (e.g., `pipe`, `socket`)

### Important Theorems

- **File Attributes**: The profile of a file is a set of attributes that determine its access rights and behavior in the UNIX operating system.
- **File Permissions**: The permissions of a file determine the access rights of the owner, group, and others.

### Revision Tips

- Review the definitions and formulas for file permissions and types.
- Practice changing file permissions using the `chmod` command.
- Study the inode table and its components, including the profile of a file.
