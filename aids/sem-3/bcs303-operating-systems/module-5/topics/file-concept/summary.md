# File Concept - Summary

## Key Definitions

- **File**: A named collection of related information stored on secondary storage, providing an abstraction over physical storage devices.

- **File Attributes**: Metadata properties describing a file's characteristics, including name, identifier, type, location, size, protection, and timestamps.

- **File Descriptor**: A small non-negative integer returned by the operating system when a file is opened, used to reference the open file in subsequent operations.

- **File Structure**: The internal organization of data within a file, determining how information is arranged and accessed.

- **Regular Files**: Standard files containing user data in any format, as distinguished from system files like directories.

## Important Formulas

- **File Position Calculation for Random Access**: `offset = record_number × record_size`

When accessing records by number in files with fixed-length records, the byte offset equals the record number multiplied by the size of each record.

- **File Descriptor Table Index**: File descriptors serve as indices into the per-process file descriptor table, mapping logical file references to system-level file table entries.

## Key Points

1. Files provide logical data storage abstraction, hiding physical storage complexities from users and applications.

2. Every file possesses attributes that the operating system maintains to manage the file effectively throughout its lifecycle.

3. The six fundamental file attributes are: name, identifier, type, location, size, and protection.

4. Timestamp attributes record creation time, last modification time, and last access time for each file.

5. File operations (create, open, read, write, seek, close, delete) form the primitive interface between applications and stored data.

6. The open operation returns a file descriptor used for subsequent file references within a process.

7. File structures include byte sequence (most flexible), record sequence (organized), and tree structure (indexed) models.

8. Regular files contain user data; directories organize file hierarchies; special files represent devices.

9. File names follow operating system-specific conventions regarding length, case sensitivity, and allowed characters.

10. The file abstraction enables data persistence across program executions and supports multi-user data sharing.

## Common Mistakes

1. **Confusing file descriptors with file names**: File descriptors are temporary handles returned by open(), while file names are persistent string identifiers stored in directories.

2. **Assuming immediate physical writes**: Write operations may be buffered by the operating system; data may not reach physical storage until buffer flushing occurs (explicitly or during close).

3. **Ignoring file type implications**: Attempting to treat all files identically ignores that directories and special files require different operations than regular files.

4. **Forgetting to close files**: Failing to close files can cause resource leaks and data loss from unflushed buffers in long-running programs.

5. **Misunderstanding file position**: The file position indicator advances automatically after read/write operations but can be repositioned using seek; exceeding file size during seek creates a "hole" in sparse files.
