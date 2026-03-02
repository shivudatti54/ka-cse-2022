# Transport Layer Security (TLS)


## Table of Contents

- [Transport Layer Security (TLS)](#transport-layer-security-tls)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [TLS Architecture](#tls-architecture)
  - [Cipher Suites](#cipher-suites)
  - [X.509 Certificates](#x509-certificates)
  - [Session Resumption](#session-resumption)
  - [Forward Secrecy](#forward-secrecy)
- [TLS Handshake Protocol (TLS 1.2 Example)](#tls-handshake-protocol-tls-12-example)
  - [Step-by-Step Process](#step-by-step-process)
- [TLS Record Protocol](#tls-record-protocol)
  - [Data Processing Pipeline](#data-processing-pipeline)
- [TLS Alert Protocol](#tls-alert-protocol)
  - [Critical Alert Types](#critical-alert-types)
- [Examples](#examples)
  - [Example 1: TLS 1.2 Handshake with RSA Key Exchange](#example-1-tls-12-handshake-with-rsa-key-exchange)
- [Extract keys: client_MAC_key, server_MAC_key, client_write_key, server_write_key](#extract-keys-clientmackey-servermackey-clientwritekey-serverwritekey)
  - [Example 2: Perfect Forward Secrecy with ECDHE](#example-2-perfect-forward-secrecy-with-ecdhe)
- [Exam Tips](#exam-tips)

## Introduction

Transport Layer Security (TLS) is a cryptographic protocol that provides end-to-end security for data transmitted over networks. As the successor to SSL (Secure Sockets Layer), TLS 1.3 (latest version) is widely used in HTTPS, email, VoIP, and IoT communications. It ensures three fundamental security properties:

1. **Confidentiality** through symmetric encryption (AES, ChaCha20)
2. **Integrity** via HMAC or AEAD modes
3. **Authentication** using X.509 digital certificates

TLS operates between the application layer (HTTP, SMTP) and transport layer (TCP), making it protocol-agnostic. Its importance stems from:

- Protecting against eavesdropping (man-in-the-middle attacks)
- Preventing data tampering during transmission
- Verifying server identity (and optionally client identity)

## Key Concepts

### TLS Architecture

TLS comprises four sub-protocols:

```math
1. \text{Handshake Protocol} \rightarrow \text{Negotiates parameters, authenticates endpoints}
2. \text{Record Protocol} \rightarrow \text{Encrypts data using session keys}
3. \text{Alert Protocol} \rightarrow \text{Signals errors (e.g., bad\_certificate)}
4. \text{Change Cipher Spec Protocol} \rightarrow \text{Activates negotiated security parameters}
```

### Cipher Suites

A cipher suite specifies cryptographic algorithms in TLS 1.2 and earlier:

```
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  ├── Key Exchange: ECDHE (Elliptic Curve Diffie-Hellman Ephemeral)
  ├── Authentication: RSA
  ├── Encryption: AES-128 in GCM mode
  └── MAC: SHA256
```

In TLS 1.3, cipher suites are simplified (e.g., TLS_AES_256_GCM_SHA384).

### X.509 Certificates

Digital certificates bind public keys to entities. Critical fields:

- Subject (CN=www..ac.in)
- Issuer (O=DigiCert Inc)
- Validity Period
- Public Key (RSA/ECDSA)
- Digital Signature (CA's signature)

### Session Resumption

Two methods to reduce handshake overhead:

1. **Session IDs** (Stateful, server-side storage)
2. **Session Tickets** (Stateless, encrypted ticket sent to client)

### Forward Secrecy

Achieved via Ephemeral Diffie-Hellman (DHE/ECDHE) where temporary keys are used. Compromised long-term keys don't expose past sessions.

## TLS Handshake Protocol (TLS 1.2 Example)

### Step-by-Step Process

1. **ClientHello**
   - Supported TLS versions
   - Client random (32 bytes)
   - Cipher suites list
   - Compression methods

2. **ServerHello**
   - Selected TLS version
   - Server random (32 bytes)
   - Chosen cipher suite
   - Session ID

3. **Certificate**
   - Server sends X.509 certificate chain

4. **ServerKeyExchange**
   - Diffie-Hellman parameters (if using DHE/ECDHE)

5. **ClientKeyExchange**
   - Client's DH public value
   - Pre-master secret generated

6. **Change Cipher Spec**
   - Both parties switch to encrypted communication

7. **Finished**
   - Verify handshake integrity

## TLS Record Protocol

### Data Processing Pipeline

1. **Fragmentation**: Split data into ≤ 16KB blocks
2. **Compression** (Deprecated in TLS 1.3)
3. **Add MAC**: HMAC calculation
4. **Encrypt**: Using symmetric cipher (AES_GCM)
5. **Add TLS Record Header**:
   ```
   struct {
       ContentType type;
       ProtocolVersion version;
       uint16 length;
   } TLSPlaintextRecord;
   ```

## TLS Alert Protocol

### Critical Alert Types

| Alert Level | Examples          | Action Required       |
| ----------- | ----------------- | --------------------- |
| Warning     | close_notify      | Log & Continue        |
| Fatal       | handshake_failure | Immediate Termination |
| Fatal       | bad_certificate   | Connection Aborted    |

## Examples

### Example 1: TLS 1.2 Handshake with RSA Key Exchange

**Scenario**: Client connects to https://.ac.in

1. **ClientHello**: Offers TLS 1.2, cipher suites including TLS_RSA_WITH_AES_128_CBC_SHA
2. **ServerHello**: Selects TLS_RSA_WITH_AES_128_CBC_SHA
3. **Certificate**: Server sends RSA certificate
4. **ClientKeyExchange**:
   - Generate 48-byte pre-master secret
   - Encrypt with server's public key: `C = (PMS)^e mod n`
5. **Key Derivation**:
   ```python
   master_secret = PRF(pre_master_secret, "master secret",
                       ClientHello.random + ServerHello.random)
   key_block = PRF(master_secret, "key expansion",
                   server_random + client_random)
   # Extract keys: client_MAC_key, server_MAC_key, client_write_key, server_write_key
   ```

### Example 2: Perfect Forward Secrecy with ECDHE

**Parameters**:

- Curve: secp256r1
- Server's ephemeral private key: d_s = 0x2A3B...
- Client's ephemeral private key: d_c = 0x5F1E...

**Key Exchange**:

1. Server computes public key: Q_s = d_s \* G
2. Client computes public key: Q_c = d_c \* G
3. Shared secret: Z = d*c * Q*s = d_s * Q_c
4. PMS = x-coordinate of Z (32 bytes)

## Exam Tips

1. **Protocol Versions**: Memorize TLS 1.2 vs 1.3 differences (1.3 removes RSA key transport, adds 0-RTT)
2. **Handshake Steps**: Be able to draw sequence diagram of full TLS 1.2 handshake
3. **Cipher Suite Decoding**: Practice parsing cipher suite codes (e.g., TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)
4. **Key Derivation**: Understand PRF usage in master secret and key block generation
5. **Certificate Validation**: Steps to validate X.509 cert (check expiry, trust chain, CRL/OCSP)
6. **Attack Prevention**: Know how TLS mitigates BEAST, CRIME, POODLE attacks
7. **Alert Codes**: Remember common alerts like handshake_failure (40) and unsupported_certificate (43)
