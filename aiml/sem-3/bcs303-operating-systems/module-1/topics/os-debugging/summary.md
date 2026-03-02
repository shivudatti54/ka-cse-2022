# OS Debugging - Summary

## Key Definitions

- **Kernel Panic**: A fatal error condition in the OS kernel that halts the system to prevent data loss or corruption.

- **Kernel Oops**: A non-fatal error in the Linux kernel that prints error information but allows the system to continue operating.

- **Core Dump**: A file containing the memory state of a crashed process, used for post-mortem analysis.

- **Crash Dump**: A snapshot of kernel memory and state when the kernel itself crashes, captured via kdump.

- **Race Condition**: A bug where system behavior depends on the unpredictable timing of concurrent operations.

- **Deadlock**: A state where two or more processes wait indefinitely for resources held by each other.

- **KGDB**: Kernel GNU Debugger, a patch enabling GDB to debug the Linux kernel remotely.

## Important Formulas

- **Virtual Memory Address Translation**: Physical Address = (Page Directory Entry × Page Size) + Page Table Entry Offset + Offset

- **Stack Trace Analysis**: Return Address = Saved Frame Pointer + sizeof(return address)

## Key Points

1. OS debugging operates at multiple privilege levels: user-space (less privileged) and kernel-space (highest privilege).

2. Kernel panics display error messages and stack traces that are essential for diagnosis; always note the call trace first.

3. Memory leaks in the kernel are tracked using tools like kmemleak, which scans for unreferenced allocations.

4. Race conditions and deadlocks require careful analysis of synchronization primitives and resource acquisition ordering.

5. strace traces system calls, while ltrace traces library calls—both are fundamental for diagnosing process behavior.

6. Core dumps require ulimit settings and may need to be enabled explicitly; crash dumps require kdump configuration.

7. The /proc filesystem provides real-time access to kernel data structures for debugging running systems.

8. Debugging symbols (CONFIG_DEBUG_INFO) are essential for meaningful crash dump and kernel debugging analysis.

9. Hardware-assisted debugging (JTAG) provides lowest-level debugging for embedded systems and firmware.

## Common Mistakes

1. **Forgetting to enable debug symbols**: Without CONFIG_DEBUG_INFO, crash dumps show only memory addresses, not source code locations.

2. **Not configuring core dump size limits**: Applications may fail to generate core dumps if ulimit -c is set to zero.

3. **Overlooking the difference between user-space and kernel debugging tools**: strace and GDB work for user processes but require KGDB or SystemTap for kernel debugging.

4. **Ignoring race conditions in concurrent code**: Timing-dependent bugs may not reproduce consistently, leading to incorrect conclusions about root causes.

5. **Failing to preserve crash dumps**: Systems may overwrite crash dumps on reboot; immediate preservation is critical for analysis.