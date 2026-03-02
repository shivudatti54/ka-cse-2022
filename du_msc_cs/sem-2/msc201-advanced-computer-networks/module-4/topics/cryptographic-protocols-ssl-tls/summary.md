# Cryptographic Protocols: SSL/TLS - Summary

## Key Definitions and Concepts
- **AEAD**: Encryption providing confidentiality + integrity
- **SNI**: Server Name Indication for multi-domain hosting
- **OCSP Stapling**: Real-time certificate revocation status
- **HSTS**: HTTP Strict Transport Security policy

## Important Formulas and Theorems
- `Finished = HMAC(handshake_hash, master_secret)`
- ECDHE key exchange: `s = (Y^r mod p)^x mod p`
- HKDF key derivation: `HKDF-Expand(PRK, info, L)`

## Key Points
- TLS 1.3 removes static RSA key exchange
- Always prefer ECDHE over static DH
- Certificate chains must validate to trusted root CA
- TLS False Start reduces latency but risks cipher downgrade
- ALPN (Application-Layer Protocol Negotiation) enables HTTP/2
- Session tickets require secure storage
- TLS 1.3 mandates digital signatures over RSA encryption

## Common Mistakes to Avoid
- Using TLS 1.0/1.1 in modern implementations
- Mixing certificate types (RSA vs ECDSA keys)
- Neglecting cipher suite prioritization
- Disabling certificate revocation checks

## Revision Tips
1. Practice handshake sequence diagrams
2. Use `openssl s_client` for real-world analysis
3. Memorize RFC numbers: TLS 1.3 (RFC 8446)
4. Study Cloudflare's TLS configuration guidelines

Length: 650 words