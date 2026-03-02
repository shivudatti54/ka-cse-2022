# Point-to-Point Protocol (PPP) - Summary

## Key Definitions and Concepts

- **Point-to-Point Protocol (PPP)**: A data link layer protocol (RFC 1331) for establishing direct connections between two network nodes over serial links, providing framing, addressing, and control functions.

- **Link Control Protocol (LCP)**: The core PPP subprotocol responsible for establishing, maintaining, testing, and terminating point-to-point connections.

- **Network Control Programs (NCPs)**: A family of protocols that negotiate network layer parameters; IPCP handles IPv4 configuration while IPv6CP handles IPv6.

- **PAP (Password Authentication Protocol)**: A simple authentication protocol that transmits username and password in plaintext.

- **CHAP (Challenge Handshake Authentication Protocol)**: A secure authentication protocol using challenge-response mechanism with MD5 hashing; passwords are never transmitted.

- **PPPoE**: PPP over Ethernet, combining PPP features with Ethernet for broadband DSL access.

## Important Formulas and Theorems

- **Standard PPP Frame Format**: Flag (0x7E) - Address (0xFF) - Control (0x03) - Protocol (2 bytes) - Information - FCS (2 bytes) - Flag (0x7E)

- **Protocol Field Values**:
- 0x0021 = IPv4
- 0xC021 = LCP
- 0xC023 = PAP
- 0xC223 = CHAP

- **CHAP Response**: MD5(Challenge ID + Password + Challenge Value)

- **LCP Packet Types**: Configure-Request/Ack/Nak/Reject, Terminate-Request/Ack, Echo-Request/Reply, Code-Reject

## Key Points

1. PPP operates at the data link layer and provides a modular framework with separate protocols for link control (LCP), authentication, and network layer configuration (NCPs).

2. The five PPP phases must occur in sequence: Link Dead → Link Establishment → Authentication (optional) → NCP Configuration → Link Termination.

3. PAP sends credentials in plaintext and is vulnerable to eavesdropping and replay attacks; CHAP uses random challenges and never transmits passwords.

4. LCP handles link configuration options including MRU, compression, and error detection; it also performs link testing through Echo-Request/Reply packets.

5. IPCP negotiates dynamic IP address assignment (essential for dial-up Internet) and DNS server addresses.

6. PPPoE encapsulates PPP frames in Ethernet for DSL broadband access, using Discovery and Session phases.

7. Multilink PPP aggregates multiple physical links into one logical link for bandwidth aggregation and redundancy.

8. The Address field in PPP is always 0xFF because point-to-point links have only two endpoints.

## Common Mistakes to Avoid

1. Confusing LCP with NCP: Remember LCP handles link-level functions while NCP handles network layer protocol configuration.

2. Assuming PAP is secure: PAP transmits passwords in plaintext; always prefer CHAP for security.

3. Forgetting that PPP requires the Address field: Unlike HDLC, PPP explicitly includes the 0xFF address byte.

4. Not understanding the optional nature of authentication: Authentication is not mandatory in PPP; it is negotiated based on configuration.

5. Mixing up PPP phases: The phase sequence must be maintained—NCP cannot start before successful LCP establishment.

## Revision Tips

1. Draw the complete PPP frame structure and label each field with its standard value and size in bytes.

2. Create a flowchart of PPP phases showing the sequence and transitions between phases.

3. Memorize the key protocol field values as they frequently appear in multiple-choice questions.

4. Practice tracing CHAP authentication exchanges, focusing on why it is more secure than PAP.

5. Review previous question papers to identify the pattern of questions asked on PPP.
