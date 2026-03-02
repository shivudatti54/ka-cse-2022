# **Operating System Structure Revision Notes**

## **I. Introduction**

- Definition: A computer system that manages hardware and software resources
- Function: Provides common services to computer programs

## **II. Operating System Structure**

- **Hardware Abstraction Layer (HAL)**: provides interface between OS and hardware
- **System Software**: includes OS, device drivers, and utilities
- **Application Software**: user-level programs that interact with OS

## **III. Operating System Components**

- **Process Management**:
  - Process creation and termination
  - Process scheduling (FCFS, SJF, Priority Scheduling)
  - Process synchronization (semaphores, monitors)
- **Memory Management**:
  - Memory allocation and deallocation
  - Virtual memory
  - Paging and segmenting
- **File Systems**:
  - File organization and storage
  - File access control
  - File protection
- **Input/Output Management**:
  - Input devices ( keyboards, mice)
  - Output devices (monitors, printers)
  - I/O scheduling

## **IV. Operating System Models**

- **Batch Processing Model**: jobs are executed in batches
- **Time-Sharing Model**: multiple jobs are executed concurrently
- **Multitasking Model**: multiple jobs are executed simultaneously

## **V. Operating System Types**

- **Single-User, Single-Tasking OS**: one user, one process
- **Single-User, Multi-Tasking OS**: one user, multiple processes
- **Multi-User, Multi-Tasking OS**: multiple users, multiple processes

## **VI. Important Formulas and Definitions**

- **CPU Utilization**: (number of processes in the system) / (number of available CPUs)
- **Turnaround Time (TAT)**: average time from arrival to completion
- **Response Time (RT)**: average time from arrival to completion
- **Processor Utilization**: percentage of time CPU is busy
- **Throughput**: number of jobs completed per unit time

## **VII. Important Theorems**

- **Amdahl's Law**: maximum theoretical speedup of a parallel algorithm
- **Golubie's Law**: maximum theoretical speedup of a parallel algorithm (modified Amdahl's Law)
