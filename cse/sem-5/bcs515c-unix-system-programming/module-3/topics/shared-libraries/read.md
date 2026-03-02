# Shared Libraries in Linux/Unix Systems

## Introduction

Shared libraries are a fundamental concept in modern operating systems that enable multiple programs to share common code at runtime. Also known as dynamic link libraries (DLLs) in Windows or shared objects (.so files) in Linux, these libraries play a crucial role in reducing executable file sizes, conserving memory, and facilitating software updates without requiring recompilation of applications.

In the context of the CSE curriculum, understanding shared libraries is essential for system programming and operating system courses. The concept of shared libraries represents one of the most important advancements in software engineering, allowing developers to create modular, maintainable, and efficient software systems. When a program uses a shared library, the library code is not embedded into the executable during compilation; instead, the program references the library at runtime, enabling dynamic loading and sharing of code across multiple processes.

The development of shared libraries addressed several limitations of static libraries, where each program had its own copy of library code, leading to increased storage requirements and memory usage. Today, virtually all modern operating systems and applications leverage shared libraries for system functions, application frameworks, and third-party components.

## Key Concepts

### Static vs. Shared Libraries

**Static Libraries** (archive files with .a extension) are linked at compile time. The linker copies the required object code directly into the final executable. This results in larger executable files but ensures the program is self-contained and will run regardless of library availability on the system.

**Shared Libraries** (.so files in Linux, .dll in Windows) are linked at runtime. The executable contains only references to the library functions, and the actual code is loaded into memory when the program starts or when the function is first called. This approach significantly reduces executable size and allows library updates without recompiling programs.

### The Anatomy of Shared Libraries

A shared library in Linux follows specific naming conventions:

- **Real Name (soname)**: libname.so.major, where 'major' is the major version number (e.g., libm.so.6)
- **Link Name**: libname.so (symbolic link used during compilation)
- **Development Name**: libname.so (the actual file used for linking)

The library file contains position-independent code (PIC) that can be loaded at any memory address. This is crucial because the same library code may be mapped to different addresses in different processes.

### The Linking Process

The process of creating dynamically linked executables involves multiple stages:

1. **Compilation**: The compiler generates object code with unresolved external references
2. **Dynamic Linking**: The linker (ld) creates an executable with references to shared libraries rather than actual code
3. **Runtime Loading**: When the program starts, the dynamic linker (ld-linux.so) loads required libraries into memory
4. **Symbol Resolution**: The dynamic linker resolves function addresses and updates the program's GOT (Global Offset Table) and PLT (Procedure Linkage Table)

### Library Search Paths

The dynamic linker searches for shared libraries in the following order:

1. Paths specified in the executable's DT_RPATH attribute (deprecated)
2. LD_LIBRARY_PATH environment variable
3. Paths in /etc/ld.so.cache (built from /etc/ld.so.conf)
4. Default paths /lib and /usr/lib

### Loading and Symbol Resolution

When a program using shared libraries executes, the following occurs:

1. The kernel loads the executable and identifies shared library dependencies from the PT_DYNAMIC segment
2. The dynamic linker (ld-linux.so) loads all required libraries
3. For each external symbol, the linker searches in:

- The executable itself
- Libraries in the dependency order
- The main program can also export symbols for libraries

The PLT and GOT are used for lazy binding, where symbols are resolved only when first called, improving startup time.

### Position Independent Code (PIC)

PIC is machine code that executes correctly regardless of its absolute memory address. This is essential for shared libraries because:

- The same library code can be shared across multiple processes
- ASLR (Address Space Layout Randomization) can place libraries at different addresses
- The code uses relative addressing instead of absolute addresses

Compilers generate PIC using the -fPIC flag in GCC.

## Examples

### Example 1: Creating and Using a Shared Library

**Step 1: Create source files**

```c
// math_utils.c
int add(int a, int b) {
 return a + b;
}

int multiply(int a, int b) {
 return a * b;
}
```

**Step 2: Compile to object file with PIC**

```bash
gcc -fPIC -c math_utils.c -o math_utils.o
```

**Step 3: Create shared library**

```bash
gcc -shared -o libmathutils.so math_utils.o
```

**Step 4: Create main program**

```c
// main.c
#include <stdio.h>

extern int add(int a, int b);
extern int multiply(int a, int b);

int main() {
 printf("Add: %d\n", add(10, 5));
 printf("Multiply: %d\n", multiply(10, 5));
 return 0;
}
```

**Step 5: Compile and link with shared library**

```bash
gcc -o program main.c -L. -lmathutils
```

**Step 6: Run the program**

```bash
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
./program
```

### Example 2: Inspecting Shared Library Dependencies

Using the `ldd` command to view shared library dependencies:

```bash
$ ldd /bin/ls
linux-vdso.so.1 (0x00007fff...)
libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3
libdl.so.2 => /lib/x86_64-linux-gnu/liblibdl.so.2
/lib64/ld-linux-x86-64.so.2
```

Each line shows:

- The library name requested
- The actual library file found (after =>)
- The memory address where the library is mapped

### Example 3: Using dlopen for Dynamic Loading

The `dlopen` API allows programs to load libraries at runtime:

```c
#include <stdio.h>
#include <dlfcn.h>

typedef int (*add_func)(int, int);

int main() {
 void *handle = dlopen("./libmathutils.so", RTLD_LAZY);
 if (!handle) {
 fprintf(stderr, "Error: %s\n", dlerror());
 return 1;
 }

 add_func add = (add_func)dlsym(handle, "add");
 printf("Result: %d\n", add(20, 30));

 dlclose(handle);
 return 0;
}
```

Compile with: `gcc -o dynamic main.c -ldl`

## Exam Tips

1. **Know the difference between static and shared libraries** - This is frequently asked in exams. Remember: static libraries (.a) are linked at compile time, while shared libraries (.so) are linked at runtime.

2. **Understand the naming convention** - Remember: libname.so.major is the real name, and libname.so is the linker name.

3. **Library search order** - Memorize the order: DT_RPATH (deprecated) → LD_LIBRARY_PATH → /etc/ld.so.cache → /lib, /usr/lib.

4. **PIC importance** - Position Independent Code is essential for shared libraries to be loadable at any memory address and shareable across processes.

5. **Lazy binding concept** - Understand that PLT and GOT enable lazy binding, resolving symbols only when first called rather than at program startup.

6. **Advantages of shared libraries** - Reduced executable size, reduced memory usage, easier updates without recompilation.

7. **dlopen/dlsym functions** - Know these for dynamic loading at runtime, not compile time.

8. **LD_LIBRARY_PATH** - Remember this environment variable to add custom library search paths at runtime.

9. **ldconfig command** - Used to update the shared library cache in /etc/ld.so.cache after adding libraries to system directories.

10. **Dependency tracking** - Use `ldd` to view dependencies and `nm` to list symbols in libraries.
