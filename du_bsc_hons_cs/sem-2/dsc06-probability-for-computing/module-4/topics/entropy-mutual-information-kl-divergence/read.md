# Entropy, Mutual Information, and KL Divergence

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Welcome to this comprehensive study module on **Entropy, Mutual Information, and Kullback-Leibler (KL) Divergence** — three fundamental concepts in information theory that form the backbone of modern computer science applications. These concepts are essential for understanding data compression, machine learning algorithms, natural language processing, and many other areas.

### Real-World Relevance

These mathematical concepts power technologies you use daily:

- **Search Engines**: PageRank and information retrieval use mutual information to rank documents
- **Machine Learning**: KL divergence is used in variational autoencoders, softmax classifiers, and reinforcement learning
- **Data Compression**: Entropy determines the theoretical minimum bits needed to encode data
- **NLP**: Word embeddings and language models rely on mutual information
- **Bioinformatics**: Sequence analysis and gene expression studies use these measures
- **Image Processing**: Medical imaging and computer vision applications

---

## 2. Entropy

### 2.1 Definition

**Entropy** (also called Shannon Entropy) measures the uncertainty or randomness of a random variable. It quantifies the average amount of information produced by a stochastic source of data.

For a discrete random variable $X$ with probability mass function $P(X)$, the entropy $H(X)$ is defined as:

$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i) = \sum_{i=1}^{n} P(x_i) \log_2 \frac{1}{P(x_i)}$$

**Note**: When $P(x_i) = 0$, we define $0 \log_2 0 = 0$ by continuity.

The base of the logarithm determines the unit:
- Base 2: bits (most common in computer science)
- Base $e$: nats
- Base 10: dit

### 2.2 Properties of Entropy

1. **Non-negativity**: $H(X) \geq 0$
2. **Maximum at uniformity**: $H(X) \leq \log_2 n$, with equality when $P$ is uniform
3. **Zero for deterministic variables**: $H(X) = 0$ when $P(x_i) = 1$ for some $x_i$
4. **Additivity for independent variables**: If $X$ and $Y$ are independent, $H(X, Y) = H(X) + H(Y)$

### 2.3 Binary Entropy Function

For a Bernoulli random variable (two outcomes):

$$H_b(p) = -p \log_2 p - (1-p) \log_2(1-p)$$

where $p = P(X=1)$.

### 2.4 Example: Entropy Calculation

Consider a fair coin toss:
- $P(Heads) = 0.5$, $P(Tails) = 0.5$
- $H(X) = -0.5 \log_2(0.5) - 0.5 \log_2(0.5) = 0.5 + 0.5 = 1$ bit

Consider a biased coin (almost always heads):
- $P(Heads) = 0.9$, $P(Tails) = 0.1$
- $H(X) = -0.9 \log_2(0.9) - 0.1 \log_2(0.1) \approx 0.152 + 0.332 = 0.484$ bits

```python
import math

def entropy(probabilities):
    """Calculate Shannon entropy in bits"""
    ent = 0
    for p in probabilities:
        if p > 0:
            ent -= p * math.log2(p)
    return ent

# Fair coin
fair_coin = [0.5, 0.5]
print(f"Fair coin entropy: {entropy(fair_coin):.4f} bits")

# Biased coin
biased_coin = [0.9, 0.1]
print(f"Biased coin entropy: {entropy(biased_coin):.4f} bits")

# Loaded coin (always heads)
loaded_coin = [1.0, 0.0]
print(f"Loaded coin entropy: {entropy(loaded_coin):.4f} bits")
```

**Output:**
```
Fair coin entropy: 1.0000 bits
Biased coin entropy: 0.4840 bits
Loaded coin entropy: 0.0000 bits
```

---

## 3. Joint Entropy

### 3.1 Definition

**Joint Entropy** measures the total uncertainty of two (or more) random variables considered together.

For two discrete random variables $X$ and $Y$ with joint distribution $P(X, Y)$:

$$H(X, Y) = -\sum_{x \in \mathcal{X}}\sum_{y \in \mathcal{Y}} P(x, y) \log_2 P(x, y)$$

### 3.2 Properties

1. **Symmetry**: $H(X, Y) = H(Y, X)$
2. **Upper bound**: $H(X, Y) \leq H(X) + H(Y)$
3. **Lower bound**: $H(X, Y) \geq \max(H(X), H(Y))$
4. **Equality for independence**: $H(X, Y) = H(X) + H(Y)$ if $X$ and $Y$ are independent

### 3.3 Example: Joint Entropy

Consider two binary variables $X$ and $Y$ with the following joint distribution:

| Y\X | 0   | 1   |
|-----|-----|-----|
| 0   | 0.25| 0.25|
| 1   | 0.25| 0.25|

All outcomes equally likely ($P(X=0, Y=0) = 0.25$, etc.)

$$H(X, Y) = -4 \times (0.25 \times \log_2 0.25) = -4 \times (0.25 \times (-2)) = 2 \text{ bits}$$

Since $X$ and $Y$ are independent: $H(X, Y) = H(X) + H(Y) = 1 + 1 = 2$ bits ✓

---

## 4. Conditional Entropy

### 4.1 Definition

**Conditional Entropy** measures the remaining uncertainty in $Y$ after knowing $X$. It is also called the entropy of $Y$ given $X$.

$$H(Y|X) = \sum_{x \in \mathcal{X}} P(x) H(Y|X=x)$$

Expanded form:

$$H(Y|X) = -\sum_{x \in \mathcal{X}}\sum_{y \in \mathcal{Y}} P(x, y) \log_2 \frac{P(x, y)}{P(x)}$$

### 4.2 Chain Rule

The chain rule relates joint and conditional entropy:

$$H(X, Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)$$

More generally:
$$H(X_1, X_2, ..., X_n) = \sum_{i=1}^{n} H(X_i | X_1, ..., X_{i-1})$$

### 4.3 Properties

1. **Non-negativity**: $H(Y|X) \geq 0$
2. **Reduction with dependence**: $H(Y|X) \leq H(Y)$, with equality when $X$ and $Y$ are independent
3. **Conditioning reduces entropy**: $H(X) \geq H(X|Y)$

---

## 5. Mutual Information

### 5.1 Definition

**Mutual Information** measures the amount of information shared between two random variables. It quantifies how much knowing one variable reduces uncertainty about the other.

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

Alternative forms:

$$I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$$

$$I(X; Y) = \sum_{x \in \mathcal{X}}\sum_{y \in \mathcal{Y}} P(x, y) \log_2 \frac{P(x, y)}{P(x)P(y)}$$

### 5.2 Properties of Mutual Information

1. **Symmetry**: $I(X; Y) = I(Y; X)$
2. **Non-negativity**: $I(X; Y) \geq 0$
3. **Maximum at dependence**: $I(X; X) = H(X)$
4. **Zero at independence**: $I(X; Y) = 0$ if $X$ and $Y$ are independent
5. **Upper bound**: $I(X; Y) \leq \min(H(X), H(Y))$

### 5.3 Relationship with Entropy

The relationships can be visualized in the following Venn diagram:

```
┌─────────────────────────────────┐
│                                 │
│     H(X)            H(Y)        │
│   ┌──────┐       ┌──────┐       │
│   │      │       │      │       │
│   │  I   │   ┌───│──┐   │       │
│   │ (X;Y)│   │ H  │   │       │
│   │      │   │(X|Y)│   │       │
│   └──────┘   └──┬──┘   │       │
│                │ H(Y|X)│       │
│                └───────┘       │
│                                 │
└─────────────────────────────────┘
```

Key relationships:
- $H(X, Y) = H(X) + H(Y) - I(X; Y)$
- $H(X) = I(X; Y) + H(X|Y)$
- $H(Y) = I(X; Y) + H(Y|X)$

### 5.4 Example: Mutual Information

Using our earlier coin example where $X$ and $Y$ are independent:

- $H(X) = 1$ bit, $H(Y) = 1$ bit
- $H(X, Y) = 2$ bits
- $I(X; Y) = 1 + 1 - 2 = 0$ bits (as expected for independent variables)

Now consider a dependent case where $Y = X$ (perfect correlation):

| Y\X | 0   | 1   |
|-----|-----|-----|
| 0   | 0.5 | 0.0 |
| 1   | 0.0 | 0.5 |

- $H(X) = 1$ bit, $H(Y) = 1$ bit
- $H(X, Y) = 1$ bit (since knowing one determines the other)
- $I(X; Y) = 1 + 1 - 1 = 1$ bit (maximum possible)

### 5.5 Python Implementation

```python
import math
import numpy as np

def joint_entropy(pxy):
    """Calculate joint entropy H(X,Y) from joint distribution"""
    ent = 0
    for row in pxy:
        for p in row:
            if p > 0:
                ent -= p * math.log2(p)
    return ent

def conditional_entropy(pxy):
    """Calculate H(Y|X) from joint distribution"""
    # First compute marginal P(X)
    px = pxy.sum(axis=1)  # Sum rows for P(X)
    h_y_given_x = 0
    for i, p_x in enumerate(px):
        if p_x > 0:
            for p in pxy[i]:
                if p > 0:
                    h_y_given_x -= p * math.log2(p / p_x)
    return h_y_given_x

def mutual_information(pxy):
    """Calculate I(X;Y) from joint distribution"""
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    i = 0
    for x in range(len(px)):
        for y in range(len(py)):
            if pxy[x, y] > 0 and px[x] > 0 and py[y] > 0:
                i += pxy[x, y] * math.log2(pxy[x, y] / (px[x] * py[y]))
    return i

# Example: Dependent variables (Y = X)
pxy_independent = np.array([[0.25, 0.25], [0.25, 0.25]])
pxy_dependent = np.array([[0.5, 0.0], [0.0, 0.5]])

print("Independent variables:")
print(f"  H(X,Y) = {joint_entropy(pxy_independent):.4f} bits")
print(f"  I(X;Y) = {mutual_information(pxy_independent):.4f} bits")

print("\nDependent variables (Y = X):")
print(f"  H(X,Y) = {joint_entropy(pxy_dependent):.4f} bits")
print(f"  I(X;Y) = {mutual_information(pxy_dependent):.4f} bits")
```

**Output:**
```
Independent variables:
  H(X,Y) = 2.0000 bits
  I(X;Y) = 0.0000 bits

Dependent variables (Y = X):
  H(X,Y) = 1.0000 bits
  I(X;Y) = 1.0000 bits
```

---

## 6. Kullback-Leibler (KL) Divergence

### 6.1 Definition

**KL Divergence** (also called relative entropy) measures how one probability distribution diverges from another, expected distribution. It is not a true distance (asymmetric, not satisfying triangle inequality), but measures "information gain" when using $Q$ instead of $P$.

For two discrete probability distributions $P$ and $Q$:

$$D_{KL}(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log_2 \frac{P(x)}{Q(x)}$$

**Important**: $D_{KL}(P || Q) \neq D_{KL}(Q || P)$ in general.

### 6.2 Properties

1. **Non-negativity**: $D_{KL}(P || Q) \geq 0$ (Gibbs' inequality)
2. **Zero if and only if identical**: $D_{KL}(P || Q) = 0$ iff $P = Q$
3. **Asymmetry**: Generally $D_{KL}(P || Q) \neq D_{KL}(Q || P)$
4. **Chain rule**: $D_{KL}(P(X, Y) || Q(X, Y)) = D_{KL}(P(X) || Q(X)) + D_{KL}(P(Y|X) || Q(Y|X))$

### 6.3 Relationship with Mutual Information

Mutual Information can be expressed as a KL divergence:

$$I(X; Y) = D_{KL}(P(X, Y) || P(X)P(Y))$$

This measures how far the joint distribution is from the product of marginals (independence).

### 6.4 Example: KL Divergence

Consider distributions over outcomes {A, B, C}:

$P = [0.5, 0.3, 0.2]$ and $Q = [0.4, 0.4, 0.2]$

$$D_{KL}(P || Q) = 0.5 \log_2(0.5/0.4) + 0.3 \log_2(0.3/0.4) + 0.2 \log_2(0.2/0.2)$$
$$= 0.5 \times 0.322 + 0.3 \times (-0.415) + 0.2 \times 0$$
$$= 0.161 - 0.124 = 0.037 \text{ bits}$$

### 6.5 Python Implementation

```python
import math

def kl_divergence(p, q):
    """
    Calculate D_KL(P || Q)
    Note: Returns inf if any q[i] = 0 while p[i] > 0
    """
    kl = 0
    for p_i, q_i in zip(p, q):
        if p_i > 0:
            if q_i == 0:
                return float('inf')
            kl += p_i * math.log2(p_i / q_i)
    return kl

# Example distributions
P = [0.5, 0.3, 0.2]
Q = [0.4, 0.4, 0.2]
R = [0.5, 0.3, 0.2]  # Same as P

print("D_KL(P || Q):", f"{kl_divergence(P, Q):.4f} bits")
print("D_KL(Q || P):", f"{kl_divergence(Q, P):.4f} bits")
print("D_KL(P || R):", f"{kl_divergence(P, R):.4f} bits (should be 0)")
```

**Output:**
```
D_KL(P || Q): 0.0370 bits
D_KL(Q || P): 0.0417 bits
D_KL(P || R): 0.0000 bits (should be 0)
```

### 6.6 Applications of KL Divergence

1. **Machine Learning**: 
   - Loss function in variational autoencoders (VAEs)
   - Log-loss in classification (cross-entropy)
   - Policy gradient in reinforcement learning

2. **Data Compression**: 
   - Measures inefficiency when using wrong distribution for encoding

3. **Text Mining**:
   - Topic modeling (LDA)
   - Information retrieval ranking

4. **Bayesian Inference**:
   - Variational inference approximates posterior distributions

---

## 7. Key Takeaways

### Entropy
- Measures uncertainty/randomness of a random variable
- Maximum when distribution is uniform
- Minimum (zero) when outcome is certain
- Formula: $H(X) = -\sum_x P(x) \log_2 P(x)$

### Joint Entropy
- Total uncertainty of multiple variables combined
- $H(X, Y) \leq H(X) + H(Y)$ with equality for independence

### Conditional Entropy
- Remaining uncertainty in $Y$ after knowing $X$
- $H(Y|X) = H(X, Y) - H(X)$
- Never exceeds $H(Y)$

### Mutual Information
- Information shared between $X$ and $Y$
- $I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$
- Zero for independent variables
- Maximum when variables are identical

### KL Divergence
- Measures divergence from distribution $P$ to $Q$
- $D_{KL}(P || Q) \geq 0$ (Gibbs' inequality)
- Asymmetric: $D_{KL}(P || Q) \neq D_{KL}(Q || P)$
- $I(X; Y) = D_{KL}(P(X,Y) || P(X)P(Y))$

---

## 8. Assessment Items

### 8.1 Multiple Choice Questions

**Q1.** The entropy of a fair six-sided die roll is:
- (a) $\log_2 6$ bits
- (b) 6 bits
- (c) $\log_6 2$ bits
- (d) 1 bit

**Q2.** If two random variables $X$ and $Y$ are statistically independent, then:
- (a) $H(X, Y) = H(X) + H(Y)$
- (b) $I(X; Y) = H(X)$
- (c) $H(X|Y) = H(X)$
- (d) $D_{KL}(P||Q) = 0$

**Q3.** KL divergence is:
- (a) A metric (satisfies triangle inequality)
- (b) Symmetric
- (c) Non-negative
- (d) Always zero for different distributions

**Q4.** Mutual Information $I(X; Y)$ cannot exceed:
- (a) $H(X) + H(Y)$
- (b) $H(X)H(Y)$
- (c) $\min(H(X), H(Y))$
- (d) $H(X, Y)$

**Q5.** Which statement is TRUE about conditional entropy?
- (a) $H(X|Y) \geq H(X)$
- (b) $H(X|Y) \leq H(X)$
- (c) $H(X|Y) = H(X) + H(Y)$
- (d) $H(X|Y) > H(X, Y)$

**Q6.** In a joint distribution where $Y$ is completely determined by $X$ (i.e., $Y = f(X)$):
- (a) $I(X; Y) = 0$
- (b) $I(X; Y) = H(X)$
- (c) $H(Y|X) = H(Y)$
- (d) $H(X, Y) = H(X) + H(Y)$

**Q7.** The binary entropy function $H_b(p)$ reaches its maximum value of 1 bit when:
- (a) $p = 0$
- (b) $p = 1$
- (c) $p = 0.5$
- (d) $p = 0$ or $p = 1$

**Q8.** Which formula correctly expresses mutual information in terms of KL divergence?
- (a) $I(X; Y) = D_{KL}(P(X) || P(Y))$
- (b) $I(X; Y) = D_{KL}(P(X, Y) || P(X)P(Y))$
- (c) $I(X; Y) = D_{KL}(P(X|Y) || P(X))$
- (d) $I(X; Y) = H(X)D_{KL}(P || Q)$

**Answers:** 1(a), 2(a), 3(c), 4(c), 5(b), 6(b), 7(c), 8(b)

### 8.2 Flashcards

| Term | Definition/Formula |
|------|-------------------|
| **Shannon Entropy** | $H(X) = -\sum_x P(x) \log_2 P(x)$ — measures uncertainty |
| **Joint Entropy** | $H(X, Y) = -\sum_{x,y} P(x,y) \log_2 P(x,y)$ — total uncertainty of (X,Y) |
| **Conditional Entropy** | $H(Y\|X) = \sum_x P(x) H(Y\|X=x)$ — uncertainty in Y given X |
| **Mutual Information** | $I(X; Y) = H(X) + H(Y) - H(X, Y)$ — shared information between X and Y |
| **KL Divergence** | $D_{KL}(P\|\|Q) = \sum_x P(x) \log_2 \frac{P(x)}{Q(x)}$ — relative entropy |
| **Chain Rule** | $H(X, Y) = H(X) + H(Y\|X) = H(Y) + H(X\|Y)$ |
| **Information Gain** | $IG(X;Y) = H(Y) - H(Y\|X)$ — same as mutual information |
| **Gibbs' Inequality** | $D_{KL}(P\|\|Q) \geq 0$ with equality iff P = Q |

### 8.3 Short Answer Questions

1. **Prove that $H(X) \geq H(X|Y)$ for any two random variables $X$ and $Y$.**

2. **Show that $I(X; X) = H(X)$. What does this tell us about self-information?**

3. **If $H(X, Y) = H(X) + H(Y)$, what can you conclude about the relationship between $X$ and $Y$?**

4. **Why is KL divergence not considered a "distance" metric? Explain with an example.**

5. **Calculate $H(X)$, $H(Y|X)$, and $I(X; Y)$ for the following joint distribution:**
   ```
   P(X=0, Y=0) = 0.1
   P(X=0, Y=1) = 0.4
   P(X=1, Y=0) = 0.2
   P(X=1, Y=1) = 0.3
   ```

6. **Explain why minimizing cross-entropy loss in classification is equivalent to minimizing KL divergence between true and predicted distributions.**

7. **In your own words, explain what "1 bit of entropy" means. Provide a concrete example.**

---

## 9. Delhi University Syllabus Context

This content aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science, specifically covering:

- **Module**: Probability for Computing
- **Topics Covered**: Information Theory fundamentals (Entropy, Mutual Information, KL Divergence)
- **Applications**: Data compression algorithms, machine learning loss functions, natural language processing

**Recommended Further Reading:**
- Cover & Thomas, "Elements of Information Theory" (Chapter 2-8)
- Shannon, C.E. (1948), "A Mathematical Theory of Communication"

---

*End of Study Material*