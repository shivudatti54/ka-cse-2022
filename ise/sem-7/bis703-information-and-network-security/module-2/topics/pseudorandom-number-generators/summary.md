# Pseudorandom Number Generators

=====================================

### Overview

A Pseudorandom Number Generator (PRNG) is a deterministic algorithm that produces sequences of numbers approximating true randomness from an initial seed value. In cryptography, PRNGs are essential for generating keys, nonces, and initialization vectors. A Cryptographically Secure PRNG (CSPRNG) must provide unpredictability and pass statistical randomness tests.

### Key Points

- **Deterministic:** Output is fully determined by the seed; same seed produces identical sequences.
- **CSPRNG Requirements:** (1) Unpredictability -- infeasible to predict the next bit from previous outputs; (2) Statistical randomness -- uniform distribution and independence.
- **Internal Structure:** Consists of internal state, output function (G), and update function (F): output*i = G(S_i), S*(i+1) = F(S_i).
- **LCG (Not Secure):** S\_(n+1) = (a \* S_n + c) mod m; highly predictable from a few outputs.
- **Blum Blum Shub (BBS):** S\_(i+1) = (S_i)^2 mod n; based on integer factorization difficulty; theoretically secure but slow.
- **Hash-Based CSPRNG:** Uses SHA-256 in a feedback loop with timestamps for unpredictable output.
- **Block Cipher CSPRNG (CTR Mode):** Output_i = Encrypt_K(Counter_i); efficient and secure using AES.
- **Seed Security:** The PRNG is only as secure as its seed; seed must come from a true random source (TRNG).

### Important Concepts

- PRNG vs. TRNG: PRNG is deterministic and fast; TRNG uses physical phenomena and is slower but truly unpredictable.
- Hybrid approach in practice: TRNG gathers entropy to seed a fast CSPRNG for bulk random data generation.
- Weak PRNG in RSA key generation can lead to predictable primes and total system compromise.
- Reseeding periodically provides backward secrecy if the current state is compromised.

### Notes

- Memorize the two CSPRNG properties: unpredictability and statistical randomness.
- Know why LCG is bad for crypto (linear, predictable) vs. why AES-CTR mode PRNG is secure.
- Understand that the seed is the secret; the algorithm is public. A predictable seed breaks everything.
