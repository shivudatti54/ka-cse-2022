# Reading and Writing Text Files in C++

## Introduction

File handling is a fundamental aspect of programming that enables persistent data storage. In C++, the Standard Template Library (STL) provides powerful mechanisms for reading from and writing to files through the fstream library. Text file operations are essential for applications that need to store user data, configuration settings, logs, or any sequential information that can be represented as human-readable characters.

In the context of object-oriented programming with C++, file I/O operations are implemented through stream classes that follow the same paradigms as console I/O. The ifstream class handles input operations from files, ofstream handles output operations to files, and fstream provides both input and output capabilities. Understanding these classes and their member functions is crucial for developing practical C++ applications that can persist and retrieve data efficiently.

This topic covers the theoretical concepts and practical implementations of text file operations in C++, which is a core requirement for the university's BCS306B-Object-Oriented Programming with C++ course. Mastery of file handling enables programmers to build applications that maintain state between executions, making programs more useful and professional.

## Key Concepts

### File Stream Classes

C++ provides three main classes for file operations, all defined in the `<fstream>` header:

**ifstream (Input File Stream):** This class is specifically designed for reading data from files. It inherits from istream and provides member functions specifically suited for file input operations. When you create an ifstream object and associate it with a file, you can use the extraction operator (>>) to read formatted data, or use member functions like get() and getline() for character and line-by-line reading.

**ofstream (Output File Stream):** This class handles writing data to files. Inheriting from ostream, it provides the insertion operator (<<) for writing formatted data and put() for writing individual characters. The ofstream class automatically creates the file if it doesn't exist, or truncates an existing file by default when opened for writing.

**fstream (File Stream):** This class provides both input and output capabilities, inheriting from both iostream. It requires specifying the mode when opening the file to determine whether to read, write, or both.

### Opening and Closing Files

Files must be opened before any read or write operations. The open() member function associates a stream object with a physical file:

```cpp
ofstream outFile;
outFile.open("data.txt");

// or directly in constructor
ifstream inFile("data.txt");
```

Files should be closed when operations are complete using the close() member function:

```cpp
outFile.close();
inFile.close();
```

The destructor automatically closes the file when the stream object goes out of scope, but explicit closing is good practice.

### File Opening Modes

The second parameter of open() or the constructor specifies how the file should be opened:

| Mode Flag   | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| ios::in     | Open for reading (default for ifstream)                     |
| ios::out    | Open for writing (default for ofstream)                     |
| ios::app    | Append mode - data added to end of file                     |
| ios::ate    | Seek to end of file on opening                              |
| ios::trunc  | Truncate file to zero length (default when ios::out is set) |
| ios::binary | Open in binary mode (instead of text mode)                  |

Multiple modes can be combined using the bitwise OR operator (|). For example, `ios::out | ios::app` opens a file for appending.

### Reading from Text Files

**Using Extraction Operator (>>):** The >> operator reads whitespace-separated values, similar to cin:

```cpp
ifstream inFile("numbers.txt");
int num;
while (inFile >> num) {
 cout << num << endl;
}
```

**Using get() and getline():** For character-by-character reading or line-by-line reading:

```cpp
char ch;
ifstream inFile("text.txt");

// Read character by character
while (inFile.get(ch)) {
 cout << ch;
}

// Read line by line
string line;
while (getline(inFile, line)) {
 cout << line << endl;
}
```

**Checking File State:** Several member functions help check file state:

- `is_open()`: Returns true if file is successfully opened
- `good()`: Returns true if no errors occurred
- `eof()`: Returns true when end-of-file is reached
- `fail()`: Returns true if an operation fails

### Writing to Text Files

**Using Insertion Operator (<<):** The << operator writes formatted data:

```cpp
ofstream outFile("output.txt");
outFile << "Name: " << "John Doe" << endl;
outFile << "Age: " << 25 << endl;
outFile << "Score: " << 95.5 << endl;
outFile.close();
```

**Using put() method:** For writing single characters:

```cpp
ofstream outFile("char_file.txt");
outFile.put('A');
outFile.put('B');
outFile.put('C');
outFile.close();
```

## Examples

### Example 1: Copying Contents from One File to Another

**Problem:** Write a C++ program to read content from "source.txt" and copy it to "destination.txt".

**Solution:**

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
 ifstream sourceFile("source.txt");
 ofstream destFile("destination.txt");

 // Check if files opened successfully
 if (!sourceFile.is_open()) {
 cout << "Error: Could not open source file!" << endl;
 return 1;
 }

 if (!destFile.is_open()) {
 cout << "Error: Could not open destination file!" << endl;
 sourceFile.close();
 return 1;
 }

 string line;
 while (getline(sourceFile, line)) {
 destFile << line << endl;
 }

 cout << "File copied successfully!" << endl;

 sourceFile.close();
 destFile.close();

 return 0;
}
```

**Step-by-step explanation:**

1. Create ifstream object for reading from source file
2. Create ofstream object for writing to destination file
3. Check if both files opened successfully using is_open()
4. Use getline() to read each line from source file
5. Write each read line to destination file using insertion operator
6. Close both files to flush data and release resources

### Example 2: Student Grade Management System

**Problem:** Create a program that stores student records (name and marks) to a file and reads them back to display average marks.

**Solution:**

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Student {
private:
 string name;
 int marks;
public:
 Student() : name(""), marks(0) {}
 Student(string n, int m) : name(n), marks(m) {}

 void display() const {
 cout << "Name: " << name << ", Marks: " << marks << endl;
 }

 string getName() const { return name; }
 int getMarks() const { return marks; }
};

void writeStudentData() {
 ofstream outFile("student_data.txt");

 if (!outFile) {
 cout << "Error opening file for writing!" << endl;
 return;
 }

 int n;
 cout << "Enter number of students: ";
 cin >> n;

 for (int i = 0; i < n; i++) {
 string name;
 int marks;
 cout << "Enter name: ";
 cin >> name;
 cout << "Enter marks: ";
 cin >> marks;

 outFile << name << " " << marks << endl;
 }

 outFile.close();
 cout << "Data written successfully!" << endl;
}

void readAndDisplay() {
 ifstream inFile("student_data.txt");

 if (!inFile) {
 cout << "Error opening file for reading!" << endl;
 return;
 }

 string name;
 int marks;
 int total = 0, count = 0;

 cout << "\nStudent Records:" << endl;
 while (inFile >> name >> marks) {
 cout << "Name: " << name << ", Marks: " << marks << endl;
 total += marks;
 count++;
 }

 if (count > 0) {
 cout << "\nAverage Marks: " << (float)total / count << endl;
 }

 inFile.close();
}

int main() {
 writeStudentData();
 readAndDisplay();
 return 0;
}
```

**Step-by-step explanation:**

1. Define a Student class with name and marks as private members
2. Create constructor and getter functions
3. In writeStudentData():

- Open file in output mode
- Accept number of students from user
- Loop and accept student details
- Write each student's data as whitespace-separated values
- Close the file after writing

4. In readAndDisplay():

- Open file in input mode
- Use extraction operator to read name and marks
- Display each student's data
- Calculate and display average marks
- Close the file after reading

### Example 3: Appending Data to Log File

**Problem:** Create a logging system that appends timestamped entries to a log file.

**Solution:**

```cpp
#include <iostream>
#include <fstream>
#include <ctime>
#include <string>
using namespace std;

class Logger {
private:
 string filename;
public:
 Logger(string fname) : filename(fname) {}

 void log(string message) {
 ofstream logFile(filename, ios::app);

 if (!logFile) {
 cout << "Error: Cannot open log file!" << endl;
 return;
 }

 // Get current time
 time_t now = time(0);
 char* dt = ctime(&now);

 // Remove newline from ctime output
 dt[strlen(dt) - 1] = '\0';

 logFile << "[" << dt << "] " << message << endl;

 logFile.close();
 }

 void readLog() {
 ifstream logFile(filename);

 if (!logFile) {
 cout << "No log file found!" << endl;
 return;
 }

 string line;
 cout << "--- Log Contents ---" << endl;
 while (getline(logFile, line)) {
 cout << line << endl;
 }

 logFile.close();
 }
};

int main() {
 Logger logger("application.log");

 logger.log("Application started");
 logger.log("User logged in");
 logger.log("Processing data");
 logger.log("Operation completed");

 cout << "Log entries added successfully!" << endl;

 logger.readLog();

 return 0;
}
```

**Step-by-step explanation:**

1. Create a Logger class with private filename member
2. Constructor initializes filename
3. The log() function:

- Opens file in append mode using ios::app
- Gets current timestamp using ctime()
- Writes timestamped message to file
- File remains open only during write operation

4. The readLog() function:

- Opens file in input mode
- Reads line by line using getline()
- Displays all log entries
- Properly closes file after reading

## Exam Tips

1. **Remember the Header File:** Always include `<fstream>` for file operations in C++. For string operations, include `<string>`.

2. **Know the Three Stream Classes:** ifstream (input), ofstream (output), and fstream (both). Understand which class to use based on operation type.

3. **File Mode Combinations:** Remember that ios::out implies ios::trunc by default. Use ios::app if you want to preserve existing data by appending.

4. **Always Check File Opening:** Use is_open() to verify files opened successfully before performing operations. This is a common exam requirement.

5. **Difference between >> and getline():** The >> operator stops at whitespace and leaves newline in the buffer, while getline() reads entire lines including spaces.

6. **Close Files Explicitly:** While destructors close files, explicit close() ensures data is flushed and is considered good practice in exams.

7. **End-of-File Handling:** Use while(stream >> variable) for reading until EOF. This automatically handles the EOF condition properly.

8. **Default Modes:** ifstream defaults to ios::in, ofstream defaults to ios::out | ios::trunc. Remember these defaults for exam questions.
