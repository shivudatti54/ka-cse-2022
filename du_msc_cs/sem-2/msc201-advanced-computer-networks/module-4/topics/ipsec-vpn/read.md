# IPSec VPN

## Introduction
IPSec (Internet Protocol Security) VPN is a critical framework for securing internet communications through cryptographic authentication and encryption. As organizations increasingly rely on public networks for sensitive data transmission, IPSec VPNs provide essential confidentiality, integrity, and authentication services. Unlike traditional VPNs, IPSec operates at the network layer (Layer 3), enabling secure communication between entire networks, hosts, and applications.

The protocol suite gained prominence with IPv6 adoption but remains vital in IPv4 environments. Modern applications include secure site-to-site connections for multinational corporations, remote workforce access, and IoT device security. Recent research focuses on post-quantum cryptography integration and optimizing IPSec for 5G/6G networks, making it a dynamic area in network security studies.

## Key Concepts
1. **Security Associations (SA)**: 
   - Unidirectional logical connections defining security parameters
   - Includes SPI (Security Parameters Index), encryption algorithms (AES, ChaCha20), and integrity checks (SHA-2)
   - Managed through IKE (Internet Key Exchange)

2. **Authentication Header (AH)**:
   - Provides data origin authentication and integrity
   - Protocol 51, covers immutable IP header fields
   - Vulnerable to NAT traversal issues

3. **Encapsulating Security Payload (ESP)**:
   - Protocol 50 offering confidentiality (encryption) + authentication
   - Supports multiple modes: Transport (host-to-host) vs Tunnel (gateway-to-gateway)

4. **IKE Phases**:
   - Phase 1: Establishes secure channel using Diffie-Hellman (Elliptic Curve variants preferred)
   - Phase 2: Negotiates IPSec SAs for data transfer
   - IKEv2 improvements: MOBIKE for mobility, denial-of-service protection

5. **Modes of Operation**:
   - Transport Mode: Encrypts payload only (ideal for end-to-end security)
   - Tunnel Mode: Encrypts entire IP packet (used in site-to-site VPNs)

## Examples
**Example 1: Site-to-Site VPN Setup**
1. Network A (192.168.1.0/24) ↔ Network B (10.0.0.0/16)
2. Configure IKEv2 with ECDH-384 and AES-256-GCM
3. Establish tunnel mode ESP SAs
4. Test connectivity: `ping 10.0.0.1` from Network A while capturing ESP packets in Wireshark

**Example 2: ESP Packet Analysis**
Original IP Packet:
- SRC: 203.0.113.5, DST: 198.51.100.10
- Payload: "DU_CS_NEP2024"

ESP Packet Structure:
- SPI: 0x1a2b3c4d
- Sequence: 1
- IV: 16-byte nonce
- Encrypted Data: AES-256(GCM("DU_CS_NEP2024"))
- ICV: 96-bit authentication tag

**Example 3: IKEv2 Negotiation**
1. Initiator → Responder: SAi1 (propose AES-GCM, SHA-384)
2. Responder ← Initiator: SAr1 (selected algorithms)
3. Key Exchange: ECDH over secp384r1
4. Authentication: Mutual PSK verification
5. Create Child SA for ESP

## Exam Tips
1. Always distinguish between AH (integrity) vs ESP (confidentiality+integrity)
2. Memorize IKE phase details: Phase 1 (ISAKMP SA) vs Phase 2 (IPSec SA)
3. Transport vs Tunnel mode diagrams are frequent in 10-mark questions
4. Know modern algorithm pairs: AES-GCM with ECDH-521 for quantum resistance
5. Practice ESP packet header field identification from hex dumps
6. Understand NAT-Traversal (UDP 4500) implications on AH
7. Recent research angle: Discuss IPSec in SDN/NFV architectures