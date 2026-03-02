# Types of System Calls - Summary

## Key Definitions and Concepts

- **System Calls**: Programming interfaces that allow user-space applications to request services from the operating system kernel; the only legal gateway for user programs to access hardware and system resources

- **Kernel Mode**: Privileged execution mode where the operating system has full access to hardware and can execute protected operations

- **User Mode**: Unprivileged mode where user applications run with restricted access to system resources

- **File Descriptor**: A small non-negative integer that uniquely identifies an open file for a process; standard file descriptors are 0 (stdin), 1 (stdout), and 2 (stderr)

## Important System Calls by Category

| Category | Key System Calls |
|----------|------------------|
| Process Control | fork(), exec(), wait(), exit() |
| File Management | open(), read(), write(), close(), lseek() |
| Device Management | ioctl(), read(), write() on device files |
| Information Maintenance | getpid(), getuid(), time(), uname() |
| Communication | pipe(), socket(), connect(), bind(), send(), recv() |
| Protection | chmod(), chown(), setuid(), setgid() |

## Key Points

1. System calls provide controlled access to kernel services, maintaining system security and stability

2. The fork() system call creates a new process by duplicating the parent; exec() replaces the current process image with a new program

3. File descriptors are used to reference open files; multiple processes can share file descriptors through inheritance or explicit sharing

4. Pipes (created via pipe()) provide unidirectional IPC between parent and child processes; sockets enable bidirectional communication between arbitrary processes

5. The setuid bit allows programs to run with elevated privileges; this is essential for system utilities requiring root access

6. Device files in UNIX treat hardware as special files, enabling uniform access through standard file operations

7. System call numbers identify specific operations; arguments are passed through CPU registers during the mode transition

8. The wait() system call allows parent processes to synchronize with child termination and retrieve exit status

## Common Mistakes to Avoid

- Confusing fork() with exec(): fork() creates a new process, exec() replaces the program in the current process

- Forgetting to close file descriptors: This can lead to resource leaks, especially in long-running processes

- Misunderstanding the direction of pipes: Data flows from the write end to the read end; writing to the read end or reading from the write end will fail

- Confusing real UID with effective UID: Real UID identifies the actual user, effective UID determines current privileges

## Revision Tips

1. Create a table mapping each system call category to its functions and purposes

2. Practice writing small C programs using fork(), exec(), pipe(), and file operations

3. Trace through program execution with fork() and exec() to understand the process lifecycle

4. Review the difference between blocking and non-blocking I/O operations

5. Understand how file permissions work (owner/group/others × read/write/execute)