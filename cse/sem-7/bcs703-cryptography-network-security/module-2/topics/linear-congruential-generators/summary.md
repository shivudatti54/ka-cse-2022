# Linear Congruential Generators

=====================================

### Overview

A Linear Congruential Generator (LCG) is one of the oldest and simplest pseudorandom number generators (PRNGs). It produces a deterministic sequence of numbers using a linear recurrence relation. While historically important, LCGs are highly predictable and cryptographically insecure, making them unsuitable for generating encryption keys or nonces.

### Key Points

- **Formula:** X\_(n+1) = (a \* X_n + c) mod m, where a is the multiplier, c is the increment, m is the modulus.
- **Deterministic:** The same seed X_0 always produces the same sequence.
- **Periodicity:** The sequence must eventually repeat; maximum possible period is m with proper parameter choice.
- **Full Period Conditions:** c and m coprime; (a-1) divisible by all prime factors of m; if m is a multiple of 4, (a-1) must also be a multiple of 4.
- **Highly Predictable:** Observing a few consecutive values allows an attacker to solve for a, c, and m, predicting all future values.
- **Cryptographically Insecure:** Must never be used for key generation, nonces, or any security-critical random values.
- **Legacy Use:** Still found in non-security contexts like simulations, Monte Carlo methods, and basic rand() functions.
- **Modern Replacements:** CSPRNGs based on hash functions (SHA-256) or block ciphers (AES in counter mode).

### Important Concepts

- X\_(n+1) = (a \* X_n + c) mod m is the defining recurrence relation.
- The sequence is entirely determined by the seed and the parameters (a, c, m).
- Short periods result from poor parameter choices (e.g., m=9, a=2, c=5 gives period 2).
- The linear relationship is the fundamental weakness that makes LCGs predictable and insecure.

### Notes

- Be able to generate a sequence from given parameters (a, c, m, X_0) for exam calculations.
- Always state that LCGs are NOT cryptographically secure and explain why (predictability from linearity).
- Know the contrast: LCGs are fast but insecure; CSPRNGs are slightly slower but cryptographically sound.
