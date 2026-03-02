# Multiplexer - Summary

## Key Definitions
- **Multiplexer (MUX)**: A combinational circuit with 2^n data inputs, n selection lines, and one output that routes the selected input to the output based on the binary pattern on selection lines
- **Selection (Address) Lines**: Control inputs that determine which data input is connected to the output
- **Demultiplexer (DEMUX)**: The inverse of a MUX; routes one input to one of 2^n outputs based on selection lines

## Key Theorems
- **Generalized Expression**: Y = Σ(m_k · I_k) where m_k is the k-th minterm
- **Cascading Requirement**: A 2^n:1 MUX requires (2^n - 1) 2:1 MUXes
- **Universal Function Realization**: Any n-variable Boolean function can be implemented using a 2^n:1 MUX

## Design Formulas
- Number of data inputs: 2^n
- Number of selection lines: n = log₂(number of inputs)
- Minimum 2:1 MUXes for 2^n:1 MUX: 2^n - 1

## Implementation Methods
1. **Direct Method (2^n:1 MUX)**: Connect all n variables to selection lines; map truth table outputs to data inputs
2. **Efficient Method (2^(n-1):1 MUX)**: Connect (n-1) variables to selection lines; remaining variable becomes data input

## Key Applications
- ALU operation selection
- Register file read/write selection
- Memory address multiplexing
- Parallel-to-serial conversion
- Data routing in communication systems