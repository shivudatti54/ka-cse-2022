# Polynomial Representation Using Data Structures


## Table of Contents

- [Polynomial Representation Using Data Structures](#polynomial-representation-using-data-structures)
- [1. Mathematical Foundation and Definitions](#1-mathematical-foundation-and-definitions)
  - [1.1 Formal Definition of Polynomials](#11-formal-definition-of-polynomials)
  - [1.2 Polynomial Abstract Data Type (ADT)](#12-polynomial-abstract-data-type-adt)
- [2. Dense Coefficient Array Representation](#2-dense-coefficient-array-representation)
  - [2.1 Conceptual Foundation](#21-conceptual-foundation)
  - [2.2 Implementation](#22-implementation)
  - [2.3 Polynomial Addition in Dense Representation](#23-polynomial-addition-in-dense-representation)
  - [2.4 Polynomial Evaluation: Horner's Method](#24-polynomial-evaluation-horners-method)
- [3. Sparse (Term-Based) Array Representation](#3-sparse-term-based-array-representation)
  - [3.1 Motivation and Mathematical Justification](#31-motivation-and-mathematical-justification)
  - [3.2 Implementation](#32-implementation)
- [4. Linked List Representation](#4-linked-list-representation)
  - [4.1 Node Structure](#41-node-structure)
  - [4.2 Complexity Analysis](#42-complexity-analysis)
- [5. Comparison of Representations](#5-comparison-of-representations)
- [6. Multiple Choice Questions](#6-multiple-choice-questions)

## 1. Mathematical Foundation and Definitions

### 1.1 Formal Definition of Polynomials

A **polynomial** is a fundamental algebraic construct with extensive applications in computer science, particularly in numerical analysis, computer graphics, signal processing, and symbolic computation. Understanding the mathematical properties of polynomials is essential for designing efficient data structures for their representation and manipulation.

**Definition 1.1 (Polynomial over a Field):** Let F be a field (typically ℝ, the field of real numbers). A polynomial P(x) of degree n (where n ∈ ℕ₀) is defined as:

```
P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀ = Σᵢ₌₀ⁿ aᵢxⁱ
```

where:

- **Coefficients**: The scalars a₀, a₁, ..., aₙ ∈ F constitute the coefficient vector
- **Leading Coefficient**: aₙ ≠ 0 (the coefficient of the highest power)
- **Degree**: deg(P) = n = max{i | aᵢ ≠ 0}, the highest exponent with non-zero coefficient
- **Constant Term**: a₀, the coefficient of x⁰

**Definition 1.2 (Term):** A term is an ordered pair (aᵢ, i) where aᵢ ∈ F is the coefficient and i ∈ ℕ₀ is the exponent. A polynomial is thus a finite set of terms T = {(c₀, e₀), ..., (cₖ, eₖ)}.

**Definition 1.3 (Sparse vs Dense):** A polynomial with k non-zero terms, where k << n (the degree), is termed **sparse**. Conversely, when k ≈ n+1, the polynomial is **dense**.

### 1.2 Polynomial Abstract Data Type (ADT)

The Polynomial ADT provides a mathematical abstraction specifying the interface without implementation details, enabling different representation strategies.

**Data Structure:**
A finite set of terms T = {(c₀, e₀), (c₁, e₁), ..., (cₖ, eₖ)} where each eᵢ ∈ ℕ₀ and cᵢ ∈ F.

**Operations:**

| Operation   | Signature                   | Description                         |
| ----------- | --------------------------- | ----------------------------------- |
| create      | create() → Polynomial       | Returns empty polynomial            |
| add         | add(P, Q) → Polynomial      | Returns sum P + Q                   |
| multiply    | multiply(P, Q) → Polynomial | Returns product P × Q               |
| evaluate    | evaluate(P, x₀) → F         | Returns P(x₀) using Horner's method |
| degree      | degree(P) → ℕ               | Returns deg(P)                      |
| coefficient | coefficient(P, e) → F       | Returns coefficient of xᵉ           |
| display     | display(P) → void           | Outputs polynomial in standard form |

---

## 2. Dense Coefficient Array Representation

### 2.1 Conceptual Foundation

The **dense representation** stores all coefficients from 0 to n (the degree), utilizing array indices directly as exponents. For a polynomial of degree n, an array of size n+1 is allocated, where index i stores coefficient aᵢ.

**Theorem 2.1 (Space Complexity):** For a polynomial P(x) of degree n, the dense array representation requires Θ(n) storage space.

_Proof:_ The representation maintains an array `coeff[0...n]` of size n+1, storing all coefficients including zeros. The space complexity is S(n) = (n+1) × sizeof(element), which is asymptotically Θ(n). ∎

### 2.2 Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_DEGREE 1000

typedef struct {
    int *coeff;     // Dynamic array of coefficients
    int degree;     // Current degree of polynomial
    int maxSize;    // Allocated array size
} Polynomial;

// Initialize polynomial with specified maximum degree
Polynomial createPoly(int maxDegree) {
    Polynomial p;
    p.maxSize = maxDegree + 1;
    p.coeff = (int*)calloc(p.maxSize, sizeof(int));
    p.degree = 0;
    return p;
}

// Read polynomial from user input
void readPoly(Polynomial *p) {
    int i;
    printf("Enter degree of polynomial (max %d): ", p->maxSize - 1);
    scanf("%d", &p->degree);

    if (p->degree >= p->maxSize) {
        p->maxSize = p->degree + 1;
        p->coeff = (int*)realloc(p->coeff, p->maxSize * sizeof(int));
    }

    // Initialize all coefficients to zero
    for (i = 0; i < p->maxSize; i++)
        p->coeff[i] = 0;

    // Read coefficients in descending order of exponent
    for (i = p->degree; i >= 0; i--) {
        printf("Enter coefficient of x^%d: ", i);
        scanf("%d", &p->coeff[i]);
    }
}

// Display polynomial in standard form
void displayPoly(Polynomial p) {
    int i;
    int first = 1;

    if (p.degree == 0 && p.coeff[0] == 0) {
        printf("0\n");
        return;
    }

    for (i = p.degree; i >= 0; i--) {
        if (p.coeff[i] != 0) {
            if (!first)
                printf(" %s ", (p.coeff[i] > 0) ? "+" : "-");
            else if (p.coeff[i] < 0)
                printf("-");

            int absCoeff = abs(p.coeff[i]);
            if (i == 0 || absCoeff != 1)
                printf("%d", absCoeff);

            if (i == 1)
                printf("x");
            else if (i > 1)
                printf("x^%d", i);

            first = 0;
        }
    }
    printf("\n");
}
```

### 2.3 Polynomial Addition in Dense Representation

**Theorem 2.2 (Addition Complexity):** Given two polynomials P(x) of degree m and Q(x) of degree n, the addition operation P + Q using dense representation has time complexity Θ(max(m, n)).

_Proof:_ The algorithm iterates from 0 to max(m, n), performing a single addition at each index. The loop executes max(m, n) + 1 times, yielding Θ(max(m, n)) operations. ∎

```c
// Add two polynomials: R = P + Q
Polynomial addPoly(Polynomial P, Polynomial Q) {
    int maxDeg = (P.degree > Q.degree) ? P.degree : Q.degree;
    Polynomial R = createPoly(maxDeg);
    R.degree = maxDeg;

    int i;
    for (i = 0; i <= maxDeg; i++) {
        int pc = (i <= P.degree) ? P.coeff[i] : 0;
        int qc = (i <= Q.degree) ? Q.coeff[i] : 0;
        R.coeff[i] = pc + qc;
    }

    // Adjust actual degree
    while (R.degree > 0 && R.coeff[R.degree] == 0)
        R.degree--;

    return R;
}
```

### 2.4 Polynomial Evaluation: Horner's Method

**Theorem 2.3 (Horner's Method Correctness):** Given polynomial P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₀, Horner's method computes P(x₀) correctly.

_Proof:_ By induction on degree n, Horner's method computes:

- Step k: bₖ = bₖ₊₁ × x₀ + aₖ
- Base case: bₙ = aₙ
  Expanding recursively: b₀ = (((aₙ × x₀ + aₙ₋₁) × x₀ + ...) × x₀ + a₀ = P(x₀). ∎

**Theorem 2.4 (Evaluation Complexity):** Horner's method evaluates a polynomial of degree n in Θ(n) time with O(1) auxiliary space.

_Proof:_ The algorithm performs n iterations, each with one multiplication and one addition. No additional data structures are required beyond the accumulator variable. ∎

```c
// Evaluate polynomial using Horner's method
double evaluatePoly(Polynomial P, double x) {
    double result = 0.0;
    int i;

    for (i = P.degree; i >= 0; i--)
        result = result * x + P.coeff[i];

    return result;
}
```

---

## 3. Sparse (Term-Based) Array Representation

### 3.1 Motivation and Mathematical Justification

For sparse polynomials where k << n (k = number of non-zero terms), dense representation wastes significant memory. The sparse representation stores only non-zero terms as (coefficient, exponent) pairs.

**Theorem 3.1 (Space Complexity):** Let k be the number of non-zero terms in a polynomial of degree n. Sparse representation requires Θ(k) space, compared to Θ(n) for dense representation.

_Proof:_ Each non-zero term requires two integers (coefficient, exponent), so space = 2k = Θ(k). Since k << n for sparse polynomials, we achieve space savings of factor approximately n/k. ∎

**Example:** For P(x) = 8x¹⁰⁰⁰ + 5x² + 10 (degree 1000, k=3):

- Dense: 1001 integers
- Sparse: 6 integers (3 pairs)

### 3.2 Implementation

```c
#define MAX_TERMS 100

typedef struct {
    int coeff;
    int expo;
} Term;

typedef struct {
    Term *terms;
    int numTerms;
    int capacity;
} SparsePoly;

// Create sparse polynomial
SparsePoly createPolySparse(int capacity) {
    SparsePoly p;
    p.capacity = capacity;
    p.numTerms = 0;
    p.terms = (Term*)malloc(capacity * sizeof(Term));
    return p;
}

// Insert term maintaining descending order by exponent
void insertTerm(SparsePoly *p, int coeff, int expo) {
    if (p->numTerms >= p->capacity) {
        printf("Error: Capacity exceeded\n");
        return;
    }

    int i = p->numTerms - 1;
    while (i >= 0 && p->terms[i].expo < expo) {
        p->terms[i + 1] = p->terms[i];
        i--;
    }
    p->terms[i + 1].coeff = coeff;
    p->terms[i + 1].expo = expo;
    p->numTerms++;
}

// Add two sparse polynomials
SparsePoly addSparsePoly(SparsePoly P, SparsePoly Q) {
    SparsePoly R = createPolySparse(P.numTerms + Q.numTerms);

    int i = 0, j = 0;
    while (i < P.numTerms && j < Q.numTerms) {
        if (P.terms[i].expo == Q.terms[j].expo) {
            int sum = P.terms[i].coeff + Q.terms[j].coeff;
            if (sum != 0)
                insertTerm(&R, sum, P.terms[i].expo);
            i++; j++;
        } else if (P.terms[i].expo > Q.terms[j].expo) {
            insertTerm(&R, P.terms[i].coeff, P.terms[i].expo);
            i++;
        } else {
            insertTerm(&R, Q.terms[j].coeff, Q.terms[j].expo);
            j++;
        }
    }

    while (i < P.numTerms) {
        insertTerm(&R, P.terms[i].coeff, P.terms[i].expo);
        i++;
    }
    while (j < Q.numTerms) {
        insertTerm(&R, Q.terms[j].coeff, Q.terms[j].expo);
        j++;
    }

    return R;
}
```

---

## 4. Linked List Representation

### 4.1 Node Structure

For dynamic polynomial manipulation with frequent insertions/deletions, linked list representation provides O(1) insertion at the head.

```c
typedef struct PolyNode {
    int coeff;
    int expo;
    struct PolyNode *next;
} PolyNode;

// Create new node
PolyNode* createNode(int coeff, int expo) {
    PolyNode *node = (PolyNode*)malloc(sizeof(PolyNode));
    node->coeff = coeff;
    node->expo = expo;
    node->next = NULL;
    return node;
}

// Insert term in descending order
void insertSorted(PolyNode **head, int coeff, int expo) {
    PolyNode *newNode = createNode(coeff, expo);

    if (*head == NULL || (*head)->expo < expo) {
        newNode->next = *head;
        *head = newNode;
        return;
    }

    PolyNode *temp = *head;
    while (temp->next && temp->next->expo > expo)
        temp = temp->next;

    newNode->next = temp->next;
    temp->next = newNode;
}
```

### 4.2 Complexity Analysis

**Theorem 4.1 (Linked List Addition):** Adding two polynomials with k₁ and k₂ terms respectively requires O(k₁ + k₂) time.

_Proof:_ The algorithm performs a single pass through both lists, comparing exponents and advancing pointers. Each iteration processes one node from either list, requiring k₁ + k₂ iterations total. ∎

---

## 5. Comparison of Representations

| Criterion        | Dense Array | Sparse Array | Linked List  |
| ---------------- | ----------- | ------------ | ------------ |
| Space (dense P)  | Θ(n)        | Θ(n)         | Θ(n)         |
| Space (sparse P) | Θ(n)        | Θ(k)         | Θ(k)         |
| Addition Time    | Θ(max(m,n)) | Θ(k₁ + k₂)   | Θ(k₁ + k₂)   |
| Evaluation Time  | Θ(n)        | Θ(k log k)   | Θ(k)         |
| Insertion        | O(n)        | O(k)         | O(1) at head |
| Cache Locality   | Excellent   | Good         | Poor         |

---

## 6. Multiple Choice Questions

**Question 1:** For a polynomial P(x) = 5x¹⁰⁰ + 3x⁵ + 2x + 1, what is the space requirement using dense representation?

- (a) 4 integers
- (b) 101 integers
- (c) 100 integers
- (d) 5 integers

**Answer:** (b) 101 integers. Dense representation stores all coefficients from degree 0 to degree 100, requiring 100+1 = 101 integer slots.

**Question 2:** The time complexity of adding two sparse polynomials with k₁ and k₂ non-zero terms using array-based sparse representation is:

- (a) O(k₁ + k₂)
- (b) O(k₁ × k₂)
- (c) O(max(k₁, k₂))
- (d) O(n) where n is max degree

**Answer:** (a) O(k₁ + k₂). The algorithm performs a single merge-like pass through both term arrays.

**Question 3:** Horner's method evaluates a polynomial of degree n in:

- (a) O(n²) time
- (b) O(n log n) time
- (c) O(n) time
- (d) O(2ⁿ) time

**Answer:** (c) O(n) time. Each of the n iterations performs one multiplication and one addition.

**Question 4:** Which representation is most suitable for a polynomial with only 3 non-zero terms out of degree 1000?

- (a) Dense array
- (b) Sparse array
- (c) Linked list
- (d) All have equal space complexity

**Answer:** (b) Sparse array. Space = Θ(3) = O(1) vs Θ(1000) for dense representation.
