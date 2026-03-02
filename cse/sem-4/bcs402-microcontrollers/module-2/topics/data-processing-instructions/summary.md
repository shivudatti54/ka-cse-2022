# Data Processing Instructions in 8051 - Summary

## Key Definitions
- **Accumulator (A)**: Primary 8-bit register for arithmetic and logical operations in 8051
- **Program Status Word (PSW)**: SFR at address 0xD0 containing C, AC, OV, and P flags
- **Addressing Mode**: Method by which instructions specify operand locations (register, direct, indirect, immediate)
- **BCD (Binary-Coded Decimal)**: Number representation where each decimal digit is stored in 4 bits
- **Bit-addressable RAM**: Internal RAM addresses 0x20-0x2F where each bit can be individually accessed

## Important Formulas
- **ADD**: A = A + src; C = carry out of bit 7; AC = carry out of bit 3; OV = carry out of bit 6 XOR carry out of bit 7
- **ADDC**: A = A + src + C; same flag rules as ADD
- **SUBB**: A = A - src - C; C = 1 if src + C > A (borrow)
- **MUL AB**: B:A = A × B (16-bit result); OV = (B ≠ 0); C = 0 always
- **DA A**: If AC=1 or (A[3:0] > 9), add 0x06; if C=1 or (A[7:4] > 9), add 0x60

## Key Points
1. The 8051 instruction set provides 8 arithmetic, 6 logical, 4 rotate, 1 swap, and multiple boolean instructions for data manipulation.
2. The Accumulator serves as the implicit operand for most data processing instructions, with destination usually being the Accumulator itself.
3. ADD affects C, AC, and OV flags based on unsigned and signed overflow conditions; INC/DEC affect AC but not C.
4. ADDC is essential for multi-byte arithmetic to propagate carries between bytes.
5. Logical instructions (ANL, ORL, XRL) clear C and AC flags; they operate bit-wise on operands.
6. Rotate instructions RL/RR exclude Carry, while RLC/RRC use Carry as a ninth bit, enabling multi-byte shifts.
7. DA A corrects binary addition results to valid BCD representation after BCD+BCD operations.
8. Boolean instructions operate on 128 individually addressable bits in internal RAM and specific SFR bits.
9. MUL and DIV are unsigned operations; signed multiplication requires software implementation.
10. The Carry flag serves dual roles: as overflow indicator for unsigned arithmetic and as temporary storage for rotate-through-carry operations.

## Common Mistakes
1. **Using ADD instead of ADDC**: Failing to use ADDC when adding multi-byte numbers loses carries from previous byte additions.
2. **Forgetting DA after BCD addition**: Adding BCD numbers without DA produces invalid BCD results (e.g., 0x5E instead of 0x64).
3. **Confusing rotate instructions**: Using RL when RLC is needed, or forgetting that RL/RR don't involve the Carry flag.
4. **Incorrect flag expectations**: Assuming logical operations affect C; they always clear C and AC in 8051.
5. **Bit-addressing confusion**: Attempting to access bits outside 0x20-0x2F range or non-bit-addressable SFRs using bit instructions.
6. **MUL/DIV register confusion**: Forgetting that MUL places high byte in B (not A), and DIV places remainder in B (not A).