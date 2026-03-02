# System Programs and OS Structure

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction to System Programs](#1-introduction-to-system-programs)
2. [Operating System Structures](#2-operating-system-structures)
3. [Memory Management Programs](#3-memory-management-programs)
4. [Language Translators](#4-language-translators)
5. [System Calls](#5-system-calls)
6. [Boot Process](#6-boot-process)
7. [Key Takeaways](#7-key-takeaways)
8. [Multiple Choice Questions (MCQs)](#8-multiple-choice-questions-mcqs)
9. [Flashcards for Quick Revision](#9-flashcards-for-quick-revision)

---

## 1. Introduction to System Programs

### 1.1 What Are System Programs?

System programs (also known as system software) are essential software components that provide a platform for running application software. They act as an intermediary between the computer hardware and the user/application programs. Unlike application software that performs specific user tasks, system programs manage and control the computer hardware and provide services to other software.

### 1.2 Real-World Relevance

System programs are the backbone of every computing device we use daily:

- **Smartphones**: Android and iOS rely on system programs to manage memory, processes, and hardware access
- **Banking Systems**: ATM machines use system programs to process transactions securely
- **Enterprise Servers**: Data centers run on operating systems that manage thousands of concurrent processes
- **Embedded Systems**: Washing machines, microwaves, and car control units all contain system programs

For Delhi University students, understanding system programs is crucial because they form the foundation for advanced topics like operating system design, compiler construction, and system programming.

### 1.3 Categories of System Programs

| Category | Examples | Purpose |
|----------|----------|---------|
| Language Translators | Assembler, Compiler, Interpreter | Convert source code to machine code |
| System Management | Task Manager, Disk Defragmenter | Monitor and optimize system performance |
| Device Drivers | Printer drivers, Graphics drivers | Enable hardware communication |
| Utility Programs | Antivirus, File compressors | Provide additional functionality |
| Boot Program | BIOS, UEFI | Initialize hardware on startup |

---

## 2. Operating System Structures

The internal organization of an operating system defines how its components interact and are arranged. Different OS structures offer various trade-offs between performance, complexity, and maintainability.

### 2.1 Monolithic Structure

In a monolithic kernel architecture, the entire operating system runs in a single address space (kernel space). All core services—process management, memory management, file systems, and device drivers—are tightly integrated.

**Characteristics:**
- Single large executable file
- All components share the same address space
- High performance due to minimal context switching
- Difficult to maintain and debug
- If one component fails, the entire system may crash

**Example: Traditional UNIX**

```c
// Simplified representation of monolithic kernel structure
struct kernel_data {
    process_table_t process_table;
    memory_manager_t memory_manager;
    file_system_t file_system;
    device_drivers_t device_drivers;
} kernel;

// All services run in kernel mode
void system_call(int call_number, void* params) {
    switch(call_number) {
        case READ: file_system.read(params); break;
        case WRITE: file_system.write(params); break;
        case FORK: process_table.fork(params); break;
        // All kernel services accessible directly
    }
}
```

**Real-World Examples**: Traditional UNIX (BSD, System V), Linux (monolithic with loadable modules), MS-DOS

### 2.2 Microkernel Architecture

Microkernel design philosophy advocates for minimal functionality in kernel mode—only essential services like inter-process communication (IPC), basic scheduling, and memory management reside in the kernel. Other services (file systems, device drivers, networking) run as user-space processes called servers.

**Characteristics:**
- Minimal kernel (~10,000 lines of code)
- High modularity and extensibility
- Better fault isolation (failure in one server doesn't crash the system)
- Higher communication overhead due to message passing
- More secure design

**Example: MINIX 3 Architecture**

```
┌─────────────────────────────────────────────┐
│              User Space                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│  │ File     │ │ Network  │ │ Process  │    │
│  │ Server   │ │ Server   │ │ Server   │    │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘    │
└───────┼────────────┼────────────┼──────────┘
        │            │            │
        └────────────┴────────────┘
                   │ IPC
        ┌──────────┴──────────┐
        │     Microkernel     │
        │  (IPC, Scheduling,  │
        │   Basic Memory Mgmt)│
        └─────────────────────┘
        ┌─────────────────────┐
        │    Hardware         │
        └─────────────────────┘
```

**Real-World Examples**: MINIX 3, QNX, GNU Hurd, L4Linux

### 2.3 Layered Structure

The layered approach organizes the OS into distinct hierarchical layers, where each layer provides services to the layer above it. The lowest layer interacts with hardware, while the highest layer interfaces with users.

**Layers (Bottom to Top):**
1. **Hardware**: Physical components (CPU, memory, I/O devices)
2. **Instruction Set Architecture (ISA)**: Interface between hardware and software
3. **System Programs**: Language translators, utility programs
4. **Operating System Kernel**: Process management, memory management
5. **Operating System Services**: File system, device management
6. **User Interface**: Command-line shell, GUI
7. **Application Programs**: User software

**Example: Traditional OS/2 Layered Design**

```python
# Conceptual representation of layered system
class Hardware:
    def read_byte(self, address): pass
    def write_byte(self, address, data): pass

class InstructionSetArchitecture(Hardware):
    def execute_instruction(self, opcode, operands): pass

class SystemPrograms:
    def compile(self, source_code): pass
    def assemble(self, assembly_code): pass

class Kernel(SystemPrograms):
    def create_process(self): pass
    def allocate_memory(self, size): pass
    def handle_interrupt(self): pass

class OSService(Kernel):
    def read_file(self, filename): pass
    def write_file(self, filename, data): pass

class UserInterface(OSService):
    def display_prompt(self): pass
    def get_input(self): pass
```

**Real-World Examples**: Windows NT (hybrid), traditional OS/2, MULTICS

### 2.4 Hybrid Structure

Modern operating systems often combine elements from multiple architectural approaches to leverage their strengths while mitigating weaknesses.

**Characteristics:**
- Combines performance of monolithic kernels
- Incorporates modularity of microkernels
- Uses loadable kernel modules (LKMs)
- Most common design in contemporary systems

**Example: Linux with Loadable Modules**

```c
// Example of a loadable kernel module in Linux
#include <linux/module.h>
#include <linux/kernel.h>

// Module initialization
int init_module(void) {
    printk(KERN_INFO "Hello Kernel World!\n");
    return 0;
}

// Module cleanup
void cleanup_module(void) {
    printk(KERN_INFO "Goodbye Kernel World!\n");
}

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Student");
MODULE_DESCRIPTION("Simple Hello World Module");
```

The Linux kernel is monolithic but supports dynamic loading/unloading of modules, effectively providing hybrid benefits.

**Real-World Examples**: Linux, macOS (XNU hybrid), Windows (hybrid kernel)

### 2.5 Comparison of OS Structures

| Aspect | Monolithic | Microkernel | Layered | Hybrid |
|--------|------------|-------------|---------|--------|
| Performance | Highest | Lower | Moderate | High |
| Size | Large | Small | Medium | Flexible |
| Maintainability | Difficult | Easy | Moderate | Easy |
| Reliability | Low | High | Moderate | High |
| Extensibility | Limited | High | Moderate | High |
| Examples | Traditional UNIX | MINIX, QNX | OS/2, MULTICS | Linux, Windows |

---

## 3. Memory Management Programs

Memory management is a critical function of system programs that handles allocation and deallocation of memory to processes.

### 3.1 Key Memory Management Programs

#### 3.1.1 Memory Allocator

Manages dynamic memory allocation in user programs.

```c
// Example of memory allocation system call usage
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Dynamic memory allocation using malloc
    int *numbers = (int*)malloc(10 * sizeof(int));
    
    if (numbers == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }
    
    // Using allocated memory
    for (int i = 0; i < 10; i++) {
        numbers[i] = i * 10;
    }
    
    // Freeing allocated memory
    free(numbers);
    
    return 0;
}
```

#### 3.1.2 Virtual Memory Manager

Implements paging and swapping to extend available memory using disk space.

**Key Functions:**
- Page table management
- Translation Lookaside Buffer (TLB) management
- Page replacement algorithms (LRU, FIFO, Optimal)
- Swap space management

#### 3.1.3 Memory Pools and Garbage Collectors

Memory pools pre-allocate fixed-size memory blocks, while garbage collectors automatically reclaim unused memory in managed languages.

```python
# Example: Simple memory pool implementation
class MemoryPool:
    def __init__(self, block_size, num_blocks):
        self.block_size = block_size
        self.free_blocks = []
        
        # Pre-allocate blocks
        for _ in range(num_blocks):
            self.free_blocks.append(bytearray(block_size))
    
    def allocate(self):
        if not self.free_blocks:
            raise MemoryError("Pool exhausted")
        return self.free_blocks.pop()
    
    def deallocate(self, block):
        self.free_blocks.append(block)
```

---

## 4. Language Translators

Language translators convert source code written in high-level or assembly languages into machine code that can be executed by the computer.

### 4.1 Assembler

Translates assembly language (low-level, mnemonic-based) into machine code.

**Types of Assemblers:**
- **One-pass Assembler**: Processes the entire program in a single pass
- **Two-pass Assembler**: First pass generates symbol table, second pass generates machine code

**Example: Assembly to Machine Code Translation**

```assembly
; Assembly source code
SECTION .data
    msg db 'Hello, World!', 0

SECTION .text
    global _start

_start:
    ; sys_write system call (syscall number 1)
    mov rax, 1        ; syscall number for write
    mov rdi, 1        ; file descriptor 1 (stdout)
    mov rsi, msg      ; pointer to message
    mov rdx, 13       ; message length
    syscall           ; invoke kernel
    
    ; sys_exit system call
    mov rax, 60       ; syscall number for exit
    xor rdi, rdi      ; exit code 0
    syscall           ; invoke kernel
```

**Equivalent Machine Code (64-bit Linux x86-64):**
```
b8 01 00 00 00    mov eax, 1
bf 01 00 00 00    mov edi, 1
48 be [msg]       mov rsi, msg
ba 0d 00 00 00    mov edx, 13
0f 05             syscall
b8 3c 00 00 00    mov eax, 60
31 ff             xor edi, edi
0f 05             syscall
```

### 4.2 Compiler

Translates entire source code into machine code or intermediate code (bytecode) before execution. Produces an executable file.

**Compilation Process:**

```
Source Code (high-level language)
        │
        ▼
┌───────────────────┐
│ 1. Lexical        │ → Tokenizes input
│    Analysis       │
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 2. Syntax         │ → Checks grammar
│    Analysis       │
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 3. Semantic       │ → Checks meaning
│    Analysis       │
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 4. Intermediate  │ → Generates IR
│    Code Gen       │
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 5. Optimization  │ → Improves code
│                   │
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 6. Code           │ → Generates
│    Generation     │   machine code
└────────┬──────────┘
         ▼
   Object Code / Executable
```

**Example: C Program Compilation**

```c
// hello.c
#include <stdio.h>

int main() {
    printf("Hello, Delhi University!\n");
    return 0;
}
```

Commands to compile and run:
```bash
# Preprocessing
gcc -E hello.c -o hello.i

# Compilation to assembly
gcc -S hello.c -o hello.s

# Assembly to object file
gcc -c hello.c -o hello.o

# Linking to create executable
gcc hello.o -o hello

# Execute
./hello
```

### 4.3 Interpreter

Translates and executes source code line-by-line at runtime. No separate executable is created.

**Example: Python Interpreter Execution**

```python
# Interprets line by line at runtime
def greet(university):
    message = f"Welcome to {university}!"
    print(message)

greet("Delhi University")
```

**Key Differences:**

| Feature | Assembler | Compiler | Interpreter |
|---------|-----------|----------|-------------|
| Input | Assembly | High-level | High-level |
| Output | Machine Code | Executable | No executable |
| Speed | Fastest | Fast | Slow |
| Debugging | Difficult | Moderate | Easy |
| Memory | Low | Moderate | High |
| Examples | NASM, MASM | GCC, Clang | Python, Ruby |

### 4.4 Hybrid Approaches

#### 4.4.1 Java Compilation Model

```java
// Java source code compiled to bytecode
// Then interpreted by JVM or JIT compiled

// Source: Hello.java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, DU!");
    }
}
```

**Process:**
```
Hello.java → [Java Compiler] → Hello.class (Bytecode)
                                            │
                                            ▼
                                    [JVM Interpreter/JIT]
                                            │
                                            ▼
                                    Machine Code Execution
```

#### 4.4.2 Just-In-Time (JIT) Compilation

Modern interpreters use JIT compilation to improve performance by compiling frequently executed code to native machine code at runtime.

---

## 5. System Calls

System calls provide the interface between user programs and the operating system kernel. They allow user processes to request services from the OS.

### 5.1 Categories of System Calls

| Category | Examples | Purpose |
|----------|----------|---------|
| Process Control | fork(), exec(), exit() | Create, manage processes |
| File Management | open(), read(), write(), close() | File operations |
| Device Management | ioctl(), read(), write() | Device communication |
| Information Maintenance | getpid(), getuid(), uname() | Query system info |
| Communication | pipe(), socket(), send(), recv() | Inter-process communication |
| Protection | chmod(), chown(), setuid() | Access control |

### 5.2 System Call Implementation in Linux

**Example: Creating a Process with fork()**

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork();  // System call to create new process
    
    if (pid < 0) {
        // Fork failed
        fprintf(stderr, "Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Child Process: PID = %d, Parent PID = %d\n", 
               getpid(), getppid());
        execlp("/bin/ls", "ls", "-l", NULL);  // Replace with new program
    }
    else {
        // Parent process
        printf("Parent Process: PID = %d, Child PID = %d\n", 
               getpid(), pid);
        wait(NULL);  // Wait for child to complete
        printf("Child completed\n");
    }
    
    return 0;
}
```

**System Call Flow:**
```
User Program
    │
    ▼
Library Function (fork wrapper)
    │
    ▼
System Call Interface (software interrupt / syscall)
    │
    ▼
Kernel Mode (switch from user to kernel)
    │
    ▼
System Call Handler
    │
    ▼
Corresponding Kernel Service
    │
    ▼
Return to User Mode
```

### 5.3 Common System Calls with Examples

#### 5.3.1 File Operations

```c
#include <fcntl.h>
#include <unistd.h>

int main() {
    // Open file (system call)
    int fd = open("sample.txt", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    
    // Read from file (system call)
    char buffer[100];
    ssize_t bytes_read = read(fd, buffer, 100);
    
    // Write to file (system call)
    const char *msg = "Hello via system call!\n";
    write(STDOUT_FILENO, msg, 25);
    
    // Close file (system call)
    close(fd);
    
    return 0;
}
```

#### 5.3.2 Memory Allocation

```c
#include <sys/mman.h>

int main() {
    // Allocate memory using mmap (system call)
    void *mapped_mem = mmap(NULL,           // Let kernel choose address
                            4096,           // Size of mapping
                            PROT_READ | PROT_WRITE,  // Read/write permissions
                            MAP_PRIVATE | MAP_ANONYMOUS,  // Anonymous mapping
                            -1,             // No file descriptor
                            0);             // No offset
    
    if (mapped_mem == MAP_FAILED) {
        perror("mmap");
        return 1;
    }
    
    // Use the memory
    sprintf(mapped_mem, "Allocated via mmap");
    
    // Release memory
    munmap(mapped_mem, 4096);
    
    return 0;
}
```

---

## 6. Boot Process

The boot process initializes the computer system from a powered-off state to a fully operational state where the operating system takes over.

### 6.1 Boot Sequence Overview

```
Power On
    │
    ▼
┌────────────────────┐
│ 1. Power-On Self  │ → POST (Power-On Self Test)
│    Test (POST)    │ → Check CPU, memory, basic hardware
└────────┬───────────┘
         ▼
┌────────────────────┐
│ 2. BIOS/UEFI      │ → Initialize critical hardware
│    Initialization │ → Load boot loader from MBR/UEFI
└────────┬───────────┘
         ▼
┌────────────────────┐
│ 3. Boot Loader    │ → GRUB, Windows Boot Manager
│    (Stage 1/2)    │ → Select operating system
└────────┬───────────┘
         ▼
┌────────────────────┐
│ 4. Kernel Loading  │ → Load OS kernel into memory
│                    │ → Initialize kernel structures
└────────┬───────────┘
         ▼
┌────────────────────┐
│ 5. Kernel Startup  │ → Start essential processes
│    (init/systemd)  │ → Mount file systems
└────────┬───────────┘
         ▼
┌────────────────────┐
│ 6. User Space     │ → Start GUI/Display Manager
│    Initialization │ → Login screen appears
└────────────────────┘
         ▼
    Full System Ready
```

### 6.2 Detailed Boot Process Stages

#### Stage 1: Power-On Self Test (POST)

- BIOS/UEFI performs hardware diagnostics
- Checks CPU, RAM, keyboard, basic video
- If errors found, beep codes or error messages displayed

#### Stage 2: BIOS/UEFI Initialization

```
BIOS Functions:
├── Initialize CPU registers
├── Set up interrupt descriptor table
├── Initialize memory controller
├── Detect and configure hardware (Plug and Play)
├── Load boot device from CMOS settings
└── Read first sector (512 bytes) from boot device
```

#### Stage 3: Boot Loader

**MBR (Master Boot Record) Layout:**
```
Offset 0-445:     Boot code (446 bytes)
Offset 446-509:   Partition table (64 bytes)
Offset 510-511:   Magic number (0x55AA)
```

**Example: GRUB Boot Loader**
```
GRUB Stage 1 (boot.img)
    │
    ▼
GRUB Stage 1.5 (core.img) - Loads filesystem drivers
    │
    ▼
GRUB Stage 2 (/boot/grub/) - Shows menu, loads kernel
    │
    ▼
Selected Kernel (vmlinuz) loaded into memory
```

#### Stage 4: Kernel Loading

```bash
# Example: Kernel boot parameters
# In GRUB menu, press 'e' to edit
linux /boot/vmlinuz-5.15.0-generic root=/dev/sda1 ro quiet splash
initrd /boot/initrd.img-5.15.0-generic
```

**Kernel Initialization Steps:**
1. Decompress kernel (if compressed)
2. Setup page tables
3. Enable memory paging
4. Initialize interrupt controllers
5. Detect and enumerate devices
6. Mount root filesystem

#### Stage 5: Init Process (systemd in modern Linux)

```c
// Simplified init process flow (systemd target units)
// /sbin/init or /lib/systemd/systemd

int main(int argc, char *argv[]) {
    // Load kernel modules
    load_kernel_modules();
    
    // Mount essential filesystems
    mount_filesystems();  // /proc, /sys, /dev
    
    // Start essential services
    start_systemd_units();  // graphical.target, multi-user.target
    
    // Transition to default target
    switch_root();
    exec("/sbin/init");  // Start systemd proper
}
```

#### Stage 6: User Space Initialization

```
Systemd Services Started:
├── Basic system services (logging, D-Bus)
├── Device enumeration (udev)
├── Network configuration
├── Display manager (gdm, lightdm)
└── Login prompt / Desktop environment
```

---

## 7. Key Takeaways

1. **System Programs** are foundational software that manage hardware and provide services to application programs. They include language translators, system management tools, and utility programs.

2. **OS Structures** determine the internal organization of operating systems:
   - **Monolithic**: High performance, single address space (e.g., traditional UNIX, Linux)
   - **Microkernel**: Minimal kernel, high modularity, better fault isolation (e.g., MINIX, QNX)
   - **Layered**: Hierarchical organization with clear abstractions
   - **Hybrid**: Combines advantages of multiple approaches (e.g., Linux with modules, Windows)

3. **Language Translators** convert source code to executable forms:
   - Assemblers convert assembly to machine code
   - Compilers translate entire programs before execution
   - Interpreters execute line-by-line at runtime

4. **System Calls** are the primary interface between user programs and OS kernel, enabling process control, file management, device communication, and information retrieval.

5. **Boot Process** involves multiple stages from power-on through BIOS/UEFI, boot loader, kernel loading, to user space initialization.

---

## 8. Multiple Choice Questions (MCQs)

### Unit 1: Introduction to System Programs

**Q1. Which of the following is NOT a system program?**
- a) Compiler
- b) Text Editor
- c) Device Driver
- d) Assembler

**Q2. System programs run primarily in:**
- a) User mode only
- b) Kernel mode only
- c) Both user and kernel mode
- d) Neither mode

**Q3. The main purpose of system programs is to:**
- a) Perform specific user tasks
- b) Provide a platform for running application software
- c) Replace hardware components
- d) Connect computers to the internet

### Unit 2: OS Structures

**Q4. In a monolithic kernel architecture:**
- a) All components run in user space
- b) All components share the same address space in kernel mode
- c) Components communicate via message passing
- d) The kernel size is minimal

**Q5. Which OS architecture provides the highest fault isolation?**
- a) Monolithic
- b) Layered
- c) Microkernel
- d) Hybrid

**Q6. Linux kernel is primarily:**
- a) Microkernel
- b) Layered
- c) Monolithic with loadable modules
- d) Pure monolithic

**Q7. Loadable Kernel Modules (LKMs) are primarily associated with:**
- a) Microkernel architecture
- b) Monolithic architecture
- c) Layered architecture
- d) Both B and hybrid systems

**Q8. MINIX 3 is an example of:**
- a) Monolithic kernel
- b) Microkernel
- c) Hybrid kernel
- d) Exokernel

**Q9. The layered approach to OS design ensures:**
- a) Highest performance
- b) Complete isolation of hardware
- c) Each layer uses services from lower layers only
- d) No inter-process communication needed

**Q10. Windows NT architecture is best described as:**
- a) Pure monolithic
- b) Pure microkernel
- c) Hybrid
- d) Layered with fixed hierarchy

### Unit 3: Memory Management Programs

**Q11. Which component manages dynamic memory allocation in C programs?**
- a) Hardware MMU
- b) Memory allocator in standard library
- c) BIOS
- d) Boot loader

**Q12. Virtual memory extends physical memory by using:**
- a) CPU registers
- b) Hard disk space
- c) ROM
- d) Cache memory

**Q13. A memory pool pre-allocates:**
- a) Variable-sized blocks
- b) Fixed-sized blocks
- c) No blocks until requested
- d) Only kernel memory

**Q14. Garbage collection is primarily associated with:**
- a) C programming
- b) Assembly language
- c) Managed languages like Java and Python
- d) System programming

**Q15. The component that translates virtual addresses to physical addresses is:**
- a) CPU
- b) TLB (Translation Lookaside Buffer)
- c) Hard disk
- d) BIOS

### Unit 4: Language Translators

**Q16. An assembler translates:**
- a) High-level language to machine code
- b) Assembly language to machine code
- c) Bytecode to machine code
- d) Source code to object code

**Q17. Which translator produces an executable file?**
- a) Assembler
- b) Compiler
- c) Interpreter
- d) Both a and b

**Q18. Java uses which approach for execution?**
- a) Pure interpretation
- b) Pure ahead-of-time compilation
- c) Compilation to bytecode with JIT interpretation
- d) Direct machine code generation

**Q19. The process of converting source code to tokens is called:**
- a) Parsing
- b) Semantic analysis
- c) Lexical analysis
- d) Code generation

**Q20. Which produces the fastest execution?**
- a) Interpreter
- b) Just-in-time compiler
- c) Ahead-of-time compiler
- d) Assembler

### Unit 5: System Calls

**Q21. System calls operate in:**
- a) User mode
- b) Kernel mode
- c) Either mode depending on the call
- d) Supervisory mode

**Q22. The fork() system call is used to:**
- a) Terminate a process
- b) Create a new process
- c) Replace process image
- d) Wait for a process

**Q23. Which system call is used to read from a file?**
- a) open()
- b) read()
- c) close()
- d) write()

**Q24. To change file permissions, the appropriate system call is:**
- a) chmod()
- b) chown()
- c) umask()
- d) Both a and b

**Q25. The system call used to allocate memory dynamically in Linux is:**
- a) malloc()
- b) alloc()
- c) mmap()
- d) Both a and c

### Unit 6: Boot Process

**Q26. POST stands for:**
- a) Power On System Test
- b) Power-On Self Test
- c) Primary Operating System Test
- d) Program Output System Test

**Q27. The MBR (Master Boot Record) is located in:**
- a) BIOS chip
- b) First sector of hard disk
- c) Kernel partition
- d) RAM

**Q28. Which program loads the operating system kernel?**
- a) BIOS/UEFI
- b) Boot loader
- c) Device driver
- d) Init process

**Q29. The first process started by the Linux kernel is:**
- a) bash
- b) systemd or init
- c) login
- d) kernel

**Q30. GRUB is primarily a:**
- a) Text editor
- b) Boot loader
- c) Kernel
- d) Device driver

---

## 9. Flashcards for Quick Revision

### Flashcard Set 1: OS Structures

| # | Term | Definition |
|---|------|------------|
| 1 | Monolithic Kernel | OS architecture where entire kernel runs in single address space; high performance but poor fault isolation |
| 2 | Microkernel | Minimal kernel design with only essential services; other services run as user-space servers |
| 3 | Loadable Kernel Module (LKM) | Code that can be loaded into kernel at runtime to extend functionality (e.g., Linux drivers) |
| 4 | Hybrid Kernel | Combines monolithic and microkernel approaches; used by modern OS like Linux and Windows |
| 5 | Layered OS | Architecture where OS is organized in hierarchical layers, each using services of lower layers |

### Flashcard Set 2: Language Translators

| # | Term | Definition |
|---|------|------------|
| 1 | Assembler | Translates assembly language instructions to machine code |
| 2 | Compiler | Translates entire high-level source code to machine code/executable before execution |
| 3 | Interpreter | Executes source code line-by-line at runtime without producing separate executable |
| 4 | Lexical Analysis | First phase of compilation that tokenizes input source code |
| 5 | JIT Compilation | Just-In-Time compilation that translates bytecode to machine code at runtime for performance |

### Flashcard Set 3: System Calls

| # | Term | Definition |
|---|------|------------|
| 1 | fork() | Creates a new process by duplicating the calling process |
| 2 | exec() | Replaces the current process image with a new program |
| 3 | open() | Opens a file and returns a file descriptor |
| 4 | read() | Reads data from a file descriptor into a buffer |
| 5 | write() | Writes data from a buffer to a file descriptor |
| 6 | mmap() | Maps a file or device into memory or creates anonymous memory mapping |
| 7 | exit() | Terminates the calling process with specified exit status |

### Flashcard Set 4: Boot Process

| # | Term | Definition |
|---|------|------------|
| 1 | POST | Power-On Self Test; BIOS/UEFI performs hardware diagnostics at power-on |
| 2 | BIOS | Basic Input/Output System; firmware that initializes hardware and loads boot loader |
| 3 | MBR | Master Boot Record; 512-byte sector containing boot code and partition table |
| 4 | Boot Loader | Program that loads OS kernel into memory (e.g., GRUB, Windows Boot Manager) |
| 5 | Init | First user-space process that starts all other processes and services |

### Flashcard Set 5: Memory Management

| # | Term | Definition |
|---|------|------------|
| 1 | Virtual Memory | Memory management technique that uses disk to extend available RAM |
| 2 | MMU | Memory Management Unit; hardware that translates virtual to physical addresses |
| 3 | Page Table | Data structure that maps virtual pages to physical frames |
| 4 | TLB | Translation Lookaside Buffer; hardware cache for recent virtual-to-physical translations |
| 5 | Swapping | Moving entire processes between RAM and disk to free memory space |

### Answers to MCQs

| Q# | Answer | Q# | Answer | Q# | Answer |
|----|--------|----|--------|----|--------|
| 1 | b | 11 | b | 21 | b |
| 2 | c | 12 | b | 22 | b |
| 3 | b | 13 | b | 23 | b |
| 4 | b | 14 | c | 24 | d |
| 5 | c | 15 | b | 25 | d |
| 6 | c | 16 | b | 26 | b |
| 7 | d | 17 | d | 27 | b |
| 8 | b | 18 | c | 28 | b |
| 9 | c | 19 | c | 29 | b |
| 10 | c | 20 | d | 30 | b |

---

*Study material prepared according to Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus. For detailed coverage, refer to "Operating System Concepts" by Silberschatz, Galvin, and Gagne, and "Modern Operating Systems" by Andrew S. Tanenbaum.*