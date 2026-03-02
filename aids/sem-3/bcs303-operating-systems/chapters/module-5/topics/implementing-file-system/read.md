# Unix File System Organization

## Introduction to the Unix File System

The Unix file system is a hierarchical, tree-structured method of organizing files and directories. This structure provides a unified and consistent way to access all data, regardless of the physical storage device. Unlike some operating systems that use drive letters (like C:\, D:\), Unix uses a single root from which all files and directories branch out.

**Key Principle:** "Everything is a file." This includes not only text documents and programs but also hardware devices, directories, and even system processes. This abstraction simplifies many operations.

## The Root Directory (`/`)

The very top of the file system hierarchy is the **root directory**, denoted by a single forward slash (`/`). All other files and directories are descendants of this root.

```
/
```

_Example ASCII Diagram of the Root_

```
    /
    |
    +-- bin
    |
    +-- etc
    |
    +-- home
    |   |
    |   +-- user1
    |   |
    |   +-- user2
    |
    +-- usr
    |
    +-- var
```

## Basic File Types

In Unix, files are categorized into several types. You can identify a file's type using the `ls -l` command; the first character of the permission string indicates the type.

| Type Symbol | Description                                                                                             | Example (`ls -l` output) |
| :---------- | :------------------------------------------------------------------------------------------------------ | :----------------------- |
| `-`         | **Regular File:** Contains data: text, binary, program code, etc. Most common file type.                | `-rw-r--r--`             |
| `d`         | **Directory:** A special file that contains the names of other files and pointers to them. A folder.    | `drwxr-xr-x`             |
| `l`         | **Symbolic Link:** A pointer to another file. Similar to a shortcut in Windows.                         | `lrwxrwxrwx`             |
| `c`         | **Character Special File:** Provides buffered access to hardware devices (e.g., terminals).             | `crw--w----`             |
| `b`         | **Block Special File:** Provides direct, unbuffered access to hardware devices (e.g., hard disks, USB). | `brw-rw----`             |
| `p`         | **Named Pipe (FIFO):** A special file used for inter-process communication (IPC).                       | `prw-------`             |
| `s`         | **Socket:** Another type of file used for network communication between processes.                      | `srwxrwxrwx`             |

## Standard Directory Hierarchy (FHS)

The Filesystem Hierarchy Standard (FHS) defines the structure and purpose of the main directories in a Unix-like system. This standardization ensures consistency across different distributions.

| Directory | Primary Purpose                                                                                                                                                                  |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/bin`    | **Essential user command binaries.** Contains fundamental commands needed for system operation and available to all users (e.g., `ls`, `cp`).                                    |
| `/sbin`   | **Essential system binaries.** Contains commands needed for system administration and repair, typically used by the `root` user (e.g., `ifconfig`, `fsck`).                      |
| `/dev`    | **Device files.** Contains the special files that represent physical and virtual hardware devices (e.g., `/dev/sda` for a disk, `/dev/tty` for a terminal).                      |
| `/etc`    | **Host-specific system configuration files.** Contains administrative configuration files for the system and applications (e.g., `/etc/passwd`, `/etc/hosts`).                   |
| `/home`   | **User home directories.** Each regular user has a subdirectory here (e.g., `/home/alice`) to store their personal files and configurations.                                     |
| `/lib`    | **Essential shared libraries and kernel modules.** Contains code libraries needed by the binaries in `/bin` and `/sbin`.                                                         |
| `/tmp`    | **Temporary files.** A world-writable space for temporary files created by programs and users. Files may be deleted on reboot.                                                   |
| `/usr`    | **Secondary hierarchy.** Contains the majority of user utilities and applications, often read-only. It has its own subdirectories like `/usr/bin`, `/usr/lib`, and `/usr/local`. |
| `/var`    | **Variable data.** Contains files that are expected to change during normal operation (e.g., logs in `/var/log`, mail queues, spool files).                                      |
| `/boot`   | **Static boot loader files.** Contains the kernel and other files needed to boot the operating system.                                                                           |
| `/proc`   | **Virtual filesystem.** Provides a window into kernel data structures and process information. Files here are generated on-the-fly by the kernel.                                |
| `/mnt`    | **Temporary mount point.** A generic location for temporarily mounting filesystems (e.g., a CD-ROM or a USB drive).                                                              |
| `/opt`    | **Add-on application software packages.** Used for installing large, self-contained third-party software applications.                                                           |
| `/root`   | **Home directory for the root user.** This is separate from `/home` for security reasons.                                                                                        |

## The Home Directory and the `$HOME` Variable

Every user on a Unix system is assigned a personal directory called their **home directory**. This is typically located within `/home/` (e.g., `/home/username`). The superuser (`root`) has its home directory at `/root`.

The shell environment uses a special environment variable called `HOME` to keep track of your home directory's location. You can use the tilde (`~`) character as a shortcut for your `$HOME` path.

**Examples:**

- `cd ~` or just `cd` - Changes to your home directory.
- `cd ~/Documents` - Changes to the `Documents` directory inside your home.
- `echo $HOME` - Prints the absolute path to your home directory (e.g., `/home/alice`).

## The `PATH` Variable

The `PATH` is a crucial environment variable that tells the shell which directories to search for executable programs when you type a command. It is a colon-separated (`:`) list of directories.

**Example:** `PATH=/usr/local/bin:/usr/bin:/bin`

When you type a command like `ls`, the shell searches through each directory in the `PATH`, in order, until it finds an executable file named `ls`. If it doesn't find it in any `PATH` directory, you will get a "command not found" error.

- `echo $PATH` - View your current `PATH`.
- You can add a directory to your `PATH` (e.g., for scripts in your home dir): `export PATH=$PATH:~/my_scripts`

## Pathnames: Absolute vs. Relative

A **pathname** is a text string that specifies the location of a unique file or directory in the filesystem.

- **Absolute Pathname:** Begins with a forward slash (`/`). It specifies the complete path from the root directory to the target file.
  - Example: `/home/alice/docs/report.txt`
  - Always refers to the same file, regardless of your current working directory.

- **Relative Pathname:** Does _not_ begin with a slash. It specifies the path relative to your **current working directory**.
  - Special symbols:
    - `.` (dot) - Represents the current directory.
    - `..` (dot-dot) - Represents the parent directory (one level up).
  - Example: If your current directory is `/home/alice`, the relative path `docs/report.txt` refers to the same file as the absolute path above.

## Hidden Files

Any file or directory whose name begins with a dot (`.`) is considered a **hidden file** (or "dotfile"). These are not shown in a normal `ls` listing. They are typically used for user preference files and program configuration.

- `ls -a` - The `-a` (all) option for `ls` shows hidden files.
- Common examples: `.bashrc`, `.profile`, `.ssh/`

## Key Directory and File Commands

| Command  | Description                                                                                                                      | Common Usage Examples                                                         |
| :------- | :------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| `pwd`    | **Print Working Directory.** Displays the absolute path of your current directory.                                               | `pwd`                                                                         |
| `cd`     | **Change Directory.** Moves you to the specified directory.                                                                      | `cd /tmp`, `cd ..`, `cd ~/Documents`                                          |
| `ls`     | **List directory contents.**                                                                                                     | `ls`, `ls -l` (long format), `ls -a` (show hidden)                            |
| `mkdir`  | **Make Directory.** Creates a new directory.                                                                                     | `mkdir new_folder`, `mkdir -p project/docs/images` (`-p` creates parent dirs) |
| `rmdir`  | **Remove Directory.** Removes an empty directory.                                                                                | `rmdir old_folder`                                                            |
| `rm -r`  | **Remove** (with the recursive option). Used to remove directories and their contents recursively. **Use with extreme caution!** | `rm -r directory_name`                                                        |
| `cp`     | **Copy files and directories.**                                                                                                  | `cp file1.txt file2.txt`, `cp -r dir1/ dir2/` (copy recursively)              |
| `mv`     | **Move (or rename) files and directories.**                                                                                      | `mv oldname.txt newname.txt`, `mv file.txt ~/Documents/`                      |
| `find`   | **Search for files in a directory hierarchy.** A very powerful search tool.                                                      | `find /home -name "*.txt"`                                                    |
| `locate` | **Find files by name quickly** using a pre-built database. Faster than `find` but may not have recent changes.                   | `locate report.pdf`                                                           |

## Exam Tips

1.  **Understand the FHS:** Be able to state the purpose of at least the core directories (`/`, `/bin`, `/home`, `/etc`, `/var`, `/usr`). This is a very common question.
2.  **Absolute vs. Relative Paths:** Know the difference cold. Be prepared to write both an absolute and a relative path to the same file from a given current directory.
3.  **File Types:** Remember the symbols from `ls -l` (`-`, `d`, `l`). You will likely be asked to identify a file's type from a long listing.
4.  **`PATH` Variable:** Understand what it does and why it's important. Know how a shell uses it to find commands.
5.  **Command Syntax:** Practice the basic directory navigation and manipulation commands (`cd`, `ls`, `pwd`, `mkdir`, `rmdir`). Remember which commands require the `-r` flag for directories.
6.  **Hidden Files:** Remember they start with a `.` and are viewed with `ls -a`.
