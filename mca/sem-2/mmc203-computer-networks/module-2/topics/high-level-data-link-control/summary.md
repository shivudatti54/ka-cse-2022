# High-Level Data Link Control (HDLC) - Summary

## Key Definitions and Concepts

- **HDLC**: A bit-oriented Data Link Layer protocol developed by ISO for synchronous serial communication
- **Station Configurations**: Primary (controls link), Secondary (responds to primary), Combined (both capabilities)
- **Bit Stuffing**: Technique of inserting '0' after five consecutive '1's to prevent flag sequence appearance in data

## Important Formulas and Theorems

- **Frame Format**: Flag (8b) + Address (8b) + Control (8/16b) + Information (variable) + FCS (16/32b) + Flag (8b)
- **CRC Generation**: Append (n-1) zeros to data, divide by generator polynomial, remainder is CRC
- **Maximum Window Size**: Standard = 7 frames, Extended = 127 frames

## Key Points

1. HDLC uses synchronous transmission with frames delimited by flag sequence 01111110
2. Three frame types: I-frames (data), S-frames (supervisory/flow control), U-frames (unnumbered/management)
3. Control field in I-frames contains both send sequence number (N(S)) and receive sequence number (N(R))
4. Bit stuffing ensures data transparency - receiver performs bit unstuffing
5. HDLC supports three modes: NRM (polled), ARM (secondary can init), ABM (balanced)
6. Error detection uses CRC-16 or CRC-32 with very high detection capability
7. Flow control uses RR (Ready) and RNR (Not Ready) commands
8. Extended format uses 16-bit control field for larger sequence number space

## Common Mistakes to Avoid

1. Confusing I-frame, S-frame, and U-frame control field formats
2. Forgetting bit stuffing at transmitter and unstuffing at receiver
3. Not understanding that FCS comes after Information field, not before
4. Mixing up the purpose of different supervisory frame types (RR, RNR, REJ)
5. Assuming address field always indicates destination - it identifies the secondary station

## Revision Tips

1. Draw the complete HDLC frame structure from memory repeatedly until memorized
2. Practice bit stuffing examples: count five consecutive '1's and insert '0'
3. Remember: Control field determines frame type - check first 1-2 bits
4. Understand that flags appear at both beginning and end of frame
5. Review sequence numbers in sliding window context for error recovery
