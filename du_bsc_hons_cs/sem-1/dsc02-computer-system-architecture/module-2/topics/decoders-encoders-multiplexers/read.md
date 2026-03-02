# Decoders, Encoders, and Multiplexers

## Comprehensive Study Material for Computer System Architecture

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Decoders](#2-decoders)
3. [Encoders](#3-encoders)
4. [Multiplexers](#4-multiplexers)
5. [Demultiplexers (Brief Overview)](#5-demultiplexers-brief-overview)
6. [Practical Examples and Applications](#6-practical-examples-and-applications)
7. [Assessment Questions](#7-assessment-questions)
8. [Key Takeaways](#8-key-takeaways)

---

## 1. Introduction and Real-World Relevance

### 1.1 Background

In digital computer systems, data communication and processing require efficient methods for routing, selecting, and converting information between different formats. **Combinational logic circuits** form the backbone of such operations, and among these, **decoders**, **encoders**, and **multiplexers** are fundamental building blocks that every computer architecture student must master.

These circuits are categorized as **data selector/distributor circuits** and are extensively used in:

- Memory address selection
- Data routing in processors
- Communication systems
- Digital displays
- Seven-segment displays
- Arithmetic Logic Units (ALUs)

### 1.2 Context in Delhi University Syllabus

This topic aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science, specifically under the "Computer System Architecture" paper. Students are expected to understand the internal working, design, and application of these circuits, including the ability to derive truth tables and boolean expressions.

---

## 2. Decoders

### 2.1 Definition

A **decoder** is a combinational circuit that converts binary information from n input lines to a maximum of 2ⁿ unique output lines. It is essentially the inverse of an encoder. If the decoder has n inputs, it can activate exactly one of its 2ⁿ outputs (assuming active-high outputs).

### 2.2 Types of Decoders

1. **2-to-4 Decoder**
2. **3-to-8 Decoder**
3. **4-to-16 Decoder**

### 2.3 2-to-4 Decoder

#### 2.3.1 Truth Table

| E | A₁ | A₀ | D₃ | D₂ | D₁ | D₀ |
|---|----|----|----|----|----|----|
| 0 | X  | X  | 0  | 0  | 0  | 0  |
| 1 | 0  | 0  | 0  | 0  | 0  | 1  |
| 1 | 0  | 1  | 0  | 0  | 1  | 0  |
| 1 | 1  | 0  | 0  | 1  | 0  | 0  |
| 1 | 1  | 1  | 1  | 0  | 0  | 0  |

**Note:** E is the enable input (active-high). X represents "don't care" condition.

#### 2.3.2 Boolean Expressions

```
D₀ = E · A₁' · A₀'
D₁ = E · A₁' · A₀
D₂ = E · A₁ · A₀'
D₃ = E · A₁ · A₀
```

#### 2.3.3 Logic Circuit Diagram

```
        ┌─ NOT ─┐
   A₁───┤       ├──────┐
        └───────┘      │    ┌─ NOT ─┐        ┌─ AND ─┐
                       ├─────┤       ├───────┤       ├─── D₀
                       │    └───────┘       └───────┘
   A₀──────────────────┤
                       │    ┌─ NOT ─┐        ┌─ AND ─┐
                       ├─────┤       ├───────┤       ├─── D₁
                       │    └───────┘       └───────┘
        ┌─ NOT ─┐      │
   E────┤       ├──────┘
        └───────┘
```

The circuit uses NOT gates to generate complements and AND gates for each minterm.

### 2.4 3-to-8 Decoder

#### 2.4.1 Truth Table

| E | A₂ | A₁ | A₀ | D₇ | D₆ | D₅ | D₄ | D₃ | D₂ | D₁ | D₀ |
|---|----|----|----|----|----|----|----|----|----|----|----|
| 1 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |
| 1 | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |
| 1 | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 1 | 0  | 1  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 1 | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1 | 1  | 0  | 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 1 | 1  | 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 1 | 1  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |

#### 2.4.2 Boolean Expressions

```
D₀ = A₂' · A₁' · A₀'       (m₀)
D₁ = A₂' · A₁' · A₀        (m₁)
D₂ = A₂' · A₁ · A₀'        (m₂)
D₃ = A₂' · A₁ · A₀         (m₃)
D₄ = A₂ · A₁' · A₀'        (m₄)
D₅ = A₂ · A₁' · A₀         (m₅)
D₆ = A₂ · A₁ · A₀'         (m₆)
D₇ = A₂ · A₁ · A₀          (m₇)
```

Each output represents a minterm of the input variables.

### 2.5 Implementing a 4-to-16 Decoder using Two 3-to-8 Decoders

This is an important design application:

```
         ┌─────────────────┐
    A₃───┤                │
         │   3-to-8       │── D₀ to D₇
    A₂───┤   Decoder 1    │
         │   (Enable=1)   │
    A₁───┤                │
         └─────────────────┘
              ▲
              │
              │ A₃ = 0 selects lower outputs
              │ A₃ = 1 (inverted) selects upper outputs
              │
         ┌─────────────────┐
    A₃'──┤                │
         │   3-to-8       │── D₈ to D₁₅
    A₂───┤   Decoder 2    │
         │   (Enable=1)   │
    A₁───┤                │
         └─────────────────┘
```

### 2.6 Decoder Applications

1. **Memory Address Decoding**: In computer systems, memory chips have multiple address lines. A decoder converts the high-order address bits to select a particular memory chip (chip select signal).

2. **Seven-Segment Display**: Decoders convert BCD (Binary Coded Decimal) input to the appropriate outputs to light up segments of a display.

3. **Demultiplexing**: When combined with a data line, a decoder can route a single input to multiple outputs.

4. **Implementing Boolean Functions**: Any Boolean function can be expressed as a sum of minterms and implemented using a decoder with an external OR gate.

---

## 3. Encoders

### 3.1 Definition

An **encoder** performs the inverse operation of a decoder. It converts 2ⁿ input lines into n output lines, producing the binary code corresponding to the activated input line.

### 3.2 Types of Encoders

1. **Binary Encoder (2ⁿ-to-n)**
2. **Priority Encoder**
3. **BCD Encoder**
4. **Seven-Segment Encoder**

### 3.3 4-to-2 Binary Encoder

#### 3.3.1 Truth Table

| D₃ | D₂ | D₁ | D₀ | A₁ | A₀ |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | 0  | 0  | 1  |
| 0  | 1  | 0  | 0  | 1  | 0  |
| 1  | 0  | 0  | 0  | 1  | 1  |

#### 3.3.2 Boolean Expressions

```
A₁ = D₂ + D₃
A₀ = D₁ + D₃
```

#### 3.3.3 Logic Circuit

```
        ┌───────┐
   D₃───┤       │
        │  OR   ├────── A₁
   D₂───┤       │
        └───────┘
        
        ┌───────┐
   D₃───┤       │
        │  OR   ├────── A₀
   D₁───┤       │
        └───────┘
```

### 3.4 Problem with Basic Encoders

The basic binary encoder has a critical flaw: **it doesn't handle multiple simultaneous inputs correctly**. If two inputs are HIGH simultaneously (e.g., D₁=1 and D₂=1), the output becomes ambiguous.

**Example:**
- If D₁=1 and D₂=1: A₁ = 1, A₀ = 1 (indicates D₃, which is actually 0)
- This is incorrect!

### 3.5 Priority Encoder

A **priority encoder** solves this problem by assigning priority levels to inputs. If multiple inputs are HIGH, the output corresponds to the input with the **highest priority**.

#### 3.5.1 8-to-3 Priority Encoder Truth Table

| D₇ | D₆ | D₅ | D₄ | D₃ | D₂ | D₁ | D₀ | A₂ | A₁ | A₀ | V (Valid) |
|----|----|----|----|----|----|----|----|----|----|----|-----------|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1         |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | X  | 0  | 0  | 1  | 1         |
| 0  | 0  | 0  | 0  | 0  | 1  | X  | X  | 0  | 1  | 0  | 1         |
| 0  | 0  | 0  | 0  | 1  | X  | X  | X  | 0  | 1  | 1  | 1         |
| 0  | 0  | 0  | 1  | X  | X  | X  | X  | 1  | 0  | 0  | 1         |
| 0  | 0  | 1  | X  | X  | X  | X  | X  | 1  | 0  | 1  | 1         |
| 0  | 1  | X  | X  | X  | X  | X  | X  | 1  | 1  | 0  |1          |
| 1  | X  | X  | X  | X  | X  | X  | X  | 1  | 1  | 1  |1          |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | X  | X  | X  |0          |

**Note:** X = Don't Care. Priority: D₇ > D₆ > D₅ > D₄ > D₃ > D₂ > D₁ > D₀

#### 3.5.2 Boolean Expressions for Priority Encoder

**For A₂ (MSB):**
```
A₂ = D₄ + D₅ + D₆ + D₇
```

**For A₁:**
```
A₁ = D₂·D₄' + D₃ + D₅ + D₆ + D₇
    = D₂·D₄' + D₃ + D₅ + D₆ + D₇
```

**For A₀:**
```
A₀ = D₁·D₂'·D₄' + D₃ + D₅ + D₆ + D₇
```

**Valid Output (V):**
```
V = D₀ + D₁ + D₂ + D₃ + D₄ + D₅ + D₆ + D₇
```

### 3.6 Example: Implementing a 4-to-2 Priority Encoder

**Problem:** Design a 4-to-2 priority encoder with priority to input D₃ (highest) and D₀ (lowest).

**Solution:**

**Truth Table:**

| D₃ | D₂ | D₁ | D₀ | A₁ | A₀ | V |
|----|----|----|----|----|----|---|
| 1  | X  | X  | X  | 1  | 1  | 1 |
| 0  | 1  | X  | X  | 1  | 0  | 1 |
| 0  | 0  | 1  | X  | 0  | 1  | 1 |
| 0  | 0  | 0  | 1  | 0  | 0  | 1 |
| 0  | 0  | 0  | 0  | X  | X  | 0 |

**Boolean Expressions:**
```
A₁ = D₃ + D₂
A₀ = D₃ + D₁
V = D₀ + D₁ + D₂ + D₃
```

---

## 4. Multiplexers

### 4.1 Definition

A **Multiplexer (MUX)** is a combinational circuit that selects one of many input lines and forwards it to a single output line. The selection of a particular input is controlled by a set of **select lines** (also called control lines or address lines).

For n select lines, the multiplexer can select from 2ⁿ input lines.

### 4.2 Types of Multiplexers

1. **2-to-1 MUX**
2. **4-to-1 MUX**
3. **8-to-1 MUX**
4. **16-to-1 MUX**

### 4.3 2-to-1 Multiplexer

#### 4.3.1 Truth Table

| S | I₁ | I₀ | Y |
|---|----|----|---|
| 0 | X  | 0  | 0 |
| 0 | X  | 1  | 1 |
| 1 | 0  | X  | 0 |
| 1 | 1  | X  | 1 |

**Where:** S = Select line, I₁, I₀ = Input lines, Y = Output

#### 4.3.2 Boolean Expression

```
Y = S·I₁ + S'·I₀
```

#### 4.3.3 Logic Circuit

```
        ┌─ NOT ─┐
   S────┤       ├─── S'
        └───────┘
        
   I₀───┌───────┐
        │       │
   S'───┤  AND  ├───┐
        │       │   │
        └───────┘   │   ┌───────┐
                    ├───┤       │
   I₁───┌───────┐   │   │  OR   ├─── Y
        │       │   │   │       │
   S────┤  AND  ├───┘   └───────┘
        │       │
        └───────┘
```

### 4.4 4-to-1 Multiplexer

#### 4.4.1 Truth Table

| S₁ | S₀ | Y   |
|----|----|-----|
| 0  | 0  | I₀  |
| 0  | 1  | I₁  |
| 1  | 0  | I₂  |
| 1  | 1  | I₃  |

#### 4.4.2 Boolean Expression

```
Y = S₁'·S₀'·I₀ + S₁'·S₀·I₁ + S₁·S₀'·I₂ + S₁·S₀·I₃
```

#### 4.4.3 Implementation using Gates

```
I₀ ──┬─── AND ──┐
     │    │     │
S₀' ─┤    │     │
     │    │     │     ┌─── OR ─── Y
S₁' ─┤────┤─────┤
     │    │     │     │
I₁ ──┼─── AND ──┤
     │    │     │
S₀ ───┤    │     │
     │    │     │
S₁' ──┴────┴─────┘
```

### 4.5 8-to-1 Multiplexer

#### 4.5.1 Truth Table

| S₂ | S₁ | S₀ | Output Y |
|----|----|----|----------|
| 0  | 0  | 0  | I₀       |
| 0  | 0  | 1  | I₁       |
| 0  | 1  | 0  | I₂       |
| 0  | 1  | 1  | I₃       |
| 1  | 0  | 0  | I₄       |
| 1  | 0  | 1  | I₅       |
| 1  | 1  | 0  | I₆       |
| 1  | 1  | 1  | I₇       |

#### 4.5.2 Boolean Expression

```
Y = S₂'·S₁'·S₀'·I₀ + S₂'·S₁'·S₀·I₁ + S₂'·S₁·S₀'·I₂ + S₂'·S₁·S₀·I₃ 
  + S₂·S₁'·S₀'·I₄ + S₂·S₁'·S₀·I₅ + S₂·S₁·S₀'·I₆ + S₂·S₁·S₀·I₇
```

### 4.6 Multiplexer Implementation of Boolean Functions

One of the most important applications of MUX is implementing Boolean functions directly, which is more efficient than using gate-level implementation.

**General Rule:** An n-variable Boolean function can be implemented using a 2ⁿ-to-1 MUX.

**Example: Implement F(A,B,C) = Σ(1,3,5,6) using a 8-to-1 MUX**

**Solution:**

The function has 3 variables (A, B, C), so we use an 8-to-1 MUX with:
- A, B, C as select lines (A=S₂, B=S₁, C=S₀)
- I₀ = F(0,0,0) = 0
- I₁ = F(0,0,1) = 1 → Connect to 1
- I₂ = F(0,1,0) = 0
- I₃ = F(0,1,1) = 1 → Connect to 1
- I₄ = F(1,0,0) = 0
- I₅ = F(1,0,1) = 1 → Connect to 1
- I₆ = F(1,1,0) = 1 → Connect to 1
- I₇ = F(1,1,1) = 0

### 4.7 Multiplexer Applications

1. **Data Selection**: Routing one of several data sources to a single destination
2. **Parallel-to-Serial Conversion**: Converting parallel data to serial by selecting each bit sequentially
3. **Function Implementation**: Implementing Boolean functions (as shown above)
4. **Time Division Multiplexing (TDM)**: Combining multiple signals into one channel
5. **Memory Selection**: Selecting different memory chips in microprocessor systems

### 4.8 Implementing Larger Multiplexers from Smaller Ones

**Example: Implement a 16-to-1 MUX using four 4-to-1 MUXes**

```
              ┌───────────────┐
   I₀ - I₃ ───┤               │
              │   4-to-1 MUX 1├──
   S₁, S₀ ────┤   (Enable=1)  │
              └───────────────┘
                     │
                     ▼
              ┌───────────────┐
   I₄ - I₇ ───┤               │
              │   4-to-1 MUX 2├──── Y
   S₁, S₀ ────┤   (Enable=1)  │
              └───────────────┘
                     ▲
                     │
        ┌────────────┴────────────┐
        │    2-to-4 Decoder       │
        │   (outputs enable)      │
        └────────────┬────────────┘
                     │
               S₃ S₂ (Select)
```

---

## 5. Demultiplexers (Brief Overview)

A **Demultiplexer (DEMUX)** performs the inverse operation of a MUX. It takes a single input and routes it to one of 2ⁿ possible output lines, based on the select line configuration.

### 5.1 1-to-4 Demultiplexer Truth Table

| S₁ | S₀ | D  | O₃ | O₂ | O₁ | O₀ |
|----|----|----|----|----|----|----|
| 0  | 0  | X  | 0  | 0  | 0  | D  |
| 0  | 1  | X  | 0  | 0  | D  | 0  |
| 1  | 0  | X  | 0  | D  | 0  | 0  |
| 1  | 1  | X  | D  | 0  | 0  | 0  |

### 5.2 Boolean Expressions

```
O₀ = S₁'·S₀'·D
O₁ = S₁'·S₀·D
O₂ = S₁·S₀'·D
O₃ = S₁·S₀·D
```

### 5.3 Relationship with Decoders

A demultiplexer can be implemented using a decoder with an enable input. The decoder outputs become the demultiplexer outputs, and the data input is connected to the enable input.

---

## 6. Practical Examples and Applications

### 6.1 Example 1: Seven-Segment Display Decoder

**Problem:** Design a BCD to seven-segment decoder for common cathode display.

**Solution:**

A BCD (4-bit) input represents digits 0-9. The seven outputs (a, b, c, d, e, f, g) control the segments.

**Truth Table (Simplified):**

| Digit | D | C | B | A | a | b | c | d | e | f | g |
|-------|---|---|---|---|---|---|---|---|---|---|---|
| 0     | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1     | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2     | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 3     | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| ...   |   |   |   |   |   |   |   |   |   |   |   |

**Application:** This decoder is used in digital clocks, calculators, and any device displaying numerical information.

### 6.2 Example 2: CPU Address Decoding

**Problem:** A CPU has 16 address lines (A₀-A₁₅) and needs to interface with 4 memory chips of 4KB each.

**Solution:**

Each 4KB memory requires 12 address lines for internal addressing (2¹² = 4096 = 4KB).
The remaining 4 address lines (A₁₂-A₁₅) are used to select which memory chip is active.

```
         ┌─────────────────────────────────┐
A₁₅ A₁₄ ─┤                                 │
         │      2-to-4 Decoder             ├── Chip 0 (A₁₂A₁₃=00)
A₁₃ A₁₂ ─┤      (Enable = 1)               ├── Chip 1 (A₁₂A₁₃=01)
         │                                 ├── Chip 2 (A₁₂A₁₃=10)
         └─────────────────────────────────┘
                                    └── Chip 3 (A₁₂A₁₃=11)
```

### 6.3 Example 3: Multiplexer-based Logic Circuit

**Problem:** Implement the function F(A,B,C) = A'B + AB'C + AC using a 4-to-1 MUX.

**Solution:**

**Step 1:** Express in terms of two variables

Let A be the select input. Then:

```
F = A'(B) + A(B'C + C)
  = A'(B) + A(C + B')
  = A'(B) + A(1)    [Since B' + C = 1]
  = A'(B) + A
  = A + B
```

Actually, let's use a different approach - treat B as the MSB of select:

```
F = A'B + AB'C + AC
  = A'B + A(C + B'C)
  
When B = 0: F = A'(0) + A(C) = AC
When B = 1: F = A'(1) + A(1 + C') = A' + A = 1

Using 4-to-1 MUX with B, C as select lines (B=S₁, C=S₀):

I₀ = F(A,0,0) = A'(0) + A(0) + A(0) = 0
I₁ = F(A,0,1) = A'(0) + A(1) + A(1) = 1
I₂ = F(A,1,0) = A'(1) + A(0) + A(0) = A'
I₃ = F(A,1,1) = A'(1) + A(1) + A(1) = 1

Connect I₁=I₃=1, I₂=A', I₀=0
```

---

## 7. Assessment Questions

### Section A: Easy (Knowledge & Understanding)

**A1.** What is the difference between a decoder and an encoder?

**A2.** How many select lines are required for a 16-to-1 multiplexer?

**A3.** Define the enable input in a decoder circuit.

**A4.** What is the output of a 3-to-8 decoder when all inputs are 0?

**A5.** State one application of each: Decoder, Encoder, Multiplexer.

### Section B: Medium (Application & Analysis)

**B1.** Design a 2-to-4 decoder with active-low outputs using NAND gates only.

**B2.** Implement a 4-to-2 priority encoder that gives priority to D₃ over D₂ over D₁ over D₀. Derive the truth table and boolean expressions.

**B3.** Using a 4-to-1 MUX, implement the function F(A,B,C) = Σm(1,3,4,6,7).

**B4.** Explain how a decoder can be used as a demultiplexer. Show the connection diagram.

**B5.** Design a circuit that converts a 4-bit binary number to its BCD equivalent using appropriate decoders and logic gates.

### Section C: Hard (Design & Synthesis)

**C1.** Design a BCD to 7-segment decoder using a ROM approach. How would you program the ROM contents?

**C2.** Implement a 1-to-16 demultiplexer using four 1-to-4 demultiplexers and a 2-to-4 decoder. Draw the complete circuit diagram.

**C3.** Design a circuit that accepts a 3-bit number and generates an output "1" if the number is prime. Use only a 8-to-1 MUX and minimal additional logic.

**C4.** Compare the implementation of a full adder using:
   - Basic gates
   - A decoder and OR gates
   - Multiplexers
   
   Which method is most efficient in terms of gate count?

**C5.** A system requires selecting one of 32 input data lines to one output line. Design this using:
   - 8-to-1 multiplexers only
   - 4-to-1 multiplexers only
   Compare the hardware requirements.

**C6.** Design a 8-to-3 priority encoder with proper valid output indicator. Show the complete boolean expression derivation for all three outputs.

### Section D: Code-Based Questions (Application)

**D1.** Write a Verilog module for a 4-to-1 multiplexer using case statement.

**D2.** Write Verilog code for a 3-to-8 decoder with enable input.

**D3.** Implement a 4-to-2 priority encoder in Verilog with priority to MSB input.

---

## 8. Key Takeaways

### 8.1 Decoders
- A decoder has **n inputs** and **2ⁿ outputs**
- Only **one output is HIGH** at a time (for enabled condition)
- Can be used to **implement Boolean functions** (as sum of minterms)
- Essential in **memory address decoding** and **display driving**
- Enable input allows **cascading** to create larger decoders

### 8.2 Encoders
- Performs **inverse of decoding** (2ⁿ inputs → n outputs)
- **Priority encoder** solves the multiple input problem
- Priority encoder includes a **valid output (V)** to indicate if any input is active
- Used in **interrupt handling** and **keyboard encoding**

### 8.3 Multiplexers
- A MUX has **2ⁿ data inputs**, **n select lines**, and **1 output**
- Select lines determine which **data input** is connected to output
- Can implement **any Boolean function** directly
- Essential in **data routing**, **parallel-to-serial conversion**
- Larger MUXes can be built from **cascading smaller MUXes**

### 8.4 Key Relationships
- **Decoder** = 1-of-N selector (selects one output line)
- **Encoder** = Converts one-of-N input to binary code
- **Multiplexer** = Data selector (routes one input to output)
- **Demultiplexer** = Data distributor (routes input to one output)

### 8.5 Design Guidelines
1. Always derive **truth table** first
2. Write **boolean expressions** from truth table
3. Simplify using **K-maps** or algebraic methods
4. Implement using appropriate **gates**
5. Consider **enable inputs** for cascading
6. Verify design against **all input combinations**

---

## References

1. Morris Mano, M. (2017). *Digital Design* (5th ed.). Pearson Education.
2. Tocci, R. J., & Widmer, N. S. (2018). *Digital Systems* (12th ed.). Pearson Education.
3. Delhi University NEP 2024 UGCF Syllabus - Computer System Architecture.

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*