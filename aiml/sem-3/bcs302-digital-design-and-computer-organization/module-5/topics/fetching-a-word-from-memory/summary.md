# Fetching A Word From Memory
### Quick Summary: Fetching a Word from Memory

- **MAR (Memory Address Register):** Holds the address of the memory location to be accessed (n-bit MAR addresses 2^n locations)
- **MDR (Memory Data Register):** Temporarily holds data being transferred between CPU and memory
- **Process:** Address placed on address bus → MemRead asserted → Memory places data on data bus → Data captured in MDR → Data transferred to destination register
- **RTL Notation:** MAR ← [Source]; MDR ← Memory[MAR]; Register ← [MDR]
- **Instruction Fetch:** PC provides address; instruction goes to IR; PC increments
- **Data Fetch:** Address from general-purpose register; data goes to specified CPU register
- **Timing:** Memory access time determines wait states; CPU-memory speed gap bridged by caches