# Decoders, Encoders & Multiplexers

## Introduction
These are fundamental **combinational digital circuits** used extensively in computer system architecture for data routing, address decoding, and information encoding. They form the backbone of memory systems, CPU design, and communication interfaces.

---

## Decoders

- **Definition**: Converts n-input binary code into 2^n unique output lines (one-hot encoding)
- **Types**:
  - 2-to-4 decoder
  - 3-to-8 decoder (expanded from 2-to-4)
  - 4-to-16 decoder
- **Enable Input**: Active-high or active-low enable pin for cascading
- **Boolean Expression**: For 2-to-4 decoder: Y0 = E·¬A1·¬A0, Y1 = E·¬A1·A0, etc.
- **Applications**:
  - Memory address decoding
  - I/O device selection
  - Demultiplexing (with enable input)
  - Implementing combinational logic functions

---

## Encoders

- **Definition**: Converts 2^n input lines into n-output binary code (opposite of decoder)
- **Types**:
  - **Binary Encoder**: Simple priority-less encoding
  - **Priority Encoder**: Handles multiple active inputs (higher priority to MSB)
- **Truth Table Example (4-to-2)**:
  - Inputs: D3, D2, D1, D0 → Outputs: A1, A0
- **Output**: Valid bit to indicate when at least one input is active
- **Applications**:
  - Interrupt handling (priority encoders)
  - Keyboard encoding
  - Reducing number of transmission lines

---

## Multiplexers (MUX)

- **Definition**: Selects one of many input lines and directs it to single output
- **Working**: Uses **select lines** (n select lines for 2^n inputs)
- **Types**:
  - 2-to-1 MUX (1 select line)
  - 4-to-1 MUX (2 select lines)
  - 8-to-1 MUX (3 select lines)
- **Boolean Expression**: Y = I0·¬S0 + I1·S0 (for 2:1 MUX)
- **Applications**:
  - Data routing in CPUs
  - Implementing boolean functions (via truth table mapping)
  - Parallel-to-serial conversion
  - Waveform generation

---

## Demultiplexers (DEMUX)

- Distributes one input to multiple outputs based on select lines
- Acts as inverse of MUX
- Used in data distribution and address routing

---

## Key Relationships

| Circuit | Inputs | Outputs | Function |
|---------|--------|---------|----------|
| Decoder | n | 2^n | Binary → One-hot |
| Encoder | 2^n | n | One-hot → Binary |
| MUX | 2^n + n (select) | 1 | Data selection |
| DEMUX | 1 + n (select) | 2^n | Data distribution |

---

## Conclusion
Decoders, encoders, and multiplexers are essential building blocks in digital computer architecture. They enable efficient data handling, memory addressing, and system integration. Understanding their design, Boolean expressions, and applications is crucial for exam success and practical digital system design.