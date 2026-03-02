# Memory Layout of a C Program

## Introduction

In Unix System Programming, understanding how a C program organizes its memory at runtime is crucial for efficient programming, debugging, and system-level interaction. The memory layout defines how different parts of your program—code, data, stack, and heap—are arranged in the process's virtual address space. This structure is fundamental to the environment of a UNIX process, as covered in Module-3.

## The Typical Memory Layout

A running C program's memory is typically divided into several segments. Each segment serves a specific purpose and has distinct characteristics regarding read/write/execute permissions, lifetime, and storage content.

A high-level ASCII diagram of the memory layout is as follows:

```
High Addresses +----------------------+
                |   Command Line Args   | \
                |    and Environment    |  |-> Kernel Space (often)
                +----------------------+ /
                |         Stack         |  | Grows downwards
                |          |            |
                |          v            |
                |                      |
                |          ^            |
                |          |            |
                |         Heap          |  | Grows upwards
                +----------------------+
                |     Uninitialized     |
                |       Data (BSS)      |
                +----------------------+
                |    Initialized Data   |
                +----------------------+
                |       Text/Code       |
Low Addresses  +----------------------+
```

**Note:** The division between user space and kernel space varies by system architecture. The stack and heap grow towards each other.

## Detailed Segment Breakdown

### 1. Text Segment (Code Segment)

The text segment is a read-only area that contains the executable instructions of your program. This includes the machine code compiled from your C functions.

- **Characteristics:**
  - **Read-Only:** Prevents a program from accidentally modifying its own instructions.
  - **Shared:** Multiple instances of the same program (e.g., multiple users running `ls`) can share a single, physical copy of this segment in memory, saving significant RAM.
  - **Fixed Size:** Its size is determined at compile time and does not change during execution.

### 2. Initialized Data Segment (Data Segment)

This segment contains global and static variables that have a predefined value assigned in the source code.

- **Example:**
  ```c
  int global_var = 100;        // Stored in initialized data
  static int static_var = 50;  // Stored in initialized data
  char hello[] = "Hello World"; // The string literal "Hello World" might be in text/rodata, but the array `hello` is in initialized data.
  ```

### 3. Uninitialized Data Segment (BSS - Block Started by Symbol)

The BSS segment holds global and static variables that are either explicitly uninitialized or initialized to zero. A key feature is that the operating system initializes this entire block to zero before the program starts executing.

- **Why it exists:** It's an optimization. Instead of storing a long list of zeros in the executable file on disk, the executable only needs to record the _size_ of the BSS segment. The OS allocates and zeroes out the memory at load time.
- **Example:**
  ```c
  int global_uninit;     // Stored in BSS (will be 0)
  static int static_uninit; // Stored in BSS (will be 0)
  int global_zero = 0;   // Typically also stored in BSS
  ```

**Comparison Table: Data and BSS Segments**

| Feature          | Initialized Data Segment               | Uninitialized Data Segment (BSS)                  |
| ---------------- | -------------------------------------- | ------------------------------------------------- |
| **Content**      | Explicitly initialized globals/statics | Zero-initialized or uninitialized globals/statics |
| **Disk Storage** | Occupies space in the executable file  | Only size is stored in the executable             |
| **Runtime Init** | Loaded from disk                       | Set to zero by the OS/loader                      |
| **Example**      | `int x = 5;`                           | `int y;` or `int z = 0;`                          |

### 4. Heap Segment

The heap is a pool of memory used for **dynamic memory allocation** during program execution. It is not managed automatically; the programmer must explicitly request memory (`malloc`, `calloc`, `realloc`) and release it (`free`).

- **Characteristics:**
  - **Grows Upwards:** As memory is allocated, the heap grows towards higher addresses.
  - **Variable Size:** Its size can change during runtime.
  - **Manual Management:** The programmer is responsible for managing (allocating and freeing) heap memory. Failure to free memory leads to **memory leaks**.
  - **Fragmentation:** Repeated allocation and deallocation can fragment the heap.

- **Example:**
  ```c
  int *ptr = (int *)malloc(10 * sizeof(int)); // Allocates memory on the heap
  if (ptr != NULL) {
      // Use the memory
      free(ptr); // Must free to avoid a leak
  }
  ```

### 5. Stack Segment

The stack is used for storing **automatic variables** (local variables), function parameters, return addresses, and context information during function calls. It operates in a Last-In-First-Out (LIFO) manner.

- **Characteristics:**
  - **Grows Downwards:** It grows towards lower memory addresses.
  - **Automatic Management:** Memory for local variables is automatically allocated when a function is called and freed when the function returns.
  - **Fast:** Allocation and deallocation are simple pointer operations.
  - **Limited Size:** The stack size is often fixed per thread and can be small (e.g., 8MB on some systems). Exceeding this limit causes a **stack overflow**.

- **How it works:** When a function is called:
  1.  Arguments are pushed onto the stack.
  2.  The return address is pushed.
  3.  A new **stack frame** is created, which includes space for the function's local variables.
      When the function returns, its stack frame is popped, and the stack pointer is reset.

- **Example:**
  ```c
  void func(int param) { // 'param' is on the stack
      int local_var = 10; // 'local_var' is on the stack
      // ...
  } // 'local_var' and 'param' are automatically deallocated here
  ```

**Comparison Table: Heap vs. Stack**

| Feature                 | Heap                            | Stack                               |
| ----------------------- | ------------------------------- | ----------------------------------- |
| **Management**          | Manual (`malloc`, `free`)       | Automatic (on function call/return) |
| **Size**                | Large, limited by system        | Smaller, fixed size per thread      |
| **Allocation Speed**    | Slower (complex management)     | Very Fast (pointer movement)        |
| **Lifetime**            | Persists until explicitly freed | Limited to function scope           |
| **Usage**               | Dynamic data, large structures  | Local variables, function calls     |
| **Direction of Growth** | Grows upwards                   | Grows downwards                     |

### 6. Command-Line Arguments and Environment

This area, typically located at the highest memory addresses of the user space, stores the arguments passed to the program (`argv`) and the environment variable list (`envp`).

- **Access:** These are accessible via the parameters to `main()`: `int main(int argc, char *argv[], char *envp[])`.

## Putting It All Together: A Complete Example

```c
#include <stdio.h>
#include <stdlib.h>

int global_init = 10;    // Initialized Data Segment
int global_uninit;       // BSS Segment (initialized to 0)

void function(int param) { // Code/Text Segment
    int local_var = 5;   // Stack (local variable)
    static int static_local = 0; // Initialized Data (static variable, retained between calls)
    char *heap_mem = (char *)malloc(20); // Heap (allocated memory)

    printf("Param (Stack): %d\n", param);
    printf("Local (Stack): %d\n", local_var);
    printf("Static (Data): %d\n", static_local);
    printf("Heap Mem Address: %p\n", (void*)heap_mem);

    static_local++;
    free(heap_mem);      // Must free heap memory
}

int main(int argc, char *argv[]) { // Code/Text Segment
    // argc, argv, envp are on the stack (or just above it)
    printf("Command: %s\n", argv[0]);

    function(100); // Function call creates a stack frame
    function(200);

    return 0;
}
```

## Exam Tips

1.  **Know the Order:** Be able to draw the memory layout from low to high addresses (Text -> Data -> BSS -> Heap -> Stack) and explain each segment.
2.  **Heap vs. Stack:** Expect questions that test your understanding of the differences between heap and stack allocation, including lifetime, size, speed, and management.
3.  **Static Variables:** Remember that `static` variables inside functions are _not_ stored on the stack; they reside in the Data segment (initialized or BSS) and persist for the program's lifetime.
4.  **BSS Optimization:** Understand _why_ the BSS segment exists (to save disk space by not storing zeros).
5.  **Addresses:** You might be asked to predict the approximate memory address ranges of variables (e.g., global variables will have lower addresses than heap-allocated pointers, which will have lower addresses than local variables).
6.  **Common Errors:** Link common errors like segmentation faults, memory leaks, and stack overflows to their respective memory segments.
