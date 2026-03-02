# Adders, Decoders, Encoders, and Multiplexers

## A Comprehensive Study Material for GE2C — Computer System Architecture

**Delhi University | BSc Physical Science (CS) | NEP 2024**

---

## 1. Introduction

Digital electronics forms the backbone of all modern computing systems. At the heart of every processor, every microcontroller, and every digital device lies a set of fundamental building blocks that perform arithmetic and data-routing operations. Among these, **adders**, **decoders**, **encoders**, and **multiplexers** are essential combinational circuits that you will encounter repeatedly in computer architecture, digital design, and embedded systems.

This study material aligns with the **GE2C — Computer System Architecture** syllabus under Delhi University's NEP 2024 framework for BSc Physical Science (CS). It provides detailed conceptual coverage, practical examples, self-assessment tools, and revision flashcards to ensure complete understanding of these critical topics.

---

## 2. Adders

### 2.1 What is an Adder?

An **adder** is a combinational circuit that performs binary addition. It is the fundamental arithmetic unit in the Arithmetic Logic Unit (ALU) of a CPU. Adders process two binary numbers and produce a **sum** and a **carry** as output.

### 2.2 Half Adder

A **Half Adder** adds two single-bit binary numbers. It has two inputs (A and B) and two outputs: **Sum (S)** and **Carry (C)**.

**Truth Table:**

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 |    0    |     0     |
| 0 | 1 |    1    |     0     |
| 1 | 0 |    1    |     0     |
| 1 | 1 |    0    |     1     |

**Boolean Expressions:**

- Sum: $S = A \oplus B$ (XOR gate)
- Carry: $C = A \cdot B$ (AND gate)

**Limitation:** A half adder cannot add a carry-in from a previous stage, which is necessary for multi-bit addition.

### 2.3 Full Adder

A **Full Adder** adds three bits: two significant bits (A and B) and an incoming carry ($C_{in}$). It produces a **Sum (S)** and a **Carry-out ($C_{out}$)**.

**Truth Table:**

| A | B | C_in | Sum (S) | Carry (C_out) |
|---|---|------|---------|---------------|
| 0 | 0 |  0   |    0    |       0       |
| 0 | 0 |  1   |    1    |       0       |
| 0 | 1 |  0   |    1    |       0       |
| 0 | 1 |  1   |    0    |       1       |
| 1 | 0 |  0   |    1    |       0       |
| 1 | 0 |  1   |    0    |       1       |
| 1 | 1 |  0   |    0    |       1       |
| 1 | 1 |  1   |    1    |       1       |

**Boolean Expressions:**

- Sum: $S = A \oplus B \oplus C_{in}$
- Carry-out: $C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B))$

### 2.4 Ripple Carry Adder (RCA)

When multiple full adders are cascaded in series, the output carry of one stage becomes the carry-in for the next stage. This cascading forms an **n-bit parallel adder**, commonly called a **Ripple Carry Adder**.

For an **n-bit RCA**, n full adders are connected such that:

- The sum outputs ($S_0, S_1, \dots, S_{n-1}$) are available in parallel.
- The carry propagates sequentially from the least significant bit (LSB) to the most significant bit (MSB).

**4-bit Ripple Carry Adder Structure:**

```
       A3 A2 A1 A0
  +    B3 B2 B1 B0
  -----------------
       S3 S2 S1 S0  → Sum
  C4 ← C3 C2 C1 C0  → Carry Out
```

**Working:** The LSB full adder (FA0) receives $A_0$, $B_0$, and $C_{in}=0$. Its $C_{out}$ becomes the $C_{in}$ for FA1, and so on. This ripple effect gives the circuit its name.

**Disadvantage:** The propagation delay increases linearly with the number of bits because each full adder must wait for the carry from the previous stage. For large adders, this causes significant delay.

### 2.5 Carry Look-Ahead Adder (CLA)

The **Carry Look-Ahead Adder** solves the propagation delay problem of the RCA by calculating carry bits in **parallel** using **generate** and **propagate** signals.

**Definitions:**

- **Generate ($G_i$):** A carry is generated at bit position i regardless of input carry.
  - $G_i = A_i \cdot B_i$
- **Propagate ($P_i$):** A carry-in at position i will be propagated to position i+1.
  - $P_i = A_i \oplus B_i$

**Carry Equations:**

- $C_1 = G_0 + (P_0 \cdot C_0)$
- $C_2 = G_1 + (P_1 \cdot G_0) + (P_1 \cdot P_0 \cdot C_0)$
- $C_3 = G_2 + (P_2 \cdot G_1) + (P_2 \cdot P_1 \cdot G_0) + (P_2 \cdot P_1 \cdot P_0 \cdot C_0)$

**Advantage:** All carries are computed simultaneously in constant time (O(1)), regardless of the number of bits, making CLAs significantly faster than RCAs for wide data paths.

### 2.6 Real-World Relevance of Adders

Adders are not limited to CPUs. They appear in:

- **Graphics Processing Units (GPUs)** for parallel vector addition.
- **Digital Signal Processors (DSPs)** for filter implementations.
- **Address generation** in memory controllers.
- **Microcontrollers** for arithmetic operations in ALUs.

---

## 3. Decoders

### 3.1 What is a Decoder?

A **decoder** is a combinational circuit that converts **n input lines** into **$2^n$ output lines**. It is the inverse of an encoder. At any given time, **only one output line is HIGH** (or active), based on the binary value of the input.

A decoder with **n inputs** and **$2^n$ outputs** is called an **n-to-$2^n$ decoder**.

### 3.2 2-to-4 Decoder

A 2-to-4 decoder has 2 input lines (A₁, A₀) and 4 output lines (D₃, D₂, D₁, D₀).

**Truth Table:**

| A₁ | A₀ | D₀ | D₁ | D₂ | D₃ |
|----|----|----|----|----|----|
|  0 |  0 |  1 |  0 |  0 |  0 |
|  0 |  1 |  0 |  1 |  0 |  0 |
|  1 |  0 |  0 |  0 |  1 |  0 |
|  1 |  1 |  0 |  0 |  0 |  1 |

**Boolean Expressions:**

- $D_0 = \overline{A_1} \cdot \overline{A_0}$
- $D_1 = \overline{A_1} \cdot A_0$
- $D_2 = A_1 \cdot \overline{A_0}$
- $D_3 = A_1 \cdot A_0$

Each output corresponds to one unique minterm of the input combinations.

### 3.3 3-to-8 Decoder

A 3-to-8 decoder has 3 inputs and 8 outputs. It is commonly used in memory address decoding.

**Truth Table (Partial):**

| A₂ | A₁ | A₀ | Active Output |
|----|----|----|---------------|
|  0 |  0 |  0 | D₀ = 1       |
|  0 |  0 |  1 | D₁ = 1       |
|  0 |  1 |  0 | D₂ = 1       |
|  0 |  1 |  1 | D₃ = 1       |
|  1 |  0 |  0 | D₄ = 1       |
|  1 |  0 |  1 | D₅ = 1       |
|  1 |  1 |  0 | D₆ = 1       |
|  1 |  1 |  1 | D₇ = 1       |

### 3.4 Decoder with Enable Input

Most practical decoders include an **Enable (E)** input. When E = 0, all outputs are disabled (0 or high-impedance). When E = 1, the decoder operates normally.

**2-to-4 Decoder with Enable:**

- If E = 0: All outputs = 0
- If E = 1: Outputs correspond to input combination

### 3.5 Applications of Decoders

| Application | Description |
|-------------|-------------|
| **Memory Address Decoding** | Used to select a specific memory chip or memory location from an address bus. |
| **Instruction Decoding** | In a CPU, decoders interpret opcode bits to determine which operation to execute. |
| **Demultiplexing** | A decoder can function as a demultiplexer by using the enable input as the data input. |
| **Seven-Segment Display** | BCD-to-7-segment decoders drive numeric displays. |
| **Network Routing** | Route data packets to specific output lines based on address bits. |

### 3.6 Expanding Decoders

Two 2-to-4 decoders can be combined to form a **3-to-8 decoder**:

- Use the third input (A₂) to enable one of the two 2-to-4 decoders.
- When A₂ = 0, lower decoder is enabled.
- When A₂ = 1, upper decoder is enabled.

---

## 4. Encoders

### 4.1 What is an Encoder?

An **encoder** is a combinational circuit that performs the **inverse operation of a decoder**. It converts **$2^n$ input lines** into **n output lines**. The output is a binary code corresponding to the active input line.

### 4.2 Binary Encoder (4-to-2)

A 4-to-2 binary encoder has 4 input lines (D₃, D₂, D₁, D₀) and 2 output lines (A₁, A₀). Only **one input should be HIGH at a time** for correct operation.

**Truth Table:**

| D₃ | D₂ | D₁ | D₀ | A₁ | A₀ |
|----|----|----|----|----|----|
|  0 |  0 |  0 |  1 |  0 |  0 |
|  0 |  0 |  1 |  0 |  0 |  1 |
|  0 |  1 |  0 |  0 |  1 |  0 |
|  1 |  0 |  0 |  0 |  1 |  1 |

**Boolean Expressions:**

- $A_1 = D_2 + D_3$
- $A_0 = D_1 + D_3$

**Limitation:** If multiple inputs are HIGH simultaneously, the encoder produces incorrect output. This issue is resolved by a **priority encoder**.

### 4.3 Priority Encoder

A **priority encoder** assigns a priority level to each input. When multiple inputs are HIGH, the output corresponds to the **highest-priority input**. This is critical in interrupt handling and error detection.

**4-to-2 Priority Encoder Truth Table:**

| D₃ | D₂ | D₁ | D₀ | A₁ | A₀ | V (Valid) |
|----|----|----|----|----|----|-----------|
|  0 |  0 |  0 |  0 |  X |  X |    0      |
|  0 |  0 |  0 |  1 |  0 |  0 |    1      |
|  0 |  0 |  1 |  X |  0 |  1 |    1      |
|  0 |  1 |  X |  X |  1 |  0 |    1      |
|  1 |  X |  X |  X |  1 |  1 |    1      |

The **V** output indicates whether the output is valid (V=1 means at least one input is active).

**Equations for Priority Encoder:**

- $A_1 = D_3 + D_2$
- $A_0 = D_3 + (\overline{D_2} \cdot D_1)$
- $V = D_3 + D_2 + D_1 + D_0$

### 4.4 Applications of Encoders

| Application | Description |
|-------------|-------------|
| **Keyboard Encoding** | Converts key presses into binary codes for processing by the CPU. |
| **Interrupt Request (IRQ) Handling** | Priority encoders resolve multiple simultaneous interrupt requests in microprocessors. |
| **Position Sensing** | Rotary encoders convert shaft position into digital signals. |
| **Memory Chip Selection** | Encoders generate chip-select signals in memory systems. |

---

## 5. Multiplexers (Mux)

### 5.1 What is a Multiplexer?

A **multiplexer (Mux)** is a combinational circuit that selects **one data input** from multiple input lines and routes it to a **single output line**. The selection is controlled by **select lines**.

Think of a multiplexer as a **digital switch** — it connects one of many data sources to a single destination based on a binary address.

### 5.2 2-to-1 Multiplexer

A 2-to-1 Mux has:

- 2 data inputs: $I_0$, $I_1$
- 1 select line: $S$
- 1 output: $Y$

**Truth Table:**

| S | Y |
|---|------|
| 0 | $I_0$ |
| 1 | $I_1$ |

**Boolean Expression:**

$Y = \overline{S} \cdot I_0 + S \cdot I_1$

### 5.3 4-to-1 Multiplexer

A 4-to-1 Mux has 4 data inputs ($I_0, I_1, I_2, I_3$), 2 select lines ($S_1, S_0$), and 1 output ($Y$).

| S₁ | S₀ | Output (Y) |
|----|----|------------|
|  0 |  0 |    $I_0$   |
|  0 |  1 |    $I_1$   |
|  1 |  0 |    $I_2$   |
|  1 |  1 |    $I_3$   |

**Boolean Expression:**
$Y = \overline{S_1} \cdot \overline{S_0} \cdot I_0 + \overline{S_1} \cdot S_0 \cdot I_1 + S_1 \cdot \overline{S_0} \cdot I_2 + S_1 \cdot S_0 \cdot I_3$

### 5.4 8-to-1 Multiplexer

An 8-to-1 Mux requires 3 select lines ($S_2, S_1, S_0$) to select one of 8 inputs. It is commonly used in data routing and function implementation.

### 5.5 Multiplexer Implementation of Boolean Functions

One of the most important applications of multiplexers is implementing **logic functions** directly from a truth table without designing a custom circuit.

**Example:** Implement the following Boolean function using a 4-to-1 Mux:
$f(A, B, C) = \sum m(1, 3, 5, 6)$

**Solution:**

| A | B | C | f |
|---|---|---|---|
| 0 | 0 | 0 | 0 | → Connect 0 to I₀
| 0 | 0 | 1 | 1 | → Connect 1 to I₁
| 0 | 1 | 0 | 0 | → Connect 0 to I₂
| 0 | 1 | 1 | 1 | → Connect 1 to I₃
| 1 | 0 | 0 | 0 | → Connect 0 to I₄
| 1 | 0 | 1 | 1 | → Connect 1 to I₅
| 1 | 1 | 0 | 1 | → Connect 1 to I₆
| 1 | 1 | 1 | 0 | → Connect 0 to I₇

Use A and B as select lines ($S_1 = A$, $S_0 = B$). Connect the values of $f$ for each combination of C to inputs $I_0$ through $I_3$.

### 5.6 Applications of Multiplexers

| Application | Description |
|-------------|-------------|
| **Data Routing** | Selects one of multiple data sources to send to a single destination (e.g., sharing a communication line). |
| **Parallel-to-Serial Conversion** | Converts parallel data streams into serial by selecting bits sequentially. |
| **Function Generation** | Implements Boolean logic functions using Mux as a universal logic module. |
| **Memory Read/Write Operations** | Selects one memory location from multiple banks. |
| **Video/Audio Switching** | Switches between multiple video or audio sources in multimedia systems. |

### 5.7 Demultiplexer (Demux)

A **demultiplexer** performs the inverse operation of a multiplexer. It takes a single input and routes it to one of $2^n$ output lines based on **n select lines**.

- **1-to-2 Demux:** 1 input, 1 select line, 2 outputs.
- **1-to-4 Demux:** 1 input, 2 select lines, 4 outputs.

Demultiplexers are widely used in **data distribution** and **communication systems**.

---

## 6. Practical Examples with Code

### Example 1: Verilog Code for a Full Adder

```verilog
// Behavioral modeling of a Full Adder
module FullAdder (
    input A,
    input B,
    input Cin,
    output Sum,
    output Cout
);

assign Sum = A ^ B ^ Cin;
assign Cout = (A & B) | (Cin & (A ^ B));

endmodule
```

**Explanation:** The XOR operation computes the sum of three bits, and the carry-out is computed using the standard full adder expression.

### Example 2: Implementing a 4-to-1 Mux in Verilog

```verilog
// 4-to-1 Multiplexer using case statement
module Mux4to1 (
    input [3:0] I,      // 4 data inputs
    input [1:0] S,      // 2 select lines
    output reg Y       // output
);

always @(*)
begin
    case (S)
        2'b00: Y = I[0];
        2'b01: Y = I[1];
        2'b10: Y = I[2];
        2'b11: Y = I[3];
        default: Y = 1'b0;
    endcase
end

endmodule
```

### Example 3: 3-to-8 Decoder using Two 2-to-4 Decoders

```verilog
// 3-to-8 Decoder using enable and two 2-to-4 decoders
module Decoder3to8 (
    input [2:0] A,
    input En,
    output [7:0] Y
);

wire en_low, en_high;

assign en_low = ~A[2];      // Enable for lower decoder when A2=0
assign en_high = A[2];     // Enable for upper decoder when A2=1

// Lower decoder (outputs D0-D3)
assign Y[0] = en_low & ~A[1] & ~A[0];
assign Y[1] = en_low & ~A[1] &  A[0];
assign Y[2] = en_low &  A[1] & ~A[0];
assign Y[3] = en_low &  A[1] &  A[0];

// Upper decoder (outputs D4-D7)
assign Y[4] = en_high & ~A[1] & ~A[0];
assign Y[5] = en_high & ~A[1] &  A[0];
assign Y[6] = en_high &  A[1] & ~A[0];
assign Y[7] = en_high &  A[1] &  A[0];

endmodule
```

---

## 7. Multiple Choice Questions

### Easy Questions

1. **How many output lines does a 3-to-8 decoder have?**
   - (a) 3
   - (b) 8
   - (c) 11
   - (d) 5

2. **Which gate is used to implement the Sum output in a half adder?**
   - (a) AND
   - (b) OR
   - (c) XOR
   - (d) NAND

3. **In a 4-to-1 multiplexer, how many select lines are required?**
   - (a) 1
   - (b) 2
   - (c) 4
   - (d) 3

4. **A priority encoder resolves the issue of:**
   - (a) Multiple HIGH inputs
   - (b) Propagation delay
   - (c) Power consumption
   - (d) Signal attenuation

5. **The carry-out of a full adder is given by:**
   - (a) $A \oplus B \oplus C_{in}$
   - (b) $A + B + C_{in}$
   - (c) $(A \cdot B) + (C_{in} \cdot (A \oplus B))$
   - (d) $A \cdot B \cdot C_{in}$

### Medium Questions

6. **In a 4-bit Ripple Carry Adder, if each full adder has a propagation delay of 10 ns, what is the total delay for the most significant bit?**
   - (a) 10 ns
   - (b) 20 ns
   - (c) 40 ns
   - (d) 80 ns

7. **Which of the following is NOT an application of a decoder?**
   - (a) Memory address decoding
   - (b) Instruction decoding in CPU
   - (c) Parallel-to-serial conversion
   - (d) Demultiplexing

8. **A multiplexer can be used to implement which of the following?**
   - (a) Only combinational circuits
   - (b) Only sequential circuits
   - (c) Both combinational and sequential circuits
   - (d) Neither

9. **What is the primary advantage of a Carry Look-Ahead Adder over a Ripple Carry Adder?**
   - (a) Lower power consumption
   - (b) Constant propagation delay regardless of bit width
   - (c) Simpler circuit design
   - (d) Uses fewer gates

10. **In a 4-to-2 encoder, if inputs D1 and D3 are both HIGH simultaneously, the output will be:**
    - (a) 00
    - (b) 01
    - (c) 10
    - (d) 11

### Hard Questions

11. **How many 2-to-1 multiplexers are required to implement a 16-to-1 multiplexer?**
    - (a) 8
    - (b) 15
    - (c) 16
    - (d) 32

12. **A 3-bit carry look-ahead adder generates carry at the third stage using:**
    - (a) Only Generate signals
    - (b) Only Propagate signals
    - (c) Both Generate and Propagate signals
    - (d) None of the above

13. **If the truth table of a Boolean function has three minterms (m1, m3, m5), the function can be implemented using a multiplexer with select lines equal to:**
    - (a) 1
    - (b) 2
    - (c) 3
    - (d) 4

14. **In a 1-to-4 demultiplexer, the output lines are activated based on:**
    - (a) Data input
    - (b) Select lines
    - (c) Clock signal
    - (d) Enable signal

15. **For a 4-input priority encoder with inputs D3 (highest priority), D2, D1, D0 (lowest priority), if D3 = 1 and D1 = 1, the output will be:**
    - (a) 00
    - (b) 01
    - (c) 10
    - (d) 11

**Answer Key:**
1. (b), 2. (c), 3. (b), 4. (a), 5. (c), 6. (c), 7. (c), 8. (c), 9. (b), 10. (a), 11. (b), 12. (c), 13. (b), 14. (b), 15. (d)

---

## 8. Flashcards for Quick Revision

| # | Concept | Answer |
|---|---------|--------|
| 1 | What is a half adder? | A combinational circuit that adds two 1-bit numbers, producing Sum and Carry. Sum = A ⊕ B, Carry = A · B |
| 2 | How does a full adder differ from a half adder? | Full adder accepts three inputs (A, B, Cin), while half adder accepts only two. |
| 3 | Why is a Ripple Carry Adder slow? | Carry propagates sequentially through each full adder stage, causing linear delay with bit width. |
| 4 | What are Generate (G) and Propagate (P) signals in a CLA? | G = A · B (carry generated), P = A ⊕ B (carry propagated to next stage). |
| 5 | What does a decoder do? | Converts n input lines into 2ⁿ unique output lines; only one output is active at a time. |
| 6 | What is the difference between a binary encoder and a priority encoder? | Binary encoder requires only one HIGH input; priority encoder handles multiple HIGH inputs by prioritizing the highest-order input. |
| 7 | What is a multiplexer? | A combinational circuit that selects one of multiple data inputs and routes it to a single output based on select lines. |
| 8 | How many select lines are needed for an 8-to-1 Mux? | 3 select lines (2³ = 8). |
| 9 | Can a Mux implement any Boolean function? | Yes, by using select lines as input variables and connecting 0/1 or function of remaining variables to data inputs. |
| 10 | What is the inverse operation of multiplexing? | Demultiplexing — routing a single input to one of multiple outputs based on select lines. |
| 11 | What is the output of a 2-to-4 decoder when inputs are A₁=1, A₀=0 and Enable=1? | D₂ = 1 (active), all other outputs = 0. |
| 12 | What does the Valid (V) output indicate in a priority encoder? | V = 1 indicates at least one input is active; V = 0 indicates no input is active. |
| 13 | Which adder is preferred in modern CPUs and why? | Carry Look-Ahead Adder — because it computes all carries in parallel, providing constant delay independent of bit width. |
| 14 | What is the Boolean expression for the output of a 2-to-1 Mux? | Y = S̄ · I₀ + S · I₁ |
| 15 | How can two 2-to-4 decoders create a 3-to-8 decoder? | Use the third input bit to enable one decoder at a time — when third bit is 0, lower decoder is enabled; when 1, upper decoder is enabled. |

---

## 9. Key Takeaways

1. **Adders** are fundamental to arithmetic operations in CPUs. Half adders handle 1-bit addition, full adders incorporate carry-in, ripple carry adders cascade full adders (simple but slow), and carry look-ahead adders use generate/propagate logic for high-speed parallel computation.

2. **Decoders** convert binary addresses into unique output signals. They are essential in memory addressing, instruction decoding, and can also function as demultiplexers when combined with an enable input.

3. **Encoders** perform the reverse of decoders, compressing multiple input lines into a binary code. Priority encoders are crucial in systems where multiple simultaneous requests must be resolved, such as interrupt handling.

4. **Multiplexers** are universal data-routing devices. They select one input from many based on select lines, making them invaluable for data routing, parallel-to-serial conversion, and implementing Boolean functions directly from truth tables without custom gate design.

5. **Design relationships** between these circuits are important: decoders and encoders are complements of each other; multiplexers and demultiplexers are complements of each other; adders form the arithmetic backbone of all digital processors.

6. **Real-world applications** span microprocessors, memory systems, communication devices, and embedded systems. Understanding these building blocks is critical for advanced courses in computer architecture and digital design.

7. **Delhi University (NEP 2024) Focus:** The GE2C syllabus emphasizes conceptual clarity, practical implementation (Verilog/VHDL), and application-oriented understanding. Mastery of these combinational circuits prepares you for sequential circuit design, microprocessor interfacing, and system-on-chip (SoC) design in higher semesters.

---

*Study Material prepared for BSc Physical Science (CS), GE2C — Computer System Architecture, Delhi University, NEP 2024.*