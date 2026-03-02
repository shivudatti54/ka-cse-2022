# Divide and Conquer - Advanced

## Introduction

Divide and Conquer is one of the most fundamental algorithmic paradigms in computer science, forming the backbone of many efficient algorithms used in modern computing. The paradigm works by recursively breaking down a problem into smaller subproblems of the same type, solving those subproblems, and then combining their solutions to solve the original problem. This approach is particularly powerful because it often transforms problems with exponential time complexity into polynomial-time solutions.

In the context of Advanced Algorithms at the University of Delhi's MSc Computer Science program, this topic extends beyond basic sorting algorithms to explore sophisticated applications that demonstrate the true power of the divide and conquer paradigm. We will examine algorithms that achieve theoretical breakthroughs in computational complexity, such as Strassen's matrix multiplication (O(n^2.81) vs naive O(n³)), the Fast Fourier Transform (O(n log n) vs naive O(n²)), and the randomized QuickSelect algorithm for order statistics.

The importance of these advanced divide and conquer techniques cannot be overstated in contemporary computer science research. They form the foundation for many modern applications, from image processing and signal analysis to machine learning and computational geometry. Understanding these algorithms not only prepares students for advanced coursework but also provides essential tools for research in algorithms and computational theory.

## Key Concepts

### The Divide and Conquer Paradigm

The divide and conquer paradigm consists of three main steps:
1. **Divide**: Break the problem into smaller subproblems that are similar to the original problem
2. **Conquer**: Solve the subproblems recursively. If subproblems are small enough, solve them directly (base case)
3. **Combine**: Merge the solutions of subproblems into a solution for the original problem

The effectiveness of this approach depends critically on two factors: the ability to divide the problem into roughly equal-sized subproblems, and the efficiency of the combining step.

### Fast Fourier Transform (FFT)

The FFT is a landmark algorithm that computes the Discrete Fourier Transform (DFT) in O(n log n) time rather than O(n²). Given a polynomial of degree n-1, the DFT computes its values at n complex roots of unity.

The divide step in FFT exploits the property that even-indexed and odd-indexed coefficients can be processed separately:
- A(x) = A_even(x²) + x × A_odd(x²)
- This reduces the problem of computing DFT of size n to two DFTs of size n/2

The Cooley-Tukey algorithm implements this recursively, achieving the significant speedup that revolutionized signal processing. The FFT has numerous applications including image compression (JPEG), digital signal processing, polynomial multiplication, and convolution operations.

### Strassen's Matrix Multiplication

Traditional matrix multiplication of two n×n matrices requires Θ(n³) scalar multiplications. Strassen's algorithm achieves O(n^log₂7) ≈ O(n^2.81) by reducing the number of recursive matrix multiplications from 8 to 7.

The algorithm computes seven intermediate matrices (M1 through M7), each requiring one matrix multiplication. These are combined to produce the final result matrix. While the constant factors are larger than naive multiplication, for sufficiently large matrices, the asymptotic improvement is significant.

Research context: Strassen's work (1969) sparked intense research into fast matrix multiplication. The current best known exponent is approximately 2.3728596 (Coppersmith-Winograd algorithm and improvements), though these algorithms are primarily of theoretical interest due to large constants.

### Closest Pair of Points

The closest pair of points problem finds the minimum distance between any two points in a set of n points in the plane. A naive approach requires O(n²) comparisons, but divide and conquer achieves O(n log n).

The algorithm:
1. Sort points by x-coordinate
2. Divide the point set by a vertical line into two halves
3. Recursively find the closest pair in each half (d_left, d_right)
4. Let d = min(d_left, d_right)
5. Consider points within distance d of the dividing line
6. Sort the strip points by y-coordinate and scan, keeping at most 7 neighbors

The key insight is that at most 7 points can fit in a d×2d rectangle in the strip (packing argument), making the combine step O(n).

### Median Finding and Order Statistics

The selection problem asks for the kth smallest element in an unsorted array. While sorting solves this in O(n log n), the randomized QuickSelect algorithm achieves expected O(n) time.

QuickSelect works by:
1. Choosing a random pivot element
2. Partitioning the array around the pivot
3. Recursively selecting in the appropriate partition

The deterministic O(n) selection algorithm (Median of Medians) guarantees linear time by choosing pivots that are guaranteed to be better than random. It divides the array into groups of 5, finds medians of each group, and recursively finds the median of those medians.

### Master Theorem

The Master Theorem provides asymptotic analysis for recurrence relations of the form:
T(n) = aT(n/b) + f(n)

where a ≥ 1, b > 1, and f(n) is asymptotically positive. It compares f(n) with n^(log_b a):

1. **Case 1**: f(n) = O(n^(log_b a - ε)) → T(n) = Θ(n^(log_b a))
2. **Case 2**: f(n) = Θ(n^(log_b a) × log^k n) → T(n) = Θ(n^(log_b a) × log^(k+1) n)
3. **Case 3**: f(n) = Ω(n^(log_b a + ε)) and regularity condition → T(n) = Θ(f(n))

This theorem is essential for analyzing divide and conquer algorithms.

## Examples

### Example 1: FFT Polynomial Multiplication

**Problem**: Multiply two polynomials A(x) = 1 + 2x and B(x) = 3 + 4x

**Solution**:
Step 1: Represent polynomials in coefficient form: A = [1, 2], B = [3, 4]

Step 2: Pad to power of 2: degree 2 → size 4. A = [1, 2, 0, 0], B = [3, 4, 0, 0]

Step 3: Compute FFT of both polynomials (using recursive Cooley-Tukey)
- For size 4, the 4th roots of unity are: 1, i, -1, -i
- Computing DFT(A): [3, 1+2i, -1, 1-2i]
- Computing DFT(B): [7, 3+4i, -1, 3-4i]

Step 4: Pointwise multiplication
- DFT(Product) = [21, (1+2i)(3+4i), 1, (1-2i)(3-4i)]
- = [21, -5+10i, 1, -5-10i]

Step 5: Inverse FFT to get coefficients
- Result: [3, 10, 8, 0] representing 3 + 10x + 8x²

Verification: (1+2x)(3+4x) = 3 + 4x + 6x + 8x² = 3 + 10x + 8x² ✓

**Time Complexity**: O(n log n) where n is the next power of 2 greater than the degree sum.

### Example 2: Strassen's Matrix Multiplication

**Problem**: Multiply A = [[1,2],[3,4]] and B = [[5,6],[7,8]]

**Solution**:

Step 1: Compute the 7 intermediate matrices:
- M1 = a₁₁ × (b₁₂ - b₂₂) = 1 × (6-8) = -2
- M2 = (a₁₁ + a₁₂) × b₂₂ = (1+2) × 8 = 24
- M3 = (a₂₁ + a₂₂) × b₁₁ = (3+4) × 5 = 35
- M4 = a₂₂ × (b₂₁ - b₁₁) = 4 × (7-5) = 8
- M5 = (a₁₁ + a₂₂) × (b₁₁ + b₂₂) = (1+4) × (5+8) = 5 × 13 = 65
- M6 = (a₁₂ - a₂₂) × (b₂₁ + b₂₂) = (2-4) × (7+8) = -2 × 15 = -30
- M7 = (a₁₁ - a₂₁) × (b₁₁ + b₁₂) = (1-3) × (5+6) = -2 × 11 = -22

Step 2: Combine results:
- c₁₁ = M5 + M4 - M2 + M6 = 65 + 8 - 24 + (-30) = 19
- c₁₂ = M1 + M2 = -2 + 24 = 22
- c₂₁ = M3 + M4 = 35 + 8 = 43
- c₂₂ = M5 + M1 - M3 - M7 = 65 - 2 - 35 - (-22) = 50

Result: [[19, 22], [43, 50]]

Verification: Naive multiplication gives [[1×5+2×7, 1×6+2×8], [3×5+4×7, 3×6+4×8]] = [[19,22],[43,50]] ✓

### Example 3: QuickSelect for Order Statistics

**Problem**: Find the 3rd smallest element in [7, 2, 9, 1, 5, 6, 3, 8, 4]

**Solution**:
- Random pivot selection: say pivot = 5
- Partition around 5: [2, 1, 3, 4] | [5] | [7, 9, 6, 8]
- Position of pivot = 4 (1-indexed)
- k=3 < 4, so recurse on left partition [2, 1, 3, 4]
- Random pivot: say pivot = 2
- Partition: [1] | [2] | [3, 4]
- Position = 2, k=3 > 2, recurse on [3, 4]
- Random pivot: say pivot = 4
- Partition: [3] | [4]
- Position = 2, k=3 > 2, recurse on []
- Actually, k=3 at this point, we need 3rd smallest. Let's trace more carefully:
- At [3, 4] with k=3, both elements remain candidates
- If pivot=3: partition gives [3], position=1. k=3 > 1, continue with [4]
- k=2 now, pivot=4: position=1, k=2 > 1, continue... 

Final result: 3rd smallest is 4.

**Expected Time**: O(n) - significantly better than sorting for single order statistics.

## Exam Tips

1. **Master Theorem Applications**: Be prepared to apply the Master Theorem to analyze recurrence relations. Remember to identify a, b, and f(n) correctly, and determine which case applies.

2. **FFT Recurrence**: For FFT, T(n) = 2T(n/2) + Θ(n), giving T(n) = Θ(n log n) by Case 2 of Master Theorem.

3. **Strassen's Complexity**: Remember that Strassen achieves Θ(n^log₂7) ≈ Θ(n^2.807), a significant theoretical improvement over Θ(n³).

4. **QuickSelect vs Sorting**: For finding a single order statistic, QuickSelect's expected O(n) beats sorting's O(n log n). However, for guaranteed worst-case, use Median of Medians.

5. **Closest Pair Packing Argument**: The 7-point packing argument in the closest pair algorithm is crucial for the O(n log n) bound. Know why 7 and not 6.

6. **Divide and Conquer vs Dynamic Programming**: Remember that divide and conquer works best when subproblems are independent. When there's overlapping subproblems, dynamic programming is preferable.

7. **Algorithm Selection**: Understand when to use each algorithm. FFT for polynomial operations, Strassen for large matrices, QuickSelect for order statistics, closest pair for computational geometry.

8. **Proof of Correctness**: Study the correctness proofs, particularly the divide and combine justifications for each algorithm.