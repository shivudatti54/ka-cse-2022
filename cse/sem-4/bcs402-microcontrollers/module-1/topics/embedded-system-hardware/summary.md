# Embedded System Hardware - Summary

## Key Definitions

- **ARM (Advanced RISC Machines)**: A family of RISC processor architectures widely used in embedded microcontrollers
- **CPSR (Current Program Status Register)**: A special register containing condition flags (N, Z, C, V), processor mode bits, and interrupt disable flags
- **AMBA (Advanced Microcontroller Bus Architecture)**: ARM's standardized bus protocol for connecting processor cores to memories and peripherals
- **NVIC (Nested Vectored Interrupt Controller)**: Integrated interrupt controller in Cortex-M processors supporting priority-based interrupt handling
- **Load-Store Architecture**: RISC principle where memory access and data processing are performed by separate instructions
- **Register Banking**: Hardware duplication of registers for different processor modes, enabling fast context switching

## Important Formulas

- **Stack frame size**: 8 registers × 4 bytes = 32 bytes (minimum for Cortex-M exception handling)
- **Memory access time**: (Setup cycles + Wait states + Hold cycles) × Clock period
- **Pipeline throughput**: 1 instruction per cycle (for single-cycle instructions in Cortex-M3)
- **Code density formula**: Thumb-2 provides ~25-30% better code density than 32-bit ARM instructions

## Key Points

1. ARM Cortex-M processors dominate embedded microcontrollers with their 3-stage pipeline (Cortex-M3) and integrated NVIC
2. The CPSR contains four condition flags: N (Negative), Z (Zero), C (Carry), V (Signed Overflow)—each reflecting specific arithmetic outcomes
3. ARM implements RISC design through load-store architecture, fixed-length 32-bit instructions, and single-cycle execution for most operations
4. The AMBA bus hierarchy uses AHB for high-speed transfers (memory, DMA) and APB for low-speed peripherals (UART, I2C, SPI)
5. Exception handling automatically stacks 8 registers (32 bytes), enabling fast context save/restore without software intervention
6. The NVIC supports up to 240 interrupts with configurable priority and vectored entry points
7. Power management in ARM microcontrollers offers multiple sleep modes to balance active performance against idle power consumption

## Common Mistakes

1. Confusing the V flag (signed overflow) with the C flag (unsigned carry)—these represent different arithmetic conditions
2. Assuming all ARM instructions execute in single cycle—memory access instructions (LDR, STR) require additional cycles depending on wait states
3. Forgetting that the PC is a banked register in ARM state, but is readable/writable as a normal register in Thumb state
4. Incorrectly calculating stack frame size—floating-point context saving adds significant overhead (64 additional bytes when FPCA is set)
5. Treating APB and AHB as interchangeable—APB's simpler protocol increases latency but reduces power consumption for low-speed peripherals