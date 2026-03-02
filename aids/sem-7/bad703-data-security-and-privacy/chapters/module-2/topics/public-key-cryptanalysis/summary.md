# Public Key Cryptanalysis - Summary

## Key Definitions and Concepts

- **Cryptanalysis**: The study of methods for defeating cryptographic techniques, analyzing vulnerabilities in encryption systems
- **Factorization Attack**: Breaking RSA by factoring the modulus n = p × q to derive the private key
- **Timing Attack**: Side-channel attack exploiting variation in computation time to deduce key bits
- **Chosen Ciphertext Attack (CCA)**: Attack where attacker obtains decryptions of chosen ciphertexts; adaptive CCA2 allows queries based on previous results
- **Wiener's Attack**: Exploits small private exponents (d < n^0.25) using continued fraction approximation
- **Hastad's Broadcast Attack**: Recovers plaintext when same message is encrypted to multiple recipients using low exponent

## Important Formulas and Theorems

- RSA: c = m^e mod n, m = c^d mod n where n = p × q and d × e ≡ 1 (mod φ(n))
- Coppersmith's Theorem: Given lower half bits of root, entire root can be recovered efficiently
- Complexity of GNFS: Sub-exponential, the fastest known factorization method
- Wiener's bound: d < n^0.25 provides security against continued fraction attacks

## Key Points

- RSA security rests on computational difficulty of integer factorization
- Raw RSA without padding is vulnerable to multiple attacks and should never be used
- PKCS#1 v1.5 padding was vulnerable to Bleichenbacher's attack; OAEP provides better security
- Small public exponents (e = 3) enable broadcast attacks but can be safe with proper padding
- Side-channel attacks like timing attacks require constant-time implementations as countermeasures
- Each RSA user should have unique modulus; common modulus attacks can otherwise recover messages
- 2048-bit RSA keys are currently considered secure; 512-bit keys have been factored

## Common Mistakes to Avoid

- Confusing factorization complexity (exponential vs sub-exponential) in answers
- Assuming RSA is broken just because factorization is theoretically possible
- Forgetting that padding serves both semantic security and attack prevention purposes
- Overlooking the requirement that moduli must be coprime for certain attacks to work

## Revision Tips

1. Focus on understanding the preconditions for each attack—this helps in identifying vulnerable scenarios
2. Practice the mathematical basis of Wiener's and Hastad's attacks with small examples
3. Remember that real-world security requires multiple defensive layers beyond algorithm choice
4. Review the relationship between key size, computational power, and security guarantees
5. Connect cryptanalysis concepts to the RSA algorithm description from earlier topics in the module