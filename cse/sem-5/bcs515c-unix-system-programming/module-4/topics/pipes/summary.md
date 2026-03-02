# Pipes in Unix/Linux - Summary

## Key Definitions and Concepts

- **Pipe**: A unidirectional communication channel in the kernel that allows data flow between related processes (parent-child).
- **Anonymous Pipe**: Created using `pipe()` system call, exists only in kernel memory, used for parent-child communication.
- **Named Pipe (FIFO)**: A special filesystem file created using `mkfifo()`, persists in filesystem, enables unrelated process communication.
- **File Descriptor**: An integer that identifies an open file descriptor table entry; pipe returns two: read end and write end.

## Important Formulas and Theorems

- `pipe(int pipefd[2])`: Creates pipe, returns 0 on success, -1 on failure. `pipefd[0]` = read end, `pipefd[1]` = write end.
- `mkfifo(const char *pathname, mode_t mode)`: Creates a named pipe at specified path with given permissions.
- Default pipe buffer size: 64KB on Linux.
- `PIPE_BUF`: 4096 bytes—writes smaller than this are guaranteed atomic.

## Key Points

- Pipes are unidirectional; for bidirectional communication, use two pipes.
- Always close unused pipe ends in each process to enable proper EOF detection.
- `read()` on empty pipe blocks until data arrives; `read()` returns 0 when all write ends are closed (EOF).
- `write()` blocks when pipe buffer is full.
- After `fork()`, child inherits parent's pipe file descriptors.
- Named pipes (FIFOs) allow unrelated processes to communicate.
- Use `wait()` in parent to prevent zombie processes.
- Data in pipes follows FIFO (First-In-First-Out) ordering.
- Named pipes appear as regular files in filesystem but behave like pipes.

## Common Mistakes to Avoid

1. Forgetting to close unused pipe ends, leading to blocking or EOF detection issues.
2. Confusing read and write ends—data flows from write (index 1) to read (index 0).
3. Not checking return values of pipe(), read(), and write() system calls.
4. Attempting to use anonymous pipes between unrelated processes.
5. Not using wait() in parent, causing zombie processes.

## Revision Tips

1. Remember the pipe creation syntax: `int pipefd[2]; pipe(pipefd);`
2. Visualize data flow: write end → kernel buffer → read end
3. Practice coding both anonymous and named pipe examples.
4. Review the relationship between fork() and pipe() for parent-child communication.
5. Understand EOF condition: read() returns 0 when all write ends are closed.
