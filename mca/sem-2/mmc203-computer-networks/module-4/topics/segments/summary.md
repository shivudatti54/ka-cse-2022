# TCP Segments - Summary

## Key Definitions

- **Segment**: The protocol data unit (PDU) at the TCP Transport Layer
- **Sequence Number**: 32-bit number indicating the byte position of the first data byte in a segment
- **Acknowledgment Number**: 32-bit number indicating the next expected byte, confirming receipt of all prior bytes
- **Maximum Segment Size (MSS)**: The largest amount of data in a single TCP segment
- **Control Flags**: Six bits (URG, ACK, PSH, RST, SYN, FIN) controlling segment behavior
- **Window Size**: 16-bit field indicating the receive buffer capacity for flow control

## Important Formulas

- **Sequence Number Range**: If Seq = X and Data Length = L, bytes range from X to (X + L - 1)
- **Next Expected Byte**: Acknowledgment Number = Last Received Byte + 1
- **Header Length**: Data Offset × 4 bytes (value 5 = 20 bytes, 15 = 60 bytes)
- **Maximum Window**: 65,535 bytes (without window scaling)

## Key Points

1. TCP segment header has a minimum of 20 bytes and maximum of 60 bytes
2. Both source and destination ports are 16-bit fields identifying applications
3. Sequence numbers are 32-bit and use modulo 2³² arithmetic
4. The ACK flag indicates the acknowledgment number field is valid
5. The SYN flag is used exclusively during connection establishment
6. The FIN flag initiates graceful connection termination
7. TCP provides reliable, ordered, connection-oriented communication
8. The checksum provides error detection for header and data
9. Options like MSS, window scaling, and timestamps extend segment capabilities

## Common Mistakes

1. Confusing sequence number with segment number—they represent byte positions
2. Forgetting that acknowledgment numbers are cumulative
3. Not accounting for the pseudo-header when calculating checksums
4. Assuming all segments carry data—SYN and FIN segments carry no data
5. Misinterpreting the window size field as bytes available rather than receive capacity