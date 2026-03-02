# File I/O: Introduction, File Description, open, create, read, write, close, fcntl functions

### Introduction

- File I/O is a fundamental concept in computer programming, allowing programs to interact with files.
- Files are used to store and retrieve data, providing a convenient way to persist data between program runs.

### File Description

- A file is a collection of bytes stored on secondary storage devices, such as hard drives or solid-state drives.
- Files have the following characteristics:
  - Name
  - Location (path)
  - Size (number of bytes)
  - Attributes (permissions, ownership, etc.)

### Open Function

- The `open()` function is used to open a file for input/output operations.
- It takes two arguments:
  - `file descriptor`: a unique identifier for the file
  - `file name`: the name of the file to open
- Returns a file descriptor, which can be used for subsequent file operations.

### Create Function

- The `creat()` function is used to create a new file.
- It takes two arguments:
  - `file descriptor`: a unique identifier for the file
  - `file name`: the name of the file to create
- Creates a new file with default permissions and ownership.

### Read Function

- The `read()` function is used to read data from a file.
- It takes three arguments:
  - `file descriptor`: a unique identifier for the file
  - `buffer`: a buffer to store the read data
  - `size`: the number of bytes to read
- Returns the number of bytes read.

### Write Function

- The `write()` function is used to write data to a file.
- It takes three arguments:
  - `file descriptor`: a unique identifier for the file
  - `buffer`: a buffer containing the data to write
  - `size`: the number of bytes to write
- Returns the number of bytes written.

### Close Function

- The `close()` function is used to close a file for input/output operations.
- It takes one argument:
  - `file descriptor`: a unique identifier for the file
- Releases system resources associated with the file.

### Fcntl Functions

- The `fcntl()` function is used to perform file control operations.
- Examples of fcntl functions:
  - `F_GETFD`: gets the file descriptor flags
  - `F_SETFD`: sets the file descriptor flags
  - `F_GETLK`: gets the locks on the file
  - `F_SETLK`: sets the locks on the file

## Important Formulas and Definitions

- File descriptor: a unique identifier for a file
- File name: the name of a file
- Location: the path to a file
- Size: the number of bytes in a file
- Attributes: permissions, ownership, etc. of a file

## Key Points

- File I/O is a fundamental concept in computer programming.
- Files are used to store and retrieve data.
- The `open()` function is used to open a file for input/output operations.
- The `creat()` function is used to create a new file.
- The `read()` and `write()` functions are used to read and write data to a file.
- The `close()` function is used to close a file for input/output operations.
- The `fcntl()` function is used to perform file control operations.
