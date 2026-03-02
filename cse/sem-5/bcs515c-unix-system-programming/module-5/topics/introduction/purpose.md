# Learning Objectives

After studying this topic, you should be able to:

1. Define what a signal is in the context of Unix System Programming and explain its purpose in process communication.

2. Identify the different sources of signal generation in a Unix system, including hardware, software, and terminal-generated signals.

3. Explain the concept of signal disposition and describe the three possible actions: default, ignore, and custom handler.

4. List and describe the common signal types in Unix, including SIGINT, SIGKILL, SIGTERM, SIGSEGV, and SIGCHLD.

5. Compare the signal() and sigaction() interfaces, understanding why sigaction() is preferred in modern Unix programming.

6. Demonstrate the ability to write a C program that installs a signal handler using sigaction() to handle asynchronous events.

7. Understand the concept of async-signal-safe functions and identify which functions can be safely called from within signal handlers.

8. Explain how signals are used for inter-process communication using the kill() system call and parent-child process signal relationships.