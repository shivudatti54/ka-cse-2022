# Playfair Cipher

=====================================

### Overview

The Playfair Cipher, invented by Charles Wheatstone in 1854 and popularized by Lord Playfair, is the first practical digraph substitution cipher. It encrypts pairs of letters (digraphs) using a 5x5 keyword matrix, making it significantly more resistant to frequency analysis than single-letter substitution ciphers. It was used in World War I and World War II for tactical communications.

### Key Points

- **Digraphic Cipher:** Encrypts letter pairs, not individual letters, yielding 676 possible digraphs.
- **5x5 Matrix:** Built from a keyword; letters I and J are combined into one cell.
- **Same Row Rule:** Replace each letter with the letter to its right (wrap around).
- **Same Column Rule:** Replace each letter with the letter below it (wrap around).
- **Rectangle Rule:** For letters in different rows and columns, swap to opposite horizontal corners.
- **Preprocessing:** Split plaintext into pairs; insert 'X' between repeated letters; pad with 'X' if odd length.
- **Decryption:** Reverse the rules (left instead of right, up instead of down; rectangle rule is symmetric).
- **Weakness:** Vulnerable to digraph frequency analysis and known plaintext attacks.

### Important Concepts

- Matrix construction: fill keyword letters first (no duplicates), then remaining alphabet letters in order.
- Decryption reverses the direction: same row moves left, same column moves up.
- The cipher hides single-letter frequencies but preserves digraph frequency patterns.
- Playfair was a stepping stone from monoalphabetic ciphers to modern block ciphers.

### Notes

- Practice constructing the 5x5 matrix from a keyword and encrypting/decrypting digraphs for exam problems.
- Remember to handle double letters (insert X) and odd-length plaintext (append X) during preprocessing.
- Know the three encryption rules (same row, same column, rectangle) and their decryption counterparts.
