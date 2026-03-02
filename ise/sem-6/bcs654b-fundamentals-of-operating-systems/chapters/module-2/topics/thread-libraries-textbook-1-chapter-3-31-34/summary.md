# **Thread Libraries Textbook 1: Chapter 3: 3.1-3.4 Revision Notes**

## **3.1 Process Concepts**

- **Definition:** A process is a program in execution, executing a sequence of instructions.
- **Process Attributes:**
  - **Process ID (PID):** Unique identifier for a process.
  - **Process Name:** Name given to a process.
  - **Process Priority:** Determines the order in which processes are executed.
  - **Process State:** Running, Waiting, Sleeping, Zombie, Dead.

## **3.2 Process Scheduling**

- **Definition:** The process of allocating system resources to a process.
- **Process Scheduling Algorithms:**
  - **FCFS (First-Come-First-Served):** Allocates resources to the process that arrived first.
  - **SJF (Shortest Job First):** Allocates resources to the process with the shortest execution time.
  - **RR (Round Robin):** Allocates resources for a fixed time period to each process.
  - **Priority Scheduling:** Allocates resources to the process with the highest priority.

## **3.3 Operations on Processes**

- **Process Creation:** Creating a new process using the `fork()` system call.
- **Process Termination:** Terminating a process using the `exit()` system call.
- **Process Communication:** Using pipes, semaphores, and shared memory to communicate between processes.
- **Process Synchronization:** Ensuring that multiple processes access shared resources safely and efficiently.

## **3.4 Process Synchronization**

- **Definition:** The act of coordinating access to shared resources by multiple processes.
- **Synchronization Primitives:**
  - **Mutex (Mutual Exclusion):** Ensures exclusive access to a shared resource.
  - **Semaphore:** Limits the number of concurrent accesses to a shared resource.
  - **Monitors:** A abstract data type that allows multiple processes to access shared resources safely and efficiently.
- **Deadlock Prevention:** Techniques to prevent the occurrence of deadlocks, including avoiding nested locks and using lock ordering.

**Important Formulas and Definitions:**

- **Priority Ceiling Algorithm:** `C_i = max(C_j)`, where `C_i` is the priority ceiling of process `i`.
- **Earliest Deadline First (EDF) Scheduling:** Schedules processes based on their earliest deadline.
- **Definition:** A process is said to be **deadlock-free** if it can be executed to completion without encountering a deadlock situation.
