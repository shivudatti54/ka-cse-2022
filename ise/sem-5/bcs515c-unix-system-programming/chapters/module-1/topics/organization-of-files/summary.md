# **Organization of Files**

### Overview

- The UNIX file system is a hierarchical system that organizes files and directories in a tree-like structure.
- The file system is based on the concept of a root directory, which serves as the top-most directory in the hierarchy.

### Key Concepts

- **Directory**: A directory is a container that holds files and other directories.
- **Filesystem**: A filesystem is the collection of directories and files that make up the file system.
- **Path**: A path is a sequence of directories that locate a file or directory.
- **File attributes**: Files can have attributes such as permissions, ownership, and timestamps.

### Filesystem Structure

- **Root directory** ( `/` ): The top-most directory in the hierarchy.
- **Home directory** ( `~` ): The personal directory of a user.
- **Current working directory** ( `cwd` ): The directory from which commands are executed.

### Filesystem Hierarchy

| Directory | Description               |
| --------- | ------------------------- |
| `/`       | Root directory            |
| `~`       | Home directory            |
| `.`       | Current working directory |
| `..`      | Parent directory          |

### File permissions

- **Read (r)**: The file can be read by the owner and others.
- **Write (w)**: The file can be written by the owner and others.
- **Execute (x)**: The file can be executed by the owner and others.

### Formulae and Theorems

- **Filesystem hierarchy standard (FHS)**: A standard for the organization of the filesystem.
- **Inodes**: A data structure that represents a file or directory in the filesystem.

### Important Commands

- ` pwd`: Prints the current working directory.
- ` cd`: Changes the current working directory.
- ` ls`: Lists files and directories in the current directory.
- ` mkdir`: Creates a new directory.
- ` rm`: Removes a file or directory.
