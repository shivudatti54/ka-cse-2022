# File System Operations

## Overview

File system operations provide interface for manipulating files and directories. Basic operations include create, delete, open, close, read, write, and seek on files, plus create, delete, and list operations on directories, all implemented through system calls.

## Key Points

- **Create**: Allocate space, make entry in directory, file initially empty
- **Delete**: Free space, remove directory entry, cannot delete if file open
- **Open**: Search directory for entry, load file control block (FCB) to memory, return file descriptor
- **Close**: Write back modified data, release file descriptor, deallocate memory structures
- **Read**: Transfer data from file to user buffer, update file pointer
- **Write**: Transfer data from user buffer to file, update file pointer, may extend file
- **Seek (lseek)**: Reposition file pointer to specified location for random access
- **Append**: Write at end of file, special case of write operation
- **Directory Operations**: create, delete, list (readdir), rename

## Important Concepts

- File descriptor (Unix) or handle (Windows) references open file in process
- Open file table tracks all open files system-wide
- Per-process file table tracks files opened by each process
- File pointer (current position) maintained separately for each open instance

## Notes

- Practice system call sequences: open() → read()/write() → close()
- Understand file descriptor vs file pointer distinction
- Know operations require open file: read, write, seek
- Remember close() essential to flush buffers and release resources
