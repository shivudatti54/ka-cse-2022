# Types of System Calls

## Introduction

System calls can be grouped into six major categories based on the type of service they provide. Each category corresponds to a fundamental OS function. Understanding these categories and their representative system calls is essential for both programming and examinations.

## The Six Categories of System Calls

```
+--------------------------------------------------+
| TYPES OF SYSTEM CALLS |
+--------------------------------------------------+
| 1. Process Control |
| 2. File Management |
| 3. Device Management |
| 4. Information Maintenance |
| 5. Communication |
| 6. Protection |
+--------------------------------------------------+
```

## 1. Process Control

Process control system calls manage the creation, execution, and termination of processes.

### Key System Calls

| System Call | Description                                                     |
| ----------- | --------------------------------------------------------------- |
| `fork()`    | Create a new (child) process by duplicating the calling process |
| `exec()`    | Replace the current process image with a new program            |
| `exit()`    | Terminate the calling process                                   |
| `wait()`    | Wait for a child process to terminate                           |
| `abort()`   | Abnormally terminate a process                                  |
| `getpid()`  | Get the process ID of the calling process                       |
| `kill()`    | Send a signal to a process                                      |

### How fork() and exec() Work Together

```
Parent Process (PID = 100)
 |
 fork() ---> Creates child process
 | |
 Parent (PID=100) Child (PID=101)
 returns child PID returns 0
 | |
 continues exec("/bin/ls")
 | |
 wait() replaces process
 | image with "ls"
 resumes |
 when child ls executes
 exits and exits
```

### Example: Process Control in C

```c
#include <unistd.h>
#include <sys/wait.h>

int main() {
 pid_t pid = fork(); // Create child process

 if (pid == 0) {
 // Child process
 exec("/bin/ls"); // Replace with "ls" program
 exit(1); // Only reached if exec fails
 } else {
 // Parent process
 wait(NULL); // Wait for child to finish
 printf("Child done\n");
 }
 return 0;
}
```

### Windows Equivalents

| UNIX/Linux | Windows                 | Purpose             |
| ---------- | ----------------------- | ------------------- |
| `fork()`   | `CreateProcess()`       | Create new process  |
| `exec()`   | `CreateProcess()`       | Execute new program |
| `exit()`   | `ExitProcess()`         | Terminate process   |
| `wait()`   | `WaitForSingleObject()` | Wait for process    |
| `abort()`  | `TerminateProcess()`    | Kill a process      |
| `getpid()` | `GetCurrentProcessId()` | Get process ID      |

## 2. File Management

File management system calls handle the creation, deletion, reading, writing, and manipulation of files.

### Key System Calls

| System Call             | Description                                         |
| ----------------------- | --------------------------------------------------- |
| `open()`                | Open a file and return a file descriptor            |
| `close()`               | Close an open file descriptor                       |
| `read()`                | Read data from an open file                         |
| `write()`               | Write data to an open file                          |
| `create()`              | Create a new file                                   |
| `delete()` / `unlink()` | Delete a file                                       |
| `lseek()`               | Move the file pointer to a specific position        |
| `stat()`                | Get file attributes (size, permissions, timestamps) |
| `chmod()`               | Change file permissions                             |
| `chown()`               | Change file owner                                   |

### File Operations Flow

```
+--------+ +---------+ +---------+ +---------+
| open() | --> | read() | --> | write() | --> | close() |
| | | or | | (modify)| | |
| Get fd | | read() | | | | Release |
+--------+ +---------+ +---------+ +---------+
 | |
 +-- File Descriptor (fd) used throughout -------+
```

### Example: File Operations in C

```c
int fd = open("data.txt", O_RDWR); // Open file
char buf[100];
read(fd, buf, 100); // Read 100 bytes
write(fd, "Hello", 5); // Write 5 bytes
lseek(fd, 0, SEEK_SET); // Move to beginning
close(fd); // Close file
```

### Windows Equivalents

| UNIX/Linux | Windows            | Purpose      |
| ---------- | ------------------ | ------------ |
| `open()`   | `CreateFile()`     | Open file    |
| `read()`   | `ReadFile()`       | Read data    |
| `write()`  | `WriteFile()`      | Write data   |
| `close()`  | `CloseHandle()`    | Close file   |
| `lseek()`  | `SetFilePointer()` | Seek in file |

## 3. Device Management

Device management system calls handle I/O devices. In UNIX, devices are treated as special files, so many file system calls also work for devices.

### Key System Calls

| System Call             | Description                                  |
| ----------------------- | -------------------------------------------- |
| `open()` / `request()`  | Request access to a device                   |
| `close()` / `release()` | Release a device                             |
| `read()`                | Read from a device                           |
| `write()`               | Write to a device                            |
| `ioctl()`               | Device-specific control operations           |
| `mmap()`                | Map device memory into process address space |

### UNIX: Everything is a File

In UNIX/Linux, devices appear as special files in the `/dev` directory:

```
/dev/sda --> Hard disk
/dev/tty --> Terminal
/dev/null --> Null device (discards all data)
/dev/random --> Random number generator
/dev/usb --> USB devices
```

This allows the same `read()`, `write()`, and `open()` system calls to work with both files and devices.

### Windows Equivalents

| UNIX/Linux | Windows             | Purpose          |
| ---------- | ------------------- | ---------------- |
| `ioctl()`  | `DeviceIoControl()` | Device control   |
| `read()`   | `ReadFile()`        | Read from device |
| `write()`  | `WriteFile()`       | Write to device  |

## 4. Information Maintenance

Information maintenance system calls transfer information between the user program and the operating system.

### Key System Calls

| System Call      | Description                               |
| ---------------- | ----------------------------------------- |
| `getpid()`       | Get process ID                            |
| `getuid()`       | Get user ID                               |
| `time()`         | Get current time                          |
| `gettimeofday()` | Get time with microsecond precision       |
| `sleep()`        | Suspend process for specified time        |
| `alarm()`        | Set an alarm timer                        |
| `uname()`        | Get system information (OS name, version) |
| `sysinfo()`      | Get overall system statistics             |

### Categories of Information

```
+------------------------------------------+
| Information Maintenance |
+------------------------------------------+
| |
| Time: time(), gettimeofday(), |
| clock_gettime() |
| |
| Process: getpid(), getppid(), |
| getuid(), getgid() |
| |
| System: uname(), sysinfo(), |
| gethostname() |
| |
| Timer: alarm(), sleep(), |
| nanosleep() |
+------------------------------------------+
```

### Windows Equivalents

| UNIX/Linux | Windows                 | Purpose          |
| ---------- | ----------------------- | ---------------- |
| `time()`   | `GetLocalTime()`        | Get current time |
| `sleep()`  | `Sleep()`               | Pause execution  |
| `getpid()` | `GetCurrentProcessId()` | Get process ID   |
| `uname()`  | `GetComputerName()`     | Get system info  |

## 5. Communication

Communication system calls enable inter-process communication (IPC). There are two fundamental models:

### Message Passing Model

Processes communicate by exchanging messages through the kernel.

```
+----------+ +----------+
| Process | send() | Process |
| A | -------> | B |
| | <------- | |
+----------+ receive()+----------+
 \ /
 \ Kernel /
 +----------+
 | Message |
 | Queue |
 +----------+
```

### Shared Memory Model

Processes share a region of memory for communication.

```
+----------+ +----------+
| Process | | Process |
| A | | B |
| | | |
+----+-----+ +-----+----+
 | |
 +-------> +----------+ <--------+
 | Shared |
 | Memory |
 | Region |
 +----------+
```

### Key System Calls

| System Call | Model           | Description                                   |
| ----------- | --------------- | --------------------------------------------- |
| `pipe()`    | Message Passing | Create a unidirectional communication channel |
| `socket()`  | Message Passing | Create a network communication endpoint       |
| `send()`    | Message Passing | Send data through a socket                    |
| `recv()`    | Message Passing | Receive data from a socket                    |
| `msgsnd()`  | Message Passing | Send message to a message queue               |
| `msgrcv()`  | Message Passing | Receive message from a message queue          |
| `shmget()`  | Shared Memory   | Create/access a shared memory segment         |
| `shmat()`   | Shared Memory   | Attach shared memory to process address space |
| `shmdt()`   | Shared Memory   | Detach shared memory                          |

### Comparison: Message Passing vs Shared Memory

| Feature             | Message Passing          | Shared Memory                       |
| ------------------- | ------------------------ | ----------------------------------- |
| **Speed**           | Slower (kernel involved) | Faster (direct memory access)       |
| **Ease of use**     | Easier (OS handles sync) | Harder (programmer handles sync)    |
| **Data size**       | Small messages           | Large data sets                     |
| **Synchronization** | Built-in (send/receive)  | Requires explicit sync (semaphores) |
| **Network support** | Yes (sockets)            | No (same machine only)              |

### Windows Equivalents

| UNIX/Linux | Windows               | Purpose        |
| ---------- | --------------------- | -------------- |
| `pipe()`   | `CreatePipe()`        | Create pipe    |
| `shmget()` | `CreateFileMapping()` | Shared memory  |
| `socket()` | `socket()` (Winsock)  | Network socket |

## 6. Protection

Protection system calls control access to resources and enforce security policies.

### Key System Calls

| System Call | Description                        |
| ----------- | ---------------------------------- |
| `chmod()`   | Change file permission mode        |
| `chown()`   | Change file owner and group        |
| `umask()`   | Set default file permission mask   |
| `setuid()`  | Set user ID                        |
| `setgid()`  | Set group ID                       |
| `chroot()`  | Change root directory (sandboxing) |

### UNIX File Permissions

```
Permission Format: rwxrwxrwx
 | | |
 | | +-- Others (world)
 | +----- Group
 +-------- Owner

r = read (4)
w = write (2)
x = execute (1)

Example: chmod 755 file.txt
Owner: rwx (7 = 4+2+1)
Group: r-x (5 = 4+0+1)
Others: r-x (5 = 4+0+1)
```

### Windows Equivalents

| UNIX/Linux | Windows             | Purpose              |
| ---------- | ------------------- | -------------------- |
| `chmod()`  | `SetFileSecurity()` | Set file permissions |
| `chown()`  | `SetSecurityInfo()` | Change owner         |

## Complete Summary Table

| Category              | UNIX Examples                    | Windows Examples                                | Purpose            |
| --------------------- | -------------------------------- | ----------------------------------------------- | ------------------ |
| **Process Control**   | fork, exec, exit, wait, abort    | CreateProcess, ExitProcess, WaitForSingleObject | Manage processes   |
| **File Management**   | open, close, read, write, lseek  | CreateFile, ReadFile, WriteFile, CloseHandle    | Manage files       |
| **Device Management** | open, close, read, write, ioctl  | ReadFile, WriteFile, DeviceIoControl            | Manage devices     |
| **Info Maintenance**  | getpid, time, sleep, uname       | GetCurrentProcessId, GetLocalTime, Sleep        | System information |
| **Communication**     | pipe, shmget, socket, send, recv | CreatePipe, CreateFileMapping, socket           | IPC mechanisms     |
| **Protection**        | chmod, chown, umask, chroot      | SetFileSecurity, SetSecurityInfo                | Access control     |

## Exam Tips

1. **Six categories** is a classic 10-mark question. Memorize: Process Control, File Management, Device Management, Information Maintenance, Communication, Protection.
2. **Know at least 3-4 system calls per category** with brief descriptions -- this is frequently asked.
3. **UNIX vs Windows equivalents** table is an important comparison that shows you understand cross-platform concepts.
4. **fork() and exec()** are the most commonly asked process control system calls. Know how they work together to create and run a new process.
5. **Message Passing vs Shared Memory** comparison is a common question. Know the differences in speed, ease of use, and synchronization.
6. **File management system calls** (open, read, write, close) form the basis for understanding I/O -- trace through a complete file operation.
7. **UNIX philosophy "Everything is a file"** -- understand that devices in /dev are accessed using the same system calls as regular files.
8. ** commonly asks:** "Explain the different types of system calls with examples" or "List and explain system calls for process control and file management."
