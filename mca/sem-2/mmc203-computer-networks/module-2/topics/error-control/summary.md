# Error Control in Data Communication - Summary

## Key Definitions and Concepts

- **Error Control**: Mechanisms to detect and correct errors in transmitted data to ensure reliable communication.
- **Single-bit Error**: Only one bit changes state; easier to detect and correct.
- **Burst Error**: Multiple consecutive bits corrupted; more common in practical systems.
- **Parity Bit**: Redundant bit added to make total number of 1s either even (even parity) or odd (odd parity).
- **Checksum**: Error detection method using arithmetic sum of data words; commonly 16-bit words in Internet protocols.
- **CRC (Cyclic Redundancy Check)**: Powerful error detection based on polynomial division; detects all burst errors up to degree of generator.
- **Hamming Code**: Linear block code that can detect and correct single-bit errors using strategically placed parity bits.

## Important Formulas and Theorems

- **Hamming Code Relation**: 2^r ≥ m + r + 1 (where m = data bits, r = parity bits)
- **Codeword Length**: n = m + r
- **Parity Positions**: 1, 2, 4, 8, 16, ... (powers of 2)
- **CRC Generation**: Append r zeros to data (where r = degree of generator), divide by generator polynomial, append remainder as CRC

## Key Points

- Simple parity can only detect odd-numbered errors (1, 3, 5, etc.)
- Two-dimensional parity can detect and correct single-bit errors
- CRC is more powerful than checksum for burst error detection
- Hamming code requires minimum 3 redundant bits for 1 data bit, 4 for 2 data bits, and so on
- Syndrome = 0 indicates no error in Hamming code; non-zero indicates error position
- Generator polynomial for CRC must have at least two terms with first and last bits as 1
- CRC-32 is widely used in Ethernet, ZIP, PNG; CRC-16 in USB/Bluetooth

## Common Mistakes to Avoid

- Forgetting to append zeros equal to the degree of generator polynomial before CRC division
- Incorrectly calculating parity bit positions in Hamming code (always powers of 2)
- Confusing between error detection (knowing error occurred) and error correction (fixing the error)
- Not considering that CRC remainder length equals (degree of generator - 1) bits
- Mixing up even and odd parity requirements when solving problems

## Revision Tips

- Practice binary division for CRC problems as it frequently appears in exams
- Memorize the Hamming code inequality 2^r ≥ m + r + 1 for quick calculations
- Remember the pattern of bit positions checked by each parity bit in Hamming code
- Understand that syndrome bits from all parity checks, when read in binary, directly give error position
- Focus on understanding polynomial representation for CRC as it helps in solving numerical problems
