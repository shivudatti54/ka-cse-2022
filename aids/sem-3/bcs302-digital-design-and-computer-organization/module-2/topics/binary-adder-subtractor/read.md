# Binary Adder-Subtractor


## Table of Contents

- [Binary Adder-Subtractor](#binary-adder-subtractor)
- [1. Introduction](#1-introduction)
- [2. Half Adder](#2-half-adder)
  - [2.1 Theory and Operation](#21-theory-and-operation)
  - [2.2 Truth Table](#22-truth-table)
  - [2.3 Boolean Expressions and Proof](#23-boolean-expressions-and-proof)
  - [2.4 Logic Gate Implementation](#24-logic-gate-implementation)
- [3. Full Adder](#3-full-adder)
  - [3.1 Theory and Operation](#31-theory-and-operation)
  - [3.2 Truth Table](#32-truth-table)
  - [3.3 Boolean Expressions and Derivation](#33-boolean-expressions-and-derivation)
  - [3.4 Implementation Using Half Adders](#34-implementation-using-half-adders)
- [4. N-Bit Ripple Carry Adder](#4-n-bit-ripple-carry-adder)
  - [4.1 Architecture](#41-architecture)
  - [4.2 4-Bit Ripple Carry Adder Structure](#42-4-bit-ripple-carry-adder-structure)
  - [4.3 Propagation Delay Analysis](#43-propagation-delay-analysis)
  - [4.4 Timing Diagram (Conceptual)](#44-timing-diagram-conceptual)
- [5. Carry Lookahead Adder (CLA)](#5-carry-lookahead-adder-cla)
  - [5.1 Principle](#51-principle)
  - [5.2 Generate and Propagate Functions](#52-generate-and-propagate-functions)
  - [5.3 Carry Equations](#53-carry-equations)
  - [5.4 Delay Analysis](#54-delay-analysis)
- [6. Binary Subtraction and Two's Complement](#6-binary-subtraction-and-twos-complement)
  - [6.1 Theory](#61-theory)
  - [6.2 Example](#62-example)
- [7. 4-Bit Adder-Subtractor Circuit](#7-4-bit-adder-subtractor-circuit)
  - [7.1 Unified Circuit Design](#71-unified-circuit-design)
  - [7.2 Circuit Diagram](#72-circuit-diagram)
  - [7.3 VHDL Implementation](#73-vhdl-implementation)
- [8. Overflow Detection](#8-overflow-detection)
  - [8.1 Theory](#81-theory)
  - [8.2 Detection Logic](#82-detection-logic)
  - [8.3 Example](#83-example)
- [9. Numerical Problems](#9-numerical-problems)
  - [Problem 1](#problem-1)
  - [Problem 2](#problem-2)

## 1. Introduction

Binary adders and subtractors constitute the fundamental arithmetic backbone of digital computing systems. These combinational circuits perform essential mathematical operations that underpin all computational processes within a processor's Arithmetic Logic Unit (ALU). The capability to add and subtract binary numbers efficiently directly impacts processor performance, making the design and analysis of these circuits a critical topic in digital design and computer organization.

This chapter provides an exhaustive treatment of fundamental adder circuits, progressing from basic half adders to sophisticated carry lookahead architectures, and demonstrates how a unified circuit can perform both addition and subtraction through two's complement representation.

## 2. Half Adder

### 2.1 Theory and Operation

A half adder is the simplest arithmetic circuit that performs binary addition of two single-bit operands. It accepts two binary inputs, typically denoted as A and B, and produces two outputs: the sum bit (S) and the carry bit (C). The half adder derives its name from the limitation that it cannot accept a carry input from a previous less significant stage, making it suitable only for adding the least significant bits of multi-bit numbers.

### 2.2 Truth Table

| A   | B   | Sum (S) | Carry (C) |
| --- | --- | ------- | --------- |
| 0   | 0   | 0       | 0         |
| 0   | 1   | 1       | 0         |
| 1   | 0   | 1       | 0         |
| 1   | 1   | 0       | 1         |

### 2.3 Boolean Expressions and Proof

From the truth table, we derive the Boolean expressions using Boolean algebra:

**Sum Expression: S = A ⊕ B**

_Proof via Sum of Products (SOP):_
S = A'B + AB'
This is the exclusive-OR (XOR) function, which can be expressed as S = A ⊕ B.

**Carry Expression: C = A · B**

_Proof:_
Carry is generated only when both inputs are 1 (the fourth row of the truth table).
C = A ∧ B = A · B

### 2.4 Logic Gate Implementation

The half adder can be implemented using one XOR gate and one AND gate:

```
A ──────[XOR]──→ S
 │ │
 └────[AND]──→ C
B ──────────────
```

## 3. Full Adder

### 3.1 Theory and Operation

A full adder extends the half adder's capability by incorporating a carry-in input (C_in) from a previous stage. This allows cascading multiple full adders to construct n-bit parallel adders. The full adder processes three single-bit inputs: A, B, and C_in, producing two outputs: Sum (S) and Carry-out (C_out).

### 3.2 Truth Table

| A   | B   | C_in | Sum (S) | C_out |
| --- | --- | ---- | ------- | ----- |
| 0   | 0   | 0    | 0       | 0     |
| 0   | 0   | 1    | 1       | 0     |
| 0   | 1   | 0    | 1       | 0     |
| 0   | 1   | 1    | 0       | 1     |
| 1   | 0   | 0    | 1       | 0     |
| 1   | 0   | 1    | 0       | 1     |
| 1   | 1   | 0    | 0       | 1     |
| 1   | 1   | 1    | 1       | 1     |

### 3.3 Boolean Expressions and Derivation

**Sum: S = A ⊕ B ⊕ C_in**

_Derivation:_
S = Σ(1,2,4,7) = A'B'C_in + A'BC_in' + AB'C_in' + ABC_in
Using Boolean algebra simplification:
S = C_in(A'B' + AB) + C_in'(A'B + AB')
S = C_in(A ⊙ B) + C_in'(A ⊕ B)
S = A ⊕ B ⊕ C_in (the three-input XOR function)

**Carry-out: C_out = AB + AC_in + BC_in = AB + (A ⊕ B)C_in**

_Proof via Karnaugh Map:_
For C_out, the minterms are (3,5,6,7). Using K-map minimization:
C_out = AB + AC_in + BC_in

_Alternative derivation using generate and propagate:_
Let G = AB (Generate: carry generated regardless of C_in)
Let P = A ⊕ B (Propagate: carry propagated from C_in)
Then: C_out = G + P · C_in = AB + (A ⊕ B)C_in

### 3.4 Implementation Using Half Adders

A full adder can be constructed using two half adders and one OR gate:

```
 ┌─────────────┐
 A ───┤ ├── S1 = A ⊕ B
 B ───┤ Half ├── C1 = A · B
 │ Adder 1 │
 └─────────────┘
 │
 S1 ──→ ┌─────────────┐
 C_in ─┤ ├── S = Sum
 B ───┤ Half ├── C2 = S1 · C_in
 │ Adder 2 │
 └─────────────┘
 │
 C_out ←──[OR]── C1 + C2
```

## 4. N-Bit Ripple Carry Adder

### 4.1 Architecture

An n-bit ripple carry adder cascades n full adders in series, where the carry-out of each stage feeds into the carry-in of the next higher significant stage. This straightforward architecture enables addition of multi-bit binary numbers but suffers from inherent propagation delays.

### 4.2 4-Bit Ripple Carry Adder Structure

```
 C4 C3 C2 C1 C0 (= 0)
 ↑ ↑ ↑ ↑ ↑
 +-----+-----+-----+-----+
A3,B3→| FA3 | FA2 | FA1 | FA0 |←A0,B0
 +-----+-----+-----+-----+
 ↓ ↓ ↓ ↓
 S3 S2 S1 S0
```

### 4.3 Propagation Delay Analysis

The critical path delay determines the maximum operating frequency of the adder. For a ripple carry adder:

**Total Propagation Delay = n × t_fa**

Where t_fa is the propagation delay of a single full adder (typically from C_in to C_out).

_Derivation:_
In the worst case, a carry must propagate from the least significant bit (FA0) through all n stages to the most significant bit (FAn-1). The delay accumulates linearly with the number of stages, making ripple carry adders impractical for large values of n.

For a 4-bit adder with t_fa = 10ns:
Worst-case delay = 4 × 10ns = 40ns

### 4.4 Timing Diagram (Conceptual)

```
C_out (MSB) ─┐
 │ _______
 └─── ──────
 ↑
 Carry propagates
 through all stages
```

## 5. Carry Lookahead Adder (CLA)

### 5.1 Principle

The Carry Lookahead Adder overcomes the linear propagation delay of ripple carry adders by computing carry bits simultaneously using generate and propagate functions. This parallel approach reduces delay to a constant value independent of the number of bits.

### 5.2 Generate and Propagate Functions

For each full adder stage i:

- **Generate (G_i):** G_i = A_i · B_i (carryout generated when both inputs are 1)
- **Propagate (P_i):** P_i = A_i ⊕ B_i (carryin propagates to carryout when P_i = 1)

### 5.3 Carry Equations

- C_1 = G_0 + P_0 · C_0
- C_2 = G_1 + P_1 · G_0 + P_1 · P_0 · C_0
- C_3 = G_2 + P_2 · G_1 + P_2 · P_1 · G_0 + P_2 · P_1 · P_0 · C_0

### 5.4 Delay Analysis

**CLA Propagation Delay = 2 × t_gate + t_AND + t_OR**

The delay is constant (typically 2-3 gate delays) regardless of operand width, making CLA essential for high-speed processors.

## 6. Binary Subtraction and Two's Complement

### 6.1 Theory

Subtraction can be performed using addition by employing the two's complement representation:

**A - B = A + (−B) = A + (B' + 1) = A + B' + 1**

Where B' represents the one's complement (bitwise inversion) of B.

### 6.2 Example

Subtract 5 from 13 (13 - 5):

```
 13 = 1101
 -5 = 1011 (two's complement of 0101)

 1101
+ 1011
------
 11000
```

Discarding the overflow bit (5th bit), we get 1000₂ = 8, which is correct (13 - 5 = 8).

## 7. 4-Bit Adder-Subtractor Circuit

### 7.1 Unified Circuit Design

A single circuit performs both addition and subtraction using a mode control input (M):

- **When M = 0 (Addition):** Output = A + B
- XOR gates pass B unchanged (B ⊕ 0 = B)
- Initial carry C_0 = 0

- **When M = 1 (Subtraction):** Output = A - B = A + B' + 1
- XOR gates complement B (B ⊕ 1 = B')
- Initial carry C_0 = 1

### 7.2 Circuit Diagram

```
 M (Mode Control)
 |
 +--------+--------+
 | |
B3 ──┼─[XOR]──→FA3←───A3 → S3
B2 ──┼─[XOR]──→FA2←───A2 → S2
B1 ──┼─[XOR]──→FA1←───A1 → S1
B0 ──┼─[XOR]──→FA0←───A0 → S0
 | |
 +--------C0 = M---+
```

### 7.3 VHDL Implementation

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity adder_subtractor is
 Port ( A : in STD_LOGIC_VECTOR (3 downto 0);
 B : in STD_LOGIC_VECTOR (3 downto 0);
 M : in STD_LOGIC;
 S : out STD_LOGIC_VECTOR (3 downto 0);
 C_out : out STD_LOGIC;
 V : out STD_LOGIC);
end adder_subtractor;

architecture Behavioral of adder_subtractor is
 signal B_xor : STD_LOGIC_VECTOR (3 downto 0);
 signal C : STD_LOGIC_VECTOR (4 downto 0);
begin
 B_xor <= B XOR (M & M & M & M);
 C(0) <= M;

 process(A, B_xor, C)
 begin
 S(0) <= A(0) XOR B_xor(0) XOR C(0);
 C(1) <= (A(0) AND B_xor(0)) OR (C(0) AND (A(0) XOR B_xor(0)));

 S(1) <= A(1) XOR B_xor(1) XOR C(1);
 C(2) <= (A(1) AND B_xor(1)) OR (C(1) AND (A(1) XOR B_xor(1)));

 S(2) <= A(2) XOR B_xor(2) XOR C(2);
 C(3) <= (A(2) AND B_xor(2)) OR (C(2) AND (A(2) XOR B_xor(2)));

 S(3) <= A(3) XOR B_xor(3) XOR C(3);
 C(4) <= (A(3) AND B_xor(3)) OR (C(3) AND (A(3) XOR B_xor(3)));
 end process;

 C_out <= C(4);
 V <= C(4) XOR C(3); -- Overflow detection
end Behavioral;
```

## 8. Overflow Detection

### 8.1 Theory

In signed arithmetic using two's complement, overflow occurs when the result exceeds the representable range. For n-bit signed numbers, the range is [−2^(n−1), 2^(n−1) − 1].

### 8.2 Detection Logic

**Overflow (V) = C*n ⊕ C*(n−1)**

Where:

- C_n = carry-out from the most significant bit (MSB) stage
- C\_(n−1) = carry-in to the MSB stage

_Proof:_ Overflow occurs when:

1. Adding two positive numbers produces a negative result (C*n = 0, C*(n−1) = 1)
2. Adding two negative numbers produces a positive result (C*n = 1, C*(n−1) = 0)

Both conditions are detected by XOR of the two carry bits.

### 8.3 Example

Add +6 and +5 in 4-bit signed arithmetic:

```
 0110 (+6)
+ 0101 (+5)
--------
 1011 (-5 in 2's complement, INCORRECT)

C_out = 0, C_in(MSB) = 1
V = 0 ⊕ 1 = 1 → Overflow detected
```

## 9. Numerical Problems

### Problem 1

Given a 4-bit ripple carry adder with full adder propagation delay of 15ns, calculate the worst-case delay for adding two 8-bit numbers.

**Solution:**
Worst-case delay = n × t_fa = 8 × 15ns = 120ns

### Problem 2

For a full adder with A=1, B=1, C_in=1, determine the outputs using the derived expressions.

**Solution:**
S = A ⊕ B ⊕ C_in = 1 ⊕ 1 ⊕ 1 = 1 ⊕ 1 = 0 ⊕ 1 = 1
C_out = AB + (A ⊕ B)C_in = 1·1 + (1⊕1)·1 = 1 + 0·1 = 1
