# Shared Libraries in Linux/Unix Systems - Summary

## Key Definitions and Concepts

- **Shared Library**: A collection of object code that can be loaded into memory at runtime and shared among multiple programs (.so files in Linux)
- **Dynamic Linking**: The process of linking libraries at runtime rather than compile time
- **Position Independent Code (PIC)**: Machine code that can execute correctly regardless of its absolute memory address
- **Lazy Binding**: Resolving symbols only when first called, using PLT and GOT tables
- **Dynamic Linker**: The system program (ld-linux.so) responsible for loading shared libraries and resolving symbols at runtime

## Important Formulas and Theorems

- **Library Naming**: libname.so.major.minor (e.g., libm.so.6.0.29)
- **Library Search Order**: DT_RPATH → LD_LIBRARY_PATH → /etc/ld.so.cache → /lib, /usr/lib
- **GCC flags**: -fPIC for position-independent code, -shared for creating shared libraries, -L for library path, -l for library name

## Key Points

- Shared libraries reduce executable size and memory usage by allowing code sharing across processes
- The dynamic linker (ld-linux.so) performs symbol resolution at runtime
- Libraries must contain PIC code to be loadable at any address
- LD_LIBRARY_PATH environment variable temporarily adds library search paths
- The ldd command displays shared library dependencies of an executable
- dlopen() and dlsym() enable runtime library loading without compile-time linking
- Library updates can be deployed without recompiling dependent applications
- The /etc/ld.so.conf and ldconfig manage system-wide library cache

## Common Mistakes to Avoid

1. Forgetting to export LD_LIBRARY_PATH when testing custom libraries in non-standard locations
2. Not using -fPIC flag when compiling shared libraries, leading to relocation errors
3. Confusing the library linker name (libname.so) with the actual library file (libname.so.major)
4. Not updating ldconfig after installing libraries in system directories
5. Using static libraries (.a) when dynamic linking (.so) is required

## Revision Tips

1. Practice creating a simple shared library from scratch and linking it with a program
2. Use `ldd program_name` to analyze dependencies of common system commands
3. Remember the library search order sequence for runtime linker
4. Review the difference between compile-time linking and runtime loading (dlopen)
5. Understand how GOT and PLT work together for lazy symbol binding
6. Know the purpose of /etc/ld.so.cache and when to run ldconfig
