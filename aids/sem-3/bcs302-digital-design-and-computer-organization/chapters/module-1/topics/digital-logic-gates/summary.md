# Digital Logic Gates - Summary

## Key Definitions and Concepts

- **Logic Gate**: An electronic circuit that performs a logical operation on one or more binary inputs to produce a single binary output.

- **NOT Gate (Inverter)**: A single-input gate that produces the complement of the input; Y = A̅.

- **AND Gate**: Produces HIGH output only when ALL inputs are HIGH; Y = A·B or AB.

- **OR Gate**: Produces HIGH output when ANY input is HIGH; Y = A + B.

- **NAND Gate**: Universal gate producing complement of AND; Y = (AB)̅. Can implement any Boolean function alone.

- **NOR Gate**: Universal gate producing complement of OR; Y = (A + B)̅. Can implement any Boolean function alone.

- **XOR Gate**: Exclusive OR produces 1 when inputs differ; Y = A ⊕ B.

- **XNOR Gate**: Produces 1 when inputs are equal; Y = (A ⊕ B)̅.

## Important Formulas and Theorems

- **AND Operation**: 0·0 = 0, 0·1 = 0, 1·0 = 0, 1·1 = 1
- **OR Operation**: 0+0 = 0, 0+1 = 1, 1+0 = 1, 1+1 = 1
- **NOT Operation**: NOT 0 = 1, NOT 1 = 0
- **De Morgan's Theorem 1**: (A·B)̅ = A̅ + B̅
- **De Morgan's Theorem 2**: (A + B)̅ = A̅ · B̅

## Key Points

- Binary logic uses only two voltage levels: logic 0 (LOW, typically 0V) and logic 1 (HIGH, typically 5V or 3.3V).

- NAND and NOR gates are called universal gates because each can individually implement any Boolean function.

- XOR gate output is 1 when inputs have different values (odd number of 1s); XNOR output is 1 when inputs are equal (even number of 1s including zero).

- The small circle (bubble) on gate symbols represents logical inversion/complementation.

- Multiple-input AND/OR gates follow the same logical rules extended to n inputs.

- Gate-level circuits are analyzed by computing outputs at each stage, working from inputs to final output.

## Common Mistakes to Avoid

- Confusing AND with OR: AND requires ALL inputs to be 1, while OR requires ANY input to be 1.

- Forgetting that 1 + 1 = 1 in Boolean algebra (not 2 as in decimal arithmetic).

- Misapplying De Morgan's theorems by forgetting to invert each individual variable, not just the entire expression.

- Overlooking inversion bubbles when analyzing circuits, leading to incorrect output values.

- Confusing XOR with OR: XOR excludes the case when both inputs are 1.

## Revision Tips

- Create flashcards with gate symbols on one side and truth tables on the other for quick recall.

- Practice drawing gate circuits from Boolean expressions and vice versa regularly.

- Work through at least 5-10 gate network analysis problems to build speed and accuracy.

- Memorize the NAND and NOR gate symbols particularly well, as these are most frequently tested as universal gates.

- Understand the bubble-matching concept: an input bubble and output bubble connected together cancel each other.