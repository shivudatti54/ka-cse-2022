# Abort Function - Summary

## Key Definitions and Concepts

- **abort()**: A function in <stdlib.h> that causes abnormal program termination by raising SIGABRT signal
- **SIGABRT**: Signal sent by abort(), with default action of terminating the process
- **Abnormal Termination**: Program ending without performing normal cleanup operations
- **Core Dump**: Memory image file generated on abnormal termination for debugging

## Important Formulas and Theorems

- Function prototype: `void abort(void);`
- Signal raised: SIGABRT (signal number 6 on POSIX systems)
- assert() macro internally uses abort() when assertion fails

## Key Points

- abort() does NOT call functions registered with atexit() or at_quick_exit()
- abort() does NOT flush output buffers or close files
- abort() sends SIGABRT signal which by default terminates the program
- Unlike exit(), abort() represents abnormal/emergency termination
- assert() failures internally call abort() when NDEBUG is not defined
- abort() typically generates a core dump for post-mortem debugging
- If SIGABRT is caught and handler returns, most implementations call \_exit()

## Common Mistakes to Avoid

- Confusing abort() with exit() - they have different cleanup behaviors
- Thinking abort() always returns (it never returns to caller)
- Forgetting to include <stdlib.h> header
- Assuming abort() performs normal cleanup operations

## Revision Tips

1. Create a comparison table of abort(), exit(), and return from main()
2. Write small C programs to observe abort() behavior and core dumps
3. Remember: "A-bort" = Abnormal termination (no cleanup)
4. Practice identifying when each termination method should be used
5. Review signal handling concepts alongside abort()
