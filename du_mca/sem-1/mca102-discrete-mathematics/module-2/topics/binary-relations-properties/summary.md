# Binary Relations – Quick Revision (MCA – Delhi University, Revised June 2024)

## Introduction
A **binary relation** \(R\) from set \(A\) to set \(B\) is a subset of the Cartesian product \(A\times B\). When \(A=B\) we speak of a relation **on** the set \(A\). Relations are used to model ordering, equivalence, connectivity, and many other structures in discrete mathematics.

---

## Core Properties (for a relation on a set \(A\))

- **Reflexive** – \(\forall x\in A,\;(x,x)\in R\).  
- **Irreflexive** – \(\forall x\in A,\;(x,x)\notin R\).  
- **Symmetric** – \(\forall x,y\in A,\;(x,y)\in R\Rightarrow(y,x)\in R\).  
- **Antisymmetric** – \(\forall x,y\in A,\;(x,y)\in R\land(y,x)\in R\Rightarrow x=y\).  
- **Asymmetric** – \(\forall x,y\in A,\;(x,y)\in R\Rightarrow(y,x)\notin R\).  
- **Transitive** – \(\forall x,y,z\in A,\;(x,y)\in R\land(y,z)\in R\Rightarrow(x,z)\in R\).

> **Note:** A relation can be *both* symmetric and antisymmetric only if it is a subset of the identity (i.e., each ordered pair is of the form \((x,x)\)).

---

## Important Types of Relations (Syllabus – Unit “Relations & Functions”)

- **Equivalence Relation** – reflexive + symmetric + transitive.  
  - *Equivalence class*: \([a]=\{x\mid (a,x)\in R\}\).  
  - Partition of \(A\) into disjoint equivalence classes.

- **Partial Order (Poset)** – reflexive + antisymmetric + transitive.  
  - **Hasse diagram** visualises the order.  
  - *Total order (chain)*: every pair of elements is comparable.  
  - *Well-ordering*: every non‑empty subset has a least element.

- **Strict Partial Order** – irreflexive + transitive (equivalently, asymmetric + transitive).

---

## Operations & Closures

- **Composition**: \(R\circ S = \{(x,z)\mid\exists y\;(x,y)\in R\land(y,z)\in S\}\).  
- **Inverse (Converse)**: \(R^{-1} = \{(y,x)\mid(x,y)\in R\}\).  
- **Union / Intersection** of relations inherit property combinations (e.g., union of two symmetric relations is symmetric).  

**Closures** (smallest superset with the property):  
- **Reflexive closure**: \(R\cup I_A\).  
- **Symmetric closure**: \(R\cup R^{-1}\).  
- **Transitive closure**: \(R^{+}= \bigcup_{i=1}^{\infty}R^{i}\) (or using Warshall’s algorithm).  

The *equivalence closure* is the transitive closure of the symmetric closure of \(R\).

---

## Exam Quick‑Revision Points

- **Checklist** when analysing a relation:  
  1. Draw the **digraph** or **matrix** – visual inspection reveals symmetry/antichain patterns.  
  2. Verify each property with a generic element argument.  
- **Common traps**:  
  - “Antisymmetric” is **not** the same as “asymmetric”.  
  - A relation can be **neither** reflexive nor irreflexive.  
- **Theorems**:  
  - *If a relation is both an equivalence relation and a partial order, it must be the identity relation.*  
  - *Every partial order can be extended to a total order (Zorn’s Lemma).*  

---

## Conclusion
Binary relations and their properties form the backbone of ordering and equivalence concepts in discrete mathematics. Master the definitions, recognise the four key properties (reflexive, symmetric, antisymmetric, transitive), and be comfortable constructing closures and identifying equivalence classes and posets. This core knowledge is essential for the Delhi University MCA examinations and for later topics such as graph theory and lattice theory.