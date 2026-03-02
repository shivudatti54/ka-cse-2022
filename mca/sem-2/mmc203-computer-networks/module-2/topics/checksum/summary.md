# Checksum - Summary

## Key Definitions and Concepts

- **Checksum**: A mathematical value computed from a block of data to detect transmission errors. It serves as a fingerprint of the data.
- **One's Complement**: A binary number representation where negative numbers are formed by inverting all bits of the positive number.
- **End-around Carry**: In one's complement addition, when a carry bit is generated beyond the most significant bit, it must be added back to the result.
- **Error Detection**: The process of identifying whether data has been corrupted during transmission.

## Important Formulas and Theorems

- **Checksum Calculation**: Data is divided into 16-bit segments, all segments are added using one's complement arithmetic, and the one's complement of the sum is the checksum.
- **Verification Condition**: At receiver: Data Sum + Checksum = All 1s (in one's complement representation)
- **Error Detection Capability**: Can detect all odd number of bit errors and most burst errors up to a certain length.

## Key Points

- Checksum is widely used in network protocols (IP, UDP, TCP) for header and data validation
- The standard internet checksum uses 16-bit words and one's complement arithmetic
- End-around carry must be added back to the sum during calculation
- Receiver verification: if sum of all segments plus checksum equals all 1s, no error is detected
- Checksum is simpler than CRC but less powerful for burst error detection
- It provides redundancy against errors but cannot correct them
- The algorithm processes data in fixed-size segments (typically 16 bits)
- One's complement of the sum produces the final checksum value

## Common Mistakes to Avoid

- Forgetting to handle end-around carry during one's complement addition
- Confusing one's complement with two's complement
- Not padding the last segment with zeros if it's less than 16 bits
- Thinking checksum can correct errors (it can only detect them)
- Using regular binary addition instead of one's complement arithmetic

## Revision Tips

- Practice at least 5 checksum calculation problems before the exam
- Remember the verification rule: sum of all data plus checksum should give all 1s
- Know the difference between checksum, parity check, and CRC
- Understand why end-around carry is necessary in one's complement arithmetic
- Review the role of checksum in major network protocols
