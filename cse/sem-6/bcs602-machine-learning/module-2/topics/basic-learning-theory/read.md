# Basic Learning Theory

## Introduction

**Computational Learning Theory (CLT)** is the mathematical study of learning algorithms, providing theoretical guarantees about their performance. Unlike empirical machine learning that focuses on practical implementations, learning theory answers fundamental questions: What can be learned? How much data is required? What are the inherent limitations of learning algorithms? This theoretical framework, pioneered by researchers like Leslie Valiant, Vladimir Vapnik, and Michael Kearns, provides the foundational principles that explain when and why machine learning algorithms succeed or fail.

The field emerged from the recognition that empirical success alone is insufficient—we need formal guarantees to understand the conditions under which learning is possible. Computational learning theory bridges the gap between practical algorithms and mathematical rigor, enabling us to make precise statements about generalization, sample complexity, and the representational power of hypothesis classes.

## Hypothesis Space

### Definition and Formal Framework

The **hypothesis space** (denoted **H**) is the set of all possible hypotheses (functions) that a learning algorithm can output. Formally, given an input space **X** and output space **Y**, a hypothesis is a function h: **X** → **Y**. The hypothesis space **H** is a subset of all possible functions from **X** to **Y**.

The choice of hypothesis space is fundamental to learning because it determines:

- What concepts the algorithm can represent
- The complexity of the search for a good hypothesis
- The theoretical guarantees that can be provided

**Examples of Hypothesis Spaces:**

For a binary classification problem where **X** = ℝ^d and **Y** = {+1, -1}:

1. **Linear Classifiers in d dimensions:**

```
H_linear = { h(x) = sign(w·x + b) | w ∈ ℝ^d, b ∈ ℝ }
```

The VC dimension of this hypothesis class is d + 1.

2. **Axis-aligned Rectangles in ℝ²:**

```
H_rect = { h(x) = +1 if x ∈ [a₁,b₁] × [a₂,b₂], else -1 }
```

The VC dimension is 4.

3. **Decision Trees of depth d:**

```
H_DT(d) = { all decision trees with maximum depth d }
```

The VC dimension grows with the number of leaves.

### Key Properties

- **Expressive Power**: Larger hypothesis spaces can represent more complex patterns
- **Search Complexity**: Larger spaces are harder to search efficiently
- **Overfitting Risk**: Smaller spaces may underfit; larger spaces may overfit
- **Representability**: The target concept must be contained in H for perfect learning

## Version Space

### Definition

The **version space** VS(H, D) is the subset of hypotheses in **H** that are consistent with all training examples. Given a training set S = {(x₁,y₁), (x₂,y₂), ..., (xₘ,yₘ)} drawn from distribution D, the version space is:

```
VS(H, S) = { h ∈ H | h(xᵢ) = yᵢ for all i = 1, 2, ..., m }
```

### The Candidate Elimination Algorithm

The Candidate Elimination Algorithm maintains two boundary hypotheses:

- **Most General Hypothesis (G)**: The most general hypothesis consistent with all positive examples
- **Most Specific Hypothesis (S)**: The most specific hypothesis consistent with all examples

The version space is bounded by these extremes: all hypotheses more general than G and more specific than S are consistent.

### Version Space Convergence

As training data increases, the version space shrinks. Under certain conditions:

- If the target concept is in H, the version space converges to the target
- If the version space becomes empty, the target concept is not in H
- The rate of convergence depends on the hypothesis space complexity

## Sample Complexity

### Problem Definition

**Sample complexity** answers: How many training examples are needed to learn a concept reliably? Formally, given accuracy parameter ε (0 < ε < 1/2) and confidence parameter δ (0 < δ < 1/2), we want m such that with probability at least (1-δ), the learned hypothesis has error at most ε.

### Sample Complexity for Finite Hypothesis Spaces

**Theorem**: Let H be a finite hypothesis space with |H| hypotheses. For any target concept in H, with probability at least (1-δ), a hypothesis with error at most ε can be learned from m samples where:

```
m ≥ (1/ε) × (ln|H| + ln(1/δ))
```

**Proof**:

Let H₁, H₂, ..., Hₖ be the "bad" hypotheses in H, each with error > ε on the true distribution. For any fixed bad hypothesis hᵢ, the probability that it appears consistent with all m training examples is:

```
P(hᵢ is consistent with m examples) ≤ (1 - ε)^m ≤ e^(-εm)
```

Using the union bound, the probability that ANY bad hypothesis is consistent with all m examples is:

```
P(any bad h is consistent) ≤ |H| × e^(-εm)
```

We want this probability to be at most δ:

```
|H| × e^(-εm) ≤ δ
e^(-εm) ≤ δ/|H|
-εm ≤ ln(δ/|H|)
m ≥ (1/ε) × (ln|H| + ln(1/δ))
```

This completes the proof. ∎

### Implications

| Factor                | Effect on Sample Complexity      |
| --------------------- | -------------------------------- | --- | ------------- |
| Desired accuracy (ε)  | m ∝ 1/ε (inversely proportional) |
| Confidence (δ)        | m ∝ ln(1/δ) (logarithmic)        |
| Hypothesis space size | m ∝ ln                           | H   | (logarithmic) |

## PAC Learning Framework

### Introduction

The **Probably Approximately Correct (PAC)** learning framework, introduced by Leslie Valiant in 1984, formalizes when a concept can be learned from examples. It provides theoretical guarantees about learning quality without requiring perfect learning.

### Formal Definition

A concept class C is **PAC-learnable** if there exists an algorithm A such that for any:

- Target concept c ∈ C
- Distribution D over the input space X
- Accuracy parameter ε: 0 < ε < 1/2
- Confidence parameter δ: 0 < δ < 1/2

The algorithm A, given at least m(ε, δ) training examples drawn from D, outputs a hypothesis h such that:

```
P_D(error_D(h) ≤ ε) ≥ 1 - δ
```

where error*D(h) = Pr*{x~D}[h(x) ≠ c(x)]

**Key interpretations:**

- **(1-δ) confidence**: With high probability, the learning succeeds
- **ε accuracy**: When successful, the hypothesis is approximately correct
- **m depends on ε and δ**: More samples needed for higher accuracy/confidence

### Sample Complexity Bounds

For finite hypothesis spaces, the sample complexity is:

```
m(ε, δ) ≤ (1/ε) × (log|H| + log(1/δ))
```

A concept class is **efficiently PAC-learnable** if m(ε, δ) is polynomial in 1/ε and 1/δ.

### Agnostic PAC Learning

In realistic scenarios, the target concept may not be perfectly representable. **Agnostic PAC learning** handles this by not assuming c ∈ H:

The algorithm outputs h such that:

```
P_D[h(x) ≠ y] ≤ min_{h'∈H} P_D[h'(x) ≠ y] + ε
```

This guarantees learning even when no perfect hypothesis exists.

## VC Dimension

### Definitions

The **Vapnik-Chervonenkis (VC) dimension** measures the expressive power of a hypothesis class. It quantifies the maximum number of points that can be perfectly classified in all possible ways.

**Definition 1 (Shattering)**: A hypothesis class H **shatters** a set S ⊆ X if for every labeling of S, there exists h ∈ H that produces that labeling.

**Definition 2 (VC Dimension)**: The VC dimension of H, denoted VC(H), is the size of the largest set that can be shattered by H. Formally:

```
VC(H) = max{ |S| : S ⊆ X is shattered by H }
```

If arbitrarily large finite sets can be shattered, VC(H) = ∞.

### Examples and Proofs

**Example 1: Linear Classifiers in ℝ²**

_Claim_: VC dimension = 3

_Proof_:

- **Can shatter 3 points**: Any 3 non-collinear points can be shattered. For all 2³ = 8 labelings, we can find a linear separator.
- **Cannot shatter 4 points**: Consider the XOR configuration (four points at corners of a square). Label opposite corners with +1 and the other two with -1. No linear separator exists for this labeling.
- Therefore, VC(H) = 3. ∎

**Example 2: Intervals on the Real Line**

_Claim_: VC dimension = 2

_Proof_:

- Can shatter 2 points: Given any labeling of 2 points, an interval can be chosen to separate them appropriately.
- Cannot shatter 3 points: For 3 points x₁ < x₂ < x₃, the labeling (+, -, +) cannot be achieved by a single interval.
- Therefore, VC(H) = 2. ∎

### VC Dimension of Common Hypothesis Classes

| Hypothesis Class                 | VC Dimension                  |
| -------------------------------- | ----------------------------- |
| Linear classifiers in ℝ^d        | d + 1                         |
| Axis-aligned rectangles in ℝ^d   | 2d                            |
| Decision trees with k leaves     | O(k log k)                    |
| Neural networks (with w weights) | O(w)                          |
| Sin(x) function                  | ∞ (can shatter infinite sets) |

### Fundamental Theorem of Statistical Learning

The fundamental theorem connects VC dimension to learnability:

**Theorem**: For a hypothesis class H with finite VC dimension d, for any distribution D, with probability at least (1-δ):

```
error_D(h) ≤ error_S(h) + O(√(d/m × log(m/d) + log(1/δ)))
```

This shows that:

- Generalization error = training error + complexity term
- The complexity term decreases as m increases
- VC dimension controls the rate of convergence

## No-Free-Lunch Theorem

### Statement

The No-Free-Lunch (NFL) theorem states that for any two learning algorithms A and B, there exists a distribution D on which A performs better than B, and vice versa. Formally:

```
∀ algorithms A, B, ∃ distribution D: E_D[L_D(A)] ≥ E_D[L_D(B)]
```

### Implications

1. **No universal best learner**: No algorithm is universally superior
2. **Assumptions are essential**: Learning is only possible with prior assumptions (inductive bias)
3. **The need for domain knowledge**: Understanding the problem structure is crucial

### Resolution

The NFL theorem does not negate learning—it emphasizes that:

- We must encode assumptions about the problem into the hypothesis space
- Good performance on real-world problems comes from matching assumptions to reality
- Theoretical guarantees require assumptions about the data distribution

## Assessment

### Multiple Choice Questions

**Question 1**: Consider a hypothesis space H with |H| = 1000. Using the sample complexity bound for PAC learning, how many training examples are needed to achieve ε = 0.1 and δ = 0.05?

A) 37
B) 69
C) 100
D) 230

**Answer**: B
**Explanation**: Using m ≥ (1/ε)(ln|H| + ln(1/δ)) = (1/0.1)(ln(1000) + ln(20)) = 10(6.908 + 2.996) = 10(9.904) ≈ 69

---

**Question 2**: What is the VC dimension of linear classifiers in ℝ³?

A) 2
B) 3
C) 4
D) 5

**Answer**: C
**Explanation**: For linear classifiers in d dimensions, VC dimension = d + 1. In ℝ³, d = 3, so VC = 4.

---

**Question 3**: In PAC learning, if we decrease ε (want higher accuracy) while keeping δ constant, what happens to the required sample complexity?

A) Decreases
B) Increases
C) Stays the same
D) Becomes infinite

**Answer**: B
**Explanation**: Sample complexity m ∝ 1/ε. As ε decreases (higher accuracy required), more samples are needed.

---

**Question 4**: A hypothesis class H can shatter 5 points but cannot shatter 6 points. What is VC(H)?

A) 4
B) 5
C) 6
D) Cannot be determined

**Answer**: B
**Explanation**: VC dimension is the largest size of a set that can be shattered. Since 5 points can be shattered but 6 cannot, VC(H) = 5.

---

**Question 5**: Which of the following statements is FALSE about the version space?

A) Contains all hypotheses consistent with training data
B) Shrinks as more training examples are seen
C) Always contains the true target hypothesis
D) May become empty if target not in H

**Answer**: C
**Explanation**: The version space contains the true hypothesis ONLY if the target concept is representable in H. If the target is not in H, the version space may become empty or may not contain the true hypothesis.

---

**Question 6**: The No-Free-Lunch theorem implies that:

A) Learning is impossible
B) There is no universal best learning algorithm
C) All algorithms perform equally on all problems
D) VC dimension is irrelevant

**Answer**: B
**Explanation**: NFL theorem states that no single algorithm can be universally superior; performance depends on the problem structure and prior assumptions.

---

**Question 7**: For a finite hypothesis space with |H| = 2^10 = 1024, calculate the sample complexity to achieve ε = 0.05 with δ = 0.01.

A) 150
B) 230
C) 380
D) 460

**Answer**: C
**Explanation**: m ≥ (1/0.05)(ln(1024) + ln(100)) = 20(6.928 + 4.605) = 20(11.533) ≈ 380

---

**Question 8**: A concept class is PAC-learnable if:

A) It has finite VC dimension
B) Sample complexity is polynomial in 1/ε and 1/δ
C) Both A and B
D) None of the above

**Answer**: C
**Explanation**: A concept class is PAC-learnable if there exists an algorithm with polynomial sample complexity. For finite hypothesis spaces, finite VC dimension implies PAC-learnability.

---

**Question 9**: What is the VC dimension of axis-aligned rectangles in ℝ²?

A) 2
B) 3
C) 4
D) 5

**Answer**: C
**Explanation**: For axis-aligned rectangles in ℝ^d, VC dimension = 2d. In ℝ², this equals 4.

---

**Question 10**: In the context of agnostic PAC learning:

A) The target concept must be in H
B) We learn even when no perfect hypothesis exists
C) We require infinite training data
D) The hypothesis space must be infinite

**Answer**: B
**Explanation**: Agnostic PAC learning does not assume the target concept is in H. It guarantees learning up to the best hypothesis in H, plus a small error term.
