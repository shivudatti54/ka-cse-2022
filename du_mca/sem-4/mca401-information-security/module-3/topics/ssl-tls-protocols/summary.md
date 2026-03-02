# SSL/TLS Protocols - Summary

## Key Definitions and Concepts
- **CipherSuite**: Negotiated algorithms for encryption/MAC (e.g., TLS_AES_128_GCM_SHA256)
- **Ephemeral Keys**: Temporary keys for forward secrecy
- **OCSP Stapling**: Real-time certificate revocation checking
- **ALPN**: Application-Layer Protocol Negotiation extension

## Important Formulas and Theorems
- **Diffie-Hellman Key Exchange**: \( g^{ab} \mod p \)
- **HMAC**: \( \text{HMAC}(K, m) = H((K' \oplus opad) || H((K' \oplus ipad) || m)) \)
- **AEAD**: Authenticated Encryption with Associated Data (AES-GCM)

## Key Points
- TLS 1.3 reduces handshake latency by 50% compared to TLS 1.2
- Always prefer ECDHE over static RSA key exchange
- Session tickets are encrypted and authenticated by the server
- Certificate transparency logs prevent rogue CA issuance
- TLS 1.3 removed compression to prevent CRIME attacks
- 0-RTT data in TLS 1.3 risks replay attacks
- HSTS header enforces HTTPS-only connections

## Common Mistakes to Avoid
- Using SSLv3 or TLS 1.0 in new implementations
- Mixing certificate types (RSA vs ECDSA keys)
- Ignoring SNI configuration in multi-domain hosting
- Disabling certificate revocation checks

## Revision Tips
1. Practice Wireshark captures of TLS handshakes
2. Memorize TLS 1.3 handshake sequence diagram
3. Use OpenSSL commands: `openssl s_client -connect` for debugging
4. Create comparison tables of TLS versions and ciphersuites