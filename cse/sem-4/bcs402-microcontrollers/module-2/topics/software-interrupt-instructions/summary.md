# Software Interrupt Instructions - Summary

## Key Definitions

- **Software Interrupt**: An interrupt explicitly triggered by executing a dedicated instruction in program code, used for system calls, debugging, and OS services

- **TRAP Interrupt**: The 8051's software interrupt mechanism with vector address 0x0023

- **SWI (Software Interrupt)**: ARM instruction that triggers Supervisor mode for operating system service calls

- **Interrupt Vector Table**: Fixed memory locations containing addresses of interrupt service routines for each interrupt source

- **RETI Instruction**: Return from Interrupt instruction that restores PC and signals interrupt completion to hardware

## Important Formulas

- **8051 Stack Depth for Interrupt**: SP_before - SP_after = 3 bytes (2 for PC, 1 for PSW)

- **Total Stack Required**: Base stack + (maximum nesting depth × 3) bytes for 8051

- **Interrupt Latency**: Completion of current instruction + hardware save sequence (typically 2-4 machine cycles in 8051)

## Key Points

- Software interrupts differ from subroutine calls (ACALL/LCALL) in that they trigger full interrupt handling sequence including PSW save and mode change

- The 8051 TRAP interrupt has fixed vector address 0x0023 and is non-maskable at the individual level but can be globally disabled via EA bit

- The IE register (0xA8) controls interrupt enable/disable with EA bit (bit 7) providing global interrupt control

- RETI must be used instead of RET for returning from interrupt service routines to properly signal interrupt completion

- ARM SWI instruction provides system call mechanism with 24-bit immediate field for service identification

- Proper stack pointer initialization is critical before enabling interrupts to prevent stack corruption

- Software interrupt handling saves PC and PSW automatically; additional registers must be saved by the ISR if used

## Common Mistakes

1. **Confusing ACALL/LCALL with software interrupts**: These are subroutine calls that do not trigger interrupt handling sequences or save PSW

2. **Using RET instead of RETI**: This prevents proper nested interrupt handling and leaves interrupt system in incorrect state

3. **Forgetting to initialize stack pointer**: Uninitialized SP leads to stack corruption when interrupts occur

4. **Not setting EA bit**: Individual interrupt enables require global enable bit EA to be set first

5. **Incorrect vector address**: TRAP vector is 0x0023, not to be confused with other interrupt vectors like 0x0003 (INT0) or 0x0013 (INT1)