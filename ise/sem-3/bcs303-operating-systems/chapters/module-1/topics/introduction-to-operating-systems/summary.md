# Introduction to Operating Systems - Summary

## Key Definitions and Concepts

- **Operating System**: A collection of system software that acts as an interface between computer hardware and users, managing hardware resources and providing services to application programs
- **Bootstrap Program**: Firmware code executed at power-on that initializes hardware and loads the operating system kernel
- **Process**: A program in execution, represented by a Process Control Block (PCB)
- **Kernel**: The core component of the OS that has complete control over all system resources
- **System Call**: The interface between user programs and the OS kernel

## Important Formulas and Theorems

No specific formulas apply to this introductory topic. However, key ratios to understand include:
- **CPU Utilization**: Percentage of time the CPU is actively processing (improved by multiprogramming)
- **Throughput**: Amount of work completed per unit time
- **Turnaround Time**: Time from job submission to job completion

## Key Points

1. An OS serves dual roles: AS A RESOURCE MANAGER (allocating hardware resources) and AS AN EXTENDED MACHINE (abstracting hardware complexity)

2. Operating system evolution: Batch Processing → Multiprogrammed Systems → Time-Sharing → Personal Computer OS → Modern Distributed/Mobile OS

3. Six main functions of OS: Process Management, Memory Management, File Management, Device Management, Security and Protection, Error Detection

4. Types of OS: Batch, Time-sharing, Distributed, Real-time (RTOS), Network, and Mobile Operating Systems

5. Real-time OS guarantees response within strict time constraints—used in embedded systems and medical devices

6. Bootstrap process: POST → Boot device selection → Boot loader → Kernel loading → Kernel initialization → System services → User interface

7. Multiprogramming improves CPU utilization by keeping multiple jobs in memory; time-sharing extends this to multiple interactive users

8. OS provides user convenience through GUI, command-line interface, and system calls

## Common Mistakes to Avoid

1. Confusing multiprogramming with time-sharing—multiprogramming is about CPU efficiency, time-sharing is about user interactivity

2. Thinking the OS is the only software on a computer—the OS is system software, while Microsoft Office, Chrome, etc., are application software

3. Assuming all operating systems are the same—each type (batch, RTOS, distributed) has specific design goals and use cases

4. Overlooking the security function of OS—protection mechanisms are a fundamental OS responsibility

5. Forgetting that the OS must manage both hardware resources AND provide services to applications

## Revision Tips

1. Create a timeline of OS evolution and write one paragraph explaining WHY each transition occurred

2. Practice defining OS, kernel, system call, and process from memory—these definitions frequently appear in exams

3. For each type of OS, note one real-world example and one characteristic feature

4. Draw the "OS as intermediate layer" diagram showing User → Application → OS → Hardware

5. Re-read examples in the textbook and try to explain them in your own words

6. Solve previous year DU question papers to understand the pattern and difficulty level