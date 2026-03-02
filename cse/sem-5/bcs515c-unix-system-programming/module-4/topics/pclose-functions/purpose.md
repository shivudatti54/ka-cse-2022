# Learning Objectives

After studying this topic, you should be able to:

1. Understand the purpose and functionality of the `popen()` and `pclose()` functions in C programming.

2. Explain how pipes facilitate inter-process communication (IPC) between a parent process and a child process.

3. Identify the different types of pipe modes ("r" for read and "w" for write) and their appropriate usage.

4. Write C programs that successfully open pipes to external commands, read from them, and write to them.

5. Properly close pipes using `pclose()` and ensure all child processes are terminated without creating zombie processes.

6. Interpret the exit status returned by `pclose()` using the standard macros (WIFEXITED, WEXITSTATUS, WIFSIGNALED, WTERMSIG).

7. Implement appropriate error handling for both `popen()` and `pclose()` operations in system programs.

8. Apply best practices for resource management when working with process pipes in real-world applications.
