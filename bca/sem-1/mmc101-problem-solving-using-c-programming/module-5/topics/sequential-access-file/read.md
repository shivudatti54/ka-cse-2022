# Sequential Access File


## Table of Contents

- [Sequential Access File](#sequential-access-file)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. File Pointer and File Stream](#1-file-pointer-and-file-stream)
  - [2. File Opening Modes](#2-file-opening-modes)
  - [3. Writing to Sequential Files](#3-writing-to-sequential-files)
  - [4. Reading from Sequential Files](#4-reading-from-sequential-files)
  - [5. End-of-File (EOF) Detection](#5-end-of-file-eof-detection)
  - [6. File Closing](#6-file-closing)
  - [7. Rewind and Sequential Navigation](#7-rewind-and-sequential-navigation)
- [Examples](#examples)
  - [Example 1: Writing and Reading a Text File Character by Character](#example-1-writing-and-reading-a-text-file-character-by-character)
  - [Example 2: Managing Student Records with fprintf() and fscanf()](#example-2-managing-student-records-with-fprintf-and-fscanf)
  - [Example 3: Appending Data to an Existing File](#example-3-appending-data-to-an-existing-file)
- [Exam Tips](#exam-tips)

## Introduction

File handling is a fundamental aspect of programming that enables persistent data storage. In the C programming language, files serve as the primary mechanism for storing and retrieving data beyond the runtime of a program. Sequential access files, also known as stream-oriented files, are a category of files where data is read or written in a sequential manner—starting from the beginning and proceeding linearly until the end of the file. This is in contrast to random access files, where any part of the file can be accessed directly without traversing preceding data.

Sequential access files are extensively used in various real-world applications, including log file management, transaction processing systems, and data backup operations. When you write a program that maintains customer records, processes bank transactions, or generates system logs, you are working with sequential access files. Understanding how to manipulate these files efficiently is crucial for any programmer, as it forms the backbone of data persistence in C.

In the University of Delhi's Computer Science curriculum, this topic carries significant weight in end-semester examinations. Students must be proficient in using file handling functions, understanding file modes, and implementing error-free file operations. This chapter provides an exhaustive exploration of sequential access files, complete with practical examples and examination-oriented insights.

## Key Concepts

### 1. File Pointer and File Stream

In C, a file is represented by a structure called FILE, which is defined in the standard input/output header (stdio.h). When you open a file, the operating system creates a file structure and returns a pointer to this structure, known as a file pointer. This pointer is of type FILE* and serves as your handle to interact with the file.

Every file operation in C requires a file pointer. The standard library provides three pre-defined file pointers: stdin (standard input), stdout (standard output), and stderr (standard error). When you work with disk files, you will create your own file pointers using the fopen() function.

### 2. File Opening Modes

The mode in which you open a file determines what operations are permitted and how the file behaves. For sequential access files, understanding these modes is critical:

| Mode | Description | File Position | File Creation | Behavior if File Exists |
|------|-------------|---------------|---------------|-------------------------|
| "r" | Read | Beginning | No | Opens existing file |
| "w" | Write | Beginning | Yes (if not exists) | Truncates to zero length |
| "a" | Append | End | Yes (if not exists) | Creates if doesn't exist |
| "r+" | Read+Write | Beginning | No | Opens for both operations |
| "w+" | Read+Write | Beginning | Yes | Truncates existing file |
| "a+" | Read+Append | End for writing, Beginning for reading | Yes | Creates if doesn't exist |

The 'b' character can be appended to any mode (e.g., "rb", "wb") to open the file in binary mode, which is essential for non-text data like images or compiled executables.

### 3. Writing to Sequential Files

C provides multiple functions for writing data to sequential access files:

**fputc() Function:** The fputc() function writes a single character to a file. Its prototype is:

```c
int fputc(int character, FILE *fp);
```

It returns the character written on success, or EOF on error. The character is cast to int to accommodate the EOF return value.

**fputs() Function:** To write a string to a file, fputs() is used:

```c
int fputs(const char *str, FILE *fp);
```

It writes the null-terminated string pointed to by str to the file pointed to by fp. It returns a non-negative value on success, or EOF on failure.

**fprintf() Function:** For formatted output to files, fprintf() works identically to printf() but directs output to a file:

```c
int fprintf(FILE *fp, const char *format, ...);
```

This function provides the flexibility of printf() but writes to the file stream instead of the console.

### 4. Reading from Sequential Files

Similar to writing, C provides corresponding functions for reading data:

**fgetc() Function:** Reading a single character from a file:

```c
int fgetc(FILE *fp);
```

It returns the character read as an unsigned char cast to an int, or EOF on reaching end-of-file or error.

**fgets() Function:** For reading strings:

```c
char *fgets(char *str, int n, FILE *fp);
```

This function reads at most (n-1) characters from the file and stores them into the buffer pointed to by str. It stops reading when a newline is encountered, at end-of-file, or when (n-1) characters have been read. The string is null-terminated.

**fscanf() Function:** For formatted input from files:

```c
int fscanf(FILE *fp, const char *format, ...);
```

This function works like scanf() but reads from the file stream instead of standard input.

### 5. End-of-File (EOF) Detection

The EOF macro, typically defined as -1, indicates that the end of a file has been reached or an error has occurred. When using fgetc(), you must check the return value against EOF to determine if the file has ended. However, a common pitfall arises when reading binary files, as a valid byte might have the value 255 (0xFF), which when cast to int becomes -1 (EOF). To handle this correctly, fgetc() returns an int rather than a char.

### 6. File Closing

Always close files after use using fclose():

```c
int fclose(FILE *fp);
```

This function flushes any unwritten data to the file, releases all allocated resources, and returns zero on success, or EOF if an error occurs. Failing to close files can lead to data loss if buffers are not flushed.

### 7. Rewind and Sequential Navigation

While sequential access primarily involves reading/writing in order, the rewind() function resets the file position indicator to the beginning of the file:

```c
void rewind(FILE *fp);
```

This allows you to start reading from the beginning again without closing and reopening the file.

## Examples

### Example 1: Writing and Reading a Text File Character by Character

Problem: Write a C program to accept a string from the user and write it to a file named "data.txt", then read and display the contents of the file.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    char str[100];
    char ch;
    
    // Open file in write mode
    fp = fopen("data.txt", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }
    
    printf("Enter a string: ");
    gets(str);  // Note: gets() is unsafe, for educational purposes
    
    // Write string character by character
    int i = 0;
    while (str[i] != '\0') {
        fputc(str[i], fp);
        i++;
    }
    
    fclose(fp);
    
    // Open file in read mode
    fp = fopen("data.txt", "r");
    if (fp == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }
    
    printf("\nContents of file: ");
    // Read and display characters until EOF
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }
    
    fclose(fp);
    return 0;
}
```

Explanation: The program first opens "data.txt" in write mode, accepts a string from the user, and writes each character using fputc(). It then closes the file and reopens it in read mode to display the contents using fgetc() in a loop that terminates when EOF is encountered.

### Example 2: Managing Student Records with fprintf() and fscanf()

Problem: Write a program to store student records (roll number, name, marks) in a file and then read and display all records.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

struct student {
    int roll;
    char name[50];
    float marks;
};

int main() {
    struct student s;
    FILE *fp;
    int n, i;
    
    // Open file for writing
    fp = fopen("student.txt", "w");
    if (fp == NULL) {
        printf("Cannot open file!\n");
        exit(1);
    }
    
    printf("Enter number of students: ");
    scanf("%d", &n);
    
    for (i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Roll Number: ");
        scanf("%d", &s.roll);
        printf("Name: ");
        scanf("%s", s.name);
        printf("Marks: ");
        scanf("%f", &s.marks);
        
        // Write record to file using fprintf
        fprintf(fp, "%d %s %.2f\n", s.roll, s.name, s.marks);
    }
    
    fclose(fp);
    
    // Open file for reading
    fp = fopen("student.txt", "r");
    if (fp == NULL) {
        printf("Cannot open file!\n");
        exit(1);
    }
    
    printf("\n--- Student Records ---\n");
    printf("%-10s %-20s %-10s\n", "Roll No", "Name", "Marks");
    printf("-----------------------------------\n");
    
    // Read and display records
    while (fscanf(fp, "%d %s %f", &s.roll, s.name, &s.marks) != EOF) {
        printf("%-10d %-20s %-10.2f\n", s.roll, s.name, s.marks);
    }
    
    fclose(fp);
    return 0;
}
```

Explanation: This program demonstrates structured data handling using fprintf() and fscanf(). Each student record is written as a formatted line in the file. The reading loop continues until fscanf() returns EOF, indicating no more data to read. The %.2f format specifier ensures marks are displayed with two decimal places.

### Example 3: Appending Data to an Existing File

Problem: Create a program that adds more student records to an existing file without deleting the previous data.

Solution:

```c
#include <stdio.h>
#include <stdlib.h>

struct student {
    int roll;
    char name[50];
    float marks;
};

int main() {
    struct student s;
    FILE *fp;
    char choice;
    
    // Open file in append mode
    fp = fopen("student.txt", "a");
    if (fp == NULL) {
        printf("Cannot open file!\n");
        exit(1);
    }
    
    do {
        printf("\nEnter student details:\n");
        printf("Roll Number: ");
        scanf("%d", &s.roll);
        printf("Name: ");
        scanf("%s", s.name);
        printf("Marks: ");
        scanf("%f", &s.marks);
        
        fprintf(fp, "%d %s %.2f\n", s.roll, s.name, s.marks);
        
        printf("Add another record? (y/n): ");
        scanf(" %c", &choice);  // Space before %c to consume newline
        
    } while (choice == 'y' || choice == 'Y');
    
    fclose(fp);
    printf("\nRecords appended successfully!\n");
    
    return 0;
}
```

Explanation: The key difference in this program is using "a" (append) mode instead of "w" mode. In append mode, new data is always written at the end of the file, preserving all existing content. This is essential for applications like maintaining transaction logs or adding new entries to a database without losing historical data.

## Exam Tips

1. **Understanding File Modes**: Remember that "w" mode truncates (deletes) existing file content, while "a" mode appends to the end. This distinction is frequently tested in examinations.

2. **EOF Handling**: Always use an int variable (not char) when storing the return value of fgetc() to correctly detect EOF, especially when dealing with binary files.

3. **Return Values**: Remember that fgetc(), fputc(), fprintf(), and fscanf() return specific values that can be used for error checking.

4. **Null Pointer Check**: Always check if fopen() returns NULL before performing file operations to handle file opening failures gracefully.

5. **Buffer Flushing**: Remember that fclose() automatically flushes buffers. In some systems, you may need to use fflush() to ensure data is written immediately.

6. **Difference Between fgets() and gets()**: fgets() includes the newline character if read, while gets() does not. Also, fgets() is safe as it specifies buffer size.

7. **Binary vs Text Mode**: Use "rb", "wb", "ab" for binary files. Text mode translations (like carriage return-line feed) may corrupt binary data.

8. **Command Line Arguments**: In advanced problems, files may be opened using command line arguments passed to main(), which is useful for processing external files.