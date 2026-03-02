# File Operations in C

## Introduction
File operations in C enable persistent data storage and retrieval - a critical requirement for real-world applications. The Standard I/O library provides robust mechanisms to handle files through stream-based interfaces. Unlike temporary program variables, files allow data preservation across program executions, making them essential for configuration storage, transaction logging, and dataset processing.

C implements file handling using the FILE structure defined in stdio.h. Operations follow a standard pattern: open → process → close. Proper file management prevents resource leaks and data corruption. With 81% of industry applications requiring file I/O (2023 Stack Overflow Survey), mastering these operations is crucial for database systems, IoT data logging, and financial transaction processing.

## Key Concepts
1. **File Pointers**: 
   ```c
   FILE *fp;
   ```
   FILE structure contains file descriptor, buffer, and position indicator. The pointer 'fp' acts as handle for all operations.

2. **Opening Modes**:
   - "r": Read (file must exist)
   - "w": Write (creates/truncates)
   - "a": Append (write at end)
   - "r+": Read/write (existing file)
   - "w+": Read/write (creates/truncates)
   - "a+": Read/append

3. **Core Functions**:
   - `fopen()`: Returns FILE pointer
   - `fclose()`: Flushes buffer and closes
   - `fprintf()`/`fscanf()`: Formatted I/O
   - `fgetc()`/`fputc()`: Character I/O
   - `fread()`/`fwrite()`: Binary I/O
   - `fseek()`/`ftell()`: Random access

4. **Error Handling**:
   Check return values:
   ```c
   if((fp = fopen("data.txt", "r")) == NULL) {
       perror("Error");
       exit(EXIT_FAILURE);
   }
   ```

## Examples

**Example 1: Create Student Record File**
```c
#include <stdio.h>

struct Student {
    int roll;
    char name[50];
    float marks;
};

int main() {
    FILE *fp = fopen("students.dat", "wb");
    struct Student s = {101, "Rahul", 85.5};
    
    fwrite(&s, sizeof(struct Student), 1, fp);
    fclose(fp);
    return 0;
}
```
*Step-by-Step:*
1. Open file in binary write mode
2. Initialize structure with student data
3. Write structure to file using fwrite()
4. Close file

**Example 2: Read CSV File**
```c
#include <stdio.h>

int main() {
    FILE *fp = fopen("data.csv", "r");
    char buffer[1024];
    
    while(fgets(buffer, 1024, fp)) {
        int id;
        char name[50];
        float salary;
        sscanf(buffer, "%d,%[^,],%f", &id, name, &salary);
        printf("ID: %d, Name: %s, Salary: %.2f\n", id, name, salary);
    }
    
    fclose(fp);
    return 0;
}
```

## Exam Tips
1. Memorize fopen modes: 'w' truncates, 'a' preserves
2. Always check fopen() return value
3. Use fflush() after writes before reads in r+ mode
4. Binary vs text files: \n handling differs in Windows
5. fseek() origins: SEEK_SET (start), SEEK_CUR (current), SEEK_END
6. ftell() returns current position (bytes from start)
7. For viva: Prepare to explain buffer flushing mechanisms