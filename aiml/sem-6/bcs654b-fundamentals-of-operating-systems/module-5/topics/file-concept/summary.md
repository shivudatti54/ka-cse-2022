# File Concept

## Overview

A file is a named collection of related information stored on secondary storage, providing abstraction over physical storage details. Files have attributes (name, type, size, permissions, timestamps), types (regular, directory, special, symbolic link), and operations (create, delete, open, close, read, write).

## Key Points

- **File Definition**: Named collection of related information recorded on secondary storage
- **File Attributes**: Name (human-readable identifier), type (text, binary, executable), size (bytes), location (device and path), permissions (who can access), timestamps (creation, modification, access)
- **File Types**: Regular files (data), directories (file names and pointers), special files (devices), symbolic links (path to another file)
- **File Operations**: Create (allocate space, directory entry), delete (free space, remove entry), open (prepare for I/O, return descriptor), close (release resources), read (transfer from file), write (transfer to file), reposition/seek (move file pointer), truncate (reset size to zero)
- **File Descriptor**: Integer identifying open file in process, used in all file operations
- **File Pointer**: Current position in file, maintained by OS for each open instance
- **Access Modes**: Read-only, write-only, read-write, append

## Important Concepts

- File provides logical unit of information storage, independent of physical structure
- File descriptor abstracts open file, enables multiple processes accessing same file
- File operations require file to be open (except create and delete)
- File pointer separate for each open instance, multiple opens of same file have independent pointers

## Notes

- Memorize file attributes and their purposes
- Understand file operation sequences: create → open → read/write → close
- Know difference between file descriptor and file pointer
- Practice permission representations: rwx (symbolic), 755 (octal)
