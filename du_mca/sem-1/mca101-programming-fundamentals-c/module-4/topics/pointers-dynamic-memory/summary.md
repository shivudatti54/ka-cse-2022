# Pointers & Dynamic Memory (C) – Quick Revision  

**Introduction**  
In C, pointers provide low‑level memory access and are essential for dynamic memory management. The Revised June 2024 MCA syllabus (Unit‑3) expects you to understand pointer declaration, arithmetic, relationship with arrays, and the use of heap memory via `malloc`/`calloc`/`realloc`/`free`. This summary covers the core ideas for rapid recall.  

**Key Concepts**

- **Pointer Basics**  
  - A pointer stores a memory address of another variable.  
  - Declaration: `type *ptr;` (e.g., `int *p;`).  
  - Address‑of (`&`) yields a pointer; dereference (`*`) accesses the pointed value.  
  - `void *` is a generic pointer that can be cast to any type.  
  - **Pointer to Pointer**: `type **p;` stores address of a pointer; used for dynamic 2‑D arrays and for functions that need to modify a pointer.  

- **Pointer Arithmetic**  
  - Increment/ decrement moves by `sizeof(type)` bytes.  
  - Allowed operations: `+`, `-`, `++`, `--`, comparison (`==`, `<`, `>`) between pointers to the same array.  
  - Subtraction of two pointers yields the number of elements between them.  

- **Pointers and Arrays**  
  - Array name acts as a constant pointer to the first element.  
  - `arr[i]` ≡ `*(arr + i)`.  
  - Passing arrays to functions passes the address, enabling in‑place modification.  
  - **Dynamic 2‑D Arrays**: allocate an array of pointers (`int **arr = malloc(rows * sizeof(int*));`) then each row (`arr[i] = malloc(cols * sizeof(int));`).  

- **Dynamic Memory Allocation (DMA)**  
  - `malloc(size)`: allocates raw bytes; returns `void*`, cast to required type.  
  - `calloc(n, size)`: allocates and zero‑initializes; useful for arrays.  
  - `realloc(ptr, newSize)`: resizes previously allocated block; may move data.  
  - `free(ptr)`: releases heap memory; always pair with `malloc`/`calloc`/`realloc`.  
  - Header: `<stdlib.h>`.  

- **Memory Layout & Allocation**  
  - **Stack**: automatic storage for local variables.  
  - **Heap**: region for DMA; manually managed.  
  - Use `sizeof` to compute allocation sizes; avoid hard‑coded literals.  

- **Common Pitfalls & Best Practices**  
  - **Dangling pointers**: using a pointer after `free`; set to `NULL` after freeing.  
  - **Memory leaks**: forgetting to `free`; always balance allocation with deallocation.  
  - **Buffer overflow**: accessing beyond allocated size; validate indices.  
  - **Null‑pointer checks**: verify `malloc`/`calloc` return (`NULL` indicates failure).  
  - **Alignment**: ensure pointer type matches the data type to avoid undefined behaviour.  

- **Syllabus Alignment (Delhi University, June 2024)**  
  - Unit‑3 topics: pointer declaration, pointer arithmetic, array‑pointer relationship, dynamic allocation functions (`malloc`, `calloc`, `realloc`, `free`), pointer‑to‑pointer and dynamic 2‑D arrays, memory‑leak prevention.  
  - Practical questions often require writing a program that allocates a 1‑D or 2‑D array dynamically, populates it, and frees the memory.  

**Conclusion**  
Master pointers and DMA to harness C’s power for efficient, flexible programs. Remember the allocation‑deallocation cycle, avoid common errors, and align your revision with Unit‑3 of the Delhi University syllabus to ace the exam.