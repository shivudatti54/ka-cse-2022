# Digital Encoders

## 1. Introduction and Theoretical Foundation

An **encoder** is a fundamental combinational logic circuit that performs the inverse function of a decoder. While a decoder converts an n-bit binary code into one of 2^n possible output lines, an encoder converts multiple input lines (typically 2^n) into a compact n-bit binary code. This data compression capability makes encoders essential in digital systems where efficient line reduction is required.

Mathematically, an encoder implements a many-to-one mapping function f: {0, 1}^{2^n} → {0, 1}^n, where exactly one input line is expected to be active at a time. The formal definition requires that for any valid input vector I = (I₀, I₁, ..., I\_{2^n-1}), there exists exactly one index k such that I_k = 1, and the output Y represents the binary representation of k.

The encoder is formally defined as a mapping function that satisfies the condition: if I_j = 1 for some j ∈ {0, 1, ..., 2^n-1}, then the output Y equals the binary representation of j. This defines a surjective function from the set of input combinations with exactly one '1' to the set of n-bit binary numbers.

## 2. Simple (Non-Priority) Encoder

### 2.1 Definition and Basic Principle

A simple encoder, also known as a basic encoder, operates under the fundamental assumption that **only one input line is active (logic '1') at any given time**. This constraint simplifies the logic design but imposes strict operational limitations.

For an n-output simple encoder, the circuit accepts 2^n input lines and produces an n-bit binary code at the output. The relationship between inputs and outputs follows directly from the binary numbering system.

### 2.2 4-to-2 Line Encoder: Complete Analysis

The 4-to-2 line encoder represents the simplest non-trivial encoder configuration. Let the inputs be denoted as I₀, I₁, I₂, I₃ (where I₀ corresponds to binary 00, I₁ to binary 01, I₂ to binary 10, and I₃ to binary 11), and let the outputs be Y₁ and Y₀ representing the 2-bit binary code.

**Truth Table:**

| I₃  | I₂  | I₁  | I₀  | Y₁  | Y₀  |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 1   | 0   | 0   |
| 0   | 0   | 1   | 0   | 0   | 1   |
| 0   | 1   | 0   | 0   | 1   | 0   |
| 1   | 0   | 0   | 0   | 1   | 1   |

**Derivation of Boolean Expressions Using Boolean Algebra:**

From the truth table, Y₁ = 1 when either I₂ = 1 or I₃ = 1. Therefore:

Y₁ = I₂ + I₃

Similarly, Y₀ = 1 when either I₁ = 1 or I₃ = 1. Therefore:

Y₀ = I₁ + I₃

**Karnaugh Map Minimization:**

```
Y₁ K-map:
 I₁I₀
 00 01 11 10
I₃I₂ 00 0 0 X 0
 01 0 0 X 1 ← I₂=1, I₁=0, I₀=0 → Y₁=1
 11 1 1 X 1 ← I₃=1, I₂=1 → Y₁=1 (don't care I₁,I₀)
 10 1 1 X 1 ← I₃=1, I₂=0 → Y₁=1

Grouping: One group of 4 (I₃=1) → Y₁ = I₃
 One group of 2 (I₂=1, I₁=0, I₀=0) → Y₁ = I₂

Therefore: Y₁ = I₃ + I₂ (verified by Boolean algebra)
```

The minimal implementation requires two 2-input OR gates, achieving a circuit with minimal gate count. However, this simplicity comes at the cost of significant operational limitations.

### 2.3 Critical Limitation: Ambiguity Problem

The fundamental limitation of the simple encoder manifests when multiple inputs are simultaneously active. Consider the input combination I₁ = 1 and I₂ = 1:

- According to the standard Boolean expressions: Y₁ = I₂ + I₃ = 1 + 0 = 1, and Y₀ = I₁ + I₃ = 1 + 0 = 1
- The output Y₁Y₀ = 11 (binary 3) is generated
- However, this output correctly represents neither I₁ (which should produce 01) nor I₂ (which should produce 10)

This ambiguity renders the simple encoder unsuitable for real-world applications where simultaneous multiple inputs are probable. The solution to this problem is the **priority encoder**.

## 3. Priority Encoder: Theory and Design

### 3.1 Concept and Formal Definition

A priority encoder resolves the ambiguity of simple encoders by establishing a strict **priority hierarchy** among input lines. When multiple inputs are active simultaneously, the encoder outputs the binary code corresponding to the **highest-priority active input**.

Formally, let the priority ordering be defined as I*{2^n-1} > I*{2^n-2} > ... > I₁ > I₀, where '>' denotes "has higher priority than." The priority encoder output Y is determined by:

Y = max{k | I_k = 1}

where max{} returns the largest index k such that I_k = 1. If no input is active (all I_k = 0), a separate **valid output indicator** V is set to 0 to signal this condition.

### 3.2 4-to-2 Priority Encoder: Complete Design

**Truth Table with Don't-Care Conditions:**

| I₃  | I₂  | I₁  | I₀  | Y₁  | Y₀  | V   | Interpretation              |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- |
| 0   | 0   | 0   | 0   | X   | X   | 0   | No input                    |
| 0   | 0   | 0   | 1   | 0   | 0   | 1   | I₀ active                   |
| 0   | 0   | 1   | X   | 0   | 1   | 1   | I₁ has priority over I₀     |
| 0   | 1   | X   | X   | 1   | 0   | 1   | I₂ has priority over I₁, I₀ |
| 1   | X   | X   | X   | 1   | 1   | 1   | I₃ has highest priority     |

**Derivation of Y₁:**

From the truth table, Y₁ = 1 when I₂ = 1 (regardless of I₁, I₀) or when I₃ = 1 (regardless of all other inputs).

Using Boolean algebra:

- When I₃ = 1: Y₁ must be 1 (output 11 for input 3)
- When I₃ = 0 and I₂ = 1: Y₁ must be 1 (output 10 for input 2)
- Therefore: Y₁ = I₃ + (I₃' · I₂) = I₃ + I₂

**Derivation of Y₀:**

From the truth table:

- Y₀ = 1 when I₁ = 1 (with I₂ = 0, I₃ = 0), OR
- Y₀ = 1 when I₃ = 1 (regardless of other inputs)

Using Boolean algebra with minterms:

- Y₀ = Σm(3, 5, 7, 9, 11, 13, 15) for a general case
- For 4-to-2: Y₀ = I₁ · I₂' · I₃' + I₃

**Proof of Y₀ Expression:**

- Case 1: I₃ = 1 → Output must be 11 → Y₀ = 1 (regardless of I₂, I₁, I₀)
- Case 2: I₃ = 0, I₂ = 0, I₁ = 1 → Output must be 01 → Y₀ = 1
- Case 3: I₃ = 0, I₂ = 1 → Output must be 10 → Y₀ = 0

Therefore: Y₀ = I₃ + I₁ · I₂' · I₃' = I₃ + I₁ · I₂'

**Valid Output (V):**
V = 1 if and only if at least one input is active:
V = I₀ + I₁ + I₂ + I₃

This can be implemented as a 4-input OR gate or cascaded 2-input OR gates.

### 3.3 Karnaugh Map Derivation for 4-to-2 Priority Encoder

```
Y₁ K-map (with don't cares for lower-priority inputs):
 I₁I₀
 00 01 11 10
I₃I₂ 00 X 0 1 0 ← Row: I₃=0, I₂=0: Y₁=1 only when I₁=1,I₀=0
 01 1 1 1 1 ← Row: I₃=0, I₂=1: Y₁=1 always (I₂ priority)
 11 1 1 1 1 ← Row: I₃=1, I₂=1: Y₁=1 (don't care lower)
 10 1 1 1 1 ← Row: I₃=1, I₂=0: Y₁=1 (I₃ priority)

Minimal expression: Y₁ = I₂ + I₃
```

```
Y₀ K-map:
 I₁I₀
 00 01 11 10
I₃I₂ 00 X 0 0 0
 01 0 0 0 0
 11 1 1 1 1
 10 1 1 1 1

Minimal expression: Y₀ = I₁·I₂' + I₃
```

## 4. 8-to-3 Priority Encoder: Extended Design

### 4.1 Truth Table

For an 8-to-3 priority encoder with I₇ having highest priority:

| I₇  | I₆  | I₅  | I₄  | I₃  | I₂  | I₁  | I₀  | Y₂  | Y₁  | Y₀  | V   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | X   | X   | X   | 0   |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 1   |
| 0   | 0   | 0   | 0   | 0   | 0   | 1   | X   | 0   | 0   | 1   | 1   |
| 0   | 0   | 0   | 0   | 0   | 1   | X   | X   | 0   | 1   | 0   | 1   |
| 0   | 0   | 0   | 0   | 1   | X   | X   | X   | 0   | 1   | 1   | 1   |
| 0   | 0   | 0   | 1   | X   | X   | X   | X   | 1   | 0   | 0   | 1   |
| 0   | 0   | 1   | X   | X   | X   | X   | X   | 1   | 0   | 1   | 1   |
| 0   | 1   | X   | X   | X   | X   | X   | X   | 1   | 1   | 0   | 1   |
| 1   | X   | X   | X   | X   | X   | X   | X   | 1   | 1   | 1   | 1   |

### 4.2 Minimized Boolean Expressions

Through K-map minimization (detailed derivation omitted for brevity), the minimal expressions are:

- Y₂ = I₄ + I₅ + I₆ + I₇
- Y₁ = I₂·I₄' + I₃ + I₅ + I₆ + I₇
- Y₀ = I₁·I₂'·I₄' + I₃·I₄' + I₅ + I₇
- V = I₀ + I₁ + I₂ + I₃ + I₄ + I₅ + I₆ + I₇

## 5. Enable Inputs and Cascading

### 5.1 Encoder with Enable (Enable Input)

Practical encoder circuits include an **enable input (E)** to control operation. When E = 0, all outputs are forced to 0 (or high-impedance). When E = 1, the encoder operates normally.

The modified output expressions become:

- Y = f(I) · E (for each output bit)
- V = (OR of all inputs) · E

### 5.2 Cascading Priority Encoders

To handle more than 2^n inputs, multiple priority encoders can be cascaded. The valid output (V) of a lower-priority encoder is used as an enable input to the next higher-priority encoder stage. This hierarchical arrangement enables construction of encoders with arbitrary numbers of input lines.

For example, two 8-to-3 priority encoders can be cascaded to create a 16-to-4 priority encoder by:

1. Using the first encoder for inputs I₀-I₇ (lower priority group)
2. Using the second encoder for inputs I₈-I₁₅ (higher priority group)
3. Using a higher-order bit that indicates which group is active

## 6. Timing Analysis and Propagation Delay

### 6.1 Critical Path Analysis

In combinational encoders, the propagation delay determines the maximum operating frequency. The critical path in a 4-to-2 priority encoder:

1. **Input to Valid (V)**: V = I₀ + I₁ + I₂ + I₃ through a 4-input OR gate: t_p(V)
2. **Input to Y₁**: Path through OR gate: t_p(OR)
3. **Input to Y₀**: Path through NOT gate + AND gate + OR gate: t_p(NOT) + t_p(AND) + t_p(OR)

The maximum propagation delay determines the clock period constraint in synchronous systems incorporating encoders.

### 6.2 Glitch Considerations

Priority encoders may exhibit static hazards (glitches) when input combinations change between codes that differ in multiple bits. For example, transitioning from I₂ = 1 (output 10) to I₃ = 1 (output 11) may cause a momentary incorrect output due to different propagation delays in the AND/OR paths. These hazards can be eliminated using hazard-free design techniques or by using synchronous circuits with appropriate setup/hold times.

## 7. HDL Implementation

### 7.1 VHDL Model of 4-to-2 Priority Encoder

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity priority_encoder_4to2 is
 Port ( I : in STD_LOGIC_VECTOR (3 downto 0);
 Y : out STD_LOGIC_VECTOR (1 downto 0);
 V : out STD_LOGIC);
end priority_encoder_4to2;

architecture Behavioral of priority_encoder_4to2 is
begin
 process(I)
 begin
 V <= '0';
 Y <= "00";

 if I(3) = '1' then
 Y <= "11";
 V <= '1';
 elsif I(2) = '1' then
 Y <= "10";
 V <= '1';
 elsif I(1) = '1' then
 Y <= "01";
 V <= '1';
 elsif I(0) = '1' then
 Y <= "00";
 V <= '1';
 end if;
 end process;
end Behavioral;
```

### 7.2 Verilog Model of 8-to-3 Priority Encoder

```verilog
module priority_encoder_8to3 (
 input [7:0] I,
 output reg [2:0] Y,
 output reg V
);
 always @(*) begin
 V = 1'b0;
 Y = 3'b000;

 if (I[7]) begin
 Y = 3'b111;
 V = 1'b1;
 end
 else if (I[6]) begin
 Y = 3'b110;
 V = 1'b1;
 end
 else if (I[5]) begin
 Y = 3'b101;
 V = 1'b1;
 end
 else if (I[4]) begin
 Y = 3'b100;
 V = 1'b1;
 end
 else if (I[3]) begin
 Y = 3'b011;
 V = 1'b1;
 end
 else if (I[2]) begin
 Y = 3'b010;
 V = 1'b1;
 end
 else if (I[1]) begin
 Y = 3'b001;
 V = 1'b1;
 end
 else if (I[0]) begin
 Y = 3'b000;
 V = 1'b1;
 end
 end
endmodule
```

## 8. Practical Applications

### 8.1 Keyboard Matrix Encoding

In computer keyboards, a matrix of switches (typically 8×8 or larger) is scanned by the controller. Each key press corresponds to a unique row-column intersection. A priority encoder converts the pressed key into its corresponding scan code. When multiple keys are pressed (key rollover), the priority encoder ensures deterministic output by selecting the highest-priority active key according to the keyboard's priority scheme.

### 8.2 Interrupt Priority Encoding

In microprocessor systems, multiple peripheral devices may request service simultaneously through interrupt request (IRQ) lines. A priority encoder embedded in the interrupt controller (such as the 8259A PIC) resolves conflicts by granting the interrupt request with highest priority, allowing the processor to handle the most critical event first.

### 8.3 Analog-to-Digital Conversion

Flash ADCs use a bank of comparators that compare the input voltage against reference levels. The outputs of these comparators form a thermometer code, which is converted to binary output using a priority encoder. The priority ensures that the most significant changed comparator determines the digital output.

## 9. Comparison: Encoder vs. Decoder

| Aspect       | Encoder                      | Decoder                           |
| ------------ | ---------------------------- | --------------------------------- |
| Function     | 2^n inputs → n outputs       | n inputs → 2^n outputs            |
| Type         | Many-to-few                  | Few-to-many                       |
| Inverse      | Decoder                      | Encoder                           |
| Priority     | Present in priority encoders | Not typically applicable          |
| Valid output | Indicates active input       | Often includes enable input       |
| Applications | Keyboard, interrupts, ADC    | Memory addressing, demultiplexing |

---

## Summary

An encoder is a combinational circuit that converts multiple input lines into a compact binary code. Simple encoders are limited to single active input conditions, while priority encoders resolve conflicts through hierarchical priority assignment. The 4-to-2 and 8-to-3 configurations demonstrate the scaling principles. Modern implementations include enable inputs for cascading, and HDL models enable synthesis for FPGA/ASIC implementation. Understanding encoder theory is essential for digital system design, particularly in input processing, interrupt handling, and data compression applications.
