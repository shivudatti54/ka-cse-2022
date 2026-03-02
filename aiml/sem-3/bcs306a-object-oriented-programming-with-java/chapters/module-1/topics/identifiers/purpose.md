# Learning Objectives

After studying this topic, you should be able to:

1. Define what a Process Identifier (PID) is and explain its purpose in a Unix/Linux system.
2. Identify the special reserved PIDs (0 and 1) and explain their significance.
3. Use the key system calls (`getpid`, `getppid`, `getpgid`) correctly in a C program to retrieve process identification information.
4. Differentiate between a Process ID (PID), Parent Process ID (PPID), and Process Group ID (PGID).
5. Explain the lifecycle of a PID, including how and when it is created, used, and reused by the kernel.
6. Describe how the `/proc` filesystem organizes information based on PIDs and how to access it.
