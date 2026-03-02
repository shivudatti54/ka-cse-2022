# File I/O Basics Operations in C++

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction to File I/O](#introduction-to-file-io)
2. [Why File I/O Matters](#why-file-io-matters)
3. [File Streams in C++](#file-streams-in-c)
4. [File Modes](#file-modes)
5. [Opening and Closing Files](#opening-and-closing-files)
6. [Reading from Files](#reading-from-files)
7. [Writing to Files](#writing-to-files)
8. [File Positioning: seekp(), seekg(), tellp(), tellg()](#file-positioning-seekg-seekp-tellg-tellp)
9. [Binary File I/O](#binary-file-io)
10. [Error Handling in File Operations](#error-handling-in-file-operations)
11. [Practical Examples](#practical-examples)
12. [Key Takeaways](#key-takeaways)
13. [Multiple Choice Questions](#multiple-choice-questions)
14. [Flashcards](#flashcards)

---

## Introduction to File I/O

**File Input/Output (File I/O)** is a fundamental concept in programming that allows data to be persisted in storage devices (hard disks, SSDs, USB drives) beyond the lifetime of a program's execution. In C++, file I/O is implemented through the **Standard Template Library (STL)** using stream classes that provide a unified interface for reading from and writing to files.

When a C++ program executes, data stored in variables exists only in RAM (Random Access Memory). Once the program terminates, this data is lost unless it has been saved to a permanent storage medium. File I/O bridges this gap by enabling programs to:

- **Store** data persistently
- **Retrieve** previously saved data
- **Share** data between different program executions
- **Process** large datasets that cannot fit in memory

---

## Why File I/O Matters

### Real-World Relevance

File I/O is ubiquitous in software development. Consider these practical applications:

| Application | File I/O Usage |
|-------------|----------------|
| **Banking Systems** | Transaction logs, account balances, customer records |
| **E-commerce Platforms** | Product catalogs, user profiles, order history |
| **Social Media** | Posts, comments, media files, user preferences |
| **Databases** | Underlying storage mechanisms (though often abstracted) |
| **Gaming** | Save states, configuration settings, high scores |
| **Data Analysis** | Reading CSV/Excel files, generating reports |

For a Computer Science student, understanding file I/O is essential because:

1. **Data Persistence**: Every application needs to save user data
2. **System Programming**: Operating systems heavily rely on file operations
3. **Industry Relevance**: File processing skills are tested in placements and interviews
4. **Foundation for Advanced Topics**: Binary files lead to understanding database systems

---

## File Streams in C++

C++ provides three main classes for file operations, which are derived from the `iostream` hierarchy:

### Class Hierarchy

```
ios (base class)
    |
    +-- istream (input stream)
    |       |
    |       +-- ifstream (input file stream)
    |
    +-- ostream (output stream)
            |
            +-- ofstream (output file stream)
    |
    +-- iostream (input/output stream)
            |
            +-- fstream (file stream - both input and output)
```

### Class Descriptions

| Class | Purpose | Default Mode |
|-------|---------|--------------|
| **ifstream** | Read from files | `ios::in` |
| **ofstream** | Write to files | `ios::out \| ios::trunc` |
| **fstream** | Read and write | `ios::in \| ios::out` |

---

## File Modes

File modes specify how a file should be opened—determining whether data can be read, written, or appended. The `ios` class provides these mode flags:

### Complete List of File Modes

| Mode Flag | Description |
|-----------|-------------|
| `ios::in` | Open for reading (input) |
| `ios::out` | Open for writing (output) |
| `ios::app` | Append mode — seek to end before each write |
| `ios::ate` | At end — seek to end on opening (can seek elsewhere) |
| `ios::trunc` | Truncate — discard file contents if file exists |
| `ios::binary` | Open in binary mode (no text translation) |

### Important Notes on File Modes

1. **Default behavior**:
   - `ofstream` defaults to `ios::out | ios::trunc`
   - `ifstream` defaults to `ios::in`
   - `fstream` defaults to `ios::in | ios::out` (but may not create file)

2. **Append mode (`ios::app`)**:
   - Automatically positions cursor at end of file before each write
   - Existing data is preserved; new data is added at the end
   - Cannot overwrite existing content

3. **Binary mode (`ios::binary`)**:
   - Data is read/written in raw binary form
   - No newline translation (`\n` ↔ `\r\n`)
   - Essential for non-text data (images, executables, structures)

4. **Combining modes**:
   ```cpp
   ofstream outFile("data.bin", ios::out | ios::binary);  // Binary write
   ifstream inFile("log.txt", ios::in | ios::ate);        // Read, start at end
   ```

---

## Opening and Closing Files

### Opening Files

There are two methods to open a file:

#### Method 1: Using Constructor (Recommended for simple cases)

```cpp
#include <fstream>
using namespace std;

int main() {
    // Opening for writing
    ofstream outFile("sample.txt");  // Creates or overwrites
    
    // Opening for reading
    ifstream inFile("existing.txt");  // Fails if file doesn't exist
    
    // Opening with explicit mode
    ofstream appendFile("log.txt", ios::app);
    
    return 0;
}
```

#### Method 2: Using open() method

```cpp
#include <fstream>
using namespace std;

int main() {
    ofstream outFile;
    outFile.open("output.txt");  // Default: ios::out | ios::trunc
    
    ofstream appendFile;
    appendFile.open("log.txt", ios::app);
    
    // Always check if file opened successfully
    if (!outFile.is_open()) {
        cerr << "Error: Could not open file!" << endl;
        return 1;
    }
    
    outFile.close();  // Always close when done
    
    return 0;
}
```

### Closing Files

**Always close files** after use to:

1. Flush buffered data to disk
2. Release system resources
3. Prevent data loss

```cpp
outFile.close();  // Flushes buffer and closes file handle
```

**Best Practice**: Use RAII (Resource Acquisition Is Initialization) with local variables, which automatically close files when they go out of scope:

```cpp
void writeData() {
    ofstream outFile("data.txt");
    if (outFile.is_open()) {
        outFile << "Hello, World!";
    }  // File automatically closes here when outFile is destroyed
}
```

---

## Reading from Files

### Using >> Operator (Formatted Input)

The extraction operator `>>` reads whitespace-separated tokens:

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream inFile("numbers.txt");
    
    if (!inFile) {
        cerr << "Cannot open file!" << endl;
        return 1;
    }
    
    int num;
    while (inFile >> num) {
        cout << num << endl;
    }
    
    inFile.close();
    return 0;
}
```

### Using get() — Single Character

```cpp
char ch;
while (inFile.get(ch)) {
    cout << ch;
}
```

### Using getline() — Line Input

```cpp
string line;
while (getline(inFile, line)) {
    cout << line << endl;
}
```

### Using read() — Binary Input

```cpp
struct Student {
    char name[50];
    int roll;
    float marks;
};

Student s;
ifstream inFile("student.dat", ios::binary);
inFile.read(reinterpret_cast<char*>(&s), sizeof(Student));
inFile.close();
```

---

## Writing to Files

### Using << Operator (Formatted Output)

```cpp
#include <fstream>
using namespace std;

int main() {
    ofstream outFile("output.txt");
    
    outFile << "Name: John Doe" << endl;
    outFile << "Age: 21" << endl;
    outFile << "CGPA: 8.5" << endl;
    
    outFile.close();
    return 0;
}
```

### Using put() — Single Character

```cpp
outFile.put('A');
outFile.put('\n');
```

### Using write() — Binary Output

```cpp
struct Product {
    char name[30];
    int quantity;
    double price;
};

Product p = {"Laptop", 10, 45000.00};

ofstream outFile("inventory.dat", ios::binary);
outFile.write(reinterpret_cast<const char*>(&p), sizeof(Product));
outFile.close();
```

---

## File Positioning: seekp(), seekg(), tellp(), tellg()

When working with files, it's often necessary to move to a specific position rather than reading/writing sequentially. C++ provides functions for this.

### Function Overview

| Function | Description |
|----------|-------------|
| `seekg(offset, direction)` | Set get position (input) |
| `seekp(offset, direction)` | Set put position (output) |
| `tellg()` | Get current get position |
| `tellp()` | Get current put position |

### Direction Constants

| Constant | Meaning |
|----------|---------|
| `ios::beg` | From beginning of file (default) |
| `ios::cur` | From current position |
| `ios::end` | From end of file |

### Practical Examples

#### Example 1: Reading from a specific position

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    // Create a sample file
    ofstream create("test.txt");
    create << "0123456789ABCDEF";
    create.close();
    
    // Read specific characters
    ifstream inFile("test.txt");
    
    // Seek to position 5
    inFile.seekg(5, ios::beg);
    
    char ch;
    inFile.get(ch);
    cout << "Character at position 5: " << ch << endl;  // Output: '5'
    
    // Seek 3 positions forward from current
    inFile.seekg(3, ios::cur);
    inFile.get(ch);
    cout << "Character 3 positions ahead: " << ch << endl;  // Output: '8'
    
    // Seek 4 positions before end
    inFile.seekg(-4, ios::end);
    inFile.get(ch);
    cout << "Character 4 from end: " << ch << endl;  // Output: 'D'
    
    // Get current position
    streampos pos = inFile.tellg();
    cout << "Current position: " << pos << endl;
    
    inFile.close();
    return 0;
}
```

#### Example 2: Updating file content at specific position

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    // Create initial file
    ofstream create("data.txt");
    create << "ABCDEFGHIJ";
    create.close();
    
    // Open for read and write
    fstream file("data.txt", ios::in | ios::out);
    
    // Seek to position 4
    file.seekp(4, ios::beg);
    
    // Overwrite character at position 4
    file.put('X');
    
    // Verify: seek back and read
    file.seekg(0, ios::beg);
    
    char ch;
    string result;
    while (file.get(ch)) {
        result += ch;
    }
    
    cout << "Modified content: " << result << endl;  // Output: ABCDEFGHIJ -> ABCDXFGHIJ
    
    file.close();
    return 0;
}
```

---

## Binary File I/O

Binary files store data in its raw memory representation, without any text formatting. This is crucial for:

- Storing complex data structures
- Preserving exact byte values
- Handling non-text data (images, audio, video)
- Improving performance for large datasets

### Writing Binary Data

```cpp
#include <fstream>
#include <string>
using namespace std;

struct Employee {
    int id;
    char name[50];
    double salary;
};

int main() {
    Employee emp = {101, "Priya Sharma", 55000.50};
    
    ofstream outFile("employee.dat", ios::binary);
    
    if (!outFile) {
        cerr << "Error opening file!" << endl;
        return 1;
    }
    
    // Write entire structure as binary
    outFile.write(reinterpret_cast<const char*>(&emp), sizeof(Employee));
    
    outFile.close();
    cout << "Employee data written to binary file." << endl;
    
    return 0;
}
```

### Reading Binary Data

```cpp
#include <fstream>
#include <iostream>
using namespace std;

struct Employee {
    int id;
    char name[50];
    double salary;
};

int main() {
    Employee emp;
    
    ifstream inFile("employee.dat", ios::binary);
    
    if (!inFile) {
        cerr << "Error opening file or file doesn't exist!" << endl;
        return 1;
    }
    
    // Read entire structure as binary
    inFile.read(reinterpret_cast<char*>(&emp), sizeof(Employee));
    
    cout << "ID: " << emp.id << endl;
    cout << "Name: " << emp.name << endl;
    cout << "Salary: " << emp.salary << endl;
    
    inFile.close();
    return 0;
}
```

### Binary vs Text Files Comparison

| Aspect | Text Files | Binary Files |
|--------|------------|--------------|
| **Human Readable** | Yes | No |
| **File Size** | Larger (text representation) | Smaller (raw bytes) |
| **Portability** | Platform-dependent newlines | Same representation |
| **Precision** | May lose precision for floats | Exact byte representation |
| **Speed** | Slower (formatting) | Faster (direct) |
| **Use Case** | Logs, config, CSV | Objects, images, databases |

---

## Error Handling in File Operations

Proper error handling is critical for robust file I/O operations. C++ streams provide several methods to check stream state.

### Stream State Flags

| Method | Returns true when |
|--------|-------------------|
| `good()` | No errors; operation successful |
| `eof()` | End of file reached |
| `fail()` | Logical error (e.g., type mismatch, file not found) |
| `bad()` | Irrecoverable stream error (e.g., disk failure) |

### Example: Comprehensive Error Handling

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream inFile("data.txt");
    
    // Method 1: Check during file opening
    if (!inFile.is_open()) {
        cerr << "Error: Cannot open file for reading!" << endl;
        return 1;
    }
    
    int value;
    while (true) {
        // Method 2: Check after each read operation
        inFile >> value;
        
        if (inFile.eof()) {
            cout << "End of file reached." << endl;
            break;
        }
        
        if (inFile.fail()) {
            cerr << "Error: Failed to read integer value!" << endl;
            inFile.clear();  // Clear error flags
            // Skip bad input
            inFile.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        
        if (inFile.bad()) {
            cerr << "Fatal error: Irrecoverable stream error!" << endl;
            break;
        }
        
        cout << "Read value: " << value << endl;
    }
    
    inFile.close();
    return 0;
}
```

### Best Practices for Error Handling

1. **Always check if file opened successfully**
   ```cpp
   if (!inFile) { /* handle error */ }
   ```

2. **Check for end-of-file properly**
   ```cpp
   // Correct way
   while (inFile >> data) { /* process data */ }
   
   // NOT recommended: checking eof() before read
   while (!inFile.eof()) { /* may read last value twice */ }
   ```

3. **Clear error flags before retrying**
   ```cpp
   inFile.clear();
   inFile.seekg(0);
   ```

4. **Use exceptions (optional)**
   ```cpp
   ofstream outFile;
   outFile.exceptions(ofstream::failbit | ofstream::badbit);
   ```

---

## Practical Examples

### Example 1: Student Record Management System

```cpp
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Student {
    int rollNo;
    string name;
    string course;
    int marks;
};

// Function to add a new student record
void addStudent() {
    ofstream outFile("students.dat", ios::app | ios::binary);
    
    Student s;
    cout << "Enter Roll Number: ";
    cin >> s.rollNo;
    cout << "Enter Name: ";
    cin.ignore();
    getline(cin, s.name);
    cout << "Enter Course: ";
    getline(cin, s.course);
    cout << "Enter Marks: ";
    cin >> s.marks;
    
    outFile.write(reinterpret_cast<const char*>(&s), sizeof(Student));
    outFile.close();
    
    cout << "Student record saved successfully!" << endl;
}

// Function to display all students
void displayAll() {
    ifstream inFile("students.dat", ios::binary);
    
    if (!inFile) {
        cout << "No records found!" << endl;
        return;
    }
    
    Student s;
    cout << "\n===== STUDENT RECORDS =====" << endl;
    
    while (inFile.read(reinterpret_cast<char*>(&s), sizeof(Student))) {
        cout << "Roll No: " << s.rollNo << endl;
        cout << "Name: " << s.name << endl;
        cout << "Course: " << s.course << endl;
        cout << "Marks: " << s.marks << endl;
        cout << "---------------------------" << endl;
    }
    
    inFile.close();
}

// Function to search a student by roll number
void searchStudent(int rollNo) {
    ifstream inFile("students.dat", ios::binary);
    
    Student s;
    bool found = false;
    
    while (inFile.read(reinterpret_cast<char*>(&s), sizeof(Student))) {
        if (s.rollNo == rollNo) {
            cout << "\nStudent Found!" << endl;
            cout << "Roll No: " << s.rollNo << endl;
            cout << "Name: " << s.name << endl;
            cout << "Course: " << s.course << endl;
            cout << "Marks: " << s.marks << endl;
            found = true;
            break;
        }
    }
    
    if (!found) {
        cout << "Student with Roll No " << rollNo << " not found!" << endl;
    }
    
    inFile.close();
}

int main() {
    int choice;
    
    do {
        cout << "\n===== MENU =====" << endl;
        cout << "1. Add Student" << endl;
        cout << "2. Display All Students" << endl;
        cout << "3. Search Student" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                displayAll();
                break;
            case 3:
                int roll;
                cout << "Enter Roll Number to search: ";
                cin >> roll;
                searchStudent(roll);
                break;
            case 4:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice!" << endl;
        }
    } while (choice != 4);
    
    return 0;
}
```

### Example 2: Transaction Log System with Append Mode

```cpp
#include <fstream>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

// Function to get current timestamp
string getTimestamp() {
    time_t now = time(0);
    char* dt = ctime(&now);
    string timestamp(dt);
    timestamp.pop_back();  // Remove newline
    return timestamp;
}

// Function to log transaction
void logTransaction(const string& username, const string& action, double amount) {
    ofstream logFile("transactions.log", ios::app);
    
    if (!logFile) {
        cerr << "Error: Cannot open log file!" << endl;
        return;
    }
    
    logFile << "[" << getTimestamp() << "] ";
    logFile << "User: " << username << " | ";
    logFile << "Action: " << action;
    
    if (amount > 0) {
        logFile << " | Amount: $" << amount;
    }
    
    logFile << endl;
    
    logFile.close();
    cout << "Transaction logged successfully!" << endl;
}

// Function to view transaction history
void viewHistory(const string& username) {
    ifstream logFile("transactions.log");
    
    if (!logFile) {
        cout << "No transactions found!" << endl;
        return;
    }
    
    string line;
    bool found = false;
    
    cout << "\n===== TRANSACTION HISTORY FOR " << username << " =====" << endl;
    
    while (getline(logFile, line)) {
        if (line.find("User: " + username) != string::npos) {
            cout << line << endl;
            found = true;
        }
    }
    
    if (!found) {
        cout << "No transactions found for this user!" << endl;
    }
    
    logFile.close();
}

int main() {
    int choice;
    string username;
    
    do {
        cout << "\n===== BANKING SYSTEM =====" << endl;
        cout << "1. Deposit Money" << endl;
        cout << "2. Withdraw Money" << endl;
        cout << "3. View Transaction History" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;
        
        cout << "Enter username: ";
        cin >> username;
        
        double amount;
        
        switch (choice) {
            case 1:
                cout << "Enter deposit amount: ";
                cin >> amount;
                logTransaction(username, "DEPOSIT", amount);
                break;
            case 2:
                cout << "Enter withdrawal amount: ";
                cin >> amount;
                logTransaction(username, "WITHDRAWAL", amount);
                break;
            case 3:
                viewHistory(username);
                break;
            case 4:
                cout << "Thank you for using the system!" << endl;
                break;
            default:
                cout << "Invalid choice!" << endl;
        }
    } while (choice != 4);
    
    return 0;
}
```

---

## Key Takeaways

1. **File I/O Essentials**: C++ uses `ifstream`, `ofstream`, and `fstream` classes for file operations, providing a stream-based interface similar to `cin` and `cout`.

2. **File Modes**: Understanding modes (`ios::in`, `ios::out`, `ios::app`, `ios::binary`, `ios::trunc`, `ios::ate`) is crucial for correct file behavior.

3. **Always Close Files**: Use `close()` or RAII (local variables) to ensure data is flushed and resources are released.

4. **File Positioning**: Use `seekg()`/`seekp()` to move to specific positions and `tellg()`/`tellp()` to get current position for random access file operations.

5. **Binary I/O**: Use `read()` and `write()` with `ios::binary` mode for storing complex data structures and non-text data.

6. **Error Handling**: Always check file open success, use proper EOF detection (`while(inFile >> data)`), and handle different error conditions using `good()`, `fail()`, `eof()`, and `bad()`.

7. **Practical Applications**: File I/O is essential for data persistence, logging systems, configuration management, and database fundamentals.

---

## Multiple Choice Questions

### Level 1: Basic Recall

1. **Which class is used to read from a file in C++?**
   - A) `ofstream`
   - B) `fstream`
   - C) `ifstream`
   - D) `iostream`

2. **What is the default file mode for `ofstream`?**
   - A) `ios::in`
   - B) `ios::out | ios::trunc`
   - C) `ios::app`
   - D) `ios::binary`

3. **Which function is used to close a file in C++?**
   - A) `end()`
   - B) `finish()`
   - C) `close()`
   - D) `exit()`

### Level 2: Intermediate (File Modes & Operations)

4. **What does `ios::app` mode do when opening a file?**
   - A) Overwrites existing content
   - B) Seeks to beginning before each write
   - C) Appends to end of file before each write
   - D) Opens file in binary mode

5. **Which method reads a single character from a file stream?**
   - A) `get()`
   - B) `read()`
   - C) `>>`
   - D) Both A and C

6. **If you want to preserve existing data and add new data at the end, which mode should you use?**
   - A) `ios::trunc`
   - B) `ios::out`
   - C) `ios::app`
   - D) `ios::ate`

### Level 3: Advanced (File Positioning & Binary I/O)

7. **What will be the output position after `file.seekg(5, ios::end);` on a file with 100 characters?**
   - A) Position 5 from beginning
   - B) Position 95 from beginning
   - C) Position 105 from beginning
   - D) Position 5 from end

8. **Which of the following is used for random access (moving to specific positions) in a file?**
   - A) `seekg()` and `seekp()`
   - B) `tellg()` and `tellp()`
   - C) Both A and B
   - D) `fseek()` and `ftell()`

9. **In binary file I/O, what does `reinterpret_cast<char*>(&obj)` do?**
   - A) Converts object to string
   - B) Treats object's memory address as char pointer for reading/writing bytes
   - C) Creates a new object
   - D) Encrypts the object

10. **Which stream member function returns true when end-of-file is reached?**
    - A) `fail()`
    - B) `bad()`
    - C) `eof()`
    - D) `good()`

### Level 4: Challenging (Error Handling & Edge Cases)

11. **What happens if you try to open a file for reading that does not exist using `ifstream`?**
    - A) An empty file is created
    - B) The stream enters fail state
    - C) The program crashes immediately
    - D) It opens in binary mode

12. **Which method should be called after a read operation fails to reset the stream state?**
    - A) `reset()`
    - B) `clear()`
    - C) `restart()`
    - D) `refresh()`

13. **What is the difference between `seekg(0, ios::end)` and `seekp(0, ios::end)`?**
    - A) They are identical in all file streams
    - B) `seekg` sets read position, `seekp` sets write position
    - C) `seekg` only works with `ifstream`, `seekp` only with `ofstream`
    - D) They cannot be used with the same file stream object

14. **In which scenario would `ios::binary` mode be necessary?**
    - A) Writing a text report
    - B) Writing a CSV file
    - C) Writing a C++ structure containing non-text data
    - D) Writing user messages to display

15. **What does `file.tellg()` return?**
    - A) The total size of the file
    - B) The current get position as a `streampos` object
    - C) The number of bytes read so far
    - D) The end-of-file flag status

### Answer Key

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | C | `ifstream` is specifically for input (reading) operations |
| 2 | B | `ofstream` defaults to `ios::out \| ios::trunc`, which creates new file or truncates existing |
| 3 | C | `close()` is the standard method to close a file stream |
| 4 | C | `ios::app` (append) positions cursor at end before each write operation |
| 5 | D | Both `get()` and extraction operator `>>` can read single characters |
| 6 | C | Append mode (`ios::app`) preserves existing data and adds new data at the end |
| 7 | B | With `seekg(5, ios::end)` on 100-char file: position = 100 - 5 = 95 |
| 8 | C | `seekg/seekp` move position; `tellg/tellp` report current position—used together for random access |
| 9 | B | `reinterpret_cast<char*>` treats memory as byte array for binary read/write operations |
| 10 | C | `eof()` returns true when EOF flag is set after attempting to read past end |
| 11 | B | `ifstream` fails to open non-existent file, entering fail state |
| 12 | B | `clear()` resets all error flags (fail, eof, bad) to allow subsequent operations |
| 13 | B | `seekg` controls reading position; `seekp` controls writing position |
| 14 | C | Binary mode preserves exact byte representation needed for structures with raw data |
| 15 | B | `tellg()` returns `streampos` representing current get (read) position in bytes |

---

## Flashcards

### Basic Concepts

| Term | Definition |
|------|------------|
| **Stream** | An abstraction that represents a flow of data from a source to a destination |
| **Buffer** | A memory area used to temporarily hold data being transferred between program and file |
| **ifstream** | Input file stream class used for reading data from files |
| **ofstream** | Output file stream class used for writing data to files |
| **fstream** | File stream class that supports both input and output operations |

### File Modes

| Term | Definition |
|------|------------|
| **ios::in** | Opens file for reading only |
| **ios::out** | Opens file for writing only |
| **ios::app** | Opens file for appending; cursor positioned at end before each write |
| **ios::trunc** | Discards existing file content when opening for writing |
| **ios::binary** | Opens file in binary mode (no text translation) |
| **ios::ate** | Opens file and positions cursor at end, but allows seeking elsewhere |

### File Operations

| Term | Definition |
|------|------------|
| **seekg()** | Sets the get (read) position in an input stream |
| **seekp()** | Sets the put (write) position in an output stream |
| **tellg()** | Returns current get position as streampos |
| **tellp()** | Returns current put position as streampos |
| **get()** | Reads a single character from stream |
| **put()** | Writes a single character to stream |
| **read()** | Reads raw bytes into memory buffer (binary) |
| **write()** | Writes raw bytes from memory buffer (binary) |
| **getline()** | Reads entire line up to delimiter |

### Error Handling

| Term | Definition |
|------|------------|
| **good()** | Returns true if stream is in good state with no errors |
| **eof()** | Returns true when end-of-file is reached |
| **fail()** | Returns true on logical error (e.g., file not found, type mismatch) |
| **bad()** | Returns true on irrecoverable error (e.g., disk failure) |
| **clear()** | Resets stream error flags to good state |
| **is_open()** | Returns true if file is successfully opened |

---

## Delhi University Syllabus Context

This study material aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science at Delhi University. The content covers:

- ✅ File handling fundamentals (streams, buffers, classes)
- ✅ File modes and their applications
- ✅ Opening, reading, writing, and closing operations
- ✅ File positioning functions (seekg, seekp, tellg, tellp)
- ✅ Binary file operations
- ✅ Error handling and stream states
- ✅ Practical implementations

**Recommended Practical Assignments**:
1. Create a student record management system using binary files
2. Implement a transaction logging system with append mode
3. Build a text file word counter
4. Create a file encryption/decryption utility using binary I/O

---

*Generated for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)*