# IP Security (IPsec) Overview

## Introduction to IP Security

IP Security (IPsec) is a suite of protocols that provides security services at the IP layer of the networking stack. It enables secure communication over IP networks by authenticating and encrypting each IP packet in a data stream. IPsec operates at the network layer (Layer 3), making it transparent to applications and providing protection for all higher-layer protocols.

**Why IPsec?**
- Provides end-to-end security for IP communications
- Protects against various network attacks (eavesdropping, tampering, spoofing)
- Works with both IPv4 and IPv6 implementations
- Can secure communications between hosts, networks, or host-to-network

## IPsec Architecture Components

IPsec consists of three main components that work together to provide security services:

### 1. Authentication Header (AH)
Provides authentication, integrity, and anti-replay protection for IP packets.

```
+---------------+---------------+---------------+---------------+
|   IP Header   |     AH Header |     TCP/UDP   |     Data      |
|               |               |    Header     |               |
+---------------+---------------+---------------+---------------+
```

### 2. Encapsulating Security Payload (ESP)
Provides confidentiality, authentication, integrity, and anti-replay protection.

```
+---------------+---------------+---------------+---------------+---------------+
|   IP Header   |     ESP Header|     TCP/UDP   |     Data      | ESP Trailer   |
|               |               |    Header     |               | & Auth        |
+---------------+---------------+---------------+---------------+---------------+
```

### 3. Internet Key Exchange (IKE)
A protocol used to establish Security Associations (SAs) and manage cryptographic keys.

## Security Associations (SA)

A Security Association is a fundamental concept in IPsec that defines how communicating entities will use security services. Each SA is a one-way (simplex) logical connection that provides security services to traffic carried on it.

**SA Parameters Include:**
- Security Parameter Index (SPI)
- IP destination address
- Security protocol (AH or ESP)
- Cryptographic algorithms and keys
- Lifetime information
- Mode (transport or tunnel)
- Sequence number counter

```
+----------------------+----------------------+----------------------+
|     SA Parameter     |       Purpose        |       Example        |
+----------------------+----------------------+----------------------+
| Security Parameter   | Identifies the SA    | 32-bit value         |
| Index (SPI)          |                      |                      |
+----------------------+----------------------+----------------------+
| Sequence Number      | Prevents replay      | Counter value        |
| Counter              | attacks              |                      |
+----------------------+----------------------+----------------------+
| Cryptographic        | Encryption/          | AES, 3DES, SHA-1     |
| Algorithms           | authentication      |                      |
+----------------------+----------------------+----------------------+
| Mode                 | Transport or Tunnel  | Transport            |
+----------------------+----------------------+----------------------+
| Lifetime             | Duration of SA      | 86,400 seconds       |
+----------------------+----------------------+----------------------+
```

## IPsec Modes of Operation

### Transport Mode
In transport mode, only the payload of the IP packet is encrypted and/or authenticated. The IP header remains intact.

```
BEFORE IPsec (Original Packet):
+----------------+----------------+----------------+
| IP Header      | TCP Header     | Data           |
+----------------+----------------+----------------+

AFTER IPsec Transport Mode:
+----------------+----------------+----------------+----------------+
| IP Header      | AH/ESP Header  | TCP Header     | Data           |
+----------------+----------------+----------------+----------------+
```

**Use Cases:** Host-to-host communications where both ends support IPsec.

### Tunnel Mode
In tunnel mode, the entire original IP packet is encrypted and/or authenticated, and then encapsulated with a new IP header.

```
BEFORE IPsec (Original Packet):
+----------------+----------------+----------------+
| IP Header      | TCP Header     | Data           |
+----------------+----------------+----------------+

AFTER IPsec Tunnel Mode:
+----------------+----------------+--------------------------------+
| New IP Header  | AH/ESP Header  | Original IP Packet (Encrypted) |
+----------------+----------------+--------------------------------+
```

**Use Cases:** Network-to-network communications (VPNs), host-to-network communications.

## Comparison of AH and ESP

| Feature                  | Authentication Header (AH) | Encapsulating Security Payload (ESP) |
|--------------------------|----------------------------|--------------------------------------|
| Confidentiality          | No                         | Yes                                  |
| Authentication           | Yes                        | Yes (optional)                       |
| Integrity Protection     | Yes                        | Yes                                  |
| Anti-replay Protection   | Yes                        | Yes                                  |
| Protocol Number          | 51                         | 50                                   |
| Protects IP Header       | Yes (except mutable fields)| No                                   |
| NAT Compatibility        | Poor                       | Better (with NAT-T)                  |

## Internet Key Exchange (IKE)

IKE is used to establish shared security parameters and authenticated keys between two entities. It consists of two phases:

### IKE Phase 1
Establishes a secure, authenticated channel for Phase 2 negotiations. Can use either:
- **Main Mode:** 6 messages, more secure but slower
- **Aggressive Mode:** 3 messages, faster but less secure

### IKE Phase 2
Establishes Security Associations for actual data protection using Quick Mode.

## IPsec Implementation Example

Consider a corporate VPN scenario where a remote employee connects to the corporate network:

```
Remote Host (192.168.1.100) <---> Internet <---> Corporate Gateway (10.0.0.1)
                                                                     |
                                                                     |
                                                             Corporate Network (10.0.0.0/24)
```

1. Remote host initiates IKE negotiation with corporate gateway
2. Phase 1 establishes secure channel using pre-shared key or certificates
3. Phase 2 negotiates ESP parameters for data encryption
4. All traffic between remote host and corporate network is encrypted using IPsec tunnel mode

## Security Considerations

**Strengths of IPsec:**
- Strong cryptographic protection
- End-to-end security at the network layer
- Transparency to applications
- Flexibility in algorithm selection

**Potential Vulnerabilities:**
- Implementation flaws in specific vendors
- Misconfiguration of security policies
- Key management issues
- Compatibility problems with Network Address Translation (NAT)

## Exam Tips

1. **Remember the differences between AH and ESP:** AH provides authentication and integrity but no encryption, while ESP provides encryption, authentication, and integrity.
2. **Understand the modes:** Transport mode protects only the payload, while tunnel mode protects the entire original packet.
3. **Know the IKE phases:** Phase 1 establishes the secure channel, Phase 2 establishes the SAs for data protection.
4. **Be familiar with SA parameters:** SPI, algorithms, mode, lifetime are all important components.
5. **Practice packet diagrams:** Be able to draw and explain how packets look in different IPsec modes.