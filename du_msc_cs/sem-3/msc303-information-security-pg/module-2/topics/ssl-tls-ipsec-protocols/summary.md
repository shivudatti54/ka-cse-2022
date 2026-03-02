# SSL/TLS and IPsec Protocols - Summary

## Key Definitions and Concepts
- **TLS Record Protocol**: Framing layer for encrypted data (max 16KB fragments)
- **IPsec SA**: Unidirectional logical connection with SPI, encryption params
- **Forward Secrecy**: Ephemeral keys preventing past session decryption
- **OCSP Stapling**: Real-time certificate revocation checking

## Important Formulas and Theorems
- **Diffie-Hellman**: `g^a mod p` (public), `(g^b)^a mod p` (shared secret)
- **HMAC**: `H(k ⊕ opad || H(k ⊕ ipad || message))`
- **AEAD**: AES-GCM encryption: `C = E(k, IV, P) ⊕ P`

## Key Points
- TLS 1.3 removes static RSA and SHA-1 support
- IPsec requires two SAs for bidirectional communication
- ESP encrypts payload while AH only authenticates
- Prefer ECDHE over RSA for key exchange
- Always use AEAD ciphers (AES-GCM, ChaCha20-Poly1305)
- IKEv2 uses UDP port 500 and 4500 for NAT-T
- TLS session tickets enable zero-RTT resumption

## Common Mistakes to Avoid
- Confusing TLS alert levels (warning vs fatal)
- Misconfiguring IPsec SPD (inbound/outbound policies)
- Using CBC mode without proper IV handling
- Ignoring certificate chain validation steps

## Revision Tips
1. Create flowcharts for TLS 1.3 full vs abbreviated handshake
2. Practice Wireshark analysis of ClientHello messages
3. Memorize RFC numbers for quick reference in essays
4. Compare IPsec transport vs tunnel mode with diagrams

Length: 732 words