# Directory Structure


## Table of Contents

- [Directory Structure](#directory-structure)
- [What is a Directory?](#what-is-a-directory)
- [Directory Operations](#directory-operations)
- [Directory Structures](#directory-structures)
  - [1. Single-Level Directory](#1-single-level-directory)
  - [2. Two-Level Directory](#2-two-level-directory)
  - [3. Tree-Structured Directory](#3-tree-structured-directory)
  - [4. Acyclic Graph Directory](#4-acyclic-graph-directory)
  - [5. General Graph Directory](#5-general-graph-directory)
- [Path Names](#path-names)
  - [Absolute Path](#absolute-path)
  - [Relative Path](#relative-path)
- [Directory Implementation](#directory-implementation)
  - [Linear List](#linear-list)
  - [Hash Table](#hash-table)
- [Hard Link vs Soft Link](#hard-link-vs-soft-link)

## What is a Directory?

A special file containing information about other files. Maps file names to file metadata.

## Directory Operations

1. Search for file
2. Create file
3. Delete file
4. List directory contents
5. Rename file
6. Traverse file system

## Directory Structures

### 1. Single-Level Directory

```
Root: [file1, file2, file3, ...]
```

- Simple implementation
- Naming problems (all names must be unique)
- No grouping

### 2. Two-Level Directory

```
Root/
├── User1/[files]
├── User2/[files]
└── User3/[files]
```

- User isolation
- Same names in different user directories OK
- No user grouping of files

### 3. Tree-Structured Directory

```
Root/
├── bin/
├── home/
│ ├── user1/
│ │ ├── docs/
│ │ └── code/
│ └── user2/
└── etc/
```

- Hierarchical organization
- Efficient searching
- Absolute and relative paths

### 4. Acyclic Graph Directory

```
Root/
├── dir1/
│ └── shared → ../shared_file
├── dir2/
│ └── shared → ../shared_file
└── shared_file
```

- Allows file sharing via links
- **Hard links**: Multiple directory entries point to same inode
- **Soft links (symbolic)**: File containing path to another file
- Deletion problem: When to delete actual file?

### 5. General Graph Directory

- Allows cycles (links can create loops)
- Risk of infinite loops during traversal
- Most systems prevent cycles

## Path Names

### Absolute Path

From root: `/home/user/documents/file.txt`

### Relative Path

From current directory: `./documents/file.txt` or `../other/file.txt`

## Directory Implementation

### Linear List

- Simple list of (name, pointer) pairs
- Easy to implement
- Slow search: O(n)

### Hash Table

- Hash function on file name
- Fast lookup: O(1) average
- Collision handling needed

## Hard Link vs Soft Link

| Feature                  | Hard Link      | Soft Link    |
| ------------------------ | -------------- | ------------ |
| Points to                | Inode directly | Path name    |
| Cross filesystem         | No             | Yes          |
| Broken if target deleted | No             | Yes          |
| Inode count              | Incremented    | Not affected |
