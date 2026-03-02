# File I/O: Introduction, File Description, open, create, read, write, close, fcntl functions

## **Introduction**

- File Input/Output (I/O) is a fundamental concept in programming, allowing data to be exchanged between a program and the operating system.
- File I/O operations are performed using system calls.

## **File Description**

- A file is a sequence of bytes stored on disk.
- Files have attributes such as:
  - File name
  - File type (e.g., regular file, directory, special file)
  - File permissions
  - File ownership
  - File size
  - File location

## **Open Function**

- `open()`: creates a file descriptor for a file.
- Syntax: `int open(const char *filename, int flag);`
- Parameters:
  - `filename`: file name to open
  - `flag`: file mode (e.g., `O_RDONLY`, `O_WRONLY`, `O_RDWR`)

## **Create Function**

- `creat()`: creates a new file.
- Syntax: `int creat(const char *filename, mode_t mode);`
- Parameters:
  - `filename`: file name to create
  - `mode`: file permissions

## **Read Function**

- `read()`: reads data from a file.
- Syntax: `ssize_t read(int fd, void *buf, size_t count);`
- Parameters:
  - `fd`: file descriptor
  - `buf`: buffer to store read data
  - `count`: number of bytes to read

## **Write Function**

- `write()`: writes data to a file.
- Syntax: `ssize_t write(int fd, const void *buf, size_t count);`
- Parameters:
  - `fd`: file descriptor
  - `buf`: buffer to write data from
  - `count`: number of bytes to write

## **Close Function**

- `close()`: closes a file descriptor.
- Syntax: `int close(int fd);`
- Parameters:
  - `fd`: file descriptor to close

## **fcntl Function**

- `fcntl()`: performs various file control operations.
- Syntax: `int fcntl(int fd, int cmd, ...);`
- Parameters:
  - `fd`: file descriptor
  - `cmd`: file control command (e.g., `F_GETFD`, `F_SETFD`)

## Important Formulas, Definitions, and Theorems

- File size: `size_t filesize(FILE *fp)`
- File position: `off_t lseek(int fd, off_t offset, int whence)`
- File descriptor: `int open(const char *filename, int flag);`
- File mode: `O_RDONLY`, `O_WRONLY`, `O_RDWR`, etc.
