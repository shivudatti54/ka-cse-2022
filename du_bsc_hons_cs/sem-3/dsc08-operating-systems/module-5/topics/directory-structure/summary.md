# Directory Structure - Operating Systems

## Introduction

A directory is a logical container that organizes files and other directories in a hierarchical manner, enabling efficient file management and retrieval. The directory structure defines how files are named, stored, and accessed within a computer system. Understanding different directory structures is essential for effective file system design and management.

## Key Concepts

### Purpose of Directory Structure
- **Organization**: Groups related files together for easy navigation
- **Efficiency**: Enables fast file search and access
- **Naming**: Allows multiple files with same name in different directories
- **Protection**: Implements access control mechanisms

### Types of Directory Structures

**1. Single-Level Directory**
- All files in one central directory
- Simple but severely limited
- Naming conflicts possible
- Not suitable for multi-user systems

**2. Two-Level Directory**
- Separate directory for each user (MFD - Master File Directory)
- User files stored in User File Directory (UFD)
- Eliminates naming conflicts between users
- Limited directory hierarchy

**3. Hierarchical (Tree) Directory**
- Root directory with nested subdirectories
- Most widely used structure
- Supports unlimited directory depth
- Enables logical file grouping
- Efficient search and organization

**4. Acyclic Graph Directory**
- Allows directories to be shared via links
- Files can appear in multiple locations
- More flexible than tree structure
- Requires garbage collection for deleted links

**5. General Graph Directory**
- Allows cycles (directories referencing each other)
- Complex traversal algorithms needed
- Risk of infinite loops during navigation
- Rarely implemented in modern systems

### Directory Operations
- Create, delete, and rename directories
- Open, close, read, and write files
- Traverse directory hierarchy
- Set and modify file attributes
- Search for files by name or attributes

### Path Names
- **Absolute Path**: Complete path from root directory (e.g., /home/user/documents/file.txt)
- **Relative Path**: Path relative to current working directory
- **Current Directory (.)**: Represents present working directory
- **Parent Directory (..)**: Represents directory one level up

## Conclusion

The choice of directory structure impacts system performance, user convenience, and file management capabilities. Modern operating systems primarily use hierarchical (tree) structures due to their flexibility and efficiency. Understanding these structures is crucial for file system implementation and management in operating systems.

*Reference: Delhi University BSc (Hons) CS NEP 2024 UGCF Syllabus - Operating Systems Unit*