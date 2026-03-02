# Directory Structure, Protection, File System Implementation

**Directory Structure**

- A directory is a collection of files and subdirectories
- File system structure:
  - Root directory (or root node)
  - Subdirectories (or subnodes)
  - Files (or leaf nodes)

**Protection**

- **Access Control Lists (ACLs)**: define permissions for each file and directory
- **Access Control Models**:
  - Discretionary Access Control (DAC)
  - Mandatory Access Control (MAC)
  - Role-Based Access Control (RBAC)

**File System Operations**

- **File Operations**:
  - Create
  - Delete
  - Read
  - Write
  - Copy
  - Move
- **Directory Operations**:
  - Create
  - Delete
  - List
  - Search

**File System Internals**

- **File System Structure**:
  - File allocation tables (FATs)
  - Inode-based file systems
- **File System Algorithms**:
  - File allocation algorithms (e.g. First-Fit, Best-Fit)
  - File searching algorithms (e.g. Linear Search, Binary Search)

**Important Formulas and Definitions**

- **Inode**: a data structure that represents a file or directory in a file system
- **Block size**: the number of bytes allocated to a file or directory
- **Fragmentation**: the waste space between files due to unequal block sizes

**Important Theorems and Concepts**

- **File system consistency**: ensuring that file system state is consistent across all nodes
- **Page table**: a data structure that maps virtual addresses to physical addresses in memory
- **Virtual memory**: a memory management technique that combines physical and virtual memory
