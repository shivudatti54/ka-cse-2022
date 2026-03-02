# Multiplexers (MUX)

## What is a Multiplexer?

A **Multiplexer (MUX)** is a combinational circuit that selects one of several input signals and forwards it to a single output line. It acts as a digital switch controlled by select lines. Often called a "data selector" or "many-to-one" device.

## Basic Structure

### 2:1 Multiplexer

- **2 data inputs:** I0, I1
- **1 select line:** S
- **1 output:** Y
- **Expression:** Y = S'I0 + SI1

### 4:1 Multiplexer

- **4 data inputs:** I0, I1, I2, I3
- **2 select lines:** S1, S0
- **1 output:** Y
- **Expression:** Y = S1'S0'I0 + S1'S0I1 + S1S0'I2 + S1S0I3

### General n:1 Multiplexer

- **n = 2^k data inputs**
- **k select lines**
- **1 output**

## Truth Tables

### 2:1 MUX

| S   | Y   |
| --- | --- |
| 0   | I0  |
| 1   | I1  |

### 4:1 MUX

| S1  | S0  | Y   |
| --- | --- | --- |
| 0   | 0   | I0  |
| 0   | 1   | I1  |
| 1   | 0   | I2  |
| 1   | 1   | I3  |

## Gate-Level Implementation

### 2:1 MUX

- 2 AND gates
- 1 OR gate
- 1 NOT gate (inverter)

### 4:1 MUX

- 4 AND gates (3-input each)
- 1 OR gate (4-input)
- 2 NOT gates

## Multiplexer as Universal Function Generator

A **2^n:1 MUX can implement any n-variable Boolean function** by:

1. Connect function variables to select lines
2. Connect function values (0/1) or remaining variables to data inputs

### Example: F(A,B) = A XOR B using 4:1 MUX

- S1 = A, S0 = B
- I0 = 0 (when A=0, B=0, F=0)
- I1 = 1 (when A=0, B=1, F=1)
- I2 = 1 (when A=1, B=0, F=1)
- I3 = 0 (when A=1, B=1, F=0)

## Building Larger MUX from Smaller

### 4:1 MUX from 2:1 MUX

- Use 3 two-input multiplexers
- Two 2:1 MUX in first level
- One 2:1 MUX in second level

### 8:1 MUX from 4:1 MUX

- Use 2 four-input MUX + 1 two-input MUX
- Or use tree structure

## Applications

1. **Data Routing:** Select data source in communication
2. **Function Implementation:** Replace complex gate networks
3. **Bus Systems:** Select data from multiple sources
4. **ALU Design:** Operation selection
5. **Memory Addressing:** Select memory bank
6. **Time-Division Multiplexing:** Communication systems

## Key Parameters

| Parameter         | Description                      |
| ----------------- | -------------------------------- |
| Propagation Delay | Time from input change to output |
| Fan-out           | Number of gates output can drive |
| Power Consumption | Typically low for CMOS           |
| Enable Input      | Additional control for output    |

## Multiplexer with Enable

Many MUX have an enable (E) input:

- E = 1: MUX operates normally
- E = 0: Output is 0 (or high-Z) regardless of inputs

## Key Points Summary

- MUX selects one of 2^n inputs using n select lines
- Acts as a digital switch or data selector
- 2:1 MUX: Y = S'I0 + SI1
- Can implement any Boolean function
- Building block for larger multiplexers
- Essential in data routing and ALU design
