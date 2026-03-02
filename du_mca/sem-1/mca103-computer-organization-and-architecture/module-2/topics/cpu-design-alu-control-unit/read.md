# CPU Design: ALU and Control Unit

## Introduction
The Arithmetic Logic Unit (ALU) and Control Unit form the core components of a CPU's datapath. In modern computer architecture, these elements work synergistically to execute instructions efficiently. The ALU performs all arithmetic and logical operations, while the Control Unit coordinates data flow and manages instruction execution through precise timing signals.

With the advent of RISC architectures and pipelining techniques, optimized ALU-Control Unit interaction has become critical for achieving high IPC (Instructions Per Cycle). Modern applications like AI acceleration and real-time systems demand specialized ALU configurations with parallel execution capabilities.

This topic is fundamental for understanding processor microarchitecture, performance optimization, and hardware-software co-design. Industry applications range from embedded systems design to high-performance computing clusters.

## Key Concepts

1. **ALU Architecture**
- *Arithmetic Circuits*: Carry-lookahead adders, Booth multipliers
- *Logic Circuits*: Bitwise operators (AND, OR, XOR)
- *Shifters*: Barrel shifters for fast bit manipulation
- *Status Flags*: Zero, Carry, Overflow, Sign flags

2. **Control Unit Types**
- *Hardwired Control*: Finite state machine implementation (e.g., MIPS)
- *Microprogrammed Control*: Horizontal vs vertical microcode (e.g., x86)
- *Nanoprogramming*: Two-level control store organization

3. **Instruction Cycle Coordination**
- Fetch-Decode-Execute cycle synchronization
- Timing signals generation using system clock
- Pipeline stage control in superscalar architectures

4. **Advanced Concepts**
- ALU bypass networks for hazard resolution
- Predicated execution units
- Dynamic microcode patching in modern CPUs

## Examples

**Example 1: ALU Operation with Status Flags**
*Problem*: Perform (-5) + 7 using 4-bit two's complement. Determine status flags.

*Solution*:
1. Convert to binary: -5 = 1011₂, 7 = 0111₂
2. Add: 
   1011
 +0111
 ------
10010 (Discard overflow bit → 0010)
3. Flags:
   - Zero: 0 (result ≠ 0)
   - Carry: 1 (overflow bit exists)
   - Overflow: 1 (sign change: -5 + 7 = +2 → correct)
   - Sign: 0 (positive result)

**Example 2: Control Signal Generation**
*Problem*: Design control signals for MOV R1, [MEM] instruction in a 3-bus architecture.

*Solution*:
1. Fetch: PC → MAR, MEM → MDR → IR
2. Decode: Opcode identifies MOV operation
3. Execute:
   - MAR ← Effective Address
   - MEM → MDR
   - MDR → R1
Control Signals Required:
- MARin, MEMread, MDRoutE, IRin (Fetch)
- ALU_EA (Decode)
- MARin, MEMread, MDRoutD, R1in (Execute)

**Example 3: Microprogrammed Control Design**
*Problem*: Create microcode for ADD instruction in a vertical microcode format.

*Solution*:
| Address | Microinstruction          |
|---------|---------------------------|
| 0x00    | PC→MAR, MEMread, IncrPC   |
| 0x01    | MDR→IR                    |
| 0x02    | Decode Opcode             |
| 0x03    | Rsrc1→A, Rsrc2→B          |
| 0x04    | ALU_ADD, Zin              |
| 0x05    | Z→Rdst                    |

## Exam Tips
1. Always draw timing diagrams for control signal visualization
2. Memorize status flag calculation rules for different operations
3. Differentiate clearly between hardwired and microprogrammed control units
4. Practice designing control sequences for complex instructions (e.g., conditional jumps)
5. Understand pipeline conflicts related to ALU operations (WAW, WAR hazards)
6. Study real-world architectures: MIPS control signals vs ARM barrel shifter integration
7. Remember microinstruction formats: Harvard vs Princeton, horizontal vs vertical coding