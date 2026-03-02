# Addressing Modes

## Introduction

In computer architecture, addressing modes refer to the ways in which a computer can access and manipulate data in its memory. An addressing mode is a way of specifying the location of an operand, which is the data being operated on by an instruction. The choice of addressing mode affects the performance, efficiency, and complexity of a computer program.

Addressing modes are a fundamental concept in computer architecture because they determine how a computer can access and manipulate data. Different addressing modes provide varying levels of flexibility, efficiency, and complexity, making them suitable for different applications and programming styles.

In this topic, we will explore the different types of addressing modes, their characteristics, and examples of how they are used in computer programs.

## Key Concepts

### 1. Immediate Addressing Mode

In immediate addressing mode, the operand is specified directly in the instruction. The operand is a constant value that is embedded in the instruction itself.

Example: `MOV AX, 10` - moves the value 10 into the AX register.

### 2. Direct Addressing Mode

In direct addressing mode, the operand is specified by its memory address. The instruction contains the memory address of the operand.

Example: `MOV AX, [1000]` - moves the value stored at memory address 1000 into the AX register.

### 3. Indirect Addressing Mode

In indirect addressing mode, the operand is specified by a pointer to its memory address. The instruction contains the memory address of a pointer, which in turn points to the operand.

Example: `MOV AX, [BX]` - moves the value stored at the memory address pointed to by the BX register into the AX register.

### 4. Indexed Addressing Mode

In indexed addressing mode, the operand is specified by a base address and an index. The instruction contains a base address and an index, which is used to calculate the final memory address of the operand.

Example: `MOV AX, [BX + 10]` - moves the value stored at the memory address pointed to by the BX register plus 10 into the AX register.

### 5. Relative Addressing Mode

In relative addressing mode, the operand is specified by a relative offset from the current instruction. The instruction contains a relative offset, which is used to calculate the final memory address of the operand.

Example: `JMP +10` - jumps to the instruction 10 bytes ahead of the current instruction.

## Examples

### Example 1: Immediate Addressing Mode

Suppose we want to move the value 10 into the AX register using immediate addressing mode.

```assembly
MOV AX, 10
```

In this example, the operand 10 is specified directly in the instruction.

### Example 2: Direct Addressing Mode

Suppose we want to move the value stored at memory address 1000 into the AX register using direct addressing mode.

```assembly
MOV AX, [1000]
```

In this example, the operand is specified by its memory address.

### Example 3: Indirect Addressing Mode

Suppose we want to move the value stored at the memory address pointed to by the BX register into the AX register using indirect addressing mode.

```assembly
MOV AX, [BX]
```

In this example, the operand is specified by a pointer to its memory address.

## Exam Tips

1. Be able to identify and explain the different types of addressing modes.
2. Understand how to specify operands using each addressing mode.
3. Be able to write assembly code examples using each addressing mode.
4. Understand the advantages and disadvantages of each addressing mode.
5. Be able to analyze the performance and efficiency of different addressing modes.
6. Understand how addressing modes affect the complexity of a computer program.
7. Be able to identify and explain the use of addressing modes in different applications and programming styles.