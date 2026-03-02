# Substitution Ciphers: Caesar and Monoalphabetic

## 1. Introduction to Classical Cryptography

Cryptography, the art of secret writing, has ancient origins. Classical encryption techniques form the foundation of modern cryptography. These techniques are characterized by their operation on letters of the alphabet, unlike modern ciphers that operate on binary bits. The two primary categories of classical ciphers are:
*   **Substitution Ciphers**: Letters in the plaintext are replaced by other letters or symbols.
*   **Transposition Ciphers**: Letters in the plaintext are rearranged.

This module focuses on **Substitution Ciphers**, specifically the Caesar and Monoalphabetic ciphers.

## 2. The Core Concept: Substitution

A substitution cipher replaces each letter in the plaintext (the original message) with another letter to produce the ciphertext (the encrypted message). This replacement is governed by a fixed rule or a key.

The basic process can be visualized as follows:
```
+-------------+      +-------------------+      +--------------+
|             |      |                   |      |              |
|  PLAINTEXT  |  ->  | SUBSTITUTION RULE |  ->  |  CIPHERTEXT  |
|             |      |       (Key)       |      |              |
+-------------+      +-------------------+      +--------------+
```

## 3. The Caesar Cipher

The Caesar Cipher, named after Julius Caesar who reportedly used it for military communications, is one of the simplest and most widely known encryption techniques. It is a type of **shift cipher**.

### 3.1. How it Works
The encryption algorithm involves replacing each letter in the plaintext by a letter a fixed number of positions down the alphabet. This fixed number is the **key**.

**Encryption Formula:**
`C = E(K, P) = (P + K) mod 26`

Where:
*   `C` = Ciphertext letter (as a number, A=0, B=1, ..., Z=25)
*   `P` = Plaintext letter (as a number, A=0, B=1, ..., Z=25)
*   `K` = Key (the shift value, e.g., 3 for a classic Caesar cipher)
*   `mod 26` = The modulo operation, which handles wrap-around (e.g., Z + 1 = A)

**Decryption Formula:**
`P = D(K, C) = (C - K) mod 26`

### 3.2. Example
Let's encrypt the word "SECRET" with a key `K = 3` (a right shift of 3 positions).

| Step | Letter | P (Number) | (P + 3) | mod 26 | C (Letter) |
| :--- | :----- | :--------: | :-----: | :----: | :-------- |
| 1    | S      |     18     |   21    |   21   | V         |
| 2    | E      |     4      |    7    |    7   | H         |
| 3    | C      |     2      |    5    |    5   | F         |
| 4    | R      |     17     |   20    |   20   | U         |
| 5    | E      |     4      |    7    |    7   | H         |
| 6    | T      |     19     |   22    |   22   | W         |

**Result:** Plaintext "SECRET" encrypts to ciphertext "VHFUHW".

Decryption simply reverses the process using `(C - 3) mod 26`.

### 3.3. Cryptanalysis of the Caesar Cipher
The Caesar cipher is incredibly weak and can be broken easily with two primary methods:
1.  **Brute-Force Attack**: Since the key is an integer between 1 and 25, there are only 25 possible keys to try. An attacker can quickly decrypt the message with all possible shifts and look for the one that produces intelligible text.
2.  **Frequency Analysis**: Even faster than brute-force, an attacker can analyze the frequency of letters in the ciphertext. For example, in English, 'E' is the most common letter. The most frequent letter in the ciphertext is likely the encryption of 'E'. The shift value `K` can be deduced from this difference.

```
Ciphertext Frequency Chart (e.g., 'X' is most common)
      |
      |  Assuming 'X' = Encrypted 'E'
      V
Key (K) = ('X' - 'E') mod 26 = (23 - 4) = 19
```

## 4. Monoalphabetic Substitution Cipher

The Monoalphabetic Substitution Cipher is a significant improvement over the Caesar cipher. Instead of shifting the alphabet, it uses **any random permutation** of the 26 letters. This means the mapping from plaintext to ciphertext can be completely jumbled.

### 4.1. How it Works
A key for this cipher is a randomly shuffled alphabet. Each plaintext letter maps to one unique ciphertext letter throughout the entire message.

**Example Key Mapping:**
```
Plaintext:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
```
Using this key:
*   "HELLO" would encrypt to "I T K K G" (but without spaces: "ITKKG").
*   "ATTACK" would encrypt to "Q Z Z Q E H".

### 4.2. Keyspace and Theoretical Strength
The number of possible keys is the number of ways to permute the 26 letters, which is `26!` (factorial).
`26! = 26 × 25 × 24 × ... × 2 × 1 ≈ 2⁸⁸ ≈ 4 x 10²⁶`

This is a massive number of possible keys. A brute-force attack that tries every single key is computationally infeasible, even for modern computers.

### 4.3. Cryptanalysis using Frequency Analysis
Despite the large keyspace, the monoalphabetic cipher is vulnerable to **frequency analysis**. Because it always maps one plaintext letter to one ciphertext letter, it preserves the frequency distribution of the original language.

**How to Break It:**
1.  **Collect Ciphertext**: Obtain a sufficiently long ciphertext message.
2.  **Calculate Frequencies**: Count the occurrence of each letter in the ciphertext.
3.  **Compare to Language Profiles**: Compare the frequency distribution to the known frequency distribution of the language (e.g., English).
4.  **Make educated guesses**:
    *   The most frequent ciphertext letter likely corresponds to 'E'.
    *   The least frequent likely corresponds to 'Z', 'Q', 'J', etc.
    *   Look for common words: single-letter words are likely 'A' or 'I'; three-letter words like "THE", "AND" are common.
5.  **Refine the Mapping**: Use these guesses to partially decrypt the text and make further guesses based on context until the entire plaintext is recovered.

**Table: Typical Letter Frequencies in English**
| Letter | Frequency (%) | Letter | Frequency (%) |
| :----- | :-----------: | :----- | :-----------: |
| E      |     12.02     | M      |      2.41     |
| T      |      9.10     | H      |      5.92     |
| A      |      8.12     | F      |      2.20     |
| O      |      7.68     | P      |      1.82     |
| I      |      7.31     | Y      |      1.72     |
| N      |      6.95     | W      |      1.73     |
| S      |      6.28     | G      |      2.03     |
| R      |      6.02     | B      |      1.49     |
| H      |      5.92     | V      |      0.98     |
| D      |      4.32     | K      |      0.77     |
| L      |      3.98     | X      |      0.15     |
| U      |      2.88     | Q      |      0.10     |
| C      |      2.71     | J      |      0.10     |
|        |               | Z      |      0.07     |

## 5. Comparison of Ciphers

| Feature               | Caesar Cipher                          | Monoalphabetic Cipher                  |
| --------------------- | -------------------------------------- | -------------------------------------- |
| **Key**               | A single integer (1-25)                | A random permutation of the alphabet   |
| **Keyspace Size**     | Very Small (25)                        | Very Large (~4x10²⁶)                   |
| **Encryption Process**| Simple shift                           | Simple substitution based on a mapping |
| **Strength**          | Very Weak                              | Stronger than Caesar, but still weak   |
| **Primary Vulnerability** | Brute-Force Attack                 | Frequency Analysis                     |
| **Number of Alphabets**| One (Monoalphabetic)                  | One (Monoalphabetic)                   |

## 6. Conclusion and Historical Context

Both Caesar and Monoalphabetic ciphers are **monoalphabetic**, meaning they use a single, fixed substitution alphabet for the entire message. This fundamental property is their greatest weakness, as it directly leaks the statistical patterns of the underlying plaintext language.

These ciphers are obsolete for modern secure communication but are essential for learning the basic principles of cryptography. They illustrate the concepts of substitution, keys, and cryptanalysis. Their weaknesses led to the development of stronger ciphers, such as the **Polyalphabetic cipher** (e.g., the Vigenère cipher), which uses multiple substitution alphabets to defeat simple frequency analysis.

---

## Exam Tips

*   **Memorize the Formulas**: Be able to write and apply the encryption/decryption formulas for the Caesar Cipher, `C = (P + K) mod 26` and `P = (C - K) mod 26`.
*   **Practice Frequency Analysis**: You will likely be asked to decrypt a short monoalphabetic ciphertext using a provided frequency table. Start by identifying the most common letter as 'E'.
*   **Understand the Keyspace**: Explain why a large keyspace alone (like in the monoalphabetic cipher) does not guarantee security. The focus should be on the preservation of letter frequencies.
*   **Draw the Table**: For a Caesar cipher question, drawing a simple encryption/decryption table (like in section 3.2) is a clear way to show your work and avoid calculation errors.
*   **Know the Differences**: Be prepared to compare and contrast Caesar and Monoalphabetic ciphers in a short essay question, highlighting their keys, strengths, and weaknesses.