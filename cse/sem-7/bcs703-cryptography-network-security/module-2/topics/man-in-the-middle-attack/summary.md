# Man In The Middle Attack - Summary

## Key Definitions

- **Man In The Middle (MITM) Attack**: An attack where an adversary intercepts, alters, and relays communications between two parties who believe they are communicating directly with each other

- **Key Exchange Protocol**: A cryptographic protocol enabling two or more parties to establish a shared secret key over an insecure channel

- **Public Key Substitution**: Attack where an attacker replaces the legitimate public key with their own, allowing decryption of encrypted communications

- **Active MITM**: Attack where the adversary actively modifies, deletes, or injects new messages into the communication stream

- **Passive MITM**: Attack where the adversary only observes communications without altering them

## Important Formulas

- **Diffie-Hellman Shared Secret**: S = g^(ab) mod p
- **MITM Compromised Secret (Alice-Eve)**: S₁ = B^e mod p (where B is Bob's public value, e is Eve's private key)
- **MITM Compromised Secret (Bob-Eve)**: S₂ = A^e mod p (where A is Alice's public value)

## Key Points

1. MITM attacks exploit the lack of authentication in key exchange protocols, particularly when parties cannot verify each other's identity

2. The fundamental vulnerability is that public keys can be intercepted and replaced without detection if no authentication mechanism exists

3. In Diffie-Hellman exchange, Eve establishes two separate shared secrets—one with Alice and one with Bob—allowing her to decrypt and re-encrypt all communications

4. Weak pseudorandom number generators compromise key exchange security by making cryptographic keys predictable

5. SSL stripping attacks downgrade HTTPS connections to HTTP, enabling plaintext interception

6. Countermeasures include: digital signatures, certificate authorities, pre-shared keys, and authenticated key exchange protocols

7. The PKI (Public Key Infrastructure) with certificate authorities is the primary defense against MITM attacks in modern internet communications

8. Perfect Forward Secrecy (PFS) ensures that compromising one session key does not compromise past sessions

## Common Mistakes

1. **Confusing interception with MITM**: Simply capturing traffic is not MITM; the attack requires active relay and deception of both parties

2. **Assuming encryption alone prevents MITM**: Without authentication, encryption keys can be intercepted and substituted

3. **Neglecting PRNG security**: Many students focus on protocol design but forget that weak random number generation undermines the entire security

4. **Forgetting endpoint verification**: Having secure channel establishment is useless if the endpoint identity cannot be verified