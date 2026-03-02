# Asymptotic Notations

## Introduction

Asymptotic notations are mathematical tools used to describe the limiting behavior of a function when its argument tends towards a particular value or infinity. In the context of computer science and algorithm analysis, these notations provide a standardized way to express the efficiency and performance of algorithms without getting bogged down in implementation details or hardware-specific characteristics.

When we analyze algorithms, we are primarily concerned with how the execution time or memory requirements grow as the input size increases. This growth rate is what matters most in determining an algorithm's scalability. For instance, an algorithm that takes 5 seconds for 10 elements but 500 seconds for 100 elements clearly doesn't scale well compared to one that takes 5 seconds for 10 elements and 10 seconds for 100 elements.

The study of asymptotic notations forms the foundation of algorithm analysis and is crucial for making informed design choices when implementing software systems. In the University of Delhi's Computer Science curriculum, this topic appears prominently in papers like DSC07-Data Structures and DSC06-Theory of Computation, making it essential for students to master these concepts thoroughly.

## Key Concepts

### Big O Notation (O-notation)

Big O notation describes an upper bound on the time complexity of an algorithm. It tells us the worst-case scenario - the maximum time an algorithm will take. Formally, we say f(n) = O(g(n)) if there exist positive constants c and n₀ such that 0 ≤ f(n) ≤ c × g(n) for all n ≥ n₀.

The function f(n) represents the actual running time, while g(n) is a simpler function that bounds it from above. Common Big O complexities, from most efficient to least efficient, are: O(1) - constant time, O(log n) - logarithmic time, O(n) - linear time, O(n log n) - linearithmic time, O(n²) - quadratic time, O(n³) - cubic time, and O(2ⁿ) - exponential time.

### Big Omega Notation (Ω-notation)

Big Omega notation provides a lower bound on the time complexity, representing the best-case scenario or the minimum time an algorithm will require. Formally, f(n) = Ω(g(n)) if there exist positive constants c and n₀ such that 0 ≤ c × g(n) ≤ f(n) for all n ≥ n₀.

Understanding the lower bound is equally important because it tells us the absolute minimum time we cannot improve beyond. For example, any comparison-based sorting algorithm has a lower bound of Ω(n log n).

### Theta Notation (Θ-notation)

Theta notation provides a tight bound, meaning it describes both the upper and lower bounds when they are the same. We say f(n) = Θ(g(n)) if there exist positive constants c₁, c₂, and n₀ such that 0 ≤ c₁ × g(n) ≤ f(n) ≤ c₂ × g(n) for all n ≥ n₀.

When an algorithm has Θ(g(n)) complexity, we say it "grows exactly as fast as" g(n). This is the most precise classification we can give.

### Little O Notation (o-notation)

Little O notation describes an upper bound that is not tight. While Big O allows for equality (f(n) can equal c × g(n) for large n), little o strictly means f(n) grows strictly slower than g(n). Formally, f(n) = o(g(n)) if for all c > 0, there exists n₀ such that 0 ≤ f(n) < c × g(n) for all n ≥ n₀.

### Little Omega Notation (ω-notation)

Little Omega is the opposite of little O - it describes a lower bound that is not tight. f(n) = ω(g(n)) means f(n) grows strictly faster than g(n).

### Properties and Theorems

Several important properties govern asymptotic notations. **Transitivity** states that if f(n) = O(g(n)) and g(n) = O(h(n)), then f(n) = O(h(n)). Similarly, this applies to Ω, Θ, o, and ω notations. **Reflexivity** means f(n) = O(f(n)), f(n) = Ω(f(n)), and f(n) = Θ(f(n)). **Symmetry** applies only to Θ: if f(n) = Θ(g(n)), then g(n) = Θ(f(n)). **Transpose symmetry** states that f(n) = O(g(n)) if and only if g(n) = Ω(f(n)), and f(n) = o(g(n)) if and only if g(n) = ω(f(n)).

## Examples

### Example 1: Analyzing a Simple Loop

Consider the following code:

```
for (i = 1; i ≤ n; i++)
    x = x + 1;
```

The loop runs n times, and each iteration takes constant time. Therefore, the time complexity is O(n), Ω(n), and Θ(n).

**Step-by-step analysis:**
- The loop executes exactly n times (from i = 1 to i = n)
- Each iteration performs one addition operation, which is O(1)
- Total time = n × O(1) = O(n)
- Since this is both upper and lower bound, it's Θ(n)

### Example 2: Nested Loops

Consider the algorithm:

```
for (i = 1; i ≤ n; i++)
    for (j = 1; j ≤ n; j++)
        print(i, j)
```

The outer loop runs n times, and for each iteration of the outer loop, the inner loop also runs n times. Therefore, the total number of operations is n × n = n².

- Time complexity: O(n²), Ω(n²), Θ(n²)

### Example 3: Logarithmic Time

Consider binary search:

```
low = 0, high = n-1
while (low ≤ high):
    mid = (low + high) / 2
    if (arr[mid] == target):
        return mid
    else if (arr[mid] < target):
        low = mid + 1
    else:
        high = mid - 1
```

In binary search, the search space reduces by half in each iteration. After k iterations, the remaining elements are n/2^k. The search continues until only one element remains, so n/2^k = 1, giving us k = log₂n.

- Time complexity: O(log n), Ω(log n), Θ(log n)

### Example 4: Proving Big O

**Prove that 3n² + 5n + 7 = O(n²)**

We need to find constants c and n₀ such that: 3n² + 5n + 7 ≤ c × n² for all n ≥ n₀

Let n ≥ 1:
- 3n² + 5n + 7 ≤ 3n² + 5n² + 7n² = 15n²

So c = 15 and n₀ = 1 works. Therefore, 3n² + 5n + 7 = O(n²).

### Example 5: Comparing Functions

Arrange in ascending order of growth:
n³, log n, 2ⁿ, n, n log n, √n, 1

**Answer (from slowest to fastest growth):**
1 < log n < √n < n < n log n < n³ < 2ⁿ

This order follows the hierarchy: constant < logarithmic < square root < linear < linearithmic < polynomial < exponential

## Exam Tips

1. **Remember the formal definitions**: For exam questions requiring proofs, you must state the definitions of Big O, Ω, and Θ correctly with the inequalities and quantifiers (∃c, n₀ such that ∀n ≥ n₀).

2. **Know the relationship between notations**: Big O gives upper bound, Ω gives lower bound, Θ gives tight bound. Remember: f = O(g) iff g = Ω(f).

3. **Practice identifying the dominant term**: When analyzing polynomials like 4n³ + 2n² + 5n + 1, always drop lower-order terms - the dominant term (n³) determines the complexity.

4. **Drop constants**: In Big O analysis, we drop constants. O(5n) is simply O(n), and O(3n²) is O(n²).

5. **Understand when to use each notation**: Use Big O for worst-case analysis (most common), Ω for best-case analysis, and Θ when upper and lower bounds are the same.

6. **Be careful with logarithms**: Remember that log₂n = log₁₀n = logₑn differ only by a constant factor, so all logarithms are O(log n).

7. **Common complexities to memorize**: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ). This hierarchy is frequently tested.

8. **Practice previous year questions**: DU exams often ask students to find the complexity of code segments or prove relationships between functions using asymptotic notation.