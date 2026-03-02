# Binary Adder-Subtractor - Summary

## Key Definitions

**Half Adder:** A combinational circuit that adds two single-bit binary numbers A and B, producing sum (S = A ⊕ B) and carry (C = A · B) outputs. Cannot handle carry-in from previous stages.

**Full Adder:** A combinational circuit that adds three single-bit inputs (A, B, C_in), producing Sum (S = A ⊕ B ⊕ C_in) and Carry-out (C_out = AB + (A ⊕ B)C_in). Can be constructed from two half adders and one OR gate.

**Ripple Carry Adder:** An n-bit parallel adder constructed by cascading n full adders, where each stage's carry-out feeds the next stage's carry-in. Suffers from O(n) propagation delay.

**Carry Lookahead Adder (CLA):** An improved adder architecture that computes carries in parallel using generate (G = AB) and propagate (P = A ⊕ B) functions, achieving O(1) delay independent of operand width.

**Two's Complement Subtraction:** Method of performing subtraction A - B by computing A + B' + 1, where B' is the one's complement of B.

**Adder-Subtractor:** Unified circuit that performs both addition and subtraction using a mode control input M. When M=0, performs A+B; when M=1, performs A-B using two's complement.

**Overflow:** Condition in signed arithmetic when the result exceeds the representable range. Detected by V = C_n ⊕ C_(n-1), where C_n is carry-out from MSB and C_(n-1) is carry-in to MSB.

## Key Equations

| Circuit | Sum Output | Carry Output |
|---------|------------|--------------|
| Half Adder | S = A ⊕ B | C = A · B |
| Full Adder | S = A ⊕ B ⊕ C_in | C_out = AB + (A ⊕ B)C_in |
| CLA Stage | S = P ⊕ C_in | C_out = G + P · C_in |

## Key Formulas

**Ripple Carry Delay:** T_rc = n × t_fa (n stages, t_fa = full adder delay)

**CLA Delay:** T_cla = 2t_gate + t_AND + t_OR (constant, typically 2-3 gate delays)

**Overflow Detection:** V = C_n ⊕ C_(n-1)

## Key Diagrams

- Half adder: XOR gate for sum, AND gate for carry
- Full adder: Two half adders cascaded with OR gate for carry-out
- 4-bit adder-subtractor: Four full adders with XOR gates on B inputs, mode control M connected to XOR gates and initial carry

## Assessment Questions

### Recall (Basic)
1. What are the two outputs of a half adder called?
2. How many full adders are required to build a 4-bit ripple carry adder?

### Application (Intermediate)
3. Implement a full adder using NAND gates only.
4. For a 4-bit adder with A=1011 and B=0101, determine the output sum when M=0 (addition mode).

### Analysis (Advanced)
5. A 16-bit ripple carry adder has a full adder propagation delay of 20ns. Calculate the maximum delay for adding two numbers. If we replace it with a 4-bit CLA blocks, what would be the approximate improvement in delay?
6. For the addition 0111 (+7) + 0010 (+2) in 4-bit signed arithmetic, determine whether overflow occurs and explain why.