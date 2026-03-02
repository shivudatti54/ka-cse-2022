# **Overview of IPC Methods, Pipes, popen, pclose Functions, Coprocesses, FIFOs, System V IPC, Message Queues, Semaphores**

## **I. IPC Methods**

- Inter-Process Communication (IPC) is used to enable communication between two or more processes.
- Methods:
  - Pipes
  - Sockets
  - Message Queues
  - Semaphores
  - Shared Memory
  - System V IPC

## **II. Pipes**

- A pipe is a unidirectional communication channel.
- Created using `pipe()` system call.
- Data is sent from parent process to child process.
- Read from the pipe in child process.

## **III. popen, pclose Functions**

- `popen()` function opens a pipe to the specified command.
- `pclose()` function closes the pipe.

## **IV. Coprocesses**

- A coprocess is a special type of process that runs in parallel with the parent process.
- Used in `fork()` system call.

## **V. FIFOs (Named Pipes)**

- A FIFO is a unidirectional communication channel.
- Created using `mkfifo()` system call.
- Can be read from and written to by multiple processes.

## **VI. System V IPC**

- System V IPC provides a set of inter-process communication functions.
- Includes:
  - `IPC_CREAT` and `IPC_EXCL` flags for creating pipes.
  - `pipe2()` system call.
  - `close()` system call with `IPC_CLOSE_ONExecuting` flag.

## **VII. Message Queues**

- A message queue is a data structure that holds messages between processes.
- Created using `msgget()` system call.
- Used with `msgsnd()` and `msgrcv()` system calls.

## **VIII. Semaphores**

- A semaphore is a variable that controls access to a shared resource.
- Created using `semget()` system call.
- Used with `sembuf` structure and `sem_wait()` and `sem_post()` system calls.

**Important Formulas and Definitions:**

- Pipe buffer size: `PIPE_BUF`
- Semaphore buffer size: `SEMAPHORE_MAXBUF`
- Message queue maximum size: `MSG_MAX`
- System V IPC flags:
  - `IPC_CREAT`: Creates a new pipe if it does not exist.
  - `IPC_EXCL`: Fails if the pipe does not exist.

**Theorems:**

- "The communication between two processes is possible only through the use of IPC."
- "The use of IPC provides a way for processes to communicate with each other."
