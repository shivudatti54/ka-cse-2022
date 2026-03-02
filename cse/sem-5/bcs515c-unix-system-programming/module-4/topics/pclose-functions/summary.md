# Pipes and Process Management with pclose() - Summary

## Key Definitions and Concepts

- **popen()**: Creates a pipe and spawns a shell command, returning a FILE pointer for reading or writing
- **pclose()**: Closes a pipe opened by popen(), waits for the child process to terminate, and returns its exit status
- **Pipe**: A unidirectional communication channel between two related processes
- **Zombie Process**: A terminated process whose parent hasn't collected its exit status via wait()/waitpid()
- **Exit Status**: An integer returned by a process indicating success (0) or failure (non-zero)

## Important Formulas and Theorems

- **popen() prototype**: `FILE *popen(const char *command, const char *type)`
- **pclose() prototype**: `int pclose(FILE *stream)`
- **Exit status macros** (from `<sys/wait.h>`):
  - `WIFEXITED(status)` - True if normal exit
  - `WEXITSTATUS(status)` - Exit code (0-255)
  - `WIFSIGNALED(status)` - True if terminated by signal
  - `WTERMSIG(status)` - Signal number that killed process

## Key Points

- `popen()` creates unidirectional pipes only; type must be "r" (read) or "w" (write)
- Always check if `popen()` returns NULL before using the FILE pointer
- Every `popen()` must be matched with a corresponding `pclose()` to prevent zombie processes
- `pclose()` blocks until the child process terminates and returns its exit status
- The exit status is stored in the lower 8 bits of the status word (0-255 range)
- Standard I/O functions (fprintf, fscanf, fgets, fread, fwrite) can be used with the pipe FILE pointer
- `popen()` internally uses fork() to create a child process

## Common Mistakes to Avoid

- Forgetting to call `pclose()`, leading to resource leaks and zombie processes
- Not checking the return value of `popen()` before using it
- Attempting bidirectional communication with a single popen() call (not supported)
- Not flushing buffers before closing, causing data loss
- Ignoring the exit status returned by pclose(), missing command failure detection

## Revision Tips

1. Practice writing programs that pipe to common commands like `ls`, `grep`, `bc`, and `cat`
2. Always check exit status using the WIFEXITED macro before calling WEXITSTATUS
3. Remember that pclose() returns -1 on error; check errno in such cases
4. Understand that pclose() waits for the specific child process created by its corresponding popen()
5. Review the difference between normal termination (WIFEXITED) and signal termination (WIFSIGNALED)
