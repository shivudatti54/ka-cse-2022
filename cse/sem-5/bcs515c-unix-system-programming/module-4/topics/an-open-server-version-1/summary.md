# An Open Server Version 1 - Summary

## Key Definitions

- **Open Server**: A server process that accepts connections from multiple clients using IPC mechanisms like pipes or FIFOs
- **Unnamed Pipe**: A one-way communication channel created via `pipe()`, existing only while related processes hold references to it
- **FIFO (Named Pipe)**: A named pipe accessible via filesystem path, enabling communication between unrelated processes
- **File Descriptor**: An integer that uniquely identifies an open file for a process
- **Protocol**: A set of rules defining the format and order of messages exchanged between client and server

## Important Formulas

- `pipe(int pipefd[2])` - Creates pipe, fd[0] for read, fd[1] for write
- `mkfifo(const char *pathname, mode_t mode)` - Creates a named pipe
- `read(int fd, void *buf, size_t count)` - Reads data from pipe
- `write(int fd, const void *buf, size_t count)` - Writes data to pipe
- `fdopen(int fd, const char *mode)` - Converts file descriptor to FILE pointer

## Key Points

- Open server version 1 represents the simplest client-server model using pipes or FIFOs
- Unnamed pipes require parent-child relationship, while FIFOs enable unrelated process communication
- Server must close unused pipe ends: write end of input pipe, read end of output pipe
- Clients must close: read end of input pipe, write end of output pipe
- The server typically operates in a loop, reading requests, processing them, and sending responses
- Message delimiters (newlines, length prefixes) are essential for parsing multiple requests
- `fork()` creates a copy of file descriptors; both parent and child initially share the same pipe ends
- EOF is detected when all write ends of a pipe are closed—read returns 0
- FIFOs are unlinked using `unlink()` when no longer needed

## Common Mistakes

1. **Forgetting to close unused pipe ends**: Causes the server to block indefinitely waiting for EOF that never comes because an extra write end remains open
2. **Not flushing output buffers**: When using `fdopen()` with buffered I/O, forgetting to call `fflush()` can cause the server to hang waiting for buffered data
3. **Incorrect pipe direction**: Confusing which file descriptor is for reading (index 0) versus writing (index 1)
4. **Not handling blocking reads**: Failing to account for the blocking nature of pipe reads can cause processes to hang
5. **Protocol ambiguity**: Not defining clear message boundaries leads to incorrect parsing when multiple messages are sent through the pipe