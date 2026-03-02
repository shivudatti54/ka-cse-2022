# **Basic File Types and Categories**

## **Introduction**

In UNIX, files are the basic building blocks of the file system. Understanding the different types of files and categories is essential for efficient file management and programming. In this section, we will explore the basic file types and categories in UNIX.

## **Types of Files**

### 1. Regular Files

- Definition: Regular files are the most common type of file in UNIX. They contain data that can be read and written.
- Characteristics:
  - Contain data (e.g., text, images, executable programs)
  - Can be read and written by the owner, group, and others
  - Have a file type associated with them (e.g., text, binary)
- Examples:
  - `example.txt` (a text file)
  - `image.jpg` (an image file)
  - `script.sh` (an executable program)

### 2. Directory Files

- Definition: Directory files, also known as directories, are used to store and organize other files.
- Characteristics:
  - Contain metadata about other files (e.g., file names, permissions)
  - Used to create new directories and files
  - Have a `/` symbol at the beginning of the name (e.g., `/home/user/documents`)
- Examples:
  - `/home/user/documents` (a directory)
  - `/var/log` (a log directory)

### 3. Symbolic Links

- Definition: Symbolic links are pointers to other files or directories.
- Characteristics:
  - Point to a file or directory
  - Can be used to create shortcuts or aliases
  - Can be changed or deleted
- Examples:
  - `ln -s /usr/bin/ls /usr/bin/linked_ls` (a symbolic link to `ls`)
  - `ln -s /home/user/documents /usr/local/documents` (a symbolic link to a directory)

### 4. Special Files

- Definition: Special files are system files that perform special actions when accessed.
- Characteristics:
  - Represent a device or a process
  - Used to interact with devices (e.g., disk, network)
  - Used to interact with processes (e.g., ps, kill)
- Examples:
  - `/dev/sda1` (a partition device)
  - `/proc/cpuinfo` (process information file)

## **File Categories**

### 1. File Creation Time

- Definition: Files are categorized based on when they were created.
- Characteristics:
  - New files are created with a creation time
  - Files can be modified to change their creation time
- Examples:
  - `touch example.txt` (creates a new file with the current time)
  - `stat -c "%Y" example.txt` (prints the creation time of the file)

### 2. File Modification Time

- Definition: Files are categorized based on when they were last modified.
- Characteristics:
  - Files can be modified to change their modification time
  - Files can be checked to see when they were last modified
- Examples:
  - `touch example.txt` (modifies the creation time of the file)
  - `stat -c "%M" example.txt` (prints the modification time of the file)

### 3. File Access Time

- Definition: Files are categorized based on when they were last accessed.
- Characteristics:
  - Files can be modified to change their access time
  - Files can be checked to see when they were last accessed
- Examples:
  - `touch example.txt` (modifies the access time of the file)
  - `stat -c "%X" example.txt` (prints the access time of the file)

## **Key Concepts**

- File type: The type of file (e.g., text, binary, directory)
- File category: A way to categorize files based on characteristics (e.g., creation time, modification time)
- Symbolic link: A pointer to another file or directory
- Special file: A system file that performs a special action when accessed
- File metadata: Information about a file (e.g., file name, permissions, creation time)

## **Practice Exercises**

1.  Create a new file called `example.txt` and modify its creation time using `touch example.txt`.
2.  Create a symbolic link to `ls` using `ln -s /usr/bin/ls /usr/bin/linked_ls`.
3.  Check the file metadata of `example.txt` using `stat -c "%Y %M %X" example.txt`.
