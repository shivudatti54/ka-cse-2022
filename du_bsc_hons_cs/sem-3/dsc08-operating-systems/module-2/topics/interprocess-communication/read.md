# Interprocess Communication (IPC)

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

**Interprocess Communication (IPC)** is a fundamental concept in operating systems that enables processes to communicate, share data, and synchronize their activities. In modern computing environments, almost every non-trivial application relies on IPC mechanisms. When you stream a video while downloading a file, when your web browser communicates with a web server, or when different components of a distributed application exchange data—all of these scenarios depend on effective interprocess communication.

For students preparing for Delhi University examinations, IPC is a core topic in the Operating Systems paper. Understanding IPC mechanisms is not just crucial for academic success but also essential for practical software development, particularly in areas like client-server programming, microservices architecture, and system-level programming.

---

## 2. Why Do Processes Need to Communicate?

Processes in an operating system are typically isolated from each other for security and stability reasons. This isolation, while beneficial, creates a need for controlled communication channels. The primary reasons for IPC include:

- **Data Sharing**: Multiple processes may need access to the same data (e.g., a shared database or configuration file).
- **Resource Sharing**: Processes may need to share hardware resources like printers, memory, or CPU time.
- **Synchronization**: Processes often need to coordinate their activities to avoid race conditions or deadlocks.
- **Modularity**: Breaking down complex applications into smaller, communicating processes improves maintainability and allows different programming languages or systems to work together.

---

## 3. Classification of IPC Mechanisms

IPC mechanisms can be broadly classified into two categories:

| Category | Description | Examples |
|----------|-------------|----------|
| **Message Passing** | Processes exchange messages through communication channels | Pipes, FIFOs, Message Queues, Sockets |
| **Shared Memory** | Multiple processes access a common memory region | Shared Memory, Memory-Mapped Files |
| **Synchronization** | Mechanisms to coordinate process activities | Semaphores, Mutexes, Condition Variables, Signals |

---

## 4. Shared Memory

### 4.1 Concept

Shared memory is the fastest IPC mechanism because it allows multiple processes to access the same physical memory location directly. One process creates a shared memory segment, and other processes can attach to it. Once attached, processes can read from and write to this shared memory without kernel intervention, making it extremely efficient for high-speed data exchange.

### 4.2 Implementation in UNIX/Linux

In POSIX systems, shared memory is implemented using the following system calls:

- `shmget()`: Creates a shared memory segment
- `shmat()`: Attaches the shared memory segment to a process's address space
- `shmdt()`: Detaches the shared memory segment
- `shmctl()`: Controls shared memory operations (like removal)

### 4.3 Example: Producer-Consumer using Shared Memory

```c
// producer.c - Creates shared memory and writes data
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>

int main() {
    // Create shared memory segment
    key_t key = ftok("/tmp", 'A');
    int shmid = shmget(key, 1024, IPC_CREAT | 0666);
    
    // Attach to shared memory
    char *str = (char*) shmat(shmid, NULL, 0);
    
    // Write data to shared memory
    printf("Producer: Writing to shared memory...\n");
    strcpy(str, "Hello from Producer Process!");
    
    printf("Data written: %s\n", str);
    
    // Detach
    shmdt(str);
    
    return 0;
}

// consumer.c - Reads from shared memory
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int main() {
    key_t key = ftok("/tmp", 'A');
    int shmid = shmget(key, 1024, 0666);
    
    // Attach to shared memory
    char *str = (char*) shmat(shmid, NULL, SHM_RDONLY);
    
    printf("Consumer: Reading from shared memory...\n");
    printf("Data read: %s\n", str);
    
    // Detach
    shmdt(str);
    
    // Remove shared memory
    shmctl(shmid, IPC_RMID, NULL);
    
    return 0;
}
```

---

## 5. Pipes

### 5.1 Concept

A **pipe** is a unidirectional communication channel that connects the output of one process to the input of another. Pipes are the simplest form of IPC and are created using the `pipe()` system call. Data written to the write end of the pipe can be read from the read end.

### 5.2 Types of Pipes

1. **Anonymous Pipes**: Only visible to related processes (parent-child or sibling processes). Created using `pipe()`.
2. **Named Pipes (FIFOs)**: Visible in the filesystem, allowing unrelated processes to communicate. Created using `mkfifo()`.

### 5.3 Example: Anonymous Pipe

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    char buffer[100];
    
    // Create pipe
    if (pipe(pipefd) == -1) {
        perror("pipe");
        return 1;
    }
    
    pid_t pid = fork();
    
    if (pid == 0) {
        // Child process - write to pipe
        close(pipefd[0]); // Close read end
        char message[] = "Message from child process";
        write(pipefd[1], message, strlen(message) + 1);
        close(pipefd[1]);
    } else {
        // Parent process - read from pipe
        wait(NULL);
        close(pipefd[1]); // Close write end
        read(pipefd[0], buffer, sizeof(buffer));
        printf("Parent received: %s\n", buffer);
        close(pipefd[0]);
    }
    
    return 0;
}
```

---

## 6. FIFOs (Named Pipes)

### 6.1 Concept

A **FIFO (First In, First Out)**, also known as a named pipe, is a special file type in the filesystem that allows unrelated processes to communicate. Unlike anonymous pipes, FIFOs persist in the filesystem and can be opened by any process with appropriate permissions.

### 6.2 Implementation

FIFOs can be created using the `mkfifo()` command or system call:

```c
// Creating a FIFO programmatically
#include <sys/types.h>
#include <sys/stat.h>

int main() {
    if (mkfifo("/tmp/myfifo", 0666) == -1) {
        perror("mkfifo");
    }
    return 0;
}
```

**Using FIFO from command line:**

```bash
# Terminal 1 - Reader
$ mkfifo /tmp/myfifo
$ cat /tmp/myfifo

# Terminal 2 - Writer
$ echo "Hello through FIFO" > /tmp/myfifo
```

### 6.3 Real-World Use Case

FIFOs are commonly used in:
- Client-server applications where the server needs to handle multiple clients
- Producer-consumer scenarios between unrelated processes
- Logging systems where multiple processes write to a central logger

---

## 7. Message Queues

### 7.1 Concept

Message queues provide a way for processes to exchange messages stored in a kernel-managed queue. Unlike pipes, message queues support:
- Multiple senders and receivers
- Message prioritization (priority-based messaging)
- Message boundaries (structured messages)
- Asynchronous communication

### 7.2 Implementation in POSIX

```c
// sender.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/msg.h>

struct msgbuf {
    long mtype;
    char mtext[100];
};

int main() {
    key_t key = ftok("/tmp", 'B');
    int msgid = msgget(key, IPC_CREAT | 0666);
    
    struct msgbuf message;
    message.mtype = 1;
    strcpy(message.mtext, "Hello from sender");
    
    msgsnd(msgid, &message, sizeof(message.mtext), 0);
    printf("Message sent: %s\n", message.mtext);
    
    return 0;
}

// receiver.c
#include <stdio.h>
#include <stdlib.h>
#include <sys/msg.h>

struct msgbuf {
    long mtype;
    char mtext[100];
};

int main() {
    key_t key = ftok("/tmp", 'B');
    int msgid = msgget(key, 0666);
    
    struct msgbuf message;
    msgrcv(msgid, &message, sizeof(message.mtext), 1, 0);
    printf("Message received: %s\n", message.mtext);
    
    // Remove message queue
    msgctl(msgid, IPC_RMID, NULL);
    
    return 0;
}
```

---

## 8. Signals

### 8.1 Concept

**Signals** are software interrupts that notify a process of an event. They are asynchronous notification mechanisms used for:
- Terminating a process (`SIGTERM`, `SIGKILL`)
- Reporting errors (`SIGSEGV`, `SIGFPE`)
- User interactions (`SIGINT` - Ctrl+C)
- Custom communication between processes

### 8.2 Common Signals

| Signal | Default Action | Description |
|--------|----------------|-------------|
| SIGTERM | Terminate | Graceful termination request |
| SIGKILL | Terminate | Forced termination (cannot be caught) |
| SIGINT | Terminate | Interrupt from keyboard (Ctrl+C) |
| SIGSEGV | Terminate + Core | Segmentation fault |
| SIGALRM | Terminate | Timer alarm |
| SIGCHLD | Ignore | Child process status change |

### 8.3 Signal Handling Example

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void signal_handler(int signum) {
    printf("\nCaught signal %d (", signum);
    if (signum == SIGINT) printf("SIGINT");
    else if (signum == SIGTERM) printf("SIGTERM");
    printf("). Cleaning up and exiting...\n");
    exit(0);
}

int main() {
    signal(SIGINT, signal_handler);
    signal(SIGTERM, signal_handler);
    
    printf("Process ID: %d\n", getpid());
    printf("Press Ctrl+C to send SIGINT\n");
    
    while(1) {
        printf("Running...\n");
        sleep(1);
    }
    
    return 0;
}
```

### 8.4 Real-World Relevance

Signals are extensively used in:
- Unix/Linux systems for process management
- Implementing timeouts in network programming
- Handling asynchronous events in servers
- Job control in shell environments

---

## 9. Semaphores

### 9.1 Concept

A **semaphore** is a synchronization primitive that controls access to shared resources by multiple processes. It is essentially a counter that:
- Increments on resource release
- Decrements on resource acquisition
- Blocks when the count is zero (waiting)

### 9.2 Types of Semaphores

1. **Binary Semaphore (Mutex)**: Can only be 0 or 1; used for mutual exclusion
2. **Counting Semaphore**: Can take non-negative integer values; used for resource counting

### 9.3 Implementation using POSIX Semaphores

```c
// process1.c - Increment semaphore
#include <stdio.h>
#include <semaphore.h>
#include <fcntl.h>

int main() {
    sem_t *sem = sem_open("/mysem", O_CREAT, 0666, 1);
    
    sem_wait(sem);
    printf("Process 1: Entered critical section\n");
    sleep(2);
    printf("Process 1: Leaving critical section\n");
    sem_post(sem);
    
    sem_close(sem);
    return 0;
}

// process2.c
#include <stdio.h>
#include <semaphore.h>
#include <fcntl.h>

int main() {
    sem_t *sem = sem_open("/mysem", O_CREAT, 0666, 1);
    
    sem_wait(sem);
    printf("Process 2: Entered critical section\n");
    sleep(2);
    printf("Process 2: Leaving critical section\n");
    sem_post(sem);
    
    sem_close(sem);
    return 0;
}
```

### 9.4 System V Semaphores

For more complex synchronization, System V semaphores are used:

```c
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>

int main() {
    // Create semaphore set
    int semid = semget(IPC_PRIVATE, 1, IPC_CREAT | 0666);
    
    // Initialize semaphore to 1
    union semun arg;
    arg.val = 1;
    semctl(semid, 0, SETVAL, arg);
    
    // Operation structure
    struct sembuf sop;
    sop.sem_num = 0;
    sop.sem_op = -1;  // Wait (decrement)
    sop.sem_flg = 0;
    
    // Wait operation
    semop(semid, &sop, 1);
    
    printf("Critical section\n");
    
    // Signal operation
    sop.sem_op = 1;
    semop(semid, &sop, 1);
    
    // Remove semaphore
    semctl(semid, 0, IPC_RMID);
    
    return 0;
}
```

---

## 10. Sockets

### 10.1 Concept

**Sockets** provide a mechanism for communication between processes on different machines (or the same machine) over a network. They are the foundation of network programming and support:
- Local communication (Unix domain sockets)
- Network communication (TCP/UDP sockets)
- Connection-oriented (TCP) and connectionless (UDP) communication

### 10.2 Types of Sockets

1. **Stream Sockets (SOCK_STREAM)**: TCP - reliable, connection-oriented
2. **Datagram Sockets (SOCK_DGRAM)**: UDP - unreliable, connectionless
3. **Raw Sockets**: Direct access to network protocols
4. **Unix Domain Sockets**: Local interprocess communication

### 10.3 Example: Unix Domain Socket

```c
// server.c
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>

int main() {
    int server_fd, client_fd;
    struct sockaddr_un address;
    char buffer[100];
    
    // Create socket
    server_fd = socket(AF_UNIX, SOCK_STREAM, 0);
    
    // Configure address
    address.sun_family = AF_UNIX;
    strcpy(address.sun_path, "/tmp/mysocket");
    unlink(address.sun_path);
    
    // Bind
    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    listen(server_fd, 5);
    
    // Accept connection
    client_fd = accept(server_fd, NULL, NULL);
    read(client_fd, buffer, sizeof(buffer));
    printf("Server received: %s\n", buffer);
    
    // Close
    close(client_fd);
    close(server_fd);
    unlink("/tmp/mysocket");
    
    return 0;
}

// client.c
#include <stdio.h>
#include <sys/socket.h>
#include <sys/un.h>

int main() {
    int sock_fd;
    struct sockaddr_un address;
    
    sock_fd = socket(AF_UNIX, SOCK_STREAM, 0);
    
    address.sun_family = AF_UNIX;
    strcpy(address.sun_path, "/tmp/mysocket");
    
    connect(sock_fd, (struct sockaddr*)&address, sizeof(address));
    write(sock_fd, "Hello from client", 18);
    
    close(sock_fd);
    
    return 0;
}
```

---

## 11. Comparison of IPC Mechanisms

| Mechanism | Direction | Speed | Complexity | Use Case |
|-----------|-----------|-------|------------|----------|
| Pipes | Unidirectional | Fast | Low | Parent-child communication |
| FIFOs | Unidirectional | Fast | Medium | Unrelated processes |
| Message Queues | Bidirectional | Medium | Medium | Priority-based messaging |
| Shared Memory | Bidirectional | Very Fast | Medium | High-speed data sharing |
| Sockets | Bidirectional | Medium | High | Network communication |
| Signals | Asynchronous | Very Fast | Low | Event notification |
| Semaphores | Synchronization | Fast | Low | Resource synchronization |

---

## 12. Delhi University Syllabus Context

This study material covers the following topics as per the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus:

- **Unit I**: Introduction to Processes and Interprocess Communication
- **Unit II**: Shared Memory and Memory-Mapped Files
- **Unit III**: Message Passing (Pipes, FIFOs, Message Queues)
- **Unit IV**: Signals and Signal Handling
- **Unit V**: Synchronization Mechanisms (Semaphores, Mutexes)
- **Unit VI**: Socket Programming Basics

---

## 13. Key Takeaways

1. **IPC is Essential**: Interprocess communication is fundamental to modern operating systems and enables process cooperation, data sharing, and system modularity.

2. **Message Passing vs. Shared Memory**: Message passing (pipes, queues, sockets) involves copying data between address spaces, while shared memory provides direct access to common memory. Shared memory is faster but requires explicit synchronization.

3. **Synchronization is Critical**: When multiple processes access shared resources, synchronization mechanisms like semaphores and mutexes are essential to prevent race conditions and ensure data consistency.

4. **Signals are Asynchronous**: Signals provide a lightweight mechanism for process notification but should not be used for regular data transfer due to their asynchronous nature.

5. **Sockets are Versatile**: Sockets support both local and network communication, making them the most versatile IPC mechanism for distributed systems.

6. **Choose Appropriate Mechanism**: The choice of IPC mechanism depends on factors like data volume, communication pattern, process relationship, and performance requirements.

7. **Practical Application**: Understanding IPC is crucial for system programming, embedded systems, distributed computing, and software development roles.

---

## References

1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson.
3. Stevens, W. R., & Rago, S. A. (2013). *Advanced Programming in the UNIX Environment* (3rd ed.). Addison-Wesley.
4. Kumar, R. (2023). *Operating Systems: A Concept-Based Approach*. Delhi University Publications.
5. Linux Man Pages: `shmget`, `shmat`, `pipe`, `mkfifo`, `msgget`, `semget`, `signal`, `socket`

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University as per the NEP 2024 UGCF curriculum.*