# Learning Objectives

After studying this topic, you should be able to:

1. Understand the purpose and functionality of the wait() system call for parent-child process synchronization

2. Explain the difference between wait(), waitpid(), and wait3() system calls and their appropriate use cases

3. Analyze the termination status of a process using standard macros like WIFEXITED(), WEXITSTATUS(), WIFSIGNALED(), and WTERMSIG()

4. Identify and explain zombie and orphan processes, and describe how wait() prevents zombie process formation

5. Implement programs that properly handle child process termination using waitpid() with various options like WNOHANG

6. Utilize wait3() to retrieve resource usage information about terminated child processes

7. Apply these concepts to design robust process management solutions in C programs for Unix/Linux systems

8. Evaluate process behavior under different termination conditions (normal exit, signal death, stopped)
