# Diffie-Hellman Key Exchange

## Introduction

Diffie-Hellman key exchange, introduced by Whitfield Diffie and Martin Hellman in 1976, represents a groundbreaking breakthrough in cryptography as the first practical method for establishing a shared secret over an insecure communication channel without relying on prior shared information. This protocol enables two parties who have never met to derive a common secret key that can subsequently be used for symmetric encryption, thereby solving one of the fundamental challenges in classical cryptography: the key distribution problem. The innovation lies in its elegant utilization of the one-way function property of modular exponentiation, making it computationally infeasible for an eavesdropper to determine the shared secret even when observing all public communications.

The Diffie-Hellman protocol holds particular significance within the broader context of Cryptography and Network Security, forming the foundation for numerous key exchange mechanisms in modern secure communication protocols including TLS/SSL, SSH, and IPsec. While the module focuses on Pseudorandom Number Generators (PRNGs), Diffie-Hellman establishes a direct connection: the shared secret derived from the protocol can serve as a seed for cryptographic PRNGs, enabling the generation of deterministic yet unpredictable keystreams. The security of Diffie-Hellman rests upon the computational intractability of the Discrete Logarithm Problem (DLP), which remains unbroken for appropriately chosen parameters, making it a cornerstone of contemporary cryptographic systems.

## Key Concepts

### The Discrete Logarithm Problem

The security of Diffie-Hellman rests upon the mathematical hardness of the Discrete Logarithm Problem. Given a prime modulus $p$, a generator $g$ of the multiplicative group $\mathbb{Z}_p^*$, and a value $y = g^x \pmod p$, the problem of determining $x$ is computationally infeasible for sufficiently large primes $p$ (typically 2048 bits or more). Formally, the DLP states: given $(p, g, y)$, find $x$ such that $g^x \equiv y \pmod p$. The best-known algorithms for solving DLP include Pollard's rho algorithm (with complexity $O(\sqrt{n})$) and the Index Calculus method (sub-exponential complexity), both of which remain computationally prohibitive for properly chosen parameters.

### The Decisional Diffie-Hellman Assumption

Beyond the DLP, the security of Diffie-Hellman relies on the Decisional Diffie-Hellman (DDH) assumption, which states that given $(g^a, g^b, g^c)$, it is computationally infeasible to distinguish whether $c = ab \pmod p$ (meaning the triple represents a valid DH exchange) or whether $c$ is randomly chosen from $\mathbb{Z}_p^*$. The DDH assumption implies the hardness of DLP, though the converse is not proven. This assumption is essential for the semantic security of DH-based encryption schemes.

### Protocol Parameters

The protocol requires carefully chosen public parameters: a large prime $p$ (the field modulus), and a generator $g$ of the multiplicative subgroup of order $q$, where $q$ is also prime. For optimal security, $p$ should be a "safe prime" of the form $p = 2q + 1$ where $q$ is prime, ensuring that $g$ generates a large-order subgroup. The generator $g$ must satisfy $g^q \equiv 1 \pmod p$ and $g \not\equiv 1 \pmod p$, preventing attacks based on small subgroups.

### Complete Protocol Description

The protocol operates as follows:

**Step 1 - Parameter Agreement**: Alice and Bob agree on public parameters $(p, g)$ where $p$ is a large prime and $g$ is a generator of $\mathbb{Z}_p^*$.

**Step 2 - Private Key Generation**:

- Alice selects a private key $a \in \{1, 2, ..., p-2\}$ randomly
- Bob selects a private key $b \in \{1, 2, ..., p-2\}$ randomly

**Step 3 - Public Key Computation**:

- Alice computes $A = g^a \pmod p$ and sends $A$ to Bob
- Bob computes $B = g^b \pmod p$ and sends $B$ to Alice

**Step 4 - Shared Secret Computation**:

- Alice computes $K = B^a \pmod p = (g^b)^a = g^{ab} \pmod p$
- Bob computes $K = A^b \pmod p = (g^a)^b = g^{ab} \pmod p$

Both parties arrive at the identical shared secret $K = g^{ab} \pmod p$, which can then be used as a symmetric encryption key.

### Numerical Example

Let $p = 23$ and $g = 5$ (generator of $\mathbb{Z}_{23}^*$):

- Alice selects $a = 6$, computes $A = 5^6 \mod 23 = 8$
- Bob selects $b = 15$, computes $B = 5^{15} \mod 23 = 19$

- Alice receives $B = 19$, computes $K = 19^6 \mod 23 = 2$
- Bob receives $A = 8$, computes $K = 8^{15} \mod 23 = 2$

Shared secret $K = 2$.

## Security Analysis

### Man-in-the-Middle Attack

The basic Diffie-Hellman protocol is vulnerable to an active man-in-the-middle (MITM) attack where an adversary intercepts and modifies communications between Alice and Bob. The attacker, positioned between them, establishes separate DH exchanges with each party: one with Alice pretending to be Bob, and another with Bob pretending to be Alice. Both parties believe they share a secret with each other, but actually share distinct secrets with the attacker. The attacker can then decrypt, modify, and re-encrypt all communications. Mitigation requires authentication mechanisms such as digital signatures or certificates to verify the identities of the communicating parties.

### Forward Secrecy

Diffie-Hellman provides perfect forward secrecy (PFS) when fresh random values are used for each session, meaning that compromise of long-term keys does not retroactively compromise past session keys. This property makes ephemeral Diffie-Hellman (DHE or ECDHE) preferred in modern protocols.

### Parameter Selection Security

Incorrect parameter selection can catastrophically weaken the protocol. Using small primes allows efficient Index Calculus attacks; non-prime orders enable the Pohlig-Hellman attack; weak generators may result in small subgroups susceptible to discrete log attacks. Industry standards (RFC 7919, NIST SP 800-56A) provide vetted parameter sets.

## Examples

### Example 1: Application-Level MCQ

Given Diffie-Hellman parameters $p = 47$, $g = 5$, Alice's public value $A = 17$, and Bob's public value $B = 37$, what is the shared secret?

Solution: Alice computes $K = B^a \mod 47 = 37^a \mod 47$. Without knowing private keys, we cannot compute directly. However, if we know Alice's private key $a = 8$ (where $5^8 \equiv 17 \mod 47$), then $K = 37^8 \mod 47 = 14$.

### Example 2: Identifying MITM Attack

In a Diffie-Hellman exchange, if Alice computes shared secret $K_A$ and Bob computes shared secret $K_B$ where $K_A \neq K_B$, and neither party can detect the discrepancy without authentication, this indicates:

- (a) Implementation error
- (b) Man-in-the-Middle attack
- (c) Discrete logarithm compromise
- (d) Incorrect parameter selection

Answer: (b) Man-in-the-Middle attack. Without authentication, both parties believe they share a secret with each other while actually sharing different secrets with the attacker.

### Example 3: Parameter Strength Analysis

Which of the following Diffie-Hellman parameter choices provides the LEAST security?

- (a) $p$ = 2048-bit safe prime, $g$ generates prime-order subgroup
- (b) $p$ = 1024-bit safe prime, $g$ generates prime-order subgroup
- (c) $p$ = 2048-bit prime, $g$ = 2 (small subgroup)
- (c) is correct because small generators may generate small-order subgroups, enabling the Pohlig-Hellman attack regardless of prime size.

## Exam Tips

1. Understand the mathematical foundation: Diffie-Hellman security derives from the one-way nature of modular exponentiation and the hardness of the Discrete Logarithm Problem.

2. Remember the complete protocol flow: Parameter agreement → Private key generation → Public key exchange → Shared secret computation.

3. Be able to work through numerical examples with small primes to verify understanding of modular arithmetic.

4. Know the difference between DLP hardness and DDH assumption—the former is a computational problem, the latter is an indistinguishability assumption.

5. Always mention authentication when discussing MITM attacks—basic DH provides no authentication inherently.

6. Understand why ephemeral versions (DHE/ECDHE) provide forward secrecy while static DH does not.

7. Recognize that parameter selection is critical: safe primes, appropriate generators, and sufficient key sizes (minimum 2048 bits for classical DH) are essential for security.

8. Connect the topic to the module: the shared secret from DH can seed Pseudorandom Number Generators for symmetric encryption.
