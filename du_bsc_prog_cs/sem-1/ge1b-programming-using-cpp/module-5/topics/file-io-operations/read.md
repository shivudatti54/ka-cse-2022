# File I/O Operations in C++

## Comprehensive Study Material for GE1B: Programming Using C++

---

## 1. Introduction

File Input/Output (File I/O) operations are fundamental to any programming language and are essential for persistent data storage. In C++, file I/O allows programs to read data from files stored on disk and write data to files for future use. Unlike console I/O which deals with temporary screen output, file I/O enables data persistence beyond program execution.

This topic is a critical component of the GE1B (Generic Elective) syllabus for BSc Physical Science (CS) under NEP 2024 at Delhi University. File handling concepts form the foundation for database systems, file processing applications, and software development in general.

---

## 2. Need and Real-World Relevance

### Why File I/O Matters

- **Data Persistence**: Programs need to store data permanently. When you close a program, without file I/O, all data is lost.
- **Large Data Handling**: Processing data from files allows handling datasets larger than available RAM.
- **Configuration Storage**: Applications store settings and preferences in files.
- **Data Sharing**: Files enable data exchange between different programs and systems.
- **Logging and Auditing**: Applications maintain logs for debugging and security purposes.

### Real-World Applications

| Application Area | Example Use Case |
|-----------------|------------------|
| Banking Systems | Transaction records, account balances |
| Inventory Management | Product database, stock levels |
| Student Records | University grade systems |
| Multimedia | Image/audio file processing |
| Web Servers | Access logs, configuration files |

---

## 3. File I/O Basics in C++

### 3.1 Stream Classes Hierarchy

C++ uses a stream-based approach for file I/O, built upon the iostream library:

```
ios (base class)
    ├── istream (input stream)
    │   └── ifstream (input file stream)
    ├── ostream (output stream)
    │   └── ofstream (output file stream)
    └── iostream (input/output stream)
        └── fstream (file stream)
```

### 3.2 File Stream Classes

| Class | Purpose | Default Mode |
|-------|---------|--------------|
| `ifstream` | Read from files | Input |
| `ofstream` | Write to files | Output |
| `fstream` | Read and write | None (must specify) |

### 3.3 File Opening Modes

The `open()` member function accepts a mode parameter:

| Mode Flag | Description |
|-----------|-------------|
| `ios::in` | Open for reading (input) |
| `ios::out` | Open for writing (output) |
| `ios::app` | Append to end of file |
| `ios::trunc` | Truncate file to zero length (default for ofstream) |
| `ios::binary` | Open in binary mode |
| `ios::ate` | Seek to end of file on opening |

**Note**: Multiple modes can be combined using the bitwise OR operator (`|`).

```cpp
// Example: Opening in multiple modes
ofstream outFile("data.txt", ios::out | ios::app);  // Append mode
fstream inOutFile("file.dat", ios::in | ios::out);  // Read and write
```

---

## 4. Opening and Closing Files

### 4.1 Opening Files

There are two methods to open a file:

**Method 1: Using open() member function**

```cpp
#include <fstream>
using namespace std;

int main() {
    ofstream outFile;
    outFile.open("student.txt");  // Opens student.txt for writing
    
    if (outFile.is_open()) {
        outFile << "Student Name: John Doe" << endl;
        outFile << "Roll Number: 101" << endl;
        outFile.close();  // Important: Always close files
    }
    
    return 0;
}
```

**Method 2: Using constructor (preferred)**

```cpp
#include <fstream>
using namespace std;

int main() {
    // ofstream constructor opens file immediately
    ofstream outFile("output.txt");  // Opens for writing
    
    if (outFile) {
        outFile << "Writing to file using constructor" << endl;
        outFile.close();
    }
    
    return 0;
}
```

### 4.2 Checking if File Opened Successfully

Always verify file opening before performing operations:

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream inFile("nonexistent.txt");
    
    if (!inFile) {
        cout << "Error: Could not open file!" << endl;
        return 1;
    }
    
    // Proceed with file operations...
    inFile.close();
    return 0;
}
```

### 4.3 Closing Files

**Critical**: Always close files after use to:
- Flush buffers and ensure all data is written
- Release system resources
- Prevent data corruption

```cpp
fileStream.close();  // Explicit close

// Or use RAII - file closes automatically when goes out of scope
{
    ofstream out("data.txt");
    out << "Data";
}  // File automatically closed here
```

---

## 5. Text File I/O Operations

### 5.1 Writing to Text Files

Text mode writes human-readable characters:

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ofstream outFile("marks.txt");
    
    if (!outFile) {
        cout << "Error opening file!" << endl;
        return 1;
    }
    
    // Writing individual data items
    outFile << "Student Marks Record" << endl;
    outFile << "---------------------" << endl;
    outFile << "Mathematics: 95" << endl;
    outFile << "Physics: 88" << endl;
    outFile << "Chemistry: 92" << endl;
    
    outFile.close();
    cout << "Data written successfully!" << endl;
    
    return 0;
}
```

### 5.2 Reading from Text Files

```cpp
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ifstream inFile("marks.txt");
    string line;
    
    if (!inFile) {
        cout << "Error opening file!" << endl;
        return 1;
    }
    
    // Method 1: Read line by line using getline()
    while (getline(inFile, line)) {
        cout << line << endl;
    }
    
    inFile.close();
    return 0;
}
```

### 5.3 Reading Word by Word

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream inFile("data.txt");
    string word;
    
    while (inFile >> word) {  // Reads word by word
        cout << word << endl;
    }
    
    inFile.close();
    return 0;
}
```

---

## 6. Binary File I/O

Binary mode writes data in its raw binary representation without any text conversion. This is essential for:
- Storing non-text data (images, audio, video)
- Preserving exact data representation
- Efficient storage (binary is typically smaller than text)

### 6.1 Writing Binary Data

```cpp
#include <fstream>
using namespace std;

struct Student {
    int rollNo;
    char name[50];
    float marks;
};

int main() {
    Student s1 = {101, "Amit Kumar", 85.5};
    Student s2 = {102, "Priya Sharma", 92.0};
    
    ofstream outFile("student.dat", ios::binary);
    
    if (!outFile) {
        cout << "Error opening file!" << endl;
        return 1;
    }
    
    // Write entire structure as binary
    outFile.write(reinterpret_cast<char*>(&s1), sizeof(Student));
    outFile.write(reinterpret_cast<char*>(&s2), sizeof(Student));
    
    outFile.close();
    cout << "Binary data written successfully!" << endl;
    
    return 0;
}
```

### 6.2 Reading Binary Data

```cpp
#include <fstream>
#include <iostream>
using namespace std;

struct Student {
    int rollNo;
    char name[50];
    float marks;
};

int main() {
    Student s;
    
    ifstream inFile("student.dat", ios::binary);
    
    if (!inFile) {
        cout << "Error opening file!" << endl;
        return 1;
    }
    
    // Read binary data
    while (inFile.read(reinterpret_cast<char*>(&s), sizeof(Student))) {
        cout << "Roll No: " << s.rollNo << endl;
        cout << "Name: " << s.name << endl;
        cout << "Marks: " << s.marks << endl;
        cout << "-------------------" << endl;
    }
    
    inFile.close();
    return 0;
}
```

---

## 7. Error Handling in File I/O

Proper error handling is crucial for robust file operations. C++ provides several member functions to check stream state:

### 7.1 Stream State Functions

| Function | Returns true when |
|----------|------------------|
| `good()` | Everything is fine, no errors |
| `eof()` | End of file reached |
| `fail()` | Logical error (e.g., failed to open, type mismatch) |
| `bad()` | Irrecoverable stream error (e.g., disk failure) |

### 7.2 Example: Comprehensive Error Handling

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream inFile("data.txt");
    
    // Check if file opened successfully
    if (!inFile) {
        cout << "Error: Cannot open file for reading!" << endl;
        return 1;
    }
    
    int value;
    while (true) {
        inFile >> value;
        
        if (inFile.eof()) {
            cout << "End of file reached." << endl;
            break;
        }
        
        if (inFile.fail()) {
            cout << "Error: Failed to read integer value!" << endl;
            inFile.clear();  // Clear error flags
            inFile.ignore(); // Ignore bad character
            continue;
        }
        
        if (inFile.bad()) {
            cout << "Fatal error: Irrecoverable stream error!" << endl;
            break;
        }
        
        cout << "Read value: " << value << endl;
    }
    
    inFile.close();
    return 0;
}
```

### 7.3 Proper Error Checking Pattern

```cpp
#include <fstream>
using namespace std;

void writeData(const char* filename) {
    ofstream outFile(filename);
    
    if (!outFile.good()) {
        // Cannot use outFile after this point
        cerr << "File could not be opened!" << endl;
        return;
    }
    
    outFile << "Data";
    outFile.close();
}
```

---

## 8. Random Access and File Positioning

Random access allows moving to any position in a file without reading sequentially. This is essential for:
- Database-like operations
- Updating specific records
- Searching within large files

### 8.1 File Position Indicators

C++ maintains two position pointers:
- **get pointer**: Position for reading (`tellg()`)
- **put pointer**: Position for writing (`tellp()`)

### 8.2 seekp() - Set Write Position

```cpp
#include <fstream>
using namespace std;

int main() {
    ofstream outFile("sample.txt");
    
    outFile << "ABCDEFGHIJ";  // Write 10 characters
    
    // Move to position 5 (6th character)
    outFile.seekp(5);
    outFile << "X";  // Replaces 'F' with 'X'
    
    outFile.close();
    // File now contains: ABCDEXGHIJ
    
    return 0;
}
```

### 8.3 seekg() - Set Read Position

```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream inFile("sample.txt");
    
    // Move to position 3 (4th character)
    inFile.seekg(3);
    
    char ch;
    inFile >> ch;  // Reads 'D'
    cout << "Character at position 3: " << ch << endl;
    
    inFile.close();
    return 0;
}
```

### 8.4 tellg() and tellp() - Get Current Position

```cpp
#include <fstream>
using namespace std;

int main() {
    fstream file("test.txt", ios::in | ios::out);
    
    file << "Hello World";
    
    // Get current write position
    streampos pos = file.tellp();
    cout << "Current write position: " << pos << endl;
    
    // Move back to beginning
    file.seekg(0);
    
    // Get current read position
    pos = file.tellg();
    cout << "Current read position: " << pos << endl;
    
    file.close();
    return 0;
}
```

### 8.5 Seeking from Different Reference Points

The seek functions accept a secondary argument:

```cpp
file.seekg(offset, direction);
file.seekp(offset, direction);
```

| Direction Constant | Meaning |
|--------------------|---------|
| `ios::beg` | From beginning of file (default) |
| `ios::cur` | From current position |
| `ios::end` | From end of file |

```cpp
#include <fstream>
using namespace std;

int main() {
    // Example: Read last 10 characters
    ifstream inFile("largefile.txt", ios::ate);  // Open at end
    
    if (inFile) {
        // Get file size
        streampos size = inFile.tellg();
        
        // Move 10 bytes before end
        inFile.seekg(-10, ios::end);
        
        char buffer[11];
        inFile.read(buffer, 10);
        buffer[10] = '\0';
        
        cout << "Last 10 characters: " << buffer << endl;
    }
    
    inFile.close();
    return 0;
}
```

---

## 9. Practical Examples

### Example 1: Employee Management System (Text Files)

```cpp
#include <fstream>
#include <iostream>
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
    
    void display() {
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Salary: " << salary << endl;
    }
    
    void writeToFile(ofstream& out) {
        out << id << endl;
        out << name << endl;
        out << salary << endl;
    }
    
    void readFromFile(ifstream& in) {
        in >> id;
        in.ignore();
        getline(in, name);
        in >> salary;
    }
};

void addEmployee() {
    Employee emp;
    ofstream outFile("employees.txt", ios::app);
    
    emp.getData();
    emp.writeToFile(outFile);
    
    outFile.close();
    cout << "Employee added successfully!" << endl;
}

void displayAll() {
    Employee emp;
    ifstream inFile("employees.txt");
    
    if (!inFile) {
        cout << "No employee records found!" << endl;
        return;
    }
    
    while (true) {
        emp.readFromFile(inFile);
        if (inFile.eof()) break;
        emp.display();
        cout << "-------------------" << endl;
    }
    
    inFile.close();
}

int main() {
    int choice;
    
    do {
        cout << "\n===== Employee Menu =====" << endl;
        cout << "1. Add Employee" << endl;
        cout << "2. Display All Employees" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                addEmployee();
                break;
            case 2:
                displayAll();
                break;
            case 3:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice!" << endl;
        }
    } while (choice != 3);
    
    return 0;
}
```

### Example 2: Student Record Management (Binary Files)

```cpp
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    int rollNo;
    char name[30];
    float marks;
    
public:
    void input() {
        cout << "Enter Roll Number: ";
        cin >> rollNo;
        cout << "Enter Name: ";
        cin.ignore();
        cin.getline(name, 30);
        cout << "Enter Marks: ";
        cin >> marks;
    }
    
    void display() {
        cout << "\nRoll Number: " << rollNo << endl;
        cout << "Name: " << name << endl;
        cout << "Marks: " << marks << endl;
    }
    
    int getRollNo() {
        return rollNo;
    }
    
    // Binary write
    void writeRecord(fstream& out) {
        out.write(reinterpret_cast<char*>(this), sizeof(Student));
    }
    
    // Binary read
    void readRecord(fstream& in) {
        in.read(reinterpret_cast<char*>(this), sizeof(Student));
    }
};

void addStudent() {
    Student s;
    s.input();
    
    ofstream outFile("students.dat", ios::binary | ios::app);
    s.writeRecord(outFile);
    outFile.close();
    
    cout << "Student record added!" << endl;
}

void searchStudent(int roll) {
    Student s;
    bool found = false;
    
    ifstream inFile("students.dat", ios::binary);
    
    while (inFile.read(reinterpret_cast<char*>(&s), sizeof(Student))) {
        if (s.getRollNo() == roll) {
            s.display();
            found = true;
            break;
        }
    }
    
    inFile.close();
    
    if (!found) {
        cout << "Student with Roll No " << roll << " not found!" << endl;
    }
}

void displayAllStudents() {
    Student s;
    ifstream inFile("students.dat", ios::binary);
    
    if (!inFile) {
        cout << "No records found!" << endl;
        return;
    }
    
    while (inFile.read(reinterpret_cast<char*>(&s), sizeof(Student))) {
        s.display();
        cout << "-------------------" << endl;
    }
    
    inFile.close();
}

int main() {
    int choice, rollNo;
    
    do {
        cout << "\n===== Student Record Menu =====" << endl;
        cout << "1. Add Student" << endl;
        cout << "2. Search Student by Roll No" << endl;
        cout << "3. Display All Students" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                cout << "Enter Roll Number to search: ";
                cin >> rollNo;
                searchStudent(rollNo);
                break;
            case 3:
                displayAllStudents();
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

---

## 10. Common Mistakes and Best Practices

### Common Mistakes to Avoid

1. **Forgetting to close files**: Always close files or use RAII
2. **Not checking file open status**: Always verify before operations
3. **Using text mode for binary data**: Use `ios::binary` for non-text data
4. **Mixing >> with getline()**: May cause issues with newline characters
5. **Not clearing error flags**: After `fail()`, clear flags before continuing

### Best Practices

```cpp
// ✅ GOOD: Using RAII (automatic file closing)
{
    ofstream out("file.txt");
    if (out) {
        out << "Data";
    }
}  // File automatically closed

// ✅ GOOD: Explicit error checking
if (!inFile.is_open()) {
    cerr << "Error opening file";
    return;
}

// ✅ GOOD: Use binary mode for structures
ofstream out("data.bin", ios::binary);

// ❌ BAD: Forgetting to check if file opened
ofstream out("file.txt");
out << "Data";  // May fail silently

// ❌ BAD: Not clearing error state
while (inFile >> value) {  // Infinite loop if fail() but not eof()
    // process
}
```

---

## 11. Assessment Questions

### Multiple Choice Questions

**Question 1:** Which file stream class is used for both reading and writing?
- A) ifstream
- B) ofstream
- C) fstream
- D) iostream

**Question 2:** What is the default mode when opening a file with `ofstream`?
- A) ios::in
- B) ios::out
- C) ios::app
- D) ios::trunc

**Question 3:** Which function is used to move the read pointer to a specific position?
- A) seekp()
- B) tellg()
- C) seekg()
- D) tellp()

**Question 4:** What does the `ios::binary` flag do?
- A) Opens file in read-only mode
- B) Opens file in text mode
- C) Opens file in binary mode (no text conversion)
- D) Creates a backup of the file

**Question 5:** Which function returns true when end of file is reached?
- A) fail()
- B) bad()
- C) good()
- D) eof()

### Scenario-Based Questions

**Question 6:** A program needs to update a specific record in the middle of a file without rewriting the entire file. Which combination of functions is most appropriate?

- A) ios::app and seekg()
- B) ios::in and getline()
- C) fstream with ios::in|ios::out, seekg(), and seekp()
- D) ofstream with ios::trunc

**Question 7:** You are writing a program to read employee records stored as binary data. Each record is 100 bytes. After reading the 5th record, you need to go back and read the 2nd record. What should you do?

- A) Use ios::app to reopen the file
- B) Use seekg(100) to move to the beginning of the 2nd record
- C) Close and reopen the file
- D) Use getline() in a loop

**Question 8:** Consider the following code:

```cpp
ofstream out("data.txt");
out << 100 << endl;
out << "Hello";
out.close();
```

If you open "data.txt" in a text editor, what will you see?

- A) 100Hello
- B) 100\nHello
- C) Binary data
- D) Error

### Coding Questions

**Question 9:** Write a C++ program to count the number of words in a text file named "article.txt".

**Question 10:** Create a program that stores employee data (ID, Name, Salary) in a binary file and provides options to:
- Add new employee
- Display all employees
- Search by ID

**Question 11:** Write a function that reads a binary file containing integers and returns the sum of all integers.

**Question 12:** Explain the difference between seekg() and seekp(). When would you use each?

### Answers

1. **C** - fstream provides both input and output capabilities
2. **B** - ofstream defaults to ios::out which truncates existing files
3. **C** - seekg() sets the get (read) position
4. **C** - Binary mode prevents text conversion
5. **D** - eof() returns true when EOF is reached
6. **C** - fstream with both modes allows random access update
7. **B** - Each record is 100 bytes, so 2nd record starts at byte 100 (0-indexed)
8. **B** - endl adds newline, so output is "100\nHello"
9-12: (See solutions below)

---

## 12. Key Takeaways

1. **File I/O Basics**: C++ uses stream classes (`ifstream`, `ofstream`, `fstream`) for file operations. Always check if files open successfully before proceeding.

2. **Opening Modes**: Understand different modes (`ios::in`, `ios::out`, `ios::app`, `ios::binary`, `ios::trunc`) to choose appropriate file handling behavior.

3. **Text vs Binary**: Use text mode for human-readable data and binary mode for efficient storage of structured data, preserving exact byte representation.

4. **Error Handling**: Always use `good()`, `eof()`, `fail()`, and `bad()` functions to check stream state and handle errors gracefully.

5. **Random Access**: The `seekg()` and `seekp()` functions enable random access within files, essential for database-like operations. Remember `tellg()` and `tellp()` for getting current positions.

6. **File Closing**: Always close files explicitly or use RAII (automatic destructor calls) to ensure data is flushed and resources are released.

7. **Best Practices**: Check file open status, use appropriate modes, handle errors properly, and prefer RAII patterns for resource management.

---

## References

- Delhi University NEP 2024 GE1B Syllabus: Programming Using C++
- C++ Standard Library Documentation
- "The C++ Programming Language" by Bjarne Stroustrup

---

*Study Material prepared for BSc Physical Science (CS), Delhi University, NEP 2024*