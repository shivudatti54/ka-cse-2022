# Combinational Logic

### Introduction

- Combinational logic is a type of digital logic that uses AND, OR, and NOT gates to produce an output based on multiple inputs.
- It is also known as combinational digital circuits or sequential logic without memory.

### Combinational Circuits

- A combinational circuit is a circuit that produces an output based on the current inputs and does not have any memory.
- Characteristics:
  - No flip-flops or registers
  - Outputs depend only on present inputs
  - Outputs do not change over time
- Types:
  - Boolean algebra
  - Karnaugh maps
  - Truth tables

### Design Procedure

- Choose the type of circuit needed
- Determine the number of inputs and outputs
- Draw the circuit diagram using gates
- Use Karnaugh maps or Boolean algebra to simplify the circuit
- Test the circuit using truth tables

### Binary Adder-Subtractor

- A binary adder/subtractor is a combinational circuit that adds or subtracts two binary numbers.
- Formula: `S = A + B (addition)`
- Formula: `S = A - B (subtraction)`
- Truth table:

| A   | B   | S   | Carry |
| --- | --- | --- | ----- |
| 0   | 0   | 0   | 0     |
| 0   | 1   | 1   | 0     |
| 1   | 0   | 1   | 0     |
| 1   | 1   | 0   | 1     |

### Decoders

- A decoder is a combinational circuit that generates a binary output from a single binary input.
- Formula: `Y = d × A (where d is a binary number)`
- Truth table:

| A   | d   | Y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

### Encoders

- An encoder is a combinational circuit that generates a binary input from a single binary output.
- Formula: `A = Y / d (where d is a binary number)`
- Truth table:

| Y   | d   | A   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

### Multiplexers

- A multiplexer is a combinational circuit that selects one of multiple binary inputs based on a single binary input.
- Formula: `Y = i × m + (i+1) × n (where i is the select input)`
- Truth table:

| m   | n   | i   | Y   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |

Important Formulas and Definitions:

- De Morgan's laws:
  - A + B = !(!A × !B)
  - A × B = !(!A + !B)
- Boolean algebra:
  - AND (conjunction): A × B
  - OR (disjunction): A + B
  - NOT (negation): !A
- Truth tables: Used to determine the output of a logic circuit based on the inputs
