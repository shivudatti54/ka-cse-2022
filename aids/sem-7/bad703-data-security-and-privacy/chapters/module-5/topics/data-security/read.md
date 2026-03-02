# Transport Layer Security (TLS)

## Introduction to TLS

Transport Layer Security (TLS) is a cryptographic protocol designed to provide secure communication over a computer network. It is the successor to the Secure Sockets Layer (SSL) protocol. TLS ensures **privacy**, **data integrity**, and **authentication** between two communicating applications, most commonly a web client (browser) and a web server.

The protocol operates at the transport layer of the OSI model, sitting between the application layer (e.g., HTTP) and the transport layer (e.g., TCP). When HTTP is used over TLS, it is referred to as HTTPS (HTTP Secure).

## The Need for TLS

Without TLS, data sent over a network is transmitted in plaintext. This makes it vulnerable to:
*   **Eavesdropping**: An attacker can read sensitive information.
*   **Tampering**: An attacker can alter the data in transit.
*   **Impersonation**: An attacker can pretend to be a legitimate website (e.g., a phishing site).

TLS mitigates these threats by encrypting the communication channel and verifying the identity of the communicating parties.

## TLS Protocol Architecture

TLS is not a single protocol but a framework comprised of several protocols. The two main layers are:

1.  **TLS Handshake Protocol**: Responsible for negotiating the cryptographic parameters of the session, authenticating the server (and optionally the client), and establishing shared secret keys.
2.  **TLS Record Protocol**: Responsible for the actual secure transmission of data using the parameters established by the Handshake Protocol. It provides confidentiality through symmetric encryption and integrity through a Message Authentication Code (MAC).

```
+---------------------------------+
|  HTTP, SMTP, FTP (Application)  |
+---------------------------------+
|    TLS Handshake Protocol       |
|    TLS Change Cipher Spec       |
|    TLS Alert Protocol           |
+---------------------------------+
|        TLS Record Protocol      |
+---------------------------------+
|          TCP / IP               |
+---------------------------------+
```
*Figure 1: TLS Protocol Stack*

## TLS Handshake Protocol

The handshake is the most complex part of TLS. Its purpose is to create a shared secret between the client and server, known as the **master secret**, from which the actual encryption and MAC keys are derived.

### Detailed Handshake Steps

```
Client                                                                  Server
  |                                                                        |
  | 1. ClientHello (Random_C, CipherSuites, TLS Version)                   |
  |----------------------------------------------------------------------->|
  |                                                                        |
  | 2. ServerHello (Random_S, Chosen CipherSuite, SessionID, TLS Version)  |
  | 3. Certificate (Server's digital certificate)                           |
  | 4. ServerKeyExchange (Optional, e.g., for DH parameters)                |
  | 5. CertificateRequest (Optional, for client authentication)             |
  | 6. ServerHelloDone                                                      |
  |<-----------------------------------------------------------------------|
  |                                                                        |
  | 7. Certificate (Optional, if requested)                                |
  | 8. ClientKeyExchange (Pre-master secret, encrypted with server's PK)   |
  | 9. CertificateVerify (Optional, proves client owns the private key)    |
  |----------------------------------------------------------------------->|
  |                                                                        |
  | 10. ChangeCipherSpec (Switch to negotiated ciphers)                    |
  | 11. Finished (First encrypted message under new keys)                  |
  |----------------------------------------------------------------------->|
  |                                                                        |
  | 12. ChangeCipherSpec                                                   |
  | 13. Finished                                                           |
  |<-----------------------------------------------------------------------|
  |                                                                        |
  |                       Secure Application Data Flow                     |
  |<======================================================================>|
```
*Figure 2: TLS Full Handshake (with client authentication)*

1.  **ClientHello**: The client initiates the handshake by sending:
    *   `Client Random`: A 32-byte random number.
    *   `Cipher Suites`: A list of cryptographic algorithms the client supports (e.g., TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256).
    *   `TLS Version`: The highest TLS version it supports.

2.  **ServerHello**: The server responds with:
    *   `Server Random`: Its own 32-byte random number.
    *   `Session ID`: An identifier for this session (for session resumption).
    *   `Chosen Cipher Suite`: The strongest cipher suite from the client's list that the server also supports.
    *   `TLS Version`: The version that will be used for this connection.

3.  **Certificate**: The server sends its digital certificate (X.509), which contains its public key and is signed by a trusted Certificate Authority (CA). This allows the client to authenticate the server.

4.  **ServerKeyExchange (Optional)**: This message is sent if the certificate does not contain enough data for key exchange (e.g., in Diffie-Hellman Ephemeral (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE)).

5.  **CertificateRequest (Optional)**: The server can request a certificate from the client for mutual authentication.

6.  **ServerHelloDone**: Signals the end of the server's hello phase.

7.  **Certificate (Client)**: If requested, the client sends its own certificate.

8.  **ClientKeyExchange**: The client generates a **pre-master secret**, a 48-byte random value. It encrypts this pre-master secret with the server's public key (from its certificate) and sends it to the server. *Only the server, possessing the corresponding private key, can decrypt it.*

9.  **CertificateVerify (Optional)**: If client authentication was used, this message contains a digital signature over the handshake messages, proving the client possesses the private key for the certificate it sent.

10. **ChangeCipherSpec**: Both client and server send this message to signal that all subsequent messages will be encrypted using the newly negotiated keys and algorithms.

11. **Finished**: The first message encrypted with the new keys. It contains a cryptographic hash (MAC) of all previous handshake messages. This verifies that the handshake was not tampered with.

Both client and server now independently compute the same **master secret** from the pre-master secret, client random, and server random using a Pseudorandom Function (PRF). From this master secret, they derive the symmetric encryption keys and MAC keys for the session.

## TLS Record Protocol

Once the handshake is complete, the Record Protocol takes over to securely transmit application data.

Its operation involves several steps:
1.  **Fragmentation**: The application data is split into manageable blocks (`TLSPlaintext` records).
2.  **Compression (Deprecated)**: Historically, data could be compressed. This is now disabled due to attacks like CRIME.
3.  **Add MAC**: A Message Authentication Code (MAC) is computed over the compressed data and appended to it, ensuring integrity. This creates a `TLSCompressed` record.
4.  **Encryption**: The data + MAC is encrypted using the symmetric cipher and keys agreed upon during the handshake, resulting in a `TLSCiphertext` record.
5.  **Add Record Header**: A header is prepended, containing content type, TLS version, and length.
6.  **Transmit**: The final record is transmitted over the TCP connection.

The receiving end reverses the process: decrypt, verify MAC, decompress (if applicable), reassemble, and pass to the application.

## Key Cryptographic Components in TLS

TLS leverages concepts from all previous modules:

| Cryptographic Function | TLS Usage | Module Reference |
| :--- | :--- | :--- |
| **Symmetric Encryption** (AES, ChaCha20) | Encrypting bulk application data for confidentiality. | Module-1 (Block Ciphers) |
| **Public Key Cryptography** (RSA, ECDSA) | Authenticating the server (and client) via digital certificates. Also used in RSA key exchange to encrypt the pre-master secret. | Module-2 (Public Key) |
| **Key Exchange** (Diffie-Hellman, ECDH) | Ephemeral variants (DHE, ECDHE) allow **Forward Secrecy**. The pre-master secret is derived from DH parameters, not static keys. | Module-2 (Diffie-Hellman) |
| **Hash Functions** (SHA-256) | Used in the PRF to generate keys. Also used for computing the MAC in the Record Protocol and the hash in the Finished message. | Module-3 (Hash Functions) |
| **Digital Certificates (X.509)** | Used to bind a public key to a server's identity, forming the basis of authentication. Relies on a Public Key Infrastructure (PKI). | Module-3 (PKI) |
| **Message Authentication Code (MAC)** | HMAC is commonly used to ensure the integrity of transmitted records. | Module-3 (Hash Functions) |

## TLS Versions and Evolution

*   **SSL 1.0**: Never released publicly due to security flaws.
*   **SSL 2.0 (1995)**: First public release. Deprecated due to numerous weaknesses.
*   **SSL 3.0 (1996)**: A complete redesign. Now considered insecure (POODLE attack) and deprecated.
*   **TLS 1.0 (1999)**: Based on SSL 3.0 but not interoperable. Now considered obsolete.
*   **TLS 1.1 (2006)**: Added protection against cipher block chaining (CBC) attacks. Now deprecated.
*   **TLS 1.2 (2008)**: Introduced support for authenticated encryption (AEAD) ciphers like AES-GCM. Significantly more secure. Still widely used but being phased out.
*   **TLS 1.3 (2018)**: A major overhaul for speed and security. Removed insecure features (static RSA key exchange, compression), reduced handshake to 1-RTT (or 0-RTT with caveats), and mandated forward secrecy.

**Comparison of TLS 1.2 vs TLS 1.3 Handshake**

| Feature | TLS 1.2 | TLS 1.3 |
| :--- | :--- | :--- |
| **RTTs to full handshake** | 2 | 1 (or 0 for resumption) |
| **Negotiable Ciphers** | Many legacy/insecure options | Only secure, modern ciphers |
| **Key Exchange** | Supports non-PFS (RSA) | Mandates PFS (only DHE/ECDHE) |
| **Secrecy of identity** | Server identity (certificate) sent in clear text | Server certificate is encrypted |
| **Features Removed** | - | Compression, Renegotiation, many cipher suites |

## Common Attacks and Mitigations

*   **Man-in-the-Middle (MitM)**: Prevented by proper certificate validation. Clients must verify the server's certificate chain against a list of trusted CAs.
*   **BEAST (Browser Exploit Against SSL/TLS)**: Targeted a vulnerability in TLS 1.0's CBC-mode encryption. Mitigated by using TLS 1.1+ or RC4 (now also insecure).
*   **POODLE (Padding Oracle On Downgraded Legacy Encryption)**: Attack on the padding in SSL 3.0's CBC mode. Mitigation: disable SSL 3.0 entirely.
*   **Heartbleed (2014)**: A buffer-overread bug in the OpenSSL implementation's heartbeat extension, not a protocol flaw. It allowed reading memory from the server.
*   **Downgrade Attacks**: Where an attacker forces a client and server to use a weaker protocol version. Mitigated by using **TLS_FALLBACK_SCSV** or simply supporting only modern versions like TLS 1.3.

## Exam Tips

1.  **Memorize the Handshake Steps**: Be able to list and describe the purpose of each major message (`ClientHello`, `ServerHello`, `Certificate`, `ClientKeyExchange`, `Finished`). Understand what the pre-master secret and master secret are.
2.  **Understand the "Why"**: Don't just learn the steps. Know *why* each step is necessary (e.g., `Server Random` and `Client Random` prevent replay attacks).
3.  **Focus on TLS 1.2 and 1.3**: Know the key differences between them, especially the move to mandatory forward secrecy and the faster 1-RTT handshake in TLS 1.3.
4.  **Link to Other Modules**: TLS is a synthesis of earlier topics. Be prepared to explain how symmetric encryption, public-key crypto, hashes, and PKI all work together in TLS.
5.  **Know the Record Protocol**: Understand the steps of fragmentation, adding a MAC, and encryption. A simple diagram can be worth many words.
6.  **Be Aware of Attacks**: You should know the general concepts behind common attacks like BEAST, POODLE, and Heartbleed, and more importantly, how they are mitigated (e.g., disabling old protocols).