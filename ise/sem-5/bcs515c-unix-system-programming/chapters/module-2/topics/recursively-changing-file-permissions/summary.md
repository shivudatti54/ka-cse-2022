# **Recursively Changing File Permissions**

### Key Points

- **Change File Permissions**:
  - `chmod [permissions] [file]`: changes the permissions of a single file or directory
  - `chmod [permissions] [directory]/[file]`: changes the permissions of a directory and all its contents
- **Recursive Permission Change**:
  - Use `chmod -R [permissions] [directory]`: changes the permissions of a directory and all its contents recursively
  - Use `chmod -r [permissions] [directory]`: similar to `-R`, but changes the permissions of the directory itself, not its contents
- **Permission Notation**:
  - `u`: user
  - `g`: group
  - `o`: others
  - `a`: all (user, group, others)
  - `+`: add permission
  - `-`: remove permission
    +=`: set permission
- **Default Permissions**:
  - New files created with `touch`: default permissions are 644 (rw-r--r--)
  - New files created with `echo`: default permissions are 666 (rw-rw-rw-)
- **Theorem**: The Unix permission system is based on the concept of "access control", which allows you to control who can read, write, or execute a file.

### Important Formulas and Definitions

- No specific formulas are required for this topic, but you should be familiar with the concept of access control and permission notation.

### Key Formulas

- `chmod [permissions] [file]`: changes the permissions of a single file or directory
- `chmod -R [permissions] [directory]`: changes the permissions of a directory and all its contents recursively
- `chmod -r [permissions] [directory]`: similar to `-R`, but changes the permissions of the directory itself, not its contents

### Quick Revision Tips

- Use `chmod -R` to change permissions recursively
- Use `chmod -r` to change permissions of a directory itself, not its contents
- Pay attention to permission notation (u, g, o, a)
- Remember that default permissions are 644 for new files created with `touch` and 666 for files created with `echo`
