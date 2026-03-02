# Operating System Structure, Services, and System Calls - Summary

## Key Definitions and Concepts

- **Operating System Structure**: The internal architectural design of an OS determining how components are organized—monolithic, layered, microkernel, or hybrid.

- **Monolithic Kernel**: Entire OS runs in single kernel address space with all core services; high performance but poor fault isolation (Linux, traditional UNIX).

- **Layered Architecture**: OS organized into hierarchical layers where each layer uses services from below and provides services to above (THE OS, modern systems' organizational principle).

- **Microkernel**: Minimal kernel containing only essential functions; most services run as user-space processes; excellent reliability and security but IPC overhead (QNX, MINIX 3).

- **System Calls**: Programming interface allowing user programs to request privileged kernel services; involves mode switch from user mode to kernel mode.

- **Mode Switch**: Transition between user mode (restricted privileges) and kernel mode (full hardware access); fundamental to OS security.

## Important Formulas and Theorems

- **System Call Number Dispatch**: The kernel uses the system call number in RAX (x86-64) to index into a system call table to find the appropriate handler function.

- **Parameter Passing Limits**: Register-based parameter passing typically limited to 6 arguments on x86-64; larger parameter sets require memory block/table approach.

## Key Points

1. Linux uses a monolithic architecture with loadable kernel modules providing extensibility while maintaining performance.

2. The layered approach simplifies OS development and debugging but can impact performance due to multiple function call levels.

3. Microkernel design prioritizes reliability and security—service failures don't crash the kernel—making it suitable for embedded and safety-critical systems.

4. Most modern systems (Windows, macOS) use hybrid architectures combining microkernel principles with monolithic performance optimizations.

5. System calls are the sole interface between user programs and kernel services; all privileged operations must go through this controlled boundary.

6. The `syscall` instruction on x86-64 triggers the mode switch with minimal overhead compared to older interrupt-based mechanisms.

7. OS services include user-facing functions (UI, program execution) and system-facing functions (process management, memory management, file systems).

8. Real-world OS examples: Linux (monolithic with modules), QNX (microkernel), Windows NT (hybrid), macOS (hybrid XNU).

## Common Mistakes to Confuse

- Treating `printf()` as a system call—it is a library function that internally calls the `write()` system call.

- Believing microkernels are always slower—modern implementations have largely eliminated IPC overhead through optimization.

- Confusing OS structure with user interface—the GUI is merely a user-facing component, not the structural architecture.

## Revision Tips

1. Draw comparison diagrams showing data flow in monolithic vs. microkernel architectures.

2. Practice tracing system call execution: identify what happens when you call `open()`, `fork()`, or `read()`.

3. Remember that Linux is monolithic but supports loadable modules—it's not purely one category.

4. Focus on understanding why each architectural choice exists, not just memorizing categories.

5. Review the system call categories and be able to provide at least two examples of each.