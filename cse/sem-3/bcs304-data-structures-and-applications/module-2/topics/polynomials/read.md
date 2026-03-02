# Polynomials: Representation and Operations

## Introduction

Polynomials are fundamental mathematical expressions of the form P(x) = a₀ + a₁x + a₂x² + ... + aₙxⁿ, where coefficients a₀, a₁, ..., aₙ are constants and n represents the degree of the polynomial. In data structures, polynomials serve as an excellent application of linked lists, demonstrating how linear data structures can represent mathematical objects with variable numbers of terms. The study of polynomial representation and manipulation provides insight into sparse data structures, memory efficiency, and algorithmic design.

The representation of polynomials in computer memory depends on the density of non-zero terms. A **dense polynomial** contains non-zero coefficients for most exponent values, while a **sparse polynomial** has relatively few non-zero terms compared to its degree. Choosing the appropriate representation is crucial for efficient storage and computation, particularly when performing operations such as addition, subtraction, multiplication, and evaluation.

## Key Concepts

### Polynomial Representation

#### Dense Representation Using Arrays

In dense representation, an array of size (n+1) stores all coefficients from a₀ to aₙ, where n is the degree. This approach is suitable when most coefficients are non-zero.

```
P(x) = 3 + 2x + 5x² + 0x³ + 0x⁴ + x⁵
Array: [3, 2, 5, 0, 0, 1]
```

**Memory Complexity**: O(n) where n is the degree

#### Sparse Representation Using Linked Lists

For sparse polynomials with few non-zero terms, a linked list structure stores only non-zero terms. Each node contains:

- **coef**: The coefficient value
- **exp**: The exponent value
- **next**: Pointer to the next term

```c
typedef struct PolyNode {
    float coef;
    int exp;
    struct PolyNode *next;
} PolyNode;
```

**Advantage**: Memory proportional to the number of non-zero terms (k), not the degree (n).

### Polynomial Addition

Given two polynomials P(x) and Q(x), addition produces R(x) = P(x) + Q(x). The algorithm compares exponents of corresponding terms:

**Algorithm**:

1. Initialize pointers to the heads of both polynomials
2. Compare exponents of current terms:
   - If equal: add coefficients, create new term if sum is non-zero
   - If P's exponent > Q's exponent: copy P's term to result
   - If Q's exponent > P's exponent: copy Q's term to result
3. Advance pointers accordingly
4. Copy remaining terms

**Time Complexity**: O(m + n) where m and n are the number of terms in the two polynomials.

**Proof of Correctness**: The algorithm maintains the invariant that all terms with exponents less than the current comparison point have been correctly processed and added to the result. By exhaustively comparing exponents and advancing through both lists, every term is processed exactly once.

### Polynomial Subtraction

Subtraction follows the same algorithm as addition, except coefficients are subtracted instead of added. If P(x) - Q(x) is computed, the coefficient of each term in Q is negated before the addition process.

### Polynomial Multiplication

Given P(x) of degree m and Q(x) of degree n, the product has degree m+n with at most (m+1)(n+1) terms before combining like terms.

**Algorithm**:

1. Initialize result polynomial as zero
2. For each term in P(x):
   - Multiply with each term in Q(x)
   - Add the resulting term to the result polynomial
3. Combine terms with same exponents

**Time Complexity**: O(m × n × k) where k is the number of terms in the result after combining like terms. Without optimization, it's O(m × n).

### Polynomial Evaluation

Evaluating P(x₀) for a given value x₀ can use Horner's Rule for efficiency:

**Horner's Rule**: P(x) = a₀ + a₁x + a₂x² + ... + aₙxⁿ = a₀ + x(a₁ + x(a₂ + ... + x(aₙ)...))

```c
float evaluate(PolyNode *poly, float x) {
    float result = 0;
    PolyNode *current = poly;
    while (current != NULL) {
        result = result * x + current->coef;
        current = current->next;
    }
    return result;
}
```

**Time Complexity**: O(k) where k is the number of non-zero terms.

## Examples

### Example 1: Sparse Polynomial Addition

Given:

- P(x) = 5x³ + 3x + 2 (terms: (5,3), (3,1), (2,0))
- Q(x) = 4x³ + 2x² + 1 (terms: (4,3), (2,2), (1,0))

**Solution**:

- Compare exponents: 3 = 3 → add: 5 + 4 = 9 → term: 9x³
- Compare exponents: Q has 2, P has 1 → term: 2x²
- Compare exponents: 1 > 0 → term: 3x
- Compare exponents: 0 = 0 → add: 2 + 1 = 3 → term: 3

**Result**: R(x) = 9x³ + 2x² + 3x + 3

### Example 2: Array-Based Dense Addition

Given:

- P(x) = [1, 2, 3] representing 1 + 2x + 3x²
- Q(x) = [4, 5, 6] representing 4 + 5x + 6x²

**Solution**: Add corresponding coefficients

- Result: [1+4, 2+5, 3+6] = [5, 7, 9]

**Result**: R(x) = 5 + 7x + 9x²

### Example 3: Horner's Rule Evaluation

Evaluate P(x) = 2x³ + 3x² + 5x + 7 at x = 2

**Using Horner's Rule**:

- Step 1: result = 0 × 2 + 2 = 2
- Step 2: result = 2 × 2 + 3 = 7
- Step 3: result = 7 × 2 + 5 = 19
- Step 4: result = 19 × 2 + 7 = 45

**Result**: P(2) = 45

**Verification**: 2(8) + 3(4) + 5(2) + 7 = 16 + 12 + 10 + 7 = 45 ✓

## Exam Tips

1. **Representation Choice**: Use array representation for dense polynomials (degree close to number of terms) and linked list for sparse polynomials to optimize memory.

2. **Complexity Analysis**: Remember that array representation gives O(1) coefficient access while linked list requires O(k) traversal for the k-th term.

3. **Polynomial Addition Invariants**: In the linked list addition algorithm, maintain the invariant that all terms with exponents less than the current comparison point have been processed.

4. **Horner's Rule Efficiency**: Always use Horner's rule for polynomial evaluation—reduces time from O(n²) to O(n) and prevents overflow in integer arithmetic.

5. **Multiplication Complexity**: When multiplying polynomials of degrees m and n, the naive algorithm has O(mn) complexity; using hash tables can improve this for sparse polynomials.

6. **Memory Considerations**: Linked list representation stores only non-zero terms, making it space-efficient for sparse polynomials where k << n (number of terms much less than degree).

7. **Edge Cases**: Always handle polynomials with zero coefficients, empty polynomials (zero polynomial), and polynomials of different degrees during operations.
