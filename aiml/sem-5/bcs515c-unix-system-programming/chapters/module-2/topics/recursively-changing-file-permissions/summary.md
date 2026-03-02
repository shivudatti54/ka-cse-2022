# Recursive File Permission Changes

### Key Points

- The `chmod` command is used to change file permissions in UNIX systems.
- The `chmod` command can be used with the `-R` option to recursively change file permissions.
- The `chmod` command uses the following syntax:
  - `chmod [permissions] [file]`
  - `chmod -R [permissions] [file]`
  - `chmod -R [permissions] [directory]` (changes permissions recursively on all files and subdirectories)
- The permissions can be specified using the following notation:
  - `u` for owner
  - `g` for group
  - `o` for others
  - `+` for add permission
  - `-` for remove permission
  - `=` for set permission
- The permissions can also be specified using the following octal notation:
  - `0` for no permission
  - `1` for execute permission
  - `2` for write permission
  - `4` for read permission

### Important Formulas

- `chmod u+x file.txt` adds execute permission for the owner
- `chmod g-w file.txt` removes write permission for the group
- `chmod o+r file.txt` adds read permission for others

### Definitions

- ** permission**: The level of access granted to a user, group, or others to read, write, or execute a file or directory.
- **octal notation**: A way to specify permissions using a base-8 number (0-7).

### Theorems

- The `chmod` command is a powerful tool for managing file permissions in UNIX systems.
- The `-R` option is essential for recursively changing file permissions on all files and subdirectories within a directory.

### Quick Revision Tips

- Familiarize yourself with the `chmod` command syntax and options.
- Understand the permissions notation and octal notation.
- Practice changing file permissions using the `chmod` command.
