# Learning Objectives

After studying this topic, you should be able to:

1. Explain the concept of process creation and the role of the fork() system call in Unix-like operating systems

2. Describe the three possible return values of fork() and what each signifies (positive, zero, and negative)

3. Analyze the execution flow of a program before and after fork(), understanding that both parent and child continue execution from the return point

4. Understand the Copy-on-Write (COW) mechanism and its importance in making fork() efficient

5. Distinguish between fork(), vfork(), and the fork()+exec() combination for process creation

6. Write C programs that correctly use fork() to create child processes and handle their execution

7. Identify and prevent common issues such as zombie processes using wait() and waitpid() system calls

8. Apply knowledge of process hierarchy in Unix systems to understand parent-child relationships between processes
