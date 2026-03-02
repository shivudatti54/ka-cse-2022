# Cryptanalysis of a Simple Substitution

=====================================

## What is Cryptanalysis?

---

Cryptanalysis is the process of breaking or cracking the encryption of a ciphertext to obtain the original plaintext. It involves identifying patterns, vulnerabilities, and weaknesses in the encryption algorithm, allowing the attacker to decipher the encrypted data.

## What is a Simple Substitution?

---

A simple substitution is a type of encryption technique where each plaintext character is replaced by a different plaintext character. This is the simplest form of substitution cipher.

## Types of Substitution Ciphers

---

- **Single Substitution Cipher**: Each plaintext character is replaced by a different plaintext character.
- **Double Substitution Cipher**: Each plaintext character is replaced by a different plaintext character, which in turn is replaced by another plaintext character.

## How Simple Substitution Ciphers Work

---

Here's an example of a simple substitution cipher:

| Plaintext | Substitution | Ciphertext |
| :-------- | :----------- | :--------- |
| A         | D            | B          |
| B         | E            | C          |
| C         | F            | D          |
| ...       | ...          | ...        |

In this example, each plaintext character is replaced by a different plaintext character. The attacker needs to figure out the mapping between plaintext characters and their corresponding ciphertext characters.

## Types of Attacks on Simple Substitution Ciphers

---

- **Frequency Analysis**: This involves analyzing the frequency of letters in the ciphertext to deduce the most likely plaintext character.
- **Pattern Analysis**: This involves looking for patterns in the ciphertext, such as repeating sequences or common letter combinations.
- **Brute Force Attack**: This involves trying all possible combinations of plaintext characters until the correct one is found.

## Example of Frequency Analysis Attack

---

Suppose we have the following ciphertext:

`GUR PENML XRL VF ZL FRPERG`

Using frequency analysis, we can deduce that the letter `E` appears most frequently in the ciphertext.

| Letter | Frequency |
| :----- | :-------- |
| E      | 20%       |
| T      | 18%       |
| A      | 15%       |
| ...    | ...       |

Since `E` appears most frequently, we can deduce that the plaintext character corresponding to `E` in the ciphertext is likely to be the letter `T`.

## Example of Brute Force Attack

---

Suppose we have the following ciphertext:

`KHOOR`

Using a brute force attack, we can try all possible combinations of plaintext characters until the correct one is found.

| Plaintext | Ciphertext |
| :-------- | :--------- |
| Hello     | Khoor      |
| World     | Jgok       |
| Foo       | KHOOR      |

In this case, the correct plaintext is `Hello`.

## Conclusion

---

Cryptanalysis of a simple substitution cipher involves identifying patterns, vulnerabilities, and weaknesses in the encryption algorithm. Frequency analysis and brute force attacks are common methods used to break simple substitution ciphers.
