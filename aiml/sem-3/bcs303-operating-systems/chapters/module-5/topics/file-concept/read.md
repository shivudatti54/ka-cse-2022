# File Concept

## Introduction

A file is the fundamental unit of data storage in any computer system, representing a named collection of related information that resides on secondary storage devices. In the context of Operating Systems, the file concept forms the cornerstone of secondary storage management, enabling users and applications to store, retrieve, and manipulate data persistently. Unlike primary memory (RAM) which is volatile and temporary, files provide non-volatile storage that survives system restarts and power failures.

The importance of the file concept in computer science cannot be overstated. Every piece of data you create, from a simple text document to complex database records, is ultimately stored as files on disk. Operating systems abstract the complex details of physical storage into a convenient file-based interface, allowing users and programmers to work with data without worrying about the underlying hardware specifics. This abstraction layer, managed through the file system, transforms raw sectors on a hard disk into meaningful, organized collections of information that users can easily understand and manipulate.

In the University of Delhi's Computer Science curriculum, understanding the file concept is essential for comprehending how operating systems manage secondary storage, implement data persistence, and provide security and protection mechanisms. This knowledge forms the foundation for advanced topics in file system implementation, database management, and distributed systems.

## Key Concepts

### Definition and Nature of a File

A file can be defined as a named collection of related information that is stored on secondary storage media and treated as a single unit by the operating system. From the user's perspective, a file appears as a linear sequence of bytes, with the operating system determining the logical structure and meaning of these bytes. This logical view allows different applications to interpret file contents differently—a text editor sees ASCII characters, an image viewer sees pixel data, and a compiler sees source code instructions.

Files possess several intrinsic properties that distinguish them from other data structures. They have a finite length that can be measured in bytes, and this length can change during the file's lifetime as data is added or removed. Files are created by users or processes and persist until explicitly deleted, surviving process termination and system reboots. Each file within a system must have a unique name within its directory, though different directories may contain files with identical names.

### File Attributes

Every file in a system is characterized by a set of attributes that define its properties and state. These attributes, also known as metadata, are maintained by the operating system and include:

The NAME is the symbolic file name that users employ to identify the file, typically consisting of a base name and an optional extension that indicates the file type. The IDENTIFIER represents the unique internal tag, usually a numeric inode number in Unix-like systems, that the system uses internally to reference the file.

The FILE TYPE conveys information about the format and nature of the file contents. Common file types include regular files (containing user data), directory files (containing file listings), device files (representing hardware devices), and special files (pipes, sockets).

The LOCATION attribute specifies the pointer to the file's position on the secondary storage device, typically expressed as a device identifier and physical address. The SIZE attribute indicates the current length of the file in bytes.

The PROTECTION information defines access permissions, specifying which users or user groups can perform which operations (read, write, execute) on the file. The TIME, DATE, AND USER IDENTIFIER attributes record when the file was created, last modified, and last accessed, along with information about the file's owner.

### File Operations

The operating system provides a set of primitive operations that form the foundation for all file manipulation activities. Understanding these operations is crucial for both using files effectively and implementing higher-level file handling mechanisms.

The CREATE operation establishes a new file and initializes its attributes, allocating necessary space on the storage medium. The DELETE operation removes a file from the file system, releasing its allocated space for future use.

The OPEN operation prepares a file for access by establishing a connection between the user process and the file, returning a file descriptor or handle that subsequent operations will use. The CLOSE operation terminates this connection, ensuring all pending data is written to disk and releasing system resources.

The READ operation retrieves data from a file, transferring a specified number of bytes from the file's current position to a user-provided buffer. The WRITE operation stores data in a file, either appending to the end or overwriting existing content at the current position.

The SEEK operation modifies the current file position, enabling random access to any location within the file. The RENAME operation changes a file's name without affecting its contents or location.

### File Access Methods

Operating systems support different methods for accessing file contents, each suited to particular usage patterns and storage requirements.

Sequential access is the simplest method, where files are read or written in consecutive order, starting from the beginning and proceeding byte-by-byte or record-by-record. This method is efficient for tape-based storage and batch processing applications where data is processed in a predetermined order. The READ and WRITE operations automatically advance the file position, with SEEK allowing repositioning to the beginning.

Direct access, also known as relative or random access, enables reading or writing at any arbitrary position within the file without sequential progression. This method treats the file as a numbered sequence of fixed-size blocks or records, allowing immediate access to any block by specifying its block number. This approach is essential for database systems and applications requiring frequent random access to large datasets.

Indexed access builds upon direct access by maintaining an index structure that maps keys or offsets to physical file locations. The system first consults the index to locate the desired data, then uses direct access to retrieve it. This method provides efficient access to specific records but requires additional storage for the index and introduces overhead for index maintenance.

### File Types and Extensions

While modern operating systems treat all files uniformly at the system level, users and applications recognize different file types based on content structure and intended use. File extensions, the characters following the final period in a file name, conventionally indicate file types.

Text files contain ASCII or Unicode characters organized into lines, interpretable by text editors and word processors. Binary files store data in its raw binary form, meaningful only to programs that understand their specific structure. Source code files contain program statements in languages like C, Java, or Python.

Executable files contain machine code instructions that the operating system can directly execute. Image files store visual data in formats like JPEG, PNG, or GIF. Audio and video files contain multimedia content in formats like MP3, WAV, or MP4.

It is important to note that file extensions are merely conventions and do not enforce file type restrictions at the operating system level. A file named "document.txt" could contain executable code, and the system would not prevent its execution based solely on the extension.

## Examples

### Example 1: File Creation and Writing in C

Consider a simple program that creates a text file and writes data to it, demonstrating fundamental file operations:

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char data[] = "Hello, this is a test file.\nWritten for DU CS students.";
    
    // CREATE and OPEN file for writing
    fp = fopen("example.txt", "w");
    
    if (fp == NULL) {
        printf("Error creating file\n");
        return 1;
    }
    
    // WRITE operation
    fprintf(fp, "%s", data);
    
    // CLOSE operation
    fclose(fp);
    
    printf("File created successfully\n");
    return 0;
}
```

In this example, the fopen function performs both CREATE (if the file does not exist) and OPEN operations. The "w" mode specifies write access. The fprintf function performs the WRITE operation, and fclose performs the CLOSE operation, flushing any buffered data to disk.

### Example 2: Sequential File Reading

The following program demonstrates sequential access, reading the entire file byte-by-byte:

```c
#include <stdio.h>

int main() {
    FILE *fp;
    int ch;
    
    // OPEN file for reading
    fp = fopen("example.txt", "r");
    
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    
    // Sequential READ in a loop
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);  // Display each character
    }
    
    // CLOSE file
    fclose(fp);
    
    return 0;
}
```

This program opens the file in read mode ("r") and uses fgetc to read characters sequentially until reaching the End-of-File (EOF) marker. Each call to fgetc automatically advances the file position.

### Example 3: Random Access with fseek

For direct access, the fseek function reposition the file pointer:

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[20];
    
    fp = fopen("example.txt", "r");
    
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    
    // SEEK to 10th byte from beginning
    fseek(fp, 10, SEEK_SET);
    
    // READ from new position
    fgets(buffer, 20, fp);
    
    printf("Content from position 10: %s\n", buffer);
    
    fclose(fp);
    return 0;
}
```

The fseek function demonstrates random access capability. SEEK_SET indicates positioning from the file's beginning. After repositioning, freads continues from the new location, illustrating direct access.

## Exam Tips

For DU semester examinations, several key points about the file concept require special attention:

Understanding the distinction between logical and physical file organization is essential. The operating system provides logical file abstraction while managing physical storage details.

Memorize the seven essential file operations: create, delete, open, close, read, write, and seek. Questions frequently ask about these primitives and their purposes.

File attributes are commonly examined—be prepared to list at least six attributes: name, identifier, type, location, size, protection, and timestamps.

The three main file access methods—sequential, direct (random), and indexed—must be clearly understood with their respective advantages and disadvantages.

Remember that file extensions are conventions, not enforcement mechanisms. The OS treats files as byte sequences regardless of extension.

The relationship between file descriptors (process-level handles) and inodes (system-level file metadata) is important for Unix-like systems.

File buffering is a subtle but important concept—understand the difference between buffered and unbuffered I/O operations.

Pay attention to the differences between the various file opening modes in C: "r", "w", "a", "r+", "w+", "a+" and their implications for file creation and existing content.