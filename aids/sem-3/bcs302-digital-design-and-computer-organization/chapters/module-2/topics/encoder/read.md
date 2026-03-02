# Encoders

## What is an Encoder?

An **Encoder** is a combinational circuit that converts 2^n input lines into n output lines. It performs the reverse operation of a decoder, converting a one-hot input (only one input active) into a binary code.

## Types of Encoders

### 1. Simple Encoder (4:2 Encoder)

- **4 inputs:** I0, I1, I2, I3 (one-hot)
- **2 outputs:** Y1, Y0 (binary code)
- Assumes only one input is active at a time

### 2. Priority Encoder

- Handles multiple active inputs
- Outputs code for highest priority input
- Includes valid output (V) to indicate any input active

### 3. Octal-to-Binary Encoder (8:3)

- 8 inputs to 3-bit binary output
- Common in keyboard and switch applications

## 4:2 Simple Encoder

### Truth Table

| I3  | I2  | I1  | I0  | Y1  | Y0  |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 1   | 0   | 0   |
| 0   | 0   | 1   | 0   | 0   | 1   |
| 0   | 1   | 0   | 0   | 1   | 0   |
| 1   | 0   | 0   | 0   | 1   | 1   |

### Boolean Expressions

- Y1 = I3 + I2
- Y0 = I3 + I1

## 8:3 Priority Encoder

### Features

- 8 inputs (I0-I7), 3 outputs (Y2, Y1, Y0)
- Valid bit (V): 1 when any input is active
- Group Signal (GS): For cascading
- Enable Input (EI): Enable control

### Priority Table (I7 highest priority)

| Active Inputs       | Y2  | Y1  | Y0  | V   |
| ------------------- | --- | --- | --- | --- |
| None                | X   | X   | X   | 0   |
| I0 only             | 0   | 0   | 0   | 1   |
| I1 (I0 don't care)  | 0   | 0   | 1   | 1   |
| I7 (all don't care) | 1   | 1   | 1   | 1   |

### Boolean Expressions

- Y0 = I1 + I3 + I5 + I7
- Y1 = I2 + I3 + I6 + I7
- Y2 = I4 + I5 + I6 + I7
- V = I0 + I1 + I2 + I3 + I4 + I5 + I6 + I7

## Decimal-to-BCD Encoder (10:4)

Converts decimal digit (0-9) to 4-bit BCD:

- 10 input lines for digits 0-9
- 4 output lines for BCD code
- Used in calculators, keyboards

## Applications

1. **Keyboards:** Convert key press to scan code
2. **Position Encoders:** Encode shaft/wheel position
3. **Data Compression:** Reduce number of lines
4. **Interrupt Handling:** Priority interrupt controller
5. **Address Generation:** Memory systems

## Simple vs Priority Encoder

| Feature           | Simple Encoder | Priority Encoder       |
| ----------------- | -------------- | ---------------------- |
| Multiple inputs   | Invalid        | Handles gracefully     |
| No input active   | Undefined      | Valid bit = 0          |
| Output when all 0 | Same as I0     | V=0 indicates no input |
| Complexity        | Lower          | Higher                 |

## Key Points Summary

- Encoder: 2^n inputs to n outputs (reverse of decoder)
- Simple encoder assumes one-hot input
- Priority encoder handles multiple active inputs
- Outputs binary code for active (or highest priority) input
- Valid bit indicates at least one input active
- Essential for interrupt priority, keyboards, position encoding
