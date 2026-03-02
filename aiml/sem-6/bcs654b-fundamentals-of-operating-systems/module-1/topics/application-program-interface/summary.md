# Application Program Interface (API) - Summary

## Key Definitions and Concepts

- **API**: Set of pre-defined functions/routines for software interaction with OS resources
- **System Call**: Direct interface to request kernel services (e.g., `read()`, `write()`)
- **Wrapper Function**: Library routines that abstract system calls (e.g., `fopen()` wraps `open()`)
- **POSIX**: Portable OS Interface standard for UNIX-like systems
- **Standard Library**: Collection of APIs (e.g., glibc in Linux, WinAPI in Windows)

## Important Mechanisms and Structures

```c
// Typical system call flow through API
1. User program calls library function (e.g., printf())
2. Library prepares system call parameters
3. Executes trap instruction (int 0x80 in x86)
4. Switch to kernel mode
5. Kernel executes system call handler
6. Return to user space with result
```

## Key Points

- APIs provide abstraction between applications and OS kernel
- Three main types of OS APIs: POSIX (Unix), Win32 (Windows), Java API
- Common API functions: File I/O (`fopen`, `read`), Process Control (`fork`, `exec`), Memory Management (`malloc`)
- System call vs API: APIs may use multiple system calls internally
- Benefits: Portability, Standardization, Security through controlled access
- Major components: System call interface, Language libraries (C/Python), Runtime environments
- Error handling: APIs return error codes (errno in C) for system call failures
- Modern implementations: REST APIs for distributed systems (microservices architecture)

## Common Mistakes to Avoid

1. Confusing APIs with system calls (APIs are user-level, system calls are kernel-level)
2. Assuming API functions are always direct 1:1 mappings to system calls
3. Ignoring error checking in API function return values
4. Overlooking API version compatibility issues (e.g., POSIX 2008 vs 2017)

## Revision Tips

1. Create comparison tables: System Calls vs API Functions vs CLI Commands
2. Practice tracing API-to-system call mappings (e.g., `malloc()` → `brk()`/`mmap()`)
3. Memorize 5 essential POSIX APIs from each category (File, Process, Memory)
4. Use diagramming to visualize API stack: Application → Library → System Call → Kernel
