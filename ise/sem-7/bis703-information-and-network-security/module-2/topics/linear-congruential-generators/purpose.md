# Learning Purpose: Linear Congruential Generators

**1. Why this topic matters**
Linear Congruential Generators (LCGs) are among the simplest and most widely studied pseudorandom number generators, making them an essential starting point for understanding random number generation in Module 2. Studying LCGs reveals why simplicity and speed in PRNG design do not guarantee cryptographic security, and why predictability in random number generation can compromise an entire cryptographic system.

**2. What you will learn**
You will learn the mathematical formula of an LCG (X(n+1) = (aX(n) + c) mod m), how to choose parameters for full-period generation, and how to produce pseudorandom sequences from a seed value. You will also analyze why LCGs are cryptographically insecure due to their linear structure, short periods, and vulnerability to state-recovery attacks that allow prediction of future outputs.

**3. How it connects to other topics**
LCGs serve as a contrast to the cryptographically secure BBS generator studied later in Module 2, highlighting the critical difference between statistical randomness and cryptographic unpredictability. Understanding LCG weaknesses provides context for why cryptographic protocols like RSA and Diffie-Hellman require truly unpredictable random values for key generation and nonce selection.

**4. Real-world relevance**
LCGs are still used in non-security applications such as simulations, games, and statistical sampling where speed matters more than unpredictability. However, their use in cryptographic contexts has led to real-world security breaches, making them a cautionary example of why cryptographic random number generation requires purpose-built, security-proven generators.
