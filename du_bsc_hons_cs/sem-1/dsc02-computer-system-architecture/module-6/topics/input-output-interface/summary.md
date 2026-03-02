# Input-Output Interface - Summary

## Key Definitions and Concepts

- **I/O Interface**: Hardware and software components that facilitate communication between the CPU and peripheral devices, resolving differences in speed, data format, and operating characteristics.

- **I/O Controller**: Specialized hardware circuit that manages communication between CPU and I/O devices, containing data, status, and control registers along with interrupt logic.

- **Programmed I/O**: I/O technique where CPU actively polls device status registers to check for data availability, resulting in inefficient CPU utilization.

- **Interrupt-Driven I/O**: Technique where I/O devices notify the CPU via interrupt signals when attention is required, allowing CPU to perform other tasks productively.

- **DMA (Direct Memory Access)**: High-performance I/O technique where a DMA controller transfers data directly between I/O devices and memory without CPU intervention.

- **Spooling**: Buffering technique that stores output data (typically print jobs) on disk before sending to slow output devices, enabling batch processing and queue management.

## Important Formulas and Theorems

- **DMA Transfer Time** = Data Size / Device Transfer Rate
- **CPU Time with DMA** = (Number of Transfers × DMA Cycles per Transfer) / Clock Frequency
- **CPU Time with Programmed I/O** = (Number of Transfers × CPU Cycles per Transfer) / Clock Frequency
- **Interrupt Overhead** = Interrupt Frequency × ISR Execution Time

## Key Points

- I/O interfaces resolve mismatches in speed, data format, and control signaling between fast CPU/memory and diverse peripheral devices.

- An I/O controller serves as the intermediary, containing registers for data, status, and control functions, plus interrupt generation logic.

- Programmed I/O is simple but inefficient; CPU continuously polls devices wasting cycles that could execute useful instructions.

- Interrupt-driven I/O dramatically improves CPU efficiency by allowing the processor to work on other tasks until an interrupt signals device attention.

- DMA provides the highest performance for bulk transfers by bypassing the CPU entirely, letting data flow directly between devices and memory.

- Three DMA modes exist: burst mode (blocks CPU until transfer complete), cycle stealing (interleaves with CPU), and transparent mode (waits for idle cycles).

- Modern systems predominantly use serial communication (USB, PCIe, SATA) over older parallel interfaces due to superior speed and reduced signal integrity issues.

- Buffering smooths speed differences between devices, while spooling specifically handles output to slow devices like printers by using disk as an intermediate storage.

## Common Mistakes to Avoid

- Confusing polling with interrupt-driven I/O; polling is active waiting (CPU checks repeatedly), while interrupts are passive (CPU responds when notified).

- Assuming DMA completely eliminates CPU involvement; CPU still initiates transfers and handles completion interrupts.

- Believing serial communication is always slower than parallel; at high speeds, parallel suffers from clock skew making serial more efficient.

- Overlooking that interrupt service routines must save and restore CPU state to correctly resume interrupted programs.

- Ignoring the role of I/O controllers in addressing—the CPU doesn't access devices directly but through controller registers.

## Revision Tips

- Create a comparison table of the three I/O techniques covering CPU involvement, hardware complexity, speed, advantages, disadvantages, and suitable applications.

- Memorize the sequence of interrupt handling: IRQ → Interrupt Acknowledge → Vector Fetch → Save State → Execute ISR → Restore State → Return.

- Practice numerical problems on DMA transfer time calculations, as these are frequently asked in DU examinations.

- Understand why modern interfaces (USB, PCIe) use serial communication despite parallel being conceptually simpler.

- Review previous years' question papers to identify the most commonly asked concepts and problem types in this module.