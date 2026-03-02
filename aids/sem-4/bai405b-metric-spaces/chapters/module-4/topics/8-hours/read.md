# Metric Spaces: Compactness

=====================================

## Introduction

---

In topology, a metric space is a set X equipped with a metric or distance function d that assigns a non-negative real number to each pair of points in X. The concept of compactness is a fundamental property of metric spaces that plays a crucial role in many areas of mathematics and physics.

## Definition of Compactness

---

A metric space X is said to be compact if every open cover of X has a finite subcover. In other words, given any collection of open sets that cover X, there exists a finite subset of these sets that also covers X.

## Definition of Open Cover

---

An open cover of a set X is a collection of open sets such that X is contained in the union of these sets.

## Definition of Finite Subcover

---

A finite subcover of an open cover is a finite subset of the open cover that still covers the original set X.

## Properties of Compactness

---

- If X is compact, then every sequence in X has a convergent subsequence.
- If X is compact, then every sequence in X has a convergent subsequence that converges to a point in X.

## Examples of Compact Metric Spaces

---

- The closed unit ball in R^n is compact for all n.
- The closed unit disk in R^n is compact for all n.
- The Cantor set is compact.

## Examples of Non-Compact Metric Spaces

---

- R with the standard metric is not compact.
- The real line with the standard metric is not compact.

## Proofs of Compactness

---

### Proof 1: Finite Subcover

Let X be a compact metric space and {U*i} be an open cover of X. Then, for each x in X, there exists a U_i such that x is in U_i. Since X is compact, there exists a finite number of i's, say {i_1, i_2, ..., i_n}, such that X is contained in the union of {U*{i*1}, U*{i*2}, ..., U*{i_n}}.

### Proof 2: Closed Balls

Let X be a compact metric space and {U_i} be an open cover of X. For each x in X, there exists a U_i such that x is in U_i. Let r_x be the radius of the open ball B(x, r) such that x is in B(x, r) and B(x, r) is contained in U_i. Let r = max{r_x}. Then, B(x, r) is an open ball such that x is in B(x, r) and B(x, r) is contained in U_i.

### Proof 3: Closed Balls (continued)

Since X is compact, there exists a finite number of i's, say {i_1, i_2, ..., i_n}, such that X is contained in the union of {B(x_i, r_x_i)}. Let r = max{r_x_i}. Then, B(x_i, r) is an open ball such that x_i is in B(x_i, r) and B(x_i, r) is contained in U_i.

### Proof 4: Finite Subcover (continued)

Since X is compact, there exists a finite number of i's, say {i_1, i_2, ..., i_n}, such that X is contained in the union of {B(x_i, r_x_i)}. Let r = max{r_x_i}. Then, {B(x_i, r)} is a finite subcover of {U_i}.

## Key Concepts

---

- Open cover: A collection of open sets that cover a set.
- Finite subcover: A finite subset of an open cover that still covers the original set.
- Compactness: The property that every open cover has a finite subcover.
- Closed balls: Open balls that are contained in a fixed open set.

## Exercises

---

1.  Prove that the closed unit ball in R^n is compact for all n.
2.  Prove that the Cantor set is compact.
3.  Prove that the real line with the standard metric is not compact.

## Solutions

---

1.  Let X be the closed unit ball in R^n. Let {U*i} be an open cover of X. Then, for each x in X, there exists a U_i such that x is in U_i. Since X is contained in the closed unit ball, there exists a radius r such that X is contained in the closed ball B(0, r). Let {i_1, i_2, ..., i_n} be the collection of indices of the U_i's that are contained in B(0, r). Then, X is contained in the union of {U*{i*1}, U*{i*2}, ..., U*{i_n}}, which is a finite subcover of {U_i}.
2.  Let X be the Cantor set. Let {U_i} be an open cover of X. Then, for each x in X, there exists a U_i such that x is in U_i. Let n be the largest integer such that 2^n is less than or equal to the length of X. Then, X is contained in the union of {U_1, U_2, ..., U_n}, which is a finite subcover of {U_i}.
3.  Let X be the real line with the standard metric. Let {U_i} be an open cover of X. Then, for each x in X, there exists a U_i such that x is in U_i. Let n be the largest integer such that 2^n is less than or equal to the length of X. Then, X is not contained in the union of {U_1, U_2, ..., U_n}, which means that the collection {U_1, U_2, ..., U_n} is not a finite subcover of {U_i}.
