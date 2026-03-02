# Multiplexer - Summary

## Key Definitions and Concepts

- **Multiplexer (MUX)**: A combinational circuit that selects one of multiple input signals and forwards it to a single output based on select line inputs
- **Select Lines**: Control inputs that determine which data input is routed to the output; if there are n select lines, 2^n inputs can be selected
- **Enable Input**: Additional control input that enables or disables the multiplexer operation, often active LOW
- **Cascading**: Connecting multiple smaller multiplexers to create larger multiplexers with more inputs

## Important Formulas and Theorems

- **Relationship**: Number of Select Lines = log₂(Number of Data Inputs)
- **2-to-1 MUX Output**: Y = S̄·I₀ + S·I₁
- **4-to-1 MUX Output**: Y = S̄₁·S̄₀·I₀ + S̄₁·S₀·I₁ + S₁·S̄₀·I₂ + S₁·S₀·I₃
- **Function Implementation**: An n-variable function can be implemented using a multiplexer with n-1 select lines

## Key Points

- A multiplexer acts as a digital switch, routing one of many inputs to a single output
- 2-to-1 MUX requires 1 select line, 4-to-1 requires 2, 8-to-1 requires 3, 16-to-1 requires 4
- The output immediately reflects the selected input once select lines change
- Multiplexers are extensively used in data routing, bus systems, and communication multiplexing
- Any boolean function can be implemented using a multiplexer by properly setting data inputs
- Larger multiplexers can be constructed by cascading smaller ones in a tree structure
- Enable inputs allow cascading and provide additional control over multiplexer operation

## Common Mistakes to Avoid

- Confusing multiplexer (data selector) with demultiplexer (data distributor) - they perform opposite functions
- Incorrectly mapping select line binary values to input selection (remember: 00 selects I₀, 01 selects I₁, etc.)
- Forgetting that select line changes propagate through gates, causing a brief delay in output change
- Not considering the enable input polarity (active HIGH vs active LOW) when analyzing circuits

## Revision Tips

- Practice writing boolean expressions for different multiplexer configurations from truth tables
- Memorize the relationship between number of inputs and select lines as it applies to all multiplexer sizes
- Review function implementation problems as they frequently appear in DU examinations with 8-10 marks
- Draw and analyze 4-to-1 and 8-to-1 multiplexer circuits until the operation becomes automatic
- Remember that multiplexers with enable inputs can be easily cascaded for larger systems