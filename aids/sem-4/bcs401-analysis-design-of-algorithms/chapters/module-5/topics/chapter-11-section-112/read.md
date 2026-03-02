# Chapter 11: Section 11.2 - Limitations of Algoritmic Power

=====================================================

## Introduction

---

Algorithms are a crucial part of computer science, and they have numerous applications in various fields. However, there are limitations to the power of algorithms. In this section, we will discuss the limitations of algoritmic power, focusing on decision trees, P, NP, and NP-complete problems.

## Decision Trees

---

### Definition

A decision tree is a tree-like model of decision problems. It is a diagram representing a tree-like structure, where each internal node represents a decision point, and each leaf node represents an outcome.

### Properties

- Decision trees are based on a set of rules or conditions that determine the next decision point.
- They can be used to solve a wide range of decision problems, such as classification and regression problems.

### Example

Suppose we want to design a decision tree to predict whether a person will buy a car based on their income and age.

| Age | Income | Will Buy Car? |
| --- | ------ | ------------- |
| 18  | 40000  | Yes           |
| 18  | 60000  | Yes           |
| 25  | 40000  | No            |
| 25  | 60000  | Yes           |

In this example, the decision tree would look like this:

```
          +---------------+
          |  Age  = 18   |
          +---------------+
                  |
                  |
                  v
+---------------+      +---------------+
|  Income  = 40000 |      |  Income  = 60000 |
+---------------+      +---------------+
|  Yes       |      |  Yes       |
|  No        |      |  No        |
+---------------+      +---------------+
```

## P, NP, and NP-Complete Problems

---

### Definitions

- P (Polynomial Time): A set of decision problems that can be solved in polynomial time, which means the running time grows polynomially with the size of the input.
- NP (Nondeterministic Polynomial Time): A set of decision problems that can be verified in polynomial time, but may not be solvable in polynomial time.
- NP-Complete: A set of problems that are in NP and NP-complete, which means they can be verified in polynomial time, but may not be solvable in polynomial time.

### Properties

- P problems can be solved exactly in a reasonable amount of time.
- NP problems can be verified exactly in a reasonable amount of time, but may not be solvable exactly in a reasonable amount of time.
- NP-complete problems are at least as hard as the hardest problems in NP.

### Examples

- P problems: Sorting and searching algorithms.
- NP problems: Traveling salesman problem and the knapsack problem.
- NP-complete problems: The Boolean satisfiability problem (SAT) and the traveling salesman problem.

### Key Concepts

- **NP-hardness**: A problem is NP-hard if it is at least as hard as the hardest problems in NP.
- **Reducibility**: A problem A is reducible to problem B if there exists an algorithm that can solve problem A given a solution to problem B.

### Example

Suppose we want to show that the traveling salesman problem is NP-complete.

- We can reduce the SAT problem to the traveling salesman problem: given a Boolean formula, we can construct a graph where each variable and its negation are connected by an edge, and the edges have weights that represent the clauses in the formula.
- If the SAT problem is solvable, then we can find a solution to the traveling salesman problem, and vice versa.

## Limitations of Algoritmic Power

---

### Conclusion

Algorithms are powerful tools for solving decision problems, but they also have limitations. Decision trees are a type of algorithm that can be used to solve a wide range of decision problems, but they may not always be able to find the optimal solution. P, NP, and NP-complete problems are different types of decision problems that have different levels of difficulty and complexity.

### Key Takeaways

- Decision trees are a type of algorithm that can be used to solve decision problems.
- P problems can be solved exactly in a reasonable amount of time.
- NP problems can be verified exactly in a reasonable amount of time, but may not be solvable exactly in a reasonable amount of time.
- NP-complete problems are at least as hard as the hardest problems in NP.
