**Subject:** Metric Spaces | **Semester:** IV | **Module:** 4. Compactness
**Topic:** Sequential Compactness

***

### Introduction to Sequential Compactness

In the study of metric spaces, compactness is a fundamental property that generalizes the notion of a closed and bounded set from Euclidean space to more abstract settings. One of the most intuitive and powerful ways to understand compactness is through sequences. **Sequential compactness** captures the idea that in a "compact" space, no matter how a sequence of points behaves, it cannot spread out indefinitely; some of its points must accumulate or cluster around a point within the space itself. This concept is crucial for proving many important results in analysis, such as the Extreme Value Theorem.

### Core Concepts

#### 1. Definition of Sequential Compactness

A subset `K` of a metric space `(X, d)` is said to be **sequentially compact** if every sequence in `K` has a **convergent subsequence** whose limit is also in `K`.

Let's break this down:
*   **Every sequence:** This is a universal condition. It must hold for all possible sequences you can form with points from the set `K`.
*   **Convergent subsequence:** You might not be able to make the entire sequence converge, but you can always find an infinite subset of its terms (a subsequence) that does converge.
*   **Limit is in K:** The point that the subsequence approaches must be a member of the set `K` itself. This ensures the set is "closed" in a very strong sense.

#### 2. The Intuition: The "Infinite Crowd" Analogy

Imagine an infinite number of people (points) confined to a compact set `K`. If you label them in a sequence `(x_n)`, the space is so "tight" or "finite" in a topological sense that the people must crowd together. No matter how you label them, you can always find an infinite group (a subsequence) all huddled around a specific location (the limit point) within the confines of `K`.

If the set were not compact (e.g., the open interval (0,1)), you could have a sequence, like `(1/n)`, that wants to converge to `0`. However, since `0` is not in (0,1), this sequence has no convergent subsequence *whose limit is inside the set*. The people are crowding around a point outside the fence.

#### 3. The Link to Compactness (Heine-Borel Property)

In the context of metric spaces, the different notions of compactness coincide. This is a key theorem:

**Theorem:** For a metric space `(X, d)`, the following are equivalent:
1.  `X` is **compact** (every open cover has a finite subcover).
2.  `X` is **sequentially compact**.
3.  `X` is **complete and totally bounded**.

This means that for your purposes in a metric space, proving sequential compactness is just as valid as proving compactness via open covers. The sequential definition is often more practical for working with problems involving limits and continuity.

### Examples

1.  **The Closed Interval [a, b] in ℝ:**
    The most classic example. The Bolzano-Weierstrass Theorem states that every bounded sequence in `ℝ` has a convergent subsequence. If the sequence is also contained in the *closed* interval `[a, b]`, the limit of this subsequence will also lie in `[a, b]`. Hence, `[a, b]` is sequentially compact.

2.  **A Finite Set:**
    Any finite set is sequentially compact. Any sequence `(x_n)` must, by necessity, have at least one point that repeats infinitely often. The constant subsequence formed by this point is trivially convergent. This aligns with the idea that finite sets are the simplest form of compact sets.

3.  **A Non-Example: The Open Interval (0,1) in ℝ:**
    Consider the sequence `x_n = 1/n`. Every term is in `(0,1)`. This sequence itself converges to `0`, and so does every one of its subsequences. However, the limit point `0` is **not** contained in `(0,1)`. Therefore, there exists a sequence in `(0,1)` with no convergent subsequence whose limit is in `(0,1)`. This proves `(0,1)` is not sequentially compact.

### Key Points and Summary

*   **Definition:** A set `K` is sequentially compact if **every** sequence in `K` has a **subsequence** that converges to a point **in `K`**.
*   **Equivalence in Metric Spaces:** In metric spaces, sequential compactness is equivalent to the Heine-Borel (open cover) definition of compactness. This is a very important result.
*   **Utility:** It provides a practical, sequence-based method for proving a set is compact, which is often easier than finding finite subcovers.
*   **Contrast with Completeness:** A complete space requires that every *Cauchy* sequence converges. A sequentially compact space requires that *every* sequence (not necessarily Cauchy) has a convergent subsequence. In fact, sequential compactness implies completeness.
*   **Main Takeaway:** Sequential compactness is the natural generalization of the Bolzano-Weierstrass property to abstract metric spaces. It is a powerful tool for ensuring the existence of limits and is fundamental in proofs concerning continuous functions on compact sets (e.g., uniform continuity).