# Basic Concepts of Computer Organization and Architecture

## Introduction

Computer Organization and Architecture forms the backbone of modern computing systems, providing the essential framework for understanding how computers process information at the most fundamental level. This topic introduces the basic concepts that govern the design, organization, and functioning of computer systems. For students pursuing Computer Science at the University of Delhi, mastering these concepts is crucial as they form the foundation for understanding more advanced topics such as pipeline design, memory hierarchy, and performance optimization.

The distinction between computer organization and computer architecture is fundamental to this study. Computer architecture refers to the attributes visible to the programmer, including the instruction set, instruction formats, addressing modes, and data types. Computer organization, on the other hand, describes how these architectural features are implemented in hardware—encompassing the control signals, interfaces, and physical components that bring the architectural specifications to life. Understanding this distinction helps students appreciate why different computers can execute the same program while having vastly different internal structures.

## Key Concepts

### Basic Structure of a Computer System

A computer system consists of three major components: the Central Processing Unit (CPU), the memory unit, and the input/output (I/O) subsystem. The CPU serves as the brain of the computer, executing instructions and controlling the operation of all other components. The memory unit stores both data and instructions, while the I/O subsystem facilitates communication between the computer and the external world.

The CPU itself comprises three essential parts: the Control Unit (CU), the Arithmetic Logic Unit (ALU), and the Registers. The Control Unit directs the flow of data between these components and manages the execution of instructions. The ALU performs arithmetic operations (addition, subtraction, multiplication, division) and logical operations (AND, OR, NOT, comparisons). Registers are high-speed storage locations within the CPU that hold temporary data and control information during instruction execution.

### The Stored Program Concept

The stored program concept, pioneered by John von Neumann, represents one of the most important ideas in computer architecture. In this model, both instructions and data are stored in the same memory unit. This allows the computer to modify its own instructions, enabling powerful capabilities such as interpreters, compilers, and self-modifying code. The von Neumann architecture defines a computer as having a single memory space for both instructions and data, with the CPU fetching instructions from memory, decoding them, and executing them sequentially.

The implications of the stored program concept are profound. Programs can be treated as data—loaded, stored, and manipulated like any other information. This fundamental principle underlies all modern computing and enables the development of sophisticated software systems. However, it also introduces the famous von Neumann bottleneck, where the speed of data transfer between the CPU and memory limits overall system performance.

### Instruction Cycle

The instruction cycle represents the fundamental sequence of operations that the CPU performs to execute each machine instruction. This cycle consists of four main phases: fetch, decode, execute, and store. During the fetch phase, the CPU obtains the instruction from memory, using the program counter (PC) register to determine the memory address. The instruction is then stored in the instruction register (IR) for processing.

The decode phase involves interpreting the fetched instruction to determine what operation must be performed and which operands are required. The CPU identifies the operation code (opcode) and addressing modes, setting up the appropriate control signals for execution. During the execute phase, the actual operation is performed—either by the ALU for arithmetic and logical operations or by other hardware components for data transfers and control operations. Finally, in the store phase, results are written back to memory or registers as required by the instruction.

### Addressing Modes

Addressing modes define how the CPU locates the operands required for an instruction. Different addressing modes provide flexibility and efficiency in accessing data. The most common addressing modes include immediate addressing (where the operand value is included directly in the instruction), direct addressing (where the instruction contains the memory address of the operand), and indirect addressing (where the instruction contains a pointer to the memory location holding the operand address).

Register addressing provides the fastest operand access since registers are located within the CPU. Indexed addressing uses a base register plus an offset to compute the effective address, which is particularly useful for accessing array elements. Understanding these addressing modes is essential for writing efficient assembly language programs and for comprehending how high-level language constructs are translated into machine instructions.

### Data Representation

Computers represent all data using binary digits (bits), organized into larger units such as bytes (8 bits), words (typically 16, 32, or 64 bits), and double words. Integer numbers are represented using various schemes, including sign-magnitude representation (where the sign bit indicates positive or negative) and two's complement representation (the most common method for representing signed integers). Two's complement is preferred because it simplifies hardware implementation of arithmetic operations—addition and subtraction can be performed using the same circuitry regardless of whether the numbers are signed or unsigned.

Floating-point representation follows the IEEE 754 standard, which defines formats for single-precision (32-bit) and double-precision (64-bit) floating-point numbers. Each floating-point number consists of a sign bit, an exponent field, and a mantissa (fraction) field. Understanding floating-point representation is critical for numerical computing applications, as precision limitations can lead to subtle numerical errors.

### The System Bus

The system bus provides the communication pathway connecting the CPU, memory, and I/O devices. It consists of three separate buses: the address bus (which carries memory addresses), the data bus (which carries actual data), and the control bus (which carries timing and control signals). The width of the data bus (measured in bits) directly affects the amount of data that can be transferred in a single operation, while the width of the address bus determines the maximum memory capacity that the CPU can address.

Bus arbitration is a critical concern in multi-processor systems, where multiple devices may need to use the bus simultaneously. Various arbitration schemes, including daisy-chain arbitration and centralized parallel arbitration, ensure that only one device controls the bus at any given time, preventing data corruption and ensuring orderly communication.

## Examples

### Example 1: Tracing an Instruction Execution

Consider a simple assembly instruction: ADD R1, R2, R3 (which adds contents of R2 and R3, storing result in R1). Let us trace through the instruction cycle:

**Fetch Phase:**
- CPU reads the instruction from memory address stored in Program Counter (PC)
- PC value is placed on address bus, memory reads the instruction
- Instruction is placed in Instruction Register (IR)
- PC is incremented to point to the next instruction

**Decode Phase:**
- Control Unit decodes the opcode (ADD) to determine operation
- Identifies that three registers are involved as operands
- Sets up internal paths for register-to-register data transfer

**Execute Phase:**
- Contents of R2 and R3 are read from the register file
- ALU receives both values and performs addition
- The sum is computed and available at ALU output

**Store Phase:**
- Result from ALU output is written back to R1
- Update status flags (zero, carry, overflow) as needed

This complete sequence occurs within a single clock cycle or multiple cycles depending on the CPU architecture.

### Example 2: Converting Negative Numbers to Two's Complement

Convert -25 to an 8-bit two's complement representation:

Step 1: Write the positive binary representation of 25
25 = 00011001 (8 bits)

Step 2: Invert all bits (find one's complement)
00011001 → 11100110

Step 3: Add 1 to obtain two's complement
11100110 + 1 = 11100111

Therefore, -25 in 8-bit two's complement is 11100111.

To verify: 11100111 (two's complement) = -128 + 64 + 32 + 4 + 2 + 1 = -25.

This representation allows the CPU to perform subtraction using the same addition circuitry, simply by converting the subtrahend to two's complement form.

### Example 3: Calculating Effective Address

Given the instruction: LOAD R1, 100(R2)

This instruction uses indexed addressing mode, where the effective address is calculated by adding the constant offset (100) to the contents of index register R2.

If R2 contains the value 500, then:
Effective Address = Contents of R2 + Offset
= 500 + 100
= 600

The CPU will fetch the value stored at memory address 600 and load it into register R1. This addressing mode is particularly useful for accessing elements of arrays, where R2 could be incremented to access successive array elements.

## Exam Tips

1. Understand the difference between computer organization and computer architecture—this is a frequently tested concept in DU examinations.

2. Memorize the four phases of the instruction cycle (fetch, decode, execute, store) and what happens in each phase.

3. Be able to explain the von Neumann architecture and its limitations, particularly the von Neumann bottleneck.

4. Practice two's complement conversion—both positive to negative and vice versa, as this is a common examination question.

5. Know the different addressing modes with examples: immediate, direct, indirect, register, and indexed addressing.

6. Understand how the system bus works and the functions of address, data, and control buses.

7. Remember that registers are the fastest form of memory in a computer system, faster than cache and main memory.

8. Be prepared to draw and explain the basic structure of a computer system, including CPU, memory, and I/O connections.