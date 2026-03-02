# File Concept

## Introduction

The file concept is one of the most fundamental abstractions in modern computing systems. In an operating system, a file represents a logical unit of storage that allows users and applications to store, organize, and retrieve data persistently. Without files, users would need to interact directly with raw disk sectors, making computer usage extraordinarily complex and inefficient. The file concept provides an abstraction layer that hides the physical details of storage devices from users and applications, enabling convenient data management.

Files have evolved significantly since the early days of computing, when data was stored on punch cards and magnetic tapes. Today, files underpin virtually every aspect of computing—from documents and images to databases and executable programs. Understanding the file concept is essential for any computer science student, as it forms the foundation for studying file systems, directory structures, and storage management. In the University of Delhi curriculum, this topic appears in Operating Systems courses and is crucial for both theoretical understanding and practical system programming.

The importance of files extends beyond mere storage. Files provide mechanisms for data protection through permissions, enable sharing among multiple users and processes, and support various access methods optimized for different use cases. As you study this topic, you will understand how operating systems transform the physical reality of disk storage into the logical, user-friendly file abstraction.

## Key Concepts

### Definition and Characteristics of a File

A file is a named collection of related information that is stored on secondary storage devices such as hard disks, solid-state drives, and magnetic tapes. From the user's perspective, a file is the basic unit of data storage; from the operating system's perspective, it is a collection of bytes or records that can be read, written, and manipulated.

The operating system maintains several attributes for each file. These attributes, also known as metadata, include the file name, which is a unique identifier within a directory; the file type, which indicates the format and purpose of the file (such as text, executable, or image); the file size, measured in bytes; the creation, modification, and access timestamps showing when the file was created, last modified, and last accessed; the file permissions that control who can read, write, or execute the file; and the file location, which is a pointer to the physical storage location on the disk.

### File Operations

The operating system provides a set of primitive operations that can be performed on files. These operations form the foundation for all file manipulation tasks. The primary file operations include creating a new file, which allocates space and establishes its attributes; opening an existing file, which prepares it for access and returns a file descriptor; reading data from a file, which transfers bytes from the file to memory; writing data to a file, which transfers bytes from memory to the file; seeking, which moves the file pointer to a specific position within the file; closing a file, which releases resources and updates metadata; and deleting a file, which removes the file entry and deallocates its storage space.

These operations are supported by system calls such as open(), close(), read(), write(), and lseek() in Unix-like systems, and CreateFile(), ReadFile(), WriteFile(), and CloseHandle() in Windows. Understanding these system calls is crucial for system programming and for comprehending how applications interact with the file system.

### File Types

Files can be classified into several categories based on their content and usage. Regular files contain user data and can be further divided into text files, which store characters in a readable format, and binary files, which store data in machine-readable format. Directory files are special files that organize the file system hierarchy by containing references to other files and directories. Device files represent hardware devices and provide an interface for communication with peripherals. Special files include named pipes for inter-process communication and socket files for network communication.

The file type is often indicated by extensions in the file name (such as .txt, .c, .jpg, .pdf) in systems like Windows, while Unix-like systems rely more heavily on metadata and magic numbers within the file content to determine file type.

### File Structure

Files can be organized using different internal structures depending on the type of data they store and the operations they support. The simplest approach is an unstructured sequence of bytes, where the operating system treats the file as a linear array of bytes without any internal interpretation. This approach, used by Unix-like systems, provides maximum flexibility as the file format is determined by the application rather than the operating system.

Alternatively, files can be structured as a sequence of fixed-length or variable-length records, where each record contains related fields of information. This record-based organization is common in database systems and legacy applications. Another structure involves a tree of records, where records are organized in a hierarchical manner, facilitating efficient searching and indexing. Understanding file structure is essential for selecting appropriate access methods and for designing efficient file-based applications.

### File Access Methods

The operating system supports different methods for accessing data within a file. Sequential access is the simplest method, where data is read or written in order from the beginning to the end of the file. This method is efficient for tape storage and for processing files where all records must be examined. Direct access, also known as random access, allows reading or writing at any position within the file without having to traverse preceding data. This method uses a file pointer that can be moved to any location using the seek operation. Indexed access employs an index structure that provides quick lookup of data based on key values, making it efficient for large databases and files requiring frequent searches.

## Examples

### Example 1: File Creation and Writing in C

Consider a C program that creates a text file and writes student data to it. This example demonstrates the fundamental file operations discussed earlier.

```c
#include <stdio.h>
#include <stdlib.h>

struct Student {
    int rollno;
    char name[50];
    float marks;
};

int main() {
    FILE *fp;
    struct Student s;
    
    // Create and open file in write mode
    fp = fopen("student.txt", "w");
    if (fp == NULL) {
        printf("Error creating file!\n");
        exit(1);
    }
    
    // Write student records
    s.rollno = 1;
    strcpy(s.name, "Amit Kumar");
    s.marks = 85.5;
    fprintf(fp, "%d %s %.2f\n", s.rollno, s.name, s.marks);
    
    s.rollno = 2;
    strcpy(s.name, "Priya Singh");
    s.marks = 92.0;
    fprintf(fp, "%d %s %.2f\n", s.rollno, s.name, s.marks);
    
    fclose(fp);
    printf("File created successfully!\n");
    return 0;
}
```

In this example, fopen() creates a new file and returns a FILE pointer. The fprintf() function writes formatted data to the file, and fclose() properly closes the file, flushing any buffered data to disk. This demonstrates how the operating system abstracts file operations through the standard C library.

### Example 2: Random Access File Processing

This example shows how to implement direct access to read a specific record from a file containing employee data with fixed-length records.

```c
#include <stdio.h>
#include <stdlib.h>

struct Employee {
    int id;
    char name[30];
    float salary;
};

#define RECORD_SIZE sizeof(struct Employee)

void readRecord(FILE *fp, int recordNumber) {
    struct Employee emp;
    
    // Seek to the position of the desired record
    fseek(fp, recordNumber * RECORD_SIZE, SEEK_SET);
    
    // Read the record
    fread(&emp, sizeof(struct Employee), 1, fp);
    
    printf("ID: %d, Name: %s, Salary: %.2f\n", 
           emp.id, emp.name, emp.salary);
}

int main() {
    FILE *fp;
    
    // Create a file with employee records
    fp = fopen("employees.dat", "wb");
    struct Employee e1 = {101, "Raj Gupta", 50000.0};
    struct Employee e2 = {102, "Neha Sharma", 55000.0};
    struct Employee e3 = {103, "Vikram Singh", 60000.0};
    
    fwrite(&e1, sizeof(struct Employee), 1, fp);
    fwrite(&e2, sizeof(struct Employee), 1, fp);
    fwrite(&e3, sizeof(struct Employee), 1, fp);
    fclose(fp);
    
    // Read the second record using direct access
    fp = fopen("employees.dat", "rb");
    printf("Reading 2nd record:\n");
    readRecord(fp, 1);  // Record numbers start from 0
    fclose(fp);
    
    return 0;
}
```

This example illustrates direct access where fseek() positions the file pointer at the exact byte offset corresponding to the desired record, and fread() retrieves the record. The formula for calculating the position of the nth record is: position = n × sizeof(record). This method is highly efficient for large files where only specific records need to be accessed.

### Example 3: File Metadata Manipulation

Understanding file attributes is crucial for system administration and security. In Unix-like systems, the stat system call retrieves complete metadata about a file.

```c
#include <sys/stat.h>
#include <stdio.h>
#include <time.h>

int main(const char *filename) {
    struct stat fileStat;
    
    if (stat("example.txt", &fileStat) < 0) {
        printf("Error getting file information\n");
        return 1;
    }
    
    printf("File Size: %ld bytes\n", fileStat.st_size);
    printf("Number of Links: %hu\n", fileStat.st_nlink);
    printf("File Permissions: %o\n", fileStat.st_mode & 0777);
    printf("Last Access Time: %s", ctime(&fileStat.st_atime));
    printf("Last Modification: %s", ctime(&fileStat.st_mtime));
    printf("Last Status Change: %s", ctime(&fileStat.st_ctime));
    
    return 0;
}
```

This program uses the stat() function to retrieve comprehensive file metadata including size, permissions, timestamps, and link count. Such operations are essential for backup systems, file managers, and security monitoring tools.

## Exam Tips

For the University of Delhi examinations, focus on the following aspects of the file concept topic.

First, remember that a file is a logical abstraction provided by the operating system to hide the physical details of secondary storage devices. This conceptual understanding is frequently tested in exams.

Second, be thorough with file attributes. The key attributes include name, identifier, type, location, size, protection, and timestamps. You should be able to list and explain each attribute.

Third, master the six basic file operations: create, open, read, write, seek, and close. Understand the purpose of each operation and the system calls used to implement them in Unix and Windows systems.

Fourth, differentiate clearly between sequential access and direct access methods. Remember that sequential access processes records in order, while direct access allows random positioning using the seek operation. The time complexity differences between these methods are important.

Fifth, understand file types thoroughly—regular files, directories, device files, and special files. Know how each type is distinguished and its purpose in the system.

Sixth, for record-structured files, understand the calculation of record positions in direct access: byte offset = record_number × record_size. This formula is commonly tested in numerical problems.

Seventh, remember that Unix follows the "everything is a file" philosophy, where devices, pipes, and sockets are treated as files, providing a uniform interface for I/O operations.

Eighth, be familiar with the concept of file descriptor (integer identifier returned by open()) and FILE pointer (buffered I/O stream pointer used by standard library functions). Know the difference between low-level system calls and high-level standard I/O functions.