**File Systems – Directory Structures**  
*(Ge5A Operating Systems, BSc Physical Science (CS), Delhi University – NEP 2024)*  

---

### Introduction  
A directory (or folder) provides a logical organization of files, allowing users and programs to locate, protect, and manage data without knowing physical disk addresses. The **directory structure** defines how files are named, stored, and accessed within a file system, forming a core component of any operating system as prescribed in the Delhi University Ge5A syllabus.

---

### Key Concepts (Bullet Form)
- **Directory Entry**: Stores metadata – file name, inode/FCB pointer, attributes (size, dates, permissions).  
- **Logical vs. Physical Organization**: Directories manage logical file names; the file system maps them to physical disk blocks.  
- **Pathname**:  
  - *Absolute*: starts from root (e.g., `/home/user/data.txt`).  
  - *Relative*: starts from current working directory (e.g., `../docs/notes.txt`).  

---

### Types of Directory Structures  

| Structure | Description | Example |
|-----------|-------------|---------|
| **Single‑Level** | One flat list of files; simplest, but name collisions likely. | Early DOS, CP/M |
| **Two‑Level** | Separate directory per user; reduces collisions but still limited. | MS‑DOS `U:` drives |
| **Hierarchical (Tree)** | Nested directories; supports unlimited depth, easy navigation. | UNIX/Linux (`/`, `/usr`, `/home`), Windows NTFS |
| **Acyclic‑Graph (Network)** | Allows directories to share sub‑directories (aliases/shortcuts); introduces reference counting. | UNIX symbolic links, Windows shortcuts |
| **Hash‑Based** | Uses a hash table to map file names to directory entries; fast lookup, collision handling needed. | Modern file systems (NTFS, ext4) employ hash tables internally |

---

### Directory Operations  
- **Create / Delete**: Add or remove a directory entry.  
- **Rename / Move**: Change name or relocate within the hierarchy.  
- **List / Traverse**: Display contents (`ls`, `dir`) or walk the tree.  
- **Search / Lookup**: Locate a file by name or by attribute (e.g., using `find`).  
- **Protect**: Set permissions (read/write/execute) on directories to control access.

---

### Implementation Techniques  
- **Linear List**: Simple array of entries; O(n) search.  
- **Hash Table**: Maps names to offsets; O(1) average lookup, must handle collisions.  
- **B+‑Tree / Balanced Tree**: Keeps entries sorted, supports range queries; used in advanced file systems (e.g., ext4, NTFS).  

---

### Advantages & Trade‑offs  
- **Hierarchical**: Scalable, intuitive; deeper trees increase path‑lookup cost.  
- **Hash‑Based**: Fast access; extra memory for hash tables.  
- **Acyclic‑Graph**: Flexibility (shared folders); complexity in deletion and cycle detection.  

---

### Conclusion  
The directory structure is the backbone of file‑system usability, balancing simplicity, performance, and security. Understanding the various models—single‑level through hash‑based—and their implementation methods is essential for the Ge5A Operating Systems exam, as it covers the logical organization of files, path resolution, and protection mechanisms prescribed by Delhi University’s NEP 2024 syllabus.