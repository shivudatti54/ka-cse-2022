# Combinational Logic

=====================

## Introduction

---

Combinational logic is a branch of digital circuit design that deals with the creation of digital circuits that perform logical operations on binary data. These circuits are called "combinational" because their output is a function of the current input values, and not stored in any memory.

## Combinational Circuits

---

A combinatorial circuit is a digital circuit that performs a logical operation on one or more input signals. The output of the circuit is a single output signal that is a function of the current input values.

### Types of Combinational Circuits

- **AND Gate**: Produces an output of 1 only if all inputs are 1.
- **OR Gate**: Produces an output of 1 if any input is 1.
- **NOT Gate** (Inverter): Produces an output that is the opposite of the input.
- **XOR Gate**: Produces an output of 1 if any input is different from the other input.

### Characteristics of Combinational Circuits

- **No Memory**: Combinational circuits do not store any information in memory.
- **No Feedback**: Combinational circuits do not have any feedback loop.
- **Deterministic**: Combinational circuits have a deterministic output for a given input.

## Design Procedure

---

The design procedure for combinatorial circuits involves the following steps:

1. **Define the problem**: Identify the function that the circuit needs to perform.
2. **Choose the logic gates**: Select the logic gates that will be used to implement the function.
3. **Draw the circuit**: Draw the circuit using the chosen logic gates.
4. **Verify the circuit**: Verify that the circuit produces the correct output for the given input.

### Karnaugh Map Method

The Karnaugh map method is a technique used to simplify Boolean expressions and design combinatorial circuits.

**Karnaugh Map**

|     | A=0 | A=1 |
| --- | --- | --- |
| B=0 | X   | X   |
| B=1 | X   | X   |

- **Simplification**: The Karnaugh map can be simplified by combining adjacent 1's.

## Binary Adder-Subtractor

---

A binary adder-subtractor is a combinatorial circuit that adds or subtracts two binary numbers.

### Decimal to Binary Conversion

To design a binary adder-subtractor, we need to convert the decimal numbers to binary.

### Adder-Subtractor Circuit

The adder-subtractor circuit consists of the following components:

- **Half Adder**: A half adder is a simple combinatorial circuit that adds two binary digits.
- **Full Adder**: A full adder is a more complex combinatorial circuit that adds three binary digits.
- **Subtractor**: A subtractor is a combinatorial circuit that subtracts one binary number from another.

### Example: Binary Adder-Subtractor

|     | A   | B   | C   | Sum | Difference |
| --- | --- | --- | --- | --- | ---------- |
| 0   | 0   | 0   | 0   | 0   | 0          |
| 0   | 0   | 0   | 1   | 1   | 1          |
| 0   | 0   | 1   | 0   | 1   | 1          |
| 0   | 0   | 1   | 1   | 0   | 1          |
| 0   | 1   | 0   | 0   | 1   | 1          |
| 0   | 1   | 0   | 1   | 0   | 1          |
| 0   | 1   | 1   | 0   | 0   | 1          |
| 0   | 1   | 1   | 1   | 1   | 0          |
| 1   | 0   | 0   | 0   | 1   | 1          |
| 1   | 0   | 0   | 1   | 1   | 0          |
| 1   | 0   | 1   | 0   | 1   | 0          |
| 1   | 0   | 1   | 1   | 0   | 0          |
| 1   | 1   | 0   | 0   | 0   | 1          |
| 1   | 1   | 0   | 1   | 1   | 0          |
| 1   | 1   | 1   | 0   | 0   | 0          |
| 1   | 1   | 1   | 1   | 1   | 0          |

## Decoders

---

A decoder is a combinatorial circuit that converts a binary code into a set of output signals.

### Types of Decoders

- **Binary Decoder**: A binary decoder converts a binary code into a set of output signals.
- **Gray Decoder**: A Gray decoder converts a binary code into a set of output signals, where each output signal is the opposite of the Gray code.

## Encoders

---

An encoder is a combinatorial circuit that converts a set of input signals into a binary code.

### Types of Encoders

- **Binary Encoder**: A binary encoder converts a set of input signals into a binary code.
- **Gray Encoder**: A Gray encoder converts a set of input signals into a binary code, where each output signal is the opposite of the Gray code.

## Multiplexers

---

A multiplexer is a combinatorial circuit that selects one of several input signals as the output.

### Types of Multiplexers

- **Binary Multiplexer**: A binary multiplexer selects one of several binary input signals as the output.
- **Gray Multiplexer**: A Gray multiplexer selects one of several Gray input signals as the output.

### Example: Binary Multiplexer

|     | A   | B   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 0   | 1   |
| 0   | 1   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 0   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |
| 1   | 1   | 1   |

| Output | A   | B   |
| ------ | --- | --- |
| 0      | 00  | 00  |
| 0      | 00  | 01  |
| 0      | 01  | 00  |
| 0      | 01  | 01  |
| 1      | 10  | 00  |
| 1      | 10  | 01  |
| 1      | 11  | 00  |
| 1      | 11  | 01  |
