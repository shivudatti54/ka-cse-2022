# Public Key Cryptanalysis - Summary

## Key Definitions

- **Integer Factorization Problem (IFP):** The computational problem of decomposing a composite integer into its prime factors; forms the basis of RSA security.

- **Discrete Logarithm Problem (DLP):** The problem of finding the exponent x given g^x ≡ y (mod p); foundational to Diffie-Hellman and ElGamal security.

- **Chosen Ciphertext Attack (CCA):** An attack model where an attacker can obtain decryptions of arbitrary ciphertexts to extract information about the target.

- **Oracle Attack:** A cryptanalytic technique exploiting information leaked through side-channels about the correctness of intermediate values.

- **Side-Channel Attack:** Attacks exploiting physical characteristics of implementation (timing, power consumption, electromagnetic emissions) rather than mathematical properties.

## Important Formulas

- **General Number Field Sieve Complexity:** O(exp((64/9)^(1/3) × (log n)^(1/3) × (log log n)^(2/3)))

- **Fermat Factorization:** If p and q are close, n = ((p+q)/2)² - ((p-q)/2)²

- **RSA Decryption with CRT:** m = m₁ + q × ((m₁ - m₂) × q⁻¹ mod p)

## Key Points

1. The security of public key cryptography relies on mathematical problems (IFP, DLP, ECDLP) believed to be computationally hard.

2. RSA with 2048-bit keys provides approximately 112-bit security against current factoring algorithms.

3. Weak key generation (primes too close, insufficient randomness) makes RSA vulnerable to efficient factorization attacks.

4. Raw RSA without padding is vulnerable to various mathematical attacks and must use OAEP or similar schemes.

5. Side-channel attacks (timing, power analysis) can recover keys even when the mathematical problem remains unsolved.

6. Chosen ciphertext attacks like Bleichénbacher's attack exploited padding oracle in SSL/TLS implementations.

7. Protocol-level attacks (MITM, small subgroup confinement) can break systems even with mathematically secure algorithms.

8. Quantum computers threaten current public key systems through Shor's polynomial-time factoring algorithm.

## Common Mistakes

1. **Assuming large key sizes are sufficient:** Even 2048-bit RSA can be broken if implementation errors (small primes, poor randomness) exist.

2. **Confusing algorithm security with protocol security:** A secure algorithm like RSA becomes insecure with unauthenticated key exchange.

3. **Ignoring side-channel risks:** Implementing mathematically secure algorithms without constant-time operations can leak keys.

4. **Using deprecated padding schemes:** PKCS#1 v1.5 should never be used; OAEP is the current standard.

5. **Underestimating protocol attacks:** Many real-world breaches occur through protocol flaws rather than cryptographic breaks.