# System Calls and API

## 1. Introduction: Bridging User and System

An Operating System (OS) is a sophisticated piece of software that manages computer hardware and provides a convenient environment for running application programs. A fundamental design principle of modern operating systems is the concept of **Dual-Mode Operation**.

- **User Mode:** This is the restricted mode in which application programs run. In this mode, the CPU cannot execute privileged instructions (e.g., directly accessing I/O devices or memory management units). This protects the system from errant or malicious programs.
- **Kernel Mode:** This is the privileged mode in which the operating system kernel runs. It has unrestricted access to all hardware and can execute every instruction supported by the CPU.

When a user application needs to request a service from the OS that requires privilege (e.g., reading a file, creating a process, allocating memory), it cannot do so directly. This is where **System Calls** come into play. A system call is the fundamental interface between a user application and the operating system kernel.

## 2. What is a System Call?

A system call is a programmed request to the operating system kernel, made via a well-defined and secure mechanism, to perform a privileged task on behalf of the calling process.

Think of it like this: You are a user (user mode) and you need a document from a secure, restricted company archive (hardware). You cannot enter the archive yourself. Instead, you fill out a formal request form (system call) and hand it to the archivist (kernel). The archivist, who has the key (privilege), enters the archive, retrieves the document, and hands it back to you.

**Key Characteristics:**

- They are the **only** entry points into the kernel.
- They are typically implemented as software interrupts or special instructions (e.g., `syscall`/`sysenter` on x86) that trigger a hardware-assisted switch from user mode to kernel mode.
- Each system call has a unique number identifier.

## 3. The System Call Mechanism: A Step-by-Step Process

The journey of a system call involves a precise sequence of steps to ensure security and control.

```
+----------------+ 1. Call Library +--------------------------+
| User Application | ----------------------> | Standard C Library (API) |
+----------------+ Function (e.g., read()) +--------------------------+
 ^ |
 | 6. Return result | 2. Prepare parameters
 | |
 | V
 | +------------------+
 | | Invokes `int 0x80` |
 | | or `syscall` instr|
 +----------------------------------------+------------------+
 |
 | 3. CPU switches to
 | kernel mode; traps
 V
+----------------+ +------------------+
| User Process | | OS Kernel |
| (User Mode) | <------------------------------ (Kernel Mode) |
+----------------+ 5. Return to user mode +------------------+
 ^ | |
 | | 4. Execute |
 | | system call handler|
 | | (sys_read()) |
 +----------------------------------------+------------------+
```

1. **Invocation:** The application calls a function from a standard library (the API), such as `read()` in C.
2. **Preparation:** The library function prepares the necessary arguments (e.g., file descriptor, buffer address, number of bytes to read) according to the calling convention of the OS.
3. **Trap:** The library function executes a special instruction (e.g., `int 0x80` for interrupt 80hex on Linux, or the `syscall` instruction on modern processors). This causes a **trap** – a software-generated interrupt.
4. **Mode Switch:** The CPU hardware detects the trap, saves the current state of the user process, and switches to kernel mode. It then jumps to a predefined location in memory: the **trap handler**, which is part of the OS.
5. **Execution:** The OS's trap handler examines the request, identifies the specific system call using a number stored in a register (e.g., `eax`), and calls the corresponding **system call handler** (e.g., `sys_read()`) inside the kernel. The kernel now performs the privileged task.
6. **Return:** Once the task is complete, the OS returns the result (success/failure, number of bytes read) to the user process via a register. It then arranges a return from the trap, which switches the CPU back to user mode and resumes the user process just after the trap instruction.

## 4. Categories of System Calls

System calls can be broadly grouped into several categories based on the service they provide.

| Category                    | Purpose                                            | Common Examples                                                   |
| :-------------------------- | :------------------------------------------------- | :---------------------------------------------------------------- |
| **Process Control**         | Create, manage, and terminate processes.           | `fork()`, `exec()`, `exit()`, `wait()`                            |
| **File Management**         | Create, delete, read, write, and manipulate files. | `open()`, `read()`, `write()`, `close()`, `lseek()`               |
| **Device Management**       | Request and release devices, read/write to them.   | `ioctl()`, `read()`, `write()` (on device files)                  |
| **Information Maintenance** | Get/set system data like time, process attributes. | `getpid()`, `gettimeofday()`, `sysinfo()`                         |
| **Communication**           | Establish communication links between processes.   | `pipe()`, `shmget()` (shared memory), `msgget()` (message queues) |
| **Protection**              | Control access to resources (users, permissions).  | `chmod()`, `chown()`, `setuid()`                                  |

## 5. Application Programming Interface (API) vs. System Call

It is crucial to understand the distinction between an API and a system call. They are related but not the same.

- **API (Application Programming Interface):** A set of **function definitions**, protocols, and tools for building software applications. It defines how an application should request services from a library or an OS. For example, the POSIX standard defines an API for UNIX-like systems (`open`, `read`, `write`, `fork`).
- **System Call:** The actual **low-level implementation** of a service request that crosses the user-kernel boundary. It is the mechanism that fulfills the request defined by the API.

**The Relationship:** An API is a contract. A system call is the implementation of that contract. An API function may wrap a single system call, may not use any system calls (e.g., a pure math function like `sin()`), or may use multiple system calls to implement its functionality.

**Example:** The C standard library function `printf()` is part of the API. To actually print text to the screen, `printf()` eventually makes a `write()` system call to the kernel, asking it to send bytes to the standard output (usually the terminal).

## 6. Common Examples

Let's look at some code snippets to illustrate these concepts.

**C Program using `read()` API (which triggers the `sys_read` system call):**

```c
#include <unistd.h> // API header file

int main() {
 char buffer[100];
 int bytes_read;

 // The 'read' function is part of the API.
 // Its implementation WILL invoke the 'sys_read' system call.
 bytes_read = read(0, buffer, sizeof(buffer)); // 0 is stdin file descriptor

 if (bytes_read > 0) {
 write(1, buffer, bytes_read); // 1 is stdout
 }
 return 0;
}
```

**Python Program using the `os` module API:**

```python
import os

# The 'os.getpid()' function is a Python API call.
# Under the hood, it uses the 'getpid' system call.
pid = os.getpid()
print(f"Process ID is: {pid}")
```

## 7. Why Are System Calls Important?

1. **Security and Stability:** They prevent user applications from directly accessing hardware or kernel data structures, which protects the system from crashes and malicious attacks.
2. **Abstraction:** They provide a simple, uniform, and hardware-abstracted interface for applications. A program doesn't need to know the specifics of how to talk to a hard disk; it just uses the `read`/`write` system calls.
3. **Portability:** An application written using standard system calls (e.g., POSIX) can be easily recompiled to run on different hardware, as long as the OS implements the same API.

## 8. Exam Tips

- **Memorize the Core Difference:** API is the interface definition (the "what"), System Call is the implementation mechanism (the "how"). An API function may use one or more system calls.
- **Understand the Trap Mechanism:** Be able to describe the step-by-step process of how a system call transitions from user mode to kernel mode and back. Know what a software interrupt/trap is.
- **Categorization is Key:** Be familiar with the main categories of system calls (Process, File, Device, etc.) and be able to name at least two examples for each.
- **Dual-Mode Operation:** Always link the need for system calls back to the fundamental concept of user mode vs. kernel mode operation. This is the _reason_ system calls exist.
- **Watch for Trick Questions:** A question might ask "How does an application request an OS service?" The correct answer is "via a system call," not "via an API." The API is the wrapper for making that call.
