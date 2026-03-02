# File System Interface - Summary

## Key Definitions

- **File**: A named collection of related information stored on secondary storage, treated by the OS as a linear array of bytes
- **File System Interface**: The layer of the operating system that provides abstraction over physical storage, defining how files are named, accessed, and managed
- **File Descriptor**: A small non-negative integer that identifies an open file within a process
- **File Pointer**: A position indicator that tracks the current location within a file for read/write operations
- **Directory**: A special file that contains entries mapping file names to their internal identifiers
- **Access Method**: The technique used to read from or write to a file (sequential, direct, or indexed)

## Important Formulas

- **Direct Access Position**: `byte_offset = block_number × block_size`
- **File Size Extension**: When writing beyond EOF, file size automatically increases to accommodate new data
- **Maximum File Size**: Limited by both file system constraints (maximum file size) and available storage capacity

## Key Points

1. The file system interface abstracts physical storage details, presenting files as simple named collections of bytes

2. File attributes include name, identifier, type, location, size, protection information, timestamps, and owner details

3. Sequential access processes files from beginning to end, ideal for streaming data and batch processing

4. Direct (random) access enables positioning to any file location instantly using seek operations

5. Opening a file returns a file descriptor used for all subsequent operations; closing releases associated resources

6. The read operation transfers data from file to process memory; write transfers data from process memory to file

7. Directories provide hierarchical organization, typically implementing a tree structure with parent-child relationships

8. Protection mechanisms include Access Control Lists (ACLs) for fine-grained control and permission bits for simpler owner/group/others models

9. File operations are atomic in terms of the file system's consistency guarantees, with the OS maintaining integrity even during system failures through journaling or other techniques

## Common Mistakes

1. **Forgetting to close files**: Not closing files leads to resource leaks and potential data loss if buffered data isn't flushed to disk

2. **Confusing file descriptors with file pointers**: File descriptors are system-level integers, while file pointers are library-level position indicators (stdin/stdout use different abstractions)

3. **Ignoring return values**: File operations can fail; ignoring return values masks errors and can lead to undefined behavior

4. **Assuming file positions are shared**: Each process has its own file position; opening the same file twice creates independent file pointers

5. **Not checking file size before allocation**: Attempting to read or write beyond reasonable bounds without checking file size leads to errors

6. **Mixing buffered and unbuffered I/O**: Using both `printf`/`scanf` and `read`/`write` on the same file without proper synchronization causes data corruption