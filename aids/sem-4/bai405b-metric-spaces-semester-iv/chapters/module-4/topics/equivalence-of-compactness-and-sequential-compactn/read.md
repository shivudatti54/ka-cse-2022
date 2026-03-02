# Compactness vs. Sequential Compactness in Metric Spaces

**Module 4: Compactness | Topic: Equivalence of Compactness and Sequential Compactness**

## Introduction

In the study of metric spaces, two fundamental and seemingly different notions of "finiteness" or "boundedness" emerge: **compactness** (defined via open covers) and **sequential compactness** (defined via convergent subsequences). For general topological spaces, these concepts are distinct. However, one of the most elegant and powerful results in metric space theory is that these two notions are **equivalent**. This means in a metric space $(X, d)$, a subset $K$ is compact if and only if it is sequentially compact. This equivalence provides us with two powerful tools to analyze and prove properties of compact sets in metric spaces.

## Core Concepts

### 1. Compactness (Covering Property)

A subset $K$ of a metric space $(X, d)$ is **compact** if **every open cover** of $K$ has a **finite subcover**.

*   **Open Cover:** A collection $\{U_\alpha\}$ of open sets such that $K \subset \bigcup_\alpha U_\alpha$.
*   **Finite Subcover:** A finite number of these open sets, say $U_1, U_2, ..., U_n$, such that $K \subset U_1 \cup U_2 \cup ... \cup U_n$.

This is often the standard definition of compactness.

### 2. Sequential Compactness (Sequence Property)

A subset $K$ of a metric space $(X, d)$ is **sequentially compact** if **every sequence** in $K$ has a **convergent subsequence** whose limit is also **in $K$**.

This means no matter how you choose points $(x_n)$ from $K$, you can always find a subsequence $(x_{n_k})$ that converges to some point $x \in K$.

### 3. The Equivalence Theorem

**Theorem:** Let $(X, d)$ be a metric space and $K \subset X$. Then $K$ is compact if and only if $K$ is sequentially compact.

**Proof Outline:**

The proof relies on two key properties of metric spaces: the existence of a countable base (via denseness or directly) and the fact that open sets are defined using distances.

*   **Compact $\implies$ Sequentially Compact:**
    1.  Take any sequence $(x_n)$ in $K$.
    2.  If $(x_n)$ has no convergent subsequence, then every point $x \in K$ has an open neighborhood $U_x$ containing only *finitely many* terms of $(x_n)$.
    3.  The collection $\{U_x : x \in K\}$ is an open cover of $K$.
    4.  By compactness, a finite subcover $\{U_{x_1}, ..., U_{x_m}\}$ exists.
    5.  But this finite union contains only finitely many terms of $(x_n)$, which is a contradiction since the sequence has infinitely many terms. Therefore, a convergent subsequence must exist.

*   **Sequentially Compact $\implies$ Compact:**
    1.  Show that sequential compactness implies **totally bounded** (for any $\epsilon > 0$, $K$ can be covered by finitely many $\epsilon$-balls) and **complete** (every Cauchy sequence converges to a point in $K$).
    2.  Use total boundedness to construct a countable dense subset.
    3.  Take any open cover $\{U_\alpha\}$ of $K$. Using the dense subset, one can show the existence of a countable subcover (Lindelöf property in metric spaces).
    4.  Now, if this countable cover had no finite subcover, one could construct a sequence with no convergent subsequence, contradicting sequential compactness. Therefore, a finite subcover must exist.

## Example: The Closed Unit Interval

Consider $K = [0, 1]$ in the metric space $\mathbb{R}$ with the standard Euclidean metric.

*   **Compactness:** The Heine-Borel theorem tells us $[0,1]$ is compact. Any open cover, like the collection of all open intervals $(1/n, 1 + 1/n)$ for $n \in \mathbb{N}$, has a finite subcover (e.g., taking $n=1$ and $n=2$ suffices: $(-1, 2)$ and $(0.5, 1.5)$ cover $[0,1]$).
*   **Sequential Compactness:** Take any sequence $(x_n)$ in $[0,1]$. The **Bolzano-Weierstrass theorem** guarantees that this bounded sequence has a convergent subsequence. Since $[0,1]$ is closed, the limit of this subsequence must also lie in $[0,1]$.

This example perfectly illustrates the equivalence of the two properties for a fundamental set.

## Key Points & Summary

*   **Equivalence is Metric-Specific:** This result holds **specifically in metric spaces**. In more general topological spaces, compactness and sequential compactness are **not** equivalent.
*   **Two Powerful Tools:** The equivalence gives two different perspectives and techniques for working with compact sets.
    *   Use the **open cover definition** to prove a set is compact (e.g., showing a closed subset of a compact set is compact).
    *   Use the **sequential definition** to extract limits and prove convergence (e.g., showing a continuous function on a compact set is uniformly continuous).
*   **Underlying Logic:** The link between the two concepts is fundamentally tied to the **countability** axioms that metric spaces satisfy, which allow us to bridge the "finite" world of covers and the "infinite" world of sequences.

**In summary, for  engineering students, remember this powerful takeaway: In any metric space $(X, d)$, the following are equivalent for a subset $K$:**
1.  $K$ is compact.
2.  $K$ is sequentially compact.
3.  $K$ is complete and totally bounded.

This equivalence is a cornerstone result, simplifying many proofs and solidifying our understanding of these crucial concepts in real and functional analysis.