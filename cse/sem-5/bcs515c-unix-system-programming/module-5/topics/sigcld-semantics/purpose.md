# Learning Objectives

After studying this topic, you should be able to:

1. Explain the purpose and behavior of the SIGCLD signal in Unix/Linux systems

2. Describe the concept of zombie processes and explain why they occur

3. Demonstrate the use of wait() and waitpid() system calls to reap terminated child processes

4. Write C programs that properly handle SIGCLD using both signal() and sigaction() interfaces

5. Implement non-blocking child process monitoring using waitpid() with the WNOHANG option

6. Differentiate between various process states (running, sleeping, stopped, zombie) in Unix

7. Apply appropriate signal handling techniques to prevent zombie process accumulation in server and daemon programs
