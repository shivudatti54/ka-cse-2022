# Chapter 12: Limitations of Algorithmic Power

## Section 12.1: Decision Trees, P, NP, and NP-Complete Problems

### 12.1.1 Introduction

One of the fundamental limitations of algorithmic power is the concept of decision trees and the relationships between their computational complexities, denoted by P, NP, and NP-complete problems.

### 12.1.2 Decision Trees

A decision tree is a flowchart representing a tree-like structure of decisions and their possible outcomes. Each decision node in the tree represents a test on a particular feature or attribute, and each leaf node represents a class label or outcome.

#### **Key Concepts:**

- **Decision Tree**: A decision tree is a flowchart representing a tree-like structure of decisions and their possible outcomes.
- **Decision Node**: A decision node in the tree represents a test on a particular feature or attribute.
- **Leaf Node**: A leaf node in the tree represents a class label or outcome.

### 12.1.3 P (Polynomial Time)

The complexity class P denotes the set of all decision problems that can be solved in polynomial time by a deterministic Turing machine. In other words, a problem is in P if it can be solved in a finite amount of time, where the amount of time is proportional to the size of the input.

#### **Key Concepts:**

- **Polynomial Time**: A decision problem can be solved in polynomial time if it can be solved in a finite amount of time, where the amount of time is proportional to the size of the input.
- **Deterministic Turing Machine**: A deterministic Turing machine is an abstract device that can read and write symbols on an infinite tape according to a set of rules.

### 12.1.4 NP (Nondeterministic Polynomial Time)

The complexity class NP denotes the set of all decision problems that can be verified in polynomial time by a nondeterministic Turing machine. In other words, a problem is in NP if it can be verified in a finite amount of time, where the amount of time is proportional to the size of the input.

#### **Key Concepts:**

- **Nondeterministic Polynomial Time**: A decision problem can be verified in nondeterministic polynomial time if it can be verified in a finite amount of time, where the amount of time is proportional to the size of the input.
- **Nondeterministic Turing Machine**: A nondeterministic Turing machine is an abstract device that can read and write symbols on an infinite tape according to a set of probabilistic rules.

### 12.1.5 NP-Complete Problems

An NP-complete problem is a decision problem that is both in NP and NP-hard. NP-complete problems are problems that are at least as hard as the hardest problems in NP. In other words, if a problem can be solved in polynomial time, then all NP-complete problems can be solved in polynomial time.

#### **Key Concepts:**

- **NP-Complete**: A decision problem is NP-complete if it is both in NP and NP-hard.
- **NP-Hard**: A decision problem is NP-hard if it is at least as hard as the hardest problems in NP.

### 12.1.6 Example Problems

- **Traveling Salesman Problem**: The traveling salesman problem is an NP-hard problem that involves finding the shortest possible tour that visits a set of cities and returns to the starting city.
- **Circuit Scheduling Problem**: The circuit scheduling problem is an NP-complete problem that involves scheduling the production of a circuit and determining the minimum time required to complete the production.

### 12.1.7 Conclusion

In conclusion, decision trees, P, NP, and NP-complete problems represent the fundamental limitations of algorithmic power. Understanding these concepts is essential for designing efficient algorithms and solving complex problems in computer science.

### 12.1.8 Summary

| Complexity Class | Description                                               | Key Concepts                                                                       |
| ---------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| P                | Decision problems that can be solved in polynomial time   | Polynomial time, deterministic Turing machine, and input size.                     |
| NP               | Decision problems that can be verified in polynomial time | Nondeterministic polynomial time, nondeterministic Turing machine, and input size. |
| NP-Complete      | Decision problems that are both in NP and NP-hard         | NP-complete, NP-hard, and the relationship between the two.                        |
