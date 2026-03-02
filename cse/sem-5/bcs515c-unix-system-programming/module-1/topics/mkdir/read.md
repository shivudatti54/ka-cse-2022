# mkdir - Making Directories in Linux/Unix

## Introduction

The `mkdir` (make directory) command is one of the fundamental file system management utilities in Linux and Unix operating systems. It is essential for creating new directories (also called folders) within the file system hierarchy. As a core utility that every system administrator, programmer, and general user must master, `mkdir` provides the foundation for organizing files and maintaining a logical directory structure.

In the context of 's Operating Systems curriculum, understanding `mkdir` goes beyond just creating folders—it demonstrates how system calls interact with the file system, how permissions work, and how processes communicate with the operating system's kernel. The command is part of the GNU coreutils package and is available on virtually every Unix-like operating system, including Linux distributions, macOS, and Windows Subsystem for Linux (WSL).

This topic is particularly important because directory management is a daily task for anyone working with computers. Whether you are setting up a project structure, organizing documentation, or creating system configuration directories, `mkdir` is often the first command you will use. Understanding its various options and behaviors is crucial for shell scripting, automation, and system administration tasks.

## Key Concepts

### Basic Syntax of mkdir

The general syntax of the `mkdir` command is:

```
mkdir [OPTION]... DIRECTORY...
```

The command accepts one or more directory names as arguments. You can specify absolute paths (starting from root `/`) or relative paths (from the current working directory).

### Creating Simple Directories

The most basic usage of `mkdir` requires only the directory name:

```bash
mkdir myfolder
```

This creates a directory named "myfolder" in the current working directory. After execution, you can verify its creation using the `ls -ld myfolder` command.

### Creating Directories with Absolute and Relative Paths

**Absolute Path Example:**

```bash
mkdir /home/student/projects
```

This creates the "projects" directory at the exact location specified from the root directory.

**Relative Path Example:**

```bash
mkdir ./documents/reports
```

This creates "reports" inside "documents" relative to the current directory.

### The -p Option (Parent Directories)

The `-p` or `--parents` option is one of the most useful features of `mkdir`. It creates parent directories as needed:

```bash
mkdir -p /home/student/year2024/month12/reports
```

Without the `-p` flag, this command would fail if any intermediate directory doesn't exist. With `-p`, mkdir creates all necessary parent directories automatically. This is particularly useful in shell scripts where you don't know whether the directory structure exists.

### The -m Option (Setting Permissions)

The `-m` or `--mode` option allows you to set specific permissions when creating a directory:

```bash
mkdir -m 755 project
mkdir -m 700 private
```

By default, new directories get permissions based on the system default (typically 755 for regular users). The mode can be specified in octal (like 755, 700) or symbolic (like u+rwx, go=rx) format.

### The -v Option (Verbose Output)

The `-v` or `--verbose` option prints a message for each created directory:

```bash
mkdir -v newproject
# Output: mkdir: created directory 'newproject'
```

This is particularly useful in scripts to track what the command is doing.

### Creating Multiple Directories at Once

You can create multiple directories in a single command:

```bash
mkdir dir1 dir2 dir3
```

This is equivalent to running three separate `mkdir` commands but is more efficient.

### Combining Options

Multiple options can be combined:

```bash
mkdir -pv /home/student/projects/{backend,frontend,docs}
```

This creates the full path with verbose output, and can even use brace expansion to create multiple directories.

### Understanding Directory Permissions

When you create a directory, it comes with execute permission (x) by default, which is necessary to access the directory. The permissions work as follows:

- **r (read)**: Allows listing files in the directory
- **w (write)**: Allows creating, deleting, and renaming files within the directory
- **x (execute)**: Allows entering the directory and accessing its contents

### Difference Between File and Directory Creation

Unlike files, directories in Unix/Linux are special file types. When you create a file using `touch` or `cat`, you create an empty file. When you create a directory using `mkdir`, the system creates a directory entry with two special entries: `.` (current directory) and `..` (parent directory).

### Error Handling

Common errors when using `mkdir` include:

1. **Permission Denied**: When you don't have write permission in the parent directory
2. **File Exists**: When a directory with the same name already exists
3. **No Such File or Directory**: When trying to create a subdirectory without the `-p` flag and the parent doesn't exist

### Exit Status

The `mkdir` command returns an exit status:

- **0**: Success
- **Non-zero**: Failure occurred

This is important for error handling in shell scripts.

## Examples

### Example 1: Creating a Project Directory Structure

**Problem:** You need to create a complete project structure for a web application with the following hierarchy:

```
myproject/
├── src/
│ ├── css/
│ ├── js/
│ └── images/
├── docs/
└── tests/
```

**Solution:**

```bash
mkdir -p myproject/{src/{css,js,images},docs,tests}
```

**Step-by-step explanation:**

1. The `-p` flag ensures all parent directories are created
2. Brace expansion `{a,b,c}` creates multiple subdirectories from a single path
3. This creates all directories in one command instead of multiple commands

**Verification:**

```bash
find myproject -type d
```

Output:

```
myproject
myproject/src
myproject/src/css
myproject/src/js
myproject/src/images
myproject/docs
myproject/tests
```

### Example 2: Creating a Directory with Specific Permissions

**Problem:** Create a secure private directory that only the owner can access.

**Solution:**

```bash
mkdir -m 700 confidential
```

**Step-by-step explanation:**

1. The `7` in 700 represents rwx permissions for the owner (read, write, execute)
2. The first `0` represents no permissions for the group
3. The second `0` represents no permissions for others
4. This ensures complete privacy for the directory

**Verification:**

```bash
ls -ld confidential
```

Output:

```
drwx------ 2 student student 4096 Jan 15 10:30 confidential
```

The `d` at the beginning confirms it's a directory, and the permissions show only the owner has access.

### Example 3: Using mkdir in a Shell Script

**Problem:** Write a script that creates a backup directory with timestamp.

**Solution:**

```bash
#!/bin/bash
# Create backup directory with timestamp

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/home/student/backups/backup_$TIMESTAMP"

# Create directory with parent directories if needed
if mkdir -p "$BACKUP_DIR"; then
 echo "Backup directory created: $BACKUP_DIR"
 exit 0
else
 echo "Failed to create backup directory" >&2
 exit 1
fi
```

**Step-by-step explanation:**

1. Generate a timestamp using the `date` command
2. Construct the full path with the timestamp
3. Use `mkdir -p` to create the directory (safe to run multiple times)
4. Check the exit status using `if` statement
5. Print appropriate messages and return exit codes

**Running the script:**

```bash
chmod +x backup.sh
./backup.sh
```

Output:

```
Backup directory created: /home/student/backups/backup_20240115_143022
```

## Exam Tips

1. **Remember the syntax**: The basic syntax is `mkdir [OPTIONS] DIRECTORY_NAME`. Know that OPTIONS are optional but DIRECTORY_NAME is required.

2. **The -p flag is crucial**: In exams, always use `-p` when creating nested directories. Without it, the command fails if parent directories don't exist.

3. **Default permissions**: Remember that new directories get 755 (rwxr-xr-x) permissions by default, allowing everyone to read and execute but only owner to write.

4. **Error handling**: Know common error messages like "File exists" (directory already present) and "Permission denied" (insufficient privileges).

5. **Difference between -p and without -p**: Without -p, mkdir fails if any part of the path is missing. With -p, it creates all missing parent directories.

6. **Multiple directory creation**: You can create multiple directories in one command: `mkdir dir1 dir2 dir3`.

7. **Exit status matters**: mkdir returns 0 on success and non-zero on failure. This is important for scripting and automation questions.

8. **Symbolic vs Octal mode**: Both `mkdir -m 755` and `mkdir -m u=rwx,go=rx` set the same permissions—know both formats.

9. **Purpose of . and ..**: When creating a directory, the system automatically creates `.` (current) and `..` (parent) entries—understand their significance.

10. **Practical applications**: Be prepared to solve problems like creating directory trees or setting specific permissions in exam scenarios.
