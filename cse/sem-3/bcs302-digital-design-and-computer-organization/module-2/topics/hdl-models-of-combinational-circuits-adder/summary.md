# HDL Models of Combinational Circuits: Adders - Summary

## Key Definitions

- **Half Adder**: A combinational circuit that adds two single-bit binary numbers, producing sum and carry outputs.
- **Full Adder**: A circuit that adds three one-bit numbers (two significant bits and a carry-in), producing sum and carry-out.
- **Ripple Carry Adder (RCA)**: An n-bit adder formed by cascading n full adders where carry propagates sequentially.
- **Carry Look-Ahead Adder (CLA)**: An adder that computes carries in parallel using generate and propagate logic.
- **Generate (Gi)**: The condition where a carry is produced at position i, defined as Gi = Ai · Bi.
- **Propagate (Pi)**: The condition where a carry-in is propagated to carry-out, defined as Pi = Ai ⊕ Bi.

## Important Formulas

- **Half Adder Sum**: S = A ⊕ B
- **Half Adder Carry**: C = A · B
- **Full Adder Sum**: S = A ⊕ B ⊕ Cin
- **Full Adder Cout**: Cout = (A · B) + (Cin · (A ⊕ B))
- **Ripple Carry**: Ci+1 = Gi + (Pi · Ci)
- **n-bit Addition Result**: Sum = A + B (unsigned) or A + B (2's complement for signed)

## Key Points

1. Adders are fundamental building blocks for all arithmetic operations in digital systems.

2. Half adders cannot propagate carry from previous stages, limiting them to single-bit addition.

3. Full adders include carry-in input, enabling cascading for multi-bit arithmetic.

4. Behavioral HDL modeling describes functionality using truth tables or boolean equations.

5. Structural HDL modeling describes circuits as interconnected components (gate-level).

6. Ripple carry adders have simple structure but suffer from linear propagation delay O(n).

7. Carry look-ahead adders reduce delay to O(log n) by computing carries in parallel.

8. The generate-propagate concept is central to understanding fast adder architectures.

## Common Mistakes

1. **Confusing half adder with full adder**: Half adders have only 2 inputs, while full adders have 3 (including carry-in).

2. **Incorrect carry propagation**: Forgetting that the carry-out from one stage becomes the carry-in to the next in ripple carry adders.

3. **Neglecting propagation delay**: In exam questions, failing to consider the critical path delay when analyzing ripple carry adders.

4. **Mixing signed and unsigned**: Not accounting for overflow conditions when adding signed numbers in 2's complement representation.

5. **HDL syntax errors**: Common errors include using blocking assignments (=) instead of non-blocking (<=) in sequential contexts, or incorrect port mapping syntax.