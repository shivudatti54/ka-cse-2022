# Registers, Memory, RAM and ROM - Summary

## Key Definitions and Concepts

- **Registers:** Fastest memory units inside CPU, used for holding data, addresses, and control information during execution. Size matches processor word size.
- **RAM (Random Access Memory):** Volatile, read-write memory that loses data without power. Provides main working storage for programs.
- **ROM (Read-Only Memory):** Non-volatile memory retaining data without power. Used for firmware and boot programs.
- **SRAM (Static RAM):** Uses flip-flop circuits, no refresh needed, faster but expensive, used for cache memory.
- **DRAM (Dynamic RAM):** Uses capacitors, requires periodic refresh, cheaper, used for main memory.

## Important Formulas and Theorems

- Maximum addressable memory = 2^(number of address lines) × (data bus width in bytes)
- SRAM cell: 6 transistors per bit
- DRAM cell: 1 transistor + 1 capacitor per bit
- Memory locations with n address lines: 2^n

## Key Points

1. Registers are the fastest but smallest storage, located within the CPU
2. MAR holds memory addresses, MDR holds data being transferred
3. PC contains address of next instruction, IR holds current instruction
4. SRAM offers 1-10 ns access time; DRAM offers 50-100 ns access time
5. DRAM requires refresh every few milliseconds; SRAM does not
6. ROM progressed from Mask ROM → PROM → EPROM → EEPROM → Flash
7. EPROM erased by UV light; EEPROM erased electrically
8. Flash memory (NOR/NAND) is block-erasable, used in USB drives and SSDs
9. Memory hierarchy balances speed, cost, and capacity
10. L1/L2/L3 caches use SRAM; main memory uses DRAM

## Common Mistakes to Avoid

- Confusing SRAM with DRAM - remember SRAM is static (no refresh), DRAM is dynamic (needs refresh)
- Thinking ROM cannot be modified - modern ROM types (EEPROM, Flash) allow rewriting
- Forgetting that RAM is volatile while ROM is non-volatile
- Mixing up address bus and data bus functions in memory calculations

## Revision Tips

1. Create a comparison table of all memory types with characteristics
2. Practice memory capacity calculation problems with different bus configurations
3. Memorize the register purposes using the fetch-decode-execute cycle
4. Understand the memory hierarchy diagram and why each level exists
5. Focus on differences between SRAM/DRAM and EEPROM/Flash for exams