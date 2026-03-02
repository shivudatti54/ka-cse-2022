# Public-Key Encryption and Digital Signatures - Summary

## Key Definitions and Concepts

- **Public-Key Encryption**: Asymmetric cryptography using a key pair—public key for encryption, private key for decryption. Solves the key distribution problem inherent in symmetric cryptography.

- **RSA Algorithm**: The most widely used public-key cryptosystem, security based on integer factorization difficulty. Key generation involves selecting primes p and q, computing n = pq, finding e and d such that ed ≡ 1 (mod φ(n)).

- **Digital Signature**: Mathematical scheme providing authentication, integrity, and non-repudiation. Created by encrypting a hash of the message with the signer's private key.

- **Hash Function**: One-way function producing fixed-length output from arbitrary input. Essential for efficient digital signatures. Properties: one-way, collision-resistant, deterministic.

- **PKI (Public Key Infrastructure)**: Framework for managing digital certificates and public-key encryption, involving CAs, certificate registration, issuance, and revocation.

## Important Formulas and Theorems

- **RSA Encryption**: C = M^e mod n
- **RSA Decryption**: M = C^d mod n
- **Euler's Totient**: φ(n) = (p-1)(q-1) for primes p, q
- **Key Relationship**: e × d ≡ 1 (mod φ(n))

## Key Points

- Public-key cryptography enables secure communication between parties without pre-shared secrets
- RSA security relies on the computational infeasibility of factoring large composite numbers
- Digital signatures verify sender identity and message integrity simultaneously
- Hash functions ensure efficiency (signing small hashes instead of large messages) and security
- PKI establishes trust through hierarchical Certificate Authorities
- Real-world systems use hybrid cryptography: public-key for key exchange, symmetric for bulk encryption
- Common key sizes: RSA 2048-bit (current minimum secure), 4096-bit for high security
- X.509 is the standard format for digital certificates

## Common Mistakes to Avoid

1. Confusing which key encrypts and which decrypts (public encrypts, private decrypts)
2. Thinking digital signatures encrypt the entire message (only the hash is signed)
3. Using small prime numbers in RSA (educationally fine, but insecure in practice)
4. Ignoring the importance of proper padding in RSA encryption
5. Believing hash functions provide confidentiality (they provide integrity only)

## Revision Tips

1. Practice RSA calculations with small numbers to understand the mathematical flow
2. Trace through a complete digital signature cycle: hash → sign → verify
3. Remember the three properties of digital signatures: authentication, integrity, non-repudiation
4. Know why hybrid systems are used (asymmetric slow, symmetric fast)
5. Review certificate verification steps in HTTPS connections