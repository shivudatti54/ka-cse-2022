# Strassen's Matrix Multiplication

## Introduction

Matrix multiplication is one of the most fundamental operations in computer science, with applications spanning machine learning, computer graphics, scientific computing, and image processing. The standard naive approach to multiplying two n×n matrices requires O(n³) scalar multiplications, which becomes prohibitively expensive for large matrices encountered in real-world applications.

In 1969, Volker Strassen made a groundbreaking discovery that would revolutionize how we think about matrix multiplication. Through clever algebraic manipulation, Strassen demonstrated that it is possible to multiply two 2×2 matrices using only 7 multiplications instead of 8, while using 18 additions and subtractions. This seemingly modest improvement—reducing from 8 to 7 multiplications—has profound implications when extended to large matrices using the divide-and-conquer paradigm. The resulting algorithm achieves a time complexity of O(n^log₂7) ≈ O(n^2.807), which is asymptotically faster than the naive O(n³) approach.

For competitive DU examinations, understanding Strassen's algorithm is essential as it demonstrates how mathematical insight can lead to algorithmic improvements. This topic also connects to broader themes in algorithm design: divide-and-conquer, recursive problem-solving, and the analysis of asymptotic complexity.

## Key Concepts

### The Standard Matrix Multiplication Problem

Given two n×n matrices A and B, the product matrix C = A × B is defined such that:

C[i][j] = Σ(k=1 to n) A[i][k] × B[k][j]

For 2×2 matrices, this requires 8 multiplications and 4 additions:

```
| c11 c12 |   | a11 a12 |   | b11 b12 |
| c21 c22 | = | a21 a22 | × | b21 b22 |
```

Where:
- c11 = a11×b11 + a12×b21
- c12 = a11×b12 + a12×b22
- c21 = a21×b11 + a22×b21
- c22 = a21×b12 + a22×b22

### Strassen's Key Insight

Strassen observed that by introducing 7 intermediate calculations (M1 through M7), we can compute the product using only 7 multiplications. The elegance lies in trading one multiplication for several additions/subtractions—a worthwhile exchange since multiplication is typically more expensive than addition.

### The Seven Strassen Multiplications

For 2×2 matrices, define these seven products:

```
M1 = (a11 + a22) × (b11 + b22)
M2 = (a21 + a22) × b11
M3 = a11 × (b12 - b22)
M4 = a22 × (b21 - b11)
M5 = (a11 + a12) × b22
M6 = (a21 - a11) × (b11 + b12)
M7 = (a12 - a22) × (b21 + b22)
```

Then compute the result matrix:

```
C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6
```

### Recursive Algorithm Structure

For matrices of size n (where n is a power of 2), the algorithm:

1. **Divide**: Partition each matrix into four quadrants of size n/2 × n/2
2. **Conquer**: Recursively compute the 7 Strassen products (M1-M7)
3. **Combine**: Use the formulas above to compute the four quadrants of the result

If n = 1 (base case), simply multiply the single elements.

### Time Complexity Analysis

Let T(n) be the time complexity for multiplying two n×n matrices using Strassen:

- Base case: T(1) = O(1)
- Recursive case: T(n) = 7T(n/2) + O(n²)

Using the Master Theorem:
- a = 7, b = 2, f(n) = n²
- n^(log₂7) ≈ n^2.807
- Since f(n) = O(n^(log₂7 - ε)) where ε ≈ 0.807

Therefore, T(n) = Θ(n^log₂7) ≈ Θ(n^2.807)

This is asymptotically better than Θ(n³) from naive multiplication.

## Examples

### Example 1: 2×2 Matrix Multiplication Using Strassen

Multiply:
```
A = | 1  2 |    B = | 5  6 |
    | 3  4 |        | 7  8 |
```

**Step 1: Compute the 7 products**

```
M1 = (a11 + a22) × (b11 + b22) = (1 + 4) × (5 + 8) = 5 × 13 = 65
M2 = (a21 + a22) × b11 = (3 + 4) × 5 = 7 × 5 = 35
M3 = a11 × (b12 - b22) = 1 × (6 - 8) = 1 × (-2) = -2
M4 = a22 × (b21 - b11) = 4 × (7 - 5) = 4 × 2 = 8
M5 = (a11 + a12) × b22 = (1 + 2) × 8 = 3 × 8 = 24
M6 = (a21 - a11) × (b11 + b12) = (3 - 1) × (5 + 6) = 2 × 11 = 22
M7 = (a12 - a22) × (b21 + b22) = (2 - 4) × (7 + 8) = (-2) × 15 = -30
```

**Step 2: Compute result matrix elements**

```
C11 = M1 + M4 - M5 + M7 = 65 + 8 - 24 + (-30) = 19
C12 = M3 + M5 = -2 + 24 = 22
C21 = M2 + M4 = 35 + 8 = 43
C22 = M1 - M2 + M3 + M6 = 65 - 35 + (-2) + 22 = 50
```

**Result:**
```
C = | 19  22 |
    | 43  50 |
```

**Verification:** Using standard multiplication:
- c11 = 1×5 + 2×7 = 5 + 14 = 19 ✓
- c12 = 1×6 + 2×8 = 6 + 16 = 22 ✓
- c21 = 3×5 + 4×7 = 15 + 28 = 43 ✓
- c22 = 3×6 + 4×8 = 18 + 32 = 50 ✓

### Example 2: Complexity Comparison

For n = 1024 (which is 2¹⁰):

| Algorithm | Approximate Operations |
|-----------|----------------------|
| Naive     | (1024)³ = 1,073,741,824 |
| Strassen  | (1024)^2.807 ≈ 1024² × 1024^0.807 ≈ 1,048,576 × 7.3 ≈ 7.6 million |

The speedup ratio is approximately 1,073,741,824 / 7,600,000 ≈ 141x!

### Example 3: Practical Considerations

**When to use Strassen's algorithm:**
- For very large matrices (n > 1000 typically)
- When numerical stability is not critical
- When memory overhead is acceptable

**When NOT to use Strassen:**
- For small matrices (naive is faster due to lower constant factors)
- In precision-sensitive applications (more floating-point operations)
- When memory is constrained (requires more auxiliary space)

## Exam Tips

1. **Memorize the 7 formulas**: The M1-M7 calculations are essential. Practice writing them from memory until they're automatic.

2. **Understand the trade-off**: Strassen reduces multiplications but increases additions. This works because multiplication is typically more expensive than addition in practice.

3. **Master the recurrence relation**: T(n) = 7T(n/2) + O(n²) is fundamental. Be able to solve it using the Master Theorem.

4. **Remember the asymptotic improvement**: O(n^2.807) vs O(n³) — know this comparison and understand what "log₂7" represents.

5. **Know the base case**: Matrix multiplication of 1×1 matrices (scalar multiplication) is the base case for recursion.

6. **Padding for non-power-of-2**: If n is not a power of 2, pad matrices with zeros to the next power of 2—this is a common exam point.

7. **Space complexity**: Strassen requires O(n²) auxiliary space for storing intermediate results, same as standard multiplication.

8. **Numerical stability**: Be aware that Strassen has slightly less numerical stability than standard multiplication due to more addition/subtraction operations.

9. **Connection to divide-and-conquer**: This algorithm exemplifies the divide-and-conquer paradigm—remember the three steps: divide, conquer, combine.

10. **Current best algorithms**: The Coppersmith-Winograd algorithm achieves O(n^2.373) but is not practical due to very large constant factors. Strassen remains the most practically useful improvement.