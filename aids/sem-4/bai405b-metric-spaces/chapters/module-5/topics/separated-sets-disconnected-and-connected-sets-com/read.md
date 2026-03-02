# **Separated Sets, Disconnected and Connected Sets, Components, Connected Subsets of R, and Continuous Functions on Connected Sets**

## **1. Introduction**

In the study of metric spaces, the concept of connectedness plays a crucial role. A set is said to be connected if it cannot be divided into two non-empty, disjoint subsets such that each subset is open relative to the closure of the other. In this topic, we will delve into the concepts of separated sets, disconnected and connected sets, components, connected subsets of R, and continuous functions on connected sets.

## **2. Separated Sets**

A set X in a metric space is said to be **separated** if it can be written as the union of two disjoint non-empty open sets A and B. In other words:

- X = A ∪ B
- A ∩ B = ∅
- A, B are non-empty open sets

**Example:**

Consider the set X = (-1, 1) in the real line R with the standard metric. Let A = (-1, 0) and B = (0, 1). Then X = A ∪ B, and both A and B are non-empty open sets. Hence, X is separated.

## **3. Disconnected Sets**

A set X in a metric space is said to be **disconnected** if it can be written as the union of two non-empty disjoint open sets A and B. In other words:

- X = A ∪ B
- A ∩ B = ∅
- A and B are non-empty open sets

**Example:**

Consider the set X = (-1, 1) in the real line R with the standard metric. Let A = (-1, 0) and B = (0, 1). Then X = A ∪ B, and both A and B are non-empty open sets. However, this is not an example of a disconnected set, as the sets A and B are not disjoint. A disconnected set would be X = (-1, 0) ∪ (0, 1).

## **4. Connected Sets**

A set X in a metric space is said to be **connected** if it cannot be written as the union of two non-empty, disjoint open sets. In other words:

- X = A ∪ B
- A ∩ B = ∅
- A and B are non-empty open sets

**Example:**

Consider the set X = [0, 1] in the real line R with the standard metric. Let A = (-1, 0) and B = (0, 1). However, since the sets A and B are not disjoint, we cannot form a connected set using these sets. Instead, consider the set X = [0, 1] itself. Then X is connected, as it cannot be written as the union of two non-empty, disjoint open sets.

## **5. Components**

A **component** of a set X in a metric space is a maximal connected subset of X. In other words, a component is a connected subset of X that is not contained in any larger connected subset of X.

**Example:**

Consider the set X = (-1, 1) in the real line R with the standard metric. The set (-1, 0) is a component of X, as it is a connected subset of X that is not contained in any larger connected subset of X.

## **6. Connected Subsets of R**

A subset X of the real line R is said to be **connected** if it cannot be written as the union of two non-empty, disjoint open sets. In other words:

- X = A ∪ B
- A ∩ B = ∅
- A and B are non-empty open sets

**Example:**

Consider the interval [0, 1] in the real line R with the standard metric. Then [0, 1] is connected, as it cannot be written as the union of two non-empty, disjoint open sets.

## **7. Continuous Functions on Connected Sets**

A function f: X → Y between two metric spaces X and Y is said to be **continuous** at a point x in X if for every open set V in Y containing f(x), there exists an open set U in X containing x such that f(U) ⊆ V.

**Example:**

Consider the function f: [0, 1] → [0, 1] defined by f(x) = x^2. Then f is continuous on [0, 1], as it is a polynomial function and hence continuous on a closed interval.

- Key concepts:
  - Separated sets: A set X can be written as the union of two disjoint non-empty open sets A and B.
  - Disconnected sets: A set X can be written as the union of two non-empty, disjoint open sets A and B.
  - Connected sets: A set X cannot be written as the union of two non-empty, disjoint open sets.
  - Components: A maximal connected subset of a set X.
  - Connected subsets of R: A subset X of the real line R is connected if it cannot be written as the union of two non-empty, disjoint open sets.
  - Continuous functions on connected sets: A function f: X → Y between two metric spaces X and Y is continuous at a point x in X if for every open set V in Y containing f(x), there exists an open set U in X containing x such that f(U) ⊆ V.
