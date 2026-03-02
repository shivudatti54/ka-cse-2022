# Digital Logic Gates - Summary

## Key Definitions and Concepts

- **Logic Gate**: An electronic circuit that performs a specific logical operation on one or more binary inputs to produce a binary output.

- **Boolean Variable**: A binary variable that can have only two values: 0 (FALSE) or 1 (TRUE).

- **Truth Table**: A tabular representation showing all possible input combinations and their corresponding outputs for a logic gate or circuit.

- **Universal Gate**: A gate that can implement any Boolean function without requiring any other type of gate. NAND and NOR are universal gates.

## Important Formulas and Theorems

**Basic Gate Functions:**
- NOT: Y = Ā (inverts input)
- AND: Y = A · B = AB (output 1 only when ALL inputs are 1)
- OR: Y = A + B (output 1 when AT LEAST ONE input is 1)
- NAND: Y = (AB)̄ (universal gate)
- NOR: Y = (A + B)̄ (universal gate)
- XOR: Y = A ⊕ B = A·B̄ + Ā·B (output 1 when inputs are DIFFERENT)
- XNOR: Y = A ⊙ B = (A ⊕ B)̄ (output 1 when inputs are SAME)

**Gate Counting:**
- NOT requires 1 gate
- AND/OR requires 1 gate for 2 inputs
- XOR/XNOR requires multiple gates when built from basic gates

## Key Points

- All digital circuits ultimately consist of combinations of basic logic gates.

- NAND and NOR are called universal gates because any Boolean function can be implemented using only NAND gates or only NOR gates.

- XOR gate produces 1 when exactly one input is 1 (odd number of 1s for multiple inputs).

- XNOR is the complement of XOR; it produces 1 when all inputs are equal.

- AND operation is similar to multiplication; OR operation is similar to logical addition (but NOT arithmetic).

- Gates can have multiple inputs: AND requires all inputs HIGH, OR requires at least one input HIGH.

- Two different symbol standards exist: traditional distinctive-shape and IEEE/ANSI rectangular symbols.

## Common Mistakes to Avoid

- Confusing OR with XOR: OR gives 1 for ANY input = 1; XOR gives 1 only for EXACTLY ONE input = 1.

- Forgetting that NAND and NOR produce complemented outputs compared to AND and OR.

- Incorrectly wiring complements: Remember that AND of A and NOT B requires separate NOT gate for B.

- Assuming gates have no delay: Real gates have propagation delays, though idealized logic ignores this.

- Mixing up bubble notation: Small circles (bubbles) at gate inputs or outputs indicate inversion/complementation.

## Revision Tips

1. Create flashcards for each gate type with symbol, truth table, and Boolean expression on separate sides.

2. Practice drawing gate diagrams from Boolean expressions until the process becomes automatic.

3. Verify your circuit implementations by constructing truth tables and comparing with original function.

4. Work through previous years' DU question papers to understand the exam pattern and question types.

5. Remember the universal property: be able to draw NOT, AND, OR using NAND and using NOR from memory.

6. Understand the relationship between gates: NAND = NOT(AND), NOR = NOT(OR), XNOR = NOT(XOR).

7. Focus on XOR and XNOR applications in arithmetic circuits and comparison operations.