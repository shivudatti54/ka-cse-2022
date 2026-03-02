# File I/O Basics Operations — C++

## Introduction

File Input/Output operations in C++ enable programs to store and retrieve data permanently on secondary storage devices. This is a fundamental topic in the Delhi University BSc (Hons) Computer Science syllabus (NEP 2024, UGCF) under the Programming Using C++ paper. Understanding file handling is essential for developing practical applications that persist data.

## Key Concepts

### File Stream Classes
- **ifstream** — Input file stream (reading from files)
- **ofstream** — Output file stream (writing to files)
- **fstream** — File stream (both reading and writing)

### Opening and Closing Files
- Use `open()` member function to associate a file stream with a physical file
- Syntax: `stream.open("filename", mode);`
- Always close files using `close()` to ensure data is written and resources are freed

### File Opening Modes
| Mode | Description |
|------|-------------|
| `ios::in` | Open for reading (default for ifstream) |
| `ios::out` | Open for writing (default for ofstream) |
| `ios::app` | Append to end of file |
| `ios::trunc` | Truncate file to zero length |
| `ios::binary` | Open in binary mode |

### Reading and Writing Operations
- **Text files**: Use `<<` (insertion) and `>>` (extraction) operators
- **Binary files**: Use `read()` and `write()` functions with `char*` pointers
- Functions like `get()`, `getline()`, `put()` for character-wise I/O

### Error Handling
- Check file opening success using `is_open()` method
- Use `fail()`, `bad()`, `eof()` member functions to check stream state
- Always verify file operations for reliability

### File Pointer Operations
- `seekg()` — Move get pointer (input)
- `seekp()` — Move put pointer (output)
- `tellg()` — Get current position of get pointer
- `tellp()` — Get current position of put pointer

### Text vs Binary Mode
- **Text mode**: Automatic character translation (e.g., newline conversion)
- **Binary mode**: Exact byte-by-byte transfer without translation

## Conclusion

File I/O operations are crucial for data persistence in C++ applications. Master file streams, modes, and error handling to effectively manage data storage. For exams, remember the distinction between file types and their respective I/O functions. Practical programming practice is essential for competency in this topic.