# Substitution Ciphers: Caesar Cipher

## 1. Introduction to Classical Cryptography

Cryptography, the art and science of secret writing, has been practiced for millennia, with evidence of encryption techniques dating back to ancient Egypt and Mesopotamia. Classical encryption techniques form the conceptual foundation upon which modern cryptographic principles were developed. These techniques are characterized by their operation on characters (typically letters) of the alphabet, distinguishing them from modern cryptographic algorithms that operate on binary bits.

The primary categories of classical ciphers are:

- **Substitution Ciphers**: Each letter in the plaintext is replaced by another letter or symbol according to a fixed rule or key.
- **Transposition Ciphers**: The letters of the plaintext are rearranged according to a systematic permutation, without altering the actual letters.

This module provides an in-depth analysis of **Substitution Ciphers**, with particular emphasis on the Caesar Cipher as a canonical example.

## 2. Fundamental Concept: Substitution

A substitution cipher replaces each character in the plaintext (the original message) with another character to produce the ciphertext (the encrypted message). This replacement is governed by a deterministic rule or key, enabling both encryption and decryption.

**Definition (Substitution Cipher):** A substitution cipher is a symmetric encryption algorithm where the encryption function E_K maps each plaintext character p ∈ P to a ciphertext character c ∈ C using a key K, such that c = E_K(p). The corresponding decryption function D_K satisfies the fundamental property that p = D_K(E_K(p)) for all plaintext p.

The basic process can be visualized as:

```
+-------------+     +-------------------+     +--------------+
|             |     |                   |     |              |
|  PLAINTEXT  | --> | SUBSTITUTION RULE | --> |  CIPHERTEXT |
|   (P)       |     |      (Key K)      |     |     (C)      |
|             |     |                   |     |              |
+-------------+     +-------------------+     +--------------+
```

## 3. The Caesar Cipher

The Caesar Cipher, named after Julius Caesar who reportedly employed it for military communications during the Gallic Wars (circa 58 BC), represents one of the simplest and most historically significant encryption techniques. It belongs to the category of **shift ciphers** (also called additive ciphers or rotation ciphers).

### 3.1. Mathematical Formulation

The Caesar Cipher operates as a modular arithmetic function over the integers modulo 26. We assign numerical values to each letter: A=0, B=1, ..., Z=25.

**Encryption Function:**
For a given key K ∈ {0, 1, 2, ..., 25}, the encryption of plaintext letter P is:

```
C = E_K(P) = (P + K) mod 26
```

**Decryption Function:**
The decryption of ciphertext letter C yields the original plaintext:

```
P = D_K(C) = (C - K) mod 26
```

**Theorem (Correctness of Decryption):** For any plaintext letter P, key K, and ciphertext C = (P + K) mod 26, the decryption formula correctly recovers the original plaintext: D_K(C) = (C - K) mod 26 = ((P + K) - K) mod 26 = P mod 26 = P.

_Proof:_ By the properties of modular arithmetic, (P + K - K) mod 26 = P mod 26 = P, since P ∈ {0, 1, ..., 25}. ∎

### 3.2. Worked Numerical Example

Let us encrypt the plaintext "SECRET" with key K = 3 (a right shift of 3 positions):

| Step | Plaintext | P (Numerical) | P + K | (P + K) mod 26 | Ciphertext C |
| :--: | :-------: | :-----------: | :---: | :------------: | :----------: |
|  1   |     S     |      18       |  21   |       21       |      V       |
|  2   |     E     |       4       |   7   |       7        |      H       |
|  3   |     C     |       2       |   5   |       5        |      F       |
|  4   |     R     |      17       |  20   |       20       |      U       |
|  5   |     E     |       4       |   7   |       7        |      H       |
|  6   |     T     |      19       |  22   |       22       |      W       |

**Result:** Plaintext "SECRET" encrypts to ciphertext "VHFUHW".

For decryption, applying C - K mod 26: V→S (21-3=18), H→E (7-3=4), F→C (5-3=2), U→R (20-3=17), etc., recovering "SECRET".

### 3.3. Keyspace Analysis and Security Strength

**Keyspace Size:** The Caesar cipher has 26 possible keys (K = 0, 1, 2, ..., 25). However, K = 0 represents the identity transformation (no encryption), and K = 26 is equivalent to K = 0. Therefore, there are effectively **25 non-trivial encryption keys**.

_Formal Proof:_ The keyspace size is |K| = 26. Since E*K(p) = p when K ≡ 0 (mod 26), and E_K(p) = E*{K+26}(p) for all K due to the modulo 26 operation, the number of distinct cipher transformations is at most 26. However, since the Caesar cipher forms a cyclic group under composition (as we shall discuss), there are exactly 26 distinct transformations, but only 25 non-trivial ones for active encryption purposes.

**Computational Complexity for Brute-Force:**

- **Time Complexity:** O(25) = O(1), constant time
- **Space Complexity:** O(1), constant space

This analysis demonstrates the fundamental weakness: with only 25 possible keys, an attacker can trivially exhaustive search the entire keyspace.

### 3.4. Group Theoretic Perspective

The set of all Caesar ciphers, under the operation of composition, forms a cyclic group of order 26.

**Definition:** A cyclic group G is a group that can be generated by a single element g, such that every element of G can be expressed as g^n for some integer n.

**Theorem:** The set C = {E_0, E_1, ..., E_25} with composition as the binary operation forms a cyclic group of order 26.

_Proof:_

1. **Closure:** For any E*a, E_b ∈ C, E_a ∘ E_b = E*{(a+b) mod 26} ∈ C
2. **Associativity:** Function composition is inherently associative
3. **Identity:** E_0 acts as the identity element (no shift)
4. **Inverse:** For each E*K, E*{-K mod 26} serves as its inverse
5. **Cyclic Generation:** E_1 generates the entire group since E_1^k = E_k for 0 ≤ k ≤ 25

This group-theoretic perspective reveals that the Caesar cipher is a special case of the more general **affine cipher** with parameters a=1, b=K.

### 3.5. Cryptanalysis of the Caesar Cipher

Cryptanalysis refers to the process of breaking cryptographic systems without knowledge of the key. The Caesar cipher is vulnerable to multiple attacks.

#### 3.5.1. Brute-Force Attack

Since the keyspace contains only 25 non-trivial keys, an attacker can systematically try each possible shift value. The attack proceeds as follows:

1. For K = 1 to 25, compute P_i = (C - K) mod 26 for each ciphertext character
2. Evaluate each decrypted result for linguistic validity
3. Identify the key that produces coherent, meaningful text

**Example:** Given ciphertext "KHOOR" (which we know is encrypted with a Caesar cipher):

| Key K | Decrypted Text | Assessment       |
| :---: | :------------: | :--------------- |
|   1   |     JGNQQ      | Incoherent       |
|   2   |     IFMMP      | Incoherent       |
| **3** |   **HELLO**    | **English word** |

The key K = 3 yields "HELLO", confirming the plaintext.

#### 3.5.2. Frequency Analysis Attack

This more sophisticated attack exploits the statistical properties of natural language. In English, letter frequencies are highly non-uniform: 'E' occurs approximately 12.02% of the time, while 'Z' occurs less than 0.1%.

**Algorithm for Frequency Analysis:**

1. Compute the frequency distribution f(c) for each ciphertext letter c
2. Identify the most frequent letter in the ciphertext, denote it as c_max
3. Compute the probable shift: K = (c_max - e) mod 26, where e = 4 (numerical value of 'E')
4. Apply decryption with this key to obtain the plaintext candidate
5. If the result is not meaningful, examine the second or third most frequent letters

**Worked Example:**

Given ciphertext: "WKH SDOace LV BRONH" (Note: For simplicity, using a continuous string without spaces)

Let us compute letter frequencies in this ciphertext. Assuming the most frequent letter is 'K' (appears 3 times), and knowing 'E' is most frequent in English:

K (numerical value 10) - E (4) = 6

Therefore, probable key K = 6. Decrypting with K = 6:

- W (22) - 6 = 16 → Q
- K (10) - 6 = 4 → E
- H (7) - 6 = 1 → B

This does not yield meaningful text. Trying the next candidate: If most frequent is 'H' (7):
H - E = 3 → K = 3

Decrypting with K = 3:

- W (22) - 3 = 19 → T
- K (10) - 3 = 7 → H
- H (7) - 3 = 4 → E

Result: "THE..." which confirms K = 3.

**Complexity of Frequency Analysis:**

- **Best Case:** O(n) where n is ciphertext length, if the most frequent letter corresponds to 'E'
- **Worst Case:** O(25n), still linear in ciphertext length

This contrasts sharply with the exponential complexity required to brute-force modern block ciphers, demonstrating why classical ciphers are unsuitable for contemporary security applications.

### 3.6. Limitations and Historical Context

The Caesar cipher, while historically significant, suffers from fundamental weaknesses that render it unsuitable for modern cryptographic applications:

1. **Trivial Keyspace:** Only 25 meaningful keys enable instantaneous brute-force attacks
2. **Susceptibility to Frequency Analysis:** Preserves statistical patterns of the plaintext language
3. **Lack of Semantic Security:** Identical plaintext blocks always produce identical ciphertext blocks
4. **No Key Expansion:** The single integer key provides insufficient entropy

These limitations motivated the development of more sophisticated classical ciphers, including polyalphabetic substitution ciphers (such as the Vigenère cipher) and mechanical encryption devices (such as the Enigma), which address the frequency analysis vulnerability through multiple substitution alphabets.

## 4. Summary

The Caesar cipher represents the foundational example of substitution-based encryption. Despite its historical prominence and mathematical simplicity, it demonstrates critical vulnerabilities that exemplify fundamental cryptographic principles:

- Small keyspaces permit exhaustive search attacks
- Preserving linguistic statistics enables frequency analysis
- Deterministic encryption reveals patterns in the plaintext

Understanding these weaknesses provides essential insight into the evolutionary trajectory of cryptography toward modern symmetric-key algorithms and the principles of computational security.
