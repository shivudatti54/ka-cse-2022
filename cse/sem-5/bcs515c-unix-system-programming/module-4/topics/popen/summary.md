# popen() Function - Summary

## Key Definitions and Concepts

- **popen()**: A C library function that creates a pipe and executes a shell command, returning a FILE pointer for communication.
- **Pipe**: A unidirectional communication channel connecting stdout of one process to stdin of another.
- **pclose()**: Closes a pipe opened by popen() and waits for the child process to terminate.

## Important Formulas and Theorems

```c
FILE *popen(const char *command, const char *mode);
int pclose(FILE *stream);
```

- **Modes**: "r" (read from command's stdout) or "w" (write to command's stdin)
- **Return value**: FILE pointer on success, NULL on failure
- **pclose() return**: Exit status of the command (use WEXITSTATUS to extract)

## Key Points

1. popen() creates a pipe and forks a child process to execute the specified command.

2. Only two modes are supported: "r" for reading command output, "w" for sending input to command.

3. The returned FILE pointer can be used with standard I/O functions (fgets, fprintf, fread, fwrite).

4. Always check return value against NULL before using the FILE pointer.

5. pclose() MUST be called to prevent zombie processes and resource leaks.

6. The command is executed through /bin/sh -c, so shell features like pipes and redirections work.

7. In write mode, always flush (fflush) or close the stream before calling pclose() to ensure all data is sent.

## Common Mistakes to Avoid

- Forgetting to call pclose() - leads to resource leaks and zombie processes
- Not checking popen() return value for NULL
- Trying to use both read and write modes simultaneously (not supported)
- Not flushing the buffer before pclose() in write mode - data may be lost

## Revision Tips

1. Memorize the function prototype: `FILE *popen(const char *command, const char *mode)`

2. Remember: "r" = read from command, "w" = write to command

3. Always pair popen() with pclose()

4. Practice writing at least 2-3 programs using popen() before the exam

5. Understand that popen() is a higher-level abstraction combining pipe(), fork(), and exec()
