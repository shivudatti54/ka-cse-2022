# QUIC Protocol - Summary

## Key Definitions and Concepts
- **QUIC**: Transport protocol over UDP with encryption, multiplexing, and reduced latency.
- **Connection UUID**: Persistent identifier for connection migration.
- **Stream**: Bidirectional byte stream with independent flow control.
- **HOL Blocking**: Delays in ordered data delivery (eliminated in QUIC).

## Important Formulas and Theorems
- **Packet Loss Calculation**: Loss rate = (Lost packets) / (Total sent packets)
- **BBR Congestion Control**: max_BW × min_RTT = optimal congestion window
- **0-RTT Data Limit**: Anti-replay window (e.g., < 64 KB per session)

## Key Points
- Uses UDP to bypass middlebox restrictions
- Mandatory encryption with TLS 1.3
- 1-RTT for new connections, 0-RTT for resumed
- Stream independence prevents HOL blocking
- Connection migration supports mobile devices
- Pluggable congestion control algorithms
- Standardized as RFC 9000 (QUIC) and RFC 9114 (HTTP/3)

## Common Mistakes to Avoid
- Confusing QUIC with HTTP/3 (QUIC is transport layer; HTTP/3 is application layer)
- Assuming all UDP-based protocols are unreliable (QUIC adds reliability)
- Overlooking QUIC's anti-ossification mechanisms
- Ignoring 0-RTT security implications (replay attacks)

## Revision Tips
1. Use Wireshark with QUIC dissector to analyze real packets.
2. Compare QUIC's frame types with TCP segments.
3. Practice drawing state diagrams for connection migration.
4. Review IETF RFCs 9000-9002 for protocol details.

Length: 600 words