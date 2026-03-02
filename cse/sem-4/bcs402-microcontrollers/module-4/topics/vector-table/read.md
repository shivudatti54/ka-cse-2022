# Vector Table in ARM Cortex-M Microcontrollers

## Table of Contents

- [Vector Table in ARM Cortex-M Microcontrollers](#vector-table-in-arm-cortex-m-microcontrollers)
- [Introduction](#introduction)
- [Theoretical Foundation](#theoretical-foundation)
  - [Why the First Entry Must Be the Main Stack Pointer](#why-the-first-entry-must-be-the-main-stack-pointer)
  - [Vector Table Structure and Memory Layout](#vector-table-structure-and-memory-layout)
  - [Vector Table Alignment Requirements](#vector-table-alignment-requirements)
- [Vector Table Offset Register (VTOR)](#vector-table-offset-register-vtor)
  - [VTOR Register Structure](#vtor-register-structure)
  - [Code Example: Vector Table Relocation to SRAM](#code-example-vector-table-relocation-to-sram)
- [Comparison: Cortex-M vs ARM7/ARM9 Vector Tables](#comparison-cortex-m-vs-arm7arm9-vector-tables)
- [Linker Script Considerations](#linker-script-considerations)
- [Summary](#summary)

## Introduction

The vector table constitutes a critical architectural component in ARM Cortex-M processors, serving as the foundational mechanism for exception and interrupt handling. Upon power-on or reset, the microcontroller requires deterministic knowledge of entry points for all exception handlers, ranging from the initial reset vector to runtime interrupts originating from peripheral devices. The vector table fulfills this requirement by storing memory addresses of exception handlers at a predefined memory location, enabling the processor to automatically branch to appropriate service routines when exceptions occur.

The ARM Cortex-M architecture implements a fundamentally different vector table approach compared to its predecessor architectures (ARM7/ARM9). While ARM7/ARM9 utilize instruction-based vector tables containing actual branch instructions at each vector location, Cortex-M employs an address-based vector table storing 32-bit function pointers. This design evolution provides substantial advantages: reduced vector table size, elimination of position-independent code constraints, and enablement of runtime vector table relocation through the Vector Table Offset Register (VTOR). Understanding this architectural distinction is essential for embedded systems developers working with modern microcontrollers such as STM32, Tiva C, and NXP LPC1768.

## Theoretical Foundation

### Why the First Entry Must Be the Main Stack Pointer

The ARM Cortex-M architecture mandates that the first vector table entry (offset 0x0000) contains the initial Main Stack Pointer (MSP) value. This requirement stems from fundamental architectural constraints: upon reset, the processor immediately requires a valid stack pointer before executing any instruction, including the reset handler itself. Unlike other processors where stack setup occurs within the reset handler, Cortex-M processors must have MSP pre-initialized to enable proper exception handling from the moment execution begins.

**Proof**: When a reset exception occurs (exception number 1), the processor automatically loads the MSP from memory location 0x00000000 before fetching the reset handler address from 0x00000004. This two-step process ensures that stack space is available for any exception that might occur during reset handler execution, including nested interrupts. If the MSP were not pre-initialized, the processor could not safely push exception frames onto the stack, making reliable interrupt handling impossible.

### Vector Table Structure and Memory Layout

The ARM Cortex-M vector table is an array of 32-bit word entries stored in flash memory at a configurable base address. For STM32 microcontrollers, the default flash memory location is 0x08000000, though the actual vector table is often remapped to 0x00000000 by the memory controller for compatibility. The structure follows a strict ordering defined by the ARMv7-M architecture:

```
Offset (hex) | Entry | Description
----------------|--------------------------------|---------------------------
0x0000 | Initial MSP | Stack pointer initial value
0x0004 | Reset Handler | Program entry point
0x0008 | NMI Handler | Non-Maskable Interrupt
0x000C | Hard Fault Handler | Hardware fault handler
0x0010 | Memory Management Fault | MPU violation handler
0x0014 | Bus Fault Handler | Bus error handler
0x0018 | Usage Fault Handler | Programming error handler
0x001C-0x0028 | Reserved | Future architectural use
0x002C | SVCall Handler | Supervisor call (SVC)
0x0030 | Debug Monitor | Debug breakpoint handler
0x0034 | Reserved | Architectural reserved
0x0038 | PendSV Handler | Pendable service call
0x003C | SysTick Handler | System timer interrupt
0x0040+ | External IRQs (IRQ0-IRQn) | Peripheral interrupts
```

### Vector Table Alignment Requirements

The ARM Cortex-M architecture imposes specific alignment constraints on the vector table base address, governed by the formula: Alignment = 2^(N+1) bytes, where N represents the number of bits required to encode the total number of interrupts supported by the implementation.

**Derivation**: The processor uses the lower bits of the vector table address as an index into the table when handling interrupts. For a system supporting I external interrupts, the required number of bits is ⌈log₂(I+16)⌉, accounting for the 16 system exceptions. The alignment requirement ensures that the table base address does not conflict with these index bits.

**Example Calculations**:

- For Cortex-M3 with 32 external interrupts: bits required = ⌈log₂(32+16)⌉ = ⌈log₂48⌉ = 6; alignment = 2^(6+1) = 128 bytes
- For Cortex-M4 with maximum 240 external interrupts: bits required = ⌈log₂(240+16)⌉ = ⌈log₂256⌉ = 8; alignment = 2^(8+1) = 512 bytes

## Vector Table Offset Register (VTOR)

The VTOR (address: 0xE000ED08) provides runtime relocation capability for the vector table, enabling flexible memory management in bootloader applications and systems requiring dynamic interrupt handler modification.

### VTOR Register Structure

```
Bits | Name | Function
--------|------------|--------------------------------
31:9 | TBLOFF | Vector table base offset (aligned to vector table alignment)
8:0 | Reserved | Reserved for future use
```

**Critical Note**: The TBLOFF field contains bits [31:9], meaning the offset must be a multiple of the vector table alignment requirement. Writing a non-aligned value results in unpredictable behavior.

### Code Example: Vector Table Relocation to SRAM

```c
#define VTOR_ADDR (*(volatile uint32_t *)0xE000ED08)

// Vector table in SRAM - must be aligned per architecture requirements
typedef void (*vector_table_entry_t)(void);

extern uint32_t _sstack; // End of stack from linker script

// Declare handler functions
void Reset_Handler(void);
void NMI_Handler(void);
void HardFault_Handler(void);
void SysTick_Handler(void);
void GPIO_IRQHandler(void);

// External interrupt handlers
void WWDG_IRQHandler(void) __attribute__((weak, alias("Default_Handler")));
void PVD_IRQHandler(void) __attribute__(__weak, alias("Default_Handler")));
// ... other handlers

// SRAM vector table
vector_table_entry_t sram_vector_table[] __attribute__((section(".sram_vector_table"))) = {
 (vector_table_entry_t)(&_sstack), // Initial MSP
 (vector_table_entry_t)(Reset_Handler),
 (vector_table_entry_t)(NMI_Handler),
 (vector_table_entry_t)(HardFault_Handler),
 // ... complete table
};

void relocate_vector_table_to_sram(void) {
 // Calculate aligned base address for SRAM vector table
 uint32_t sram_vector_base = (uint32_t)&sram_vector_table;

 // Ensure alignment per vector table requirements
 // For 240 interrupts: align to 512 bytes
 sram_vector_base = (sram_vector_base + 511) & ~511;

 // Configure VTOR to point to SRAM vector table
 VTOR_ADDR = sram_vector_base;

 // Verify configuration
 if (VTOR_ADDR != sram_vector_base) {
 // Handle alignment error
 while(1);
 }
}
```

## Comparison: Cortex-M vs ARM7/ARM9 Vector Tables

| Aspect                | ARM7/ARM9 (ARMv4T-v5TE)      | ARM Cortex-M (ARMv7-M)     |
| --------------------- | ---------------------------- | -------------------------- |
| Vector Table Location | Fixed at 0x00000000          | Configurable via VTOR      |
| Entry Content         | Branch instructions (LDR/PC) | 32-bit function addresses  |
| Vector Table Size     | 32 bytes (8 vectors)         | Variable (depends on IRQs) |
| Reset Vector          | Instruction at 0x00000000    | Address at 0x00000004      |
| Stack Initialization  | Manual in reset handler      | Automatic from table entry |
| Relocation Support    | Not supported                | Supported via VTOR         |
| Exception Priority    | Fixed priorities             | Configurable priorities    |

The address-based approach in Cortex-M eliminates the need for position-independent code at vector locations, as the linker resolves actual handler addresses at link time rather than requiring runtime calculation.

## Linker Script Considerations

Proper linker script configuration is essential for correct vector table placement. The following linker script fragment demonstrates the required sections:

```ld
MEMORY
{
 FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 256K
 RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 64K
}

SECTIONS
{
 .isr_vector :
 {
 . = ALIGN(512); /* Ensure required alignment */
 KEEP(*(.vectors))
 . = ALIGN(4);
 } >FLASH

 .text :
 {
 *(.text*)
 } >FLASH

 .data :
 {
 _sdata = .;
 *(.data*)
 _edata = .;
 } >RAM AT>FLASH

 / _sidata = LOADADDR(.data);
}
```

## Summary

The vector table in ARM Cortex-M microcontrollers represents a sophisticated evolution from earlier ARM architectures, providing address-based exception handling with configurable base locations. Key architectural features include automatic MSP initialization from the first table entry, configurable exception priorities, and runtime relocation capability through VTOR. Understanding these mechanisms is fundamental for embedded systems developers, particularly those working with bootloader architectures or applications requiring dynamic interrupt handler modification.
