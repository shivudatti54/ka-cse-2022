# Background (File Systems and Virtual Memory)

## Overview

This module covers file systems (organizing and storing data on storage devices) and virtual memory (allowing execution of processes larger than physical memory). File systems provide logical view of storage through files and directories, while virtual memory uses demand paging and page replacement.

## Key Points

- **File System**: Provides uniform logical view of information storage, abstracts physical storage details
- **File Concept**: Named collection of related information stored on secondary storage
- **Directory Structure**: Organizes files into hierarchical structure for easy navigation
- **Virtual Memory**: Separates logical memory from physical memory, allows very large logical address space
- **Demand Paging**: Loads pages into memory only when needed, reducing memory requirements
- **Page Replacement**: When memory full, selects victim page to swap out based on replacement algorithm

## Important Concepts

- File systems map logical file operations to physical disk operations
- Access methods: sequential (tape), direct (disk), indexed (database)
- Virtual memory enables multiprogramming with large processes
- Page fault occurs when referenced page not in memory, requires page fetch from disk

## Notes

- Understand file system abstracts hardware complexity
- Know virtual memory separates user logical memory from physical RAM
- Remember demand paging principle: load only when needed
- Practice page fault handling sequence
