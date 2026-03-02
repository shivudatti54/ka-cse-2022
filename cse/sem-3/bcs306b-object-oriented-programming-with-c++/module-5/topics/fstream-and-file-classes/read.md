# File Handling in C++: fstream and File Classes

## Introduction

File handling is a fundamental aspect of programming that enables persistent data storage. In C++, the Standard Template Library (STL) provides a comprehensive set of classes for file operations through the `<fstream>` header. These classes allow programmers to create, read, write, and manipulate files efficiently. For CSE students studying Object-Oriented Programming with C++, mastering file handling is essential as it forms the backbone of data persistence in real-world applications.

The C++ file handling mechanism is built upon the stream concept, extending the iostream classes to work with files. The three primary classes involved are `ifstream` (input file stream), `ofstream` (output file stream), and `fstream` (file stream supporting both input and output). Understanding these classes and their proper utilization is crucial for developing robust applications that can store and retrieve data between program executions.

This topic covers the theoretical concepts and practical implementations of file handling in C++, including file opening modes, read/write operations, file pointer manipulation, and error handling mechanisms. These skills are frequently tested in university examinations and are indispensable for practical laboratory assignments and project work.

## Key Concepts

### 1. File Stream Classes Overview

The C++ file handling system consists of three main classes defined in the `<fstream>` header:

**ifstream (Input File Stream):**

- Used for reading data from files
- Inherited from `istream`
- Default mode: `ios::in`
- Creates objects that behave like `cin` but read from files

**ofstream (Output File Stream):**

- Used for writing data to files
- Inherited from `ostream`
- Default mode: `ios::out`
- Creates objects that behave like `cout` but write to files

**fstream (File Stream):**

- Supports both input and output operations
- Inherited from `iostream`
- Requires explicit mode specification
- Combines functionality of both ifstream and ofstream

### 2. File Opening Modes

When opening a file, programmers must specify the purpose and behavior using file mode flags. These are defined in the `ios` class and can be combined using the bitwise OR operator (`|`):

| Mode Flag     | Description                                 |
| ------------- | ------------------------------------------- |
| `ios::in`     | Open for reading (input)                    |
| `ios::out`    | Open for writing (output)                   |
| `ios::ate`    | Seek to end of file on opening              |
| `ios::app`    | Append mode - seek to end before each write |
| `ios::trunc`  | Truncate file to zero length if it exists   |
| `ios::binary` | Open in binary mode (no text translation)   |

**Default Modes:**

- `ifstream`: Opens in `ios::in` mode by default
- `ofstream`: Opens in `ios::out | ios::trunc` mode by default
- `fstream`: No default mode; must be specified

### 3. Opening and Closing Files

**Opening a File:**

Files can be opened using two methods in C++:

**Method 1: Constructor initialization**

```cpp
ofstream outFile("data.txt"); // Opens for writing
ifstream inFile("data.txt"); // Opens for reading
fstream file("data.txt", ios::in | ios::out); // Opens for both
```

**Method 2: Using open() function**

```cpp
ofstream outFile;
outFile.open("data.txt");

fstream file;
file.open("data.txt", ios::in | ios::out);
```

**Closing a File:**

```cpp
outFile.close(); // Closes the file associated with outFile
inFile.close();
```

It is mandatory to close files after operations to ensure data is flushed to disk and system resources are released. The destructor of file stream objects automatically closes the file, but explicit closing is considered good practice.

### 4. Reading and Writing Operations

**Text File Operations:**

Writing to text files:

```cpp
ofstream outFile("student.txt");
outFile << "Name: John Doe" << endl;
outFile << "Age: 21" << endl;
outFile << "CGPA: 8.5" << endl;
outFile.close();
```

Reading from text files:

```cpp
ifstream inFile("student.txt");
string name;
int age;
double cgpa;

getline(inFile, name); // Reads entire line
inFile >> age >> cgpa; // Reads formatted data
inFile.close();
```

**Formatted I/O with File Streams:**
File streams support all formatted I/O operations available with console streams, including:

- `<<` operator for output
- `>>` operator for input
- `getline()` for reading lines
- `read()` and `write()` for binary operations

### 5. File Pointer Manipulation

C++ provides functions to manipulate file pointers for random access operations:

**tellg() and tellp():**

- `tellg()`: Returns current position of get (read) pointer
- `tellp()`: Returns current position of put (write) pointer
- Returns position as `streampos` (typically `long`)

**seekg() and seekp():**

- `seekg(offset, direction)`: Moves get pointer
- `seekp(offset, direction)`: Moves put pointer

**Direction parameters:**

- `ios::beg` (0): Beginning of file
- `ios::cur` (1): Current position
- `ios::end` (2): End of file

**Examples:**

```cpp
// Move to beginning
file.seekg(0, ios::beg);

// Move to 10th byte from beginning
file.seekg(10, ios::beg);

// Move 5 bytes forward from current position
file.seekg(5, ios::cur);

// Move to end of file
file.seekp(0, ios::end);

// Get current position
streampos pos = file.tellg();
```

### 6. Binary File Operations

Binary files store data in its raw memory form without any text conversion. They are more efficient for large datasets but not human-readable.

**Opening in Binary Mode:**

```cpp
ofstream outFile("data.bin", ios::binary);
ifstream inFile("data.bin", ios::binary);
```

**Using read() and write() Functions:**

The `write()` function writes raw bytes:

```cpp
#include <cstring>
struct Student {
 char name[50];
 int rollno;
 float marks;
};

Student s1 = {"Alice", 101, 95.5};
ofstream outFile("student.bin", ios::binary);
outFile.write(reinterpret_cast<char*>(&s1), sizeof(s1));
outFile.close();
```

The `read()` function reads raw bytes:

```cpp
Student s2;
ifstream inFile("student.bin", ios::binary);
inFile.read(reinterpret_cast<char*>(&s2), sizeof(s2));
inFile.close();
```

### 7. Error Handling in File Operations

File operations can fail due to various reasons (file not found, permission denied, disk full, etc.). Proper error handling is essential:

**Using fail() function:**

```cpp
ifstream inFile("data.txt");
if (inFile.fail()) {
 cout << "Error: Could not open file!" << endl;
 return 1;
}
```

**Using is_open() function:**

```cpp
ofstream outFile("output.txt");
if (!outFile.is_open()) {
 cout << "Error opening file!" << endl;
 exit(1);
}
```

**Checking for end of file:**

```cpp
while (!inFile.eof()) {
 // Read and process data
}
```

**Better approach - using the extraction operator:**

```cpp
int num;
while (inFile >> num) {
 // Process num
}
```

## Examples

### Example 1: Employee Record Management System

**Problem:** Create a program to write employee records to a file and read them back.

**Solution:**

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Employee {
private:
 int id;
 string name;
 float salary;
public:
 void getData() {
 cout << "Enter ID: ";
 cin >> id;
 cout << "Enter Name: ";
 cin.ignore();
 getline(cin, name);
 cout << "Enter Salary: ";
 cin >> salary;
 }

 void displayData() {
 cout << "ID: " << id << endl;
 cout << "Name: " << name << endl;
 cout << "Salary: " << salary << endl;
 }
};

int main() {
 Employee emp;
 ofstream outFile("employee.txt");

 // Write 3 employee records
 for (int i = 0; i < 3; i++) {
 emp.getData();
 outFile << emp.getId() << endl; // Need getter functions
 outFile << emp.getName() << endl;
 outFile << emp.getSalary() << endl;
 }
 outFile.close();

 // Read and display records
 ifstream inFile("employee.txt");
 while (inFile >> id) {
 // Read and display
 }
 inFile.close();

 return 0;
}
```

**Step-by-step explanation:**

1. Create Employee class with necessary data members
2. Open output file in text mode
3. Collect employee data from user and write to file
4. Close output file to flush data
5. Open input file for reading
6. Read records and display until EOF
7. Close input file

### Example 2: File Copy Program

**Problem:** Write a program to copy contents of one file to another.

**Solution:**

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
 ifstream source("source.txt");
 ofstream dest("destination.txt");

 if (!source.is_open()) {
 cout << "Error: Cannot open source file!" << endl;
 return 1;
 }

 if (!dest.is_open()) {
 cout << "Error: Cannot open destination file!" << endl;
 source.close();
 return 1;
 }

 char ch;
 while (source.get(ch)) {
 dest.put(ch);
 }

 source.close();
 dest.close();

 cout << "File copied successfully!" << endl;
 return 0;
}
```

**Step-by-step explanation:**

1. Open source file for reading and destination for writing
2. Check if files opened successfully using `is_open()`
3. Read character by character using `get()` until EOF
4. Write each character using `put()`
5. Close both files
6. Display success message

### Example 3: Random Access in File

**Problem:** Write a program to update a specific record in a file using random access.

**Solution:**

```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct Student {
 char name[30];
 int marks;
};

int main() {
 // Create initial records
 ofstream outFile("students.dat", ios::binary | ios::out);
 Student s1 = {"Alice", 85};
 Student s2 = {"Bob", 90};
 Student s3 = {"Charlie", 78};

 outFile.write(reinterpret_cast<char*>(&s1), sizeof(s1));
 outFile.write(reinterpret_cast<char*>(&s2), sizeof(s2));
 outFile.write(reinterpret_castchar*>(&s3), sizeof(s3));
 outFile.close();

 // Update second record (Bob's marks to 95)
 fstream file("students.dat", ios::binary | ios::in | ios::out);

 // Move to second record (offset = 1 * sizeof(Student))
 file.seekp(sizeof(s1), ios::beg);

 Student updated = {"Bob", 95};
 file.write(reinterpret_cast<char*>(&updated), sizeof(updated));
 file.close();

 // Verify the update
 ifstream inFile("students.dat", ios::binary);
 Student temp;
 while (inFile.read(reinterpret_cast<char*>(&temp), sizeof(temp))) {
 cout << temp.name << ": " << temp.marks << endl;
 }
 inFile.close();

 return 0;
}
```

**Step-by-step explanation:**

1. Open file in binary mode for writing
2. Create and write three student records
3. Close the file
4. Reopen in read-write mode (`fstream`)
5. Use `seekp()` to move to second record position
6. Write updated record
7. Close file
8. Open in read mode and verify changes

## Exam Tips

1. **Remember the three main classes:** `ifstream` for reading, `ofstream` for writing, and `fstream` for both operations. This is a frequently asked question in university exams.

2. **Know the file opening modes:** Memorize all mode flags (`ios::in`, `ios::out`, `ios::app`, `ios::ate`, `ios::trunc`, `ios::binary`) and their effects on file operations.

3. **Default modes matter:** Remember that `ofstream` defaults to `ios::out | ios::trunc`, which truncates existing files. Use `ios::app` to append.

4. **File pointer functions:** Know the difference between `seekg()` (seek get pointer) and `seekp()` (seek put pointer), and `tellg()` and `tellp()`.

5. **Binary vs Text mode:** Understand when to use binary mode (for structs, images, audio) versus text mode (for human-readable data).

6. **Always check file opening:** Use `is_open()` or `fail()` to verify file operations succeeded before performing I/O.

7. **Close files explicitly:** Although destructors close files, explicit `close()` ensures immediate flushing of buffers and is good practice.

8. **reinterpret_cast for binary I/O:** Remember to use `reinterpret_cast<char*>()` when using `read()` and `write()` functions with non-char data types.

9. **Understand inheritance hierarchy:** `ifstream` inherits from `istream`, `ofstream` from `ostream`, and `fstream` from `iostream`.

10. **Buffer flushing:** Remember that data written to file streams may be buffered. Use `flush()` or `close()` to ensure data is written to disk immediately.
