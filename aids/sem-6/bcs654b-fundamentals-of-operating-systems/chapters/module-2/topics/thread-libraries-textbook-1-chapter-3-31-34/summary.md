# Thread Libraries Textbook 1: Chapter 3

### 3.1 Process Concept

- **Definition:** A process is a program in execution, running on a particular computer.
- **Key characteristics:**
  - A program in execution
  - Runs on a particular computer
  - Has its own memory space
  - Can be executed concurrently with other processes
- **Types of processes:**
  - User-level processes
  - Kernel-level processes

### 3.2 Process Scheduling

- **Definition:** The process of allocating the CPU to a process.
- **Scheduling algorithms:**
  - First-Come-First-Served (FCFS)
  - Shortest Job First (SJF)
  - Priority Scheduling (PS)
  - Round-Robin Scheduling (RR)
- **Advantages and disadvantages:**
  - FCFS: Simple to implement, but may lead to unfair treatment of processes
  - SJF: Fair treatment, but may lead to high waiting times
  - PS: Prioritizes processes based on their priority levels
  - RR: Rounds through processes in a circular fashion, ensuring fair treatment

### 3.3 Operations on Processes

- **Process creation:**
  - fork()
  - vfork()
  - exec()
- **Process termination:**
  - exit()
  - kill()
  - SIGTERM
- **Process synchronization:**
  - semaphores
  - monitors
  - mutexes

### 3.4 Process Synchronization

- **Definition:** The coordination of multiple processes to achieve a common goal.
- **Synchronization techniques:**
  - Semaphores: Counting variables used to control access to shared resources
  - Monitors: High-level synchronization mechanism using semaphores and monitors
  - Mutexes: Locks used to protect shared resources from concurrent access

## Important Formulas and Definitions

- **CPU utilization:** The percentage of time spent executing user-level processes.
- **Context switching:** The process of switching from one process to another.
- **Process scheduling overhead:** The time spent switching between processes.

## Theorems

- **Amdahl's Law:** Limits the speedup achievable by parallel processing.
- **Goto's Law:** States that parallel processing cannot be faster than sequential processing for some tasks.
