# What Operating Systems Do - Summary

## Key Definitions and Concepts

An OPERATING SYSTEM is system software that acts as an intermediary between computer hardware and user applications, managing hardware resources while providing a consistent interface for software. The KERNEL is the core component of the operating system that manages essential system resources and provides fundamental services. A SYSTEM CALL is the interface through which user programs request services from the operating system kernel. VIRTUALIZATION refers to creating abstract or simulated representations of hardware resources, such as virtual memory or virtual CPUs.

## Important Formulas and Theorems

There are no specific formulas in this introductory topic, but key principles include: the operating system must balance efficiency (maximizing resource utilization) with fairness (ensuring all processes receive adequate resources), and the principle of abstraction (hiding complexity behind well-defined interfaces) applies throughout operating system design.

## Key Points

- Operating systems serve dual roles: as an extended virtual machine providing abstraction, and as a resource manager coordinating hardware components.

- The evolution progressed from batch processing through multiprogramming and time-sharing to modern multi-purpose operating systems.

- Essential OS services include program execution, I/O operations, file system manipulation, communications, and error detection.

- Operating systems can be classified as single-user or multi-user, single-task or multi-task, and real-time or general-purpose.

- Memory management uses virtual memory to make programs believe they have more memory than physically available through paging and swapping.

- Device drivers provide the translation between generic OS I/O requests and device-specific commands.

- The kernel remains resident in memory and provides the most fundamental operating system functions.

- Security services include user authentication, access control, and permission mechanisms.

## Common Mistakes to Avoid

Many students confuse the operating system with the user interface (shell). Remember that the graphical desktop or command shell is merely an application running on top of the operating system kernel. Another common error is believing that the operating system is the only software on a computer; firmware, device drivers, and utility programs are distinct software components. Additionally, avoid thinking that more features always mean a better operating system; embedded systems often require minimal, specialized operating systems precisely because they cannot afford the overhead of general-purpose features.

## Revision Tips

When revising this topic, focus on understanding the conceptual frameworks rather than memorizing isolated facts. Practice explaining operating system concepts in your own words, as examination questions often require you to demonstrate understanding through explanation rather than mere recall. Review how operating systems handle specific scenarios like launching an application or managing memory, as these applied examples frequently appear in examinations. Finally, ensure you can distinguish between related but distinct concepts like multiprogramming and time-sharing, or between the kernel and the shell.