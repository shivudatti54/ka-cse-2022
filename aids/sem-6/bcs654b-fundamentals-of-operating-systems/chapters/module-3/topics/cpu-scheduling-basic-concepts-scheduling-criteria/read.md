# **CPU Scheduling: Basic Concepts, Scheduling Criteria, Scheduling Algorithms, Thread Scheduling, Process Synchronization**

## **1. Introduction**

CPU scheduling is the process of allocating the CPU to a process or thread and determining the order in which they are executed. It is a critical component of an operating system, as it determines how resources are allocated and how tasks are executed.

## **2. Basic Concepts**

### 2.1 Definition of CPU Scheduling

CPU scheduling is the process of allocating the CPU to a process or thread and determining the order in which they are executed.

### 2.2 CPU Scheduling Models

There are two main CPU scheduling models:

- **Preemptive Scheduling**: In this model, the operating system can interrupt a process and switch to another process at any time.
- **Non-Preemptive Scheduling**: In this model, once a process is scheduled, it runs until it is completed.

### 2.3 CPU Scheduling Types

There are three main CPU scheduling types:

- **Short-Term Scheduling**: This type of scheduling is concerned with the allocation of the CPU to a process for a short period of time.
- **Long-Term Scheduling**: This type of scheduling is concerned with the allocation of resources to a process for an extended period of time.
- **Multilevel Scheduling**: This type of scheduling is concerned with the allocation of resources to a process based on multiple criteria.

## **3. Scheduling Criteria**

### 3.1 Factors Affecting CPU Scheduling

The following are some of the factors that affect CPU scheduling:

- **Process Priority**: The priority of a process determines the order in which it is executed.
- **Process Arrival Time**: The time at which a process arrives at the operating system determines its priority.
- **Process Burst Time**: The time a process runs on the CPU determines its priority.
- **CPU Utilization**: The amount of time the CPU is used determines the priority of a process.

## **4. Scheduling Algorithms**

### 4.1 First-Come-First-Served (FCFS) Algorithm

In the FCFS algorithm, the process that arrives first is executed first.

### 4.2 Shortest Job First (SJF) Algorithm

In the SJF algorithm, the process with the shortest burst time is executed first.

### 4.3 Priority Scheduling Algorithm

In the priority scheduling algorithm, the process with the highest priority is executed first.

### 4.4 Round Robin (RR) Algorithm

In the RR algorithm, each process is allocated a fixed time slice, called a time quantum, and the process that has the most remaining time is executed next.

### 4.5 Multilevel Feedback Queue (MLFQ) Algorithm

In the MLFQ algorithm, multiple queues are used, each with a different priority. The process with the highest priority is executed first.

### 4.6 Earliest Deadline First (EDF) Algorithm

In the EDF algorithm, the process with the earliest deadline is executed first.

## **5. Thread Scheduling**

Thread scheduling is a type of CPU scheduling that schedules threads instead of processes.

### 5.1 Thread Scheduling Types

There are three main types of thread scheduling:

- **Preemptive Thread Scheduling**: In this type of scheduling, the operating system can interrupt a thread and switch to another thread at any time.
- **Cooperative Thread Scheduling**: In this type of scheduling, threads voluntarily yield control to other threads.
- **Asynchronous Thread Scheduling**: In this type of scheduling, threads are executed in the background without the need for explicit control.

### 5.2 Thread Scheduling Algorithms

There are several thread scheduling algorithms, including:

- **Shortest Remaining Time First (SRTF) Algorithm**: This algorithm assigns the thread with the shortest remaining time to the CPU.
- **Rate Monotonic Scheduling (RMS) Algorithm**: This algorithm assigns threads based on their priority.

## **6. Process Synchronization**

Process synchronization is the process of coordinating the actions of multiple processes.

### 6.1 Synchronization Types

There are two main types of synchronization:

- **Mutual Exclusion**: This type of synchronization ensures that only one process can access a shared resource at a time.
- **Non-Mutual Exclusion**: This type of synchronization allows multiple processes to access a shared resource simultaneously.

### 6.2 Synchronization Algorithms

There are several synchronization algorithms, including:

- **Semaphore Algorithm**: This algorithm uses semaphores to coordinate access to shared resources.
- **Monitors Algorithm**: This algorithm uses monitors to coordinate access to shared resources.

### 6.3 Critical Sections

A critical section is a section of code that accesses a shared resource.

### 6.4 Locks and Semaphores

Locks and semaphores are used to protect shared resources from concurrent access.

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Basic Concepts](#2-basic-concepts)
  - [2.1 Definition of CPU Scheduling](#21-definition-of-cpu-scheduling)
  - [2.2 CPU Scheduling Models](#22-cpu-scheduling-models)
  - [2.3 CPU Scheduling Types](#23-cpu-scheduling-types)
- [3. Scheduling Criteria](#3-scheduling-criteria)
  - [3.1 Factors Affecting CPU Scheduling](#311-factors-affecting-cpu-scheduling)
- [4. Scheduling Algorithms](#4-scheduling-algorithms)
  - [4.1 First-Come-First-Served (FCFS) Algorithm](#411-first-come-first-served-fcfs-algorithm)
  - [4.2 Shortest Job First (SJF) Algorithm](#412-shortest-job-first-sjf-algorithm)
  - [4.3 Priority Scheduling Algorithm](#413-priority-scheduling-algorithm)
  - [4.4 Round Robin (RR) Algorithm](#414-round-robin-rr-algorithm)
  - [4.5 Multilevel Feedback Queue (MLFQ) Algorithm](#415-multilevel-feedback-queue-mlfq-algorithm)
  - [4.6 Earliest Deadline First (EDF) Algorithm](#416-earliest-deadline-first-edf-algorithm)
- [5. Thread Scheduling](#5-thread-scheduling)
  - [5.1 Thread Scheduling Types](#511-thread-scheduling-types)
  - [5.2 Thread Scheduling Algorithms](#512-thread-scheduling-algorithms)
- [6. Process Synchronization](#6-process-synchronization)
  - [6.1 Synchronization Types](#611-synchronization-types)
  - [6.2 Synchronization Algorithms](#612-synchronization-algorithms)
  - [6.3 Critical Sections](#613-critical-sections)
  - [6.4 Locks and Semaphores](#614-locks-and-semaphores)
