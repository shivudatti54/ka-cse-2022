# Boolean Algebra and Digital Circuits

## BSc (Hons) Computer Science — NEP 2024 UGCF, Delhi University

---

## Introduction

Boolean algebra serves as the mathematical foundation of all digital systems and computer architecture. Developed by mathematician George Boole in 1854, this algebraic system operates on binary variables that can take only two values: 0 (representing false or logical 0/LOW) or 1 (representing true or logical 1/HIGH). Every digital device—from the smartphone in your pocket to the most powerful supercomputer—relies on Boolean algebra to perform computations, make decisions, and process information at incredible speeds.

In the context of the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, this unit forms the bedrock for understanding how hardware components such as processors, memory units, and Arithmetic Logic Units (ALUs) function. The concepts covered here directly relate to the design and optimization of combinational and sequential digital circuits.

This study material provides comprehensive coverage of Boolean algebra fundamentals, canonical forms, simplification techniques using Karnaugh maps, logic gate implementations, and practical digital circuits including adders and multiplexers.

---

## 1. Fundamentals of Boolean Algebra

### 1.1 Boolean Variables and Constants

A **Boolean variable** represents a quantity that can have only two states. In digital electronics, these correspond to voltage levels:

- **Logic 0**: Typically 0V (ground)
- **Logic 1**: Typically 5V or 3.3V (Vcc)

**Boolean constants** are simply 0 and 1. Variables are usually represented by letters (A, B, C, X, Y, etc.) and can be either complemented (A̅ or A') or uncomplemented.

### 1.2 Basic Boolean Operations

Boolean algebra relies on three fundamental operations:

| Operation | Symbol | Definition |
|-----------|--------|------------|
| AND | · or ∧ | Output is 1 only when ALL inputs are 1 |
| OR | + or ∨ | Output is 1 when ANY input is 1 |
| NOT | ¬ or ' | Inverts the input value |

**Truth Tables for Basic Operations:**

**AND Operation (Logical Multiplication):**
| A | B | A · B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

**OR Operation (Logical Addition):**
| A | B | A + B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   1   |

**NOT Operation (Inversion/Complement):**
| A | A' or Ā |
|---|---------|
| 0 |    1    |
| 1 |    0    |

### 1.3 Boolean Laws and Theorems

**Identity Laws:**
- A + 0 = A
- A · 1 = A

**Null/Boundary Laws:**
- A + 1 = 1
- A · 0 = 0

**Idempotent Laws:**
- A + A = A
- A · A = A

**Complement Laws:**
- A + A' = 1
- A · A' = 0

**Commutative Laws:**
- A + B = B + A
- A · B = B · A

**Associative Laws:**
- (A + B) + C = A + (B + C)
- (A · B) · C = A · (B · C)

**Distributive Laws:**
- A · (B + C) = (A · B) + (A · C)
- A + (B · C) = (A + B) · (A + C)

**Absorption Laws:**
- A + (A · B) = A
- A · (A + B) = A

**De Morgan's Theorems** (Critical for circuit simplification):
- **(Theorem 1):** (A + B)' = A' · B'
- **(Theorem 2):** (A · B)' = A' + B'

**Proof of De Morgan's Theorem 1 using truth table:**

| A | B | A + B | (A + B)' | A' | B' | A' · B' |
|---|---|-------|----------|----|----|---------|
| 0 | 0 |   0   |    1     | 1  | 1  |    1    |
| 0 | 1 |   1   |    0     | 1  | 0  |    0    |
| 1 | 0 |   1   |    0     | 0  | 1  |    0    |
| 1 | 1 |   1   |    0     | 0  | 0  |    0    |

Since (A + B)' = A' · B' for all combinations, the theorem is proven.

---

## 2. Boolean Functions and Canonical Forms

### 2.1 Boolean Expression

A Boolean expression is an algebraic expression formed using Boolean variables and the three basic operations. For example:

F(A, B, C) = A·B + A·C' + B·C

### 2.2 Sum of Products (SOP) Form

In SOP form, the expression is a sum (OR) of product (AND) terms. Each product term is called a **minterm**.

**Example:** F(A, B, C) = A·B·C + A·B·C' + A·B'·C

The minterms where F = 1 are: m(1, 3, 5) or Σm(1,3,5)

### 2.3 Product of Sums (POS) Form

In POS form, the expression is a product (AND) of sum (OR) terms. Each sum term is called a **maxterm**.

**Example:** F(A, B, C) = (A + B + C) · (A + B + C') · (A + B' + C)

The maxterms where F = 0 are: M(0, 2, 4) or ΠM(0,2,4)

### 2.4 Conversion Between SOP and POS

**Relationship between minterms and maxterms:**
- M(i) = m(i)'

For a 3-variable function:
- If SOP uses minterms: m(1, 3, 5)
- Then POS uses maxterms: M(0, 2, 4, 6, 7)

**Example 1: Convert SOP to POS**

Given F = Σm(0, 2, 4)
- SOP minterms: 0, 2, 4
- POS maxterms: All except 0, 2, 4 → 1, 3, 5, 6, 7
- POS: F = ΠM(1, 3, 5, 6, 7) = (A + B + C)(A + B' + C)(A + B' + C')(A' + B + C')(A' + B' + C')

---

## 3. Karnaugh Map (K-Map) Method

Karnaugh maps provide a graphical method for simplifying Boolean expressions. They are particularly effective for functions with up to 4-6 variables.

### 3.1 K-Map Structure

**2-Variable K-Map:**

| AB\A | 0 | 1 |
|------|---|---|
| **0** | m0 | m2 |
| **1** | m1 | m3 |

Where: m0 = A'B', m1 = A'B, m2 = AB', m3 = AB

**3-Variable K-Map:**

| AB\C | 0 | 1 |
|------|---|---|
| 00   | m0 | m4 |
| 01   | m1 | m5 |
| 11   | m3 | m7 |
| 10   | m2 | m6 |

**4-Variable K-Map:**

| AB\CD | 00 | 01 | 11 | 10 |
|-------|----|----|----|----|
| 00    | m0 | m4 | m12| m8 |
| 01    | m1 | m5 | m13| m9 |
| 11    | m3 | m7 | m15| m11|
| 10    | m2 | m6 | m14| m10|

### 3.2 Grouping Rules

1. Groups must contain 1, 2, 4, 8, 16... cells (powers of 2)
2. Groups must be rectangular
3. Wrap-around is allowed (edges connect)
4. Each '1' must be included in at least one group
5. Groups should be as large as possible
6. Minimize the number of groups

### 3.3 Simplification Process

**Example 2: Simplify using K-Map**

Given F(A, B, C) = Σm(0, 1, 3, 5, 7)

**Step 1: Fill the 3-variable K-Map**

| AB\C | 0 | 1 |
|------|---|---|
| 00   | 1 | 0 |
| 01   | 1 | 1 |
| 11   | 0 | 1 |
| 10   | 0 | 0 |

**Step 2: Group the 1s**

- Group 1: Cells (0,0), (0,1) → wraps vertically → B' (A'B' + A'B = A')
- Group 2: Cells (1,1), (3,1), (7,1) → vertical group of 4 → C
- Group 3: Cells (1,0), (3,0) → horizontal pair → A'C'

**Step 3: Write simplified expression**

F = B' + C + A'C'

Using absorption law: C + A'C' = C + A' (since C + A'C' = (C + A')(C + C') = C + A')

**Final simplified expression: F = B' + C + A'**

This is significantly simpler than the original 5-literal expression!

---

## 4. Logic Gates

### 4.1 Basic Gates

| Gate | Symbol | Boolean Expression | Output is 1 when... |
|------|--------|---------------------|---------------------|
| AND | ![AND] | Y = A · B | Both A AND B are 1 |
| OR | ![OR] | Y = A + B | Either A OR B is 1 |
| NOT | ![NOT] | Y = A' | Input is 0 |

### 4.2 Universal Gates

**NAND Gate** and **NOR Gate** are called universal gates because any Boolean function can be implemented using only NAND gates or only NOR gates.

#### NAND as Universal Gate

**Implementing NOT using NAND:**
- NOT A = (A · A)' = A NAND A

**Implementing AND using NAND:**
- A · B = ((A · B)')' = (A NAND B)'

**Implementing OR using NAND:**
- A + B = (A' · B')' = (A NAND A) · (B NAND B)'

#### NOR as Universal Gate

**Implementing NOT using NOR:**
- NOT A = (A + A)' = A NOR A

**Implementing OR using NOR:**
- A + B = ((A + B)')' = (A NOR B)'

**Implementing AND using NOR:**
- A · B = (A' + B')' = (A NOR A) + (B NOR B)'

### 4.3 Other Important Gates

| Gate | Expression | Output is 1 when... |
|------|------------|---------------------|
| XOR | A ⊕ B = A'B + AB' | Inputs are different |
| XNOR | (A ⊕ B)' = AB + A'B' | Inputs are equal |

**XOR Truth Table:**
| A | B | A ⊕ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

---

## 5. Combinational Digital Circuits

### 5.1 Adders

Adders are fundamental arithmetic circuits that perform binary addition.

#### Half Adder

A half adder adds two single-bit numbers.

**Truth Table:**
| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

**Boolean Expressions:**
- Sum (S) = A ⊕ B = A'B + AB'
- Carry (C) = A · B

**Implementation:**
- Sum = XOR gate
- Carry = AND gate

#### Full Adder

A full adder adds three bits: two significant bits and a carry-in.

**Truth Table:**
| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |  0   |
| 0 | 0 |  1  |  1  |  0   |
| 0 | 1 |  0  |  1  |  0   |
| 0 | 1 |  1  |  0  |  1   |
| 1 | 0 |  0  |  1  |  0   |
| 1 | 0 |  1  |  0  |  1   |
| 1 | 1 |  0  |  0  |  1   |
| 1 | 1 |  1  |  1  |  1   |

**Boolean Expressions:**
- Sum (S) = A ⊕ B ⊕ Cin = A'B'Cin + A'BCin' + AB'Cin' + ABCin
- Carry Out (Cout) = AB + ACin + BCin

**Simplified using K-Map:**
- S = A ⊕ B ⊕ Cin
- Cout = AB + Cin(A ⊕ B)

#### Ripple Carry Adder

A ripple carry adder is constructed by connecting multiple full adders in cascade, where the Cout of each stage becomes the Cin of the next.

**4-bit Ripple Carry Adder Structure:**

```
A3 A2 A1 A0
     +   +
B3 B2 B1 B0
     |   |
[FA][FA][FA][FA]
     |   |
Cout S3 S2 S1 S0
```

### 5.2 Multiplexers (MUX)

A multiplexer is a combinational circuit that selects one of many input lines and directs it to a single output line. The selection is controlled by select lines.

**4-to-1 Multiplexer:**

| S1 | S0 | Output Y |
|----|----|----------|
| 0  | 0  | I0       |
| 0  | 1  | I1       |
| 1  | 0  | I2       |
| 1  1 |  I3       |

**Boolean Expression:**
Y = S1'S0'I0 + S1'S0I1 + S1S0'I2 + S1S0I3

**Implementation using gates:**
- Y = (S1' · S0' · I0) + (S1' · S0 · I1) + (S1 · S0' · I2) + (S1 · S0 · I3)

**2-to-1 Multiplexer (Commonly Used):**
Y = S'I0 + SI1

**Code Implementation (Verilog HDL):**

```verilog
module mux_4to1(
    input [3:0] I,      // 4 input lines
    input [1:0] S,      // 2 select lines
    output reg Y        // output
);
    always @(*)
    begin
        case(S)
            2'b00: Y = I[0];
            2'b01: Y = I[1];
            2'b10: Y = I[2];
            2'b11: Y = I[3];
            default: Y = 1'b0;
        endcase
    end
endmodule
```

---

## 6. Worked Examples

### Example 1: Simplify the Boolean Expression Using Boolean Algebra

**Problem:** Simplify F = (A + B)' (A' + B) + AB

**Solution:**

**Step 1:** Apply De Morgan's theorem to (A + B)'
(A + B)' = A' · B'

**Step 2:** Substitute
F = (A' · B')(A' + B) + AB

**Step 3:** Apply distributive law
= A'A' + A'B + B'A' + B'B + AB

**Step 4:** Simplify using idempotent (A'A' = A') and complement (B'B = 0)
= A' + A'B + A'B' + 0 + AB

**Step 5:** Apply absorption law (A' + A'B = A')
= A' + A'B' + AB

**Step 6:** Factor A'
= A'(1 + B') + AB = A' + AB

**Step 7:** Apply absorption again (A' + AB = A' + B)
= A' + B

**Final Simplified Expression: F = A' + B**

### Example 2: Design a 2-bit Magnitude Comparator

**Problem:** Design a circuit that compares two 2-bit numbers A(A1A0) and B(B1B0) and produces three outputs:
- G (A > B)
- E (A = B)
- L (A < B)

**Solution:**

**Truth Table:**

| A1 | A0 | B1 | B0 | G | E | L |
|----|----|----|----|---|---|---|
| 0  | 0  | 0  | 0  | 0 | 1 | 0 |
| 0  | 0  | 0  | 1  | 0 | 0 | 1 |
| 0  | 0  | 1  | 0  | 0 | 0 | 1 |
| 0  | 0  | 1  | 1  | 0 | 0 | 1 |
| 0  | 1  | 0  | 0  | 1 | 0 | 0 |
| 0  | 1  | 0  | 1  | 0 | 1 | 0 |
| 0  | 1  | 1  | 0  | 0 | 0 | 1 |
| 0  | 1  | 1  | 1  | 0 | 0 | 1 |
| 1  | 0  | 0  | 0  | 1 | 0 | 0 |
| 1  | 0  | 0  | 1  | 1 | 0 | 0 |
| 1  | 0  | 1  | 0  | 0 | 1 | 0 |
| 1  | 0  | 1  | 1  | 0 | 0 | 1 |
| 1  | 1  | 0  | 0  | 1 | 0 | 0 |
| 1  | 1  | 0  | 1  | 1 | 0 | 0 |
| 1  | 1  | 1  | 0  | 1 | 0 | 0 |
| 1  | 1  | 1  | 1  | 0 | 1 | 0 |

**Simplified Expressions using K-Maps:**

For G (A > B):
- G = A1B1' + A0B1'B0' + A1A0B0'

For E (A = B):
- E = (A1 ⊕ B1)' · (A0 ⊕ B0)' = (A1XnorB1) · (A0XnorB0)

For L (A < B):
- L = A1'B1 + A0'A1'B0 + A0'B1B0'

---

## 7. Multiple Choice Questions

### Level 1: Basic Knowledge

1. **The Boolean variable can have:**
   - a) Only 0 value
   - b) Only 1 value
   - c) 0 or 1 value
   - d) Any value
   
   **Answer:** (c)

2. **Which law states that A + A = A?**
   - a) Identity Law
   - b) Idempotent Law
   - c) Complement Law
   - d) Absorption Law
   
   **Answer:** (b)

### Level 2: Application

3. **The complement of A + B is:**
   - a) A' + B'
   - b) A'B'
   - c) AB
   - d) A + B'
   
   **Answer:** (b) [De Morgan's Theorem]

4. **A 4-to-1 multiplexer has:**
   - a) 2 select lines
   - b) 4 select lines
   - c) 8 select lines
   - d) 1 select line
   
   **Answer:** (a)

5. **The output of XOR gate is 1 when:**
   - a) All inputs are 1
   - b) All inputs are 0
   - c) Inputs are different
   - d) Inputs are equal
   
   **Answer:** (c)

### Level 3: Analysis

6. **Simplify: A + A'B**
   - a) A + B
   - b) A
   - c) A + A'B
   - d) A + B'
   
   **Answer:** (a) [Absorption Law: A + A'B = (A + A')(A + B) = 1(A + B) = A + B]

7. **How many minterms exist for 4 Boolean variables?**
   - a) 4
   - b) 8
   - c) 12
   - d) 16
   
   **Answer:** (d) [2^n = 2^4 = 16]

8. **Which gate is called a universal gate?**
   - a) AND
   - b) OR
   - c) NAND
   - d) XOR
   
   **Answer:** (c)

### Level 4: Advanced

9. **A full adder adds:**
   - a) Two 1-bit numbers
   - b) Two 2-bit numbers
   - c) Three 1-bit numbers
   - d) One 1-bit and one 2-bit number
   
   **Answer:** (c)

10. **The expression (A + B + C)' is equivalent to:**
    - a) A'B'C'
    - b) A' + B' + C'
    - c) A'B' + B'C' + A'C'
    - d) ABC
    
    **Answer:** (c) [Extended De Morgan's: (A+B+C)' = A'B'C']

11. **In a K-map with 8 cells, the maximum group size is:**
    - a) 2
    - b) 4
    - c) 8
    - d) 16
    
    **Answer:** (c)

12. **The carry output of a full adder is given by:**
    - a) A ⊕ B ⊕ Cin
    - b) AB + ACin + BCin
    - c) A + B + Cin
    - d) A'B + BCin + A'Cin
    
    **Answer:** (b)

---

## 8. Flashcards

| Term | Definition |
|------|------------|
| **Boolean Algebra** | Mathematical system dealing with binary variables (0 and 1) and operations AND, OR, NOT |
| **Minterm** | Product term that includes all variables in either complemented or uncomplemented form; equals 1 for exactly one input combination |
| **Maxterm** | Sum term that includes all variables; equals 0 for exactly one input combination |
| **Karnaugh Map** | Graphical method for simplifying Boolean expressions using grouped 1s (for SOP) or 0s (for POS) |
| **Universal Gate** | A gate (NAND or NOR) that can implement any Boolean function alone |
| **Half Adder** | Combinational circuit that adds two 1-bit numbers, producing sum and carry outputs |
| **Full Adder** | Circuit that adds three bits (two operands + carry-in), producing sum and carry-out |
| **Multiplexer** | Combinational circuit that selects one of multiple inputs based on select line values |
| **De Morgan's Theorems** | Transformation rules: (A+B)' = A'·B' and (A·B)' = A'+B' |
| **XOR Gate** | Exclusive OR gate; output is 1 when inputs are different |

---

## 9. Exam Tips and Common Pitfalls

### Exam Tips:

1. **Always start with the truth table** when designing circuits—it provides clarity and prevents errors.

2. **For simplification problems**, remember:
   - K-maps are faster for up to 4 variables
   - Boolean algebra is more flexible for complex expressions
   - Always verify your simplified expression against the original using truth tables

3. **De Morgan's theorems are frequently tested**—practice applying them to nested expressions.

4. **When designing adders**, understand the difference between half adder (2 inputs) and full adder (3 inputs).

5. **For multiplexer problems**, remember the select lines determine which input is routed to output.

### Common Pitfalls to Avoid:

- Confusing SOP (Sum of Products) with POS (Product of Sums)
- Forgetting that K-map cells must be grouped in powers of 2
- Not using parentheses in complex Boolean expressions—this changes the meaning!
- Assuming XOR is the same as OR (XOR gives 1 only when inputs differ)
- Making groups overlapping unnecessarily (though allowed, larger groups are better)

---

## Key Takeaways

1. **Boolean algebra** operates on binary variables (0 and 1) using three fundamental operations: AND (·), OR (+), and NOT (').

2. **De Morgan's theorems** are essential for expression simplification and gate conversion:
   - (A + B)' = A' · B'
   - (A · B)' = A' + B'

3. **SOP (Sum of Products)** uses minterms where the function equals 1; **POS (Product of Sums)** uses maxterms where the function equals 0.

4. **Karnaugh maps** provide a systematic method for simplifying Boolean expressions up to 4 variables—groups must be powers of 2 (1, 2, 4, 8...) and should be as large as possible.

5. **NAND and NOR are universal gates**—any digital circuit can be implemented using only NAND gates or only NOR gates.

6. **Half adders** add two 1-bit numbers; **full adders** add two bits plus a carry-in; multiple full adders cascaded form a **ripple carry adder**.

7. **Multiplexers** select one input from multiple sources based on select lines—a 2^n-to-1 MUX requires n select lines.

8. **XOR and XNOR gates** are essential for arithmetic circuits and comparison operations.

---

*Reference: Delhi University BSc (Hons) Computer Science, NEP 2024 UGCF Curriculum - Unit on Boolean Algebra and Digital Circuits*