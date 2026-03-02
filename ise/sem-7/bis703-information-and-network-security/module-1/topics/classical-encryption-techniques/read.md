# Classical Encryption Techniques


## Table of Contents

- [Classical Encryption Techniques](#classical-encryption-techniques)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [1. Substitution Ciphers](#1-substitution-ciphers)
  - [2. Transposition Ciphers](#2-transposition-ciphers)
- [Summary of Key Points](#summary-of-key-points)

**Subject:** Cryptography & Network Security
**Module:** Module 1
**Topic:** Classical Encryption Techniques

## Introduction

Before the advent of computers, secure communication relied on **classical encryption techniques**. These methods form the historical foundation of modern cryptography. Understanding them is crucial, not just for historical context, but because they introduce core cryptographic concepts like **confusion**, **diffusion**, **cryptanalysis**, and the **key**. Classical ciphers are broadly categorized into two types: **Substitution Ciphers** and **Transposition Ciphers**.

---

## Core Concepts

### 1. Substitution Ciphers

This technique involves replacing each letter or group of letters in the plaintext with another letter or group of letters to form the ciphertext. The replacement follows a fixed system or a key.

#### a) Caesar Cipher

One of the simplest and most widely known substitution ciphers. It is a **mono-alphabetic cipher**, meaning it uses a single fixed alphabet for substitution.

- **Technique:** Each letter in the plaintext is shifted a fixed number of places down or up the alphabet.
- **Key:** The shift value. For example, with a key of 3:
  - A → D, B → E, C → F, ..., X → A, Y → B, Z → C.
- **Example:** Plaintext: ` BELGAUM` with key=3 becomes Ciphertext: `YWX EHOHDXP`.
- **Weakness:** Extremely vulnerable to **brute-force attacks** (only 25 possible keys to try) and frequency analysis.

#### b) Mono-alphabetic Cipher

An improvement over the Caesar cipher that uses an arbitrary substitution where each letter is mapped to another random letter in the alphabet.

- **Technique:** A single, complex mapping defines the substitution scheme for the entire message (e.g., A→Z, B→Y, C→X, ...).
- **Key:** The entire mapping of the 26 letters.
- **Strength:** 26! possible keys, making a brute-force attack impractical.
- **Weakness:** Vulnerable to **frequency analysis**. Since the substitution is fixed, the frequency distribution of letters (e.g., 'E' is the most common letter in English) is preserved in the ciphertext.

#### c) Playfair Cipher

A significant advance that encrypts **digraphs** (pairs of letters) instead of single letters, introducing **diffusion**.

- **Technique:** A 5x5 matrix (built from a keyword) is used to encrypt pairs of letters based on their position in the grid. Rules define how to shift letters (same row, same column, or a rectangle).
- **Strength:** Hides single-letter frequency distributions, making it stronger than mono-alphabetic ciphers.
- **Weakness:** Still vulnerable to digraph frequency analysis.

#### d) Vigenère Cipher (Poly-alphabetic Substitution)

This cipher uses multiple substitution alphabets to eliminate the frequency patterns that break simpler ciphers.

- **Technique:** A keyword is repeated to match the length of the plaintext. Each letter of the keyword specifies a different Caesar shift for the corresponding plaintext letter.
- **Key:** The keyword (e.g., `KEY`).
- **Example:** Plaintext: `CRYPTO`, Key: `KEYKEY`
  - C (2) + K (10) = M (12)
  - R (17) + E (4) = V (21)
  - Y (24) + Y (24) = W (22) (26 mod 26)
  - Ciphertext: `MVW`
- **Strength:** Obscures letter frequency, making it resistant to simple frequency analysis. Known as the **"unbreakable cipher"** for a long time.
- **Weakness:** Vulnerable to the **Kasiski examination** method, which identifies the keyword length by finding repeated patterns in the ciphertext.

### 2. Transposition Ciphers

Unlike substitution, transposition ciphers do not replace letters but **rearrange** the order of the letters in the plaintext.

- **Technique:** The letters are written in a predetermined pattern (e.g., a matrix) and read out in a different pattern to produce the ciphertext.
- **Example: Rail Fence Cipher**
  - Plaintext: `ENGINEERING`
  - Write in two rails: `E G E R N` (rail 1) and `N I E I G` (rail 2)
  - Ciphertext: `EGERNNIEIG`
- **Strength:** Effective at defeating frequency analysis if the transposition is complex enough.
- **Weakness:** Vulnerable if the cryptanalyst can guess the structure (e.g., number of "rails" or column size).

---

## Summary of Key Points

| Concept             | Principle                             | Strength                       | Weakness                          |
| :------------------ | :------------------------------------ | :----------------------------- | :-------------------------------- |
| **Caesar Cipher**   | Shifts letters by a fixed number.     | Simple to implement.           | Very weak; only 25 keys.          |
| **Mono-alphabetic** | Single, random letter mapping.        | Large key space (26!).         | Vulnerable to frequency analysis. |
| **Playfair Cipher** | Encrypts digraphs using a 5x5 matrix. | Hides single-letter frequency. | Vulnerable to digraph analysis.   |
| **Vigenère Cipher** | Uses a keyword for multiple shifts.   | Obscures frequency patterns.   | Kasiski examination can find key. |
| **Transposition**   | Reorders letters of the plaintext.    | Defeats frequency analysis.    | Structure can be deduced.         |

- **Cryptanalysis:** The art of breaking ciphers. Classical ciphers are broken using techniques like brute-force, frequency analysis, and pattern finding (Kasiski examination).
- **Confusion vs. Diffusion:** Substitution provides **confusion** (hiding the relationship between ciphertext and key). Transposition provides **diffusion** (spreading the plaintext statistics over the ciphertext). Modern ciphers like AES use complex combinations of both.
- **The Key is Secret:** Kerckhoffs's Principle states that the security of a cipher should depend only on the secrecy of the key, not the secrecy of the algorithm. This is a fundamental axiom in modern cryptography.
