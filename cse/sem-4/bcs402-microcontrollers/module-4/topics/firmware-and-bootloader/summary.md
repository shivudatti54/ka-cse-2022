# Firmware and Bootloader - Summary

## Key Definitions and Concepts

- **Firmware:** Specialized software stored in non-volatile memory (ROM/Flash) that provides low-level control for hardware devices and is closely tied to specific hardware configurations.

- **Bootloader:** A small program stored in protected memory that executes after power-on/reset, initializes hardware, validates application firmware, and loads the main application into memory before transferring control to it.

- **Flash Memory:** Non-volatile memory technology used to store firmware, requiring page/sector-based erasure and specific programming sequences.

- **In-Application Programming (IAP):** Method where the running application updates its own firmware in flash memory.

- **In-System Programming (ISP):** Method of programming flash memory using external programming hardware while the chip is installed in the system.

- **Vector Table:** Memory structure containing reset handlers and interrupt service routine addresses used by the processor on startup.

## Important Formulas and Theorems

- **Flash Write Cycle:** Typically 10,000-100,000 cycles, limiting the number of firmware updates
- **UART Bootloader Standard Baud Rate:** 9600-115200 bps for reliable programming
- **Memory Address Alignment:** ARM Cortex-M requires word-aligned (4-byte) flash writes

## Key Points

- Bootloader resides in protected memory region to prevent accidental erasure during application updates
- Boot sequence: Power On/Reset → Bootloader Init → Validate App → Load to RAM → Jump to App
- Firmware is stored in non-volatile memory (Flash/ROM) and directly interacts with hardware peripherals
- UART bootloader is most common due to simplicity and ubiquity of serial interfaces
- Application jump requires proper stack pointer setup and vector table configuration
- Flash memory uses sector/page-based erasure, requiring erase before write operations
- Bootloaders can support field firmware updates without specialized programming hardware
- Watchdog timer management is critical in bootloader to prevent unwanted resets during long operations
- Digital signatures and checksums provide security and integrity verification for firmware updates

## Common Mistakes to Avoid

1. **Incorrect Stack Pointer Configuration:** Failing to properly set the stack pointer from the application's vector table before jumping can cause immediate crashes.

2. **Ignoring Flash Timing Requirements:** Flash memory has specific erase/write timing requirements; ignoring these leads to programming failures.

3. **Not Validating Application Integrity:** Bootloaders must verify application checksum/signature before executing to prevent running corrupted code.

4. **Improper Vector Table Relocation:** For ARM Cortex-M, forgetting to update VTOR when jumping to application causes interrupt handling failures.

5. **Memory Overlap:** Bootloader and application memory regions must not overlap; always verify memory boundaries during design.

## Revision Tips

1. Draw the complete memory map of a typical microcontroller showing bootloader, application, and data regions.

2. Practice writing the application jump function including stack pointer setup and interrupt disabling.

3. Remember the exact boot sequence order and be able to explain each step in detail.

4. Know the differences between ISP, IAP, and bootloader-based programming methods.

5. Review flash memory characteristics: erase granularity, write timing, and endurance limitations.
