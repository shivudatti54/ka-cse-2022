# **Relative and Absolute Permissions Changing Methods**

## **Introduction**

This summary covers the methods to change file permissions in UNIX systems, including relative and absolute methods.

## **Relative Permissions Changing Methods**

- **chmod command**: used to change file permissions
- **Symbolic Notation**: uses three numbers (owner, group, others) to specify permissions
  - 1: read permission
  - 2: write permission
  - 4: execute permission
- **Octal Notation**: uses three numbers (owner, group, others) to specify permissions
  - 0: no permissions
  - 1: read permission
  - 2: write permission
  - 4: execute permission
- **Examples**:
  - `chmod 755 file.txt` (owner read, write, execute, group read, execute, others read, execute)
  - `chmod u+x file.txt` (owner execute, group execute, others execute)

## **Absolute Permissions Changing Methods**

- **chmod command with bitwise operators**:
  - `chmod u+x file.txt` (owner execute, group execute, others execute)
  - `chmod g-wx file.txt` (group write, execute, others write, execute)
- **chmod command with user and group specifications**:
  - `chmod u+xrw file.txt` (owner read, write, execute, group read, write, execute, others read, write, execute)
  - `chmod g-wx file.txt` (group write, execute, others write, execute)

## **Important Formulas, Definitions, and Theorems**

- **File permission calculations**: `u` (owner), `g` (group), `o` (others)
  - `u+r`: owner read
  - `g+w`: group write
  - `o-x`: others execute
- **Permission flags**:
  +x, -x, +w, -w, +r, -r, u, g, o
