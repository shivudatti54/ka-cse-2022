# Assigning Interrupts in ARM Microcontrollers

## Table of Contents

- [Assigning Interrupts in ARM Microcontrollers](#assigning-interrupts-in-arm-microcontrollers)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Vector Table and Vector Table Offset Register (VTOR)](#vector-table-and-vector-table-offset-register-vtor)
  - [NVIC Register Architecture](#nvic-register-architecture)
  - [Priority Grouping and Priority Levels](#priority-grouping-and-priority-levels)
  - [IRQ and FIQ Assignment Differences](#irq-and-fiq-assignment-differences)
- [Examples](#examples)
  - [Example 1: Enabling a Timer Interrupt in Cortex-M](#example-1-enabling-a-timer-interrupt-in-cortex-m)
  - [Example 2: Configuring Priority Grouping for Nested Interrupts](#example-2-configuring-priority-grouping-for-nested-interrupts)
  - [Example 3: Relocating Vector Table to SRAM](#example-3-relocating-vector-table-to-sram)
- [Exam Tips](#exam-tips)

## Introduction

Interrupt assignment in ARM microcontrollers involves configuring the Nested Vectored Interrupt Controller (NVIC) to route interrupt requests (IRQs) to appropriate Interrupt Service Routines (ISRs). The NVIC, an integral part of the ARM Cortex-M processor, provides hardware support for interrupt handling with configurable priorities, nesting capabilities, and vector table management. Unlike simple microcontrollers with limited interrupt sources, ARM Cortex-M devices support up to 240 interrupts with programmable priority levels, enabling sophisticated real-time systems design.

The interrupt assignment process requires understanding the vector table structure, NVIC register programming, and priority grouping mechanisms. Modern ARM microcontrollers implement a memory-mapped register interface for the NVIC, allowing direct software configuration of interrupt behaviors. This module examines the theoretical foundations and practical procedures for assigning interrupts in ARM-based embedded systems, with emphasis on the Cortex-M architecture widely used in contemporary microcontroller applications.

## Key Concepts

### Vector Table and Vector Table Offset Register (VTOR)

The interrupt vector table is a memory structure containing the initial stack pointer and entry points for all exception handlers, including interrupts. In ARM Cortex-M processors, the vector table resides at address 0x00000000 during reset but can be relocated using the Vector Table Offset Register (VTOR) located at SCB->VTOR (address 0xE000ED08). The VTOR allows the vector table to be placed in flash, SRAM, or external memory based on application requirements.

The vector table entry format for Cortex-M consists of 4-byte entries: the first entry holds the initial Main Stack Pointer (MSP) value, while subsequent entries contain the address of each exception handler. For interrupt requests (IRQs), the table contains addresses of specific ISRs. The IRQ number reported by the NVIC relates to the vector table position as: IRQ 0 corresponds to vector table entry 16 (since exceptions 0-15 are reserved for processor exceptions).

### NVIC Register Architecture

The NVIC provides memory-mapped registers for interrupt configuration:

| Register                                | Address    | Function                                |
| --------------------------------------- | ---------- | --------------------------------------- |
| ISER (Interrupt Set-Enable Register)    | 0xE000E100 | Enable interrupts by writing IRQ number |
| ICER (Interrupt Clear-Enable Register)  | 0xE000E180 | Disable interrupts                      |
| ISPR (Interrupt Set-Pending Register)   | 0xE000E200 | Force interrupt to pending state        |
| ICPR (Interrupt Clear-Pending Register) | 0xE000E280 | Clear pending status                    |
| IP[0-59] (Interrupt Priority Register)  | 0xE000E400 | Set priority (8-bit per IRQ)            |

Each IRQ can be enabled by writing its interrupt number to the appropriate ISER register. The enable state is bit-mapped, so writing 1 to bit n enables IRQ n without affecting other interrupts.

### Priority Grouping and Priority Levels

The ARM Cortex-M NVIC implements a priority system where each interrupt has an 8-bit priority value (though implementations typically use fewer bits, e.g., 4 bits providing 16 levels). Lower numeric values indicate higher priority. The priority grouping mechanism divides the 8-bit priority field into group priority (preempt priority) and subpriority bits using the Application Interrupt and Reset Control Register (AIRCR) at address 0xE000ED0C.

The priority grouping is configured through bits [10:8] of the AIRCR register using the formula: Number of group priority bits = 7 - (AIRCR[10:8]). This determines how many bits control preemptive priority versus subpriority for tie-breaking among pending interrupts of equal group priority.

### IRQ and FIQ Assignment Differences

In ARM processors supporting both IRQ and FIQ (Fast Interrupt Request), the assignment mechanisms differ:

**IRQ Mode**: Standard interrupts are routed through the IRQ exception entry. The ISR address is obtained from the vector table, and the processor saves context automatically before executing the handler. IRQ handling supports nesting when higher-priority interrupts arrive during execution.

**FIQ Mode**: FIQ represents the highest-priority hardware interrupt with dedicated register banking (r8-r12), eliminating context save/restore overhead. FIQ has exclusive priority over IRQ and can preempt any IRQ handler. FIQ assignment requires configuring the interrupt source to generate FIQ instead of IRQ through peripheral control registers.

## Examples

### Example 1: Enabling a Timer Interrupt in Cortex-M

Consider a Cortex-M4 microcontroller where Timer2 generates IRQ 28. The following C code demonstrates interrupt assignment:

```c
// Define IRQ number for Timer2
#define TIM2_IRQn 28

// ISR implementation for Timer2
void TIM2_IRQHandler(void) {
 // Clear pending flag (device-specific)
 TIM2->SR &= ~TIM_SR_UIF;

 // User handler code
 // ...
}

// Main configuration function
void timer_interrupt_init(void) {
 // 1. Configure and enable Timer2 peripheral
 RCC->APB1ENR |= RCC_APB1ENR_TIM2EN;
 TIM2->PSC = 47999; // Prescaler for 1ms tick
 TIM2->ARR = 1000; // Auto-reload for 1 second
 TIM2->DIER |= TIM_DIER_UIE; // Enable update interrupt

 // 2. Set priority (lower number = higher priority)
 // IP[28] is at address 0xE000E400 + 28 = 0xE000E41C
 NVIC->IP[TIM2_IRQn] = 0x40; // Priority level 2 (shifted appropriately)

 // 3. Enable the interrupt in NVIC
 NVIC->ISER[0] = (1 << TIM2_IRQn); // Enable IRQ 28

 // 4. Start timer
 TIM2->CR1 |= TIM_CR1_CEN;
}
```

### Example 2: Configuring Priority Grouping for Nested Interrupts

This example demonstrates priority grouping configuration to enable interrupt nesting:

```c
void configure_priority_grouping(void) {
 // Read current AIRCR value
 uint32_t aircr = SCB->AIRCR;

 // Clear priority grouping bits and set new grouping
 // 0b010 = 2 group priority bits, 6 subpriority bits
 // This allows 4 distinct preemption levels
 aircr = (aircr & ~(0x07 << 8)) | (0x02 << 8) | (0x5FA << 16);
 SCB->AIRCR = aircr;

 // Now configure two interrupts with different priorities
 // Timer3 (IRQ 29) - High priority (preempts)
 NVIC->IP[29] = 0x00; // Highest priority (0x00)
 NVIC->ISER[0] = (1 << 29);

 // UART (IRQ 37) - Lower priority
 NVIC->IP[37] = 0xC0; // Lower priority (0xC0 with 2 group bits)
 NVIC->ISER[0] = (1 << 37);
}
```

### Example 3: Relocating Vector Table to SRAM

For bootloaders or dynamic ISR updating, vector table relocation is essential:

```c
#define SRAM_START 0x20000000
#define VTOR_OFFSET 0x1000 // Vector table at offset in SRAM

void relocate_vector_table_to_sram(void) {
 // 1. Copy vector table to SRAM location
 extern uint32_t _sidata, _sdata, _edata, _sbss, _ebss;
 uint32_t *src = &_sidata;
 uint32_t *dest = &_sdata;

 while (dest < &_edata) {
 *dest++ = *src++;
 }

 // 2. Clear bss
 dest = &_sbss;
 while (dest < &_ebss) {
 *dest++ = 0;
 }

 // 3. Set VTOR to new location
 SCB->VTOR = SRAM_START | VTOR_OFFSET;
}
```

## Exam Tips

1. **Remember the vector table base**: The vector table starts at 0x00000000 but can be relocated via VTOR (SCB->VTOR). The first entry is always the initial MSP.

2. **Priority encoding**: Lower priority numbers mean higher urgency. With 8 priority bits, understand how priority grouping affects preemption behavior.

3. **IRQ number calculation**: Exception number = IRQ number + 16. This is critical for understanding vector table positioning.

4. **Enable sequence**: To assign an interrupt, you must configure the peripheral, set priority in NVIC->IP, and enable in NVIC->ISER—in that order.

5. **FIQ vs IRQ distinction**: FIQ has dedicated registers (r8-r12) and cannot be masked by the I bit in CPSR, making it suitable for time-critical handlers.

6. **Pending register usage**: The ISPR allows software to trigger an interrupt for testing or synchronization purposes without the actual hardware event.

7. **Remember bit-band aliasing**: In Cortex-M, NVIC registers can be accessed via bit-band aliasing for atomic bit operations, useful in bare-metal interrupt management.
