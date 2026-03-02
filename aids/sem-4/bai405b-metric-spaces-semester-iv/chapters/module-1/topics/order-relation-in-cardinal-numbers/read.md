**Subject:** Metric Spaces  
**Semester:** IV  
**Module:** Module 1: Theory of Sets  
**Topic:** Order Relation in Cardinal Numbers  

***

### 1. Introduction

In the study of metric spaces and advanced mathematics, understanding the "size" or cardinality of sets is fundamental. Cardinal numbers provide a way to describe this size, even for infinite sets. Once we can assign a cardinal number to a set, a natural question arises: can we compare these sizes? The order relation on cardinal numbers formalizes this comparison, allowing us to state whether one set is "smaller," "larger," or the same size as another, even when both are infinite. This concept is crucial for deeper topics in analysis, topology, and set theory.

### 2. Core Concepts

#### a) Recap: Cardinality and Cardinal Numbers

The **cardinality** of a set $A$, denoted by $|A|$, is a measure of the number of its elements. Two sets have the **same cardinality** ($|A| = |B|$) if there exists a bijective function (a one-to-one and onto mapping) from $A$ to $B$.

A **cardinal number** is an equivalence class assigned to a set to denote its size. For finite sets, these are the natural numbers (0, 1, 2, 3,...). For infinite sets, we have transfinite cardinals like $\aleph_0$ (the cardinality of countable sets, e.g., $\mathbb{N}$) and $\mathfrak{c}$ (the cardinality of the continuum, e.g., $\mathbb{R}$).

#### b) Defining the Order Relation $\leq$

The order relation between cardinal numbers is defined using the concept of injective functions.

**Definition:** Let $\mathfrak{a}$ and $\mathfrak{b}$ be two cardinal numbers. We say that $\mathfrak{a}$ is **less than or equal to** $\mathfrak{b}$ (denoted $\mathfrak{a} \leq \mathfrak{b}$) if there exist sets $A$ and $B$ such that $|A| = \mathfrak{a}$, $|B| = \mathfrak{b}$, and there exists an **injective function** $f: A \to B$.

This means the elements of $A$ can be "paired" with distinct elements of $B$, suggesting that $B$ has at least as many elements as $A$.

#### c) Strict Inequality $

We say $\mathfrak{a}$ is **strictly less than** $\mathfrak{b}$ (denoted $\mathfrak{a} < \mathfrak{b}$) if $\mathfrak{a} \leq \mathfrak{b}$ but $\mathfrak{a} \neq \mathfrak{b}$. In other words, there is an injection from a set of cardinality $\mathfrak{a}$ into a set of cardinality $\mathfrak{b}$, but no bijection exists between them.

#### d) The Schröder-Bernstein Theorem

This theorem is the essential tool for proving the equality of cardinal numbers from the order relation.

**Theorem:** If $\mathfrak{a} \leq \mathfrak{b}$ and $\mathfrak{b} \leq \mathfrak{a}$, then $\mathfrak{a} = \mathfrak{b}$.

In practical terms, if you can find an injection from $A$ to $B$ *and* an injection from $B$ to $A$, then there must exist a bijection between them, meaning $|A| = |B|$.

#### e) Trichotomy and the Axiom of Choice

A fundamental question is whether cardinal numbers are always comparable. The statement that for any two cardinals $\mathfrak{a}$ and $\mathfrak{b}$, exactly one of the following must hold:
$\mathfrak{a} < \mathfrak{b}$, $\mathfrak{a} = \mathfrak{b}$, or $\mathfrak{a} > \mathfrak{b}$
is known as the **Law of Trichotomy**. It is equivalent to the **Axiom of Choice**, a key postulate in set theory accepted by most mathematicians.

### 3. Examples

1.  **Finite Sets:** Let $\mathfrak{a} = 3$ and $\mathfrak{b} = 5$. An injection exists from a 3-element set into a 5-element set, so $3 \leq 5$. Since $3 \neq 5$, we have $3 < 5$.

2.  **Countable vs. Uncountable:** Let $\mathfrak{a} = \aleph_0$ (size of $\mathbb{N}$) and $\mathfrak{b} = \mathfrak{c}$ (size of $\mathbb{R}$).
    *   The identity map $f: \mathbb{N} \to \mathbb{R}, f(n) = n$ is injective. Therefore, $\aleph_0 \leq \mathfrak{c}$.
    *   However, by Cantor's diagonalization argument, there is no bijection between $\mathbb{N}$ and $\mathbb{R}$, so $\aleph_0 \neq \mathfrak{c}$.
    *   Hence, we conclude $\aleph_0 < \mathfrak{c}$.

3.  **Using Schröder-Bernstein:** Prove that $|(0,1)| = |(0,1]|$.
    *   **Injection 1:** $f: (0,1) \to (0,1]$ defined by $f(x) = x$ is injective. So, $|(0,1)| \leq |(0,1]|$.
    *   **Injection 2:** $g: (0,1] \to (0,1)$ defined by $g(x) = x/2$ is injective (it maps every element to a number in $(0, 0.5]$). So, $|(0,1]| \leq |(0,1)|$.
    *   By the Schröder-Bernstein Theorem, $|(0,1)| = |(0,1]|$.

### 4. Key Points & Summary

*   **Purpose:** The order relation ($\leq, <$) allows us to compare the sizes of sets based on their cardinal numbers.
*   **Definition:** $\mathfrak{a} \leq \mathfrak{b}$ if there exists an injective function from a set of size $\mathfrak{a}$ to a set of size $\mathfrak{b}$.
*   **Equality Proof:** The Schröder-Bernstein Theorem is critical: if $\mathfrak{a} \leq \mathfrak{b}$ and $\mathfrak{b} \leq \mathfrak{a}$, then $\mathfrak{a} = \mathfrak{b}$.
*   **Fundamental Result:** $\aleph_0 < \mathfrak{c}$. This shows that not all infinities are the same; some are "more infinite" than others.
*   **Foundation:** The comparability of all cardinals (Trichotomy) is a profound result equivalent to the Axiom of Choice.
*   **Relevance:** This theory underpins concepts of separability and dimension in metric spaces and functional analysis, making it indispensable for engineering mathematics.