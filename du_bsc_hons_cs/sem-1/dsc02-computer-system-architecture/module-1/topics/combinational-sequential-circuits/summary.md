# Combinational and Sequential Circuits

## Introduction
In digital system design, circuits are broadly classified as **Combinational** and **Sequential** circuits. While combinational circuits form the backbone of data processing, sequential circuits provide memory and state-keeping capabilities essential for computing. Understanding both is fundamental to Computer System Architecture and digital electronics.

## Combinational Circuits
- **Definition**: Output depends *only* on the present input values; no memory of past inputs.
- **Key Characteristics**:
  - No storage elements
  - Output changes immediately with input change
  - Can be represented by Boolean functions
- **Common Examples**:
  - **Arithmetic**: Adders (Half, Full), Subtractors, ALU building blocks
  - **Data Routing**: Multiplexers (MUX), Demultiplexers (DEMUX)
  - **Encoding/Decoding**: Encoders, Decoders, Code converters
  - **Comparison**: Magnitude Comparators
- **Design Process**: Truth Table → Boolean Expression → Simplification (K-Map/Quine-McCluskey) → Logic Circuit

## Sequential Circuits
- **Definition**: Output depends on *present input* and *past history* (current state); incorporates memory elements.
- **Key Characteristics**:
  - Contains storage elements (Latches/Flip-flops)
  - Requires clock signal (for synchronous type)
  - State transitions governed by timing
- **Types**:
  - **Synchronous**: State changes synchronized with clock edge (counters, registers, FSMs)
  - **Asynchronous**: State changes depend on input changes without clock (fast but complex)
- **Core Components**:
  - **Flip-Flops**: SR, JK, D, T — basic memory units
  - **Registers**: Groups of flip-flops for storing n-bits
  - **Counters**: Ring, Johnson, Binary (async/sync)
  - **State Machines**: Mealy and Moore models
- **Design Process**: State Diagram → State Table → Excitation Table → Boolean Logic → Circuit

## Conclusion
Combinational circuits handle data transformation without memory, while sequential circuits enable state retention and control flow. Together, they form the complete building blocks of all digital systems — from simple calculators to complex processors. Mastery of their design and analysis is essential for the Delhi University B.Sc. (H) CS examination under NEP 2024 UGCF syllabus.