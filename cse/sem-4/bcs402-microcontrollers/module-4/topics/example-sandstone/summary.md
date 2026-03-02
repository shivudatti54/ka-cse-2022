# Example Sandstone - Firmware Implementation Summary

## Key Definitions

- **Bootloader**: Primary firmware component that initializes the system and loads the main application program into memory
- **Vector Table**: Memory structure containing exception and interrupt handler addresses for ARM processors
- **Flash Memory**: Non-volatile memory used to store firmware code and persistent data in microcontrollers
- **Stack Pointer**: Register that points to the top of the current stack frame in memory
- **FIQ (Fast Interrupt Request)**: High-priority interrupt mechanism in ARM processors with reduced latency

## Important Formulas

- **Stack Size Calculation**: `Total Stack = Main Stack + Process Stack + Interrupt Nesting Margin`
- **Flash Endurance**: Typical specification is 10,000 to 100,000 program/erase cycles
- **Interrupt Latency**: Time from interrupt request to first instruction of handler execution

## Key Points

- Example Sandstone demonstrates a complete firmware framework for ARM microcontroller initialization
- The reset handler must initialize the stack pointer before any other code execution
- Vector table placement determines the memory address where the processor looks for exception handlers
- Bootloader firmware performs hardware initialization, integrity checks, and application loading
- Memory partitioning between bootloader and application enables secure firmware updates
- Watchdog timers provide recovery mechanisms when firmware enters undefined states
- Flash programming requires an erase cycle before new data can be written
- FIQ handlers receive priority treatment and can preempt IRQ handlers in ARM processors
- Linker scripts define the physical memory layout and placement of code and data sections

## Common Mistakes

1. **Forgetting stack initialization**: Failing to initialize the stack pointer before function calls causes unpredictable behavior or hard faults

2. **Incorrect vector table placement**: Placing the vector table at the wrong memory address prevents exception handling from working correctly

3. **Ignoring flash timing requirements**: Not adhering to flash erase/program timing specifications can corrupt memory or cause operation failures

4. **Neglecting watchdog configuration**: Disabling watchdogs without implementing alternative error recovery can leave the system in a non-recoverable state

5. **Assuming continuous memory**: Treating flash memory as RAM and attempting to write without the proper erase-before-program sequence