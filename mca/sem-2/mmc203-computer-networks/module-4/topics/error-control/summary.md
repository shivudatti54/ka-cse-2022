# Error Control in Data Communication - Summary

## Key Definitions and Concepts

- **Error Control**: Set of techniques to detect and correct errors in transmitted data
- **Single-Bit Error**: Only one bit changes state during transmission
- **Burst Error**: Multiple consecutive bits are corrupted
- **Redundancy**: Extra bits added to data for error detection/correction
- **ARQ (Automatic Repeat reQuest)**: Protocol where receiver requests retransmission on error

## Important Formulas and Theorems

- **Hamming Code**: 2^r ≥ m + r + 1 (where m = data bits, r = parity bits)
- **Minimum Hamming Distance**: For error detection: d_min ≥ e+1; for error correction: d_min ≥ 2e+1
- **CRC**: Transmitted bits = data bits + r (remainder), where r = degree of generator polynomial
- **Stop-and-Wait ARQ Efficiency**: η = 1/(1+2a), where a = Tp/Tt

## Key Points

- Error detection finds corrupted data; error correction reconstructs original data
- Parity check is simplest but only detects odd-numbered bit errors
- CRC is the most powerful error detection method, widely used in networks
- Hamming code can correct single-bit errors using redundant parity bits
- Parity bits in Hamming code are placed at positions 1, 2, 4, 8, 16...
- Stop-and-Wait is simple but inefficient for high-latency channels
- Go-Back-N retransmits all frames after the error; Selective Repeat only retransmits erroneous frames
- CRC with generator polynomial can detect all burst errors of length ≤ r+1

## Common Mistakes to Avoid

1. Confusing the number of parity bits with their positions in Hamming code
2. Forgetting to append zeros equal to generator degree before CRC division
3. Using wrong parity type (even vs odd) when calculating or checking
4. Not considering that ARQ protocols require bidirectional communication for acknowledgments

## Revision Tips

1. Practice CRC division problems multiple times to become proficient
2. Remember the pattern of which bits each parity bit checks in Hamming code
3. Draw timeline diagrams for ARQ protocols to understand their operation
4. Memorize the Hamming code formula as it's frequently asked in exams
5. Focus on understanding when to use detection vs correction based on application requirements
