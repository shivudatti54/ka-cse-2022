# Message Authentication and Hash Functions - Summary

## Key Definitions and Concepts

- **Message Authentication Code (MAC)**: A cryptographic tag computed using a message and a secret key, allowing verification of integrity and authenticity

- **Cryptographic Hash Function**: A one-way function producing a fixed-length digest from arbitrary-length input, with properties of pre-image, second pre-image, and collision resistance

- **HMAC**: Hash-based Message Authentication Code using a secret key and hash function (typically SHA-256) in a nested structure

- **Digital Signature**: Asymmetric cryptographic scheme providing authentication and non-repudiation using private/public key pairs

## Important Formulas and Theorems

- **HMAC Definition**: HMAC(K, m) = H((K ⊕ opad) || H((K ⊕ ipad) || m))

- **Birthday Attack Complexity**: Finding a collision requires approximately 2^(n/2) attempts for an n-bit hash output

- **Merkle-Damgård Construction**: Hash function structure using a compression function to process fixed-size blocks sequentially

## Key Points

- MACs require shared secret keys; without the key, an attacker cannot forge valid authentication tags

- Hash functions must produce outputs large enough to resist birthday attacks (minimum 128 bits, preferably 256+)

- MD5 and SHA-1 are considered broken due to practical collision attacks; SHA-256 and SHA-3 remain secure

- HMAC remains secure even if the underlying hash function's collision resistance is compromised (has provable security)

- Digital signatures provide non-repudiation (sender cannot deny signing) unlike MACs

- Real-world applications include file integrity checking, password storage, blockchain proof-of-work, and TLS/SSL protocols

## Common Mistakes to Avoid

- Confusing hashing with encryption: hash functions are one-way and cannot be reversed

- Thinking hash provides authentication: anyone can compute a hash; you need a MAC (secret key) for authentication

- Using weak hash functions like MD5 or SHA-1 for security-critical applications

- Ignoring the birthday attack: always consider 2^(n/2) complexity, not 2^n

## Revision Tips

- Focus on understanding why certain properties exist rather than memorizing definitions

- Practice computing simple examples by hand for smaller hash functions to build intuition

- Review the progression of hash function standards and why older ones were deprecated

- Memorize the birthday attack formula and its security implications for different hash lengths