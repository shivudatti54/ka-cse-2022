# Directory Structure in Operating Systems

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

A **directory** (also called a **folder**) is a fundamental component of any file system that organizes and manages files on storage devices. In operating systems, directories serve as containers that group related files together, providing a logical organization scheme that enables users and applications to locate, access, and manage data efficiently.

Think of a directory as a digital filing cabinet. Just as a physical filing cabinet contains drawers (directories) that hold folders (subdirectories) with documents (files), a computer's directory structure organizes billions of files into a manageable hierarchy. Without directories, finding a specific file among millions would be like searching for a needle in a haystack.

### Real-World Relevance

Consider your own computer:

- Your **Documents** folder contains subfolders for **Work**, **Personal**, and **Studies**
- The **Studies** folder might contain course-specific subdirectories like **Operating Systems**, **Data Structures**, and **Database Management**
- Each course folder contains lecture notes, assignments, and reference materials

This hierarchical organization mirrors how businesses organize their offices—with departments, sub-departments, and individual files. Modern operating systems like Windows, macOS, and Linux all rely on directory structures to manage files effectively.

In the context of the Delhi University BSc (Hons) Computer Science curriculum (NEP 2024 UGCF), understanding directory structures is essential for grasping file system design, memory management, and system programming concepts.

---

## 2. The Need for Directory Structure

Before diving into specific directory structures, it's crucial to understand **why** we need them:

1. **File Organization**: Directories provide a logical grouping mechanism for related files
2. **Name Isolation**: Different users can have files with the same name in different directories
3. **Efficient Search**: Hierarchical structures reduce the time needed to locate files
4. **Security and Access Control**: Directories can have different permission levels
5. **Modularity**: Users can organize their work without interfering with others

---

## 3. Types of Directory Structures

Operating systems have evolved several approaches to organizing directories, each with distinct advantages and limitations.

### 3.1 Single-Level Directory

The simplest form of directory structure is the **single-level directory**, where all files are stored in a single, flat directory.

**Characteristics:**
- Only one directory containing all files
- No subdirectories whatsoever
- Also known as the **root directory** in its simplest form

**Advantages:**
- Simple to implement
- Fast file access (no path traversal needed)
- Minimal overhead

**Disadvantages:**
- Naming conflicts: Cannot have two files with the same name
- Difficult to organize related files
- Becomes unwieldy as the number of files grows

**Example:**
```
/
├── file1.txt
├── file2.txt
├── program.exe
├── data.dat
└── notes.txt
```

**Practical Implementation:**

```c
// Simple single-level directory entry structure
struct directory_entry {
    char filename[256];      // File name
    int file_size;           // File size in bytes
    int starting_block;      // Starting block on disk
    char creation_date[20];  // Creation timestamp
};
```

In early computing (like early versions of MS-DOS or CP/M), single-level directories were common due to limited memory and storage constraints.

---

### 3.2 Two-Level Directory

The **two-level directory** structure addresses the naming conflict problem by introducing separate directories for each user.

**Characteristics:**
- One root directory containing user-specific directories
- Each user has their own private directory (also called a **user file directory** or UFD)
- A **master file directory** (MFD) indexes all user directories

**Advantages:**
- Eliminates naming conflicts between users
- Provides basic user isolation
- Simple implementation with moderate organization

**Disadvantages:**
- Users cannot create subdirectories within their own directories
- Limited flexibility in file organization
- No sharing of files between users

**Example:**
```
/
├── MFD (Master File Directory)
│   ├── User: Alice
│   │   ├── document.txt
│   │   └── program.py
│   ├── User: Bob
│   │   ├── notes.txt
│   │   └── data.csv
│   └── User: Charlie
│       └── project.doc
```

**Implementation Structure:**

```c
// Master File Directory Entry
struct mfd_entry {
    char username[50];
    struct ufd_entry *user_directory;  // Pointer to User File Directory
};

// User File Directory Entry
struct ufd_entry {
    char filename[256];
    int file_size;
    int permissions;        // Read/Write/Execute flags
};
```

---

### 3.3 Hierarchical (Tree-Structured) Directory

The **hierarchical directory structure** (also called **tree-structured directory**) is the most common structure used in modern operating systems. It extends the two-level approach by allowing unlimited levels of subdirectories.

**Characteristics:**
- A tree-like structure with one root directory
- Each directory can contain files and subdirectories
- Parent-child relationships between directories
- Unlimited depth (limited by system constraints)

**Advantages:**
- Excellent organization capability
- Users can create any level of subdirectories
- Natural grouping of related files
- Supports logical file categorization

**Disadvantages:**
- More complex to implement
- Path traversal takes time
- Potential for "directory cycles" that must be handled

**Example:**
```
/
├── home/
│   └── student/
│       ├── Documents/
│       │   ├── University/
│       │   │   ├── OperatingSystems/
│       │   │   │   ├── lecture1.pdf
│       │   │   │   └── assignment1.txt
│       │   │   └── DataStructures/
│       │   └── Personal/
│       │       └── diary.txt
│       ├── Downloads/
│       │   └── software.zip
│       └── Pictures/
│           └── vacation.jpg
└── etc/
    └── configuration files
```

---

### 3.4 Acyclic-Graph Directory

The **acyclic-graph directory** allows directories to share subdirectories and files, creating a directed graph structure without cycles.

**Characteristics:**
- Multiple paths can refer to the same file or directory
- Implements **file sharing** between directories
- No cycles (no infinite loops when traversing)
- Uses **link** mechanisms (like symbolic links in Linux)

**Advantages:**
- Enables file and directory sharing
- Saves disk space (shared files don't need duplicates)
- Multiple users can access the same files

**Disadvantages:**
- More complex traversal algorithms
- Requires reference counting for deletion
- Can cause confusion with multiple paths to the same file

**Example:**
```
/
├── home/
│   └── student/
│       ├── Documents/  (shared with /shared/)
│       │   └── report.txt
│       └── Shared/    (link to /shared/)
│
└── shared/             (actual location)
    └── report.txt      (single copy on disk)
```

In this structure, `/home/student/Documents/report.txt` and `/shared/report.txt` point to the same file.

**Implementation with Links:**

```c
// Directory entry with link count
struct dir_entry {
    char name[256];
    int inode_number;          // Index to i-node (file metadata)
    int link_count;            // Number of hard links to this file
    char type;                 // 'F' for file, 'D' for directory, 'L' for link
    char target[256];          // For symbolic links: target path
};

// When deleting a file:
void delete_file(struct dir_entry *entry) {
    entry->link_count--;
    if (entry->link_count == 0) {
        // Actually free the disk space
        free_inode(entry->inode_number);
    }
}
```

---

### 3.5 Network (General Graph) Directory

The **network directory** (or general graph structure) extends the acyclic-graph by allowing cycles—directories can reference themselves or create circular dependencies.

**Characteristics:**
- Most flexible structure
- Allows cycles in the directory graph
- Used in distributed file systems and network environments
- Requires sophisticated traversal algorithms (like reference counting with garbage collection)

**Advantages:**
- Maximum flexibility for file sharing
- Suitable for networked and distributed systems
- Enables complex organizational structures

**Disadvantages:**
- Complex to implement
- Risk of infinite loops during traversal
- Difficult to determine when to delete shared resources

**Example (Symbolic Links creating cycles):**
```
/
├── home/
│   └── user1/
│       ├── mydocs/  → ../../shared/
│       └── shared/  → ../../home/user2/common/
│
├── home/
│   └── user2/
│       └── common/  → ../../home/user1/mydocs/
```

This creates a cycle between user directories, which is possible in systems like UNIX with symbolic links.

**Traversal with Cycle Detection:**

```c
// Cycle detection during directory traversal
#define MAX_VISITED 1000

int visited_inodes[MAX_VISITED];
int visited_count = 0;

int detect_cycle(int inode) {
    for (int i = 0; i < visited_count; i++) {
        if (visited_inodes[i] == inode) {
            return 1;  // Cycle detected!
        }
    }
    if (visited_count < MAX_VISITED) {
        visited_inodes[visited_count++] = inode;
    }
    return 0;  // No cycle
}
```

---

## 4. Directory Operations

Operating systems provide a set of primitive operations for creating, managing, and navigating directories. Understanding these operations is crucial for file system manipulation.

### 4.1 Create Directory

Creates a new directory in the file system.

```bash
# Linux/Unix
mkdir directory_name
mkdir -p /path/to/new/directory

# Windows
mkdir directory_name
```

### 4.2 Delete Directory

Removes an empty directory (or directory tree with contents).

```bash
# Linux/Unix - remove empty directory
rmdir directory_name

# Linux/Unix - remove directory and contents
rm -r directory_name

# Windows
rmdir directory_name
rd /s directory_name  # with contents
```

### 4.3 List Directory

Displays the contents of a directory.

```bash
# Linux/Unix
ls              # Basic list
ls -l           # Detailed list with permissions
ls -la          # Include hidden files
ls -R           # Recursive listing

# Windows
dir
dir /a          # Include hidden files
```

### 4.4 Change Directory

Navigates between directories.

```bash
# Linux/Unix
cd /path/to/directory
cd ..          # Go to parent directory
cd ~           # Go to home directory

# Windows
cd \path\to\directory
cd ..          # Go to parent directory
```

### 4.5 Rename Directory

Changes the name of a directory.

```bash
# Linux/Unix
mv old_name new_name

# Windows
ren old_name new_name
```

### 4.6 Search Directory

Locates files or directories matching criteria.

```bash
# Linux/Unix
find /path -name "filename"
find . -type d -name "dirname"
grep -r "pattern" /directory

# Windows
dir /s filename
```

---

## 5. Path Conventions

Paths define the location of files and directories in the file system hierarchy. There are two primary types:

### 5.1 Absolute Path

An **absolute path** starts from the root directory and provides the complete path to a file or directory.

**Examples:**
- Linux/Unix: `/home/student/Documents/notes.txt`
- Windows: `C:\Users\Student\Documents\notes.txt`

**Characteristics:**
- Always starts from root (/)
- Same regardless of current working directory
- Unambiguous location reference
- Typically longer than relative paths

### 5.2 Relative Path

A **relative path** is defined relative to the current working directory.

**Examples:**
- If current directory is `/home/student`:
  - `Documents/notes.txt` refers to `/home/student/Documents/notes.txt`
  - `../student2/file.txt` refers to `/home/student2/file.txt`

**Key Symbols:**
- `.` (dot) — current directory
- `..` (double dot) — parent directory

**Common Usage in Code:**

```python
# Python - Path operations
import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Construct paths
absolute_path = os.path.abspath("notes.txt")
print(f"Absolute path: {absolute_path}")

# Check if path is absolute
print(f"Is absolute: {os.path.isabs('/home/student')}")

# Join paths correctly
full_path = os.path.join("/home", "student", "Documents", "file.txt")
print(f"Joined path: {full_path}")

# Get parent directory
parent = os.path.dirname("/home/student/Documents/file.txt")
print(f"Parent: {parent}")
```

---

## 6. Implementation Details

### 6.1 Directory Implementation Methods

#### Linear List (Array-based)

The simplest implementation stores all directory entries in a linear list.

```c
struct directory {
    char name[256];
    struct dir_entry entries[1000];  // Array of entries
    int entry_count;
};

// Linear search to find a file
struct dir_entry* find_file(struct directory *dir, char *filename) {
    for (int i = 0; i < dir->entry_count; i++) {
        if (strcmp(dir->entries[i].filename, filename) == 0) {
            return &dir->entries[i];
        }
    }
    return NULL;  // Not found
}
```

**Time Complexity:** O(n) where n is the number of entries

#### Hash Table

A more efficient implementation uses hash tables for O(1) average lookup time.

```c
#define TABLE_SIZE 256

struct hash_entry {
    char filename[256];
    struct file_metadata *metadata;
    struct hash_entry *next;  // For collision handling
};

struct directory {
    struct hash_entry *hash_table[TABLE_SIZE];
};

// Hash function
int hash_function(char *filename) {
    int sum = 0;
    for (int i = 0; filename[i] != '\0'; i++) {
        sum += filename[i];
    }
    return sum % TABLE_SIZE;
}

struct dir_entry* find_file(struct directory *dir, char *filename) {
    int index = hash_function(filename);
    struct hash_entry *entry = dir->hash_table[index];
    
    while (entry != NULL) {
        if (strcmp(entry->filename, filename) == 0) {
            return entry->metadata;
        }
        entry = entry->next;
    }
    return NULL;
}
```

**Time Complexity:** O(1) average, O(n) worst case

### 6.2 I-Node Based Implementation

Modern UNIX-like systems use **i-nodes** (index nodes) to store file metadata:

```c
struct inode {
    short inode_number;
    short file_type;        // Regular file, directory, special
    short link_count;       // Number of hard links
    short uid;              // Owner user ID
    short gid;              // Owner group ID
    long file_size;         // File size in bytes
    long creation_time;
    long modification_time;
    long access_time;
    short block_pointers[15]; // Pointers to data blocks
    short single_indirect;    // Single indirect block pointer
    short double_indirect;    // Double indirect block pointer
};
```

Each directory entry contains only the filename and the inode number, making directory traversal efficient.

---

## 7. Multiple Choice Questions

### MCQ 1: Which directory structure allows multiple paths to the same file?

A) Single-Level Directory  
B) Two-Level Directory  
C) Hierarchical Directory  
D) Acyclic-Graph Directory  

**Answer: D**  
The acyclic-graph directory allows multiple directory entries to point to the same file through hard links, without creating cycles in the directory structure.

---

### MCQ 2: What is the main disadvantage of a single-level directory structure?

A) Slow file access  
B) Difficulty in implementation  
C) Naming conflicts  
D) No security features  

**Answer: C**  
Single-level directories cannot have two files with the same name, leading to naming conflicts as the number of files grows.

---

### MCQ 3: Which symbol represents the parent directory in relative paths?

A) `.`  
B) `~`  
C) `..`  
D) `/`  

**Answer: C**  
The `..` symbol represents the parent directory in relative path notation. The single dot `.` represents the current directory.

---

### MCQ 4: In a tree-structured directory, what is the "root" directory?

A) The directory containing the most files  
B) The topmost directory in the hierarchy  
C) The directory with the longest path  
D) The current working directory  

**Answer: B**  
The root directory is the topmost directory in the hierarchical structure. All other directories branch from it.

---

### MCQ 5: What technique is used to detect cycles in network directory structures?

A) Reference counting  
B) Garbage collection  
C) Visited node tracking  
D) All of the above  

**Answer: D**  
All these techniques are used together to safely handle cycles: reference counting manages shared resources, garbage collection cleans up unused entries, and visited node tracking detects cycles during traversal.

---

## 8. Key Takeaways

1. **Directory Structure Evolution**: Directory structures evolved from simple single-level designs to complex hierarchical and network structures to meet the growing needs of file organization and sharing.

2. **Types of Structures**:
   - **Single-Level**: Simple but limited; all files in one directory
   - **Two-Level**: Adds user isolation with separate user directories
   - **Hierarchical (Tree)**: Modern standard; unlimited nesting depth
   - **Acyclic-Graph**: Enables file sharing without cycles
   - **Network (General Graph)**: Maximum flexibility with cycle handling complexity

3. **Path Conventions**: Understanding absolute paths (from root) and relative paths (from current directory) is essential for file system navigation.

4. **Directory Operations**: Common operations include create, delete, list, change, rename, and search directories.

5. **Implementation Considerations**: Directories can be implemented using linear lists (simple, O(n) search) or hash tables (efficient, O(1) average search). Modern systems use i-node based structures.

6. **Real-World Applications**: All major operating systems (Windows, macOS, Linux) use hierarchical directory structures as their primary organization method.

7. **For Delhi University Students**: This topic connects with practical system programming, file system design, and understanding how operating systems manage storage—a fundamental skill for computer science professionals.

---

## References for Further Study

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
- Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson.
- Delhi University BSc (Hons) Computer Science NEP 2024 UGCF Syllabus - Operating Systems Paper

---

*This study material covers the complete directory structure topic as per the Delhi University BSc (Hons) Computer Science curriculum requirements.*