# Amortized Analysis

## Introduction
Amortized Analysis is a technique used in algorithm design to determine the **average time complexity** of operations performed on a data structure over a sequence of operations, even when the worst-case operation might be expensive. Unlike average-case analysis, amortized analysis guarantees performance over *any* sequence of operations, making it particularly useful for designing efficient data structures where occasional expensive operations are offset by many cheap ones.

## Key Concepts

### Why Amortized Analysis?
- Provides **stronger guarantees** than worst-case analysis
- Useful when occasional costly operations are necessary for long-term efficiency
- Focuses on *total time* divided by *number of operations*

### Three Main Methods

**1. Aggregate Analysis**
- Calculate total cost for sequence of n operations
- Amortized cost = Total cost / n
- **Example**: Dynamic array doubling — n insertions cost O(n), amortized cost per operation = O(1)

**2. Accounting Method**
- Assign *different* amortized costs to different operations
- Store "saved" time (credit) for cheap operations to pay for expensive ones
- **Constraint**: Total amortized cost ≥ total actual cost
- **Example**: Stack with multipop — Push: $2, Pop: $0 (uses stored credit)

**3. Potential Method**
- Define a *potential function* Φ(Di) measuring "stored energy" of data structure
- Amortized cost = Actual cost + ΔΦ (change in potential)
- Most general and flexible method
- **Formula**: âi = âi + Φ(Di) - Φ(Di-1)

### Common Examples (Delhi University Syllabus)

| Data Structure | Operation | Actual Cost | Amortized Cost |
|----------------|-----------|-------------|----------------|
| Dynamic Array | Insert | O(n) worst | O(1) |
| Stack | Multipop | O(n) | O(1) per pop |
| Binary Counter | Increment | O(k) worst | O(1) |

**Dynamic Array**: When array is full, create double-sized array and copy all elements. Although one insertion costs O(n), n insertions cost O(n) total, giving O(1) amortized.

**Binary Counter**: Increment operation may flip many bits, but total flips across n increments is O(n), making amortized cost O(1).

### Important Properties
- Differs from average-case (depends on probability distribution)
- Guarantees performance for *any* sequence
- Used in: Dynamic arrays, Fibonacci heaps, Splay trees, Union-Find

## Conclusion
Amortized analysis is essential for designing and analyzing efficient data structures. It provides a realistic measure of performance by considering the total cost over a sequence of operations rather than isolated worst cases. The three methods—Aggregate, Accounting, and Potential—offer different perspectives but yield the same amortized bounds for well-designed data structures. This technique is crucial for understanding modern algorithms and is a key topic in the Delhi University B.Sc. (H) Computer Science syllabus under Advanced Data Structures.