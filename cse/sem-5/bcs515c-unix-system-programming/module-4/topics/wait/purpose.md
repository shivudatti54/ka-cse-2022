# Learning Objectives

After studying this topic, you should be able to:

1. Explain the purpose and functionality of the wait() system call in process management

2. Describe how the wait() system call enables parent-child process synchronization

3. Interpret process termination status using macros like WIFEXITED, WEXITSTATUS, WIFSIGNALED, and WTERMSIG

4. Compare and contrast wait() and waitpid() system calls with respect to their features and use cases

5. Identify the conditions that lead to zombie and orphan processes and explain how wait() prevents zombie processes

6. Apply waitpid() with different options (WNOHANG, WUNTRACED) to solve specific process synchronization problems

7. Write C programs that demonstrate proper parent-child process synchronization using wait operations
