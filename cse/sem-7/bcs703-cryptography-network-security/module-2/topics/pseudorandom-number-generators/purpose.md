# Learning Purpose: Pseudorandom Number Generators

**1. Why this topic matters**
Pseudorandom number generators (PRNGs) are critical to cryptography because nearly every cryptographic operation, from key generation to nonce creation to initialization vectors, depends on unpredictable random values. Within Module 2, this topic establishes the distinction between statistical randomness and cryptographic security, explaining why weak random number generation can undermine otherwise strong encryption algorithms.

**2. What you will learn**
You will learn the definition and internal structure of PRNGs, including the roles of the seed, internal state, and output function. You will understand the difference between true random number generators and pseudorandom generators, learn the properties required for a cryptographically secure PRNG (CSPRNG), and evaluate why common non-cryptographic generators like LCGs fail to meet these requirements.

**3. How it connects to other topics**
This topic provides the foundation for studying the specific generators covered in Module 2, including Linear Congruential Generators and the Blum Blum Shub generator. The quality of random number generation directly affects the security of RSA key generation, Diffie-Hellman parameter selection, and the session key creation used in the TLS and IPsec protocols of Module 5.

**4. Real-world relevance**
Weak PRNGs have been responsible for major real-world security failures, including the Debian OpenSSL vulnerability that made SSH keys predictable. Proper PRNG selection and seed management are essential practices in any system that generates cryptographic keys, session tokens, or authentication challenges.
