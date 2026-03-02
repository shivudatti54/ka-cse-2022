# **The C++ I/O System Basics: Revision Notes**

## **Overview**

- C++ I/O system allows for input/output operations between programs and devices
- C++ Streams: classes for input/output operations

## **C++ Streams**

- **Input Streams**:
  - `istream` class: input operations
  - Examples: `cin`, `ifstream`
- **Output Streams**:
  - `ostream` class: output operations
  - Examples: `cout`, `ofstream`
- **Bidirectional Streams**:
  - `ostreambuf` class: input and output operations
  - Examples: `fstream`

## **Formatted I/O**

- **Insertion Operators**:
  - `<<` operator: inserts value into stream
  - Examples: `cout << "Hello World" << endl;`
- **Extraction Operators**:
  - `>>` operator: extracts value from stream
  - Examples: `cin >> x;`

## **File I/O**

- **<fstream> Class**:
  - Open, close, read, write files
  - Examples: `ifstream file("example.txt");`
- **File Modes**:
  - `in`, `out`, `trunc`, `app`: file opening modes
  - Examples: `ifstream file("example.txt", ios::in);`

## **Opening and Closing a File**

- **Opening a File**:
  - `ifstream file("example.txt");`
  - `ofstream file("example.txt");`
- **Closing a File**:
  - `file.close();`

## **Reading and Writing**

- **Reading from a File**:
  - `file >> variable;`
- **Writing to a File**:
  - `file << variable;`

## **Important Formulas and Definitions**

- None

## **Theorems**

- None

This summary covers the key points of the topic "The C++ I/O System Basics: C++ Streams, The C++ Classes, Formatted I/O File I/O: <fstream> and File Classes". It provides a concise overview of the main concepts, including C++ Streams, formatted I/O, file I/O, opening and closing a file, reading and writing, and important formulas and definitions.
