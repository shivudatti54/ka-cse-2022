# Virtual Machines - Summary

## Key Definitions
- **Virtual Machine (VM)**: A software emulation of a physical computer system that executes programs like a real machine
- **Virtual Machine Monitor (VMM)**: Software that creates and manages virtual machines, also called a hypervisor
- **Hypervisor**: The component responsible for virtualizing hardware resources and isolating guest operating systems
- **System Virtual Machine**: A VM that provides a complete system environment capable of running a full operating system
- **Process Virtual Machine**: A VM that executes a single program or process in a platform-independent manner
- **Full Virtualization**: Technique that emulates hardware to run unmodified guest operating systems
- **Paravirtualization**: Technique requiring guest OS modification for better performance
- **Hardware-Assisted Virtualization**: Uses CPU extensions (Intel VT-x, AMD-V) to improve virtualization efficiency

## Important Formulas
No specific mathematical formulas apply to this topic. The concepts are theoretical and architectural in nature.

## Key Points
1. Virtual machines provide an abstraction layer allowing multiple OS to run on single hardware
2. Type 1 hypervisors run directly on hardware (bare-metal); Type 2 run on host OS
3. System VMs (VirtualBox, VMware) can run complete operating systems
4. Process VMs (JVM, CLR) provide runtime environments for specific programs
5. Virtualization enables server consolidation, reducing hardware costs
6. VMs provide strong isolation for security and testing purposes
7. Hardware-assisted virtualization significantly reduces performance overhead
8. Paravirtualization requires modifications to guest OS but offers better performance
9. Virtual machines are fundamental to modern cloud computing infrastructure
10. Live migration allows moving running VMs between physical hosts without service interruption

## Common Mistakes
1. Confusing Type 1 and Type 2 hypervisors - remember Type 1 has no host OS
2. Mixing up system VMs and process VMs - they serve different purposes
3. Assuming virtual machines have no performance overhead - there is always some overhead
4. Thinking virtualization eliminates the need for security - the hypervisor itself can be vulnerable
5. Confusing virtualization with emulation - emulation involves software imitation of hardware, while virtualization shares actual hardware