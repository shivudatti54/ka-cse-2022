# The Security of RSA

=====================================

### Overview

The security of the RSA cryptosystem relies entirely on the computational difficulty of the Integer Factorization Problem. Breaking RSA requires factoring a large composite number n into its prime factors p and q, which is infeasible for sufficiently large key sizes. Proper parameter selection and implementation are critical for maintaining RSA security.

### Key Points

- **Integer Factorization Problem:** Factoring n back into p and q is computationally equivalent to breaking RSA
- **Brute Force Attack:** Completely infeasible for modern key sizes (2048+ bits)
- **General Number Field Sieve (GNFS):** Best known factoring algorithm; still sub-exponential complexity
- **Computing phi(n) directly:** Proven to be exactly as hard as factoring n itself
- **Chosen Ciphertext Attacks (CCA):** Mitigated by using OAEP padding scheme
- **Side-Channel Attacks:** Timing and power analysis can leak private key bits; require constant-time implementations
- **Strong Primes:** p and q should be roughly equal size, truly random, and (p-1)/(q-1) should have large prime factors
- **Quantum Threat:** Shor's Algorithm on quantum computers could break RSA, driving Post-Quantum Cryptography research

### Important Concepts

- Breaking RSA is equivalent to factoring n: if you can factor n, you can compute phi(n) = (p-1)(q-1) and derive d
- Key size requirements: 1024-bit is deprecated; 2048-bit is minimum standard; 3072/4096-bit for long-term security
- OAEP (Optimal Asymmetric Encryption Padding) prevents chosen ciphertext attacks
- Pollard's p-1 attack is thwarted by using strong primes where (p-1) has a large prime factor
- Public exponent e = 65537 is standard; very small e values risk Coppersmith's attack

### Notes

- Exam questions often ask "what makes RSA secure" -- answer with the Integer Factorization Problem
- Be able to distinguish between mathematical attacks (factoring n) and side-channel attacks (timing/power)
- Remember that computing phi(n) without factoring is equally hard as factoring itself
- Mention quantum computing and Shor's Algorithm when discussing future threats to RSA
