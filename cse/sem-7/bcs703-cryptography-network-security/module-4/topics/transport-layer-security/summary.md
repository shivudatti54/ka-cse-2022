# Transport Layer Security (TLS) - Summary

## Key Definitions and Concepts

- **TLS**: Cryptographic protocol providing end-to-end security at transport layer (OSI Layer 4)
- **Handshake Protocol**: Negotiates cipher suites, authenticates server, establishes keys
- **Record Protocol**: Encrypts data using symmetric algorithms (AES/3DES) and ensures integrity with HMAC
- **Cipher Suite**: Combination of algorithms (e.g., `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`)
- **X.509 Certificate**: Digital certificate using PKI for server authentication
- **Session Resumption**: TLS feature to reuse security parameters via Session ID/Ticket
- **Perfect Forward Secrecy (PFS)**: Ephemeral keys (DHE/ECDHE) prevent future decryption of past sessions
- **Heartbeat Extension**: Keep-alive mechanism (vulnerable to Heartbleed attack if misconfigured)

## Important Formulas and Theorems

```markdown
1. TLS Version Identifier: `0x0303` for TLS 1.2, `0x0304` for TLS 1.3
2. Premaster Secret:
   - RSA: `PremasterSecret = (ClientRandom || ServerRandom)`
   - Diffie-Hellman: `PremasterSecret = g^(ab) mod p`
3. Master Secret:
   `MasterSecret = PRF(PremasterSecret, "master secret", ClientRandom + ServerRandom)`
4. Record Protocol Encryption:
   `Ciphertext = Encrypt(MAC(SequenceNumber || Plaintext))`

Theorem: Diffie-Hellman Key Exchange

- Secure if discrete logarithm problem is hard: `(g^a mod p)^b mod p = (g^b mod p)^a mod p`
```

## Key Points

1. TLS 1.2 is most widely used version; TLS 1.3 removes legacy features (SHA-1, RSA key transport)
2. Handshake has 4 phases: Hello messages, key exchange, parameters verification, finish
3. Cipher suite contains: Key exchange (ECDHE), authentication (RSA), bulk encryption (AES), MAC (SHA256)
4. PFS requires ephemeral Diffie-Hellman (DHE/ECDHE) in cipher suite
5. Session resumption reduces handshake latency using Session ID (stateful) or Session Ticket (stateless)
6. TLS operates between transport and application layers (unlike IPsec at network layer)
7. HTTPS = HTTP + TLS; SMTP with TLS uses STARTTLS command
8. Alert Protocol (severity levels: warning/fatal) terminates insecure connections

## Common Mistakes to Avoid

1. Confusing TLS (transport layer) with SSL (deprecated predecessor) or IPsec (network layer)
2. Assuming TLS alone provides security without proper certificate validation
3. Using weak cipher suites (RC4, MD5) or static RSA key exchange (no PFS)
4. Misunderstanding TLS termination points (end-to-end vs gateway-based architectures)

## Revision Tips

1. **Handshake Flow**: Memorize sequence diagram with ClientHello, ServerHello, Certificate, ServerKeyExchange, etc.
2. **Cipher Suite Decoding**: Practice parsing examples like `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
3. **Packet Analysis**: Use Wireshark to inspect TLS handshake in HTTPS traffic
4. **Compare Protocols**: Make table contrasting TLS (OSI Layer 4) vs IPsec (Layer 3) vs SSH (Layer 7)
