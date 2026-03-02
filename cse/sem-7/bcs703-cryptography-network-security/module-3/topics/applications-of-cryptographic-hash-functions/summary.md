# Applications of Cryptographic Hash Functions - Summary

## Key Definitions

- **Digital Signature**: A cryptographic scheme providing authentication, integrity, and non-repudiation by encrypting a message hash with the sender's private key.

- **HMAC (Hash-based Message Authentication Code)**: A mechanism for message authentication using a cryptographic hash function and a secret key, following the construction HMAC(K, M) = H((K ⊕ opad) || H((K ⊕ ipad) || M)).

- **Salt**: A random value added to password hashing to ensure identical passwords produce different hashes for different users, defeating rainbow table attacks.

- **Commitment Scheme**: A cryptographic primitive allowing one party to commit to a value while keeping it hidden, later revealing it with proof of the original commitment.

- **Proof of Work**: A consensus mechanism requiring computational effort (finding hash with specific properties) to validate transactions and create new blocks in blockchain systems.

## Important Formulas

- **Digital Signature**: Signature = E_private_key(H(Message)); Verification: H(Message) =?= D_public_key(Signature)

- **HMAC Construction**: HMAC(K, M) = H((K ⊕ opad) || H((K ⊕ ipad) || M)) where ipad = 0x36, opad = 0x5C (repeated to block length)

- **Birthday Attack Complexity**: Approximately 2^(n/2) operations to find collision in n-bit hash function

- **Key Derivation**: Stored password = H(salt || password) processed through iterative function (e.g., PBKDF2 with 60,000+ iterations)

## Key Points

1. Hash functions reduce arbitrary-length messages to fixed-length digests, enabling efficient digital signatures on large documents.

2. Collision resistance is essential for digital signatures—finding two messages with identical hashes would allow signature forgery.

3. Password storage requires pre-image resistance; even with stolen hash and salt, attackers cannot recover original passwords efficiently.

4. Salt must be unique per user and randomly generated to prevent pre-computed attack tables.

5. HMAC remains secure even if the underlying hash function's collision properties are compromised, due to its key-based construction.

6. Hash chains (applying hash repeatedly) are used in cryptocurrencies and one-time password systems for forward security.

7. Merkle trees use hash functions to efficiently verify large data sets by storing only root hash values.

8. SHA-256 and SHA-512 are currently recommended standards; MD5 and SHA-1 are cryptographically broken.

## Common Mistakes

1. **Confusing hash with encryption**: Hash functions are one-way and irreversible; they do not encrypt data for later decryption.

2. **Ignoring salt in password hashing**: Using identical salt or no salt enables rainbow table attacks that can compromise entire password databases.

3. **Underestimating birthday attacks**: Assuming 2^n security for n-bit hash when only 2^(n/2) is actually required for collision finding.

4. **Using wrong hash for application**: Selecting MD5 for security-critical applications when it's known to be broken for collision resistance.

5. **Believing hash alone provides authentication**: Hashes verify integrity but not source; MAC and digital signatures add authentication through secret keys or private keys.