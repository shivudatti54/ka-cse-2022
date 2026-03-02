# Interrupts in Microcontrollers - Summary

## Key Definitions and Concepts

- **Interrupt**: A mechanism that temporarily suspends normal program execution to handle time-critical events, allowing the CPU to respond immediately to peripheral requests
- **Interrupt Service Routine (ISR)**: A special function executed in response to an interrupt, stored at the designated vector address
- **Interrupt Vector**: Fixed memory address where the CPU jumps when a specific interrupt is acknowledged
- **Interrupt Latency**: The time delay between interrupt request and start of ISR execution
- **Polling**: Continuous monitoring of peripherals by CPU, as opposed to interrupt-driven event handling

## Important Vector Addresses

| Interrupt Source           | Vector Address |
| -------------------------- | -------------- |
| External Interrupt 0 (IE0) | 0003H          |
| Timer 0 Overflow (TF0)     | 000BH          |
| External Interrupt 1 (IE1) | 0013H          |
| Timer 1 Overflow (TF1)     | 001BH          |
| Serial Port (RI/TI)        | 0023H          |

## Key Points

- The 8051 provides 5 interrupt sources: 2 external, 2 timer, and 1 serial port
- IE register (A8H): EA must be set along with individual enable bits (EA, ES, ET1, EX1, ET0, EX0)
- IP register (B8H): Sets priority (PS, PT1, PX1, PT0, PX0) - higher priority interrupts preempt lower ones
- The CPU automatically saves only the Program Counter (PC); other registers must be manually saved in ISR
- Use `RETI` instruction to return from ISR, not `RETI`
- External interrupts can be edge-triggered (ITx=1) or level-triggered (ITx=0)
- In Keil C, the `interrupt` keyword specifies the vector number (0-4)

## Common Mistakes to Avoid

1. **Forgetting to set EA bit**: Setting individual interrupt enable bits without EA=1 means no interrupts will trigger
2. **Using RET instead of RETI**: This prevents proper restoration of interrupt status and causes undefined behavior
3. **Not reloading Timer in Mode 1**: Timer 0 in Mode 1 does not auto-reload; values must be reloaded in ISR
4. **Exceeding 8-byte vector space**: Complex ISRs should use LJMP at vector address to redirect to larger memory
5. **Not clearing interrupt flags**: Serial port and timer overflow flags must be cleared in ISR before returning

## Revision Tips

- Memorize the vector table - this is frequently asked in university exams
- Practice writing complete C programs with timer and external interrupts
- Remember the format of IE and IP registers - draw them out repeatedly
- Understand that multiple interrupts of same priority are handled in fixed order: IE0 > TF0 > IE1 > TF1 > RI/TI
- Review the difference between edge-triggered and level-triggered external interrupts
