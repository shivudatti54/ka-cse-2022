# Description of the RSA Algorithm - Summary

## Key Definitions and Concepts

- **RSA**: Public-key cryptosystem using prime factorization and modular arithmetic
- **Prime Numbers**: Integers >1 divisible only by 1 and themselves (e.g., 2, 3, 5)
- **Coprimality**: Two numbers with GCD = 1 (e.g., 8 and 15)
- **φ(n) (Euler's Totient)**: Count of numbers <n coprime to n. For primes p,q: φ(pq)=(p-1)(q-1)
- **Modular Inverse**: d is inverse of e mod φ(n) if ed ≡ 1 mod φ(n)
- **Public Key**: (e, n) used for encryption
- **Private Key**: (d, n) used for decryption

## Important Formulas and Theorems

1. **Key Generation**:
   `n = p × q` (product of two primes)  
   `φ(n) = (p-1)(q-1)`  
   `1 < e < φ(n)` where GCD(e, φ(n)) = 1  
   `d ≡ e⁻¹ mod φ(n)` (using Extended Euclidean Algorithm)

2. **Encryption**:  
   `C ≡ Mᵉ mod n` (M = plaintext, C = ciphertext)

3. **Decryption**:  
   `M ≡ Cᵈ mod n`

4. **Euler's Theorem**:  
   If M and n are coprime, `M^{φ(n)} ≡ 1 mod n`

5. **Extended Euclidean Algorithm**:  
   Finds x,y such that `ax + by = GCD(a,b)`

## Key Points

- RSA security relies on difficulty of factoring large numbers into primes
- Public exponent (e) is typically 65537 (common balance between security and speed)
- Private exponent (d) must be kept secret
- Message M must satisfy 0 ≤ M < n
- Encryption is computationally expensive → used for key exchange
- Digital signatures use reverse operations (encrypt with private key)
- Key sizes typically 2048-4096 bits for modern security
- Padding schemes (PKCS#1 v1.5/OAEP) are essential for real-world security

## Common Mistakes to Avoid

- Using p and q that are too small (vulnerable to factorization)
- Choosing e that isn't coprime with φ(n)
- Confusing public/private key roles (encrypt with public, decrypt with private)
- Forgetting that M must be <n (requires message splitting for large data)

## Revision Tips

1. **Practice Numerical Examples**: Work through full key generation and encryption/decryption with small primes (e.g., p=3, q=11)
2. **Formula Flashcards**: Memorize φ(n) calculation, encryption/decryption equations
3. **Proof Understanding**: Be able to explain why M^{ed} ≡ M mod n using Euler's theorem
4. **Compare & Contrast**: Create table comparing RSA with Diffie-Hellman and ECC algorithms
