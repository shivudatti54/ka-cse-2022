# Learning Objectives

After studying this topic, you should be able to:

1. Identify which functions are async-signal-safe and can be called from signal handlers
2. Explain why certain functions (like printf) cannot be safely used in signal handlers
3. Demonstrate proper use of `volatile sig_atomic_t` for sharing variables between signal handlers and main programs
4. Compare `sigaction()` and `signal()` functions and explain why `sigaction()` is preferred
5. Write correct signal handlers that follow POSIX coding rules
6. Use `sigsuspend()` to atomically block signals and wait for them
7. Implement safe communication between signal handlers and main programs using pipes
8. Apply signal masking techniques to protect critical code sections from interruption
9. Understand the importance of re-entrancy in signal handlers
10. Write portable Unix signal handling code that works across different implementations