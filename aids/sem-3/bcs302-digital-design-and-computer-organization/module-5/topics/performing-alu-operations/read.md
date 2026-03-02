# Performing ALU Operations


## Table of Contents

- [Performing ALU Operations](#performing-alu-operations)
- [Introduction](#introduction)
- [ALU Internal Architecture](#alu-internal-architecture)
  - [Arithmetic Circuit](#arithmetic-circuit)
  - [Logic Circuit](#logic-circuit)
  - [Multiplexer-Based Operation Selection](#multiplexer-based-operation-selection)
- [ALU Control and Register Transfers](#alu-control-and-register-transfers)
  - [Control Signal Generation](#control-signal-generation)
  - [Data Path Integration](#data-path-integration)
- [Flag Generation and Usage](#flag-generation-and-usage)
  - [Status Flags](#status-flags)
- [Worked Examples](#worked-examples)
  - [Example 1: 4-bit ALU Operation Selection](#example-1-4-bit-alu-operation-selection)
  - [Example 2: Overflow Detection](#example-2-overflow-detection)
  - [Example 3: Register Transfer Sequence](#example-3-register-transfer-sequence)
- [Exam Tips](#exam-tips)

## Introduction

The Arithmetic Logic Unit (ALU) represents the computational heart of any processor, responsible for executing all arithmetic and logical operations. In the execute phase of instruction processing, the control unit generates appropriate signals to route operands from registers to the ALU, selects the desired operation through function select lines, and captures the result for storage. Understanding how ALU operations are performed requires examining the internal circuit organization, the control mechanisms that govern operation selection, the data path integration with register files, and the flag generation mechanisms that enable conditional program flow. This topic provides a comprehensive examination of these aspects, establishing the foundation for understanding processor design and pipeline implementation.

The ALU operates as a combinational circuit that produces outputs solely based on current inputs, without internal storage elements. The operation performed depends on the function select bits (F₃F₂F₁F₀) that gate various sub-circuits through multiplexers to produce the final result. Modern ALUs support a standard set of operations including addition, subtraction, logical AND, OR, XOR, NOT, comparison, and shift operations. The selection between these operations occurs through a multiplexer-based architecture where each operation's circuit computes its result in parallel, and the multiplexer selects the appropriate output based on the control signals.

## ALU Internal Architecture

### Arithmetic Circuit

The arithmetic circuit forms the core of ALU computational capability, with the ripple-carry adder (RCA) serving as the fundamental building block for addition and subtraction operations. An n-bit ripple-carry adder consists of n full adders connected in cascade, where each full adder accepts two 1-bit inputs (Aᵢ, Bᵢ) and a carry input (Cᵢ), producing a sum output (Sᵢ) and carry output (Cᵢ₊₁). The Boolean expressions for a full adder are: Sᵢ = Aᵢ ⊕ Bᵢ ⊕ Cᵢ and Cᵢ₊₁ = AᵢBᵢ + Cᵢ(Aᵢ ⊕ Bᵢ).

For implementing subtraction, the two's complement method is employed where subtrahend B is inverted and incremented by 1 through the carry input. The control signal S (subtract) determines whether B or its complement is used: when S = 0, the circuit performs A + B (addition); when S = 1, the circuit performs A + B' + 1 = A - B (subtraction). The arithmetic circuit produces two intermediate outputs: the arithmetic sum (H₁ = A + B) and arithmetic sum with B complemented (H₂ = A + B'), enabling both operations through the multiplexer select lines.

### Logic Circuit

The logic circuit provides bitwise operations essential for data manipulation and decision-making. The four fundamental logic operations implemented are AND, OR, XOR, and NOT. Each operation is implemented using corresponding gates operating on individual bit positions, meaning a 32-bit ALU contains 32 parallel AND gates, 32 parallel OR gates, and so forth. The logic circuit produces four outputs: F₁ = A ∧ B (AND), F₂ = A ∨ B (OR), F₃ = A ⊕ B (XOR), and F₄ = ¬A (NOT). These operations are computed simultaneously in parallel, with the multiplexer selecting the desired output based on operation select bits.

### Multiplexer-Based Operation Selection

The ALU uses a hierarchy of multiplexers to select between arithmetic and logic results, then within each category. The first-level multiplexer chooses between arithmetic result (H) and logic result (T) based on the operation type bit. A second-level multiplexer within the arithmetic section selects between H₁ and H₂ based on the subtract control signal. The final output (Result) is thus: Result = S₁S₀'H + S₁S₀T, where S₁S₀ represent the operation select bits that determine whether arithmetic, AND, OR, or XOR operations are performed.

## ALU Control and Register Transfers

### Control Signal Generation

The ALU receives control signals from the processor's control unit, which decodes the instruction opcode to determine the operation to perform. The primary control signals include: Operation Select (S₂S₁S₀) that choose the specific operation, Carry In (Cₙ) that enables addition/subtraction, and Result Enable that gates the output to the destination register. For a typical R-type instruction format (opcode, rs, rt, rd, shamt, funct), the funct field directly determines the ALU operation when the main opcode indicates an R-type operation.

Consider the instruction "ADD R1, R2, R3" encoded as R-type with funct = 0x20. The control unit sets ALUop to 10 (R-type), the Register Decoder activates read enable for registers R2 and R3, the Multiplexers select the register file outputs as ALU inputs, Operation Select is set to 000 (addition), and the result is written back to R1. The register transfer notation for this operation is: R[rd] ← R[rs] + R[rt], implemented through the sequence: ReadRegister(rs), ReadRegister(rt), ALU.perform(Add, R[rs], R[rt]), WriteRegister(rd, Result).

### Data Path Integration

The ALU interfaces with the register file through the processor data path. During the execute phase, two registers source their contents onto the A and B buses that connect to the ALU inputs. The ALU computes the result, which passes through the Result bus to be written back to the destination register. The timing sequence involves: T₀: Control signals asserted; T₁: Register outputs stable on A and B buses; T₂: ALU computation completes (propagation delay); T₃: Result available on result bus; T₄: Write enable writes result to destination register. For a 32-bit ripple-carry adder, the critical path delay equals n × t₍FA₎ where t₍FA₎ is the full adder propagation delay, typically limiting maximum clock frequency in non-pipelined designs.

## Flag Generation and Usage

### Status Flags

ALUs generate status flags that reflect the computational result and enable conditional operations. The four primary flags are: Zero Flag (Z) = 1 when result equals zero, indicating equality in comparisons; Carry Flag (C) = 1 when unsigned overflow occurs (carry out from most significant bit); Overflow Flag (V) = 1 when signed overflow occurs, detected when carry into and out of MSB differ; Negative Flag (N) = 1 when result is negative (MSB = 1 for signed representation).

The overflow flag for addition (V) is computed as: V = Cₙ ⊕ Cₙ₋₁, where Cₙ is the carry out and Cₙ₋₁ is the carry into the sign bit. For subtraction, overflow occurs when the signs of operands differ and the result sign differs from the first operand. The Zero flag enables efficient equality testing: after subtraction, Z = 1 indicates operands are equal. These flags are stored in the Program Status Word (PSW) or Condition Code Register and are used by conditional branch instructions to alter program flow.

## Worked Examples

### Example 1: 4-bit ALU Operation Selection

For a 4-bit ALU with select bits S₂S₁S₀ and carry input Cₙ, determine the output for operation 011 (subtraction) when A = 0101 (5) and B = 0011 (3).

Solution: Operation 011 selects subtraction (A - B). The subtract control inverts B: B' = 1100. With Cₙ = 1 (adding 1 for two's complement), the ALU computes A + B' + 1 = 0101 + 1100 + 1 = 1010 (binary) = 2 (decimal). Indeed, 5 - 3 = 2. The Zero flag (Z) = 0 since result ≠ 0. The Carry flag depends on whether unsigned underflow occurred; since 5 ≥ 3, no borrow is needed, so C = 0.

### Example 2: Overflow Detection

Given two signed 8-bit numbers A = 127 (01111111) and B = 1 (00000001), determine if overflow occurs when adding and subtracting.

Solution: For addition (A + B): Maximum positive 8-bit signed = +127. 127 + 1 = 128 exceeds range. Carry into MSB = 1, Carry out = 0. Since C₈ ⊕ C₇ = 1 ⊕ 0 = 1, Overflow flag V = 1. Signed overflow has occurred. For subtraction (A - B = A + B' + 1): 127 - 1 = 126, which is within range. Carry into MSB = 1, Carry out = 1. V = 1 ⊕ 1 = 0. No overflow. This illustrates that overflow depends on both the operation and the specific operand values.

### Example 3: Register Transfer Sequence

For the instruction "SUB R5, R1, R2" executing on a single-cycle datapath, list all control signals and register transfers.

Solution: The instruction performs R[5] ← R[1] - R[2]. Control signals: RegDst = 1 (destination in rd field), RegWrite = 1, ALUSrc = 0 (second operand from register), ALUOp = 10 (R-type), ALUControl = 110 (subtract). Register transfers: Step 1: Read registers R1 and R2, placing contents on ReadData1 and ReadData2. Step 2: ALU receives R[1] and R[2], performs subtraction, produces Result. Step 3: Result written to register R5 through WriteData input. The complete register transfer: R[5] ← R[1] - R[2], with flags updated to reflect result properties.

## Exam Tips

1. **ALU Design**: Remember that ALU is a combinational circuit—the output depends only on current inputs, not on history or previous states.

2. **Two's Complement Subtraction**: The ALU implements subtraction using addition of the two's complement. Setting carry-in to 1 while selecting B' achieves A + B' + 1 = A - B.

3. **Overflow Detection**: For signed arithmetic, overflow occurs when the carry into the sign bit differs from the carry out of the sign bit: V = Cₙ ⊕ Cₙ₋₁.

4. **Flag Usage**: The Zero flag enables branch-on-equal operations; after computing R[rs] - R[rt], if Z = 1 then registers are equal.

5. **Critical Path**: In ripple-carry adders, the critical path delay is proportional to the number of bits—key consideration for processor clock frequency.

6. **Operation Select Encoding**: Standard encoding uses multiplexer selection where S bits directly choose which sub-circuit output passes to the result.

7. **Register Transfer Notation**: Be able to translate between high-level operations (ADD R1, R2, R3) and register transfer notation (R[1] ← R[2] + R[3]).