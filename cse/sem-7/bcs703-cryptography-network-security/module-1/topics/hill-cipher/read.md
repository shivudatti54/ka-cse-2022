# Module 1: Classical Encryption Techniques

## Topic: Hill Cipher

### 1. Introduction and Historical Context

The Hill Cipher, invented by Lester S. Hill in 1929, represents a significant advancement in classical cryptography as one of the first polygraphic substitution ciphers that operates on multiple letters simultaneously. Unlike monoalphabetic substitution ciphers (such as Caesar or substitution ciphers) that encrypt single characters individually, the Hill Cipher encrypts blocks of `m` characters using linear algebra. This polygraphic approach provides substantial protection against frequency analysis attacks that exploit the statistical distribution of individual letters in plaintext.

The fundamental innovation of the Hill Cipher lies in its use of matrix operations modulo 26, where the alphabet is mapped to integers 0-25. The cipher's security rests on the difficulty of solving systems of linear equations without knowledge of the key matrix, although as we shall see, it exhibits significant vulnerabilities that preclude its use in modern cryptographic applications.

### 2. Mathematical Foundation

#### 2.1 Modulo 26 Arithmetic

All operations in the Hill Cipher are performed in the ring Z₂₆ = {0, 1, 2, ..., 25} with addition and multiplication defined modulo 26. This corresponds to the English alphabet where A=0, B=1, ..., Z=25. The choice of modulo 26 is deliberate as it accommodates all letters, though it presents challenges since 26 = 2 × 13 is not prime, meaning not all non-zero elements have multiplicative inverses.

**Definition:** An element `a ∈ Z₂₆` has a multiplicative inverse `a⁻¹` if and only if `gcd(a, 26) = 1`. The elements coprime to 26 are: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 (12 elements).

#### 2.2 Invertibility Condition for Key Matrices

**Theorem:** An `m × m` matrix **K** over Z₂₆ is invertible (has a multiplicative inverse **K⁻¹**) if and only if `gcd(det(K), 26) = 1`.

**Proof:** Let **K** be an invertible matrix over Z₂₆. Then there exists **K⁻¹** such that **K** × **K⁻¹** = **I** (the identity matrix). Taking determinants on both sides:
`det(K) × det(K⁻¹) = det(I) = 1` (mod 26)

This implies that `det(K)` must have a multiplicative inverse in Z₂₆. For an element to have a multiplicative inverse in Z₂₆, it must be coprime to 26. Therefore, `gcd(det(K), 26) = 1`.

Conversely, if `gcd(det(K), 26) = 1`, then `det(K)` has a multiplicative inverse `d⁻¹` in Z₂₆. The classical formula for the matrix inverse is:
**K⁻¹ = d⁻¹ × adj(K)** (mod 26)

Since `d⁻¹` exists, we can compute the adjugate matrix `adj(K)` and multiply by `d⁻¹` to obtain **K⁻¹**. This establishes that **K** is invertible. ∎

### 3. Key Generation

The key for an m×m Hill Cipher is an m×m matrix **K** with the following properties:

1. All entries are integers in {0, 1, ..., 25}
2. `gcd(det(K), 26) = 1` (determinant coprime to 26)

**Example:** For m=2, let **K** = [[3, 3], [2, 5]]

- det(K) = (3×5 - 3×2) = 15 - 6 = 9
- gcd(9, 26) = 1 → Valid key

### 4. Encryption Process

Given plaintext **P** and key matrix **K**, the encryption proceeds as follows:

1. **Numerical Mapping:** Convert each letter to its numeric equivalent (A=0, B=1, ..., Z=25)
2. **Block Formation:** Partition the numerical plaintext into column vectors **P₁, P₂, ..., Pₙ** of size m×1
3. **Padding:** If the plaintext length is not divisible by m, pad with dummy characters (commonly 'X' = 23)
4. **Matrix Multiplication:** For each block, compute **Cᵢ = K × Pᵢ** (mod 26)
5. **Ciphertext Conversion:** Convert the resulting numeric vectors back to letters

**Encryption Formula:** **C** = **K** × **P** (mod 26)

### 5. Decryption Process

Decryption requires computing the modular inverse of the key matrix **K**.

**Theorem:** If **K** is invertible modulo 26, then plaintext **P** is recovered as **P** = **K⁻¹** × **C** (mod 26).

**Proof:** Starting from the encryption formula **C** = **K** × **P** (mod 26), multiply both sides by **K⁻¹**:
**K⁻¹** × **C** = **K⁻¹** × (**K** × **P**) = (**K⁻¹** × **K**) × **P** = **I** × **P** = **P** (mod 26)

Thus, **P** = **K⁻¹** × **C** (mod 26). ∎

#### 5.1 Computing the Modular Inverse

To find **K⁻¹** for a 2×2 matrix [[a, b], [c, d]]:

1. Compute determinant: d = ad - bc (mod 26)
2. Find d⁻¹ such that d × d⁻¹ ≡ 1 (mod 26)
3. Compute adjugate: adj(K) = [[d, -b], [-c, a]] (mod 26)
4. Compute inverse: **K⁻¹** = d⁻¹ × adj(K) (mod 26)

**Example (continued):** For **K** = [[3, 3], [2, 5]]:

- det(K) = 9
- Find 9⁻¹ mod 26: 9 × 3 = 27 ≡ 1 (mod 26), so 9⁻¹ = 3
- adj(K) = [[5, -3], [-2, 3]] = [[5, 23], [24, 3]] (mod 26)
- **K⁻¹** = 3 × [[5, 23], [24, 3]] = [[15, 69], [72, 9]] = [[15, 17], [20, 9]] (mod 26)

### 6. Worked Example: Complete Encryption and Decryption

**Plaintext:** "VTU" (we'll use "V", "T", "U")
**Key:** **K** = [[3, 3], [2, 5]]
**Add padding:** "VTUX" → P = [21, 19, 20, 23]

**Block 1: "VT" (P₁ = [21, 19]ᵀ)**

- C₁ = K × P₁ = [[3, 3], [2, 5]] × [21, 19]
- = [3×21 + 3×19, 2×21 + 5×19] = [63+57, 42+95] = [120, 137]
- Mod 26: [120 mod 26, 137 mod 26] = [120-4×26, 137-5×26] = [16, 7]
- 16=Q, 7=H → "QH"

**Block 2: "UX" (P₂ = [20, 23]ᵀ)**

- C₂ = K × P₂ = [[3, 3], [2, 5]] × [20, 23]
- = [3×20 + 3×23, 2×20 + 5×23] = [60+69, 40+115] = [129, 155]
- Mod 26: [129 mod 26, 155 mod 26] = [129-4×26, 155-5×26] = [25, 25]
- 25=Z, 25=Z → "ZZ"

**Ciphertext:** "QHZZ"

**Decryption Verification:**

- **K⁻¹** = [[15, 17], [20, 9]]

**Block 1: "QH" (C₁ = [16, 7]ᵀ)**

- P₁ = K⁻¹ × C₁ = [[15, 17], [20, 9]] × [16, 7]
- = [15×16 + 17×7, 20×16 + 9×7] = [240+119, 320+63] = [359, 383]
- Mod 26: [359-13×26, 383-14×26] = [359-338, 383-364] = [21, 19]
- 21=V, 19=T → "VT" ✓

**Block 2: "ZZ" (C₂ = [25, 25]ᵀ)**

- P₂ = K⁻¹ × C₂ = [[15, 17], [20, 9]] × [25, 25]
- = [15×25 + 17×25, 20×25 + 9×25] = [375+425, 500+225] = [800, 725]
- Mod 26: [800-30×26, 725-27×26] = [800-780, 725-702] = [20, 23]
- 20=U, 23=X → "UX" ✓

### 7. Cryptanalysis of Hill Cipher

#### 7.1 Known-Plaintext Attack

The Hill Cipher is highly vulnerable to known-plaintext attacks. If an attacker obtains m² plaintext-ciphertext pairs (m consecutive plaintext letters and their corresponding ciphertext), they can recover the key matrix by solving a system of linear equations.

**Attack Procedure:**

1. Obtain m plaintext-ciphertext pairs: (P₁, C₁), (P₂, C₂), ..., (Pₘ, Cₘ)
2. Form matrices P = [P₁ P₂ ... Pₘ] and C = [C₁ C₂ ... Cₘ]
3. Solve for K: C = K × P (mod 26)
4. Compute K = C × P⁻¹ (mod 26), provided P is invertible

This vulnerability renders the cipher insecure for practical applications, as any partial compromise of plaintext leads to complete key recovery.

#### 7.2 Chosen-Plaintext Attack

An attacker with chosen-plaintext capability can encrypt m linearly independent plaintext blocks and recover the key in the same manner as known-plaintext attack, making the cipher even more vulnerable.

#### 7.3 Limitations

1. **Linearity:** The cipher exhibits perfect linearity, providing no diffusion or confusion in the Shannon sense
2. **Determinant Restrictions:** Only matrices with determinants coprime to 26 can be used, reducing key space
3. **Block Size Constraints:** Larger block sizes (m > 2) require more known plaintext for attacks
4. **No Authentication:** Like all classical ciphers, it provides no message authentication

### 8. Summary

| Aspect                      | Details                                                            |
| --------------------------- | ------------------------------------------------------------------ |
| **Type**                    | Polygraphic substitution cipher                                    |
| **Block Size**              | m × m key matrix                                                   |
| **Key Space**               | 26^(m²) matrices, but only ~26^(m²) × 0.4 are invertible           |
| **Encryption**              | C = K × P (mod 26)                                                 |
| **Decryption**              | P = K⁻¹ × C (mod 26)                                               |
| **Security**                | Vulnerable to known-plaintext attacks; not suitable for modern use |
| **Historical Significance** | Introduced application of linear algebra to cryptography           |

The Hill Cipher, while historically significant as a bridge between classical and modern cryptography, cannot provide adequate security for contemporary applications. Its study remains valuable for understanding the mathematical foundations of cryptography and the transition from classical to modern block ciphers.
