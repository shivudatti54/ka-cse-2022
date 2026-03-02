# Transport Layer Security

## Introduction

Transport Layer Security (TLS) is a cryptographic protocol designed to provide secure communication over a computer network. It operates between the Transport Layer and Application Layer, functioning effectively at the Session Layer of the OSI model (Layer 5). TLS evolved from Secure Sockets Layer (SSL) developed by Netscape in the mid-1990s, with TLS 1.0 standardized in 1999 as SSL 3.1. The protocol ensures confidentiality, integrity, and authentication in network communications through a combination of symmetric cryptography for bulk data encryption, asymmetric cryptography for key exchange and authentication, and hash functions for message integrity verification.

TLS serves as the foundational security protocol for numerous internet applications, including web browsing (HTTPS), email transmission (SMTP/IMAP), virtual private networks (VPNs), and enterprise authentication systems. Within the broader context of User Authentication, TLS provides certificate-based server authentication as a critical first step, and optionally supports client certificate authentication for mutual TLS (mTLS) scenarios. This positions TLS as an essential technology for securing remote user authentication workflows, complementing protocols like Kerberos and asymmetric key-based authentication mechanisms discussed in sibling topics.

The current TLS standard exists in two major versions: TLS 1.2 (RFC 5246, 2008) and TLS 1.3 (RFC 8446, 2018). TLS 1.3 represents a significant redesign, simplifying the handshake, removing obsolete cryptographic algorithms, and mandating forward secrecy. Understanding both versions is essential for network security professionals, as TLS 1.2 remains prevalent in legacy systems while TLS 1.3 increasingly powers modern secure communications.

## Key Concepts

### TLS Architecture and Protocol Stack

TLS comprises four sub-protocols that work together to establish secure sessions:

1. **Handshake Protocol**: Negotiates security parameters, authenticates parties, and establishes cryptographic keys. This is the most complex component, involving multiple round trips between client and server.

2. **Record Protocol**: Provides fragmentation, compression (optional, now disabled), encryption, and MAC generation for transmitted data. It operates on top of TCP and beneath application-layer protocols.

3. **Change Cipher Spec Protocol**: A simple signaling protocol that indicates the transitioning to encrypted communication. In TLS 1.3, this has been merged into the handshake.

4. **Alert Protocol**: Conveys error messages and warnings, including fatal alerts that terminate the connection.

The protocol stack position clarifies a common misconception: TLS operates at the Session Layer (between Transport and Application layers), not the Transport Layer itself—hence the name "Transport Layer Security" derives from its primary purpose of securing transport-layer communications.

### TLS 1.2 Handshake Protocol

The TLS 1.2 full handshake establishes a secure session through the following steps:

**Step 1 - Client Hello**: The client sends a ClientHello message containing:

- Protocol version (TLS 1.2)
- Random 32-byte value (client random)
- Session ID (for resumption)
- Cipher suites list in preference order
- Compression methods
- Extensions (e.g., SNI, ALPN)

**Step 2 - Server Hello**: The server responds with ServerHello selecting:

- Protocol version
- Server random
- Chosen cipher suite
- Compression method
- Session ID

**Step 3 - Server Certificate**: The server sends its X.509 certificate chain. The certificate contains the server's public key and is signed by a trusted Certificate Authority (CA).

**Step 4 - Server Key Exchange** (if applicable): For cipher suites requiring ephemeral key exchange (DHE, ECDHE), the server sends key exchange parameters and a digital signature over server random + client random.

**Step 5 - Certificate Request** (optional): For client authentication, the server requests a certificate.

**Step 6 - Server Hello Done**: The server signals completion of its handshake messages.

**Step 7 - Client Certificate** (if requested): The client sends its certificate chain.

**Step 8 - Client Key Exchange**: The client generates a premaster secret, encrypts it with the server's public key (or performs DH/ECDH key exchange), and sends it to the server.

**Step 9 - Certificate Verify** (if client authenticated): The client signs a hash of all handshake messages using its private key, proving possession of the private key corresponding to its certificate.

**Step 10 - Change Cipher Spec**: Both parties indicate that subsequent messages will use the negotiated algorithms and keys.

**Step 11 - Finished**: Each side sends a hash of all handshake messages, verifying that no tampering occurred.

This handshake requires **two round trips (2-RTT)** in the full case, though session resumption reduces this to 0-RTT.

### TLS 1.3 Improvements

TLS 1.3 (RFC 8446) represents a major revision with several fundamental changes:

1. **Reduced Handshake to 1-RTT**: The new handshake achieves security establishment in a single round trip. For previously connected clients, 0-RTT resumption is supported.

2. **Removed Obsolete Algorithms**: Static RSA key exchange, CBC mode ciphers, and MD5/SHA-1 hash functions are removed. Only AEAD (Authenticated Encryption with Associated Data) ciphers are permitted.

3. **Mandatory Forward Secrecy**: All key exchange methods in TLS 1.3 provide forward secrecy (ECDHE, DHE). Static RSA and DH key exchange are prohibited.

4. **Simplified Cipher Suites**: Cipher suites are reduced to five combinations based on the HKDF hash function (SHA-256 or SHA-384) and key exchange groups (X25519 or P-256).

5. **Encrypted Extensions**: Unlike TLS 1.2, most extensions are encrypted after the ServerHello, enhancing privacy.

6. **Post-Handshake Authentication**: TLS 1.3 allows authentication after the initial handshake, enabling delayed client authentication.

The TLS 1.3 handshake proceeds as:

- **Client Hello**: Proposes cipher suites, sends client key share (ECDHE)
- **Server Hello**: Selects cipher suite, sends server key share, sends certificate
- **Finished**: Both sides derive keys and verify handshake integrity

### Cipher Suites

A cipher suite defines the combination of algorithms used for:

- Key exchange (RSA, DHE, ECDHE)
- Bulk encryption (AES, ChaCha20)
- Message authentication (HMAC, AEAD)
- Hash function (SHA-256, SHA-384)

**Common TLS 1.2 Cipher Suites**:

- `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`: ECDHE key exchange, RSA signatures, AES-256-GCM encryption, SHA-384 hash
- `TLS_DHE_RSA_WITH_AES_128_CBC_SHA`: DHE key exchange, RSA signatures, AES-128-CBC encryption

**TLS 1.3 Cipher Suites** (standardized format):

- `TLS_AES_128_GCM_SHA256`
- `TLS_AES_256_GCM_SHA384`
- `TLS_CHACHA20_POLY1305_SHA256`

The selection of cipher suite critically impacts security. Modern cipher suites use AEAD (Galois/Counter Mode or ChaCha20-Poly1305) which provide both encryption and integrity in a single operation, eliminating vulnerabilities present in separate MAC-then-encrypt constructions.

### Certificate Authentication and PKI

TLS employs X.509 certificates for server authentication (and optionally client authentication). The certificate chain validation process involves:

1. **Certificate Verification**: Verify the signature on the server certificate using the issuer's public key
2. **Chain of Trust**: Follow the certificate chain to a trusted Root CA
3. **Validity Period**: Confirm the certificate is not expired and not yet valid
4. **Name Verification**: Ensure the certificate subject matches the intended server name (hostname verification)
5. **Revocation Checking** (optional but recommended): Check against CRL or OCSP responders

Certificate Pinning adds an additional layer by hardcoding or dynamically storing expected certificate public keys or CA certificates, preventing attacks using fraudulent certificates issued by compromised CAs.

### Forward Secrecy

**Forward Secrecy** (or Perfect Forward Secrecy, PFS) ensures that compromising long-term keys does not compromise past session keys. TLS achieves this through ephemeral key exchange:

- **With Forward Secrecy** (ECDHE, DHE): Each session uses unique temporary (ephemeral) DH/ECDH keys. Even if the long-term private key is compromised, past sessions remain secure.
- **Without Forward Secrecy** (static RSA): The premaster secret is encrypted with the server's static RSA key. If this private key is later compromised, all past encrypted sessions can be decrypted.

TLS 1.3 mandates forward secrecy, while TLS 1.2 requires it for modern security. Systems should disable static RSA key exchange to enforce forward secrecy.

### Session Resumption

TLS session resumption reduces handshake overhead through two mechanisms:

1. **Session Identifier** (TLS 1.2): The server assigns a session ID. Subsequent connections with the same ID can resume with abbreviated handshake, skipping key exchange.

2. **Session Tickets** (TLS 1.2/1.3): The server sends an encrypted session ticket containing session state. The client presents this ticket in subsequent handshakes for 0-RTT resumption.

**0-RTT Mode** (TLS 1.3): The client can send encrypted data immediately in the first flight using pre-derived keys from a previous session. However, 0-RTT data is vulnerable to replay attacks and should only be used for idempotent requests.

### Common TLS Attacks

Understanding TLS attacks is essential for proper configuration and security analysis:

1. **POODLE** (Padding Oracle On Downgraded Legacy Encryption): Exploits CBC mode in SSL 3.0 and TLS 1.0-1.2 by forcing downgrade and exploiting padding oracle. Mitigations: Disable SSL 3.0, use TLS 1.3, prefer AEAD ciphers.

2. **BEAST** (Browser Exploit Against SSL/TLS): Exploits CBC mode in TLS 1.0 by manipulating block boundaries to decrypt plaintext. Mitigations: Use TLS 1.1+, prefer RC4 (historically) or AEAD modes.

3. **Heartbleed**: Buffer overread vulnerability in OpenSSL's heartbeat extension allowing extraction of server memory contents including private keys. Mitigations: Update OpenSSL, disable heartbeat extension.

4. **Downgrade Attacks**: Attacker forces negotiation of weaker protocol versions or cipher suites (e.g., forcing TLS 1.2 → TLS 1.0 → SSL 3.0). Mitigations: Enforce minimum TLS 1.1/1.2, use TLS 1.3, implement protocol fallback validation.

5. **Certificate Spoofing**: Attacker obtains fraudulent certificates or compromises CAs (e.g., DigiNotar breach). Mitigations: Certificate pinning, HSTS (HTTP Strict Transport Security), CT (Certificate Transparency).

### Record Protocol

The TLS Record Protocol provides the secure transport mechanism:

1. **Fragmentation**: Application data is divided into records (typically ≤ 16KB)
2. **Compression**: Applied (disabled in TLS 1.3 due to attacks)
3. **MAC/Integrity**: MAC computed over sequence number + compressed data
4. **Encryption**: Bulk cipher encrypts the compressed data + MAC
5. **Transmission**: Encrypted record sent over TCP

AEAD ciphers (GCM, ChaCha20-Poly1305) compute authentication tags simultaneously with encryption, providing efficient combined confidentiality and integrity.

## Examples

### Example 1: Analyzing Cipher Suite Security

**Given cipher suite**: `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`

**Analysis**:

- **Key Exchange**: ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) provides forward secrecy
- **Authentication**: RSA signatures verify server identity
- **Encryption**: AES-256-GCM provides 256-bit encryption with authenticated encryption
- **Hash**: SHA-384 for key derivation and HMAC

**Security Assessment**: This cipher suite provides:

- Confidentiality: AES-256-GCM provides strong symmetric encryption
- Integrity: GCM mode includes authentication tag
- Authentication: RSA certificates authenticate the server
- Forward Secrecy: ECDHE ensures session keys are ephemeral

**Recommendation**: This is a strong, modern cipher suite suitable for high-security applications.

### Example 2: TLS 1.2 vs TLS 1.3 Handshake Comparison

**Scenario**: A client connects to a server for the first time.

**TLS 1.2 Full Handshake**:

- Client → Server: ClientHello
- Server → Client: ServerHello + Certificate + ServerKeyExchange + CertificateRequest + ServerHelloDone
- Client → Server: Certificate + ClientKeyExchange + CertificateVerify + ChangeCipherSpec + Finished
- Server → Client: ChangeCipherSpec + Finished

**Time**: 2-RTT (approximately 100-300ms latency overhead)

**TLS 1.3 Handshake**:

- Client → Server: ClientHello + ClientKeyShare
- Server → Client: ServerHello + Certificate + ServerKeyShare + Finished

**Time**: 1-RTT (approximately 50-150ms latency overhead)

**Improvement**: TLS 1.3 reduces latency by 50% and eliminates several messages, improving performance especially over high-latency networks.

### Example 3: Identifying Attack Vulnerability

**Scenario**: A server is configured with cipher suites:
`TLS_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_AES_128_CBC_SHA`

**Vulnerability Analysis**:

- **First cipher suite**: Uses static RSA key exchange (no forward secrecy)
  - If server's private key is compromised later, all past captured sessions can be decrypted
  - Vulnerable to passive decryption of recorded traffic
- **Second cipher suite**: Uses DHE (provides forward secrecy)
  - Session keys remain secure even if long-term keys are compromised

**Attack Vector**: An attacker who records encrypted traffic and later obtains the server's private key (through future compromise) can decrypt all sessions using the first cipher suite.

**Recommendation**: Disable static RSA key exchange cipher suites. Prefer ECDHE or DHE-based suites. Upgrade to TLS 1.3 which mandates forward secrecy.

## Exam Tips

1. **Clarify TLS Layer Position**: Remember TLS operates at the Session Layer (between Transport and Application), not the Transport Layer. The name reflects its function of securing transport-layer communications.

2. **TLS 1.3 is the Current Standard**: For modern security configurations, TLS 1.3 should be prioritized. Understand its mandatory forward secrecy, 1-RTT handshake, and removed obsolete algorithms.

3. **Forward Secrecy is Critical**: Always prefer ephemeral key exchange (ECDHE, DHE) over static RSA/DH. TLS 1.3 mandates this; TLS 1.2 configurations should enforce it.

4. **AEAD Ciphers Preferred**: Modern cipher suites should use AEAD modes (GCM, ChaCha20-Poly1305) which provide combined encryption and integrity, avoiding CBC vulnerabilities.

5. **Attack Mitigation Strategies**: Know that POODLE mitigation involves disabling SSL 3.0; BEAST mitigation involves using TLS 1.1+ and AEAD; Heartbleed mitigation involves patching OpenSSL.

6. **Session Resumption Trade-offs**: While session resumption improves performance, 0-RTT resumption in TLS 1.3 is vulnerable to replay attacks. Use only for idempotent operations.

7. **Certificate Chain Validation**: Understand the complete verification process including signature verification, chain of trust, validity period, hostname matching, and optionally revocation checking.
