# Polyalphabetic Ciphers

## Introduction

Polyalphabetic ciphers represent a fundamental advancement over monoalphabetic substitution ciphers in classical cryptography. While monoalphabetic ciphers employ a fixed substitution alphabet throughout the entire message, polyalphabetic ciphers utilize multiple substitution alphabets that change systematically according to a defined rule or key. This architectural difference provides substantial resistance to frequency analysis attacks, which effectively compromise simpler substitution methods.

The concept of polyalphabetic substitution was first systematically articulated by Leon Battista Alberti in his 1466 treatise "De Cifris." Alberti's revolutionary cipher disk mechanism involved rotating discs, each containing a scrambled alphabet, to change the substitution alphabet after every few letters. This groundbreaking approach established the foundational principles for centuries of cryptographic development and remained computationally secure until the emergence of advanced cryptanalysis techniques in the twentieth century.

The primary motivation behind polyalphabetic ciphers is to obfuscate the statistical properties inherent in natural language plaintexts. In English and other natural languages, certain letters appear with characteristic frequency distributions—the letter 'E' occurs approximately 12.7% of the time, while 'Z' appears less than 0.1%. Cryptanalysts exploit these frequencies to recover plaintext from monoalphabetic ciphers. By employing multiple alphabets systematically, polyalphabetic ciphers distribute ciphertext symbol frequencies more uniformly, rendering statistical attacks significantly more challenging.

## Mathematical Foundation

### The Index of Coincidence

The Index of Coincidence (IC) serves as a fundamental metric in cryptanalysis of polyalphabetic ciphers. Mathematically, the IC is defined as the probability that two randomly selected letters from a text are identical. For a text with n letters where letter i appears f_i times:

$$IC = \sum_{i=0}^{25} \frac{f_i(f_i - 1)}{n(n - 1)}$$

For English plaintext, the IC value is approximately 0.065, while uniformly random text yields an IC of approximately 0.0385 (1/26). This metric enables cryptanalysts to distinguish between monoalphabetic (higher IC) and polyalphabetic (lower IC) encryptions, and assists in estimating key length.

### Proof: Periodicity Detection

Consider a Vigenère cipher with key length L. The ciphertext can be decomposed into L independent Caesar ciphers, each containing every L-th ciphertext letter. Each such subsequence exhibits an IC approaching 0.065 as the subsequence length increases. Conversely, if we incorrectly assume a period L' that does not divide the true key length, the resulting subsequences contain a mixture of different Caesar encryptions, yielding an IC closer to 0.0385. This mathematical property forms the basis of the Friedman test for key length estimation.

## The Vigenère Cipher

The Vigenère cipher stands as the most prominent polyalphabetic substitution cipher in cryptographic history. First comprehensively described by Giovan Battista Bellaso in 1553, it was erroneously attributed to Blaise de Vigenère in the nineteenth century. The cipher employs a keyword or phrase to determine which Caesar cipher applies to each plaintext letter.

**Encryption Formula:**
$$C_i = (P_i + K_{i \mod m}) \mod 26$$

**Decryption Formula:**
$$P_i = (C_i - K_{i \mod m}) \mod 26$$

Where P_i represents the i-th plaintext letter converted to numerical value (A=0, B=1, ..., Z=25), K_i denotes the i-th key letter similarly converted, and m represents the key length.

### Worked Example

Encrypt plaintext "HELLO" using key "KEY":

- Key: K-E-Y-K-E (numerical: 10, 4, 24, 10, 4)
- Plaintext: H-E-L-L-O (numerical: 7, 4, 11, 11, 14)
- Ciphertext: R-I-X-T-S (numerical: 17, 8, 23, 19, 18)

Calculation: H(7) + K(10) = 17 = R; E(4) + E(4) = 8 = I; L(11) + Y(24) = 35 mod 26 = 9 = X

## The Autokey Cipher

The autokey cipher, also invented by Bellaso, eliminates the repeating key pattern inherent in Vigenère by using the plaintext itself as the key after an initial priming value. This enhancement provides improved security by ensuring no key portion repeats exactly.

**Encryption Formula:**
For i > 0: $$C_i = (P_i + P_{i-1}) \mod 26$$
With priming key P_0.

**Decryption Formula:**
For i > 0: $$P_i = (C_i - P_{i-1}) \mod 26$$

### Worked Example

Encrypt plaintext "ATTACK" with priming key "K":

- Key: K-A-T-T-A-C (K followed by plaintext)
- Plaintext: A-T-T-A-C-K
- Ciphertext: K-T-F-T-F-M

A notable vulnerability exists: if a cryptanalyst correctly guesses plaintext portions, they can extend the guess systematically—a property termed "self-synchronization."

## The One-Time Pad

The one-time pad represents the pinnacle of polyalphabetic encryption, achieving perfect secrecy when implemented correctly. Invented by Gilbert Vernam in 1917 and mathematically proven secure by Claude Shannon in 1949, it employs a truly random key of length equal to or exceeding the plaintext.

**Requirements for Perfect Secrecy:**

1. The key must be truly random (not pseudo-random)
2. The key must be used exactly once
3. The key must be kept completely secret
4. The key must be at least as long as the message

**Security Proof:**
For any plaintext P of length n and any observed ciphertext C of length n, there exists exactly one key K such that E_K(P) = C. Without knowledge of K, all plaintexts of length n are equally probable. This mathematically proves unbreakability under ciphertext-only attack.

The practical challenges of true random key generation, secure key distribution, and key storage have limited one-time pad deployment to ultra-sensitive applications requiring absolute security.

## Cryptanalysis of Polyalphabetic Ciphers

### Kasiski Examination (1863)

The Kasiski examination identifies repeated sequences in the ciphertext. The distances between repetitions often contain the key length as a common factor. For example, if "XYZ" appears at positions 15 and 87, the distance 72 may indicate key length divisors (1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72).

### Friedman Test (1920)

The Friedman test estimates key length using the Index of Coincidence:

$$L = \frac{0.0265n}{(0.065 - IC) + 0.0265(n-1)}$$

Where n represents the ciphertext length. This formula derives from solving for L when the observed IC falls between random (0.0385) and English (0.065) values.

### Cryptanalysis Procedure

1. Compute IC of entire ciphertext
2. Apply Friedman formula to estimate probable key length
3. Use Kasiski examination to confirm or refine estimate
4. Extract every L-th character to form L subsequences
5. Perform frequency analysis on each subsequence (Caesar cipher attack)
6. Recover key and decrypt entire message

## Additional Polyalphabetic Systems

### Beaufort Cipher

The Beaufort cipher uses the decryption formula of Vigenère as its encryption operation:

$$C_i = (K_i - P_i) \mod 26$$

It is symmetric—encryption and decryption operations are identical.

### Running-Key Cipher

The running-key cipher uses a long non-repeating key (e.g., book text) instead of a short repeating keyword. This approach increases resistance to Kasiski examination but maintains vulnerabilities to statistical attacks when the key text exhibits statistical patterns.
