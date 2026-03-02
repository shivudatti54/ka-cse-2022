# Registers and Memory (RAM & ROM)

## Introduction

In computer system architecture, **registers** and **memory (RAM/ROM)** form the fundamental storage components of a computer system. Registers provide the fastest accessible storage within the CPU, while RAM and ROM constitute the main memory hierarchy. Understanding these components is essential for comprehending how data flows and is stored during program execution—directly aligned with the Delhi University BSc (Hons) CS syllabus under Computer Organization and Architecture.

---

## Key Concepts

### **Registers**
- **Definition**: Small, high-speed storage locations within the CPU used to hold temporary data, instructions, and control information during processing.
- **Types of Registers**:
  - **General-Purpose Registers (GPR)**: Store operands and intermediate results (e.g., AX, BX, CX, DX in x86).
  - **Special-Purpose Registers**: Include Program Counter (PC), Instruction Register (IR), Memory Address Register (MAR), Memory Data Register (MDR), Accumulator (AC), and Status Register/Flags.
- **Register Organization**: Involves register file design, addressing modes, and word length considerations.

### **Random Access Memory (RAM)**
- **Definition**: Volatile, read-write memory that stores data and instructions currently in use.
- **Characteristics**:
  - Volatile (data lost when power is off)
  - Random access (any location accessed directly)
  - Faster than secondary storage but slower than registers
- **Types**:
  - **SRAM** (Static RAM): Uses flip-flops, faster, expensive, used for cache.
  - **DRAM** (Dynamic RAM): Uses capacitors, requires refresh, higher density, used for main memory.

### **Read-Only Memory (ROM)**
- **Definition**: Non-volatile memory that stores firmware and permanent data.
- **Characteristics**:
  - Non-volatile (data retained without power)
  - Primarily read-only (with exceptions in modern types)
  - Slower than RAM but faster than secondary storage
- **Types**:
  - **PROM**: Programmable once.
  - **EPROM**: Erasable and programmable (UV light).
  - **EEPROM**: Electrically erasable and programmable.
  - **Flash Memory**: Widely used in USB drives and SSDs.

### **Memory Hierarchy & Comparison**
| Feature | Registers | RAM | ROM |
|---------|-----------|-----|-----|
| Speed | Fastest | Fast | Slow |
| Location | Inside CPU | Main memory | Motherboard/BIOS |
| Volatility | Volatile | Volatile | Non-volatile |
| Access | Read/Write | Read/Write | Primarily Read |

---

## Conclusion

Registers, RAM, and ROM each serve distinct roles in computer architecture—registers enable immediate CPU operations, RAM provides working memory for active programs, and ROM stores essential permanent instructions. Mastery of these concepts is crucial for understanding data flow, memory management, and system performance—key topics in Delhi University's Computer System Architecture examinations.