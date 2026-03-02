# File Handling Libraries in Python

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

File handling is a fundamental aspect of persistent data storage and retrieval in programming. In Python, the standard library provides robust mechanisms for reading from and writing to files, enabling applications to store user data, configuration settings, logs, and processed information beyond the lifetime of a program's execution.

### Real-World Relevance

In modern software development, file handling plays a critical role across diverse domains:

- **Data Persistence**: Applications need to save user preferences, database caches, and application states
- **Log Management**: Server logs, debugging information, and audit trails require systematic file operations
- **Data Processing**: ETL (Extract, Transform, Load) pipelines handle CSV, JSON, and XML files
- **Configuration Management**: Software applications read configuration files to customize behavior
- **Document Processing**: Text editors, word processors, and report generators rely on file I/O
- **Media Applications**: Image, audio, and video processing require binary file operations

This topic aligns with the Delhi University BSc (Hons) Computer Science syllabus under the Object Oriented Programming with Python paper, emphasizing practical skills essential for software development roles.

---

## 2. File Handling Fundamentals

### 2.1 The `open()` Function

The primary function for file operations in Python is `open()`, which creates a file object connecting to a file on the filesystem.

```python
file_object = open(filename, mode)
```

**Syntax Components:**
- `filename`: String path to the file (relative or absolute)
- `mode`: String specifying the purpose and format of file access

### 2.2 File Modes

Understanding file modes is crucial for correct file operations. The mode determines whether you're reading, writing, or appending, and whether the file is treated as text or binary.

| Mode | Description | File Position | Creates File | Truncates File |
|------|-------------|---------------|--------------|----------------|
| `'r'` | Read only | Beginning | No | No |
| `'w'` | Write only | Beginning | Yes | Yes |
| `'a'` | Append only | End | Yes | No |
| `'r+'` | Read and write | Beginning | No | No |
| `'w+'` | Read and write | Beginning | Yes | Yes |
| `'a+'` | Read and append | End | Yes | No |

**Binary Modes**: Append `'b'` to any mode for binary access:
- `'rb'`, `'wb'`, `'ab'`, `'rb+'`, `'wb+'`, `'ab+'`

> **Important Note**: `'a'` (append) is a **mode**, not a function. The previous version incorrectly referred to `append()` as a built-in function. The correct usage is `open('file.txt', 'a')` to open a file in append mode.

### 2.3 Closing Files

Always close files after operations to:
- Flush unwritten data to disk
- Release system resources
- Prevent data corruption

```python
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()
```

### 2.4 Context Manager (Recommended Approach)

The `with` statement automatically handles file closure, even if exceptions occur:

```python
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
# File is automatically closed here
```

This is the **best practice** for file handling and is preferred in production code.

---

## 3. Text File Operations

### 3.1 Reading from Text Files

```python
# Reading entire file content
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Reading first n characters
with open('data.txt', 'r') as file:
    partial = file.read(50)

# Reading single line
with open('data.txt', 'r') as file:
    first_line = file.readline()

# Reading all lines into a list
with open('data.txt', 'r') as file:
    lines = file.readlines()
```

### 3.2 Writing to Text Files

```python
# Writing a string
with open('output.txt', 'w') as file:
    file.write('First line\n')
    file.write('Second line')

# Writing multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as file:
    file.writelines(lines)

# Appending to existing file
with open('output.txt', 'a') as file:
    file.write('\nAppended line')
```

---

## 4. Binary File Operations

Binary file handling is essential for non-text data like images, audio files, executables, and serialized objects.

### 4.1 Binary Mode Usage

```python
# Reading an image file
with open('photo.jpg', 'rb') as file:
    image_data = file.read()
    print(f"Read {len(image_data)} bytes")

# Copying a binary file
with open('source.png', 'rb') as src, open('destination.png', 'wb') as dst:
    dst.write(src.read())

# Writing bytes
with open('binary.dat', 'wb') as file:
    data = bytes([0, 1, 2, 3, 255])
    file.write(data)
```

### 4.2 Use Cases for Binary Files

- **Media files**: Images, audio, video
- **Compressed archives**: ZIP, GZIP
- **Serialized data**: Pickle files, database files
- **Executable files**: Binaries, libraries

---

## 5. File Seeking and Positioning

The `tell()` and `seek()` methods control file pointer position for random access operations.

### 5.1 The `tell()` Method

Returns the current file pointer position (in bytes):

```python
with open('example.txt', 'r') as file:
    print(file.tell())  # Output: 0
    file.read(10)
    print(file.tell())  # Output: 10
```

### 5.2 The `seek()` Method

Repositions the file pointer to a specific location:

```python
file.seek(offset, from_what)
```

- `offset`: Number of bytes to move
- `from_what`: Reference point (0=beginning, 1=current, 2=end)

```python
with open('example.txt', 'r') as file:
    # Move to 5th byte from beginning
    file.seek(5)
    print(file.read(10))
    
    # Move 5 bytes forward from current position
    file.seek(5, 1)
    
    # Move to 10 bytes before end
    file.seek(-10, 2)
```

### 5.3 Practical Example: Processing Large Files

```python
# Reading a log file backwards (last 100 lines)
def read_last_lines(filename, n=100):
    with open(filename, 'r') as file:
        file.seek(0, 2)  # Go to end
        size = file.tell()
        
        # Read chunks from end
        lines = []
        chunk_size = 1024
        while len(lines) < n and size > 0:
            size = max(0, size - chunk_size)
            file.seek(size)
            chunk = file.read(chunk_size)
            lines = chunk.split('\n')
        
        return lines[-n:]

# Usage
last_logs = read_last_lines('server.log', 10)
for log in last_logs:
    print(log)
```

---

## 6. Exception Handling in File Operations

Proper exception handling ensures graceful error management and prevents resource leaks.

### 6.1 Common File-Related Exceptions

- `FileNotFoundError`: File doesn't exist (raised with 'r' mode)
- `PermissionError`: Insufficient permissions
- `IOError`: General I/O failures
- `IsADirectoryError`: Path is a directory, not a file

### 6.2 Handling File Exceptions

```python
try:
    with open('config.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: Configuration file not found. Using defaults.")
except PermissionError:
    print("Error: Permission denied to read file.")
except IOError as e:
    print(f"I/O Error occurred: {e}")
finally:
    # Cleanup code if needed
    print("File operation attempted.")
```

### 6.3 Robust File Copy Function

```python
import os
import shutil

def safe_file_copy(source, destination):
    """
    Safely copy a file with comprehensive error handling.
    """
    try:
        # Check if source exists
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source file '{source}' does not exist")
        
        # Check if source is a file
        if not os.path.isfile(source):
            raise ValueError(f"'{source}' is not a file")
        
        # Perform copy
        shutil.copy2(source, destination)
        print(f"Successfully copied '{source}' to '{destination}'")
        return True
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except PermissionError as e:
        print(f"Error: Permission denied - {e}")
        return False
    except IOError as e:
        print(f"I/O Error: {e}")
        return False

# Usage
result = safe_file_copy('data.txt', 'backup/data.txt')
```

---

## 7. The Pickle Module

The `pickle` module implements binary serialization for Python objects, enabling complex data storage and inter-process communication.

### 7.1 Serialization with Pickle

```python
import pickle

# Data structure to serialize
data = {
    'users': [
        {'id': 1, 'name': 'Alice', 'grades': [85, 90, 78]},
        {'id': 2, 'name': 'Bob', 'grades': [92, 88, 95]}
    ],
    'settings': {'theme': 'dark', 'notifications': True},
    'version': '1.0'
}

# Writing serialized data
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Reading serialized data
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    
print(loaded_data['users'][0]['name'])  # Output: Alice
```

### 7.2 Pickle Protocol Versions

```python
import pickle

data = {'key': 'value'}

# Using different protocols (Python 3.8+)
for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
    filename = f'data_p{protocol}.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(data, file, protocol=protocol)
    print(f"Protocol {protocol}: {os.path.getsize(filename)} bytes")

import os
```

> **Security Warning**: Never unpickle untrusted data. Pickle can execute arbitrary code during deserialization.

---

## 8. XML Handling

XML (eXtensible Markup Language) remains widely used for configuration files, data interchange, and web services.

### 8.1 Parsing XML with `xml.etree.ElementTree`

```python
import xml.etree.ElementTree as ET

# Sample XML content
xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book id="1">
        <title>Python Programming</title>
        <author>Guido van Rossum</author>
        <year>2021</year>
    </book>
    <book id="2">
        <title>Clean Code</title>
        <author>Robert Martin</author>
        <year>2008</year>
    </book>
</library>"""

# Parse from string
root = ET.fromstring(xml_content)

# Or parse from file
# tree = ET.parse('books.xml')
# root = tree.getroot()

# Traverse XML tree
print("All books in library:")
for book in root.findall('book'):
    book_id = book.get('id')
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    print(f"  [{book_id}] {title} by {author} ({year})")

# Find specific elements
python_books = root.findall(".//title[contains(text(), 'Python')]")
```

### 8.2 Creating XML Documents

```python
import xml.etree.ElementTree as ET

# Create root element
library = ET.Element('library')

# Add book element
book = ET.SubElement(library, 'book', id='3')
ET.SubElement(book, 'title').text = 'Fluent Python'
ET.SubElement(book, 'author').text = 'Ramalho'
ET.SubElement(book, 'year').text = '2015'

# Create XML tree and write to file
tree = ET.ElementTree(library)
tree.write('new_books.xml', encoding='utf-8', xml_declaration=True)

# Pretty print with indentation
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for child in elem:
            indent(child, level+1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(library)
tree.write('pretty_books.xml', encoding='utf-8', xml_declaration=True)
```

---

## 9. Directory Operations

The `os` and `pathlib` modules provide cross-platform directory manipulation.

### 9.1 The `os` Module

```python
import os

# Current working directory
print(os.getcwd())

# List directory contents
print(os.listdir('.'))

# Create directory
os.makedirs('new_folder/subfolder', exist_ok=True)

# Remove directory (must be empty)
os.rmdir('empty_folder')

# Check existence and type
print(os.path.exists('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('folder'))

# Path operations
print(os.path.join('folder', 'subfolder', 'file.txt'))
print(os.path.splitext('file.txt'))  # ('file', '.txt')
print(os.path.basename('/path/to/file.txt'))  # 'file.txt'
print(os.path.dirname('/path/to/file.txt'))  # '/path/to'
```

### 9.2 The `pathlib` Module (Modern Approach)

```python
from pathlib import Path

# Create Path objects
p = Path('data/files/document.txt')

# Access properties
print(p.name)        # 'document.txt'
print(p.stem)        # 'document'
print(p.suffix)      # '.txt'
print(p.parent)      # PosixPath('data/files')

# File operations
if p.exists():
    print(p.read_text())
    p.write_text('New content')

# Directory operations
(Path('output') / 'results').mkdir(parents=True, exist_ok=True)

# Glob patterns
for py_file in Path('.').glob('**/*.py'):
    print(py_file)

# Iterate directory
for item in Path('.').iterdir():
    if item.is_file():
        print(f"File: {item.name}")
```

---

## 10. Practical Example: Student Record Management

```python
import pickle
import os
from pathlib import Path

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"{self.roll_no}: {self.name} - {self.marks}"

class StudentRecordManager:
    def __init__(self, filename='students.pkl'):
        self.filename = filename
        self.records = []
        self.load_records()
    
    def load_records(self):
        """Load records from pickle file."""
        if Path(self.filename).exists():
            try:
                with open(self.filename, 'rb') as f:
                    self.records = pickle.load(f)
            except Exception as e:
                print(f"Error loading records: {e}")
                self.records = []
    
    def save_records(self):
        """Save records to pickle file."""
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.records, f)
            print("Records saved successfully.")
        except Exception as e:
            print(f"Error saving records: {e}")
    
    def add_student(self, roll_no, name, marks):
        """Add a new student record."""
        student = Student(roll_no, name, marks)
        self.records.append(student)
        self.save_records()
    
    def display_all(self):
        """Display all student records."""
        if not self.records:
            print("No records found.")
            return
        print("\n--- Student Records ---")
        for student in self.records:
            print(student)
        print("----------------------\n")
    
    def search_student(self, roll_no):
        """Search for a student by roll number."""
        for student in self.records:
            if student.roll_no == roll_no:
                return student
        return None

# Usage demonstration
def main():
    manager = StudentRecordManager()
    
    # Add students
    manager.add_student("001", "Alice Sharma", [85, 90, 78])
    manager.add_student("002", "Bob Singh", [92, 88, 95])
    manager.add_student("003", "Carol Gupta", [75, 82, 80])
    
    # Display all
    manager.display_all()
    
    # Search
    result = manager.search_student("002")
    if result:
        print(f"Found: {result}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()
```

---

## 11. Assessment Section

### Multiple Choice Questions

**Question 1** (Easy)
What does the `'w'` mode do when opening a file?
- A) Opens file for reading only
- B) Opens file for writing, creates if doesn't exist, truncates if exists
- C) Opens file for appending
- D) Opens file for both reading and writing

**Answer**: B

---

**Question 2** (Medium)
Which method is used to move the file pointer to a specific position in Python?
- A) `tell()`
- B) `seek()`
- C) `move()`
- D) `position()`

**Answer**: B

---

**Question 3** (Medium)
What will be the output of the following code?

```python
with open('test.txt', 'w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('J')
```
- A) Jello
- B) Hello
- C) J
- D) Error

**Answer**: A

---

**Question 4** (Hard)
Which of the following is the safest way to handle file operations in Python?
- A) Using `try-except` blocks
- B) Using `with` statement (context manager)
- C) Always closing files manually
- D) Using relative paths only

**Answer**: B

---

**Question 5** (Hard)
What does the `pickle` module primarily provide?
- A) XML parsing capabilities
- B) Binary serialization of Python objects
- C) Directory management
- D) Text file compression

**Answer**: B

---

**Question 6** (Medium)
Which file mode would you use to read and write to a file without truncating it, positioning at the beginning?
- A) `'r+'`
- B) `'w+'`
- C) `'a+'`
- D) `'rw'`

**Answer**: A

---

### Fill in the Blanks

1. The **`with`** statement in Python ensures files are automatically closed after operations.
2. In file modes, adding `'b'` (e.g., `'rb'`) indicates **binary** mode.
3. The **`tell()`** method returns the current file pointer position in bytes.
4. **pickle** module is used for serializing and deserializing Python objects.
5. **`xml.etree.ElementTree`** is the standard Python library for XML parsing.
6. The **`pathlib`** module provides an object-oriented interface for path operations.

---

### Flashcards

| Term | Definition |
|------|------------|
| **File Object** | An object that provides methods to interact with a file on disk |
| **Context Manager** | A Python feature using `with` statement that ensures proper resource cleanup |
| **Serialization** | Converting Python objects to bytes for storage or transmission |
| **Deserialization** | Converting serialized bytes back to Python objects |
| **File Pointer** | A cursor indicating the current position in a file for read/write operations |
| **Truncation** | Reducing file size to zero when opened in write mode |
| **Seek Origin** | Reference point for `seek()`: 0=beginning, 1=current, 2=end |
| **Binary Mode** | File mode for non-text data (images, audio, serialized objects) |
| **Pathlib** | Modern Python module for cross-platform path operations |
| **Exception Handling** | Mechanism to handle runtime errors gracefully |

---

## 12. Key Takeaways

1. **File Modes Mastery**: Understanding the difference between `'r'`, `'w'`, `'a'`, and their binary variants (`'rb'`, `'wb'`, etc.) is fundamental. Remember that `'a'` is a **mode** (not a function) for appending to files.

2. **Always Use Context Managers**: The `with` statement ensures files are properly closed, even when exceptions occur. This prevents resource leaks and data corruption.

3. **Binary vs Text Modes**: Use binary modes (`'rb'`, `'wb'`) for non-text data like images, audio, and serialized objects. Text modes handle encoding automatically.

4. **Exception Handling**: Always wrap file operations in try-except blocks to handle `FileNotFoundError`, `PermissionError`, and other I/O exceptions gracefully.

5. **Random Access**: The `seek()` and `tell()` methods enable random access to file contents, essential for large file processing and specific record retrieval.

6. **Pickle for Objects**: The `pickle` module provides powerful serialization for complex Python objects, but never unpickle untrusted data due to security risks.

7. **XML Processing**: The `xml.etree.ElementTree` module offers a simple API for parsing and creating XML documents, widely used in configuration and data interchange.

8. **Modern Path Handling**: The `pathlib` module provides an object-oriented, cleaner alternative to `os.path` functions and should be preferred for new code.

9. **Directory Operations**: Use `os` module for compatibility or `pathlib` for modern, readable path operations including creating, listing, and navigating directories.

10. **Real-World Application**: File handling is essential for data persistence, configuration management, log processing, and building complete software applications that retain data between executions.

---

*This study material covers the complete File Handling Libraries topic as per Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus.*