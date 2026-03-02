# Overflow Attacks and Countermeasures

## Introduction

Buffer overflow attacks represent one of the most notorious and historically significant classes of vulnerabilities in computer security. These attacks have been responsible for some of the most devastating security incidents in computing history, including the Morris Worm of 1988, which affected approximately 6,000 computers (about 10% of the Internet at that time). Understanding buffer overflows is essential for any computer science student because they fundamentally expose the relationship between high-level programming languages and low-level memory management.

In modern software development, particularly with languages like C and C++ that provide direct memory access, buffer overflows occur when a program writes data beyond the boundaries of allocated memory. This seemingly simple programming error can be exploited by malicious actors to inject and execute arbitrary code, escalate privileges, or cause denial of service. Despite decades of research and development of countermeasures, buffer overflow vulnerabilities continue to be discovered in critical software systems, making this topic perpetually relevant for security professionals and software developers alike.

This module examines the mechanics of various overflow attacks, their exploitation techniques, and the comprehensive countermeasures employed in modern computing environments. Given that many operating systems and embedded systems are written in C/C++, understanding these vulnerabilities is crucial for developing secure software and conducting effective security assessments.

## Key Concepts

### Understanding Memory Layout

To comprehend buffer overflow attacks, one must first understand how process memory is organized in typical computing systems. A process's memory is divided into several segments:

1. **Text Segment**: Contains the program's executable code and is typically read-only
2. **Data Segment**: Stores initialized and uninitialized global variables
3. **Heap Segment**: Dynamically allocated memory during program execution, grows upward
4. **Stack Segment**: Function call frames, local variables, return addresses, grows downward
5. **Environment Variables**: System variables used by the program

The stack is particularly important for understanding buffer overflows because it stores function parameters, return addresses, saved registers, and local variables including buffers. When a function is called, a stack frame (also called activation record) is pushed onto the stack, and when the function returns, this frame is popped.

### Stack-Based Buffer Overflow

A stack-based buffer overflow occurs when a function copies data into a local buffer without proper bounds checking, allowing data to overflow the buffer and overwrite adjacent memory locations. Consider the following vulnerable C function:

```c
void vulnerable_function(char *str) {
    char buffer[64];
    strcpy(buffer, str);  // No bounds checking!
}
```

When this function is called, memory is allocated on the stack as follows (from higher to lower addresses):
- Return address (saved EIP/RIP)
- Saved base pointer (saved EBP/RBP)
- Local buffer[64]
- Other local variables

If the input string `str` is longer than 64 characters, `strcpy` will continue writing beyond the buffer, eventually overwriting the return address. An attacker can craft input that overwrites the return address with the address of injected shellcode, causing the function to return to the attacker's code instead of the calling function.

### Heap-Based Buffer Overflow

Heap-based buffer overflows occur in dynamically allocated memory (the heap segment). Unlike stack-based overflows, heap overflows exploit the metadata structures used by memory allocators. When memory is allocated and freed, the allocator maintains free lists using metadata embedded in the heap. Overflowing into this metadata can corrupt these lists, leading to arbitrary code execution when subsequent allocations are made.

Modern heap allocators like glibc's ptmalloc2 use bins and chunks with specific structures. By overflowing a chunk's metadata, an attacker can manipulate heap consolidation processes or cause the allocator to return controlled memory to the application.

### Integer Overflow

Integer overflow occurs when an arithmetic operation produces a value outside the representable range for the integer type. While not a direct buffer overflow, integer overflows can lead to buffer overflows when used to calculate buffer sizes. For example:

```c
size_t size = large_number;
char *buffer = malloc(size);
memcpy(buffer, input, size);  // size may be smaller than intended
```

If `large_number` exceeds the maximum value for `size_t` on the system, it wraps around to a small value, potentially causing a buffer overflow when data is copied.

### Format String Vulnerability

Format string attacks exploit printf-style functions where user input is used as the format string. Input like `%x%x%x%x` can leak stack contents, while `%n` can write to arbitrary memory locations:

```c
printf(user_input);  // Vulnerable!
printf("%s", user_input);  // Fixed
```

### Shellcode and Exploit Development

Shellcode is machine code written to spawn a shell or perform other privileged operations. Traditional shellcode must be position-independent and avoid null bytes (for string-based exploits). Modern exploits often use Return-Oriented Programming (ROP) to chain together existing code fragments (gadgets) from the program or libraries, avoiding the need to inject new code.

## Examples

### Example 1: Stack-Based Buffer Overflow Exploitation

Consider a simple vulnerable server program:

```c
#include <stdio.h>
#include <string.h>

void process_request(char *input) {
    char buffer[256];
    strcpy(buffer, input);  // Vulnerable!
    printf("Processing: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        process_request(argv[1]);
    }
    return 0;
}
```

**Step-by-step exploitation:**
1. Determine buffer size: The buffer is 256 bytes
2. Find offset to return address: 256 bytes + 4 bytes (saved EBP) + 4 bytes (return address) = 264 bytes
3. Create exploit payload: 264 bytes of padding + 4 bytes (overwritten return address) + shellcode
4. When function returns, it jumps to shellcode address instead of caller

In a real attack, the attacker would use techniques like brute-forcing stack canaries, using format string leaks to find addresses, or ROP chains to bypass security measures.

### Example 2: Integer Overflow Leading to Buffer Overflow

```c
void read_data(char *src, unsigned short len) {
    char *buffer = malloc(len + 1);  // Potential integer overflow!
    if (buffer) {
        memcpy(buffer, src, len);
        buffer[len] = '\0';
    }
}
```

If `len` is 65535 (maximum unsigned short), then `len + 1` wraps to 0. malloc(0) may return a small allocation, but the subsequent `memcpy` copies 65535 bytes, causing a heap overflow.

### Example 3: Protection Bypass with Return-Oriented Programming

Modern systems have Data Execution Prevention (DEP) preventing execution of injected shellcode. ROP overcomes this by:
1. Using format string leak to dump stack contents and find addresses
2. Building a ROP chain using existing code in libc or the binary
3. Each "gadget" ends with a return instruction
4. Overwrite return address with first gadget, place address of second gadget on stack, etc.
5. Chain executes existing code with controlled parameters to disable DEP or execute commands

## Exam Tips

1. **Memory Layout Knowledge**: Understand the exact order of stack frame components (return address, saved base pointer, local variables) - this is frequently tested in DU exams.

2. **Difference Between Stack and Heap Overflows**: Stack overflows overwrite return addresses directly, while heap overflows corrupt allocator metadata and require more complex exploitation.

3. **Attack Prevention at Compile Time**: Remember that Stack Canaries (GCC's -fstack-protector), FORTIFY_SOURCE, and Position Independent Executables (PIE) are compile-time protections.

4. **Runtime Protections**: ASLR (Address Space Layout Randomization) randomizes memory addresses, making exploitation difficult. DEP/NX prevents code execution in non-executable memory regions.

5. **Safe Functions**: Use safer alternatives like `strncpy`, `snprintf`, `fgets` instead of `strcpy`, `sprintf`, `gets`. Understand that `strncpy` has its own issues (no null termination if source is longer than n-1).

6. **Vulnerable Functions**: Memorize the dangerous functions: `strcpy`, `strcat`, `sprintf`, `gets`, `scanf`, `printf` (when used with user input as format string).

7. **Real-World Context**: Be prepared to explain why these vulnerabilities persist despite being known for decades - legacy code, performance considerations, and lack of secure coding practices.

8. **Countermeasure Classification**: Know how to categorize protections: compile-time (canaries, PIE), link-time (RELRO), runtime (ASLR, DEP), and coding practices (bounds checking, input validation).