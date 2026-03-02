# Introduction to Operating Systems - Summary

## Key Definitions and Concepts

- OPERATING SYSTEM: A system software that acts as an interface between computer hardware and users, managing resources and providing services to application programs.
- PROCESS: A program in execution; the unit of work in a multiprogrammed system.
- RESOURCE MANAGER: The OS function of coordinating and allocating hardware resources (CPU, memory, I/O) among competing processes.
- VIRTUAL MEMORY: A memory management technique that allows programs to use more memory than physically available by using disk space as an extension of RAM.

## Important Functions of an Operating System

1. PROCESS MANAGEMENT: Creating, scheduling, and terminating processes; implementing CPU scheduling algorithms.
2. MEMORY MANAGEMENT: Allocating and deallocating memory space; implementing virtual memory and address translation.
3. FILE MANAGEMENT: Creating, deleting, and organizing files; maintaining file system directories and access control.
4. DEVICE MANAGEMENT: Controlling I/O devices through drivers; handling device scheduling and buffering.
5. SECURITY AND PROTECTION: Implementing authentication, access control, and ensuring system integrity.

## Types of Operating Systems

- BATCH: Processes jobs in batches without user interaction
- TIME-SHARING: Allows multiple users to access the system simultaneously
- REAL-TIME: Guarantees response within strict time constraints (used in embedded systems)
- NETWORK: Provides networking capabilities and resource sharing over networks
- DISTRIBUTED: Manages multiple interconnected computers as a single system

## Key Points

- AN OS HAS TWO PRIMARY ROLES: providing user convenience and managing system resources efficiently.
- EVOLUTION PROGRESSED from single-user batch systems to sophisticated multiuser, multiprocess systems.
- MODERN OS USE MULTIPROGRAMMING to maximize CPU utilization by keeping multiple processes in memory.
- CONTEXT SWITCHING creates the illusion of concurrent execution on a single CPU.
- VIRTUAL MEMORY extends physical memory using disk storage through paging and swapping.
- DEVICE DRIVERS provide abstraction between the OS and hardware devices.
- FILE SYSTEMS organize data hierarchically with support for naming, protection, and operations.

## Common Mistakes to Avoid

- CONFUSING PROGRAM with process—a program is passive code, process is active execution.
- THINKING multiple processes run truly simultaneously on a single-core CPU; this is illusion created by rapid switching.
- IGNORING the security aspect of operating systems; protection mechanisms are fundamental OS functions.
- OVERLOOKING the importance of I/O management; I/O operations often determine overall system performance.

## Revision Tips

- CREATE COMPARISON CHARTS differentiating OS types and their characteristics.
- MEMORIZE the five main OS functions and be able to explain each with examples.
- PRACTICE DEFINITIONS using precise technical language; avoid colloquial explanations.
- UNDERSTAND RESOURCE MANAGEMENT thoroughly—this concept appears throughout operating system studies.
- REVIEW PAST EXAM PAPERS to identify frequently asked question patterns and important topics.