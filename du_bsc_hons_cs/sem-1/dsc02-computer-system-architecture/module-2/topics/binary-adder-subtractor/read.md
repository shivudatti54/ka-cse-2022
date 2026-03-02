# Binary Adder Subtractor

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

### 1.1 What is a Binary Adder/Subtractor?

A **Binary Adder** is a digital circuit that performs arithmetic addition of binary numbers. Similarly, a **Binary Subtractor** performs subtraction of binary numbers. These are fundamental building blocks of every digital computer system, from simple calculators to complex processors.

### 1.2 Real-World Relevance

In modern computing, these circuits form the **arithmetic logic unit (ALU)** — the heart of any processor. Consider these applications:

- **Microprocessors**: Every instruction involving addition or subtraction (like `ADD`, `SUB`, `INC`, `DEC` in assembly) is executed using adder/subtractor circuits
- **Digital Signal Processing (DSP)**: Used in filters, Fourier transforms, and signal compression
- **Cryptography**: Modern encryption algorithms perform extensive binary arithmetic
- **Graphical Processing Units (GPUs)**: Parallel adder circuits enable massive parallel computations for graphics and AI
- **Embedded Systems**: From digital watches to automotive control units

### 1.3 Delhi University Syllabus Context

This topic aligns with **Unit III: Data Representation and Computer Arithmetic** of the BSc (Hons) Computer Science syllabus under NEP 2024 UGCF. Students must understand both the theoretical principles and practical implementation of these circuits.

---

## 2. Fundamental Concepts Review

### 2.1 Binary Number System

Before studying adders and subtractors, recall:

| Decimal | Binary |
|---------|--------|
| 0       | 0000   |
| 1       | 0001   |
| 2       | 0010   |
| 3       | 0011   |
| 4       | 0100   |
| 5       | 0101   |
| 6       | 0110   |
| 7       | 0111   |
| 8       | 1000   |
| 9       | 1001   |
| 10      | 1010   |

### 2.2 Binary Addition Rules

```
0 + 0 = 0 (Sum = 0, Carry = 0)
0 + 1 = 1 (Sum = 1, Carry = 0)
1 + 0 = 1 (Sum = 1, Carry = 0)
1 + 1 = 0 (Sum = 0, Carry = 1)
1 + 1 + 1 = 1 (Sum = 1, Carry = 1)
```

### 2.3 Binary Subtraction Rules (Using 2's Complement)

```
0 - 0 = 0 (Borrow = 0)
1 - 0 = 1 (Borrow = 0)
1 - 1 = 0 (Borrow = 0)
0 - 1 = 1 (Borrow = 1)
```

---

## 3. Half Adder

### 3.1 Definition

A **Half Adder** is the simplest combinational circuit that adds two single-bit binary numbers. It produces a **Sum** (S) and a **Carry** (C).

### 3.2 Truth Table

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 | 0       | 0         |
| 0 | 1 | 1       | 0         |
| 1 | 0 | 1       | 0         |
| 1 | 1 | 0       | 1         |

### 3.3 Boolean Expressions

```
Sum (S) = A ⊕ B (XOR gate)
Carry (C) = A · B (AND gate)
```

### 3.4 Circuit Diagram

```
        _____
   A ---|     \
        | XOR  )--- Sum (S)
   B ---|_____/
        
        _____
   A ---|     \
        | AND  )--- Carry (C)
   B ---|_____/
```

### 3.5 Implementation

**Using Logic Gates:**
- Sum: XOR gate
- Carry: AND gate

**Verilog HDL Implementation:**

```verilog
module half_adder (
    input A,
    input B,
    output Sum,
    output Carry
);
    assign Sum = A ^ B;   // XOR operation
    assign Carry = A & B; // AND operation
endmodule
```

### 3.6 Limitation

The Half Adder **cannot** handle a carry input from a previous stage. This limitation leads to the development of the Full Adder.

---

## 4. Full Adder

### 4.1 Definition

A **Full Adder** adds three one-bit binary numbers: two significant bits (A, B) and an incoming **carry** (Cin). It produces a Sum (S) and Carry out (Cout).

### 4.2 Truth Table

| A | B | Cin | Sum (S) | Cout |
|---|---|-----|---------|------|
| 0 | 0 | 0   | 0       | 0    |
| 0 | 0 | 1   | 1       | 0    |
| 0 | 1 | 0   | 1       | 0    |
| 0 | 1 | 1   | 0       | 1    |
| 1 | 0 | 0   | 1       | 0    |
| 1 | 0 | 1   | 0       | 1    |
| 1 | 1 | 0   | 0       | 1    |
| 1 | 1 | 1   | 1       | 1    |

### 4.3 Boolean Expressions

**Sum (S):**
```
S = A ⊕ B ⊕ Cin
S = A'B'Cin + A'BCin' + AB'Cin' + ABCin
```

**Carry Out (Cout):**
```
Cout = AB + ACin + BCin
Cout = ABCin + AB'Cin + A'BCin + A BCin'
```

### 4.4 Circuit Diagram

```
                    _____
           A -------|     \
                    |      )----\
           B -------|_____/       \     _____
                             -----|     \
           Cin ----------------| XOR  )---- Sum (S)
                                 |_____/
                                         
                    _____
           A -------|     \
                    |      )----\
           B -------|_____/       \     _____
                             -----|     \
           Cin ----------------| AND  )----\
                                 |_____/    \     _____
                                            \    |     \
           A --------------------------------|     \    |      )---- Cout
           B --------------------------------|_____/    | AND  |
           Cin ------------------------------------------|______|
```

### 4.5 Implementation Using Two Half Adders

A full adder can be constructed using **two half adders** and one OR gate:

```
         A          B              A          B
         |          |              |          |
    +----+---+      |         +----+---+      |
    |         |     |         |         |     |
    | HA1     |     |         | HA2     |     |
    | Sum1    |     |         | Sum2    |     |
    +----+---+-+    |         +----+---+-+    |
         |   |     |              |   |      |
         |   +--+--+              |   +---+  |
         |      |                 |       |  |
         |   +--+--+              +---+---+  |
         |   |  |                    |   |   |
    +----+---+--+--+-------------+---+---+---+--+
    |                |            |           |
    |      OR Gate   |            |           |
    |     Cout       |            |           |
    +----------------+------------+-----------+
                                           |
                                      Sum (S)
```

**Logic:**
- First Half Adder: Sum1 = A ⊕ B, Carry1 = A·B
- Second Half Adder: Sum2 = Sum1 ⊕ Cin = A ⊕ B ⊕ Cin (This is S)
- Carry Out = Carry1 + (B·Cin) + (A·Cin) = AB + ACin + BCin

### 4.6 Verilog Implementation

```verilog
module full_adder (
    input A,
    input B,
    input Cin,
    output Sum,
    output Cout
);
    // Using continuous assignment
    assign Sum = A ^ B ^ Cin;
    assign Cout = (A & B) | (B & Cin) | (A & Cin);
endmodule
```

---

## 5. Binary Parallel Adder (Ripple Carry Adder)

### 5.1 Definition

A **Parallel Adder** adds two n-bit binary numbers simultaneously. The most common implementation is the **Ripple Carry Adder (RCA)**, where full adders are cascaded in series.

### 5.2 Circuit Diagram (4-bit Parallel Adder)

```
A3 ----->|FA3|----> Sum3
         |    |<---- C3
B3 ----->|    |
              |
A2 ----->|FA2|----> Sum2
         |    |<---- C2
B2 ----->|    |
              |
A1 ----->|FA1|----> Sum1
         |    |<---- C1
B1 ----->|    |
              |
A0 ----->|FA0|----> Sum0
         |    |<---- C0
B0 ----->|    |
         |    |
Cin=0 -->|    |
```

### 5.3 Working Principle

1. **Least Significant Bit (LSB)**: The first full adder (FA0) takes A0, B0, and Cin (usually 0)
2. **Ripple Effect**: The carry output (C0) from FA0 becomes the carry input (C1) for FA1
3. **Propagation**: This continues for all stages
4. **Final Result**: The final carry out (C4) indicates overflow in unsigned addition

### 5.4 Boolean Expressions for 4-bit RCA

For each stage `i` (where i = 0 to 3):
```
Sum[i] = A[i] ⊕ B[i] ⊕ Carry[i]
Carry[i+1] = (A[i] · B[i]) + (Carry[i] · (A[i] ⊕ B[i]))
```

### 5.5 Timing Analysis

**Total Propagation Delay:** The worst-case delay occurs when:
- The carry must propagate from LSB to MSB
- Delay = n × t (where t = propagation delay of one full adder)

For a 4-bit RCA: `Total Delay = 4 × t`

### 5.6 Verilog Implementation

```verilog
module ripple_carry_adder #(
    parameter WIDTH = 4
)(
    input [WIDTH-1:0] A,
    input [WIDTH-1:0] B,
    input Cin,
    output [WIDTH-1:0] Sum,
    output Cout
);
    wire [WIDTH:0] carry;
    assign carry[0] = Cin;
    
    genvar i;
    generate
        for (i = 0; i < WIDTH; i = i + 1) begin : adder_stage
            full_adder FA (
                .A(A[i]),
                .B(B[i]),
                .Cin(carry[i]),
                .Sum(Sum[i]),
                .Cout(carry[i+1])
            );
        end
    endgenerate
    
    assign Cout = carry[WIDTH];
endmodule
```

### 5.7 Numerical Example

**Problem:** Add `A = 1011 (11)` and `B = 0110 (6)` using 4-bit RCA

**Solution:**

| Stage | A | B | Cin | Sum | Cout |
|-------|---|---|-----|-----|------|
| 0     | 1 | 0 | 0   | 1   | 0    |
| 1     | 1 | 1 | 0   | 0   | 1    |
| 2     | 0 | 1 | 1   | 0   | 1    |
| 3     | 1 | 0 | 1   | 0   | 1    |

**Result:** `Sum = 10001 (17)` ✓
**Verification:** 11 + 6 = 17 ✓

---

## 6. Carry Look-Ahead Adder (CLA)

### 6.1 The Problem with RCA

In Ripple Carry Adder, each full adder must wait for the carry from the previous stage. This creates a **propagation delay** that increases linearly with the number of bits. For n-bit addition, the delay is O(n).

### 6.2 Solution: Carry Look-Ahead

The **Carry Look-Ahead Adder** solves this by computing carries **in parallel** using generate and propagate functions.

### 6.3 Key Concepts

**Generate (Gi):** A carry is generated at stage i regardless of input carry
```
Gi = Ai · Bi
```

**Propagate (Pi):** A carry at stage i is passed to stage i+1
```
Pi = Ai ⊕ Bi
```

**Carry Equations:**
```
C1 = G0 + P0·C0
C2 = G1 + P1·G0 + P1·P0·C0
C3 = G2 + P2·G1 + P2·P1·G0 + P2·P1·P0·C0
```

### 6.4 4-bit CLA Block Diagram

```
        Ai, Bi
          |
    +-----+-----+
    | Generate |---- Gi
    |   Unit   |
    +----------+
          |
    +-----+-----+    +---------+
    | Propagate|----|  CLA    |
    |   Unit   |    |  Logic  |
    +----------+    +---------+

Ai, Bi, Pi, Gi  -------------------->  Sum Generation
                                     (XOR gates)
```

### 6.5 Circuit for Carry Look-Ahead Logic (4-bit)

```
C1 = G0 + P0·C0
C2 = G1 + P1·G0 + P1·P0·C0
C3 = G2 + P2·G1 + P2·P1·G0 + P2·P1·P0·C0
C4 = G3 + P3·G2 + P3·P2·G1 + P3·P2·P1·G0 + P3·P2·P1·P0·C0
```

### 6.6 Advantages of CLA

| Feature | RCA | CLA |
|---------|-----|-----|
| Delay   | O(n) | O(log n) |
| Speed   | Slow | Fast |
| Hardware| Less | More |
| Cost    | Low  | High |

### 6.7 Verilog Implementation

```verilog
module carry_lookahead_adder #(
    parameter WIDTH = 4
)(
    input [WIDTH-1:0] A,
    input [WIDTH-1:0] B,
    input Cin,
    output [WIDTH-1:0] Sum,
    output Cout
);
    wire [WIDTH-1:0] P, G;
    wire [WIDTH:0] C;
    
    assign C[0] = Cin;
    
    // Generate and Propagate
    genvar i;
    generate
        for (i = 0; i < WIDTH; i = i + 1) begin : gp_logic
            assign G[i] = A[i] & B[i];
            assign P[i] = A[i] ^ B[i];
        end
    endgenerate
    
    // Carry Look-Ahead Logic
    assign C[1] = G[0] | (P[0] & C[0]);
    assign C[2] = G[1] | (P[1] & G[0]) | (P[1] & P[0] & C[0]);
    assign C[3] = G[2] | (P[2] & G[1]) | (P[2] & P[1] & G[0]) | 
                  (P[2] & P[1] & P[0] & C[0]);
    assign C[4] = G[3] | (P[3] & G[2]) | (P[3] & P[2] & G[1]) |
                  (P[3] & P[2] & P[1] & G[0]) | 
                  (P[3] & P[2] & P[1] & P[0] & C[0]);
    
    // Sum generation
    generate
        for (i = 0; i < WIDTH; i = i + 1) begin : sum_logic
            assign Sum[i] = P[i] ^ C[i];
        end
    endgenerate
    
    assign Cout = C[WIDTH];
endmodule
```

---

## 7. Binary Subtractor

### 7.1 Half Subtractor

#### Truth Table

| A | B | Difference (D) | Borrow (Br) |
|---|---|----------------|-------------|
| 0 | 0 | 0              | 0           |
| 0 | 1 | 1              | 1           |
| 1 | 0 | 1              | 0           |
| 1 | 1 | 0              | 0           |

#### Boolean Expressions

```
Difference (D) = A ⊕ B
Borrow (Br) = A' · B
```

#### Circuit Diagram

```
        _____
   A ---|     \
        | XOR  )--- Difference (D)
   B ---|_____/
        
        _____
   B ---|     \
        | AND  )--- Borrow (Br)
   A ---|_____/
        NOT
```

### 7.2 Full Subtractor

A full subtractor subtracts three bits: A (minuend), B (subtrahend), and Bin (borrow from previous stage).

#### Truth Table

| A | B | Bin | Difference (D) | Bout |
|---|---|-----|----------------|------|
| 0 | 0 | 0   | 0              | 0    |
| 0 | 0 | 1   | 1              | 1    |
| 0 | 1 | 0   | 1              | 1    |
| 0 | 1 | 1   | 0              | 1    |
| 1 | 0 | 0   | 1              | 0    |
| 1 | 0 | 1   | 0              | 0    |
| 1 | 1 | 0   | 0              | 0    |
| 1 | 1 | 1   | 1              | 1    |

#### Boolean Expressions

```
Difference (D) = A ⊕ B ⊕ Bin
Borrow Out (Bout) = A'·B + A'·Bin + B·Bin
```

### 7.3 Parallel Subtractor

Similar to parallel adder, subtractors can be cascaded to form n-bit parallel subtractors.

---

## 8. Combined Adder-Subtractor Circuit

### 8.1 Using 2's Complement Method

Instead of building separate adder and subtractor circuits, we can use a **single circuit** that performs both operations based on a control signal (M).

- **M = 0**: Addition (A + B)
- **M = 1**: Subtraction (A - B)

### 8.2 Working Principle

To perform A - B using addition:
```
A - B = A + (-B) = A + (2's complement of B)
```

The 2's complement is obtained by:
1. Taking the **1's complement** (inverting all bits)
2. **Adding 1**

This can be done using **XOR gates** with a control signal!

### 8.3 Circuit Diagram

```
                    Control Signal (M)
                         |
                    +----+----+
                    |         |
                    | XOR     |
                    |         |
                    +----+----+
                         |
              B0   B1   B2   B3
               |    |    |    |
            +--+----+----+----+--+
            |                   |
            |   Parallel Adder |
            |                   |
            +-------------------+
                         |
                      A + B
```

### 8.4 Detailed Circuit

```
        M (Control)
          |
    +-----+-----+
    |           |
    |  XOR      |
    |           |
    +-----+-----+
          |
     +----+----+
     |         |
     B0  B1   B2  B3   <-- Inputs to XOR gates
     |   |    |   |
     v   v    v   v
   +---+---+---+---+
   |   |   |   |   |
   |   |   |   |   |
   +---+---+---+---+
        |   |   |
        |   Full Adders   <-- Connected in cascade
        |   |   |
        A0  A1  A2  A3
```

### 8.5 Overflow Detection

#### For Unsigned Numbers:
Overflow occurs when there's a **carry out** from the MSB during addition, or a **borrow** during subtraction.

#### For Signed Numbers (2's Complement):
Overflow occurs when:
- Adding two positive numbers gives a negative result
- Adding two negative numbers gives a positive result

**Overflow Condition:**
```
V = Cn ⊕ Cn-1
```
Where Cn is the final carry and Cn-1 is the carry into the MSB.

### 8.6 Numerical Example

**Problem:** Perform 5 - 3 using the adder-subtractor circuit (M=1)

- A = 0101 (5)
- B = 0011 (3)
- M = 1 (subtract)

**Step 1:** Invert B (1's complement)
- B' = 1100

**Step 2:** Add 1
- B'' = 1101 (2's complement of 3 = -3)

**Step 3:** Add A + B''
- 0101 + 1101 = 10010

**Result:** 0010 (2) ✓ (5 - 3 = 2)

### 8.7 Verilog Implementation

```verilog
module adder_subtractor #(
    parameter WIDTH = 4
)(
    input [WIDTH-1:0] A,
    input [WIDTH-1:0] B,
    input M,  // M=0: Add, M=1: Subtract
    output [WIDTH-1:0] Result,
    output Overflow
);
    wire [WIDTH-1:0] B_complement;
    wire [WIDTH:0] carry;
    
    // 2's complement generation using XOR and Cin
    assign B_complement = B ^ {WIDTH{1'b1}};  // 1's complement
    assign carry[0] = M;  // Add 1 for 2's complement when M=1
    
    // Perform addition with modified B
    genvar i;
    generate
        for (i = 0; i < WIDTH; i = i + 1) begin : add_sub
            full_adder FA (
                .A(A[i]),
                .B(B_complement[i]),
                .Cin(carry[i]),
                .Sum(Result[i]),
                .Cout(carry[i+1])
            );
        end
    endgenerate
    
    // Overflow detection for signed arithmetic
    assign Overflow = carry[WIDTH] ^ carry[WIDTH-1];
endmodule
```

---

## 9. BCD Adder

### 9.1 Introduction

**BCD (Binary Coded Decimal)** represents each decimal digit (0-9) using 4 binary bits:

| Decimal | BCD |
|---------|-----|
| 0       | 0000|
| 1       | 0001|
| 2       | 0010|
| ...     | ... |
| 9       | 1001|

### 9.2 Why BCD Adder?

When adding two BCD numbers, regular binary addition may produce invalid codes (1010 to 1111) or require correction.

### 9.3 BCD Addition Algorithm

1. Add two 4-bit BCD numbers using binary addition
2. If result > 9 (or carry = 1), add 0110 (6) to correct
3. Generate proper carry for next digit

### 9.4 Circuit

```
    A (BCD) ----->|           |
    B (BCD) ----->| Binary    |---- Sum ---->| Correction |---- Result
                  | Adder     |              | Logic      |
                  |           |              |            |
                  +-----------+              +------------+
                         |                         |
                        +6                        +6 (if needed)
                         |                         |
                         +-------------------------+
                                          |
                                       Carry Out
```

### 9.5 Numerical Example

**Problem:** Add 5 + 8 in BCD

- 5 = 0101 (BCD)
- 8 = 1000 (BCD)

**Step 1:** Binary addition
- 0101 + 1000 = 1101 (13)

**Step 2:** Check (1101 > 1001 = 9), so add 0110
- 1101 + 0110 = 10011

**Step 3:** Result = 0001 (carry) 0011 (3)
- Final BCD: 0001 0011 → 13 ✓

---

## 10. Practical Examples and Numerical Problems

### Problem 1: 8-bit Ripple Carry Addition

**Question:** Add `A = 11001010` and `B = 10110100`

**Solution:**

```
       11001010
     + 10110100
     ----------
       101111110
```

Binary: 101111110 = 190 (decimal)
Verification: 202 + 180 = 382 ✓

### Problem 2: Signed Number Subtraction

**Question:** Subtract 25 from 50 using 8-bit 2's complement

**Solution:**
- 50 = 00110010
- 25 = 00011001
- -25 (2's complement): 11100111

```
     00110010
   + 11100111
   ----------
    100011001
```

Result: 00011001 = 25 ✓ (50 - 25 = 25)

### Problem 3: Overflow Detection

**Question:** Add +70 and +80 using 8-bit signed arithmetic

**Solution:**
- +70 = 01000110
- +80 = 01010000

```
     01000110
   + 01010000
   ----------
     10010110
```

Result: 10010110 = -106 (incorrect for signed!)

**Overflow occurred** because:
- Two positive numbers produced a negative result
- V = Cn ⊕ Cn-1 = 0 ⊕ 1 = 1 (Overflow!)

---

## 11. Assessment Questions

### Multiple Choice Questions

**Q1.** The output of a half adder is:
- (a) Sum only
- (b) Carry only
- (c) Sum and Carry
- (d) Difference only

**Answer:** (c) Sum and Carry

**Q2.** How many full adders are required to build a 4-bit parallel adder?
- (a) 2
- (b) 3
- (c) 4
- (d) 5

**Answer:** (c) 4

**Q3.** The main advantage of Carry Look-Ahead adder over Ripple Carry adder is:
- (a) Lower cost
- (b) Simpler design
- (c) Faster operation
- (d) Uses fewer gates

**Answer:** (c) Faster operation

**Q4.** For subtraction, A - B using 2's complement, B is:
- (a) Added directly
- (b) Inverted bit by bit
- (c) Converted to 2's complement
- (d) Left unchanged

**Answer:** (c) Converted to 2's complement

**Q5.** In a 4-bit signed number representation, the range is:
- (a) 0 to 15
- (b) -7 to +7
- (c) -8 to +7
- (d) -16 to +15

**Answer:** (c) -8 to +7

### Short Answer Questions

**Q1.** Explain why half adder cannot be used for adding multi-bit numbers.

**Q2.** Derive the boolean expression for sum output of a full adder.

**Q3.** What is overflow in binary arithmetic? Under what conditions does it occur?

**Q4.** Explain the difference between ripple carry and carry look-ahead adders.

**Q5.** How does the adder-subtractor circuit work using a single control signal?

### Long Answer Questions

**Q1.** Design a 4-bit binary parallel adder using full adders. Explain its working with a numerical example.

**Q2.** (a) Explain the concept of generate and propagate signals in Carry Look-Ahead Adder.
   (b) Design a 4-bit CLA and explain its advantages over RCA.

**Q3.** Design a circuit that can add or subtract two 4-bit binary numbers based on a control input M. Include overflow detection logic.

---

## 12. Key Takeaways

1. **Half Adder**: Adds 2 single-bit numbers, produces Sum (A⊕B) and Carry (A·B)

2. **Full Adder**: Adds 3 single-bit numbers (A, B, Cin), fundamental building block for n-bit addition

3. **Ripple Carry Adder**: Cascaded full adders; simple but slow due to sequential carry propagation

4. **Carry Look-Ahead Adder**: Uses generate (Gi = Ai·Bi) and propagate (Pi = Ai⊕Bi) to compute carries in parallel; faster but more complex

5. **Binary Subtraction**: Can be performed using 2's complement method (A - B = A + B̅ + 1)

6. **Adder-Subtractor**: Single circuit performs both operations using XOR gates and a control signal M

7. **Overflow Detection**:
   - Unsigned: Carry out from MSB
   - Signed: V = Cn ⊕ Cn-1

8. **BCD Adder**: Requires correction when binary sum exceeds 9 (add 0110)

9. **Practical Applications**: These circuits form the ALU of processors, enabling all arithmetic operations in computing

---

## References

1. Morris Mano, M. (2017). *Digital Design* (5th ed.). Pearson Education.
2. Floyd, T. L. (2014). *Digital Fundamentals* (10th ed.). Pearson Education.
3. Delhi University NEP 2024 UGCF Syllabus — Computer System Architecture
4. Verilog HDL by Samir Palnitkar (2nd ed.)

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University as per NEP 2024 UGCF guidelines.*