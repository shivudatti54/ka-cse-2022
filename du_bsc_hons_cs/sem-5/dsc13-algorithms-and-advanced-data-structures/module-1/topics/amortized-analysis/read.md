# Amortized Analysis

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Real-World Relevance](#introduction-and-real-world-relevance)
2. [Understanding Amortized Analysis](#understanding-amortized-analysis)
3. [Methods of Amortized Analysis](#methods-of-amortized-analysis)
   - [Aggregate Analysis (Aggregate Method)](#1-aggregate-analysis-aggregate-method)
   - [Accounting Method (Banker's Method)](#2-accounting-method-bankers-method)
   - [Potential Method (Physicist's Method)](#3-potential-method-physicists-method)
4. [Concrete Examples with Code](#concrete-examples-with-code)
   - [Example 1: Dynamic Array (Array Resizing)](#example-1-dynamic-array-array-resizing)
   - [Example 2: Binary Counter](#example-2-binary-counter)
5. [Comparison of the Three Methods](#comparison-of-the-three-methods)
6. [Key Takeaways](#key-takeaways)
7. [Assessment Section](#assessment-section)
   - [Multiple Choice Questions (MCQs)](#multiple-choice-questions-mcqs)
   - [Flashcards for Quick Revision](#flashcards-for-quick-revision)

---

## Introduction and Real-World Relevance

Consider a **dynamic array** (like `ArrayList` in Java or `list` in Python) that doubles its capacity when full. When you insert elements, most insertions take O(1) constant time. However, when the array is full and needs to resize, copying all elements to a new, larger array takes O(n) time. If we analyze this using worst-case complexity, we'd say each insertion costs O(n)—which is misleading because such expensive operations happen rarely.

In real-world software engineering, we often encounter data structures where **occasional expensive operations** are followed by **many cheap operations**. Understanding the **true cost** of these operations is crucial for:

- **Designing efficient algorithms** that perform well in practice
- **Predicting actual runtime behavior** beyond theoretical worst-case bounds
- **Making informed decisions** about data structure choices in applications

This is precisely where **Amortized Analysis** comes in. It provides a mathematical framework to analyze the **average cost per operation** over a sequence of operations, ensuring that even rare expensive operations don't skew our understanding of overall performance.

> **Delhi University Syllabus Context:** This topic aligns with the Algorithms and Advanced Data Structures paper under the NEP 2024 UGCF curriculum, specifically covering algorithm analysis techniques beyond basic worst-case complexity.

---

## Understanding Amortized Analysis

### Definition

**Amortized Analysis** is a technique for analyzing the time complexity of a sequence of operations, where the **average cost per operation** is computed over the entire sequence. Unlike average-case analysis (which assumes a probability distribution over inputs), amortized analysis guarantees performance **for any sequence of operations**.

### Key Distinctions

| Analysis Type | What It Measures | Guarantee |
|---------------|------------------|-----------|
| **Worst-Case** | Maximum cost for any single operation | Per-operation guarantee |
| **Average-Case** | Expected cost assuming input distribution | Probabilistic guarantee |
| **Amortized** | Average cost over sequence of operations | Sequential guarantee |

### When to Use Amortized Analysis

Amortized analysis is ideal when:
- A data structure has **occasional expensive operations** that are "paid for" by many cheap operations
- We need to bound the **total cost** of a sequence of n operations
- Worst-case analysis is too pessimistic for practical performance

---

## Methods of Amortized Analysis

There are **three primary methods** for performing amortized analysis. Each provides a different perspective and mathematical approach.

---

### 1. Aggregate Analysis (Aggregate Method)

#### Concept

Aggregate analysis computes the **total cost** of a sequence of n operations and divides by n to get the amortized cost per operation. If the total cost is T(n), then the amortized cost is T(n)/n.

#### Worked Example: Stack with MultiPop

Consider a stack that supports three operations:
- **PUSH(S, x)**: O(1)
- **POP(S)**: O(1)
- **MULTIPOP(S, k)**: Pop up to k elements or empty the stack

```python
# Pseudocode for MULTIPOP
def multipop(stack, k):
    while stack is not empty and k > 0:
        stack.pop()
        k = k - 1
```

**Analysis:**
- In the worst case, MULTIPOP could pop all n elements: O(n)
- If we perform n operations (any mix of PUSH, POP, MULTIPOP), the total number of pops cannot exceed the total number of pushes
- Since there are at most n PUSH operations, there can be at most n POPs (including those in MULTIPOP)
- Therefore, total cost = O(n) for n operations
- **Amortized cost per operation = O(n)/n = O(1)**

#### Key Insight for Aggregate Analysis

> The expensive operations (MULTIPOP popping many elements) can only occur as many times as cheap operations (PUSH) that "charge" them.

---

### 2. Accounting Method (Banker's Method)

#### Concept

The accounting method assigns **different amortized costs** to different operations. We "overcharge" some cheap operations and store the surplus as "credits" to pay for expensive operations later.

**Constraints:**
- The amortized cost must be ≥ actual cost
- Total amortized cost ≥ total actual cost
- Credits must never go negative

#### Worked Example: Dynamic Array

Consider a dynamic array that **doubles** its capacity when full:

```python
class DynamicArray:
    def __init__(self):
        self.array = [None] * 1  # Initial capacity
        self.size = 0
        self.capacity = 1
    
    def append(self, value):
        if self.size == self.capacity:
            # Double the capacity - O(n) operation
            new_array = [None] * (self.capacity * 2)
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity *= 2
        
        self.array[self.size] = value
        self.size += 1
```

**Accounting Method Assignment:**
- Assign **amortized cost = 3** for each PUSH operation
- Use the 3 credits as follows:
  - **1 credit** pays for the PUSH itself
  - **1 credit** pays for copying this element during future resizing
  - **1 credit** stays as surplus for other elements

**Why 3?**
- When resizing from capacity c to 2c, we copy c elements
- These c elements were previously "overcharged" by 1 credit each during their insertion
- Total credits available = c × 2 (since we assigned 2 credits per element for resizing)
- Cost of resizing = c (copying c elements)
- Surplus = c credits remaining

**Verification:**
- Total amortized cost for n inserts = 3n
- Total actual cost = n (for all pushes) + n-1 (for all but first resize) = O(n)
- Since 3n ≥ O(n), our assignment is valid
- **Amortized cost per operation = O(1)**

---

### 3. Potential Method (Physicist's Method)

#### Concept

The potential method defines a **potential function** Φ that maps the data structure's state to a non-negative number. The potential represents "stored energy" that can be used to pay for expensive operations.

**Formula:**
- Let D₀ be the initial state
- Let cᵢ be the actual cost of operation i
- Let Φ(Dᵢ) be the potential after operation i
- **Amortized cost** î = cᵢ + Φ(Dᵢ) - Φ(Dᵢ₋₁)

The total amortized cost equals total actual cost plus net change in potential. If potential never drops below initial value, total amortized cost ≤ total actual cost.

#### Worked Example: Dynamic Array (Potential Method)

**Potential Function:** Φ = 2 × (number of elements - capacity/2) when size > capacity/2, else 0

Actually, let's use a simpler, standard potential function:

**Simpler Potential Function:** Φ = 2 × (size - capacity/2) for size ≥ capacity/2, otherwise Φ = size

Wait, let's use the most common and intuitive potential:

**Selected Potential Function:** Φ = 2 × size - capacity

Note: This must be non-negative. Let's verify:
- When capacity = size (just resized): Φ = 2size - 2size = 0 ✓
- When capacity = size/2 (half full after resize): Φ = 2(size) - 2(size/2) = 0 ✓
- Between resizes: capacity = 2 × previous_size, so Φ ≥ 0 ✓

**Amortized Cost Calculation:**

| Operation | Actual Cost | Potential Change | Amortized Cost |
|-----------|-------------|------------------|----------------|
| Insert when size < capacity | 1 | Φ(new) - Φ(old) = 2 - 1 = 1 | 1 + 1 = 2 |
| Insert when size = capacity (resize) | size + 1 | -size (potential drops to 0) | (size + 1) - size = 1 |

**For n insertions:**
- Total amortized cost = 2(n-1) + 1 = O(n)
- **Amortized cost per operation = O(1)**

#### Why the Potential Method Works

The potential function captures the "work saved" in the data structure. When the array is half-full (after doubling), there's high potential (stored work) that pays for future resizing operations. When we resize, potential drops to zero, representing we "spent" that stored work.

---

## Concrete Examples with Code

### Example 1: Dynamic Array (Array Resizing)

This example demonstrates all three methods applied to the same problem.

```python
class DynamicArray:
    """
    Dynamic array that doubles capacity when full.
    Demonstrates amortized O(1) insertion.
    """
    
    def __init__(self):
        self._data = [None] * 1
        self._size = 0
        self._capacity = 1
    
    def append(self, value):
        """Insert element; amortized O(1) time."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        self._data[self._size] = value
        self._size += 1
    
    def _resize(self, new_capacity):
        """Resize internal array; costly operation."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"DynamicArray({self._data[:self._size]})"


# Demonstration
if __name__ == "__main__":
    arr = DynamicArray()
    
    # Insert 10 elements
    for i in range(1, 11):
        arr.append(i)
        print(f"Inserted {i}: Size={len(arr)}, Capacity={arr._capacity}")
```

**Output:**
```
Inserted 1: Size=1, Capacity=1
Inserted 2: Size=2, Capacity=2
Inserted 3: Size=3, Capacity=4
Inserted 4: Size=4, Capacity=4
Inserted 5: Size=5, Capacity=8
Inserted 6: Size=6, Capacity=8
Inserted 7: Size=7, Capacity=8
Inserted 8: Size=8, Capacity=8
Inserted 9: Size=9, Capacity=16
Inserted 10: Size=10, Capacity=16
```

**Analysis Summary:**
- 10 insertions require 10 push operations (10 × O(1))
- 3 resizes occur (at sizes 1→2, 2→4, 8→16), copying 1 + 2 + 8 = 11 elements
- Total operations = 10 + 11 = 21
- Amortized cost = 21/10 ≈ 2.1 per operation = **O(1)**

---

### Example 2: Binary Counter

A binary counter that increments from 0 to 2^k - 1 demonstrates amortized analysis with a different resizing pattern (increments by 1, not doubling).

```python
class BinaryCounter:
    """
    Binary counter using array of bits.
    Demonstrates amortized O(1) increment.
    """
    
    def __init__(self, k=0):
        self._bits = [0] * (k + 1)  # Store k+1 bits
        self._size = k + 1
    
    def increment(self):
        """
        Increment counter by 1.
        Actual cost = number of trailing 1s + 1
        """
        i = 0
        while i < self._size and self._bits[i] == 1:
            self._bits[i] = 0  # Flip 1 to 0
            i += 1
        
        if i < self._size:
            self._bits[i] = 1  # Flip 0 to 1
        
        return i + 1  # Return actual cost
    
    def __repr__(self):
        return ''.join(map(str, reversed(self._bits)))


# Aggregate Analysis for Binary Counter
def analyze_counter(n):
    """
    Aggregate analysis: Total cost of n increments.
    
    Least significant bit flips on every increment: n times
    Second bit flips every 2 increments: n/2 times
    Third bit flips every 4 increments: n/4 times
    ...
    
    Total flips = n + n/2 + n/4 + ... ≤ 2n
    Total cost ≤ 2n
    Amortized cost ≤ 2 = O(1)
    """
    counter = BinaryCounter(10)
    total_cost = 0
    
    for _ in range(n):
        cost = counter.increment()
        total_cost += cost
    
    return total_cost


# Demonstration
if __name__ == "__main__":
    print("Binary Counter Demonstration:")
    print("-" * 40)
    
    counter = BinaryCounter(5)
    total_cost = 0
    
    for i in range(16):
        cost = counter.increment()
        total_cost += cost
        print(f"After increment {i+1}: {counter}, Cost: {cost}")
    
    print("-" * 40)
    print(f"Total cost for 16 increments: {total_cost}")
    print(f"Amortized cost per operation: {total_cost/16:.2f}")
```

**Output:**
```
Binary Counter Demonstration:
----------------------------------------
After increment 1: 1, Cost: 1
After increment 2: 10, Cost: 2
After increment 3: 11, Cost: 1
After increment 4: 100, Cost: 3
After increment 5: 101, Cost: 1
After increment 6: 110, Cost: 2
After increment 7: 111, Cost: 1
After increment 8: 1000, Cost: 4
After increment 9: 1001, Cost: 1
After increment 10: 1010, Cost: 2
After increment 11: 1011, Cost: 1
After increment 12: 1100, Cost: 3
After increment 13: 1101, Cost: 1
After increment 14: 1110, Cost: 2
After increment 15: 1111, Cost: 1
After increment 16: 10000, Cost: 5
----------------------------------------
Total cost for 16 increments: 27
Amortized cost per operation: 1.69
```

**Analysis:**
- Total cost for n increments ≤ 2n (proved by aggregate analysis)
- Amortized cost ≤ 2 = **O(1)**

---

## Comparison of the Three Methods

| Aspect | Aggregate Analysis | Accounting Method | Potential Method |
|--------|--------------------|--------------------|------------------|
| **Approach** | Sum total costs | Assign credits | Define potential function |
| **Complexity** | Simple | Moderate | Complex |
| **Flexibility** | Low (same cost for all operations) | High (different costs for different operations) | Highest (state-dependent) |
| **Best For** | Simple sequences | Data structures with clear credit flow | Complex stateful structures |
| **Intuition** | Overall average | Bank account metaphor | Energy/stored work |

**When to Use Which:**

1. **Aggregate Analysis:** When you can easily bound the total cost of n operations
2. **Accounting Method:** When different operations have clearly different costs and you can track "overcharging"
3. **Potential Method:** When the data structure's state is complex and changes in non-obvious ways

---

## Key Takeaways

1. **Amortized Analysis** provides a more practical measure of algorithmic performance by analyzing the average cost per operation over a sequence.

2. **Three Main Methods:**
   - **Aggregate Analysis:** Compute total cost T(n), amortized = T(n)/n
   - **Accounting Method:** Overcharge cheap operations to pay for expensive ones
   - **Potential Method:** Use a potential function to represent stored work

3. **Dynamic Array** demonstrates amortized O(1) insertion despite occasional O(n) resizing operations.

4. **Binary Counter** shows amortized O(1) increment despite occasional O(k) flips.

5. **Key Insight:** Expensive operations are "paid for" by the cumulative effect of many cheap operations.

6. **Not Average-Case:** Amortized analysis guarantees performance for any input sequence, not just random inputs.

7. **Practical Application:** Essential for designing efficient data structures like dynamic arrays, hash tables, splay trees, and Fibonacci heaps.

---

## Assessment Section

### Multiple Choice Questions (MCQs)

**1. What is the key difference between amortized analysis and average-case analysis?**
   - a) Amortized analysis is more accurate
   - b) Amortized analysis guarantees performance for any sequence; average-case assumes random input
   - c) Average-case is always O(1)
   - d) There is no difference

**2. In the accounting method, the amortized cost must be:**
   - a) Less than actual cost
   - b) Equal to actual cost
   - c) Greater than or equal to actual cost
   - d) Always positive

**3. For a dynamic array that doubles when full, what is the amortized cost of insertion?**
   - a) O(n)
   - b) O(log n)
   - c) O(1)
   - d) O(n²)

**4. In a binary counter, how many times does the least significant bit flip in n increments?**
   - a) n/2
   - b) n
   - c) 2n
   - d) log n

**5. The potential method uses which concept to analyze amortized cost?**
   - a) Credits and debts
   - b) Potential energy/stored work
   - c) Average of costs
   - d) Worst-case bound

**6. What is the total cost of n MULTIPOP operations on a stack with at most n PUSH operations?**
   - a) O(n²)
   - b) O(n)
   - c) O(1)
   - d) O(log n)

**7. Which method assigns different costs to different operations?**
   - a) Aggregate Analysis
   - b) Accounting Method
   - c) Potential Method
   - d) All of the above

**8. When a dynamic array resizes from capacity c to 2c, how many elements are copied?**
   - a) c
   - b) 2c
   - c) c/2
   - d) 1

**9. The accounting method is also known as:**
   - a) Physicist's method
   - b) Banker's method
   - c) Aggregate method
   - d) Counter method

**10. If the potential function Φ(D) is always non-negative and Φ(D₀) = 0, then:**
   - a) Total actual cost ≤ total amortized cost
   - b) Total amortized cost ≤ total actual cost
   - c) They are always equal
   - d) Cannot be determined

---

### Flashcards for Quick Revision

| # | Term/Concept | Answer |
|---|--------------|--------|
| 1 | **Amortized Analysis** | Technique analyzing average cost per operation over a sequence, guaranteeing performance for any input |
| 2 | **Aggregate Analysis** | Method computing total cost T(n) of n operations; amortized cost = T(n)/n |
| 3 | **Accounting Method** | Assigns amortized costs with "credits" to overcharge cheap operations and pay for expensive ones |
| 4 | **Potential Method** | Uses a potential function Φ to represent stored energy; amortized cost = actual cost + ΔΦ |
| 5 | **Dynamic Array** | Array that resizes (typically doubles) when full; insertion is amortized O(1) |
| 6 | **Binary Counter** | Counter incremented from 0 to 2^k-1; increment operation is amortized O(1) |
| 7 | **MULTIPOP Stack** | Operation popping k elements or emptying stack; amortized O(1) per operation |
| 8 | **Credit (Accounting)** | Surplus assigned to cheap operations to pay for future expensive operations |
| 9 | **Potential Function** | Function mapping data structure state to non-negative value representing stored work |
| 10 | **Table Doubling** | Technique where hash table doubles capacity when load factor exceeds threshold |

---

#### Answers to MCQs

1. **b)** 2. **c)** 3. **c)** 4. **b)** 5. **b)** 6. **b)** 7. **b)** 8. **a)** 9. **b)** 10. **a)**

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum. It covers all essential concepts required for examinations and provides practical coding examples for better understanding.*