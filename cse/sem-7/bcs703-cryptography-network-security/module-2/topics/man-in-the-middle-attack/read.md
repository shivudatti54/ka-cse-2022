# Man In The Middle Attack

## Introduction

A Man In The Middle (MITM) attack represents one of the most fundamental and consequential threats in cryptographic network security. In this attack, an adversary positions themselves between two communicating parties, intercepting and potentially altering the communications without the legitimate parties being aware of the intrusion. The attack exploits the fundamental assumption that communication channels are secure and that the parties at each end of a communication are who they claim to be.

The relevance of MITM attacks to the study of Pseudorandom Number Generators (PRNGs) cannot be overstated. The security of key exchange protocols—including the Diffie-Hellman key exchange—fundamentally depends on the cryptographic strength of the random numbers used to generate session keys. When a PRNG produces predictable or biased output, an attacker can potentially determine or predict the key material, thereby facilitating a MITM attack. Weak PRNGs compromise the foundational randomness required to establish secure communication channels, making MITM attacks not only possible but often trivial to execute. This module examines the MITM attack mechanism, its intricate relationship with PRNG quality, and the mathematical foundations underlying its exploitability in unauthenticated key exchange protocols.

## Key Concepts

### Formal Definition of MITM Attack

A Man In The Middle attack is formally defined as an active eavesdropping attack where the attacker independently establishes separate connections with the victims and relays messages between them, making them believe they are communicating directly with each other when in fact the entire conversation is controlled by the attacker. In cryptographic terms, given two honest parties Alice and Bob attempting to establish a shared secret key, a MITM attacker Eve interposes herself in the protocol execution, completing separate protocol runs with both Alice and Bob while convincing each party that they are communicating with the legitimate peer.

**Definition:** Let Π be a key exchange protocol executed between parties A and B. A MITM adversary E succeeds if E can persuade A to accept a key K₁ and B to accept a key K₂ such that K₁ ≠ K₂, while E obtains both K₁ and K₂ (or can compute them). The attack is successful when A and B believe they share a common key, but in reality, E possesses the capability to decrypt, modify, and re-encrypt all communications.

### The Relationship Between PRNG Weakness and MITM Vulnerability

The security of modern key exchange protocols relies critically on the computational infeasibility of computing discrete logarithms or factoring large composite numbers. However, this security assumption becomes meaningless if the random numbers used in key generation are predictable. The connection between PRNG weakness and MITM vulnerability operates through several critical pathways:

**Insufficient Entropy:** When a PRNG lacks adequate entropy sources during initialization, the resulting random sequence may be predictable. In the context of key exchange, if an attacker can predict or narrow down the possible values of the random exponent used in Diffie-Hellman, the attacker can compute the session key with reduced computational effort.

**State Compromise:** A cryptographically weak PRNG may allow an attacker to recover internal state from observed outputs. Once the PRNG state is compromised, all future and potentially past random numbers become predictable. In key exchange protocols, compromised random exponents render the entire key exchange vulnerable to MITM.

**Bias Exploitation:** Weak PRNGs may exhibit statistical biases that reduce the effective key space. An attacker performing a MITM attack need only search the reduced key space, making brute-force recovery feasible where it should not be.

### Mathematical Vulnerability in Unauthenticated Diffie-Hellman

The Diffie-Hellman key exchange protocol provides a canonical example of a protocol vulnerable to MITM attacks when proper authentication is absent. Consider the protocol specification:

1. Alice and Bob agree on a large prime p and a primitive root g modulo p
2. Alice selects private key a ∈ ℤₚ₋₁ and computes public key A = gᵃ mod p
3. Bob selects private key b ∈ ℤₚ₋₁ and computes public key B = gᵇ mod p
4. Alice computes shared secret K_A = Bᵃ mod p = gᵃᵇ mod p
5. Bob computes shared secret K_B = Aᵇ mod p = gᵃᵇ mod p

**Theorem (MITM Vulnerability):** In the absence of authentication, an active adversary E can compute distinct shared secrets with Alice and Bob.

_Proof:_ E intercepts Alice's public key A and replaces it with E's public key E_A = gᵉ mod p, where e is E's private exponent. Similarly, when Bob sends public key B, E replaces it with E_B = gᵉ mod p. Alice computes K_A = (E_B)ᵃ = gᵉᵃ mod p, while Bob computes K_B = (E_A)ᵇ = gᵉᵇ mod p. Both parties believe they share a key with each other, but E possesses e, a, and b (having generated e and intercepted a and b through the modified public keys), allowing computation of both gᵉᵃ and gᵉᵇ. ∎

### Countermeasures and the Role of Strong PRNGs

**Digital Certificates and Public Key Infrastructure (PKI):** The primary defense against MITM attacks involves authenticating the communicating parties' public keys through trusted certificate authorities. X.509 certificates bind identity information to public keys, allowing verification that the received public key genuinely belongs to the claimed party.

**Authenticated Key Exchange Protocols:** Protocols such as Station-to-Station (STS) and HMQV incorporate mutual authentication using digital signatures or message authentication codes. These protocols ensure that even if an attacker intercepts and modifies the key exchange messages, the parties can detect the tampering.

**Strong PRNG Requirements:** For key exchange security, the PRNG must satisfy:

- **Forward Secrecy:** Compromise of long-term keys does not reveal past session keys
- **High Entropy Collection:** Adequate entropy from multiple sources during seeding
- **Unpredictability:** No polynomial-time algorithm can predict the next output with probability significantly better than random guessing
- **State Separation:** Proper isolation of PRNG state across different security contexts

## Examples

### Example 1: Diffie-Hellman MITM Attack with Numerical Values

Consider a simplified Diffie-Hellman with small parameters for illustration (not for actual use):

**Setup:** Let p = 23 and g = 5 (primitive root modulo 23)

**Normal Protocol:**

- Alice selects a = 6, computes A = 5⁶ mod 23 = 8
- Bob selects b = 15, computes B = 5¹⁵ mod 23 = 19
- Alice computes K = 19⁶ mod 23 = 2
- Bob computes K = 8¹⁵ mod 23 = 2

**MITM Attack:**

- Eve intercepts and replaces A = 8 with E_A = 5ᵉ mod 23 (choose e = 3, so E_A = 10)
- Eve intercepts and replaces B = 19 with E_B = 10 (her public key sent to Bob)
- Alice computes K_A = 10⁶ mod 23 = 3
- Bob computes K_B = 10¹⁵ mod 23 = 6
- Eve computes shared secret with Alice: 8³ mod 23 = 3
- Eve computes shared secret with Bob: 19³ mod 23 = 6

Alice and Bob believe they share secrets 3 and 6 respectively, while Eve knows both.

### Example 2: PRNG Weakness Enabling Simplified MITM

Consider a weak PRNG with reduced entropy producing only 16-bit random exponents in a 1024-bit Diffie-Hellman exchange:

**Scenario:** Instead of searching a 1024-bit space, an attacker need only search 2¹⁶ = 65,536 possible exponents. The effective security collapses from 2¹⁰²⁴ operations to 2¹⁶ operations—a trivial computation on modern hardware. The MITM attacker can:

1. Intercept the public key
2. Compute the possible shared secrets for all 65,536 exponent candidates
3. Identify the actual shared secret by testing which candidate produces valid communication patterns

This demonstrates how PRNG weakness transforms an apparently secure protocol into one vulnerable to practical MITM attacks.

### Example 3: Certificate-Based Authentication Prevention

In a properly authenticated key exchange using certificates:

1. Alice obtains Bob's certificate from a trusted CA, containing Bob's public key and identity
2. Bob obtains Alice's certificate similarly
3. During key exchange, each party signs their public key using their private key
4. The signature is verified using the peer's certificate public key

Even if Eve interposes and signs her own public keys with her private key, the signatures cannot be verified because Eve cannot produce valid signatures verifiable by the certificates issued to Alice and Bob. The CA's digital signature on each certificate provides the authentic binding between identity and public key, preventing the MITM attack.

## Exam Tips

1. **Understand the fundamental vulnerability:** MITM attacks exploit the absence of authentication in key exchange protocols. Always explain why unauthenticated protocols are vulnerable.

2. **Connect PRNG weakness to attack feasibility:** Be prepared to explain how predictable random numbers reduce the security of key exchange, enabling or simplifying MITM attacks.

3. **Remember the formal proof structure:** When proving MITM vulnerability in Diffie-Hellman, explicitly show how the attacker replaces both public keys and computes both shared secrets independently.

4. **Know the three essential countermeasures:** Digital certificates/PKI, authenticated key exchange protocols, and strong PRNGs with adequate entropy.

5. **Distinguish passive vs. active attacks:** Eavesdropping is passive MITM (only interception), while message modification is active MITM (interception and alteration).

6. **Understand forward secrecy:** Explain how strong PRNGs that generate ephemeral keys for each session provide forward secrecy, limiting the damage of long-term key compromise.

7. **Apply to RSA key exchange:** Note that RSA key exchange without authentication (sending the pre-master secret encrypted with the recipient's public key) is equally vulnerable to MITM attacks.

8. **Quantify PRNG impact:** Be prepared to calculate how reduced entropy (e.g., 16-bit vs. 256-bit exponents) affects attack complexity.
