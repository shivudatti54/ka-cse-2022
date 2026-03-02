# Encapsulating Security Payload

## Introduction

The Encapsulating Security Payload (ESP) is a core protocol in IP Security (IPSec) that provides confidentiality, data integrity, authentication, and anti-replay protection for IP packets. Defined in RFC 4303, ESP operates at the network layer (Layer 3) and is essential for secure communication in VPNs, remote access, and site-to-site connections.

ESP offers two fundamental security services:

1. **Confidentiality** through payload encryption using symmetric algorithms like AES
2. **Data Origin Authentication** through HMAC-based integrity checks

Unlike Authentication Header (AH), ESP encrypts the payload while optionally providing authentication. This makes ESP the preferred choice for most IPSec implementations where both secrecy and integrity are required. A typical use case is corporate VPNs where ESP tunnel mode encrypts all traffic between branch offices.

## ESP Packet Structure

### Header Format

```plaintext
0 1 2 3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Security Parameters Index (SPI) |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Sequence Number |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Payload Data* (variable) |
~ ~
| |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Padding (0-255 bytes) |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Pad Length | Next Header | Authentication Data* |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Key Fields:**

- **SPI (32 bits):** Identifies Security Association (SA) for packet processing
- **Sequence Number (32 bits):** Counter to prevent replay attacks
- **Payload Data:** Encrypted data (including upper-layer protocols)
- **Padding:** Ensures block alignment for encryption algorithms
- **Next Header (8 bits):** Identifies encapsulated protocol (TCP/UDP/ESP)
- **Authentication Data:** Integrity Check Value (ICV) for message authentication

### Trailer Format

The ESP trailer contains:

- Padding (0-255 bytes)
- Pad Length (1 byte)
- Next Header (1 byte)

## Modes of Operation

### 1. Transport Mode

```plaintext
Original IP Packet:
[IP Header][TCP Header][Data]

ESP in Transport Mode:
[IP Header][ESP Header][TCP Header][Data][ESP Trailer][Auth Data]
```

- Encrypts only payload (Data + TCP Header)
- Preserves original IP header
- Used for end-to-end security between hosts

### 2. Tunnel Mode

```plaintext
Original IP Packet:
[IP Header][TCP Header][Data]

ESP in Tunnel Mode:
[New IP Header][ESP Header][IP Header][TCP Header][Data][ESP Trailer][Auth Data]
```

- Encrypts entire original IP packet
- Adds new IP header for routing
- Used for site-to-site VPNs between gateways

## Supported Algorithms

| Service        | Algorithms                        |
| -------------- | --------------------------------- |
| Encryption     | AES (128/256-bit), 3DES, ChaCha20 |
| Authentication | HMAC-SHA1, HMAC-SHA256, AES-GCM   |
| Key Management | IKEv1/IKEv2 (Diffie-Hellman)      |

## Internet Key Exchange (IKE) Integration

ESP relies on IKE for:

1. SA establishment using Main Mode (IKEv1) or IKE_SA_INIT (IKEv2)
2. Key generation through Diffie-Hellman exchange
3. Perfect Forward Secrecy (PFS) support

**IKE Phase 1:** Establishes secure channel for SA negotiation
**IKE Phase 2:** Negotiates ESP-specific parameters (SPI, algorithms)

## Packet Processing Steps

### Outbound Processing

1. Lookup SA using destination IP/SPI
2. Generate sequence number
3. Encrypt payload using symmetric key
4. Calculate ICV for authentication
5. Add ESP header/trailer

### Inbound Processing

1. Validate sequence number (anti-replay window)
2. Verify ICV using shared secret
3. Decrypt payload
4. Pass decrypted data to upper layers

## Examples

### Example 1: ESP Transport Mode Configuration

**Scenario:** Secure communication between Host A (192.168.1.10) and Host B (192.168.1.20)

**Steps:**

1. Establish SA using IKE:

- Encryption: AES-256-CBC
- Authentication: HMAC-SHA256
- SPI: 0x12345678

2. Host A sends packet:

```
Original IP: [Src=192.168.1.10][Dst=192.168.1.20][TCP][Data]
ESP Packet: [IP][ESP Header][Encrypted(TCP+Data)][Auth Data]
```

3. Host B:

- Validates sequence number (e.g., 0x00000001)
- Verifies HMAC-SHA256 ICV
- Decrypts using AES-256 key

### Example 2: ESP Tunnel Mode VPN

**Scenario:** Site-to-site VPN between Gateway A (203.0.113.1) and Gateway B (198.51.100.1)

**Configuration:**

```cisco
crypto ipsec transform-set ESP_TUNNEL esp-aes 256 esp-sha256-hmac
mode tunnel
```

**Packet Flow:**

1. Original packet from 10.1.1.5 to 10.2.2.5
2. Gateway A encapsulates:

```
New IP Header: [Src=203.0.113.1][Dst=198.51.100.1]
ESP Header: [SPI=0xA1B2C3D4][Seq=0x0000A5F3]
Encrypted: [Original IP][TCP][Data]
```

## Real-World Applications

1. **Remote Access VPNs:** ESP tunnel mode secures employee connections
2. **IoT Security:** ESP transport mode protects sensor data
3. **Cloud Connectivity:** AWS VPN uses ESP for VPC peering
4. **VoIP Protection:** ESP encrypts SIP/RTP media streams

## Exam Tips

1. **ESP vs AH:** ESP provides encryption + optional auth, AH only auth
2. **Tunnel Mode Essentials:** Creates new IP header, used for gateway-to-gateway
3. **Anti-Replay Mechanism:** 32-bit sequence number with sliding window
4. **IKE Role:** Phase 2 quick mode negotiates ESP parameters
5. **Padding Purpose:** Align payload to cipher block size (e.g., 16-byte AES)
6. **SPI Function:** 32-bit identifier for Security Association
7. **Common Algorithms:** AES (encryption), HMAC-SHA256 (auth)
