# Registers in ARM Embedded Systems - Summary

## Key Definitions

- **General-Purpose Registers**: Thirteen 32-bit registers (R0-R12) used for data manipulation, function arguments, and return values following AAPCS conventions
- **Stack Pointer (SP)**: Register R13 that points to the current top of the stack; separate MSP and PSP instances support privileged and user contexts
- **Link Register (LR)**: Register R14 that stores the return address during subroutine calls (BL/BLX instructions)
- **Program Counter (PC)**: Register R15 that contains the address of the next instruction; PC = address + 8 in ARM state due to 3-stage pipeline
- **CPSR**: Current Program Status Register containing N, Z, C, V flags, processor mode bits, and state control (T, J) bits
- **SPSR**: Saved Program Status Register that preserves CPSR during exception handling
- **Banked Registers**: Physically separate register instances activated in specific processor modes for fast context switching

## Important Formulas

- PC offset in ARM state: PC_read = PC + 8
- PC offset in Thumb state: PC_read = PC + 4
- ARM register count: 37 registers in ARMv7 (13 GPRs + SP + LR + PC + CPSR + 5 SPSRs + banked variants)
- CPSR flag bits: N[31], Z[30], C[29], V[28]
- Mode bits: bits[4:0] encode processor mode

## Key Points

1. ARM provides 37 registers with uniform 32-bit width across the architecture
2. AAPCS defines R0-R3 for arguments/returns, R4-R11 callee-saved, R12 temporary, R13=SP, R14=LR, R15=PC
3. FIQ mode provides maximum banked registers (R8-R12) for high-speed interrupt handling
4. CPSR flags N, Z, C, V are updated by arithmetic/logical instructions with S suffix
5. SPSR automatically saves/restores processor state during exception entry/exit
6. Banked registers eliminate register save/restore overhead in exception handlers
7. The T bit in CPSR controls ARM (0) vs Thumb (1) instruction set state
8. Separate MSP and PSP Stack Pointers support secure embedded system designs

## Common Mistakes

1. Assuming PC points to the current instruction (actual: current instruction + 8 in ARM state)
2. Confusing User mode SP/LR with their banked counterparts in privileged modes
3. Forgetting that User and System modes lack SPSR registers
4. Incorrectly assuming all registers are available in all modes (banking must be considered)
5. Misremembering CPSR flag meanings, particularly C (carry) vs V (overflow) distinction
