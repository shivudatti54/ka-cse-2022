# Encoder

## Introduction

An encoder is a combinational circuit that converts binary information from 2^n input lines to n output lines, producing the binary code corresponding to the active input. Encoders are fundamental building blocks in digital systems, serving as crucial interfaces between multiple input signals and compressed binary representations. In the hierarchy of combinational logic circuits, encoders occupy a position complementary to decoders—they perform the inverse operation of converting multiple input lines into fewer output lines representing the input index.

The practical importance of encoders in modern computing cannot be overstated. Consider a computer keyboard: when you press a key, the keyboard encoder detects which of the 104 or more keys has been pressed and converts this information into a binary code that the computer's processor can understand. Similarly, in memory systems, encoders help reduce the number of wires needed to address multiple memory locations. Understanding encoder design and implementation is therefore essential for any computer science student, as these circuits form the backbone of input processing, data compression, and address selection in digital systems.

This topic explores various types of encoders, from basic binary encoders to more sophisticated priority encoders, examining their truth tables, logical expressions, and practical implementations using digital gates. We will also examine how these theoretical concepts translate into hardware description language (HDL) models, preparing you for both theoretical examinations and practical digital design work.

## Key Concepts

### Binary Encoder

A binary encoder is the simplest form of encoder that converts 2^n input lines into n binary output lines. It has 2^n input lines, of which only ONE can be active at any given time. The output is an n-bit binary number that indicates which input line is active. For instance, an 8-to-3 encoder has 8 input lines (I0 through I7) and 3 output lines (Y0, Y1, Y2).

The operation of a binary encoder can be understood through its truth table. For an 8-to-3 encoder, when input I0 is high (representing decimal 0), the output should be 000. When input I1 is high, the output should be 001, and so forth. However, a significant problem arises when multiple inputs are simultaneously active—the encoder produces an ambiguous or incorrect output. This limitation leads us to the concept of priority encoding.

### Truth Table for 8-to-3 Binary Encoder

| I7 | I6 | I5 | I4 | I3 | I2 | I1 | I0 | Y2 | Y1 | Y0 |
|----|----|----|----|----|----|----|----|----|----|-----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 1  |
| 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1  |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  |

### Boolean Expressions for 8-to-3 Encoder

From the truth table, we can derive the Boolean expressions for each output:

Y2 = I4 + I5 + I6 + I7

Y1 = I2 + I3 + I6 + I7

Y0 = I1 + I3 + I5 + I7

These expressions can be implemented using OR gates. The circuit would require three OR gates: a 4-input OR gate for Y2, a 4-input OR gate for Y1, and a 4-input OR gate for Y0.

### Priority Encoder

A priority encoder addresses the fundamental limitation of binary encoders by establishing a hierarchy among input lines. When multiple inputs are active simultaneously, the priority encoder outputs the binary code corresponding to the HIGHEST PRIORITY active input. Typically, input with the highest index (I7 in an 8-input encoder) has the highest priority.

The 74LS148 is a classic 10-to-4 line priority encoder IC that has been widely used in digital systems. This IC features active-low inputs and outputs, along with additional control signals like EI (Enable Input), EO (Enable Output), and GS (Group Select) for cascading multiple encoders.

### Truth Table for 8-to-3 Priority Encoder

| I7 | I6 | I5 | I4 | I3 | I2 | I1 | I0 | Y2 | Y1 | Y0 | V |
|----|----|----|----|----|----|----|----|----|----|----|---|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | X  | X  | X  | 0 |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1 |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | X  | 0  | 0  | 1  | 1 |
| 0  | 0  | 0  | 0  | 0  | 1  | X  | X  | 0  | 1  | 0  | 1 |
| 0  | 0  | 0  | 0  | 1  | X  | X  | X  | 0  | 1  | 1  | 1 |
| 0  | 0  | 0  | 1  | X  | X  | X  | X  | 1  | 0  | 0  | 1 |
| 0  | 0  | 1  | X  | X  | X  | X  | X  | 1  | 0  | 1  | 1 |
| 0  | 1  | X  | X  | X  | X  | X  | X  | 1  | 1  | 0  | 1 |
| 1  | X  | X  | X  | X  | X  | X  | X  | 1  | 1  | 1  | 1 |

In this table, V is a valid bit that indicates whether a valid input is present. When all inputs are zero, V = 0, and the output is invalid. The X represents "don't care" conditions.

### Decimal to BCD Encoder

A decimal to BCD encoder converts ten input lines (representing decimal digits 0-9) into a 4-bit BCD output. This type of encoder is commonly used in calculators and digital displays. The 74LS147 is a 10-to-4 line priority encoder that performs this function, outputting the BCD code for the highest-order active input.

The truth table for a decimal to BCD encoder shows that when input D0 (representing decimal 0) is active, the output is 0000. When D1 is active, output is 0001, and so on. Since this is a priority encoder, if multiple keys are pressed, the highest decimal digit takes priority.

### Keyboard Encoder

A practical application of encoders is in computer keyboards. A full keyboard matrix might have 16 rows and 8 columns, creating 128 possible key positions. An encoder reduces this to a 7-bit binary code that identifies which key has been pressed. Modern keyboards use more sophisticated encoding methods, including matrix scanning with microcontrollers, but the fundamental principle remains the same.

## Examples

### Example 1: Designing a 4-to-2 Binary Encoder

Design a binary encoder for 4 input lines to 2 output lines.

SOLUTION:

Step 1: Identify the number of inputs and outputs
- Inputs: I0, I1, I2, I3 (4 inputs, so 2^2 = 4)
- Outputs: Y0, Y1 (2 outputs)

Step 2: Create the truth table

| I3 | I2 | I1 | I0 | Y1 | Y0 |
|----|----|----|----|----|-----|
| 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | 0  | 0  | 1  |
| 0  | 1  | 0  | 0  | 1  | 0  |
| 1  | 0  | 0  | 0  | 1  | 1  |

Step 3: Derive Boolean expressions
- Y0 = I1 + I3
- Y1 = I2 + I3

Step 4: Draw the circuit
The circuit requires two OR gates:
- One 2-input OR gate for Y0 with inputs I1 and I3
- One 2-input OR gate for Y1 with inputs I2 and I3

### Example 2: Analyzing a Priority Encoder Problem

For a priority encoder with 4 inputs where I3 has highest priority and I0 has lowest priority, determine the output when inputs are:
(a) I3 = 1, I2 = 0, I1 = 1, I0 = 1
(b) I3 = 0, I2 = 1, I1 = 1, I0 = 0
(c) I3 = 0, I2 = 0, I1 = 0, I0 = 0

SOLUTION:

(a) Since I3 = 1 (highest priority), the output corresponds to decimal 3, which is binary 11. Output: Y1 = 1, Y0 = 1

(b) I3 = 0, but I2 = 1 (second highest priority). The output corresponds to decimal 2, which is binary 10. Output: Y1 = 1, Y0 = 0

(c) All inputs are 0. This represents an invalid or no-input condition. Typically, a valid bit V = 0 would be set, and outputs would be don't care or 00.

### Example 3: Implementing a Decimal to BCD Encoder

Implement a decimal to BCD encoder using basic gates for digits 0-5 (to simplify).

Inputs: D0 through D5 representing decimal numbers 0-5
Outputs: Y3, Y2, Y1, Y0 (BCD code)

SOLUTION:

Truth table for inputs 0-5:

| D5 | D4 | D3 | D2 | D1 | D0 | Y3 | Y2 | Y1 | Y0 |
|----|----|----|----|----|----|----|----|----|-----|
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 1  |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1  |

Deriving expressions:
- Y3 = 0 (since numbers 0-5 only need bits Y2, Y1, Y0)
- Y2 = D4 + D5
- Y1 = D2 + D3 + D5
- Y0 = D1 + D3 + D5

## Exam Tips

1. UNDERSTAND THE FUNDAMENTAL DIFFERENCE between encoders and decoders. Encoders have more inputs than outputs (2^n to n), while decoders have more outputs than inputs (n to 2^n). This is a common examination question.

2. REMEMBER THE PRIORITY CONCEPT. For priority encoders, when multiple inputs are active, the output corresponds to the highest-priority input. Know how to read priority encoder truth tables, especially the "don't care" (X) conditions.

3. KNOW HOW TO DERIVE BOOLEAN EXPRESSIONS from encoder truth tables. Practice writing Sum of Products (SOP) expressions for each output based on which input lines cause that output to be HIGH.

4. UNDERSTAND THE VALID BIT (V) in priority encoders. This output indicates whether a valid input is present. When all inputs are zero, V = 0, meaning the output is meaningless.

5. BE FAMILIAR WITH STANDARD ICs. The 74LS148 (8-to-3 priority encoder) and 74LS147 (10-to-4 priority encoder) are commonly referenced in DU examinations. Know their pin configurations and basic operation.

6. KNOW THE LIMITATION OF BINARY ENCODERS. They cannot handle multiple simultaneous inputs—only one input should be HIGH at a time. This distinction is frequently tested.

7. PRACTICE DRAWING CIRCUITS. Be able to draw the gate-level implementation of simple encoders using OR gates. This is a common short-answer question in exams.

8. UNDERSTAND CASCADING. Know how multiple priority encoders can be connected to handle more inputs. The Enable Input (EI) and Enable Output (EO) pins of the 74LS148 are crucial for this.

9. DON'T CONFUSE ENCODER WITH DECODER in the exam hall. A decoder selects one output line based on binary input; an encoder produces binary code from one-hot input.

10. KNOW THE APPLICATIONS. Keyboard encoding, address encoding in memory systems, and converting parallel data to serial are common application-based questions.