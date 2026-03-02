# Learning Purpose: Substitution Ciphers and Caesar Cipher

**1. Why this topic matters**
The Caesar cipher is the simplest and most well-known substitution cipher, making it the ideal starting point for studying cryptography in Module 1. It introduces the fundamental concept of replacing plaintext characters with ciphertext characters using a fixed shift, establishing the core vocabulary of encryption, decryption, keys, and key space that is used throughout the entire course.

**2. What you will learn**
You will learn how the Caesar cipher encrypts by shifting each letter a fixed number of positions in the alphabet and how to perform both encryption and decryption given a key. You will also calculate that the Caesar cipher has a key space of only 25, making it trivially vulnerable to brute-force attacks, and understand why this extremely small key space renders it insecure.

**3. How it connects to other topics**
The Caesar cipher is a special case of the monoalphabetic cipher and serves as the foundation for understanding all substitution techniques covered in Module 1, including the Playfair, Hill, and polyalphabetic ciphers. The weaknesses exposed by the Caesar cipher's tiny key space directly motivate the progression toward more complex classical ciphers and eventually the modern encryption systems studied in later modules.

**4. Real-world relevance**
While the Caesar cipher itself offers no practical security, it is universally used as a teaching tool to introduce encryption concepts in computer science education. The principle of substitution that it embodies remains fundamental to modern cipher design, and brute-force resistance through adequate key space size is a core requirement evaluated in every production cryptographic algorithm.
