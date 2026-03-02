# **Combinational Logic: Introduction, Combinational Circuits, Design Procedure, Binary Adder- Subtractor, Decoders, Encoders, Multiplexers**

## **Introduction**

Combinational logic is a branch of digital electronics that deals with the design and analysis of digital circuits that produce an output based on a combination of inputs. These circuits are called "combinational" because the output is a function of the input combinations, rather than a memorized sequence of inputs.

Combinational logic circuits are used in a wide range of applications, including digital arithmetic, control systems, and data processing.

## **Combinational Circuits**

A combinational circuit is a digital circuit that produces an output based on a combination of inputs. The output of a combinational circuit is a function of the input combinations, and it does not have any memory.

## **Types of Combinational Circuits**

- **Series-Parallel Combinational Circuit**: A series-parallel combinational circuit is a circuit that consists of a series of parallel circuits.
- **Parallel-Series Combinational Circuit**: A parallel-series combinational circuit is a circuit that consists of a series of parallel circuits, each of which is connected in parallel to a series circuit.

## **Design Procedure**

The design procedure for a combinational circuit involves the following steps:

1. **Define the problem**: Define the problem that the combinational circuit is intended to solve.
2. **Determine the inputs and outputs**: Determine the inputs and outputs of the combinational circuit.
3. **Choose a logic function**: Choose a logic function that will be used to determine the output of the combinational circuit.
4. **Design the logic function**: Design the logic function using a truth table or a Karnaugh map.
5. **Implement the logic function**: Implement the logic function using a combinational circuit.

## **Binary Adder-Subtractor**

A binary adder-subtractor is a combinational circuit that adds or subtracts two binary numbers. It can be used to perform both addition and subtraction operations.

**How it works**

- **Addition**: The binary adder-subtractor adds two binary numbers by performing an AND operation between the two numbers and an OR operation between the result and a carry-in signal.
- **Subtraction**: The binary adder-subtractor subtracts two binary numbers by performing a NOT operation on the second number, an AND operation between the result and a borrow-in signal, and an OR operation between the result and a carry-out signal.

**Example**

Suppose we want to add the binary numbers 101 (5) and 110 (6). The binary adder-subtractor would perform the following operations:

- **AND operation**: 101 AND 110 = 000
- **OR operation**: 000 OR 1 = 001 (carry-out)
- **Addition**: 1 + 0 + 0 = 1

The result of the addition is 001, which represents the binary number 5 + 6 = 11.

## **Decoders**

A decoder is a combinational circuit that converts a binary code into a unique output. It consists of a set of logic gates that are connected in a specific way to produce the output.

## **Types of Decoders**

- **Single-Input Decoder**: A single-input decoder is a decoder that takes a single binary input and produces a unique output.
- **Multi-Input Decoder**: A multi-input decoder is a decoder that takes multiple binary inputs and produces a unique output.

**Example**

Suppose we want to decode a binary code 1010 into a unique output. The decoder would produce the output 2, which represents the decimal number 10.

## **Encoders**

An encoder is a combinational circuit that converts a binary code into a unique multiple-bit output. It consists of a set of logic gates that are connected in a specific way to produce the output.

## **Types of Encoders**

- **Single-Output Encoder**: A single-output encoder is an encoder that produces a single multiple-bit output.
- **Multi-Output Encoder**: A multi-output encoder is an encoder that produces multiple multiple-bit outputs.

**Example**

Suppose we want to encode a binary code 1010 into a unique multiple-bit output. The encoder would produce the output 0010, which represents the binary number 2.

## **Multiplexers**

A multiplexer is a combinational circuit that selects one of multiple binary inputs and produces a unique output. It consists of a set of logic gates that are connected in a specific way to produce the output.

## **Types of Multiplexers**

- **Single-Input Multiplexer**: A single-input multiplexer is a multiplexer that takes a single binary input and produces a unique output.
- **Multi-Input Multiplexer**: A multi-input multiplexer is a multiplexer that takes multiple binary inputs and produces a unique output.

**Example**

Suppose we want to select one of three binary inputs (A, B, or C) and produce a unique output. The multiplexer would produce the output A, which represents the binary number 000.

## **Key Concepts**

- **Combinational circuit**: A digital circuit that produces an output based on a combination of inputs.
- **Series-parallel combinational circuit**: A circuit that consists of a series of parallel circuits.
- **Parallel-series combinational circuit**: A circuit that consists of a series of parallel circuits, each of which is connected in parallel to a series circuit.
- **Truth table**: A table that lists all possible input combinations and their corresponding outputs.
- **Karnaugh map**: A map that is used to simplify truth tables.
- **Binary adder-subtractor**: A combinational circuit that adds or subtracts two binary numbers.
- **Decoder**: A combinational circuit that converts a binary code into a unique output.
- **Encoder**: A combinational circuit that converts a binary code into a unique multiple-bit output.
- **Multiplexer**: A combinational circuit that selects one of multiple binary inputs and produces a unique output.
