# Data Link Layer: Error Detection and Correction - Summary

## Key Definitions and Concepts

- **Data Link Layer**: Layer 2 of the OSI model that provides node-to-node transfer of data, transforming raw bits into reliable frames.

- **Framing**: The process of dividing the data stream into manageable units called frames, each containing header (addresses, control) and trailer (error detection) information.

- **Error Detection**: Adding redundant bits to transmitted data to allow the receiver to identify if errors occurred (parity, CRC, checksum).

- **Error Correction**: Adding sufficient redundancy to not only detect but also locate and correct errors (Hamming code, Reed-Solomon).

- **Single-Bit Error**: Only one bit changes in the data unit; rare in serial transmission.

- **Burst Error**: Multiple consecutive bits are corrupted; more common in real-world scenarios.

- **LLC (Logical Link Control)**: Upper sublayer of DLL handling error control, flow control, and providing service to Network Layer.

- **MAC (Media Access Control)**: Lower sublayer of DLL handling addressing (MAC addresses) and media access protocols.

## Important Formulas and Theorems

- **Hamming Code Formula**: 2^r ≥ m + r + 1
  - Where m = number of data bits, r = number of parity bits
  - Example: For m=4, r=3 satisfies (2^3 = 8 ≥ 8)

- **CRC Detection Capability**: Detects all burst errors of length ≤ degree of generator polynomial; can detect all odd number of bit errors.

- **Parity Detection**: Simple parity can detect only odd number of bit errors.

## Key Points

1. Data Link Layer sits between Physical Layer (Layer 1) and Network Layer (Layer 3) in OSI model.

2. Four main services: Framing, Error Control, Flow Control, Access Control.

3. LLC sublayer (IEEE 802.2) provides error and flow control; MAC sublayer handles addressing and access (Ethernet 802.3, Wi-Fi 802.11).

4. MAC addresses are 48-bit unique identifiers assigned to network interface cards.

5. Error detection methods: Simple parity (1 bit), Two-dimensional parity (detects and locates single-bit errors), CRC (most powerful), Checksum (used in IP/TCP/UDP).

6. Error correction methods: Hamming code (corrects single-bit errors), Forward Error Correction (FEC) for real-time applications.

7. FEC is preferred in high-latency or broadcast scenarios; ARQ (retransmission) is used in reliable lower-latency networks.

8. CRC-32 is used in Ethernet; CRC-16 used in some serial communications; Checksum used in Internet protocols.

9. Parity check uses even or odd parity to make total number of 1s match expected count.

10. Error correction requires more redundancy than error detection.

## Common Mistakes to Avoid

1. Confusing parity check with error correction - simple parity only detects errors, not corrects them.

2. Forgetting that CRC remainder is appended to the data, not the quotient.

3. Not remembering that Hamming code parity bits are placed at positions that are powers of 2 (1, 2, 4, 8...).

4. Confusing LLC and MAC functions - LLC is for error/flow control, MAC is for addressing and access.

5. Assuming CRC can detect all errors - CRC cannot detect errors where the error pattern equals the generator polynomial.

## Revision Tips

1. Practice calculating parity bits and CRC remainders with sample data.

2. Memorize the Hamming code formula and practice constructing codewords for different data lengths.

3. Create a table comparing all error detection and correction methods with their advantages, limitations, and applications.

4. Remember the seven-layer OSI model order: Please Do Not Throw Sausage Pizza Away (Physical, Data Link, Network, Transport, Session, Presentation, Application).

5. Focus on understanding why different techniques are used in different scenarios rather than just memorizing formulas.