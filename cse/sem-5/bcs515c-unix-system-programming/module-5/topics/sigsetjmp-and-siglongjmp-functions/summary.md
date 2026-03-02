# sigsetjmp and siglongjmp Functions - Summary

## Key Definitions and Concepts

- **sigjmp_buf**: A special array type that stores execution context including program counter, stack pointer, and optionally signal mask for non-local jumps.

- **sigsetjmp()**: Function that saves the current execution environment. Returns 0 on initial call, returns the value from siglongjmp on jump. Prototype: `int sigsetjmp(sigjmp_buf env, int savesigs)`.

- **siglongjmp()**: Function that restores execution context previously saved by sigsetjmp. Prototype: `void siglongjmp(sigjmp_buf env, int val)`.

- **savesigs parameter**: When non-zero, the current signal mask is saved in env; when zero, signal mask is not saved.

## Important Formulas and Theorems

- **sigsetjmp return value**: Returns 0 if called directly; returns val if returned via siglongjmp
- **siglongjmp behavior**: Restores program counter, stack pointer, and optionally signal mask from the saved environment

## Key Points

1. sigsetjmp/siglongjmp are POSIX-standard functions for non-local jumps with signal mask support
2. The key advantage over setjmp/longjmp is the ability to save and restore signal masks
3. sigsetjmp takes two parameters: env (buffer) and savesigs (flag for saving signal mask)
4. siglongjmp takes two parameters: env (buffer) and val (return value for sigsetjmp)
5. When savesigs is non-zero, siglongjmp restores the signal mask to saved state
6. Variables modified between sigsetjmp and siglongjmp should be declared volatile
7. The sigjmp_buf must remain valid (not go out of scope) between the two calls
8. siglongjmp does not unwind the stack - execution continues as if sigsetjmp just returned

## Common Mistakes to Avoid

1. Using setjmp/longjmp instead of sigsetjmp/siglongjmp in signal handlers
2. Forgetting that sigsetjmp returns twice - once with value 0, and again after longjmp
3. Not declaring volatile for variables that change between setjmp and longjmp
4. Using a sigjmp_buf that has gone out of scope when calling longjmp
5. Calling siglongjmp with a signal blocked that triggered the handler

## Revision Tips

1. Practice writing programs with sigsetjmp/siglongjmp to understand the double return behavior
2. Remember: savesigs = 1 means save signal mask, savesigs = 0 means don't save
3. Compare with setjmp/longjmp - the only difference is signal mask handling
4. Review signal handler restrictions when using these functions
5. Remember the header file: <setjmp.h> for POSIX systems
