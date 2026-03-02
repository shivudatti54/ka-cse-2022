# Symmetric Ciphers: AES and DES

## Introduction
Symmetric-key cryptography forms the backbone of modern data encryption, with AES (Advanced Encryption Standard) and DES (Data Encryption Standard) being two pivotal algorithms. DES, developed in the 1970s, was the first standardized cipher for commercial use but became vulnerable to brute-force attacks due to its 56-bit key size. AES, adopted in 2001 as FIPS 197, uses 128/192/256-bit keys and remains unbroken despite extensive cryptanalysis.

These ciphers are fundamental to secure communication systems, including TLS/SSL, VPNs, and disk encryption. Understanding their structure is crucial for analyzing modern cryptographic systems and developing new variants resistant to quantum computing threats. Recent research focuses on AES side-channel attacks and optimized hardware implementations using FPGA/ASIC.

## Key Concepts
1. **DES Structure**: 
   - 64-bit block size, 56-bit key
   - 16 Feistel rounds with expansion permutation, S-boxes (6→4 bits), and P-box
   - Key schedule generates 48-bit round keys
   - Vulnerable to differential cryptanalysis and 2⁵⁶ complexity brute-force

2. **AES (Rijndael)**: 
   - SPN (Substitution-Permutation Network) structure
   - 128-bit block, 128/192/256-bit keys
   - Key expansion creates 44/52/60 32-bit words
   - Round steps: 
     * ByteSub (S-box using GF(2⁸) inversion)
     * ShiftRows 
     * MixColumns (matrix multiplication in GF(2⁸))
     * AddRoundKey

3. **Security Aspects**:
   - AES: Resistant to linear/differential cryptanalysis due to tight diffusion
   - DES: Broken in 22 hours using COPACOBANA (2006)
   - Meet-in-the-middle attacks on 3DES

## Examples

**Example 1: DES Round Calculation**
Given:
- Right half (R₀): 32-bit 0x12345678
- Round key (K₁): 48-bit 0xA1B2C3D4E5F6
- Calculate f(R₀, K₁):

Steps:
1. Expand R₀ to 48 bits using E-box: 0x12345678 → 0x... (specific permutation)
2. XOR with K₁: 0x... ⊕ 0xA1B2C3D4E5F6 = 0x...
3. Split into 8×6-bit chunks → S-box substitution
4. Permute using P-box → 32-bit output

**Example 2: AES MixColumns**
For state column [0xDB, 0x13, 0x53, 0x45]:
- Represent as polynomials in GF(2⁸)
- Multiply by matrix:
  ```
  [02 03 01 01]
  [01 02 03 01]
  [01 01 02 03]
  [03 01 01 02]
  ```
- Use xtime for multiplication: 0xDB•02 = (0xDB << 1) ⊕ 0x1B (if carry)

**Example 3: TLS 1.3 Key Exchange**
Show how AES-GCM (Galois/Counter Mode) combines AES-CTR with authentication:
1. Generate nonce
2. CTR mode encryption: Plaintext ⊕ AES(nonce+counter)
3. GHASH for authentication tag

## Exam Tips
1. Always compare AES/DES in terms of structure (SPN vs Feistel), key size, and cryptanalysis resistance
2. Memorize AES round numbers: 10 (128-bit), 12 (192), 14 (256)
3. DES S-boxes provide non-linearity; AES S-box uses affine transformation over GF(2⁸)
4. For numericals, practice key scheduling (AES key expansion) and MixColumns math
5. Understand modern attacks: Timing attacks on AES cache, Linear Cryptanalysis on DES
6. 3DES uses EDE (Encrypt-Decrypt-Encrypt) with 2/3 keys
7. Always mention NIST standards and replacement timelines (DES: 1977-2005, AES: 2001-present)

Length: 2500 words