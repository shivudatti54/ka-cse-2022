# Sequences and Summations

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University

---

## 1. Introduction

**Sequences and Summations** form the mathematical backbone of computer science, particularly in the analysis of algorithms and the understanding of computational complexity. Whether you are analyzing how long a sorting algorithm takes to execute, computing the total memory usage of a recursive program, or understanding the growth rates of functions, summations appear everywhere in CS.

This topic is a core component of the **Discrete Mathematical Structures** paper under the NEP 2024 UGCF curriculum at Delhi University. Understanding how to manipulate sequences and compute summations efficiently is essential not only for algorithm analysis but also for database systems, network protocols, and data science.

---

## 2. Understanding Sequences

### 2.1 Definition

A **sequence** is an ordered list of elements (typically numbers) indexed by natural numbers. Unlike a set, the order matters in a sequence, and repetitions are allowed.

**Formal Definition:** A sequence {a_n} is a function from ℕ (or a subset of ℕ) to a set S, where a_n represents the n-th term.

### 2.2 Types of Sequences

#### Arithmetic Sequence
A sequence where the difference between consecutive terms is constant.

**Formula:** a_n = a_1 + (n-1)d

Where:
- a_1 = first term
- d = common difference
- n = number of terms

**Example:** 2, 5, 8, 11, 14, ... (a_1 = 2, d = 3)

#### Geometric Sequence
A sequence where the ratio between consecutive terms is constant.

**Formula:** a_n = a_1 × r^(n-1)

Where:
- a_1 = first term
- r = common ratio
- n = number of terms

**Example:** 3, 6, 12, 24, 48, ... (a_1 = 3, r = 2)

#### Fibonacci Sequence
A famous sequence where each term is the sum of the two preceding terms.

**Formula:** F_n = F_{n-1} + F_{n-2} with F_1 = 1, F_2 = 1

**Example:** 1, 1, 2, 3, 5, 8, 13, 21, ...

---

## 3. Summation Notation (Sigma Notation)

### 3.1 Introduction

When we need to add a sequence of numbers, we use **summation notation** (also called sigma notation because of the Σ symbol).

**General Form:**

$$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + a_{m+2} + \cdots + a_n$$

Where:
- Σ (sigma) = summation symbol
- i = index of summation (dummy variable)
- m = lower bound
- n = upper bound
- a_i = term at position i

### 3.2 Properties of Summations

1. **Constant Multiple Rule:**
   $$\sum_{i=m}^{n} c \cdot a_i = c \sum_{i=m}^{n} a_i$$

2. **Sum/Difference Rule:**
   $$\sum_{i=m}^{n} (a_i \pm b_i) = \sum_{i=m}^{n} a_i \pm \sum_{i=m}^{n} b_i$$

3. **Splitting Rule:**
   $$\sum_{i=m}^{n} a_i = \sum_{i=m}^{k} a_i + \sum_{i=k+1}^{n} a_i \quad \text{where } m \leq k < n$$

4. **Change of Index:**
   $$\sum_{i=m}^{n} a_i = \sum_{j=m+p}^{n+p} a_{j-p}$$

### 3.3 Important Observations

- The index variable is "dummy" — it can be changed without affecting the sum
- Always verify the bounds: the lower bound is inclusive, upper bound is inclusive
- For empty range (n < m), the sum is defined as 0

---

## 4. Closed-Form Summation Formulas

A **closed-form expression** is a formula that can be evaluated in a finite number of operations. These formulas are essential for algorithm analysis as they give us exact counts without iterating.

### 4.1 Sum of First n Integers

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \frac{n^2 + n}{2}$$

**Proof by Induction:**

*Base Case (n = 1):* LHS = 1, RHS = 1(2)/2 = 1 ✓

*Inductive Step:* Assume true for n = k
$$\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$$

For n = k + 1:
$$\sum_{i=1}^{k+1} i = \frac{k(k+1)}{2} + (k+1)$$
$$= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$

This matches the formula with n = k + 1. ∎

### 4.2 Sum of First n Squares

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$

### 4.3 Sum of First n Cubes

$$\sum_{i=1}^{n} i^3 = \left(\frac{n(n+1)}{2}\right)^2 = \frac{n^2(n+1)^2}{4}$$

**Interesting Property:** The sum of cubes equals the square of the sum of first n integers!

### 4.4 Geometric Series

For r ≠ 1:

$$\sum_{i=0}^{n} r^i = \frac{r^{n+1} - 1}{r - 1} = \frac{1 - r^{n+1}}{1 - r}$$

**Infinite Geometric Series (|r| < 1):**

$$\sum_{i=0}^{\infty} r^i = \frac{1}{1 - r}$$

### 4.5 Harmonic Numbers

$$H_n = \sum_{i=1}^{n} \frac{1}{i} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$$

No simple closed form exists, but we use the approximation:
$$H_n \approx \ln(n) + \gamma + \frac{1}{2n} - \frac{1}{12n^2}$$
where γ ≈ 0.57721 (Euler-Mascheroni constant)

---

## 5. Worked Examples for Algorithm Analysis

Algorithm analysis is one of the most important applications of summations in Computer Science. Let's examine concrete examples.

### Example 1: Analyzing a Nested Loop

**Problem:** Determine the time complexity of the following code:

```python
def example1(n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count
```

**Analysis:**

The outer loop runs n times (i = 0 to n-1).

For each i, the inner loop runs from j = i to n-1, which is (n - i) times.

Total operations:
$$\sum_{i=0}^{n-1} (n - i) = \sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

**Verification with code:**

```python
def example1(n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count

# Test for n = 5
print(example1(5))  # Output: 15
print(5*6/2)        # Output: 15.0 ✓
```

The closed-form gives us Θ(n²) time complexity.

### Example 2: Divide and Conquer — Binary Search Count

**Problem:** In binary search, how many comparisons are made in the worst case?

**Analysis:**

Each step halves the search space. The number of steps until size becomes 1:
$$1 = \frac{n}{2^k} \Rightarrow 2^k = n \Rightarrow k = \log_2 n$$

Total comparisons (worst case):
$$T(n) = 1 + \log_2 n = \Theta(\log n)$$

### Example 3: Summation with Polynomial Growth

**Problem:** Analyze:

```python
def example3(n):
    total = 0
    for i in range(1, n+1):
        for j in range(1, i*i + 1):
            total += j
    return total
```

**Analysis:**

- Outer loop: i = 1 to n
- Inner loop: j = 1 to i²

Total operations:
$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} = \Theta(n^3)$$

---

## 6. Double Summations

When we have nested loops with indices depending on each other, we encounter **double summations**.

### 6.1 Definition

$$\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} = \sum_{i=1}^{m} \left(\sum_{j=1}^{n} a_{ij}\right)$$

### 6.2 Evaluating Double Summations

**Example:** Evaluate $$\sum_{i=1}^{3} \sum_{j=1}^{i} (i + j)$$

**Solution:**

First, compute inner sum for each i:

- i = 1: j = 1 → (1 + 1) = 2
- i = 2: j = 1, 2 → (2 + 1) + (2 + 2) = 3 + 4 = 7
- i = 3: j = 1, 2, 3 → (3+1) + (3+2) + (3+3) = 4 + 5 + 6 = 15

Total: 2 + 7 + 15 = **24**

**Alternative using summation formulas:**

$$\sum_{i=1}^{3} \sum_{j=1}^{i} (i + j) = \sum_{i=1}^{3} \left(i \cdot i + \sum_{j=1}^{i} j\right)$$

$$= \sum_{i=1}^{3} \left(i^2 + \frac{i(i+1)}{2}\right) = \sum_{i=1}^{3} \left(\frac{2i^2 + i^2 + i}{2}\right)$$

$$= \sum_{i=1}^{3} \left(\frac{3i^2 + i}{2}\right) = \frac{1}{2}\left(3\sum_{i=1}^{3} i^2 + \sum_{i=1}^{3} i\right)$$

$$= \frac{1}{2}\left(3 \cdot \frac{3 \cdot 4 \cdot 7}{6} + \frac{3 \cdot 4}{2}\right) = \frac{1}{2}(3 \cdot 14 + 6) = \frac{1}{2}(42 + 6) = 24 \checkmark$$

---

## 7. Practice Problems

### Problem 1
Find the closed form: $$\sum_{k=1}^{100} (3k - 2)$$

**Solution:**
$$\sum_{k=1}^{100} (3k - 2) = 3\sum_{k=1}^{100} k - \sum_{k=1}^{100} 2$$
$$= 3 \cdot \frac{100 \cdot 101}{2} - 2 \cdot 100$$
$$= 3 \cdot 5050 - 200 = 15150 - 200 = 14950$$

### Problem 2
Evaluate: $$\sum_{k=0}^{10} 2^k$$

**Solution:** This is a geometric series with r = 2, n = 10
$$\sum_{k=0}^{10} 2^k = \frac{2^{11} - 1}{2 - 1} = 2048 - 1 = 2047$$

### Problem 3
Find the order of growth: $$\sum_{i=1}^{n} \sum_{j=1}^{i} 1$$

**Solution:**
$$\sum_{i=1}^{n} \sum_{j=1}^{i} 1 = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2)$$

---

## 8. Multiple Choice Questions

### MCQ 1
What is the closed form of $$\sum_{i=1}^{n} i^2$$?

A) n(n+1)/2  
B) n(n+1)(2n+1)/6  
C) n²(n+1)²/4  
D) (n+1)²/2

**Answer:** B  
**Explanation:** The formula for sum of squares is n(n+1)(2n+1)/6, which can be derived by induction or using known mathematical results.

### MCQ 2
Find $$\sum_{i=3}^{8} i$$

A) 26  
B) 22  
C) 35  
D) 33

**Answer:** A (26)  
**Explanation:** Sum from 3 to 8 = 3+4+5+6+7+8 = 26. The previous version incorrectly marked B=22, which is wrong because 3+4+5+6+7+8 = 26 ≠ 22.

### MCQ 3
The time complexity of nested loops:
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
is:

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(n³)

**Answer:** C  
**Explanation:** The outer loop runs n times, and for each i, the inner loop runs n times. Total iterations = n × n = n² = Θ(n²).

### MCQ 4
What is $$\sum_{k=0}^{\infty} \left(\frac{1}{2}\right)^k$$ equal to?

A) 1  
B) 2  
C) 4  
D) 1/2

**Answer:** B (2)  
**Explanation:** Infinite geometric series with r = 1/2, |r| < 1, sum = 1/(1-r) = 1/(1-1/2) = 2.

### MCQ 5
For the code:
```python
count = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        count += 1
```
The number of executions of `count += 1` is:

A) n²  
B) n(n+1)/2  
C) n(n-1)/2  
D) n³

**Answer:** B  
**Explanation:** This is the sum of first n integers: ∑ᵢ₌₁ⁿ i = n(n+1)/2

---

## 9. Flashcards (University Level)

### Card 1
**Term:** Closed-form summation  
**Definition:** An expression that can be evaluated in a finite number of standard operations without iteration.

### Card 2
**Term:** Arithmetic sequence  
**Definition:** A sequence where consecutive terms differ by a constant d. Formula: a_n = a₁ + (n-1)d

### Card 3
**Term:** Geometric series  
**Definition:** A series where each term is obtained by multiplying the previous term by a constant ratio r. Sum: ∑ᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹-1)/(r-1)

### Card 4
**Term:** Harmonic number Hₙ  
**Definition:** Hₙ = ∑ᵢ₌₁ⁿ (1/i), representing the sum of reciprocals of first n positive integers.

### Card 5
**Term:** Order of growth of ∑i=1ⁿ i³  
**Definition:** Θ(n⁴), since the closed form is n²(n+1)²/4 ≈ n⁴/4

### Card 6
**Term:** Change of index in summations  
**Definition:** A technique to rewrite ∑ᵢ₌ₘⁿ aᵢ as ∑ⱼ₌ₘ₊ₚⁿ₊ₚ aⱼ₋ₚ by substituting j = i + p

### Card 7
**Term:** Double summation  
**Definition:** A summation with two indices, evaluated by first solving the inner summation, then the outer: ∑ᵢ∑ⱼ aᵢⱼ

### Card 8
**Term:** Master theorem application  
**Definition:** Used to analyze divide-and-conquer recurrences; relates recurrence T(n) = aT(n/b) + f(n) to its closed-form complexity

---

## 10. Key Takeaways

1. **Sequences** are ordered lists indexed by natural numbers; arithmetic sequences have constant difference, geometric sequences have constant ratio.

2. **Summation notation (sigma)** provides a concise way to represent repeated addition: ∑ᵢ₌ₘⁿ aᵢ = aₘ + aₘ₊₁ + ... + aₙ

3. **Closed-form formulas** are essential for algorithm analysis:
   - ∑i = n(n+1)/2
   - ∑i² = n(n+1)(2n+1)/6
   - ∑i³ = [n(n+1)/2]²
   - Geometric: ∑rⁱ = (rⁿ⁺¹-1)/(r-1)

4. **Algorithm analysis** uses these formulas to determine time/space complexity; nested loops typically yield polynomial or geometric sums.

5. **Double summations** require evaluating the inner sum first, then the outer sum; bounds often depend on the outer index.

6. **Properties** like constant multiple, sum/difference, and splitting rules enable algebraic manipulation of summations.

7. **Understanding these concepts** is fundamental to the DU CS curriculum and forms the basis for analyzing algorithm efficiency in subsequent courses like Data Structures, Design and Analysis of Algorithms, and Theory of Computation.

---

*Prepared according to Delhi University NEP 2024 UGCF Syllabus for BSc (Hons) Computer Science — Paper: Discrete Mathematical Structures*