# **Copy-on-Write Revision Notes**

**Definition:**

- Copy-on-write (CoW) is a technique used in operating systems to optimize disk space usage by allowing multiple pointers to a single file without having to create multiple copies.

**Key Points:**

- **How it works:**
  - When a file is opened, only the original file is copied, and subsequent changes are made directly to the original file.
  - A special pointer (called a "copy-on-write" pointer) is created to point to the original file.
- **Advantages:**
  - Reduces the amount of disk space required to store files.
  - Improves performance by reducing the number of disk I/O operations.
- **Disadvantages:**
  - Can lead to unexpected behavior if multiple processes try to modify the file at the same time.
  - Requires careful synchronization to ensure data consistency.

**Important Formulas and Definitions:**

- **Thompson's Algorithm:** A CoW algorithm that ensures data consistency by updating the copy of a file when it's modified.
- **Metadatum:** A piece of information that accompanies a file, such as its size, permissions, and ownership.

**Theorems:**

- **CoW Theorem:** If multiple processes try to modify the same file, the CoW algorithm will ensure data consistency by updating the copy of the file.
- **CoW Invariance:** The CoW algorithm maintains the original file's integrity by making changes directly to it, rather than creating a new copy.

**Important Terms:**

- **Copy-on-write pointer:** A special pointer that points to the original file.
- **Dirty bit:** A flag that indicates whether a file's copy has been modified.
- **Dirty page:** A page in memory that needs to be written back to disk.
