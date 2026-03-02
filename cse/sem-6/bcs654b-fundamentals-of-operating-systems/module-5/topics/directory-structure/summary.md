# Directory Structure

## Overview

Directory structure organizes files into hierarchical namespaces enabling efficient search, grouping, and sharing. Structures evolved from single-level (all files in one directory) to tree-structured (hierarchical organization) to acyclic-graph (allowing sharing via links).

## Key Points

- **Single-Level Directory**: All files in one directory, naming conflicts, inefficient search
- **Two-Level Directory**: Separate directory per user, eliminates naming conflicts, limits grouping
- **Tree-Structured Directory**: Hierarchical organization, subdirectories for grouping, efficient search via path names
- **Acyclic-Graph Directory**: Allows file sharing via links (hard links, symbolic links), no cycles
- **General Graph Directory**: Allows cycles, requires garbage collection, complex to implement
- **Absolute Path**: Full path from root (/usr/local/bin/file)
- **Relative Path**: Path from current directory (../bin/file)
- **Current Working Directory**: Directory where process currently operates, changes via cd command

## Important Concepts

- Tree structure most common: combines organization, naming, and reasonable sharing
- Hard link: directory entry pointing to same inode as another entry
- Symbolic link: special file containing path to another file
- Path resolution: traversing directories from root or current directory

## Notes

- Practice path resolution examples with absolute and relative paths
- Understand hard link vs symbolic link differences
- Know directory operations: create, delete, rename, list
- Remember each directory contains . (self) and .. (parent) entries
