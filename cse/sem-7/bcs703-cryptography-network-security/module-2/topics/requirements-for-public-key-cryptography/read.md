# Requirements For Public Key Cryptography

## Introduction

Public key cryptography represents a fundamental paradigm shift in cryptographic systems, introducing the revolutionary concept of asymmetric key pairs consisting of a public key and a private key. Unlike symmetric cryptography where the same key serves both encryption and decryption, public key systems enable secure communication between parties who have never exchanged keys beforehand. The mathematical foundations of public key cryptography rely on computationally hard problems such as integer factorization and discrete logarithmation, which provide the security guarantees essential for modern cryptographic applications.

The requirements for public key cryptography establish the necessary conditions that any asymmetric cryptosystem must satisfy to be considered secure and practical for deployment. These requirements serve as design principles guiding the development of cryptographic algorithms and as evaluation criteria for assessing the security of existing systems. Understanding these requirements is crucial for security professionals, as they form the theoretical basis for protocols like RSA, Diffie-Hellman, and elliptic curve cryptography that protect billions of transactions daily across global networks.

This topic examines the six fundamental requirements that define a viable public key cryptosystem, exploring the mathematical formalizations and security proofs that underpin each requirement. The discussion connects these theoretical foundations to practical considerations in key generation, encryption, and digital signature schemes, with particular attention to how these requirements relate to the broader context of cryptographic network security.

## Key Concepts

### Requirement 1: Computational Ease of Key Generation

The first requirement mandates that the process of generating key pairs must be computationally efficient for legitimate users. Given a security parameter $n$ (typically representing the key length in bits), the key generation algorithm $\text{Gen}(1^n)$ must run in polynomial time bounded by $O(n^c)$ for some constant $c$. In the RSA cryptosystem, key generation involves selecting two large prime numbers $p$ and $q$, computing their product $n = pq$, and determining the Euler's totient function $\phi(n) = (p-1)(q-1)$. The selection of primes uses probabilistic primality testing algorithms such as the Miller-Rabin test, which runs in $O(k \log^3 n)$ time where $k$ represents the number of test iterations.

The efficiency requirement extends to all legitimate operations while maintaining security. Modern implementations achieve key generation times of under a second for 2048-bit RSA keys on commodity hardware, demonstrating that practical systems can satisfy this requirement without sacrificing security. However, the relationship between key size and security must be carefully balanced, as larger keys provide greater security but require more computational resources.

### Requirement 2: Computational Ease of Encryption and Decryption

A public key cryptosystem must enable the encryption of messages and the corresponding decryption process to proceed efficiently for authorized parties. Given the public key $pk$ and a plaintext message $m$, the encryption algorithm $\text{Enc}_{pk}(m)$ must compute the ciphertext $c$ in polynomial time. Similarly, given the private key $sk$ and ciphertext $c$, the decryption algorithm $\text{Dec}_{sk}(c)$ must recover the original message $m$ efficiently.

In RSA encryption, this requirement translates to modular exponentiation. Encryption computes $c = m^e \mod n$ where $(e, n)$ constitutes the public key, requiring $O(\log e \cdot \log^2 n)$ modular multiplications using efficient exponentiation algorithms. Decryption computes $m = c^d \mod n$ where $d$ represents the private exponent, satisfying $ed \equiv 1 \pmod{\phi(n)}$. The efficiency of these operations depends critically on the choice of exponent size and implementation optimizations such as Montgomery multiplication and windowed exponentiation techniques.

### Requirement 3: Computational Infeasibility of Deriving Private Key from Public Key

This requirement constitutes the foundational security assumption of public key cryptography. The private key $sk$ must be computationally infeasible to derive from the corresponding public key $pk$, even when the attacker has complete knowledge of the encryption algorithm, public key, and potentially examples of encrypted messages. Formally, for any probabilistic polynomial-time adversary $\mathcal{A}$, the probability of success in computing $sk$ from $pk$ must be negligible:

$$\Pr[\mathcal{A}(pk) = sk] \leq \epsilon(n)$$

where $\epsilon(n)$ represents a negligible function that vanishes faster than any inverse polynomial in $n$. In RSA, this requirement relies on the intractability of integer factorization—given $n = pq$ and $e$, computing the private exponent $d$ requires determining $\phi(n)$, which in turn requires factoring $n$ to recover $p$ and $q$. The security of RSA thus reduces to the hardness of the integer factorization problem.

### Requirement 4: Computational Infeasibility of Encryption without Private Key

An essential security requirement states that without access to the private key, it must be computationally infeasible to decrypt ciphertexts or compute plaintexts from encrypted data. Even when an attacker possesses the public key and arbitrary ciphertexts, they cannot recover the corresponding plaintexts within practical time bounds. This requirement ensures the semantic security of the cryptosystem against passive adversaries.

Formally, this requirement is captured by the indistinguishability under chosen plaintext attack (IND-CPA) security model. For any probabilistic polynomial-time adversary $\mathcal{A}$ distinguishing between encryptions of two messages $m_0$ and $m_1$, the advantage must be negligible:

$$\left|\Pr[\mathcal{A}(pk, \text{Enc}_{pk}(m_0)) = 1] - \Pr[\mathcal{A}(pk, \text{Enc}_{pk}(m_1)) = 1]\right| \leq \epsilon(n)$$

The RSA encryption scheme in its basic form (without padding) fails to satisfy this requirement due to its deterministic nature—identical plaintexts always produce identical ciphertexts, allowing trivial distinguishability attacks. This limitation necessitates the use of probabilistic padding schemes such as OAEP (Optimal Asymmetric Encryption Padding) to achieve IND-CPA security.

### Requirement 5: Bidirectional Communication Capability

Public key cryptosystems must support secure bidirectional communication, enabling both encryption and decryption operations in both directions using appropriate key pairs. This requirement ensures that party A can send encrypted messages to party B using B's public key, and party B can send encrypted messages to A using A's public key. Each direction utilizes distinct key pairs, maintaining the asymmetry fundamental to public key systems.

This requirement has significant implications for key management in large-scale systems. In a network of $n$ participants, each user must maintain only one private key and one public key, enabling communication with any other participant using their public key. This contrasts sharply with symmetric cryptography, which would require $n(n-1)/2$ secret keys for complete pairwise communication—a scaling problem that makes symmetric systems impractical for large networks. The bidirectional requirement thus enables the development of scalable key infrastructure essential for modern internet communications.

### Requirement 6: Digital Signature Capability

The final requirement establishes that public key systems must enable the generation and verification of digital signatures, providing authentication and non-repudiation services essential for secure electronic commerce and legal transactions. A digital signature scheme consists of three algorithms: $\text{Sign}_{sk}(m)$ produces a signature $\sigma$ on message $m$ using the private key, while $\text{Verify}_{pk}(m, \sigma)$ returns accept or reject based on the public key corresponding to the signing private key.

Digital signatures satisfy two critical security properties: existential unforgeability under chosen message attacks (EUF-CMA) and non-repudiation. Existential unforgeability ensures that an adversary cannot produce valid signatures on messages they have not previously requested, even when given access to a signing oracle that produces signatures on messages of the adversary's choice. Non-repudiation ensures that the signer cannot later deny having signed a particular message, as only the holder of the private key could have produced the valid signature.

RSA signatures utilize a different key usage convention than encryption: the private exponent $d$ signs while the public exponent $e$ verifies. However, naive RSA signatures suffer from existential forgery attacks, necessitating hash-based signature schemes such as RSA-PSS or standards like PKCS#1 v1.5 that incorporate randomization and cryptographic hash functions.

## Examples

### Example 1: RSA Key Generation Analysis

Consider RSA key generation with security parameter $n = 2048$ bits (1024-bit primes). The prime generation process selects random odd numbers of approximately 512 bits and tests them for primality using the Miller-Rabin test with approximately 40 iterations. The probability of incorrectly declaring a composite as prime is less than $2^{-80}$, providing overwhelming confidence in primality.

The complete key generation requires approximately $O(n^3)$ bit operations: generating primes costs $O(n^2 \log n)$ with probabilistic testing, computing $\phi(n)$ requires one multiplication of $n$-bit numbers in $O(n^2)$, and computing the modular inverse using the extended Euclidean algorithm requires $O(n^2)$ operations. On modern processors, 2048-bit RSA key generation completes in under 500 milliseconds, demonstrating that Requirement 1 is satisfied for practical deployment.

The security reduction from integer factorization requires careful analysis. The most efficient known factorization algorithm for 2048-bit numbers is the General Number Field Sieve (GNFS), which has sub-exponential complexity $L_n[1/3, (64/9)^{1/3}] \approx L_n[1/3, 1.923]$. For 2048-bit moduli, GNFS requires approximately $2^{80}$ operations, placing factoring beyond practical reach while encryption and decryption remain fast.

### Example 2: Security Reduction Analysis

To demonstrate Requirement 3 formally, we present a security reduction showing that breaking RSA key recovery is no harder than integer factorization. Suppose an adversary $\mathcal{A}$ exists that, given $(n, e)$, computes the private exponent $d$ in polynomial time. We show how to use $\mathcal{A}$ to factor $n$ efficiently.

Given $n = pq$ and $e$ with $ed \equiv 1 \pmod{\phi(n)}$, we know that $ed - 1 = k\phi(n)$ for some integer $k$. Since $\phi(n) = (p-1)(q-1)$, we have $ed - 1 = k(p-1)(q-1)$. The factorization algorithm proceeds by:

1. Randomly selecting $g \in \mathbb{Z}_n^*$
2. Computing $x = g^{(ed-1)/2} \mod n$ (using the square root of $ed-1$ modulo $\phi(n)$)
3. Computing $\gcd(x-1, n)$

With non-negligible probability over random choices of $g$, this procedure yields a non-trivial factor of $n$. This reduction establishes that breaking RSA key generation is polynomially equivalent to integer factorization, formally justifying Requirement 3 under the integer factorization assumption.

### Example 3: Application to Key Exchange Protocols

The requirements for public key cryptography find direct application in Diffie-Hellman key exchange, which enables two parties to establish a shared secret over an insecure channel without prior key exchange. The protocol operates in a cyclic group $\mathbb{G}$ of prime order $q$ with generator $g$.

Party A selects private key $a \in \mathbb{Z}_q$ and computes public key $A = g^a$. Party B selects private key $b \in \mathbb{Z}_q$ and computes public key $B = g^b$. Both parties exchange their public keys and compute the shared secret: A computes $B^a = g^{ab}$, and B computes $A^b = g^{ab}$. The security relies on the computational Diffie-Hellman (CDH) assumption: given $(g, g^a, g^b)$, computing $g^{ab}$ is computationally infeasible.

This protocol satisfies all six requirements: efficient key generation (random exponentiation), efficient computation of public keys and shared secret, infeasibility of deriving private keys from public keys (discrete logarithm assumption), infeasibility of computing the shared secret without private keys (CDH assumption), bidirectional capability, and applicability to digital signatures through the ElGamal signature scheme.

## Exam Tips

1. **Memorize all six requirements** in order and be prepared to explain each with mathematical formalization. Examiners frequently ask for enumeration of the requirements with brief explanations of each.

2. **Understand the security reductions** connecting Requirements 3 and 4 to fundamental cryptographic assumptions (integer factorization, discrete logarithm). Know the formal definitions of negligible functions and polynomial-time adversaries.

3. **Differentiate between encryption and signature key usage** in RSA—remember that the private exponent signs while the public exponent verifies, which is opposite to encryption convention.

4. **Recognize why deterministic encryption fails** Requirement 4 and understand how probabilistic padding schemes (OAEP, PSS) address this vulnerability to achieve IND-CPA security.

5. **Connect requirements to practical protocols** such as TLS/SSL, where these requirements enable secure web communications, digital signatures for code signing, and key exchange for session establishment.

6. **Analyze trade-offs between key size and security**—larger keys satisfy computational infeasibility requirements but increase computational overhead. The current recommendation of 2048-bit RSA or 256-bit elliptic curve keys balances these considerations.

7. **Apply requirements to scheme analysis** when evaluating whether a given cryptographic scheme satisfies the requirements. For instance, explain why raw RSA without padding fails to satisfy semantic security.
