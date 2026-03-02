# Learning Objectives

After studying this topic, "wait and Process Termination", you should be able to:

1.  Explain the need for process synchronization between parent and child processes.
2.  Differentiate between the `exit()`, `_exit()`, and `_Exit()` functions and choose the appropriate one for a given scenario.
3.  Use the `wait()` system call correctly to reap a terminated child process and interpret its exit status using the standard macros (`WIFEXITED`, `WEXITSTATUS`, etc.).
4.  Utilize the `waitpid()` system call to wait for a specific child process and to perform non-blocking checks using the `WNOHANG` option.
5.  Define a zombie process, explain why they occur, and describe the system mechanism (involving the `init` process) that prevents them from persisting indefinitely.
6.  Identify potential race conditions in code that uses `fork()` and propose solutions using `wait()` or `waitpid()` for proper synchronization.
