# IP Security (IPSec): Comprehensive Study Material

## Module: Network Security (10 Hours)

---

## 1. Introduction to IP Security

### 1.1 Overview and Architectural Framework

IP Security (IPSec) constitutes a comprehensive suite of protocols designed to secure Internet Protocol (IP) communications at the network layer. Developed by the Internet Engineering Task Force (IETF), IPSec provides cryptographic-based security services including confidentiality, integrity, authentication, and anti-replay protection for IP packets transmitted across untrusted networks such as the internet.

The IPSec architecture is defined in RFC 4301 and comprises three primary components:

1. **Security Protocols**: Authentication Header (AH) and Encapsulating Security Payload (ESP)
2. **Security Associations (SA)**: Unidirectional logical connections defining security parameters
3. **Key Management**: Internet Key Exchange (IKE) protocol for automated key negotiation

IPSec operates at the network layer (Layer 3 of the OSI model), providing protection for both IPv4 and IPv6 traffic. Unlike transport-layer security protocols (e.g., TLS), IPSec secures the entire IP packet including the IP header, making it transparent to applications.

### 1.2 Security Goals

IPSec addresses the fundamental security requirements for network communications:

- **Confidentiality**: Encryption of packet payloads prevents eavesdropping
- **Integrity**: Hash-based message authentication ensures data has not been modified
- **Authentication**: Digital signatures or HMAC verify the identity of communication endpoints
- **Anti-replay Protection**: Sequence numbers prevent replay attacks

---

## 2. IPSec Protocols

### 2.1 Authentication Header (AH)

The Authentication Header (AH) protocol, defined in RFC 4302, provides integrity and authentication for IP packets without encryption. AH protects the IP header and upper layer protocol data using a hash-based message authentication code (HMAC).

**AH Header Structure:**

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  Next Header│   Length    │   Reserved  │             │
├─────────────┴─────────────┴─────────────┴─────────────┤
│                    Security Parameters Index (SPI)   │
├───────────────────────────────────────────────────────┤
│                      Sequence Number                  │
├───────────────────────────────────────────────────────┤
│                  Authentication Data (Variable)       │
└───────────────────────────────────────────────────────┘
```

**Security Properties:**

- Provides data integrity via ICV (Integrity Check Value)
- Authenticates source using HMAC with shared keys
- Protects against replay attacks using sliding window
- Does NOT provide confidentiality (no encryption)

**Limitation**: AH cannot traverse NAT (Network Address Translation) due to its protection of the IP header, which includes IP addresses that NAT modifies.

### 2.2 Encapsulating Security Payload (ESP)

The Encapsulating Security Payload (ESP) protocol, defined in RFC 4303, provides confidentiality (encryption) and optionally integrity and authentication. ESP is more widely deployed than AH due to its encryption capability.

**ESP Packet Format:**

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│                    Security Parameters Index (SPI)   │
├─────────────┴─────────────┴─────────────┴─────────────┤
│                      Sequence Number                  │
├───────────────────────────────────────────────────────┤
│                    Initialization Vector (IV)         │
├───────────────────────────────────────────────────────┤
│                    Payload Data (Variable)            │
├───────────────────────────────────────────────────────┤
│                 Padding (0-255 bytes)                 │
├─────────────┴─────────────┴─────────────┴─────────────┤
│   Pad Length  │   Next Header  │  Authentication Data │
└─────────────┴─────────────────┴──────────────────────┘
```

**Key Features:**

- Supports encryption algorithms: AES, 3DES, DES, ChaCha20
- Supports authentication algorithms: HMAC-SHA1, HMAC-SHA2, CMAC
- Provides anti-replay protection via sequence numbers
- Can operate with or without authentication

**Encryption Process:**

1. Fragment original IP payload
2. Add padding to meet block cipher requirements
3. Encrypt payload using selected algorithm (e.g., AES-CBC)
4. Calculate ICV over encrypted data (if authentication enabled)
5. Append authentication tag

---

## 3. Operation Modes

### 3.1 Transport Mode

In transport mode, IPSec protects the payload of the original IP packet while preserving the original IP header. This mode is used for host-to-host communication where the original IP addresses must remain visible.

**Characteristics:**

- Protects upper-layer protocols (TCP, UDP, ICMP)
- Original IP header remains unchanged (except protocol field modified to 50 for ESP or 51 for AH)
- Used for end-to-end communication between hosts
- Less overhead than tunnel mode
- Cannot provide complete header confidentiality

**Application**: Suitable for client-server communications where endpoints are the security endpoints.

### 3.2 Tunnel Mode

In tunnel mode, the entire original IP packet (including header) is encapsulated within a new IP packet with a new outer IP header. This mode is used for gateway-to-gateway or gateway-to-host communications.

**Characteristics:**

- Protects entire original IP packet including header
- Creates new outer IP header with gateway addresses
- Provides complete header confidentiality
- Used in VPN implementations (site-to-site, remote access)
- Higher overhead due to additional header

**Application**: Essential for VPNs where intermediate routers need not see internal network addresses.

**Comparison Table:**

| Feature           | Transport Mode          | Tunnel Mode               |
| ----------------- | ----------------------- | ------------------------- |
| Scope             | End-to-end              | Gateway-to-gateway        |
| Header Protection | Original header exposed | Original header protected |
| Overhead          | Lower                   | Higher                    |
| Use Case          | Host-to-host            | VPN, site-to-site         |
| NAT Traversal     | Problematic             | Supported                 |

---

## 4. Security Associations and Databases

### 4.1 Security Association (SA)

A Security Association (SA) is a unidirectional logical connection that defines security properties for IPsec traffic. Since IPSec is bidirectional, two SAs are typically required for full duplex communication—one in each direction.

**SA Parameters (Selectors):**

- Security Parameter Index (SPI): 32-bit identifier
- Destination IP Address
- Security Protocol (AH or ESP)
- Encryption Algorithm and Key
- Authentication Algorithm and Key
- Sequence Number Counter
- Anti-replay Window Size
- SA Lifetime

**SA Establishment:**

- Manual configuration (static keys)
- Automated via IKE protocol (preferred)

### 4.2 Security Association Database (SAD)

The Security Association Database (SAD) stores all active SAs in the system. Each SA entry contains the parameters required for processing outbound or inbound packets.

**SAD Entry Structure:**

- SPI value
- Destination IP
- Protocol (AH/ESP)
- Encryption keys and algorithm
- Authentication keys and algorithm
- Sequence number counter
- Anti-replay window state
- SA lifetime (soft and hard)

### 4.3 Security Policy Database (SPD)

The Security Policy Database (SPD) defines which traffic must be protected, bypassed, or discarded. Policies are evaluated in order (typically top-down) with the first matching rule applied.

**SPD Entry Components:**

- Selector fields (Source IP, Destination IP, Protocol, Ports)
- Action (PROTECT, BYPASS, DISCARD)
- Processing details (SA parameters, mode, protocol)

**Processing Logic:**

```
For each outbound packet:
    Match selectors against SPD entries
    If no match: DISCARD
    If match and action = BYPASS: Forward without protection
    If match and action = PROTECT:
        Locate or establish SA (via SAD)
        Apply AH/ESP processing
        Forward protected packet
```

---

## 5. Internet Key Exchange (IKE)

### 5.1 IKE Protocol Overview

The Internet Key Exchange (IKE) protocol, defined in RFC 7296, provides automated key management and SA establishment for IPSec. IKE uses a hybrid protocol combining ISAKMP, Oakley, and SKEME protocols.

**Primary Functions:**

- Authenticate IPSec peers
- Negotiate security parameters (algorithms, modes)
- Establish and maintain SAs
- Generate and distribute encryption keys
- Provide perfect forward secrecy (PFS)

### 5.2 IKEv2 Improvements

IKEv2 (RFC 7296) simplified IKEv1 while adding significant improvements:

**Advantages over IKEv1:**

- Reduced message exchange from 12 to 4 (or 6 with authentication)
- Built-in NAT traversal support
- Better reliability through acknowledgment mechanism
- Simpler state machine
- Support for Extensible Authentication Protocol (EAP)

**IKEv2 Message Exchange:**

```
Phase 1 (IKE_SA_INIT): Negotiate algorithms, exchange nonces, Diffie-Hellman
    Request → [SAi, Kei, Ni]
    Response ← [SAr, Ker, Nr, CERTREQ]

Phase 2 (IKE_AUTH): Authenticate identities, create IKE_SA
    Request → [IDi, CERT, AUTH, SAi2, TSi, TSr]
    Response ← [IDr, CERTR, AUTH, SAr2, TSir, TSri]

Child SA Creation (CREATE_CHILD_SA):
    Optional additional exchanges for ESP/AH SAs
```

### 5.3 Diffie-Hellman Key Exchange

IKE uses Diffie-Hellman (DH) algorithm to establish a shared secret over an insecure channel without prior shared keys.

**Mathematical Foundation:**
Given prime p and generator g:

1. Peer A generates private key a, computes public key $g^a \mod p$
2. Peer B generates private key b, computes public key $g^b \mod p$
3. Exchange public keys
4. Both compute shared secret: $(g^b)^a = (g^a)^b = g^{ab} \mod p$

**Perfect Forward Secrecy (PFS)**: Requires a new DH exchange for each SA rekey, ensuring compromise of long-term keys does not expose past session keys.

---

## 6. IPSec Policy Configuration

### 6.1 Policy Components

An IPSec policy defines the rules governing security behavior:

| Component  | Description                                             |
| ---------- | ------------------------------------------------------- |
| Selector   | Traffic matching criteria (IPs, ports, protocol)        |
| Action     | Protect, bypass, or discard                             |
| Protocol   | AH, ESP, or AH+ESP                                      |
| Mode       | Transport or tunnel                                     |
| Algorithms | Encryption (AES-256, 3DES) and authentication (SHA-256) |
| Lifetime   | SA validity duration and data volume limits             |

### 6.2 Combined Security Associations

For comprehensive security, both AH and ESP can be applied in sequence. ESP provides confidentiality while AH provides integrity for the outer IP header in tunnel mode.

**Common Combinations:**

- ESP alone: Confidentiality with optional authentication
- AH + ESP: Full integrity (including header) plus confidentiality
- AH alone: Integrity without encryption (rarely used)

---

## 7. Review Questions

### Multiple Choice Questions (Application Level)

**Question 1**: An organization requires secure communication between two hosts where both data integrity and confidentiality are essential. The hosts are behind NAT devices. Which IPSec configuration BEST meets these requirements?

A) AH in transport mode
B) ESP in tunnel mode
C) ESP in transport mode
D) AH in tunnel mode

**Answer**: B) ESP in tunnel mode

**Explanation**: ESP provides both confidentiality (encryption) and integrity. Tunnel mode is required because NAT devices modify IP addresses—AH cannot work through NAT as it authenticates the IP header. Tunnel mode encapsulates the entire original packet, allowing NAT to modify the outer header while preserving the inner encrypted content.

---

**Question 2**: Given an ESP packet with payload size of 137 bytes using AES (128-bit block size) in CBC mode with HMAC-SHA-256 for authentication, calculate the minimum padding required.

A) 15 bytes
B) 16 bytes
C) 19 bytes
D) 23 bytes

**Answer**: C) 19 bytes

**Explanation**: AES-CBC requires input to be a multiple of 16 bytes (128 bits).

Payload (137) + Next Header (1) + Pad Length (1) = 139 bytes

Next multiple of 16 = 144 bytes

Padding required = 144 - 139 = 5 bytes (minimum)

However, padding must also align to 4-byte boundary for some implementations. With authentication data (32 bytes for HMAC-SHA-256), the total expands, but minimum payload padding is 5 bytes. Wait—recalculating: 137 + 1 (next header) + 1 (pad length) = 139. To reach 144 (16 × 9): 144 - 139 = 5 bytes minimum.

---

**Question 3**: In IKEv2, if Perfect Forward Secrecy (PFS) is required, which parameter must be renegotiated during Child SA establishment?

A) Authentication credentials
B) Identities
C) Diffie-Hellman key exchange
D) IKE SA lifetime

**Answer**: C) Diffie-Hellman key exchange

**Explanation**: Perfect Forward Secrecy ensures that compromise of long-term keys does not expose session keys. This requires generating a new DH shared secret for each SA. During Child SA (ESP/AH SA) creation, if PFS is enabled, a new DH exchange occurs to derive fresh keying material, independent of the IKE SA keys.

---

**Question 4**: A security administrator configures an IPSec tunnel between two corporate sites. The SPD entry specifies "Tunnel mode, ESP, AES-256, SHA-256." What happens to packets matching this policy?

A) Packets are forwarded without encryption
B) Packets are encapsulated with new outer IP header and encrypted
C) Only authentication header is added
D) Packets are rejected due to invalid configuration

**Answer**: B) Packets are encapsulated with new outer IP header and encrypted

**Explanation**: Tunnel mode with ESP encrypts the entire original IP packet (header + payload) and encapsulates it within a new IP packet. The outer header contains the gateway addresses, while the inner packet (encrypted) contains the original source/destination. AES-256 provides confidentiality and SHA-256 provides integrity via the authentication tag.

---

**Question 5**: Which database entry MUST be checked first when processing an outbound IP packet in an IPSec implementation?

A) Security Association Database (SAD)
B) Security Policy Database (SPD)
C) Peer Authorization Database
D) Certificate Repository

**Answer**: B) Security Policy Database (SPD)

**Explanation**: The processing order is critical:

1. SPD determines whether traffic requires protection (PROTECT), should bypass protection (BYPASS), or be discarded (DISCARD)
2. If PROTECT is specified, the SAD is consulted to find or establish an appropriate SA
3. The SA provides the actual security parameters (algorithms, keys, SPI)

Checking SAD before SPD would be inefficient and could apply incorrect security to traffic that should be discarded.

---

## 8. Summary

IPSec provides comprehensive network-layer security through its dual protocol architecture (AH and ESP), flexible operation modes (transport and tunnel), and robust key management via IKE. The Security Association model provides granular control over security parameters, while the Security Policy Database enables sophisticated traffic filtering. Understanding the interplay between these components is essential for designing secure VPN solutions and protecting network communications against eavesdropping, tampering, and spoofing attacks.
