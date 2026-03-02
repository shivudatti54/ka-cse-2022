# Operating System Operations - Summary

## Key Definitions

- **Bootstrap**: The process of loading the operating system kernel into memory when a computer is powered on or reset
- **Dual-Mode Operation**: Processor execution mode supporting both user mode and kernel mode for protection
- **System Call**: A programmed procedure that allows user processes to request operating system services
- **Interrupt**: An asynchronous hardware signal requiring CPU attention for I/O or timing events
- **Exception**: A synchronous CPU-generated event during instruction execution (faults, traps, aborts)
- **Privileged Instructions**: Processor instructions that can only be executed in kernel mode
- **Timer**: Hardware component that generates periodic interrupts for CPU scheduling

## Important Formulas

- **System Call Execution Time**: T = T_mode_switch + T_service + T_return (typically 100-1000+ cycles)
- **Timer Interrupt Frequency**: f = 1/T_interval (commonly 100-1000 Hz for time-slicing)
- **Maximum Time Slice**: The timer interval determines the maximum continuous CPU time any process can receive

## Key Points

1. Bootstrap begins with BIOS/UEFI firmware, which initializes hardware and locates the boot loader
2. The boot loader loads the OS kernel into memory and transfers control to kernel initialization code
3. Dual-mode operation provides fundamental protection by separating user and kernel execution contexts
4. System calls are the only legitimate way for user programs to access protected operating system services
5. Interrupts enable asynchronous I/O operations without busy-waiting, improving CPU efficiency
6. The timer interrupt implements preemptive multitasking, preventing process monopolization of CPU
7. Exceptions handle synchronous error conditions like division by zero or page faults
8. All mode transitions involve saving processor state and switching to appropriate handler code
9. Kernel validates all system call parameters to prevent malicious or erroneous access to resources
10. Device drivers operate in kernel mode to provide hardware abstraction to user applications

## Common Mistakes

1. Confusing interrupts with exceptions - interrupts are external/async, exceptions are internal/sync
2. Believing system calls are just function calls - they involve critical mode transitions
3. Underestimating bootstrap complexity - it involves multiple stages of firmware and software
4. Forgetting that timer interrupts occur even when user processes are running normally
5. Assuming all operations can occur in user mode - only kernel mode can access hardware directly
6. Ignoring the security implications of dual-mode operation for system stability