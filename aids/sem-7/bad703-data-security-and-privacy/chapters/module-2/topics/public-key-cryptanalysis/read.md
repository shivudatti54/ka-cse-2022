# Public Key Cryptanalysis

## Introduction

Public key cryptography revolutionized secure communication by introducing asymmetric cryptographic systems where the encryption key is publicly available while the decryption key remains secret. However, the security of these systems is not absolute, and understanding how attackers attempt to break them is crucial for any computer science student. Public key cryptanalysis is the study of methods for defeating cryptographic techniques, specifically those involving public key algorithms like RSA, Diffie-Hellman, and Elliptic Curve Cryptography.

The importance of cryptanalysis extends beyond merely breaking encryption—it helps us understand the limits of our cryptographic systems and guides the development of more secure algorithms. In the context of the University of Delhi's Computer Science curriculum, understanding cryptanalytic attacks on RSA and other public key systems is essential for comprehending why certain cryptographic parameters are chosen and what vulnerabilities exist in practice. The famous quote by Kerckhoffs states that a cryptographic system should be secure even if everything about it is known except the key—this principle directly relates to why we study cryptanalysis: to ensure our systems remain secure even when attackers know the algorithm.

Modern cryptanalysis has evolved significantly since the invention of RSA in 1977. What was once considered computationally infeasible may become practical as mathematical discoveries and computing power advance. This makes the study of cryptanalysis not just an academic exercise but a practical necessity for anyone working in cybersecurity or cryptography.

## Key Concepts

### Mathematical Attacks on RSA

The security of RSA fundamentally relies on the computational difficulty of factoring large composite numbers into their prime factors. When the modulus n = p × q is factored, an attacker can compute the private exponent d from the public exponent e, completely breaking the system.

**Factorization Methods:** Several factorization algorithms exist, each with different time complexities. The basic trial division is impractical for large numbers, but more sophisticated methods pose real threats:

- **Pollard's Rho Algorithm**: Uses Floyd's cycle detection with polynomial time complexity O(√p) where p is the smaller prime factor
- **Quadratic Sieve**: Effective for numbers up to approximately 100 digits
- **General Number Field Sieve (GNFS)**: The fastest known algorithm for factoring numbers larger than 100 digits, with sub-exponential complexity

**Timing Attacks:** These are side-channel attacks that exploit variations in computation time. In RSA, the private key operation involves modular exponentiation where the time taken depends on the key bits. An attacker measuring response times can deduce the private key. Specifically, the Montgomery ladder implementation helps resist such attacks by ensuring consistent operation time regardless of key bits.

### Chosen Ciphertext Attacks

**Adaptive Chosen Ciphertext Attack (CCA2):** In this sophisticated attack, an attacker can obtain decryptions of chosen ciphertexts, but each decryption query may depend on the results of previous queries. RSA in its basic form (without padding) is vulnerable to such attacks. The seminal work of Bleichenbacher demonstrated practical CCA attacks against SSL/TLS implementations using PKCS#1 v1.5 padding.

**Manger's Attack:** This attack exploits the specific format of PKCS#1 v1.5 padding, allowing an attacker to decrypt a single ciphertext by making carefully chosen decryption oracle queries.

### Attacks on RSA with Low Exponents

**Hastad's Broadcast Attack:** When the same message is encrypted to multiple recipients using the same public exponent e (typically e = 3) with different moduli, the Chinese Remainder Theorem allows recovery of the plaintext if enough ciphertexts are available. If an attacker obtains e ciphertexts of the same message, they can recover m using CRT even without knowing any private keys.

**Coppersmith's Theorem:** This fundamental result shows that given the lower half of the bits of the root of a polynomial modulo n, one can recover the entire root efficiently. This has profound implications—it shows that encrypting related messages with low exponents can be dangerous.

### Wiener's Attack

Wiener's attack exploits small private exponents d. When d < n^0.25, the continued fraction approximation allows recovery of d from the public parameters (n, e). This is because the inequality d × e ≡ 1 (mod φ(n)) leads to a small denominator in the fraction e/φ(n), allowing approximation techniques. The defense is to ensure d is sufficiently large (typically d > n^0.25).

### Common Modulus Attacks

If the same modulus n is used for multiple users with different key pairs (n, e1, d1) and (n, e2, d2), and gcd(e1, e2) = 1, an attacker can recover the plaintext from ciphertexts intended for different recipients. This attack demonstrates why each user should have unique moduli.

### Brute Force and Dictionary Attacks

While not a mathematical cryptanalysis per se, brute force attacks on weak keys remain relevant. If the message space is small (like a password encrypted with RSA), attackers can simply encrypt all possible messages and compare with the ciphertext. This is why proper padding (OAEP) and message randomization are essential.

## Examples

### Example 1: Hastad's Broadcast Attack

**Problem:** Suppose a message m is encrypted with e = 3 for three different recipients with moduli n1, n2, n3. The ciphertexts are c1 = m^3 mod n1, c2 = m^3 mod n2, c3 = m^3 mod n3. Show how to recover m.

**Solution:**

Since m^3 < n1 × n2 × n3 (typically true for small messages), we can reconstruct m^3 exactly using the Chinese Remainder Theorem:

1. Compute M = n1 × n2 × n3
2. Find integers M1 = M/n1, M2 = M/n2, M3 = M/n3
3. Compute inverses: y1 = M1^(-1) mod n1, y2 = M2^(-1) mod n2, y3 = M3^(-1) mod n3
4. Compute C = c1 × M1 × y1 + c2 × M2 × y2 + c3 × M3 × y3 mod M

Now C = m^3 exactly (not just modulo any ni). The cube root of C gives m directly.

### Example 2: Timing Attack Demonstration

**Problem:** Explain conceptually how a timing attack works on RSA signature generation.

**Solution:**

During modular exponentiation using square-and-multiply, the operation takes longer when a '1' bit is processed (due to multiplication) versus a '0' bit (squaring only). By measuring the time taken for many signature operations, an attacker can statistically determine each bit of the private key:

1. Send many messages to be signed
2. Measure response times T1, T2, ..., Tn
3. For each bit position, analyze whether the operation was slower when that bit was processed
4. Reconstruct the private key bit by bit

**Countermeasure:** Use constant-time algorithms or Montgomery ladder that performs the same operations regardless of key bits.

### Example 3: Wiener's Attack

**Problem:** Given n = 323, e = 67, show that Wiener's attack can recover d.

**Solution:**

First, find the continued fraction expansion of e/n = 67/323:

67/323 = [0; 4, 1, 5, 1, 1]

Convergents:
- 0/1
- 1/4 → 1/4
- 1/(4+1/1) = 1/5 → 1/5
- 1/(4+1/(1+1/5)) = 6/29 → 6/29
- 7/34 → 7/34

Check each convergent k/d for whether d × e ≡ 1 (mod φ(n)).

For 7/34: d = 34
Check: 34 × 67 = 2278
We need to find n - φ(n): 323 - 34 × e = 323 - 2278 = -1955, which doesn't yield integer.

For 1/4: d = 4
Check: 4 × 67 = 268
φ(n) would be approximately n - 268/4 = 323 - 67 = 256
n - φ(n) = 323 - 256 = 67

Actually, let's find φ(n) directly. Since n = 17 × 19 = 323, φ(n) = 16 × 18 = 288
Check: 67 × 34 = 2278 ≡ 1 (mod 288) since 2278 - 1 = 2277 = 288 × 7 + 281

So d = 34 is the private key. Wiener's attack successfully recovered it.

## Exam Tips

1. **Understanding vs. Memorization**: For DU exams, understand the conceptual basis of each attack rather than memorizing formulas. Questions often ask to explain an attack or propose defenses.

2. **Key Parameters**: Remember that RSA security requires: large key sizes (2048+ bits), appropriate public exponent (typically 65537), and private exponent d > n^0.25 to resist Wiener's attack.

3. **Padding Importance**: Be prepared to explain why raw RSA is never used in practice. Understand that PKCS#1 padding and OAEP provide semantic security and prevent chosen ciphertext attacks.

4. **Attack Prerequisites**: When answering about specific attacks, mention the conditions required for each attack to work—this shows depth of understanding.

5. **Connection to Number Theory**: Many cryptanalytic attacks rely on number theory results. Review the Chinese Remainder Theorem, continued fractions, and basic factorization algorithms.

6. **Practical Implications**: DU exams may ask about real-world implications. Understand that factorization of 1024-bit RSA is still considered infeasible, but 512-bit RSA has been broken.

7. **Defense Mechanisms**: Always be ready to suggest countermeasures against the attacks discussed. For example, random padding defeats Hastad's attack, constant-time implementation defeats timing attacks.