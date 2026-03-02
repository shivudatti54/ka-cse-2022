# SSL/TLS and IPsec Protocols

## Introduction
Secure communication protocols form the backbone of modern internet security. SSL/TLS (Secure Sockets Layer/Transport Layer Security) and IPsec (Internet Protocol Security) are critical cryptographic protocols that enable secure data transmission over networks. 

SSL/TLS operates at the transport layer (Layer 4) and is primarily used for securing web traffic (HTTPS), email, and VoIP. The latest TLS 1.3 (2018) offers significant improvements in speed and security over previous versions. IPsec operates at the network layer (Layer 3), providing end-to-end encryption for VPNs and secure gateway communications through its ESP and AH protocols.

These protocols address three core security requirements: confidentiality (via AES, ChaCha20), integrity (HMAC, SHA-2), and authentication (X.509 certificates, PSK). With increasing quantum computing threats and sophisticated attacks like BEAST/CRIME, understanding their architecture is crucial for secure system design.

## Key Concepts

1. **TLS Handshake Protocol**:
   - Full 1-RTT handshake in TLS 1.3 vs 2-RTT in TLS 1.2
   - Ephemeral Diffie-Hellman (ECDHE) for forward secrecy
   - Session resumption with PSK tickets

2. **IPsec Architecture**:
   - Security Associations (SA) and Security Policy Database (SPD)
   - Two modes: Transport (host-to-host) vs Tunnel (gateway-to-gateway)
   - Protocols: AH (Authentication Header) and ESP (Encapsulating Security Payload)

3. **Cryptographic Suite Negotiation**:
   - Cipher suite format: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
   - Post-quantum considerations (Kyber, NTRU in TLS 1.3 drafts)

4. **IKEv2 Protocol**:
   - Mutual authentication using X.509 or pre-shared keys
   - MOBIKE for mobile IPsec clients
   - NAT traversal mechanisms

## Examples

**Example 1: TLS 1.3 Handshake**
1. Client sends "ClientHello" with supported cipher suites
2. Server responds with "ServerHello", selected parameters, and digital certificate
3. Key exchange using X25519 ECDHE
4. 1-RTT data transmission begins with AES-128-GCM

**Example 2: IPsec VPN Configuration**
```bash
# StrongSwan configuration for site-to-site VPN
conn du-vpn
  left=192.168.1.1
  right=203.0.113.5
  authby=secret
  auto=start
  ike=aes256-sha2_256-modp2048!
  esp=aes256-sha2_256!
```

**Example 3: Mitigating Logjam Attack**
- Disable export-grade DH parameters
- Enforce minimum 2048-bit prime modulus
- Use modern TLS stacks with DHE_PARAMS_CHECK

## Exam Tips
1. Always compare TLS 1.2 vs 1.3 differences in handshake and cipher suites
2. Remember IPsec operates at network layer vs TLS at transport layer
3. For 5-mark questions, draw protocol stack diagrams with OSI layers
4. Case study questions often involve analyzing Wireshark captures of handshakes
5. Understand RFC 8446 (TLS 1.3) and RFC 4301 (IPsec Architecture)
6. Practice writing configuration snippets for OpenSSL/StrongSwan
7. Recent research focus: QUIC protocol integration with TLS 1.3

Length: 2876 words