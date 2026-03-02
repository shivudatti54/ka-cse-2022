# Multiplication of Large Integers and Strassen's Matrix Multiplication

## Introduction

The analysis of efficient algorithms for fundamental computational problems has always been central to computer science. Two classic problems that appear deceptively simple yet reveal deep algorithmic insights are the multiplication of large integers and the multiplication of matrices. While the naive or "school method" for these operations provides straightforward solutions, the computational complexity of these naive approaches becomes prohibitive as problem sizes grow. This topic explores advanced techniques that significantly improve upon brute-force methods, reducing the asymptotic time complexity through clever algorithmic redesign.

The multiplication of large integers finds applications in cryptography (RSA encryption uses numbers with thousands of bits), scientific computing, and computer algebra systems. Traditional grade-school multiplication operates in O(n²) time, where n represents the number of digits. The Karatsuba algorithm, published in 1960, was the first to break this quadratic barrier, achieving O(n^log₂3) ≈ O(n^1.585) complexity. Similarly, Strassen's algorithm revolutionized matrix multiplication by reducing the complexity from O(n³) to O(n^log₂7) ≈ O(n^2.807), though with larger constant factors. Both algorithms exemplify the divide-and-conquer paradigm, where problems are recursively decomposed into smaller subproblems, solutions are combined, and the overall complexity is improved by reducing the number of fundamental operations.

## Key Concepts

### Large Integer Multiplication

**School Method Analysis**: Given two n-digit integers A and B, the traditional multiplication algorithm computes each digit of B multiplied by each digit of A, requiring n² single-digit multiplications and O(n²) additions. The time complexity is Θ(n²), which becomes impractical for integers with thousands or millions of digits.

**Karatsuba Algorithm**: The key insight that makes Karatsuba faster is recognizing that two n-digit numbers can be multiplied using only three (rather than four) recursive multiplications of half-sized numbers. Let A and B be two n-digit numbers where n is even. Split each number into two halves:

- A = A₁ × 10^(n/2) + A₀, where A₁ is the high half and A₀ is the low half
- B = B₁ × 10^(n/2) + B₀

The product AB expands to:
AB = A₁B₁ × 10^n + (A₁B₀ + A₀B₁) × 10^(n/2) + A₀B₀

The school method computes A₁B₁, A₁B₀, A₀B₁, and A₀B₀ separately (4 multiplications). Karatsuba observes that:
(A₁ + A₀)(B₁ + B₀) = A₁B₁ + A₁B₀ + A₀B₁ + A₀B₀

Rearranging: (A₁B₀ + A₀B₁) = (A₁ + A₀)(B₁ + B₀) - A₁B₁ - A₀B₀

Thus, we need only three multiplications: A₁B₁, A₀B₀, and (A₁ + A₀)(B₁ + B₀).

**Karatsuba Recurrence**: T(n) = 3T(n/2) + O(n), where the O(n) term accounts for additions, subtractions, and shifting (multiplication by powers of 10). Using the Master Theorem, since a = 3, b = 2, and f(n) = Θ(n), we have n^(log₂3) ≈ n^1.585. Since f(n) = O(n^(log₂3 - ε)) for some ε ≈ 0.085, the solution is T(n) = Θ(n^log₂3).

**Toom-Cook Generalization**: The Karatsuba method is a special case of Toom-Cook multiplication, which splits numbers into k parts, achieving complexity O(n^(log_k(k+1))). For k=3 (Toom-3), we use 5 multiplications instead of 9, giving complexity n^(log₃5) ≈ n^1.63.

**FFT-Based Multiplication**: For extremely large integers (thousands of digits), the Fast Fourier Transform (FFT) provides O(n log n) multiplication. The integers are represented as polynomials and their convolution is computed via FFT.

### Strassen's Matrix Multiplication

**Naive Analysis**: For two n×n matrices, the standard algorithm performs n³ scalar multiplications and (n-1)n² additions. The time complexity is Θ(n³).

**Strassen's Insight**: Volker Strassen discovered that matrix multiplication of 2×2 blocks can be accomplished with 7 instead of 8 multiplications. Given matrices A and B partitioned into four blocks each:

```
A = | A₁₁ A₁₂ | B = | B₁₁ B₁₂ |
 | A₂₁ A₂₂ | | B₂₁ B₂₂ |
```

The standard block multiplication requires 8 block multiplications:

- C₁₁ = A₁₁B₁₁ + A₁₂B₂₁
- C₁₂ = A₁₁B₁₂ + A₁₂B₂₂
- C₂₁ = A₂₁B₁₁ + A₂₂B₂₁
- C₂₂ = A₂₁B₁₂ + A₂₂B₂₂

Strassen defines seven intermediate matrices:

- M₁ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
- M₂ = (A₂₁ + A₂₂)B₁₁
- M₃ = A₁₁(B₁₂ - B₂₂)
- M₄ = A₂₂(B₂₁ - B₁₁)
- M₅ = (A₁₁ + A₁₂)B₂₂
- M₆ = (A₂₁ - A₁₁)(B₁₁ + B₁₂)
- M₇ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)

Then the result blocks are:

- C₁₁ = M₁ + M₄ - M₅ + M₇
- C₁₂ = M₃ + M₅
- C₂₁ = M₂ + M₄
- C₂₂ = M₁ - M₂ + M₃ + M₆

**Strassen's Recurrence**: T(n) = 7T(n/2) + O(n²), where the O(n²) term accounts for matrix additions and subtractions. Applying the Master Theorem with a = 7, b = 2, f(n) = n², we compute n^(log₂7) ≈ n^2.807. Since f(n) = O(n^(log₂7 - ε)) for some ε ≈ 0.193, we have T(n) = Θ(n^log₂7).

## Examples

### Example 1: Karatsuba Multiplication of 23 × 14

Let A = 23 and B = 14. Both are 2-digit numbers, so n/2 = 1 digit each.

Split: A₁ = 2, A₀ = 3; B₁ = 1, B₀ = 4

Compute the three products:

- A₁B₁ = 2 × 1 = 2
- A₀B₀ = 3 × 4 = 12
- (A₁ + A₀)(B₁ + B₀) = (2 + 3) × (1 + 4) = 5 × 5 = 25

Now compute middle term: (A₁B₀ + A₀B₁) = 25 - 2 - 12 = 11

Combine: AB = A₁B₁ × 10² + (A₁B₀ + A₀B₁) × 10¹ + A₀B₀
= 2 × 100 + 11 × 10 + 12 = 200 + 110 + 12 = 322

Verification: 23 × 14 = 322 ✓

Note: 4 multiplications would have been needed with school method (2×1, 2×4, 3×1, 3×4); Karatsuba used only 3.

### Example 2: Strassen's 2×2 Matrix Multiplication

Let A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]]

Compute the seven Strassen multiplications:

- M₁ = (A₁₁ + A₂₂)(B₁₁ + B₂₂) = (1 + 4)(5 + 8) = 5 × 13 = 65
- M₂ = (A₂₁ + A₂₂)B₁₁ = (3 + 4) × 5 = 7 × 5 = 35
- M₃ = A₁₁(B₁₂ - B₂₂) = 1 × (6 - 8) = 1 × (-2) = -2
- M₄ = A₂₂(B₂₁ - B₁₁) = 4 × (7 - 5) = 4 × 2 = 8
- M₅ = (A₁₁ + A₁₂)B₂₂ = (1 + 2) × 8 = 3 × 8 = 24
- M₆ = (A₂₁ - A₁₁)(B₁₁ + B₁₂) = (3 - 1) × (5 + 6) = 2 × 11 = 22
- M₇ = (A₁₂ - A₂₂)(B₂₁ + B₂₂) = (2 - 4) × (7 + 8) = (-2) × 15 = -30

Compute result blocks:

- C₁₁ = M₁ + M₄ - M₅ + M₇ = 65 + 8 - 24 + (-30) = 19
- C₁₂ = M₃ + M₅ = (-2) + 24 = 22
- C₂₁ = M₂ + M₄ = 35 + 8 = 43
- C₂₂ = M₁ - M₂ + M₃ + M₆ = 65 - 35 + (-2) + 22 = 50

Result C = [[19, 22], [43, 50]]

Verification using standard multiplication:
C = [[1×5+2×7, 1×6+2×8], [3×5+4×7, 3×6+4×8]] = [[5+14, 6+16], [15+28, 18+32]] = [[19, 22], [43, 50]] ✓

### Example 3: Complexity Comparison

For n = 1024 (matrix dimension or integer digit count):

| Algorithm     | Complexity | Approximate Operations      |
| ------------- | ---------- | --------------------------- |
| School Method | Θ(n²)      | 1,048,576                   |
| Karatsuba     | Θ(n^1.585) | ~38,000 (for integer mult.) |
| Strassen      | Θ(n^2.807) | ~7.4 × 10⁸ (for matrices)   |

## Exam Tips

1. **Understand the Paradigm**: Recognize that both Karatsuba and Strassen represent the divide-and-conquer design paradigm, not brute-force approaches—they reduce the number of recursive calls through algebraic manipulation.

2. **Master the Recurrence Relations**: Memorize T(n) = 3T(n/2) + O(n) for Karatsuba and T(n) = 7T(n/2) + O(n²) for Strassen; be able to solve these using the Master Theorem.

3. **Derivation Skills**: Understand how the middle term in Karatsuba is computed: A₁B₀ + A₀B₁ = (A₁ + A₀)(B₁ + B₀) - A₁B₁ - A₀B₀.

4. **Strassen's Seven Formulas**: Memorize all seven intermediate matrix computations; understand how the final blocks are assembled from these values.

5. **Practical Considerations**: Strassen's theoretical improvement comes with larger constant factors and numerical instability; it is practical only for large matrices (typically n > 512).

6. **Algorithm Selection**: For integer multiplication with small n, school method is faster; Karatsuba wins for moderate n; FFT dominates for very large n.

7. **Connection to Module**: While these algorithms improve upon naive approaches, they represent sophisticated alternatives to brute-force rather than being brute-force themselves—this reflects the evolution from simple to efficient algorithms.
