# Digital Design - The Multiplexer (MUX)

## 1. Introduction

In digital electronics, we frequently encounter the problem of efficiently routing one signal from multiple input sources to a single output line based on specified conditions. This fundamental data selection operation is performed by a **Multiplexer (MUX)**, also known as a "data selector." The multiplexer is an essential combinational logic circuit that functions as a digitally controlled multi-position switch, capable of selecting and forwarding one input data stream to the output based on the binary pattern present on its selection lines.

The multiplexer serves as a cornerstone in Computer Organization and Architecture, with extensive applications in data routing within processors, arithmetic logic units (ALUs), memory addressing schemes, communication systems, and parallel-to-serial data conversion. Understanding the multiplexer is prerequisite to comprehending more complex digital systems such as bus architectures, register transfer level (RTL) design, and system-on-chip (SoC) implementations.

## 2. Fundamental Theory

### 2.1 Definition and Mathematical Formulation

A multiplexer is a combinational circuit with **2^n input data lines** (denoted as I₀, I₁, I₂, ..., I*{2^n-1}), **n selection (or address) lines** (denoted as S₀, S₁, ..., S*{n-1}), and **one output line** (denoted as Y). The n selection lines produce 2^n distinct binary combinations, each of which selects exactly one input to be propagated to the output.

**Theorem: Generalized Boolean Expression for 2^n:1 MUX**

The output Y of an n-select-line multiplexer can be expressed as:

$$Y = \sum_{k=0}^{2^n-1} (m_k \cdot I_k)$$

where m_k represents the minterm corresponding to the binary representation of k, and I_k is the data input associated with that minterm.

_Proof:_ Each minterm m_k is equal to 1 for exactly one combination of selection lines (the combination representing binary k). When m_k = 1, the corresponding input I_k is enabled to the output through the AND gate associated with that minterm. Since exactly one minterm is true for any given selection input, exactly one input is selected and passed to the output. ∎

For a **2:1 MUX** (n=1), this simplifies to:
$$Y = S' \cdot I_0 + S \cdot I_1$$

For a **4:1 MUX** (n=2):
$$Y = S_1'S_0'I_0 + S_1'S_0I_1 + S_1S_0'I_2 + S_1S_0I_3$$

### 2.2 Block Diagram and Truth Tables

**2-to-1 Multiplexer:**

- Data Inputs: I₀, I₁
- Selection Line: S (1 bit)
- Output: Y

| S   | Y   |
| --- | --- |
| 0   | I₀  |
| 1   | I₁  |

**4-to-1 Multiplexer:**

- Data Inputs: I₀, I₁, I₂, I₃
- Selection Lines: S₁, S₀ (2 bits)
- Output: Y

| S₁  | S₀  | Y   |
| --- | --- | --- |
| 0   | 0   | I₀  |
| 0   | 1   | I₁  |
| 1   | 0   | I₂  |
| 1   | 1   | I₃  |

**8-to-1 Multiplexer:**

- Data Inputs: I₀ through I₇
- Selection Lines: S₂, S₁, S₀ (3 bits)
- Output: Y

The output follows the pattern where the binary value formed by (S₂S₁S₀) determines which input is selected (e.g., S₂S₁S₀ = 010 selects I₂).

## 3. Gate-Level Implementation

### 3.1 2:1 MUX Using Basic Gates

The Boolean expression Y = S'I₀ + SI₁ can be implemented using:

- Two AND gates
- One OR gate
- One NOT gate

Each AND gate receives one data input and the appropriate form of the selection signal (S or S'). The outputs of both AND gates feed into the OR gate, producing the final output.

### 3.2 4:1 MUX Implementation

The expression Y = S₁'S₀'I₀ + S₁'S₀I₁ + S₁S₀'I₂ + S₁S₀I₃ requires:

- Two NOT gates (for S₁' and S₀')
- Four 3-input AND gates (one for each product term)
- One 4-input OR gate

Each 3-input AND gate computes one minterm by ANDing the appropriate combination of S₁', S₁, S₀', and S₀ with the corresponding data input.

## 4. Cascading Multiplexers (Multiplexer Trees)

### 4.1 Building Larger MUXes from Smaller Ones

Larger multiplexers can be constructed by cascading smaller ones. This is essential for practical implementation when larger MUXes are not directly available.

**Example: Implementing 8:1 MUX using 4:1 MUXes**

An 8:1 MUX requires 3 selection lines (S₂S₁S₀). We can implement this using:

- Two 4:1 MUXes at the first stage
- One 2:1 MUX at the second stage to select between the outputs of the first stage

**Procedure:**

1. Connect the most significant selection line (S₂) to the enable/selection input of the final 2:1 MUX
2. Connect S₁ and S₀ to the selection inputs of both 4:1 MUXes
3. Connect data inputs I₀-I₃ to the first 4:1 MUX and inputs I₄-I₇ to the second 4:1 MUX
4. Connect outputs of the two 4:1 MUXes to the inputs of the 2:1 MUX

**Theorem: Minimum Number of 2:1 MUXes for 2^n:1 MUX**

To implement a 2^n:1 MUX using only 2:1 MUXes, we require (2^n - 1) 2:1 MUXes.

_Proof:_ A multiplexer tree is essentially a binary tree with the data inputs at the leaves and the output at the root. A complete binary tree with 2^n leaves has (2^n - 1) internal nodes, each representing a 2:1 MUX. ∎

Therefore:

- 4:1 MUX requires 3 × 2:1 MUXes
- 8:1 MUX requires 7 × 2:1 MUXes
- 16:1 MUX requires 15 × 2:1 MUXes

## 5. Implementing Boolean Functions Using Multiplexers

### 5.1 Theoretical Foundation

**Theorem: Universal Function Realization**

Any Boolean function of n variables can be realized using a 2^n:1 multiplexer without any additional logic gates.

_Proof:_ Consider a Boolean function F(x₁, x₂, ..., x_n) of n variables. A 2^n:1 MUX has n selection lines. If we connect the n variables to the selection lines, each minterm of the function corresponds to exactly one selection line combination. By connecting the truth table output values (0 or 1) to the corresponding data inputs of the MUX, the MUX output directly realizes the function. Specifically, for each selection line combination that makes F=1, we connect the corresponding data input to logic 1 (Vcc); for combinations making F=0, we connect to logic 0 (GND). ∎

### 5.2 Implementation Procedure for n-Variable Functions

**Method 1: Using 2^n:1 MUX**

1. Identify the n variables of the function
2. Connect these n variables to the n selection lines of the MUX
3. For each combination of selection lines, examine the function output
4. Connect each data input I_k to:

- Logic 1 (Vcc) if the function output is 1 for that minterm
- Logic 0 (GND) if the function output is 0 for that minterm
- The actual function output if the function depends on additional variables

**Method 2: Using 2^(n-1):1 MUX (Efficient Approach)**
For a function of n variables, we can use a 2^(n-1):1 MUX by grouping variables:

1. Select (n-1) variables for the selection lines
2. The remaining variable (or its complement) becomes the data input
3. Express the function in terms of the selected (n-1) variables
4. Connect the appropriate values to the data inputs

### 5.3 Worked Examples

**Example 1: Implement F(A,B,C) = Σm(1,3,5,7) using 4:1 MUX**

Solution:

- Using A and B as selection lines (S₁=A, S₀=B)
- C becomes the data input

Truth table:

| A   | B   | C   | F   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |

For each selection combination (A,B):

- (0,0): F = C → I₀ = C
- (0,1): F = C → I₁ = C
- (1,0): F = C → I₂ = C
- (1,1): F = C → I₃ = C

Therefore: I₀ = I₁ = I₂ = I₃ = C

**Example 2: Implement F(A,B,C) = A'B + BC' + AC using 8:1 MUX**

Solution:

- Connect A, B, C to selection lines S₂, S₁, S₀ respectively
- Compute minterms: F = Σm(1,2,3,5,6,7)

| S₂(A) | S₁(B) | S₀(C) | F   | Data Input |
| ----- | ----- | ----- | --- | ---------- |
| 0     | 0     | 0     | 0   | I₀ = 0     |
| 0     | 0     | 1     | 1   | I₁ = 1     |
| 0     | 1     | 0     | 1   | I₂ = 1     |
| 0     | 1     | 1     | 1   | I₃ = 1     |
| 1     | 0     | 0     | 0   | I₄ = 0     |
| 1     | 0     | 1     | 1   | I₅ = 1     |
| 1     | 1     | 0     | 1   | I₆ = 1     |
| 1     | 1     | 1     | 1   | I₇ = 1     |

## 6. Demultiplexer (DEMUX) - The Inverse Operation

A demultiplexer performs the inverse operation of a multiplexer. It has one input line, n selection lines, and 2^n output lines. The input is routed to exactly one output based on the selection lines.

**1-to-4 DEMUX:**

- Input: I
- Selection: S₁, S₀
- Outputs: Y₀, Y₁, Y₂, Y₃

| S₁  | S₀  | Y₀  | Y₁  | Y₂  | Y₃  |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | I   | 0   | 0   | 0   |
| 0   | 1   | 0   | I   | 0   | 0   |
| 1   | 0   | 0   | 0   | I   | 0   |
| 1   | 1   | 0   | 0   | 0   | I   |

The relationship between MUX and DEMUX enables bidirectional data routing in communication systems.

## 7. Practical Considerations

### 7.1 Propagation Delay

In real implementations, multiplexers exhibit propagation delay (t_pHL and t_pLH) due to the switching characteristics of gates. For a cascaded MUX tree, the total propagation delay equals the sum of delays through each stage. This is critical in high-speed digital systems where timing constraints must be met.

### 7.2 Enable Inputs

Most practical multiplexers include an enable (EN) or strobe input that globally enables or disables the output, regardless of selection inputs. When EN = 0, the output is typically forced to 0 or high-impedance state.

## 8. HDL Implementation

### 8.1 Verilog Code for 4:1 MUX

```verilog
module mux_4to1 (
 input [3:0] I, // Data inputs
 input [1:0] S, // Selection lines
 output reg Y // Output
);
 always @(*)
 begin
 case (S)
 2'b00: Y = I[0];
 2'b01: Y = I[1];
 2'b10: Y = I[2];
 2'b11: Y = I[3];
 endcase
 end
endmodule
```

### 8.2 VHDL Code for 8:1 MUX

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux_8to1 is
 Port ( I : in STD_LOGIC_VECTOR (7 downto 0);
 S : in STD_LOGIC_VECTOR (2 downto 0);
 Y : out STD_LOGIC);
end mux_8to1;

architecture Behavioral of mux_8to1 is
begin
 process(I, S)
 begin
 Y <= I(to_integer(unsigned(S)));
 end process;
end Behavioral;
```

## 9. Applications in Computer Organization

Multiplexers serve critical roles in processor architecture:

1. **ALU Operation Selection**: MUXes select between different arithmetic and logical operations based on control signals
2. **Register Selection**: MUXes choose which register's contents are placed on the bus
3. **Memory Addressing**: Address multiplexers select between different memory segments
4. **Parallel-to-Serial Conversion**: MUXes combine multiple parallel data lines into serial streams
5. **Bus Arbitration**: MUXes manage access to shared data buses

## 10. Summary

- A multiplexer (MUX) is a combinational circuit that selects one of 2^n inputs and routes it to a single output based on n selection lines
- The generalized Boolean expression is Y = Σ(m_k · I_k) where m_k represents minterms
- Larger MUXes can be constructed by cascading smaller ones; a 2^n:1 MUX requires (2^n - 1) 2:1 MUXes
- Any n-variable Boolean function can be realized using a 2^n:1 MUX without external gates
- The demultiplexer performs the inverse operation, routing one input to one of 2^n outputs
- MUXes are fundamental building blocks in ALUs, memory systems, and data routing applications
