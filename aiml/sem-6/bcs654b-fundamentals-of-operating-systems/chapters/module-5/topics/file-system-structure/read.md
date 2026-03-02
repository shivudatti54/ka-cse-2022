# File System Concepts

## What is a File?
A named collection of related information stored on secondary storage. Files are the logical unit of storage.

## File Attributes
| Attribute | Description |
|-----------|-------------|
| Name | Human-readable identifier |
| Identifier | Unique system ID (inode number) |
| Type | Format (text, binary, executable) |
| Location | Pointer to data on disk |
| Size | Current size in bytes/blocks |
| Protection | Access permissions (rwx) |
| Timestamps | Created, modified, accessed |

## File Operations
1. **Create**: Allocate space, add directory entry
2. **Open**: Find file, load metadata into memory
3. **Read**: Copy data from disk to memory
4. **Write**: Copy data from memory to disk
5. **Seek**: Reposition read/write pointer
6. **Close**: Free memory structures
7. **Delete**: Remove directory entry, free space

## File Access Methods

### Sequential Access
```
read_next()   // Read next record
write_next()  // Write to end
reset()       // Go to beginning
```
Used by: Text files, logs, tapes

### Direct (Random) Access
```
read(n)       // Read record n
write(n)      // Write record n
position(n)   // Move to record n
```
Used by: Databases, file systems

### Indexed Access
- Build index of key → record location
- Search index, then direct access
- Used by: Database systems

## File Types

### By Content
- Text files (ASCII, Unicode)
- Binary files (executables, images)
- Directories

### By Extension
| Extension | Type |
|-----------|------|
| .txt, .doc | Documents |
| .c, .py, .java | Source code |
| .exe, .out | Executables |
| .jpg, .png | Images |

## File Structure
- **None**: Sequence of bytes (Unix)
- **Simple record**: Lines, fixed/variable length
- **Complex**: Database, indexed

## Open File Table
When file is opened:
- **Per-process table**: File descriptor, access mode, position
- **System-wide table**: Open count, disk location, timestamps
