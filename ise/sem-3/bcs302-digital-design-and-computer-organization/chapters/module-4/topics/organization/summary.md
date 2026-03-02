# Memory Organization - Summary

## Key Definitions and Concepts

- **Memory Cell:** Basic storage unit that holds one bit of data, typically implemented using a flip-flop or capacitor
- **Word:** The natural unit of data handled by the processor in a single operation; size matches processor data path width
- **Memory Bank:** Independent division of memory that can be accessed separately from other banks
- **Address Decoding:** Process of converting binary addresses into signals that select specific memory cells
- **Memory Interleaving:** Technique distributing consecutive addresses across multiple banks to increase bandwidth

## Important Formulas and Theorems

- Memory Capacity = 2^n × m bits, where n = address lines, m = data lines per location
- For hierarchical decoding: Total address lines = row address lines + column address lines
- Internal array size (rows × columns) = 2^(rows) × 2^(columns)
- Effective bandwidth with interleaving ≈ single bank bandwidth × number of banks (for sequential access)

## Key Points

- Memory organization determines how efficiently the processor can access data
- Byte-addressable systems allow individual byte access; word-addressable systems access whole words
- Hierarchical (row-column) decoding reduces address line requirements compared to linear selection
- Memory interleaving improves performance for sequential access patterns but not for random access
- Big-endian stores most significant byte at lowest address; little-endian stores least significant byte first
- Two-level decoding divides address into row portion (selecting memory array row) and column portion (selecting specific cell)
- Bank selection in interleaved memory typically uses the least significant address bits

## Common Mistakes to Avoid

1. Confusing address lines with data lines when calculating memory capacity
2. Forgetting to convert between bits and bytes in capacity calculations
3. Applying interleaving benefits to random access patterns where they do not apply
4. Incorrectly dividing address bits between row and column in hierarchical decoding
5. Mixing up big-endian and little-endian byte ordering conventions

## Revision Tips

1. Practice memory capacity problems with varying combinations of address and data lines
2. Draw memory maps for different organization schemes to visualize address distribution
3. Trace through memory access sequences with and without interleaving
4. Memorize the key differences between big-endian and little-endian with concrete examples
5. Solve previous year examination questions to understand the problem patterns and marking scheme