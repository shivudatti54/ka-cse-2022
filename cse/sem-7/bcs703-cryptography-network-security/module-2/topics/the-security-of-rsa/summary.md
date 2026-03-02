# The Security of RSA - Summary

## Key Definitions

- **Integer Factorization Problem**: The computational problem of determining prime factors p and q from their product n = p × q, forming the foundation of RSA security.
- **RSA Problem**: Computing the e-th root of ciphertext c modulo n without knowing the private exponent d.
- **OAEP (Optimal Asymmetric Encryption Padding)**: A padding scheme that adds randomness to RSA encryption, preventing deterministic attacks.
- **PSS (Probabilistic Signature Scheme)**: A padding scheme for RSA signatures providing security proofs.
- **Side-Channel Attacks**: Attacks exploiting implementation characteristics like timing, power consumption, or cache patterns.

## Important Formulas

- Key generation: n = p × q, where p and q are large primes
- Euler's totient: φ(n) = (p-1)(q-1)
- Key relationship: e × d ≡ 1 (mod φ(n))
- Encryption: c = m^e mod n
- Decryption: m = c^d mod n

## Key Points

1. RSA security depends on the computational difficulty of factoring large composite numbers into their prime factors.

2. Current recommendations require minimum 2048-bit keys; 1024-bit RSA is considered insecure and should not be used.

3. Proper prime selection is critical: primes must be random, distinct, of similar bit length, with (p-1) and (q-1) having large prime factors.

4. Raw RSA without padding is insecure due to deterministic nature and homomorphic properties.

5. OAEP and PSS padding schemes are essential for secure RSA encryption and signatures respectively.

6. The standard public exponent e = 65537 provides a good balance between efficiency and security.

7. Side-channel attacks (timing, power analysis, fault injection) can break theoretically secure implementations.

8. Implementation security is as important as algorithmic security in practical RSA deployment.

9. The equivalence between the RSA problem and integer factorization has only been proven under specific conditions.

10. Continuous research in factorization algorithms means key sizes must increase over time to maintain security.

## Common Mistakes

1. Using small key sizes (1024 bits or less) thinking they provide adequate security for modern applications.

2. Using RSA without padding or using insecure padding schemes like textbook RSA directly.

3. Choosing primes p and q that are too close together, making n vulnerable to Fermat factorization.

4. Selecting small public exponent e = 3 without proper padding, leading to vulnerability against Hastad's broadcast attack.

5. Ignoring implementation security, assuming mathematical correctness alone ensures security against real-world attacks.