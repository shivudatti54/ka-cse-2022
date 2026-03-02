# Multiplexer - Summary

## Key Definitions and Concepts

- Multiplexer (MUX): A combinational circuit that selects one of multiple input signals and forwards it to a single output based on select line inputs
- Data Inputs: The information-bearing inputs (I₀, I₁, I₂, ...) from which one is selected
- Select Lines: Control inputs that determine which data input is routed to the output
- Enable Input: Optional input that enables or disables the multiplexer operation

## Important Formulas and Theorems

- Boolean expression for 2:1 MUX: Y = S̅·I₀ + S·I₁
- Boolean expression for 4:1 MUX: Y = S̅₁·S̅₀·I₀ + S̅₁·S₀·I₁ + S₁·S̅₀·I₂ + S₁·S₀·I₃
- Relationship: Number of data inputs (m) = 2ⁿ, where n = number of select lines

## Key Points

- Multiplexers are data selectors that route one of many inputs to a single output
- 2:1 MUX requires 1 select line, 4:1 MUX requires 2 select lines, 8:1 MUX requires 3 select lines
- Any n-variable boolean function can be implemented using a (n-1):1 multiplexer
- Larger multiplexers can be built by cascading smaller ones
- Multiplexers have applications in data routing, function implementation, and parallel-to-serial conversion

## Common Mistakes to Avoid

- Confusing select lines with data inputs in truth table construction
- Incorrectly determining the number of select lines for a given number of inputs
- Forgetting to use both the variable and its complement when implementing functions with MUX
- Incorrect cascading connections between multiplexer stages

## Revision Tips

- Practice drawing block diagrams and truth tables for different MUX configurations
- Memorize the boolean expression derivation method for 2:1 and 4:1 MUX
- Solve at least three problems on implementing boolean functions using multiplexers
- Understand the cascading methodology for building larger MUX from smaller ones