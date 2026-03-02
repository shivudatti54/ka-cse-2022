# Loading Constants in ARM Assembly

## Table of Contents

- [Loading Constants in ARM Assembly](#loading-constants-in-arm-assembly)
- [Introduction](#introduction)
- [Theoretical Foundation: ARM Immediate Value Encoding](#theoretical-foundation-arm-immediate-value-encoding)
  - [Encoding Mechanism](#encoding-mechanism)
  - [Examples of Encodable vs Non-Encodable Values](#examples-of-encodable-vs-non-encodable-values)
- [Method 1: MOV Instruction for Small Constants](#method-1-mov-instruction-for-small-constants)
- [Method 2: MVN Instruction for Bitwise Complement](#method-2-mvn-instruction-for-bitwise-complement)
- [Method 3: LDR with Literal Pool](#method-3-ldr-with-literal-pool)
- [Method 4: ADR and ADRL Pseudo-Instructions](#method-4-adr-and-adrl-pseudo-instructions)
- [Method 5: MOVW and MOVT Combination](#method-5-movw-and-movt-combination)
- [Method 6: Multiple Instruction Sequences](#method-6-multiple-instruction-sequences)
- [Worked Examples](#worked-examples)
  - [Example 1: Loading Small Constants](#example-1-loading-small-constants)
  - [Example 2: Loading 0x12345678](#example-2-loading-0x12345678)
  - [Example 3: Loading -50](#example-3-loading--50)
  - [Example 4: Analyzing Constant Encodability](#example-4-analyzing-constant-encodability)
- [Summary](#summary)
- [Key Formulas](#key-formulas)

## Introduction

Loading constants into registers constitutes a fundamental operation in ARM assembly programming for embedded systems. ARM Cortex-M microcontrollers, widely deployed in modern embedded applications, require efficient constant loading mechanisms for arithmetic operations, logical manipulations, and memory address calculations. The ARM instruction set architecture presents unique challenges in this domain due to the limited encoding space available for immediate values within 32-bit instructions.

This module examines the various techniques available in the ARM Thumb-2 instruction set for loading constants, encompassing MOV, MVN, LDR with literal pools, ADR/ADRL pseudo-instructions, and MOVW/MOVT combinations. A rigorous theoretical treatment of immediate value encoding, including formal proofs of representable ranges, prepares students for examination questions requiring analysis of specific constant values.

## Theoretical Foundation: ARM Immediate Value Encoding

### Encoding Mechanism

ARM instructions utilize a 32-bit encoding scheme. Certain data processing instructions, specifically MOV and MVN, accommodate immediate constants directly within their encoding. However, the architecture imposes significant constraints on which values can be represented.

The ARM immediate value encoding follows a well-defined mathematical pattern:

- **12-bit immediate field**: Comprised of an 8-bit value rotated right by a 4-bit rotation count
- **Rotation range**: 0-15 positions, applied as even multiples (rotation count × 2)
- **Effective range**: Any 32-bit value expressible as: `rotated_imm = imm8 ROR (2 × rot)`

**Theorem**: A 32-bit constant C can be encoded as a ARM immediate if and only if C can be expressed as an 8-bit value rotated by an even number of bit positions.

_Proof_: The 12-bit immediate field contains an 8-bit value (imm8) in bits [7:0] and a 4-bit rotation value (rot) in bits [11:8]. The effective immediate is computed as: `imm8 ROR (2 × rot)`. Since rot ranges from 0 to 15, the rotation can only be even positions (0, 2, 4, ..., 30). Therefore, only values satisfying this constraint are directly encodable. ∎

**Corollary**: The total number of representable immediate values is 2^12 = 4096, though this includes multiple encodings for some values.

### Examples of Encodable vs Non-Encodable Values

Consider the constant 256 (0x100):

- Binary: 0b0000000100000000
- Attempting to represent as 8-bit rotated: No 8-bit value rotated by even positions produces 256
- Therefore: `MOV R0, #256` is invalid

Consider the constant 0xFF (255):

- 8-bit value: 0xFF
- Rotation: 0 (no rotation required)
- Therefore: `MOV R0, #0xFF` is valid

Consider 0x1FE (510):

- 8-bit value: 0xFF (255)
- Rotation: ROR #1 (rotate right by 2 positions)
- Result: 0xFF ROR 2 = 0x3F << 30 + 0xFF >> 2 = 0x3FFFFFFC ≠ 0x1FE
- Therefore: Requires alternative loading method

## Method 1: MOV Instruction for Small Constants

The MOV instruction transfers immediate values into destination registers. The Thumb-2 variant provides enhanced capabilities over the original Thumb instruction set.

**Syntax**: `MOV{S} Rd, #imm` where S suffix updates flags

**Encoding Constraints**:

- imm8: 8-bit immediate (0-255)
- rot: 4-bit rotation (0-15), resulting in rotation of 2×rot positions

**Examples with Analysis**:

```assembly
MOVS R0, #0 ; Load 0 (Z flag set)
MOVS R1, #100 ; Load 100 (0x64, fits in imm8)
MOVS R2, #0xFF ; Load 255 (0xFF, maximum imm8 without rotation)
MOVS R3, #0x12, LSL #16 ; Load 0x00120000: imm8=0x12, LSL by 16
```

**Theorem**: The instruction `MOVS R0, #imm, LSL #shift` effectively computes `imm × 2^shift`.

_Proof_: The barrel shifter operates on the 8-bit immediate before placement into the register. For shift = n, the result equals imm << n, which equals imm × 2^n. ∎

## Method 2: MVN Instruction for Bitwise Complement

The MVN (Move Not) instruction loads the bitwise complement of an immediate constant, enabling efficient representation of certain negative numbers and bit patterns.

**Syntax**: `MVNS Rd, #imm`

**Mathematical Relationship**:

- `MVN Rd, #val` = `MOV Rd, #(~val)`
- Where ~ denotes bitwise NOT (ones complement)

**Examples**:

```assembly
MVNS R0, #0 ; Load ~0 = 0xFFFFFFFF (equivalent to -1)
MVNS R1, #0xF ; Load ~0xF = 0xFFFFFFF0
MVNS R2, #0x00 ; Load ~0 = 0xFFFFFFFF
```

**Application**: To load -1 using MVN:

- `MVN R0, #0` produces 0xFFFFFFFF (which equals -1 in two's complement)
- For arbitrary negative values, use: `MVN Rd, #(N-1)` loads -(N) when N > 0

## Method 3: LDR with Literal Pool

For constants exceeding the immediate encoding capacity, the LDR pseudo-instruction with literal pool provides the standard solution.

**Syntax**: `LDR Rt, =const`

This pseudo-instruction undergoes assembler transformation:

1. If const fits immediate encoding → generates MOV/MVN
2. If const exceeds encoding → generates PC-relative LDR to literal pool

**Literal Pool Mechanism**:

```assembly
 LDR R0, =0x12345678 ; Large constant (cannot be immediate)
 LDR R1, =my_constant ; Load address of my_constant
 ; ... code execution ...
 ; Literal pool placement
 LTORG ; Force literal pool here
my_constant DCD 0x1000 ; Define 32-bit constant
```

**Theorem**: The PC-relative offset from LDR instruction to literal pool entry must be within ±4095 bytes.

_Proof_: The LDR encoding uses 12-bit signed offset. With word-aligned constants (4-byte boundary), maximum offset spans (2^12 - 1) × 4 = 16380 bytes in each direction. ∎

## Method 4: ADR and ADRL Pseudo-Instructions

ADR loads PC-relative addresses, while ADRL provides longer-range addressing.

**ADR Syntax**: `ADR Rd, label`

```assembly
ADR R0, data_section ; Load address of data_section
ADR R1, my_array+8 ; Load address of my_array + 8 bytes
```

**Translation**:

- Forward label: `ADD Rd, PC, #offset`
- Backward label: `SUB Rd, PC, #offset`

**ADRL Syntax**: `ADRL Rd, label` (for larger address ranges)

```assembly
ADRL R0, large_data ; Works for ±64KB (2 instructions generated)
```

## Method 5: MOVW and MOVT Combination

Thumb-2 provides 16-bit immediate load instructions enabling 32-bit constant construction.

**MOVW**: Loads lower 16 bits (clears upper 16 to zero)
**MOVT**: Loads upper 16 bits (preserves lower 16)

**Example**: Loading 0x12345678

```assembly
MOVW R0, #0x5678 ; R0 = 0x00005678
MOVT R0, #0x1234 ; R0 = 0x12345678
```

**Theorem**: Any 32-bit value can be uniquely loaded using MOVW/MOVT combination.

_Proof_: Split 32-bit value V into V[31:16] (upper 16 bits) and V[15:0] (lower 16 bits). MOVW accepts any 16-bit value; MOVT accepts any 16-bit value. Loading V[15:0] via MOVW then V[31:16] via MOVT reconstructs V exactly. ∎

## Method 6: Multiple Instruction Sequences

For optimization-sensitive code, combining multiple instructions may prove faster than literal pool access.

```assembly
; Load 0x00081234
MOVW R0, #0x1234 ; Lower 16 bits
MOVT R0, #0x0008 ; Upper 16 bits
; Equivalent to:
LDR R0, =0x1234 ; Uses literal pool (1 instruction + memory access)
```

## Worked Examples

### Example 1: Loading Small Constants

**Problem**: Initialize R0-R3 with values 10, 20, 30, and 40 respectively.

**Solution**:

```assembly
MOVS R0, #10 ; 10 fits in imm8 (10 < 256)
MOVS R1, #20 ; 20 fits in imm8
MOVS R2, #30 ; 30 fits in imm8
MOVS R3, #40 ; 40 fits in imm8
```

### Example 2: Loading 0x12345678

**Problem**: Load the 32-bit constant 0x12345678 into R0.

**Analysis**: 0x12345678 exceeds immediate encoding. Verify: cannot be expressed as 8-bit rotated value.

**Solution**:

```assembly
; Method 1: MOVW/MOVT (2 instructions, no literal pool)
MOVW R0, #0x5678
MOVT R0, #0x1234

; Method 2: LDR pseudo-instruction (assembler handles)
LDR R0, =0x12345678 ; Generates PC-relative LDR
```

### Example 3: Loading -50

**Problem**: Load -50 (0xFFFFFFCE) into R0.

**Analysis**:

- Option 1: MVN with complement: MVN R0, #49 (since ~49 = 0xFFFFFFCE - 1 = 0xFFFFFFCE)
- Wait: ~49 = 0xFFFFFFCE? No, ~49 = 0xFFFFFFCE ✓

Actually: 49 = 0x31, ~0x31 = 0xFFFFFFCE ✓

**Solution**:

```assembly
MVNS R0, #49 ; Load bitwise NOT of 49 = -50
; Or equivalently:
LDR R0, =-50 ; Pseudo-instruction generates MVN
```

### Example 4: Analyzing Constant Encodability

**Problem**: Determine whether 0x102 can be loaded using single MOV instruction.

**Analysis**:

- 0x102 = 258 decimal
- Represent as 8-bit rotated?
- 0x102 = 0x04 << 8 = 0x0400, no 8-bit value works
- Try: 0x102 = 0x81 ROR 2? 0x81 ROR 2 = 0x206 ≠ 0x102
- Try: 0x102 = 0x40 ROR 1? 0x40 ROR 1 = 0x20 ≠ 0x102

**Conclusion**: 0x102 cannot be loaded directly via MOV; requires literal pool or MOVW/MOVT.

## Summary

ARM provides multiple mechanisms for loading constants, each with distinct encoding constraints. The 12-bit immediate encoding (8-bit value rotated by even positions) limits direct immediate loading to approximately 4096 distinct values. For larger constants, programmers utilize LDR with literal pools, MOVW/MOVT combinations, or multiple instruction sequences. Understanding these mechanisms enables optimal constant loading in embedded applications.

## Key Formulas

| Technique      | Maximum Range          | Instruction Count |
| -------------- | ---------------------- | ----------------- |
| MOV imm8       | 0-255 (unrotated)      | 1                 |
| MOV with shift | Up to 12-bit effective | 1                 |
| MVN            | ~0 to ~255             | 1                 |
| MOVW/MOVT      | Any 32-bit             | 2                 |
| LDR =const     | Any 32-bit             | 1 + memory access |
| ADR            | ±4095 bytes            | 1                 |
