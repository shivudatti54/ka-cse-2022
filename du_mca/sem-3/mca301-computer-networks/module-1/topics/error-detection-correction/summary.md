# Error Detection and Correction - Summary

## Key Definitions and Concepts

- **Single-bit Error**: Corruption of one bit during transmission, isolated error caused by random noise
- **Burst Error**: Multiple consecutive bits corrupted, measured from first to last error bit including correct bits between
- **Redundancy Bits**: Extra bits added to data enabling error detection/correction at receiver
- **Code Rate**: Ratio of data bits to total transmitted bits (data + redundancy)
- **Parity Bit**: Single bit indicating odd/even count of 1s in data
- **CRC (Cyclic Redundancy Check)**: Polynomial-based error detection using binary division
- **Checksum**: Error detection using one's complement addition of data segments
- **Hamming Code**: Distance-3 code enabling single-bit error correction
- **Hamming Distance**: Minimum number of bit positions differing between any two valid codewords
- **Syndrome**: Calculated value indicating error location in Hamming code decoding

## Important Formulas and Theorems

- **Two-dimensional Parity**: Detects all odd-numbered errors; detects all single-bit and many multiple-bit errors within a row or column
- **CRC Generator**: Data appended with zeros (degree of polynomial), divided by generator polynomial, remainder is CRC bits
- **Hamming Code Parity Requirement**: 2^r ≥ m + r + 1, where m = data bits, r = parity bits
- **Hamming Distance Properties**: Code with distance d detects up to d-1 errors; corrects up to ⌊(d-1)/2⌋ errors
- **Hamming Code Minimum Distance**: 3 (detects 2 errors or corrects 1 error)

## Key Points

1. Error detection adds redundancy allowing verification; error correction additionally identifies error locations for automatic fixing

2. Parity checking detects only odd-numbered errors and fails completely on even-numbered errors

3. CRC with well-chosen generator polynomials detects all bursts up to the polynomial degree and most longer bursts

4. Internet checksum uses 16-bit segments and one's complement arithmetic in IP, TCP, and UDP protocols

5. Hamming code places parity bits at positions 1,2,4,8... with each parity bit checking specific bit subsets

6. Syndrome bits in Hamming code (when calculated correctly) directly indicate error position as binary value

7. Higher redundancy provides stronger error handling but reduces effective data transmission rate

8. Error detection primarily occurs at Data Link Layer; end-to-end correction at Transport Layer in TCP

9. CRC-32 used in Ethernet, ZIP files; chosen for excellent burst error detection properties

10. Single-bit errors are rare in serial transmission; burst errors are more common in practical channels

## Common Mistakes to Avoid

1. **Confusing parity and checksum**: Parity is single-bit; checksum processes entire data segments
2. **Forgetting CRC polynomial degree**: Must append zeros equal to polynomial degree before division
3. **Incorrect Hamming parity positions**: Parity bits must occupy positions 1,2,4,8... not consecutive positions
4. **Miscalculating Hamming syndrome**: Each parity bit checks different bit subsets—must use binary position checking
5. **Assuming CRC corrects errors**: CRC only detects errors, does not correct (unlike Hamming code)

## Revision Tips

1. Practice CRC binary division with different generator polynomials until comfortable with the algorithm

2. Work through multiple Hamming code examples—encoding and error correction—to build procedural fluency

3. Create a comparison table of all error detection methods covering detection capability, overhead, and applications

4. Memorize the Hamming code parity bit formula 2^r ≥ m + r + 1 and practice deriving minimum parity bits

5. Relate concepts to real protocols: Ethernet uses CRC-32, TCP uses checksum, understand why each choice was made