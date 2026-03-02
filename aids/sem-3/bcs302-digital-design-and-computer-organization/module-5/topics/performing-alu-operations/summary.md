# Performing ALU Operations - Summary

## Key Definitions

- **ALU (Arithmetic Logic Unit)**: The combinational circuit within a processor that performs all arithmetic (addition, subtraction, multiplication, division) and logical (AND, OR, XOR, NOT) operations.

- **Ripple-Carry Adder (RCA)**: An n-bit adder constructed from n full adders cascaded together, where each full adder's carry output feeds the next stage's carry input.

- **Two's Complement Subtraction**: Method of computing A - B by computing A + B' + 1, where B' is the bitwise complement of B.

- **Status Flags**: Condition bits set by ALU operations—Zero (Z), Carry (C), Overflow (V), and Negative (N)—stored in the Program Status Word.

- **Register Transfer**: High-level notation (e.g., R[d] ← R[s] + R[t]) specifying the movement and transformation of data between processor registers.

## Important Formulas

- **Full Adder Sum**: Sᵢ = Aᵢ ⊕ Bᵢ ⊕ Cᵢ

- **Full Adder Carry**: Cᵢ₊₁ = AᵢBᵢ + Cᵢ(Aᵢ ⊕ Bᵢ)

- **Overflow Detection**: V = Cₙ ⊕ Cₙ₋₁ (carry into MSB XOR carry out of MSB)

- **Two's Complement**: A - B = A + B' + 1 (where B' is inverted B)

- **ALU Result Selection**: Result = S₁S₀' × (Arithmetic) + S₁S₀ × (Logic)

## Key Points

1. ALU is a pure combinational circuit with no internal state—outputs depend solely on current inputs.

2. The arithmetic circuit uses ripple-carry adders where the critical path delay increases linearly with bit-width.

3. Subtraction is implemented by adding the two's complement (inverting B and setting carry-in to 1).

4. Multiplexers select between parallel computation paths—one for arithmetic, one for logic operations.

5. Zero flag enables equality comparison; after subtraction, Z=1 indicates operands are equal.

6. Carry flag indicates unsigned overflow; Overflow flag indicates signed overflow.

7. ALU control signals derive from instruction opcode and function fields through the control unit.

8. The datapath routes operands from register file through ALU back to register file during execute phase.

9. Timing: ALU propagation delay determines minimum clock period in non-pipelined processors.

## Common Mistakes

1. **Confusing Carry and Overflow Flags**: Carry flag indicates unsigned overflow (for A + B when result exceeds 2ⁿ⁻¹), while Overflow flag indicates signed overflow (when result exceeds +2ⁿ⁻¹-1 or falls below -2ⁿ⁻¹).

2. **Incorrect Subtraction Implementation**: Remember that A - B requires setting the carry-in to 1, not 0, to complete the two's complement conversion.

3. **Assuming ALU Stores State**: Students sometimes forget ALU is combinational—it has no memory of previous operations.

4. **Neglecting Propagation Delay**: In timing analysis, the ripple-carry adder delay is n times the full adder delay, not constant.

5. **Misinterpreting Negative Flag**: N = 1 simply means the MSB is 1 in two's complement representation; it does not necessarily indicate an error.