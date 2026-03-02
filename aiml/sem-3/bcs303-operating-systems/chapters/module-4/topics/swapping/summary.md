# Swapping

## Operating Systems

### Revision Notes

### Definitions and Key Concepts

- **Swapping**: A process in operating systems where two or more processes are swapped out of main memory to make room for new processes or data.
- **Memory Management Unit (MMU)**: A hardware component that manages the swapping process.

### Theorem:

- **Theorem: Swapping Property** - If P and Q are processes in the system, then:

* P is swapped out of memory
* Q is swapped in

- **Theorem: Swapping Algorithm** - If P and Q are processes in the system, then:

* P is swapped out of memory and placed in the free list
* Q is swapped in and placed in the free list
* If the free list is empty, P is swapped out to disk and Q is placed in the free list

### Important Formulas

- **Swap Formula** - `Swap = (Size of process) / (Size of memory)`

### Key Operations

- **Swap Out**: Removes a process from memory and places it on the free list.
- **Swap In**: Adds a new process to memory from the free list.
- **Page Replacement**: Replaces a process in memory with a new process when memory is full.

### Key Terms

- **Page Table**: A data structure used to manage the memory page table.
- **Page Replacement Algorithm**: An algorithm used to select which page to replace when swapping occurs.

### Important Points

- Swapping is a crucial process in operating systems to manage memory.
- MMU plays a key role in swapping process.
- Theorem of swapping property and swapping algorithm are essential concepts.
- Swap formula is used to calculate the number of swaps required.
