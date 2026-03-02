# Combinational Circuits - Summary

## Core Definitions

- **Combinational Circuit**: A digital circuit where outputs depend exclusively on current inputs with no memory of previous states. Mathematically: Y = f(I₀, I₁, ..., Iₙ₋₁)
- **Propagation Delay (tₚ)**: Time interval between input change and corresponding stable output change in a logic gate
- **Fan-in**: Maximum number of independent inputs a logic gate can accommodate
- **Fan-out**: Maximum number of gate inputs a single output can drive without degradation
- **Critical Path**: Longest combinational path determining maximum circuit speed
- **Hazard**: Transient malfunction (glitch) caused by unequal propagation delays during input transitions

## Fundamental Properties

1. **No Memory**: Output = f(present inputs) only
2. **No Feedback**: Feedforward architecture
3. **Deterministic**: Same input always produces same output
4. **Complete Specification**: Every output is a Boolean function of all inputs

## Design Methodology

**Analysis**: Circuit → Boolean Expressions → Truth Table
**Synthesis**: Specification → Truth Table → Boolean Expression → Minimization (K-Map) → Circuit

## Major Circuit Categories

| Category | Examples | Primary Function |
|----------|----------|------------------|
| Arithmetic | Half Adder, Full Adder, Ripple Carry Adder | Binary addition |
| Data Routing | Multiplexer, Demultiplexer | Data selection and distribution |
| Code Conversion | Encoder, Decoder, Priority Encoder | Code transformation |
| Comparison | Magnitude Comparator | Binary number comparison |

## Critical Relationships

- **Two-level delay**: 2 × tₚ (maximum)
- **n-bit ripple carry delay**: n × tₚ (full adder)
- **K-Map grouping**: Groups of size 2ᵏ eliminate k variables
- **Hazard elimination**: Add redundant prime implicants

## Design Optimization

Combinational circuits are optimized through Boolean minimization (reducing literal count), gate decomposition (trading speed for area), and balancing paths (reducing critical path delay). The choice between two-level (fast, more gates) and multi-level (slower, fewer gates) implementations involves fundamental tradeoffs in digital design.