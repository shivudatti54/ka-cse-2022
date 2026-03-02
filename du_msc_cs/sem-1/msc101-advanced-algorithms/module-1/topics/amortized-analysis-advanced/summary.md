# Amortized Analysis Advanced - Quick Revision Summary

## Introduction
Amortized analysis is a technique for analyzing algorithms to determine the average time per operation over a worst-case sequence of operations. Unlike average-case analysis, it guarantees performance over any sequence, making it essential for data structures like dynamic arrays, stacks, and advanced tree structures. This topic is core to the Delhi University MSc CS syllabus under "Advanced Algorithms."

## Key Concepts

### 1. Fundamentals
- **Purpose**: Bound the total cost of a sequence of operations, giving average cost per operation in the worst case
- **Difference from average-case**: Uses probability over all inputs; amortized analysis guarantees performance regardless of input distribution
- **Types of bounds**: Worst-case amortized, deterministic, and randomized amortized analysis

### 2. Methods of Amortized Analysis

#### Aggregate Analysis
- Charges total cost to all operations equally
- Example: Dynamic array with doubling strategy—n insert operations cost O(n), amortized cost O(1) per insert

#### Accounting Method
- Assigns varying charges to different operations
- prepaid credit stored in data structure "bank account" to pay for expensive operations
- Example: Stack with multipush/multipop—push costs 2, pop costs 0

#### Potential Method
- Uses a potential function Φ mapping states to non-negative values
- Amortized cost = actual cost + ΔΦ (change in potential)
- Most flexible and commonly used in advanced analysis

### 3. Classic Examples
- **Dynamic Array**: Resizing by doubling gives O(1) amortized insert
- **Binary Counter**: Increment operation costs O(1) amortized using accounting method
- **Stack with Multipop**: O(1) amortized per operation using aggregate or accounting method

### 4. Advanced Data Structures (Delhi University Syllabus)
- **Splay Trees**: Amortized O(log n) access using potential method (self-adjusting property)
- **Fibonacci Heaps**: O(1) amortized insert, decrease-key; O(log n) amortized delete-min
- **Red-Black Trees**: O(log n) guaranteed for all operations
- **Binomial Heaps**: Amortized analysis for merge operations

### 5. Important Theorems & Results
- **Splay Tree Theorem**: Access costs O(log n) amortized per operation
- **Fibonacci Heap Bounds**: Insert O(1), Delete-min O(log n), Decrease-key O(1) amortized
- **Potential Function Design**: Must be non-negative and reflect "saved work"

### 6. Exam-Relevant Points
- Remember: Amortized ≠ average-case; it provides guaranteed bounds
- Practice identifying when to use each method—aggregate for simple sequences, potential for complex structures
- Know how to construct potential functions for splay trees and Fibonacci heaps

## Conclusion
Amortized analysis is crucial for designing efficient data structures. The three methods—aggregate, accounting, and potential—provide tools to prove bounds for dynamic data structures. Understanding this topic is essential for exam success and practical algorithm design. Focus on examples and potential function construction for maximum retention.

---
*Reference: Delhi University MSc CS Syllabus - Advanced Algorithms (2024-2025)*