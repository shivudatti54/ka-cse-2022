# C++ Streams and File I/O

## Introduction

C++ Streams are a powerful and flexible mechanism for input/output operations. Introduced as part of the C++ Standard Library, streams provide an abstraction for reading from and writing to various data sources including the console, files, and memory buffers. The stream-based I/O system is one of the defining features of C++ that distinguishes it from C's printf and scanf approach, offering type safety, extensibility, and object-oriented design.

In the context of the university's Object-Oriented Programming with C++ curriculum, understanding streams is essential for developing applications that need to handle persistent data, process user input, or perform file operations. The stream library follows object-oriented principles, using classes, inheritance, and polymorphism to create a flexible I/O system that can be easily extended to support new data sources and formatting options.

This module covers the complete stream hierarchy, file handling mechanisms, string streams, and various stream manipulators that enable formatted and unformatted I/O operations. Mastery of these concepts is crucial for practical C++ programming and forms an important component in university examinations.

## Key Concepts

### Stream Class Hierarchy

The C++ I/O system is built on a hierarchy of classes defined in the `<iostream>` header. At the root of this hierarchy is the `ios_base` class, which provides the fundamental functionality common to all streams. From this base class, the `ios` class derives, adding streambuf pointers and formatting state information. The `istream` class specializes in input operations, while `ostream` handles output. The `iostream` class inherits from both, supporting bidirectional I/O.

The standard stream objects include `cin` (standard input - typically keyboard), `cout` (standard output - typically console), `cerr` (standard error - unbuffered), and `clog` (standard error - buffered). These are automatically created when a C++ program starts and are available for immediate use without explicit initialization.

### Stream Buffers

Each stream is associated with a stream buffer object that manages the actual reading and writing of characters. The `streambuf` class provides the interface for buffer management, while `filebuf` and `stringbuf` specialize in file and string buffers respectively. Understanding buffers is important for advanced stream operations, though most everyday programming uses the higher-level stream interfaces.

### File Streams

C++ provides three main classes for file operations: `ifstream` (input file stream) for reading from files, `ofstream` (output file stream) for writing to files, and `fstream` (file stream) for both reading and writing. These classes are defined in the `<fstream>` header.

When opening a file, you can specify the mode parameter that determines how the file should be opened:

| Mode Flag     | Description                             |
| ------------- | --------------------------------------- |
| `ios::in`     | Open for reading (default for ifstream) |
| `ios::out`    | Open for writing (default for ofstream) |
| `ios::app`    | Append to end of file                   |
| `ios::trunc`  | Truncate file to zero length            |
| `ios::binary` | Open in binary mode                     |
| `ios::ate`    | Seek to end of file on open             |

Files can be opened using either the constructor or the `open` method. Always check if the file was opened successfully using the `is_open` method or by testing the stream object in a boolean context.

### String Streams

The `<sstream>` header provides classes for string-based streams. `ostringstream` allows output to a string, `istringstream` enables reading from a string, and `stringstream` supports both operations. These are particularly useful for converting between strings and other data types, as well as for building formatted strings programmatically.

### Stream Manipulators

Stream manipulators are special functions that modify the stream's formatting state. They provide a convenient way to control output format without direct manipulation of stream flags.

**Common Output Manipulators:**

- `endl` - Outputs newline and flushes the stream
- `flush` - Flushes the stream buffer
- `setw(int)` - Sets minimum field width
- `setprecision(int)` - Sets floating-point precision
- `fixed` - Uses fixed-point notation
- `scientific` - Uses scientific notation
- `left`, `right` - Sets alignment
- `setfill(char)` - Sets fill character
- `hex`, `oct`, `dec` - Changes number base

**Important Note on `endl` vs `"\n"`:**
The `endl` manipulator outputs a newline character AND flushes the stream buffer, forcing immediate output. This ensures data is written immediately but has performance implications. Using `"\n"` simply outputs the newline without flushing, which is more efficient for bulk output. For final output or when immediate display is required, `endl` is appropriate.

### Formatted and Unformatted I/O

C++ streams support both formatted and unformatted operations. Formatted I/O uses the extraction (`>>`) and insertion (`<<`) operators, which automatically convert between internal data representation and text format. These operators are overloaded for all fundamental types and can be extended for user-defined types through operator overloading.

Unformatted I/O operations include methods like `get`, `getline`, `read`, `write`, `peek`, `put`, and `ignore`. These provide direct character-level access without any conversion.

### Error Handling

Stream objects maintain error state flags that can be checked to determine the success of I/O operations:

- `good` - Returns true if no error flags are set
- `eof` - Returns true if end-of-file has been reached
- `fail` - Returns true if an I/O operation failed
- `bad` - Returns true if a irrecoverable stream error occurred
- `rdstate` - Returns the current error state flags

After performing I/O operations, it's good practice to check these flags to ensure the operation succeeded.

## Examples

### Example 1: Reading and Writing a Text File

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main {
 // Writing to a file
 std::ofstream outFile("data.txt");

 if (!outFile.is_open) {
 std::cerr << "Error: Could not open file for writing!" << std::endl;
 return 1;
 }

 outFile << "Name: John Doe" << std::endl;
 outFile << "Age: 25" << std::endl;
 outFile << "CGPA: 8.5" << std::endl;
 outFile.close;

 // Reading from a file
 std::ifstream inFile("data.txt");
 std::string line;

 if (!inFile.is_open) {
 std::cerr << "Error: Could not open file for reading!" << std::endl;
 return 1;
 }

 std::cout << "Contents of data.txt:" << std::endl;
 while (std::getline(inFile, line)) {
 std::cout << line << std::endl;
 }
 inFile.close;

 return 0;
}
```

**Step-by-step explanation:**

1. We create an `ofstream` object named "outFile" connected to "data.txt"
2. We check if the file opened successfully using `is_open`
3. We write three lines of formatted data using the insertion operator
4. We close the output file
5. We create an `ifstream` object to read from the same file
6. We use `getline` in a while loop to read line by line until EOF
7. Each line is displayed to console and the input file is closed

### Example 2: Using String Streams for Type Conversion

```cpp
#include <iostream>
#include <sstream>
#include <string>

int main {
 // Converting number to string
 double price = 199.99;
 std::ostringstream oss;
 oss << "Price: Rs. " << std::fixed << std::setprecision(2) << price;
 std::string priceStr = oss.str;
 std::cout << priceStr << std::endl;

 // Converting string to number
 std::string numStr = "42";
 int num;
 std::istringstream iss(numStr);
 iss >> num;
 std::cout << "Converted number: " << num << std::endl;

 // Parsing a comma-separated string
 std::string data = "10,20,30,40,50";
 std::stringstream ss(data);
 std::string token;

 std::cout << "Parsed values: ";
 while (std::getline(ss, token, ',')) {
 int value;
 std::istringstream(token) >> value;
 std::cout << value << " ";
 }
 std::cout << std::endl;

 return 0;
}
```

**Output:**

```
Price: Rs. 199.99
Converted number: 42
Parsed values: 10 20 30 40 50
```

**Explanation:**

- `ostringstream` builds a formatted string by chaining values
- `str` extracts the resulting string
- `istringstream` parses a string into numeric types
- Multiple `stringstream` instances can be used in a pipeline for complex parsing

### Example 3: Using Stream Manipulators for Formatted Output

```cpp
#include <iostream>
#include <iomanip>

int main {
 // Table of student marks
 std::cout << std::left << std::setw(15) << "Name"
 << std::right << std::setw(10) << "Marks"
 << std::setw(10) << "Percentage" << std::endl;
 std::cout << std::string(35, '-') << std::endl;

 std::string names[] = {"Alice", "Bob", "Charlie", "Diana"};
 int marks[] = {85, 92, 78, 95};
 int total = 100;

 for (int i = 0; i < 4; i++) {
 double percentage = (marks[i] * 100.0) / total;
 std::cout << std::left << std::setw(15) << names[i]
 << std::right << std::setw(10) << marks[i]
 << std::fixed << std::setprecision(2)
 << std::setw(10) << percentage << std::endl;
 }

 // Demonstrating various number bases
 int value = 255;
 std::cout << "\nNumber bases:" << std::endl;
 std::cout << "Decimal: " << value << std::endl;
 std::cout << "Hexadecimal: " << std::hex << value << std::endl;
 std::cout << "Octal: " << std::oct << value << std::endl;
 std::cout << "Decimal again: " << std::dec << value << std::endl;

 return 0;
}
```

**Output:**

```
Name Marks Percentage
-----------------------------------
Alice 85 85.00
Bob 92 92.00
Charlie 78 78.00
Diana 95 95.00

Number bases:
Decimal: 255
Hexadecimal: ff
Octal: 377
Decimal again: 255
```

## Exam Tips

1. **Stream Class Hierarchy**: Remember the inheritance hierarchy - ios_base → ios → istream/ostream → iostream. Know the purpose of each class and which header files to include.

2. **File Opening Modes**: Be thorough with file mode flags. Remember that `ios::out` defaults to truncating the file unless `ios::app` or `ios::in` is specified. For `fstream`, always specify the mode explicitly for clarity.

3. **Error Handling**: Always check file open success. Use `is_open` or test the stream directly. Understand the difference between `fail` and `bad` - fail indicates recoverable errors while bad indicates fatal errors.

4. **Manipulators**: Know when to use `endl` versus `"\n"`. Remember that some manipulators like `hex`, `oct`, `dec`, `fixed`, and `scientific` persist until changed, while `setw` applies only to the next insertion.

5. **String Streams**: Understand the three string stream classes and their uses. String streams are excellent for type conversion and parsing formatted strings without using C-style functions.

6. **Binary vs Text Mode**: For binary files, always open with `ios::binary`. Text mode on some systems may perform newline translation (e.g., \n to \r\n on Windows).

7. **Practice File Operations**: Be comfortable with reading/writing using both formatted operators and unformatted functions like getline, read, and write.

8. **Common Mistakes**: Avoid forgetting to close files (though they close automatically in destructors), not checking stream state after operations, and mixing text and binary modes inadvertently.
