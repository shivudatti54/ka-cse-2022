# Data Link Layer Protocols - Summary

## Key Definitions and Concepts

- **Framing:** The process of encapsulating Network layer packets into Data Link Layer frames with delimiters, addresses, and control information
- **Bit Stuffing:** Inserting a '0' after every five consecutive '1's in bit-oriented protocols to distinguish data from flags
- **Flow Control:** Mechanisms (Stop-and-Wait, Sliding Window) to prevent the sender from overwhelming the receiver
- **Error Detection:** Techniques (Parity, CRC, Checksum) to identify transmission errors
- **Error Correction:** Methods like Hamming Code that can identify and correct bit errors

## Important Formulas and Theorems

- **Stop-and-Wait Efficiency:** η = 1 / (1 + 2a), where a = Tp/Tt (propagation time / transmission time)
- **Hamming Code Parity Bits:** 2^r ≥ m + r + 1, where m = data bits, r = parity bits
- **CRC Generator:** Uses polynomial division; detects all burst errors up to the polynomial degree

## Key Points

- Data Link Layer provides node-to-node reliable delivery, framing, and error handling
- HDLC is a bit-oriented synchronous protocol with I, S, and U frame types
- PPP is byte-oriented and commonly used for dial-up connections with LCP and NCP
- Sliding Window protocols (Go-Back-N, Selective Repeat) achieve much higher efficiency than Stop-and-Wait
- CRC provides robust error detection and is used in Ethernet, HDLC, and many other protocols
- Hamming codes can correct single-bit errors by placing parity bits at positions 1, 2, 4, 8, 16...

## Common Mistakes to Avoid

- Confusing bit stuffing with character stuffing; remember bit stuffing adds zeros after five 1s
- Forgetting that Hamming code positions start from 1, not 0
- Not considering the return ACK time when calculating Stop-and-Wait efficiency (the 2Tp factor)
- Mixing up parity bit calculation positions in Hamming code; each parity bit checks specific bit positions

## Revision Tips

- Practice bit stuffing examples until you can do them quickly—these are frequently asked in exams
- Memorize the Hamming code parity position formula and the efficiency formula
- Understand the frame structure of HDLC thoroughly; know the flag, address, control, and FCS fields
- Focus on differences between protocols (HDLC vs PPP, Stop-and-Wait vs Sliding Window)
- Solve numerical problems from previous years' question papers to familiarize with exam patterns
