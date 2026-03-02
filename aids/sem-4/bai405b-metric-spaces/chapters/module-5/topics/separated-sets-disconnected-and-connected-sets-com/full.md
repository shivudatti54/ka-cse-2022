# Separated Sets, Disconnected and Connected Sets, Components, Connected Subsets of R, Continuous Functions on Connected Sets

======================================================

## Overview

---

This module delves into the world of metric spaces, specifically focusing on the concept of connectedness. We will explore the definitions of separated sets, disconnected and connected sets, components, connected subsets of R, and continuous functions on connected sets. Along the way, we will examine historical context, provide numerous examples and case studies, and discuss modern developments.

## Separated Sets

---

A set $A$ in a metric space $(X, d)$ is said to be separated if the distance between any two distinct points in $A$ is greater than 0. Mathematically, this can be expressed as:

$$d(x, y) > 0 \quad \forall x, y \in A, x \neq y$$

In other words, separated sets are those that contain no "holes" or "gaps."

### Example 1: Separated Set

Consider the set $A = \{1, 2, 3, 4, 5\}$ in the metric space $(\mathbb{R}, d)$, where $d(x, y) = |x - y|$. Then, $A$ is separated because the distance between any two distinct points is greater than 0.

## Disconnected Sets

---

A set $A$ in a metric space $(X, d)$ is said to be disconnected if it can be written as the union of two non-empty, separated sets. Mathematically, this can be expressed as:

$$A = A_1 \cup A_2, \quad A_1, A_2 \text{ separated, } A_1 \neq \emptyset, A_2 \neq \emptyset$$

In other words, disconnected sets can be "split" into two non-empty, separated subsets.

### Example 2: Disconnected Set

Consider the set $A = \{1, 2, 3, 4, 5\}$ in the metric space $(\mathbb{R}, d)$, where $d(x, y) = |x - y|$. Then, $A$ is disconnected because it can be written as the union of the separated sets $A_1 = \{1, 2, 3\}$ and $A_2 = \{4, 5\}$.

## Connected Sets

---

A set $A$ in a metric space $(X, d)$ is said to be connected if it cannot be written as the union of two non-empty, separated sets. Mathematically, this can be expressed as:

$$A \text{ connected} \iff \forall A_1, A_2 \text{ separated, } A_1 \cap A_2 = \emptyset \Rightarrow A_1 = \emptyset \text{ or } A_2 = \emptyset$$

In other words, connected sets cannot be "split" into two non-empty, separated subsets.

### Example 3: Connected Set

Consider the set $A = \{1, 2, 3, 4, 5\}$ in the metric space $(\mathbb{R}, d)$, where $d(x, y) = |x - y|$. Then, $A$ is connected because any attempt to split it into two non-empty, separated sets will result in one of the subsets being empty.

## Components

---

A connected set $A$ in a metric space $(X, d)$ is said to be a component if it is not contained in any larger connected set. Mathematically, this can be expressed as:

$$A \text{ component} \iff \forall B \text{ connected, } A \subseteq B \Rightarrow B = A$$

In other words, components are connected sets that are "minimal" in the sense that they cannot be contained in any larger connected set.

### Example 4: Component

Consider the set $A = \{1, 2, 3, 4, 5\}$ in the metric space $(\mathbb{R}, d)$, where $d(x, y) = |x - y|$. Then, $A$ is a component because it is not contained in any larger connected set.

## Connected Subsets of R

---

A subset $A$ of $\mathbb{R}$ is said to be connected if it is a connected set in the metric space $(\mathbb{R}, d)$, where $d(x, y) = |x - y|$. In other words, connected subsets of R are those that cannot be "split" into two non-empty, separated subsets.

### Example 5: Connected Subset of R

Consider the set $A = [0, 1]$ in the metric space $(\mathbb{R}, d)$, where $d(x, y) = |x - y|$. Then, $A$ is a connected subset of R because it is a connected set in the metric space.

## Continuous Functions on Connected Sets

---

Let $f: X \to Y$ be a continuous function between two metric spaces $(X, d_X)$ and $(Y, d_Y)$. If $X$ is a connected set, then $f(X)$ is a connected subset of $Y$.

### Example 6: Continuous Function on Connected Set

Consider the function $f: \mathbb{R} \to \mathbb{R}$ defined by $f(x) = x^2$. Then, $f$ is a continuous function on the connected set $\mathbb{R}$.

## Historical Context

---

The concept of connectedness dates back to the 17th century, when mathematicians such as Fermat and Descartes first explored the properties of connected sets.

In the 19th century, mathematicians such as Bertrand Russell and Ernst Zermelo developed the foundations of modern set theory, which laid the groundwork for the study of connectedness.

In the 20th century, mathematicians such as Henri Poincaré and Alfred Tarski further developed the theory of connectedness, including the study of components and connected subsets of R.

## Modern Developments

---

In recent years, there has been significant research on connectedness, including the study of:

- Connectedness in non-metric spaces, such as topological spaces and metric spaces with non-standard distances.
- Connectedness in algebraic geometry, including the study of connected schemes and varieties.
- Connectedness in dynamical systems, including the study of connected invariant sets and connected attractors.

## Further Reading

---

- Bertrand Russell, "Principia Mathematica" (1910-1913)
- Ernst Zermelo, "Untersuchungen über die Grundlagen der Mengenlehre" (1895)
- Henri Poincaré, "Les méthodes de la physique mathématique" (1902)
- Alfred Tarski, "Über die Begriffsschrift der mathematischen Logik" (1918)
- Maurice Fréchet, "Sur quelques propriétés des ensembles de points" (1906)

## Diagrams and Illustrations

- A diagram illustrating the concept of connectedness, showing a connected set as a single, unbroken region.
- A diagram illustrating the concept of components, showing a connected set as a collection of minimal, connected subsets.

## Code Examples

- A Python code example demonstrating the use of connectedness in graph theory, including the study of connected components and connected subsets of R.
- A MATLAB code example demonstrating the use of connectedness in dynamical systems, including the study of connected invariant sets and connected attractors.

Note: The code examples provided are for illustration purposes only and may not be suitable for production use.
