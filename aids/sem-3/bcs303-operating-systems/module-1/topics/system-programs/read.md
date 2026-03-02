# System Programs


## Table of Contents

- [System Programs](#system-programs)
- [Introduction](#introduction)
- [Categories of System Programs](#categories-of-system-programs)
  - [1. File Management](#1-file-management)
  - [2. Status Information](#2-status-information)
  - [3. File Modification](#3-file-modification)
  - [4. Programming Language Support](#4-programming-language-support)
  - [5. Program Loading and Execution](#5-program-loading-and-execution)
  - [6. Communications](#6-communications)
  - [7. Background Services / Daemons](#7-background-services--daemons)
- [System Programs vs Application Programs](#system-programs-vs-application-programs)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

**System programs** (also called **system utilities**) provide a convenient environment for program development and execution. They sit between the operating system kernel and application programs, offering useful services and tools that most users associate with "the operating system."

> **Definition:** System programs are programs that are shipped with the operating system but are not part of the kernel. They provide a convenient environment for program development and execution, and define most of the user's view of the operating system.

Most users' view of the operating system is defined by the system programs rather than the actual system calls. For example, when a user types `ls` or `copy`, they are using a system program -- not directly invoking a system call.

```
+------------------------------------------+
| User's View of the OS |
+------------------------------------------+
| |
| System Programs (utilities) |
| - File managers, editors, compilers |
| - What users actually interact with |
| |
+------------------------------------------+
| |
| System Calls |
| - Hidden from the user |
| - Used internally by system programs |
| |
+------------------------------------------+
| |
| Kernel |
| - Core OS functionality |
| |
+------------------------------------------+
```

## Categories of System Programs

System programs can be divided into the following categories:

### 1. File Management

Programs that create, delete, copy, rename, print, list, and manipulate files and directories.

| Program          | UNIX/Linux | Windows       | Description                |
| ---------------- | ---------- | ------------- | -------------------------- |
| List files       | `ls`       | `dir`         | Display directory contents |
| Copy file        | `cp`       | `copy`        | Copy files                 |
| Move/Rename      | `mv`       | `move`, `ren` | Move or rename files       |
| Delete           | `rm`       | `del`         | Delete files               |
| Create directory | `mkdir`    | `mkdir`       | Create new directory       |
| Remove directory | `rmdir`    | `rmdir`       | Remove directory           |
| Find files       | `find`     | `where`       | Search for files           |
| File permissions | `chmod`    | `icacls`      | Change file permissions    |

**Example:**

```bash
$ ls -la # List all files with details
$ cp source.txt dest.txt # Copy a file
$ mv old.txt new.txt # Rename a file
$ rm unwanted.txt # Delete a file
$ mkdir projects # Create a directory
```

### 2. Status Information

Programs that query the system for date, time, available memory, disk space, number of users, and similar status information. Some systems also provide a **registry** for storing and retrieving configuration information.

| Program      | UNIX/Linux         | Windows        | Description                   |
| ------------ | ------------------ | -------------- | ----------------------------- |
| Date/Time    | `date`             | `date`, `time` | Display current date and time |
| Disk usage   | `df`, `du`         | `chkdsk`       | Show disk space usage         |
| Memory info  | `free`             | `systeminfo`   | Display memory usage          |
| Process list | `ps`, `top`        | `tasklist`     | Show running processes        |
| System info  | `uname -a`         | `systeminfo`   | Display system information    |
| User info    | `who`, `w`         | `query user`   | Show logged-in users          |
| Performance  | `vmstat`, `iostat` | `perfmon`      | Performance statistics        |

**Example:**

```bash
$ date # Show current date and time
$ df -h # Show disk space in human-readable format
$ free -m # Show memory usage in MB
$ ps aux # Show all running processes
$ uname -a # Show system information
```

### 3. File Modification

Programs that allow creating and modifying the content of files (text editors and similar tools).

| Program         | UNIX/Linux          | Windows   | Description                     |
| --------------- | ------------------- | --------- | ------------------------------- |
| Text editor     | `vi`, `vim`, `nano` | `notepad` | Edit text files                 |
| Stream editor   | `sed`               | -         | Automated text transformations  |
| Text search     | `grep`              | `findstr` | Search text within files        |
| Text processing | `awk`               | -         | Pattern scanning and processing |
| Comparison      | `diff`              | `fc`      | Compare files                   |

**Example:**

```bash
$ vim report.txt # Edit a file using vim
$ grep "error" logfile.txt # Search for "error" in a file
$ sed 's/old/new/g' file # Replace "old" with "new" in a file
$ diff file1.txt file2.txt # Compare two files
```

### 4. Programming Language Support

Compilers, assemblers, debuggers, and interpreters for common programming languages are provided as system programs.

| Tool             | Examples                 | Description                                 |
| ---------------- | ------------------------ | ------------------------------------------- |
| **Compilers**    | `gcc`, `g++`, `javac`    | Translate source code to machine code       |
| **Assemblers**   | `as`, `nasm`             | Translate assembly language to machine code |
| **Interpreters** | `python`, `perl`, `ruby` | Execute source code directly                |
| **Debuggers**    | `gdb`, `lldb`            | Debug programs step by step                 |
| **Linkers**      | `ld`                     | Link object files into executables          |
| **Build tools**  | `make`, `cmake`          | Automate compilation process                |

**Example:**

```bash
$ gcc -o program source.c # Compile C program
$ javac Main.java # Compile Java program
$ python script.py # Run Python script
$ gdb ./program # Debug a program
$ make # Build using Makefile
```

### 5. Program Loading and Execution

Once a program is compiled (or assembled), it must be loaded into memory to be executed. The system provides loaders, linkers, and debuggers for this purpose.

```
Source Code --> Compiler --> Object File --> Linker --> Executable
 |
 Loader
 |
 Memory
 (Execute)
```

| Tool                   | Description                                                     |
| ---------------------- | --------------------------------------------------------------- |
| **Absolute loader**    | Loads program at a fixed memory address                         |
| **Relocatable loader** | Can load program at any available memory address                |
| **Linkage editor**     | Combines object modules and resolves references                 |
| **Dynamic linker**     | Links shared libraries at runtime (`ld.so` in Linux)            |
| **Overlay loader**     | Loads portions of a program as needed (for limited memory)      |
| **Debugger**           | Allows step-by-step execution, breakpoints, variable inspection |

### 6. Communications

Programs that provide mechanisms for creating virtual connections among processes, users, and computer systems.

| Program          | UNIX/Linux           | Description                         |
| ---------------- | -------------------- | ----------------------------------- |
| Remote login     | `ssh`, `telnet`      | Log into a remote machine           |
| File transfer    | `ftp`, `scp`, `sftp` | Transfer files between machines     |
| Web browsing     | `curl`, `wget`       | Download from the web               |
| Email            | `mail`, `sendmail`   | Send and receive email              |
| Messaging        | `write`, `wall`      | Send messages to users              |
| Remote execution | `rsh`, `ssh`         | Execute commands on remote machines |

**Example:**

```bash
$ ssh user@server.com # Remote login via SSH
$ scp file.txt user@host:/path # Copy file to remote machine
$ wget https://example.com/file # Download a file
$ mail user@example.com # Send email
```

### 7. Background Services / Daemons

System programs that run in the background (started at boot time) and provide ongoing services. In UNIX/Linux, these are called **daemons**; in Windows, they are called **services**.

| Daemon                        | Purpose                                      |
| ----------------------------- | -------------------------------------------- |
| `httpd` / `apache2` / `nginx` | Web server                                   |
| `sshd`                        | Secure Shell server                          |
| `cron` / `crond`              | Scheduled task execution                     |
| `syslogd` / `rsyslog`         | System logging                               |
| `init` / `systemd`            | System initialization and service management |
| `named` / `bind`              | DNS server                                   |
| `smbd`                        | Samba file sharing                           |
| `cupsd`                       | Print server                                 |
| `dhcpd`                       | DHCP server                                  |
| `nfsd`                        | Network File System server                   |

**Characteristics of daemons:**

- Run in the background without user interaction
- Started automatically at system boot
- Provide system-wide services
- Typically run with elevated (root) privileges
- Can be managed using `systemctl` (systemd) or `service` commands

```bash
$ systemctl start httpd # Start web server daemon
$ systemctl status sshd # Check SSH daemon status
$ systemctl enable cron # Enable cron daemon at boot
$ systemctl stop nginx # Stop nginx daemon
```

## System Programs vs Application Programs

| Feature                 | System Programs                           | Application Programs                 |
| ----------------------- | ----------------------------------------- | ------------------------------------ |
| **Purpose**             | Provide system utilities and environment  | Solve specific user problems         |
| **Shipped with**        | The operating system                      | Installed separately by users        |
| **Examples**            | Compilers, editors, file managers, shells | Word processors, games, web browsers |
| **User**                | System administrators, developers         | End users                            |
| **Interaction with OS** | Direct, through system calls              | Through system programs and APIs     |

## Summary

```
+--------------------------------------------------+
| System Programs - Categories |
+--------------------------------------------------+
| 1. File Management | ls, cp, mv, rm, mkdir |
| 2. Status Information | date, df, ps, top |
| 3. File Modification | vi, nano, grep, sed |
| 4. Programming Support | gcc, gdb, make, python |
| 5. Program Loading | Loaders, linkers |
| 6. Communications | ssh, ftp, scp, mail |
| 7. Background Services | httpd, sshd, cron |
+--------------------------------------------------+
```

## Exam Tips

1. **Seven categories of system programs** is a standard question. Memorize all seven with at least 2 examples each.
2. **System programs vs system calls:** Understand that users interact with system programs (like `ls`, `cp`), which internally use system calls. Users rarely invoke system calls directly.
3. **Daemons/background services:** Know what a daemon is, give examples (httpd, sshd, cron), and explain that they run at boot time without user interaction.
4. **Loaders and linkers:** Understand the compilation-linking-loading pipeline. Know the difference between absolute and relocatable loaders.
5. ** commonly asks:** "List and explain the categories of system programs" or "Differentiate between system programs and application programs."
6. **Remember the user's perspective:** Most users equate the operating system with its system programs. The kernel is invisible to them.
7. **UNIX examples are preferred** in answers since the textbook (Silberschatz) uses UNIX/Linux examples extensively.
