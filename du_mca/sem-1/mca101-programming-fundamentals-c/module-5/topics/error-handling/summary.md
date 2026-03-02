# Error Handling in C - Summary

## Key Definitions and Concepts

- **Error Handling**: The process of detecting, reporting, and recovering from programming errors to prevent program crashes
- **errno**: A global variable in `<errno.h>` that stores error codes from failed system calls and library functions
- **Signal**: Asynchronous notification sent to a process indicating an event (like Ctrl+C or division by zero)
- **setjmp/longjmp**: Mechanism for non-local jumps to handle errors across function boundaries

## Important Formulas and Theorems

- Function return value conventions: Return 0 for success, -1 (or NULL for pointers) for failure
- `perror(msg)`: Prints "msg: [error description]" to stderr
- `strerror(errno)`: Returns string describing the errno value
- `exit(EXIT_SUCCESS)` or `exit(EXIT_FAILURE)`: Terminates program with status code

## Key Points

- C lacks built-in exceptions; relies on return values, errno, and manual checking
- Always check return values, especially for file operations (fopen returns NULL on failure)
- Use errno after detecting a failure, not before—errno is only meaningful after a failure
- assert() is disabled when NDEBUG is defined; never use for runtime errors that need handling
- Signals like SIGINT, SIGSEGV, and SIGFPE can be caught and handled gracefully
- Proper error handling includes cleanup: close files, free memory before exiting on errors
- setjmp() returns twice: first with 0 (initial call), then with the value from longjmp()

## Common Mistakes to Ignore

- Ignoring return values from functions like fopen(), malloc(), printf()
- Checking errno before confirming a failure occurred
- Using assert() for runtime errors that should be handled gracefully
- Not cleaning up allocated memory when errors occur (memory leaks)
- Using exit() inappropriately when returning an error code would be cleaner
- Confusing compile-time errors (syntax) with runtime errors (logic)

## Revision Tips

1. Practice writing complete C programs with error handling for file operations—check each fopen, fread, fwrite
2. Remember the mnemonic: "Check returns, set errno, use perror, clean up"
3. For assert(), remember: assert checks what SHOULD be true; handle what CAN go wrong
4. Review standard library functions and their failure indicators—NULL vs -1 vs specific values
5. Understand signal handling with practical examples—try handling SIGINT in a simple loop program