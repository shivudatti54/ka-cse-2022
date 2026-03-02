# HDL Models of Combinational Circuits – Adder Study Material


## Table of Contents

- [HDL Models of Combinational Circuits – Adder Study Material](#hdl-models-of-combinational-circuits--adder-study-material)
- [1. Introduction to Adders](#1-introduction-to-adders)
- [2. Half Adder: Theory and HDL Implementation](#2-half-adder-theory-and-hdl-implementation)
  - [2.1 Theoretical Foundation](#21-theoretical-foundation)
  - [2.2 Truth Table and Boolean Derivation](#22-truth-table-and-boolean-derivation)
  - [2.3 VHDL Implementation (Dataflow Modeling)](#23-vhdl-implementation-dataflow-modeling)
  - [2.4 Verilog Implementation](#24-verilog-implementation)
- [3. Full Adder: Theory and HDL Implementation](#3-full-adder-theory-and-hdl-implementation)
  - [3.1 Theoretical Foundation](#31-theoretical-foundation)
  - [3.2 Truth Table and Boolean Derivation](#32-truth-table-and-boolean-derivation)
  - [3.3 VHDL Implementation (Dataflow Modeling)](#33-vhdl-implementation-dataflow-modeling)
  - [3.4 Verilog Implementation](#34-verilog-implementation)
- [4. N-Bit Ripple Carry Adder](#4-n-bit-ripple-carry-adder)
  - [4.1 Theoretical Foundation](#41-theoretical-foundation)
  - [4.2 Propagation Delay Analysis](#42-propagation-delay-analysis)
  - [4.3 VHDL Implementation (Structural Modeling)](#43-vhdl-implementation-structural-modeling)
  - [4.4 Verilog Implementation (Structural Modeling)](#44-verilog-implementation-structural-modeling)
- [5. Carry Look-Ahead Adder](#5-carry-look-ahead-adder)
  - [5.1 Theoretical Foundation](#51-theoretical-foundation)
  - [5.2 Verilog Implementation (Carry Look-Ahead)](#52-verilog-implementation-carry-look-ahead)
- [6. Comparative Analysis](#6-comparative-analysis)
- [7. Testbench for Verification](#7-testbench-for-verification)
- [8. Multiple Choice Questions](#8-multiple-choice-questions)
- [9. Conclusion](#9-conclusion)

## 1. Introduction to Adders

Adders are fundamental combinational circuits in digital electronics that perform binary arithmetic operations. An adder receives two or more binary operands (typically denoted as A and B) along with an optional carry input (C<sub>in</sub>), and produces a sum output (S) and a carry output (C<sub>out</sub>). These circuits constitute the arithmetic logic unit (ALU) backbone of processors, digital signal processors, and various computing applications.

## 2. Half Adder: Theory and HDL Implementation

### 2.1 Theoretical Foundation

The half adder is the simplest form of binary adder, designed to add two single-bit binary numbers. The addition rules follow binary arithmetic:

- 0 + 0 = 0 (Sum = 0, Carry = 0)
- 0 + 1 = 1 (Sum = 1, Carry = 0)
- 1 + 0 = 1 (Sum = 1, Carry = 0)
- 1 + 1 = 0 (Sum = 0, Carry = 1)

### 2.2 Truth Table and Boolean Derivation

| A   | B   | Sum (S) | Carry (C) |
| --- | --- | ------- | --------- |
| 0   | 0   | 0       | 0         |
| 0   | 1   | 1       | 0         |
| 1   | 0   | 1       | 0         |
| 1   | 1   | 0       | 1         |

**Formal Boolean Derivation:**

From the truth table, the Sum output S is 1 when exactly one input is 1. This corresponds to the XOR operation:

- S = A ⊕ B = A · B' + A' · B

The Carry output C is 1 only when both inputs are 1, corresponding to the AND operation:

- C = A · B

**Proof of Sum Expression:**
Using Boolean algebra, we can derive S from the minterms where S = 1:

- S = Σ(1,2) = A'B + AB'
- This is the exclusive-OR (XOR) function, verified by the identity A'B + AB' = A ⊕ B

**Proof of Carry Expression:**
The Carry output C = 1 only for input combination (1,1):

- C = Σ(3) = AB
- This is the AND function, verified by Boolean algebra: C = A · B

### 2.3 VHDL Implementation (Dataflow Modeling)

```vhdl
entity HalfAdder is
 port (
 A, B: in bit;
 S, Cout: out bit
 );
end entity HalfAdder;

architecture Dataflow of HalfAdder is
begin
 -- Sum output: XOR operation
 S <= A xor B;
 -- Carry output: AND operation
 Cout <= A and B;
end architecture Dataflow;
```

### 2.4 Verilog Implementation

```verilog
module half_adder (
 input wire A,
 input wire B,
 output wire S,
 output wire Cout
);
 // Sum: XOR operation
 assign S = A ^ B;
 // Carry: assign Cout = A AND operation
 & B;
endmodule
```

## 3. Full Adder: Theory and HDL Implementation

### 3.1 Theoretical Foundation

The full adder extends the half adder by incorporating a carry input (C<sub>in</sub>), enabling cascading for multi-bit addition. It processes three one-bit inputs: A, B, and C<sub>in</sub>, producing Sum and Carry-out (C<sub>out</sub>) outputs.

### 3.2 Truth Table and Boolean Derivation

| A   | B   | C<sub>in</sub> | Sum (S) | Carry (C<sub>out</sub>) |
| --- | --- | -------------- | ------- | ----------------------- |
| 0   | 0   | 0              | 0       | 0                       |
| 0   | 0   | 1              | 1       | 0                       |
| 0   | 1   | 0              | 1       | 0                       |
| 0   | 1   | 1              | 0       | 1                       |
| 1   | 0   | 0              | 1       | 0                       |
| 1   | 0   | 1              | 0       | 1                       |
| 1   | 1   | 0              | 0       | 1                       |
| 1   | 1   | 1              | 1       | 1                       |

**Formal Boolean Derivation for Sum:**

The Sum output S = 1 when an odd number of inputs are 1 (odd parity):

- S = Σ(1,2,4,7) = A'B'Cin + A'BCin' + AB'Cin' + ABCin

Using Boolean algebra simplification:

- S = A' (B'Cin + BCin') + A (B'Cin' + BCin)
- S = A' (B ⊕ Cin) + A (B ⊕ Cin)'
- S = A ⊕ B ⊕ Cin

**Formal Boolean Derivation for Carry-out:**

The Carry output C<sub>out</sub> = 1 when at least two inputs are 1:

- C<sub>out</sub> = Σ(3,5,6,7) = A'BCin + AB'Cin + ABCin' + ABCin

Simplifying using Boolean algebra:

- C<sub>out</sub> = A'BCin + AB'Cin + AB(Cin' + Cin)
- C<sub>out</sub> = A'BCin + AB'Cin + AB
- C<sub>out</sub> = AB + Cin (A'B + AB')
- C<sub>out</sub> = AB + Cin (A ⊕ B)

Alternatively, using canonical form:

- C<sub>out</sub> = (A ∧ B) ∨ (B ∧ C<sub>in</sub>) ∨ (A ∧ C<sub>in</sub>)

### 3.3 VHDL Implementation (Dataflow Modeling)

```vhdl
entity FullAdder is
 port (
 A, B, Cin: in bit;
 S, Cout: out bit
 );
end entity FullAdder;

architecture Dataflow of FullAdder is
begin
 -- Sum output: XOR of all three inputs
 S <= A xor B xor Cin;
 -- Carry output: majority function
 Cout <= (A and B) or (B and Cin) or (A and Cin);
end architecture Dataflow;
```

### 3.4 Verilog Implementation

```verilog
module full_adder (
 input wire A,
 input wire B,
 input wire Cin,
 output wire S,
 output wire Cout
);
 // Sum: three-input XOR (odd parity)
 assign S = A ^ B ^ Cin;
 // Carry: majority function
 assign Cout = (A & B) | (B & Cin) | (A & Cin);
endmodule
```

## 4. N-Bit Ripple Carry Adder

### 4.1 Theoretical Foundation

An N-bit adder is constructed by cascading N full adder stages, where the carry output of each stage feeds the carry input of the next higher-order stage. This architecture is called a Ripple Carry Adder (RCA) because the carry propagates through the chain like a ripple.

### 4.2 Propagation Delay Analysis

Let t<sub>FA</sub> represent the propagation delay through a single full adder stage (from any input to any output). For an N-bit RCA:

- **Worst-case delay**: Occurs when the carry must propagate from the least significant bit (LSB) to the most significant bit (MSB)
- **Total propagation delay**: T<sub>total</sub> = N × t<sub>FA</sub>

**Proof of Propagation Delay:**

Consider a 4-bit RCA adding A = 1111 and B = 0001:

- The carry generated at stage 0 must propagate through stages 1, 2, and 3
- Each stage introduces a delay of t<sub>FA</sub>
- Therefore, the final sum bit stabilizes only after N × t<sub>FA</sub>

This linear relationship (O(n)) represents a fundamental limitation of the ripple carry architecture, motivating the development of faster adder topologies.

### 4.3 VHDL Implementation (Structural Modeling)

```vhdl
entity NBitAdder is
 generic (
 N : integer := 4
 );
 port (
 A, B : in bit_vector(N-1 downto 0);
 Cin : in bit;
 Sum : out bit_vector(N-1 downto 0);
 Cout : out bit
 );
end entity NBitAdder;

architecture Structural of NBitAdder is
 -- Internal carry signals
 signal C : bit_vector(N downto 0);

 -- Component declaration for FullAdder
 component FullAdder is
 port (
 A, B, Cin : in bit;
 S, Cout : out bit
 );
 end component FullAdder;

begin
 -- Initialize carry chain
 C(0) <= Cin;

 -- Generate N full adder stages
 FA_Chain: for i in 0 to N-1 generate
 FA: FullAdder
 port map (
 A => A(i),
 B => B(i),
 Cin => C(i),
 S => Sum(i),
 Cout => C(i+1)
 );
 end generate FA_Chain;

 -- Output final carry
 Cout <= C(N);
end architecture Structural;
```

### 4.4 Verilog Implementation (Structural Modeling)

```verilog
module nbit_adder #(
 parameter N = 4
)(
 input wire [N-1:0] A,
 input wire [N-1:0] B,
 input wire Cin,
 output wire [N-1:0] Sum,
 output wire Cout
);
 // Internal carry chain
 wire [N:0] carry;

 // Initialize carry input
 assign carry[0] = Cin;

 // Generate N full adder stages
 genvar i;
 generate
 for (i = 0; i < N; i = i + 1) begin : fa_stage
 full_adder fa (
 .A (A[i]),
 .B (B[i]),
 .Cin (carry[i]),
 .S (Sum[i]),
 .Cout(carry[i+1])
 );
 end
 endgenerate

 // Output final carry
 assign Cout = carry[N];
endmodule
```

## 5. Carry Look-Ahead Adder

### 5.1 Theoretical Foundation

The Carry Look-Ahead Adder (CLA) overcomes the linear delay limitation of RCA by computing all carry outputs in parallel using generate and propagate logic.

**Key Definitions:**

- **Generate (G<sub>i</sub>)**: A carry is produced at stage i regardless of the incoming carry
- G<sub>i</sub> = A<sub>i</sub> · B<sub>i</sub>

- **Propagate (P<sub>i</sub>)**: A carry into stage i will be propagated to the next stage
- P<sub>i</sub> = A<sub>i</sub> ⊕ B<sub>i</sub>

**Carry Computation:**

The carry out of stage i is given by:

- C<sub>i+1</sub> = G<sub>i</sub> + P<sub>i</sub> · C<sub>i</sub>

Expanding recursively for a 4-bit adder:

- C<sub>1</sub> = G<sub>0</sub> + P<sub>0</sub>C<sub>0</sub>
- C<sub>2</sub> = G<sub>1</sub> + P<sub>1</sub>G<sub>0</sub> + P<sub>1</sub>P<sub>0</sub>C<sub>0</sub>
- C<sub>3</sub> = G<sub>2</sub> + P<sub>2</sub>G<sub>1</sub> + P<sub>2</sub>P<sub>1</sub>G<sub>0</sub> + P<sub>2</sub>P<sub>1</sub>P<sub>0</sub>C<sub>0</sub>
- C<sub>4</sub> = G<sub>3</sub> + P<sub>3</sub>G<sub>2</sub> + P<sub>3</sub>P<sub>2</sub>G<sub>1</sub> + P<sub>3</sub>P<sub>2</sub>P<sub>1</sub>G<sub>0</sub> + P<sub>3</sub>P<sub>2</sub>P<sub>1</sub>P<sub>0</sub>C<sub>0</sub>

**Delay Analysis:**

Since all carries are computed in parallel using a fixed-depth logic network:

- Propagation delay = O(log<sub>2</sub>n)

For a 4-bit CLA, the delay is approximately 3 gate delays, independent of operand width (for the carry computation), with additional delay for sum computation.

### 5.2 Verilog Implementation (Carry Look-Ahead)

```verilog
module cla_adder #(
 parameter N = 4
)(
 input wire [N-1:0] A,
 input wire [N-1:0] B,
 input wire Cin,
 output wire [N-1:0] Sum,
 output wire Cout
);
 wire [N-1:0] P, G;
 wire [N:0] C;

 assign C[0] = Cin;

 genvar i;
 generate
 for (i = 0; i < N; i = i + 1) begin : cla_logic
 // Propagate: Pi = Ai XOR Bi
 assign P[i] = A[i] ^ B[i];
 // Generate: Gi = Ai AND Bi
 assign G[i] = A[i] & B[i];
 // Carry computation: Ci+1 = Gi + Pi · Ci
 assign C[i+1] = G[i] | (P[i] & C[i]);
 // Sum: Si = Pi XOR Ci
 assign Sum[i] = P[i] ^ C[i];
 end
 endgenerate

 assign Cout = C[N];
endmodule
```

## 6. Comparative Analysis

| Parameter                | Ripple Carry Adder  | Carry Look-Ahead Adder            |
| ------------------------ | ------------------- | --------------------------------- |
| **Propagation Delay**    | O(n)                | O(log n)                          |
| **Hardware Complexity**  | Minimal (N FAs)     | Higher (generate/propagate logic) |
| **Fan-out Requirements** | Moderate            | Higher for carry gates            |
| **Scalability**          | Limited for large n | Excellent for large n             |
| **Power Consumption**    | Lower for small n   | Higher due to parallel logic      |
| **Area**                 | Small               | Larger                            |

## 7. Testbench for Verification

```vhdl
entity tb_FullAdder is end entity;

architecture Test of tb_FullAdder is
 signal A, B, Cin, S, Cout : bit;

 component FullAdder is
 port (A, B, Cin: in bit; S, Cout: out bit);
 end component;

begin
 -- Instantiate the Device Under Test
 dut: FullAdder port map (A, B, Cin, S, Cout);

 -- Stimulus process
 stimulus: process
 begin
 -- Test all eight input combinations
 A <= '0'; B <= '0'; Cin <= '0'; wait for 10 ns;
 A <= '0'; B <= '0'; Cin <= '1'; wait for 10 ns;
 A <= '0'; B <= '1'; Cin <= '0'; wait for 10 ns;
 A <= '0'; B <= '1'; Cin <= '1'; wait for 10 ns;
 A <= '1'; B <= '0'; Cin <= '0'; wait for 10 ns;
 A <= '1'; B <= '0'; Cin <= '1'; wait for 10 ns;
 A <= '1'; B <= '1'; Cin <= '0'; wait for 10 ns;
 A <= '1'; B <= '1'; Cin <= '1'; wait for 10 ns;

 wait; -- Terminate simulation
 end process;
end architecture Test;
```

## 8. Multiple Choice Questions

**Question 1:** For a full adder with inputs A=1, B=0, and C<sub>in</sub>=1, determine the correct output values:

- (a) S=0, C<sub>out</sub>=0
- (b) S=0, C<sub>out</sub>=1
- (c) S=1, C<sub>out</sub>=0
- (d) S=1, C<sub>out</sub>=1

**Answer:** (b) S=0, C<sub>out</sub>=1
**Explanation:** Using S = A ⊕ B ⊕ C<sub>in</sub> = 1 ⊕ 0 ⊕ 1 = 0. The carry: C<sub>out</sub> = (A·B) + (B·C<sub>in</sub>) + (A·C<sub>in</sub>) = (1·0) + (0·1) + (1·1) = 1.

**Question 2:** An 8-bit ripple carry adder has a propagation delay of 2 ns per full adder stage. Calculate the maximum propagation delay from inputs to final output:

- (a) 8 ns
- (b) 16 ns
- (c) 4 ns
- (d) 2 ns

**Answer:** (b) 16 ns
**Explanation:** For an N-bit RCA, T<sub>total</sub> = N × t<sub>FA</sub>. With N=8 and t<sub>FA</sub>=2 ns, we get T<sub>total</sub> = 8 × 2 = 16 ns.

**Question 3:** The primary advantage of a Carry Look-Ahead adder over a Ripple Carry adder is:

- (a) Reduced hardware complexity
- (b) Lower power consumption
- (c) Parallel computation of carry signals reducing propagation delay
- (d) Simpler circuit structure

**Answer:** (c) Parallel computation of carry signals reducing propagation delay
**Explanation:** CLA computes all carries simultaneously using generate (G) and propagate (P) functions, achieving O(log n) delay compared to O(n) for RCA.

**Question 4:** In a 4-bit Carry Look-Ahead adder, if A = 1100 and B = 1100 with C<sub>in</sub>=0, what is the value of G<sub>2</sub> (generate signal for bit position 2)?

- (a) 0
- (b) 1
- (c) Depends on P<sub>2</sub>
- (d) Undefined

**Answer:** (b) 1
**Explanation:** G<sub>i</sub> = A<sub>i</sub> · B<sub>i</sub>. For position 2 (third bit, 0-indexed): A<sub>2</sub>=1, B<sub>2</sub>=1, therefore G<sub>2</sub> = 1 · 1 = 1.

## 9. Conclusion

This study material has presented a comprehensive treatment of adder circuits in HDL, encompassing theoretical foundations with formal Boolean derivations, gate-level implementations, and behavioral models in both VHDL and Verilog. The comparison between Ripple Carry and Carry Look-Ahead architectures highlights fundamental trade-offs in digital design between propagation delay, hardware complexity, and scalability. Proficiency in modeling these fundamental arithmetic circuits is essential for understanding more complex combinational and sequential systems in digital electronics.
