# Multiplexer

## Introduction

A Multiplexer (MUX) is a fundamental combinational logic circuit that selects one of several input signals and forwards it to a single output line. The selection of a particular input is controlled by a set of select lines. In digital systems, multiplexers play a crucial role in data routing, enabling multiple data sources to share a common transmission medium. They are extensively used in communications, memory addressing, and digital signal processing applications.

In the context of the DU Computer Science curriculum, understanding multiplexers is essential because they form the building block for more complex digital systems. Multiplexers are classified based on the number of inputs they can handle - the most common types being 2:1, 4:1, 8:1, and 16:1 multiplexers. The nomenclature indicates the number of data inputs followed by the number of outputs. For instance, a 4:1 multiplexer has four data inputs and one output, requiring two select lines to choose among the four inputs.

The significance of multiplexers extends beyond simple data selection. They can be used to implement boolean functions, create parallel-to-serial converters, and construct combinational logic circuits with fewer gates than traditional methods. This versatility makes them indispensable in modern digital design and computer architecture.

## Key Concepts

### 2:1 Multiplexer

The simplest form of multiplexer is the 2:1 MUX, which has two data inputs (I₀ and I₁), one select line (S), and one output (Y). When the select line S is at logic 0, the output Y equals input I₀. When S is at logic 1, output Y equals input I₁.

The boolean expression for a 2:1 multiplexer is:

Y = S̅·I₀ + S·I₁

The truth table is:

| S | I₀ | I₁ | Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

The circuit can be implemented using one NOT gate, two AND gates, and one OR gate.

### 4:1 Multiplexer

A 4:1 multiplexer has four data inputs (I₀, I₁, I₂, I₃), two select lines (S₀, S₁), and one output (Y). The two select lines can represent four different binary combinations (00, 01, 10, 11), each selecting a different input to pass to the output.

The boolean expression is:

Y = S̅₁·S̅₀·I₀ + S̅₁·S₀·I₁ + S₁·S̅₀·I₂ + S₁·S₀·I₃

The truth table is:

| S₁ | S₀ | Y |
|----|----|---|
| 0 | 0 | I₀ |
| 0 | 1 | I₁ |
| 1 | 0 | I₂ |
| 1 | 1 | I₃ |

### 8:1 Multiplexer

An 8:1 multiplexer expands the concept further with eight data inputs (I₀ through I₇) and three select lines (S₀, S₁, S₂). The select lines generate eight combinations, each corresponding to one input. This follows the general rule that n select lines can handle 2ⁿ data inputs.

### General Formula

For a multiplexer with m data inputs and n select lines:
- Number of data inputs (m) = 2ⁿ
- Number of select lines (n) = log₂(m)

### Multiplexer as a Universal Logic Generator

One of the most powerful applications of multiplexers is implementing boolean functions. Any n-variable boolean function can be implemented using a multiplexer with (n-1) select lines. The remaining variable and its complement are used as data inputs, set either to 0, 1, the variable, or its complement based on the function's truth table.

### Cascading Multiplexers

Larger multiplexers can be constructed by cascading smaller ones. For example, two 4:1 multiplexers can combine to form an 8:1 multiplexer by using a 2:1 multiplexer at the output to select between the outputs of the two 4:1 multiplexers based on the most significant select bit.

## Examples

### Example 1: Implementation of a 4:1 MUX using logic gates

Construct a 4:1 multiplexer using basic logic gates.

Solution:

Step 1: Identify the inputs and outputs
- Data inputs: I₀, I₁, I₂, I₃
- Select lines: S₀, S₁
- Output: Y

Step 2: Write the boolean expression
Y = S̅₁·S̅₀·I₀ + S̅₁·S₀·I₁ + S₁·S̅₀·I₂ + S₁·S₀·I₃

Step 3: Implement using gates
- Use NOT gates to generate S̅₀ and S̅₁
- Use AND gates to create each product term
- Use OR gate to sum all product terms

The circuit requires: 2 NOT gates, 4 AND gates (3-input each), and 1 OR gate (4-input).

### Example 2: Implement the boolean function F(A,B,C) = Σm(1,3,5,6) using a multiplexer

Solution:

Step 1: Create truth table with A and B as select lines

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Step 2: Use A and B as select lines, C and its complement as data inputs

For each combination of A,B:
- AB = 00: F = C → Connect C to I₀
- AB = 01: F = C → Connect C to I₁
- AB = 10: F = C → Connect C to I₂
- AB = 11: F = C̅ → Connect C̅ to I₃

Step 3: Implement using 4:1 MUX with C and C̅ as data inputs

### Example 3: Design a 16:1 multiplexer using 4:1 multiplexers

Solution:

Step 1: Calculate number of 4:1 MUX required
- 16 inputs require 4 groups of 4 inputs each
- Therefore, we need four 4:1 multiplexers at the first stage

Step 2: First stage
- Use four 4:1 MUX units
- Each handles 4 of the 16 inputs
- Use select lines S₀ and S₁ for all four units (common)

Step 3: Second stage
- Use one 4:1 MUX to select output from the first stage
- Use select lines S₂ and S₃

Step 4: Connect outputs of first stage to inputs of second stage
- First MUX output → I₀ of second stage
- Second MUX output → I₁ of second stage
- Third MUX output → I₂ of second stage
- Fourth MUX output → I₃ of second stage

Total components: 5 multiplexers (4 of 4:1 and 1 of 4:1 at output stage)

## Exam Tips

1. Remember the fundamental relationship: number of select lines (n) = log₂(number of data inputs)

2. Always derive the boolean expression from the truth table before implementing the circuit

3. For implementing boolean functions using MUX, use (n-1) variables as select lines and the remaining variable and its complements as data inputs

4. In exam questions, carefully identify which variables are select lines and which are data inputs

5. When cascading multiplexers, ensure proper connection of select lines at each stage

6. The enable input (if present) must be properly handled - when disabled, output is always 0 or high-Z depending on type

7. Practice drawing both the circuit diagram and truth table for different multiplexer configurations

8. Know that multiplexers can be used as data selectors, function generators, and in parallel-to-serial conversion