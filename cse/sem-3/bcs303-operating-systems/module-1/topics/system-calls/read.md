# System Calls

## Introduction

A **system call** is the programmatic interface through which a user-level program requests a service from the operating system kernel. System calls provide the essential boundary between user-mode applications and kernel-mode OS services.

> **Definition:** A system call is a mechanism that provides the interface between a process and the operating system. It is the way by which a computer program requests a service from the kernel of the operating system.

Since user programs run in **user mode** (restricted access), they cannot directly access hardware or perform privileged operations. System calls provide a controlled gateway to **kernel mode** (privileged access) where the OS can perform the requested operation on behalf of the program.

## Why System Calls Are Needed

```
+-------------------+ Cannot directly access
| User Program | ---------X---------> Hardware
| (User Mode) |
+-------------------+
 |
 System Call (controlled gateway)
 |
 v
+-------------------+ Full access
| OS Kernel | -----------------> Hardware
| (Kernel Mode) |
+-------------------+
```

- User programs operate in a **restricted environment** (user mode)
- Direct hardware access by user programs would be dangerous (could crash the system, corrupt data, violate security)
- System calls provide a **safe, controlled** mechanism to request OS services
- The OS validates each request before executing it

## How System Calls Work

### Step-by-Step Process

When a program makes a system call, the following sequence occurs:

```
Step 1: User program calls API function (e.g., read())
Step 2: API function places system call number in a register
Step 3: API function executes a TRAP instruction (software interrupt)
Step 4: CPU switches from user mode to kernel mode
Step 5: Kernel examines system call number
Step 6: Kernel dispatches to the appropriate handler via
 the system call table
Step 7: Handler executes the requested operation
Step 8: Result is placed in a register
Step 9: CPU switches back to user mode
Step 10: Control returns to the user program with the result
```

### Detailed Flow Diagram

```
USER MODE KERNEL MODE
+-----------+ +------------------+
| User | | System Call |
| Program | | Table |
| | | +------+-------+ |
| read() --|--+ | | 0 | open | |
| | | | | 1 | close | |
+-----------+ | | | 2 | read | |
 | | | 3 | write | |
 v | | ... | ... | |
 +----------+ | +------+-------+ |
 | C Library| | | |
 | (libc) | | v |
 | | | +--------------+ |
 | INT 0x80 |--TRAP------>| | sys_read() | |
 | or | | | handler | |
 | SYSCALL | | +--------------+ |
 +----------+ +------------------+
 ^ |
 | |
 +------ return value -------+
```

## API vs System Call vs System Call Interface

It is important to understand the distinction between these three related concepts:

### Application Programming Interface (API)

An **API** is a set of functions available to application programmers. Programmers use APIs rather than direct system calls because:

1. **Portability:** Programs written using APIs can be compiled on any system that supports the same API
2. **Simplicity:** APIs are easier to use than raw system calls
3. **Abstraction:** APIs handle the details of invoking system calls

### Common APIs

| API                 | Platform             | Description                                                                                                  |
| ------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------ |
| **POSIX API**       | UNIX/Linux/macOS     | Portable Operating System Interface; defines standard functions like `open()`, `read()`, `write()`, `fork()` |
| **Win32/Win64 API** | Windows              | Windows-specific API; functions like `CreateFile()`, `ReadFile()`, `CreateProcess()`                         |
| **Java API**        | JVM (cross-platform) | Platform-independent API; classes like `File`, `Socket`, `Thread`                                            |

### System Call Interface

The **System Call Interface** is a layer that serves as the link between the API and the actual system calls in the kernel. It:

- Intercepts function calls made through the API
- Looks up the system call number in the **system call table**
- Invokes the appropriate kernel-mode system call handler
- Returns the result (including status and error codes) to the caller

```
+------------------+
| Application | Uses API functions
+------------------+
 |
 v
+------------------+
| API (e.g., POSIX)| Provides portable interface
+------------------+
 |
 v
+------------------+
| System Call | Maps API calls to system calls
| Interface | using system call number table
+------------------+
 |
 v
+------------------+
| Kernel | Executes the actual operation
| (System Call |
| Handlers) |
+------------------+
```

> **Key Point:** The caller (programmer) needs to know nothing about how the system call is implemented. They only need to obey the API and understand what the OS will do as a result of the call.

## System Call Parameter Passing

System calls often require parameters (e.g., file name, buffer address, number of bytes). There are three general methods for passing parameters to the OS:

### Method 1: Registers

- Parameters are placed directly in **CPU registers**
- Simplest and fastest method
- **Limitation:** Limited by the number of available registers

```
Example: read(fd, buffer, count)

Register EAX = system call number (e.g., 3 for read)
Register EBX = fd (file descriptor)
Register ECX = buffer (pointer to buffer)
Register EDX = count (number of bytes)
```

### Method 2: Block / Table in Memory

- Parameters are stored in a **block (table) in memory**
- The **address of the block** is passed in a register
- Used when there are more parameters than available registers
- Used by **Linux** and **Solaris**

```
+----------+
| Register | ----> points to ---> +-------------------+
| (address)| | Parameter Block |
+----------+ | +-------+-------+ |
 | | Param1| value | |
 | | Param2| value | |
 | | Param3| value | |
 | | ... | ... | |
 | +-------+-------+ |
 +-------------------+
```

### Method 3: Stack

- Parameters are **pushed onto the stack** by the program
- The OS **pops them off the stack** to read them
- No limit on the number or length of parameters
- Used by some systems as an alternative to block method

```
Stack:
+----------+
| count | <-- pushed last, popped first
+----------+
| buffer |
+----------+
| fd |
+----------+
| sys_call#| <-- pushed first
+----------+
```

### Comparison of Parameter Passing Methods

| Method          | Speed    | Capacity                  | Used By            |
| --------------- | -------- | ------------------------- | ------------------ |
| **Registers**   | Fastest  | Limited by register count | Simple calls       |
| **Block/Table** | Fast     | Unlimited                 | Linux, Solaris     |
| **Stack**       | Moderate | Unlimited                 | Some UNIX variants |

> **Note:** Block and stack methods do not limit the number or length of parameters being passed. The register method is the fastest but limited.

## Example: How read() System Call Works

Let us trace through a complete example of how the `read()` system call works:

### C Program Code

```c
#include <unistd.h>

int main() {
 char buffer[100];
 int fd = open("data.txt", O_RDONLY); // System call: open
 int bytes = read(fd, buffer, 50); // System call: read
 close(fd); // System call: close
 return 0;
}
```

### Detailed Trace of read(fd, buffer, 50)

```
Step 1: User program calls read(fd, buffer, 50)
 |
Step 2: C library (glibc) function read() is invoked
 |
Step 3: Library function sets up parameters:
 - EAX register = 3 (system call number for read)
 - EBX register = fd (file descriptor value)
 - ECX register = buffer (address of buffer)
 - EDX register = 50 (number of bytes to read)
 |
Step 4: Library executes INT 0x80 (x86) or SYSCALL instruction
 |
 ========= MODE SWITCH: User Mode -> Kernel Mode =========
 |
Step 5: CPU transfers control to kernel's system call handler
 |
Step 6: Kernel reads EAX (=3) and looks up system call table
 - Entry 3 = sys_read() function
 |
Step 7: Kernel calls sys_read(fd, buffer, 50)
 - Validates file descriptor
 - Checks buffer address is valid
 - Reads data from the file into kernel buffer
 - Copies data from kernel buffer to user buffer
 |
Step 8: Kernel places return value in EAX register
 - Returns number of bytes read (or -1 on error)
 |
 ========= MODE SWITCH: Kernel Mode -> User Mode =========
 |
Step 9: Control returns to C library function
 |
Step 10: Library returns the result to user program
 bytes = 50 (or actual number of bytes read)
```

## System Call Numbers

Each system call is assigned a unique number. The kernel maintains a **system call table** that maps these numbers to handler functions.

### Example System Call Numbers (Linux x86)

| Number | System Call | Description               |
| ------ | ----------- | ------------------------- |
| 1      | exit        | Terminate process         |
| 2      | fork        | Create child process      |
| 3      | read        | Read from file descriptor |
| 4      | write       | Write to file descriptor  |
| 5      | open        | Open a file               |
| 6      | close       | Close a file descriptor   |
| 7      | waitpid     | Wait for process          |
| 11     | execve      | Execute a program         |
| 20     | getpid      | Get process ID            |
| 37     | kill        | Send signal to process    |

## Mode Switch: User Mode vs Kernel Mode

```
+------------------------------------------+
| USER MODE |
| - Limited access to hardware |
| - Cannot execute privileged instructions|
| - Application programs run here |
+------------------------------------------+
 |
 System Call
 (TRAP / INT)
 |
 v
+------------------------------------------+
| KERNEL MODE |
| - Full access to hardware |
| - Can execute all instructions |
| - OS kernel runs here |
| - System call handlers execute here |
+------------------------------------------+
```

The **mode bit** in the CPU determines the current mode:

- Mode bit = 1: User mode
- Mode bit = 0: Kernel mode

A system call triggers a **trap** (software interrupt) that switches the mode bit from 1 to 0, transferring control to the kernel.

## Summary

```
+-----------------------------------------------+
| SYSTEM CALLS - Key Points |
+-----------------------------------------------+
| 1. Interface between user programs and kernel |
| 2. Invoked via TRAP/INT instruction |
| 3. Cause mode switch: User -> Kernel |
| 4. Parameters passed via: |
| - Registers (fastest, limited) |
| - Block/Table in memory |
| - Stack |
| 5. API (POSIX, Win32) wraps system calls |
| 6. System call table maps numbers to handlers |
+-----------------------------------------------+
```

## Exam Tips

1. **System call flow diagram** is a very important question. Practice drawing the complete flow from user program to kernel and back.
2. **Three methods of parameter passing** (registers, block/table, stack) -- know the differences, advantages, and which systems use which method.
3. **API vs System Call:** Understand that programmers use APIs (like POSIX), not direct system calls. The system call interface maps API calls to actual system calls.
4. **Mode switch:** Know that system calls cause a transition from user mode (mode bit = 1) to kernel mode (mode bit = 0) and back.
5. **System call table:** Understand that each system call has a unique number, and the kernel uses a table to dispatch to the correct handler.
6. **Example tracing:** Be prepared to trace a simple system call like `read()` or `open()` through all the steps from API call to kernel execution and return.
7. **Common question:** "Explain how system calls are used to provide the interface between a running program and the OS" or "Explain the three methods of passing parameters to the OS."
8. **POSIX vs Win32 API:** Know at least 2-3 example functions from each API for comparison.
