# Relative and Absolute Pathnames - Directory Commands

## Introduction

Understanding pathnames is fundamental to working with any file system, especially in Linux/Unix environments. In the context of 's Computer Science curriculum, this topic forms the foundation for shell scripting, system administration, and file management operations. Whether you're navigating through directories, accessing files, or writing automation scripts, mastering both relative and absolute pathnames is essential.

Pathnames provide a way to locate files and directories within the hierarchical file system structure. Every file and directory in Linux has a unique location identified by its path. The two primary methods of specifying these paths are absolute (complete path from root) and relative (path from current directory). This distinction is crucial because the choice between them affects script portability, efficiency, and correctness.

In this chapter, we will explore the conceptual differences between relative and absolute pathnames, understand how the Linux file system hierarchy works, and master essential directory commands that every CSE student must know. These skills are not just academic requirements but practical necessities for any software developer or system administrator.

## Key Concepts

### File System Hierarchy

Linux uses a hierarchical directory structure starting from the root directory, denoted by "/". All files and directories branch out from this single root point. The standard Linux directory structure includes important system directories that every user should understand:

- **/** (root): The topmost directory in the entire file system
- **/bin**: Essential user binaries (basic commands)
- **/boot**: Boot files and kernel
- **/etc**: System configuration files
- **/home**: User home directories (where regular users store their files)
- **/root**: Home directory for the root user (system administrator)
- **/tmp**: Temporary files (accessible by all users)
- **/usr**: User programs and utilities
- **/var**: Variable data files (logs, caches, etc.)
- **/dev**: Device files (hardware representations)
- **/proc**: Virtual file system (process and kernel information)

### Absolute Pathnames

An absolute path (also known as full path) is the complete path of a file or directory starting from the root directory. It always begins with a forward slash "/" and provides the exact location of the file regardless of the current working directory. For example:

- `/home/student/documents/project.txt`
- `/var/log/syslog`
- `/etc/passwd`

The key characteristic of absolute paths is that they remain the same no matter where you are in the file system. This makes them unambiguous and reliable for scripting and configuration files.

### Relative Pathnames

A relative path specifies the location of a file or directory relative to the current working directory. It does not start with "/" and depends entirely on where you currently are in the file system. For example, if your current directory is `/home/student`, then `documents/project.txt` refers to `/home/student/documents/project.txt`.

Common relative path notations include:

- **Current directory (.)**: The present working directory, e.g., `./script.sh`
- **Parent directory (..)**: One level up in the hierarchy, e.g., `../documents`
- **Home directory (~)**: The user's home directory, e.g., `~/downloads`

### Current Working Directory

The current working directory (CWD) is the directory in which the user is currently working. It is an essential concept because all relative paths are interpreted relative to this location. The shell maintains this information and updates it with each `cd` command.

You can determine your current working directory using the `pwd` command, and you can change it using the `cd` command. Understanding the current working directory is crucial for working with relative paths effectively.

### Special Directory References

Linux provides several special characters that simplify path navigation:

- **Dot (.)**: Represents the current directory
- **Double Dot (..)**: Represents the parent directory (one level up)
- **Tilde (~)**: Represents the current user's home directory
- **Hyphen (-)**: When used with cd, represents the previous working directory

## Directory Commands

### pwd - Print Working Directory

The `pwd` command displays the absolute path of the current working directory. This is particularly useful when you need to verify your location before performing operations with relative paths.

Syntax: `pwd [options]`

Common options:

- `-L`: Print logical path (default)
- `-P`: Print physical path (without symbolic links)

Example:

```
$ pwd
/home/student
```

### cd - Change Directory

The `cd` command is used to change the current working directory. It is one of the most frequently used commands in Linux.

Syntax: `cd [directory]`

Examples:

```
$ cd /home/student/Documents # Using absolute path
$ cd Documents # Using relative path (subdirectory)
$ cd .. # Move to parent directory
$ cd ../.. # Move up two levels
$ cd ~ # Go to home directory
$ cd # Go to home directory (same as above)
$ cd - # Change to previous directory
```

### ls - List Directory Contents

The `ls` command displays information about files and directories. It is essential for navigating and exploring the file system.

Syntax: `ls [options] [file/directory]`

Common options:

- `-l`: Use long listing format (detailed information)
- `-a`: Show all files including hidden files (starting with .)
- `-d`: List directory entries instead of contents
- `-R`: List subdirectories recursively
- `-h`: Human-readable file sizes

Examples:

```
$ ls # List files in current directory
$ ls -l # Detailed listing
$ ls -a # Show hidden files
$ ls -la # Combined detailed and hidden
$ ls /home/student # List contents of specific directory
$ ls -R # Recursive listing
```

### mkdir - Make Directory

The `mkdir` command creates new directories in the file system.

Syntax: `mkdir [options] directory_name`

Common options:

- `-p`: Create parent directories as needed (no error if existing)
- `-v`: Print message for each created directory

Examples:

```
$ mkdir newfolder # Create single directory
$ mkdir -p path/to/nested/directory # Create nested structure
$ mkdir -p project/{src,bin,doc} # Create multiple directories at once
```

### rmdir - Remove Directory

The `rmdir` command removes empty directories from the file system.

Syntax: `rmdir [options] directory_name`

Common options:

- `-p`: Remove parent directories if they become empty

Examples:

```
$ rmdir empty_folder
$ rmdir -p path/to/empty/folder # Remove empty parent directories
```

Note: `rmdir` only works on empty directories. To remove non-empty directories, use `rm -r`.

## Examples

### Example 1: Navigating a Project Structure

Consider a project located at `/home/student/project` with the following directory structure:

```
project/
├── src/
│ ├── main.c
│ └── utils.c
├── include/
│ └── utils.h
├── build/
│ └── output
└── docs/
 └── readme.txt
```

Starting from `/home/student/project`, let's navigate:

1. From `src/`, access `main.c`: Simply use `main.c` (in same directory) or `./main.c`
2. From `src/`, access `utils.h` in `include/`: Use `../include/utils.h`
3. From `src/`, access `output` in `build/`: Use `../build/output`
4. From `build/`, access `main.c` in `src/`: Use `../src/main.c`

### Example 2: Creating Nested Directories with mkdir -p

To set up a complete project structure in one command:

```
$ mkdir -p myproject/{src,include,build,lib,bin,doc,test}
$ tree myproject
myproject/
├── bin/
├── build/
├── doc/
├── include/
├── lib/
├── src/
└── test/
```

### Example 3: Practical Path Operations in a Session

```
$ pwd # Check current directory
/home/student

$ cd /var/log # Navigate using absolute path
$ pwd
/var/log

$ cd ~ # Return to home directory
$ pwd
/home/student

$ cd - # Go back to previous directory
/var/log

$ pwd
/var/log

$ cd ../.. # Go up two levels
$ pwd
/
```

### Example 4: Understanding Path Resolution

When using relative paths, understanding resolution is crucial:

- If current directory is `/home/student`, then `../etc` resolves to `/etc`
- If current directory is `/home/student/Downloads`, then `../documents` resolves to `/home/student/documents`
- If current directory is `/var`, then `./log` resolves to `/var/log`

## Exam Tips

1. **Remember the root symbol**: Absolute paths always start with "/" (e.g., /home/user), while relative paths never start with "/".

2. **"." means current directory**: Use "./file" to reference a file in the current directory or execute a script in the current directory.

3. **".." means parent directory**: Use "../" to move up one level in the directory hierarchy.

4. **Tilde (~) shortcut**: The tilde always refers to the home directory, independent of current location. Use it for quick navigation to personal directories.

5. **pwd is diagnostic**: Always use pwd to verify your current directory before using relative paths in both practice and exams.

6. **mkdir -p for nested dirs**: The -p flag creates parent directories as needed and doesn't error if they already exist.

7. **cd - for toggle**: Use "cd -" to quickly switch between your current and previous directory - very useful in exams.

8. **Hidden files**: Files starting with "." are hidden; use ls -a to see them in directory listings.

9. **Path length matters**: Absolute paths are longer but more reliable; relative paths are shorter but context-dependent.

10. **Practice common combinations**: Commands like `cd ..`, `cd ~`, `ls -la`, `mkdir -p` are frequently used together in Linux operations.

## Important Commands Summary

- **pwd**: Print Working Directory - shows current location
- **cd [path]**: Change Directory - navigate to specified path
- **ls [options] [path]**: List directory contents
- **mkdir [options] [path]**: Create new directory
- **rmdir [path]**: Remove empty directory
