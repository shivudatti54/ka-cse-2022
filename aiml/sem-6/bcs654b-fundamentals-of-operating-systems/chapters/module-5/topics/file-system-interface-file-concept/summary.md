# **File System Interface: File Concept**

### Definitions and Notations

- **File**: A collection of data stored in a physical device, such as a hard drive or solid-state drive.
- **File System**: A set of rules and structures that organize and manage files on a device.
- **File Handle**: A unique identifier for a file, used to access and manipulate its contents.
- **File Descriptor**: A small integer that represents a file descriptor.

### Key Concepts

- **File Types**:

* **Regular Files**: contain data that is not executable (e.g., documents, images)
* **Directory Files**: contain metadata about other files (e.g., subdirectories, files)
* **Special Files**: represent devices or special resources (e.g., terminals, printers)

- **File Operations**:

* **Open**: establish a connection to a file
* **Read**: retrieve data from a file
* **Write**: add data to a file
* **Close**: release a connection to a file

- **File Attributes**:

* **Access Rights**: determine what actions can be performed on a file (e.g., read, write, execute)
* **Permissions**: determine what actions can be performed on a file by which users
* **Ownership**: determine which user or group owns a file

### Important Formulas and Theorems

- **Inode Number Formula**: `inode_number = (block_number * block_size) + offset`
- **File Size Formula**: `file_size = total_blocks * block_size`

### Important Theorems and Propositions

- **The File System Interface Theorem**: states that the file system interface provides a consistent and predictable way of interacting with files.
- **The File Attribute Proposition**: states that file attributes (e.g., access rights, permissions, ownership) determine what actions can be performed on a file.
