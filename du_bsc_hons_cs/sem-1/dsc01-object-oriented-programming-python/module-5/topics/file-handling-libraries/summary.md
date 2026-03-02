# File Handling Libraries — Object Oriented Programming Python

## Introduction

File handling in Python enables programs to persist data beyond runtime by reading from and writing to external files. For BSc (Hons) Computer Science (Delhi University, NEP 2024), file handling is essential for creating robust applications that store and retrieve data efficiently.

## Key Concepts

### File Operations
- **Opening Files**: `open()` function creates file objects
- **Closing Files**: `close()` method releases resources
- **With Statement**: `with open() as f:` ensures automatic resource cleanup

### File Modes
| Mode | Description |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (overwrites) |
| `a` | Append |
| `rb/wb` | Binary read/write |
| `r+` | Read and write |

### File Object Methods
- `read()` / `readline()` / `readlines()` — Reading file content
- `write()` / `writelines()` — Writing to files
- `seek()` — Move file pointer
- `tell()` — Return current position

### Pickle Module (OOP Focus)
- Serializes Python objects to binary format
- `pickle.dump(obj, file)` — Save object
- `pickle.load(file)` — Load object
- Essential for storing class instances and complex data structures

### JSON Handling
- `json.dump()` / `json.load()` — Human-readable data storage
- Useful for configuration files and API data

## Exam-Relevant Points

- Always close files or use `with` statement to prevent resource leaks
- Differentiate between text and binary modes
- Pickle is Python-specific; JSON is universal
- File handling exceptions: `IOError`, `FileNotFoundError`
- Understanding file pointers is crucial for exams

## Conclusion

File handling libraries are fundamental for data persistence in Python applications. Mastery of file operations, the pickle module, and proper error handling is essential for practical OOP programming and exams. Practice file I/O operations thoroughly to score well in practical and theory examinations.