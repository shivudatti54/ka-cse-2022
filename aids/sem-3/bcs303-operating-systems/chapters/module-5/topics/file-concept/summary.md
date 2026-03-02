# File Concept - Summary

## Key Definitions and Concepts

- **File**: A named collection of related information stored on secondary storage, providing a logical abstraction over physical storage devices.

- **File Attributes**: Metadata maintained by the OS including name, type, size, location, protection (permissions), creation time, modification time, and access time.

- **File Descriptor**: A small non-negative integer returned by the open() system call that identifies an open file within a process.

- **File Pointer**: A position indicator tracking the current location in a file from where data will be read or written.

## Important Formulas and Theorems

- **Direct Access Position Calculation**: byte_offset = record_number × record_size

- **File Access Methods**:
  - Sequential: O(n) for accessing nth record
  - Direct: O(1) for accessing any record
  - Indexed: O(log n) with binary search, O(1) with hash index

## Key Points

- Files provide abstraction that hides physical storage device details from users and applications.

- The six primitive file operations are: create, open, read, write, seek, and close.

- File types include regular files, directory files, device files, and special files (pipes, sockets).

- Sequential access reads/writes data in order, while direct (random) access allows positioning anywhere in the file.

- Unix follows the "everything is a file" philosophy for uniform I/O interface.

- Files can be structured as byte sequences (most common in Unix) or as collections of fixed/variable-length records.

- The operating system maintains a File Control Block (FCB) for each open file to track its state and metadata.

## Common Mistakes to Avoid

- Confusing file descriptors with file pointers—descriptors are low-level OS integers while pointers are buffered I/O stream structures from standard libraries.

- Forgetting that record numbers in direct access typically start from 0, not 1.

- Assuming file extensions determine file type in all systems—Unix relies more on file permissions and magic numbers.

- Overlooking the difference between opening a file in text mode versus binary mode, which affects how newlines and EOF are handled.

## Revision Tips

- Create a table comparing all file attributes with their purposes for quick memorization.

- Practice writing simple C programs to perform file operations to reinforce theoretical concepts.

- Memorize the formula for calculating byte offsets in direct access files.

- Review system calls for Unix (open, read, write, close, lseek) and Windows (CreateFile, ReadFile, WriteFile, CloseHandle) to understand implementation differences.