# FIFOs (Named Pipes) - Summary

## Key Definitions and Concepts

- **FIFO (Named Pipe):** A special filesystem object that allows unrelated processes to communicate using the First-In-First-Out data ordering principle.
- **Anonymous Pipe:** A pipe created using the pipe() system call that only allows communication between parent and child processes.
- **Blocking Mode:** Default behavior where operations wait until they can complete (e.g., read waits for data, write waits for buffer space).
- **O_NONBLOCK Flag:** POSIX flag that makes FIFO operations non-blocking, returning immediately with appropriate error codes.

## Important Formulas and Theorems

- **FIFO Creation:** `int mkfifo(const char *pathname, mode_t mode);` - Returns 0 on success, -1 on failure.
- **FIFO Opening:** `int open(const char *pathname, int flags);` - Blocks until both ends are opened by default.
- **Buffer Size:** Unix FIFO buffer is typically 64KB; writing beyond this blocks unless O_NONBLOCK is set.
- **Blocking Behavior:** read() blocks on empty FIFO; write() blocks on full FIFO; open() blocks if no process has the other end open.

## Key Points

- FIFOs are unidirectional - use two FIFOs for bidirectional communication between processes.
- The 'p' in `ls -l` output indicates a FIFO special file type.
- Client-server patterns require separate FIFOs for request and response channels.
- Always check return values of mkfifo(), open(), read(), and write() for error handling.
- Use unlink() to remove FIFOs from the filesystem after use.
- ENXIO error occurs when attempting to open FIFO for writing with no reader present.
- Default umask affects the actual permission bits of created FIFOs.

## Common Mistakes to Avoid

1. **Forgetting to create the FIFO:** Many students forget that FIFOs must be explicitly created before use.
2. **Assuming bidirectional communication with single FIFO:** FIFOs are one-way; two FIFOs needed for two-way communication.
3. **Ignoring blocking behavior:** This leads to deadlocks in exam questions - always analyze which process opens first.
4. **Not handling ENXIO error:** Common when using O_NONBLOCK without a reader, causing program failure.

## Revision Tips

1. Practice writing programs that create, open, read, and write to FIFOs until the syntax becomes automatic.
2. Draw process diagrams showing which process opens which end of the FIFO first.
3. Memorize the header files required: `<sys/types.h>`, `<sys/stat.h>`, `<fcntl.h>`, `<unistd.h>`.
4. For exams, always analyze blocking conditions - determine what happens if processes crash or don't open their ends.
5. Remember that FIFO operations are identical to regular file operations after opening.
