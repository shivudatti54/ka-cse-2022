# Memory Register I/O Instructions

## Introduction

Memory Register I/O Instructions are fundamental to computer system architecture, facilitating communication between the CPU and peripheral devices. Under the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science, this topic covers the methods by which the processor performs input/output operations. Understanding these instructions is essential for comprehending how hardware components interact at the architectural level.

## Key Concepts

### 1. I/O Addressing Modes

- **Memory-Mapped I/O (MMIO)**: Peripheral devices are assigned memory addresses; the same instructions used for memory access handle I/O operations
- **Register-Mapped I/O (Isolated I/O)**: Separate I/O address space using dedicated IN and OUT instructions; devices have unique port addresses

### 2. Types of I/O Instructions

- **Input Instructions**: Transfer data from peripheral devices to CPU registers (e.g., IN AX, 60H)
- **Output Instructions**: Transfer data from CPU registers to peripheral devices (e.g., OUT 60H, AX)
- **Block Transfer Instructions**: Handle multiple data bytes (e.g., REP INSB, REP OUTSW)

### 3. Register Organization

- **Data Register**: Temporarily holds data being transferred
- **Status Register**: Contains flags indicating device readiness (busy, error, done)
- **Control Register**: Stores command bits for device control (start, stop, mode selection)

### 4. Communication Process

- CPU reads status register to check device readiness
- For input: CPU executes IN instruction → data placed in accumulator
- For output: CPU executes OUT instruction → data sent to device
- Interrupt-driven I/O allows asynchronous data transfer

### 5. Comparison: Memory-Mapped vs Register-Mapped

| Feature | Memory-Mapped I/O | Register-Mapped I/O |
|---------|------------------|---------------------|
| Address Space | Uses same as memory | Separate I/O space |
| Instructions | Standard memory instructions | Dedicated IN/OUT instructions |
| Speed | Slower (memory access) | Faster (direct) |
| Flexibility | More flexible | Limited |

### 6. Advantages & Disadvantages

**Memory-Mapped I/O**:
- ✓ Uses familiar memory instructions
- ✗ Consumes memory address space

**Register-Mapped I/O**:
- ✓ Simple, fast dedicated operations
- ✗ Requires separate address lines

## Conclusion

Memory Register I/O Instructions form the bridge between the CPU and external devices. Both memory-mapped and register-mapped approaches have their place in modern architecture, with selection based on speed requirements, available address space, and system complexity. Mastery of these concepts is crucial for understanding peripheral interfacing in computer systems.

*For exam preparation: Focus on differences between I/O methods, instruction formats, and the role of status/control registers in data transfer.*