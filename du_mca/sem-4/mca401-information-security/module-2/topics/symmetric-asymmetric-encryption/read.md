# Symmetric & Asymmetric Encryption

## Introduction
Modern cryptography forms the foundation of information security through two fundamental approaches: symmetric and asymmetric encryption. Symmetric encryption uses a single shared key for both encryption and decryption, offering high-speed processing ideal for bulk data encryption. Asymmetric encryption employs mathematically linked key pairs (public/private), solving key distribution challenges and enabling digital signatures.

The importance lies in their complementary roles: symmetric encryption secures data transmission (e.g., AES in WiFi networks), while asymmetric encryption manages secure key exchange and identity verification (e.g., RSA in SSL/TLS). Together, they form the backbone of secure e-commerce, digital banking, and confidential communications. With increasing cyber threats, understanding their mathematical foundations and practical implementations is crucial for security professionals.

## Key Concepts
1. **Symmetric Encryption**
   - **AES Algorithm**: 128/256-bit block cipher using substitution-permutation network
   - **Key Distribution Problem**: Secure exchange of secret keys
   - **Modes of Operation**: ECB (Electronic Code Book), CBC (Cipher Block Chaining) with IV

2. **Asymmetric Encryption**
   - **RSA Cryptosystem**: Based on prime factorization (n = p*q, φ(n) = (p-1)(q-1))
   - **Elliptic Curve Cryptography**: ECDSA for digital signatures using discrete log problem
   - **Digital Certificates**: X.509 certificates binding public keys to identities

3. **Hybrid Systems**
   - Combine both approaches (e.g., PGP: AES for message + RSA for key exchange)
   - Key encapsulation mechanisms in modern protocols like TLS 1.3

4. **Cryptographic Hash Functions**
   - SHA-256 used in Bitcoin mining and certificate signatures
   - HMAC for message authentication codes

## Examples

**Example 1: AES-128 Encryption**
```plaintext
Plaintext: "DU Cybersecurity"
Key: 54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75

Steps:
1. Convert to ASCII: 44 55 20 43... 
2. Key Expansion: Generate 11 round keys
3. Initial Round: AddRoundKey
4. 9 Main Rounds: SubBytes, ShiftRows, MixColumns, AddRoundKey
5. Final Round: Skip MixColumns
Ciphertext: 39 25 84 1D 02 DC 09 FB DC 11 85 97 19 6A 0B 32
```

**Example 2: RSA Key Generation**
```plaintext
1. Choose primes p=61, q=53
2. n = 61*53 = 3233
3. φ(n) = (61-1)(53-1) = 3120
4. Choose e=17 (coprime with φ(n))
5. Compute d ≡ e⁻¹ mod φ(n) = 2753
Public Key: (3233,17)
Private Key: (3233,2753)

Encrypt '65':
C = 65¹⁷ mod 3233 = 2790
Decrypt: 2790²⁷⁵³ mod 3233 = 65
```

**Example 3: TLS Handshake (Hybrid System)**
1. Client sends supported cipher suites
2. Server chooses ECDHE_RSA with AES_256_GCM
3. Certificate exchange with RSA signatures
4. Ephemeral ECDH key exchange
5. Derive shared secret for AES-GCM session keys

## Exam Tips
1. Always compare key sizes: RSA 3072-bit ≈ AES 128-bit security
2. Remember ECB mode is insecure for identical blocks - use CBC/GCM
3. For RSA questions, verify that e and φ(n) are coprime
4. Diffie-Hellman is key exchange, not encryption - often combined with symmetric
5. HMAC prevents tampering, encryption prevents eavesdropping - use both
6. In hybrid systems, asymmetric encrypts the symmetric key only
7. Certificate Authorities use asymmetric crypto to sign public keys