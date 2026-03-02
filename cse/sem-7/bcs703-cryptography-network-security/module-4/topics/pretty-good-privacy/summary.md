# Pretty Good Privacy (PGP): Summary

## Definition

Pretty Good Privacy (PGP) is a comprehensive cryptographic system that provides end-to-end encryption, digital signatures, and secure key management for electronic communication. Developed in 1991 by Phil Zimmermann, PGP combines symmetric encryption, asymmetric cryptography, hash functions, and digital signatures into a unified protocol.

## Key Concepts

**Hybrid Encryption Architecture:**
PGP employs a hybrid approach that generates a random session key for each message. The session key encrypts the message content using a symmetric cipher (IDEA, CAST, or AES), while the session key itself is encrypted using the recipient's public key (RSA or ElGamal). This architecture achieves both computational efficiency and secure key distribution.

**Digital Signatures:**
PGP provides authentication through digital signatures created by encrypting a hash of the message with the sender's private key. Verification involves decrypting the signature with the sender's public key and comparing the resulting hash with an independently computed hash of the received message.

**Web of Trust:**
PGP implements a decentralized key authentication model where users vouch for each other's public keys through digital signatures. This contrasts with hierarchical PKI systems and enables scalable trust without centralized certificate authorities.

## Cryptographic Operations

**Encryption:** C = (E_pub(K_pub, K_s), E_sym(K_s, M))

**Decryption:** M = D_sym(D_priv(K_priv, E_pub(K_pub, K_s)), C)

## Security Properties

- **Confidentiality**: End-to-end encryption ensures only intended recipients can read messages
- **Authentication**: Digital signatures verify sender identity and message integrity
- **Non-repudiation**: Sender cannot deny having sent an authenticated message

## Applications

Secure email communication, file encryption, software code signing, and protection of sensitive communications in journalism, legal, medical, and government sectors.