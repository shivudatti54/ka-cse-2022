# Chapter 4: Process Management

### 4.1 Process Concept

### Definition

A process is an independent program that runs on a computer, executing a specific task or a set of tasks. It consists of a sequence of instructions, called program instructions or machine code, that are executed by the computer's processor.

### Characteristics of a Process

- **Independence**: A process can be executed independently of other processes.
- **Resource allocation**: A process requires its own resources, such as memory, CPU time, and I/O devices.
- **Communication**: Processes can communicate with each other through inter-process communication (IPC) mechanisms.

### Types of Processes

There are two types of processes:

- **User-level process**: A process created by a user, which is executed in the user's address space.
- **Kernel-level process**: A process created by the operating system, which is executed in the kernel's address space.

### Process Identification

A process is identified by a unique identifier, called a process ID (PID), which is assigned by the operating system.

### Examples

- A web browser is a process that runs on the computer, displaying a web page and responding to user input.
- A printer driver is a process that manages communication between the operating system and a printer.

### Key Concepts

- **Process creation**: The process of creating a new process in the operating system.
- **Process termination**: The process of terminating a process in the operating system.
- **Process synchronization**: The process of coordinating the execution of multiple processes.

### Process Synchronization

Process synchronization is the process of ensuring that multiple processes access shared resources in a safe and efficient manner. This is achieved through synchronization primitives, such as:

- **Mutex (mutual exclusion)**: A lock that prevents only one process from accessing a shared resource.
- **Semaphore**: A variable that controls the access to a shared resource.
- **Monitors**: A high-level synchronization construct that allows multiple processes to access shared resources.

### Example

Consider two processes, P1 and P2, that are accessing a shared resource, a file. To synchronize access to the file, we can use a semaphore.

```markdown
// Create a semaphore to control access to the file
sem_t file_sem;

// Process P1 tries to access the file
if (sem_wait(&file_sem) == 0) {
// Access the file
printf("P1 accessing file\n");
sem_post(&file_sem); // Release the semaphore
} else {
printf("P1 failed to access file\n");
}

// Process P2 tries to access the file
if (sem_wait(&file_sem) == 0) {
// Access the file
printf("P2 accessing file\n");
sem_post(&file_sem); // Release the semaphore
} else {
printf("P2 failed to access file\n");
}
```

In this example, the semaphore ensures that only one process can access the file at a time, preventing conflicts and ensuring safe access to the shared resource.
