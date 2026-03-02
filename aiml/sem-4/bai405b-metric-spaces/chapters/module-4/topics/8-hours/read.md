# **Metric Spaces: Compactness**

### Introduction

---

In metric geometry, a metric space is a set X together with a metric or distance function d that satisfies certain properties. In this topic, we will focus on compactness, a fundamental concept in metric spaces that plays a crucial role in many areas of mathematics.

### Definition of Compactness

---

A metric space X is said to be compact if every open cover of X has a finite subcover. In other words, if we have a collection of open sets that cover X, we can always find a finite subset of these open sets that still covers X.

### Definition of an Open Cover

---

An open cover of a set X is a collection of open sets that cover X. That is, every point in X is contained in at least one of the open sets.

### Definition of a Finite Subcover

---

A finite subcover of an open cover is a finite subset of the open sets that still covers X.

### Examples of Compact Metric Spaces

---

- The closed unit interval [0, 1] in the standard metric space with the usual distance function d(x, y) = |x - y| is a compact metric space.
- The closed disk D = {x ∈ ℝ² | x ∈ [0, 1]²} in the Euclidean metric space ℝ² with the distance function d(x, y) = √((x₁ - y₁)² + (x₂ - y₂)²) is a compact metric space.

### Examples of Non-Compact Metric Spaces

---

- The open interval (0, 1) in the standard metric space with the usual distance function d(x, y) = |x - y| is not a compact metric space.
- The set of all rational numbers Q in the Euclidean metric space ℝ with the distance function d(x, y) = |x - y| is not a compact metric space.

### Key Concepts

---

- **Compactness**: A metric space X is compact if every open cover of X has a finite subcover.
- **Open Cover**: A collection of open sets that cover a set X.
- **Finite Subcover**: A finite subset of open sets that still covers X.

### Theorem: Heine-Borel Theorem

---

The Heine-Borel theorem states that a metric space X is compact if and only if every sequence in X has a convergent subsequence.

### Proof of the Heine-Borel Theorem

---

Let X be a compact metric space and {xₙ} be a sequence in X. Then, the set {xₙ} is an open cover of X. By compactness, there exists a finite subcover {x₁, x₂, ..., xₙ} that still covers X. Since each xi is an open set, there exists an ε > 0 such that B(xi, ε) ⊂ X for each i. Let ε = 1/n. Then, B(xₙ, 1/n) ⊂ X for each n. Since X is compact, there exists a point x₀ in X such that xₙ ∈ B(x₀, 1/n) for all n. This implies that d(xₙ, x₀) < 1/n for all n, which implies that the sequence {xₙ} converges to x₀.

Conversely, suppose that every sequence in X has a convergent subsequence. Let X be a set and let {U₁, U₂, ...} be an open cover of X. For each xi in X, there exists a point ui in U₁ such that xi ∈ ui. Then, the set {ui} is an open cover of X. By assumption, there exists a point x₀ in X such that ui ∈ B(x₀, 1/n) for all i. This implies that xi ∈ B(x₀, 1/n) for all i, which implies that the sequence {xi} converges to x₀. Therefore, X is compact.

### Conclusion

---

In this topic, we have studied compactness in metric spaces, a fundamental concept that plays a crucial role in many areas of mathematics. We have defined compactness, open covers, and finite subcovers, and we have provided examples of compact and non-compact metric spaces. We have also proven the Heine-Borel theorem, which states that a metric space is compact if and only if every sequence in the space has a convergent subsequence.
