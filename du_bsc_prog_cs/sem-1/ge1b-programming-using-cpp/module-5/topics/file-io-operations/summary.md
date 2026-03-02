# File I/O Operations in C++

## Introduction

File Input/Output (I/O) operations in C++ enable programs to store and retrieve data permanently from secondary storage devices. This is essential for data persistence, allowing information to be saved between program executions. The Delhi University NEP 2024 syllabus for BSc Physical Science (CS) covers file handling as a fundamental concept in C++ programming.

---

## Key Concepts

### 1. File Stream Classes
C++ provides three main stream classes for file operations:
- **ifstream** (Input File Stream) – for reading data from files
- **ofstream** (Output File Stream) – for writing data to files
- **fstream** (File Stream) – for both reading and writing

### 2. Opening and Closing Files
```cpp
#include <fstream>
using namespace std;

ofstream outFile("data.txt");  // Opens file for writing
ifstream inFile("data.txt");   // Opens file for reading
fstream file("data.txt", ios::in | ios::out);  // Opens for both

file.close();  // Always close files after use
```

### 3. File Opening Modes
| Mode | Description |
|------|-------------|
| `ios::in` | Open for reading |
| `ios::out` | Open for writing |
| `ios::app` | Append to end of file |
| `ios::trunc` | Truncate (delete) existing content |
| `ios::binary` | Open in binary mode |
| `ios::ate` | Set position at end of file |

### 4. Reading and Writing Operations
- **Text Files**: Use `<<` (insertion) and `>>` (extraction) operators
- **Binary Files**: Use `read()` and `write()` functions with `char*` casting

```cpp
// Text file writing
ofstream out("student.txt");
out << "Name: Rahul" << endl;
out << "Marks: 85" << endl;

// Text file reading
ifstream in("student.txt");
string name;
getline(in, name);
```

### 5. Error Handling
Important error-checking functions:
- `good()` – returns true if no errors
- `eof()` – returns true if end-of-file reached
- `fail()` – returns true if operation failed
- `bad()` – returns true if fatal error occurred

### 6. File Pointer Manipulation
- **seekg()** – sets get pointer position
- **seekp()** – sets put pointer position
- **tellg()** – returns current get position
- **tellp()** – returns current put position

```cpp
file.seekg(0, ios::beg);  // Move to beginning
file.seekg(10, ios::cur); // Move 10 bytes forward
```

---

## Important Points for Exam

- Always check if file opened successfully before operations
- Use `ios::app` mode to append data without overwriting
- Binary files are faster but not human-readable
- Close files explicitly or rely on destructor
- Text mode is default; specify `ios::binary` for binary files

---

## Conclusion

File I/O operations are crucial for developing practical C++ applications that persist data. Mastery of stream classes, file modes, and error handling enables programmers to create robust applications capable of data storage and retrieval. Understanding these concepts is essential for the Delhi University examinations under the NEP 2024 curriculum.