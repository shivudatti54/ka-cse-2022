# Applications of Cryptographic Hash Functions

=====================================

### Overview

Cryptographic hash functions take an arbitrary-length input and produce a fixed-size digest that acts as a digital fingerprint. They are fundamental building blocks used in data integrity verification, password storage, digital signatures, and blockchain technology, relying on properties like pre-image resistance and collision resistance.

### Key Points

- **Hash Function:** Maps arbitrary-length input to a fixed-size output (message digest)
- **Pre-image Resistance:** Given hash h, infeasible to find any input m such that hash(m) = h
- **Second Pre-image Resistance:** Given m1, infeasible to find m2 where hash(m1) = hash(m2)
- **Collision Resistance:** Infeasible to find any two distinct inputs producing the same hash
- **Avalanche Effect:** A single-bit change in input produces a drastically different output
- **Merkle-Damgard Construction:** Iterative structure using IV, padding, and compression function H*i = f(H*{i-1}, M_i)
- **MD5 (128-bit):** Broken -- vulnerable to collisions; not suitable for security
- **SHA-1 (160-bit):** Broken -- being phased out due to collision vulnerabilities
- **SHA-2 (256/512-bit):** Secure and widely used (includes SHA-256, SHA-512)
- **SHA-3:** Secure; uses Keccak sponge construction instead of Merkle-Damgard

### Important Concepts

- Data Integrity: Compute and compare hash digests to detect file tampering
- Password Storage: Store hash(password + salt), never store plaintext passwords; salting prevents rainbow table attacks
- Digital Signatures: Sign hash(message) with private key for efficiency instead of signing the entire message
- Blockchain: Hash links blocks together; each block contains hash of the previous block
- Hashing is one-way (irreversible); Encryption is two-way (reversible with a key)

### Notes

- Memorize all three resistance properties with clear definitions -- frequently tested
- Always mention salting when discussing password hashing in exams
- Know that MD5 and SHA-1 are broken; SHA-256 is the current standard
- Be ready to differentiate hashing (one-way, no key) from encryption (two-way, requires key)
