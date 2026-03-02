# Problem Solving Strategies in Object Oriented Programming (Python)

## A Comprehensive Study Material for BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

### 1.1 What is Problem Solving?

Problem solving is the systematic process of identifying a problem, analyzing it, and developing viable solutions using computational thinking. In the context of Object-Oriented Programming (OOP) with Python, problem solving involves breaking down complex real-world problems into smaller, manageable components and representing them as objects and classes.

### 1.2 Real-World Relevance

Problem solving skills are fundamental to every software developer and are extensively tested in placements, internships, and higher studies. Consider these practical applications:

- **Banking Systems**: Calculating interest, managing accounts, and processing transactions
- **E-commerce Platforms**: Shopping cart management, inventory systems, and recommendation engines
- **Social Media**: Friend suggestions, news feed algorithms, and message filtering
- **Healthcare Management**: Patient records, appointment scheduling, and billing systems
- **Navigation Apps**: Finding shortest paths, traffic optimization, and route planning

The Delhi University syllabus emphasizes problem solving because it forms the foundation for advanced topics like Data Structures, Algorithms, Database Management Systems, and Software Engineering.

### 1.3 Connection to Object-Oriented Programming

Python's OOP paradigm provides an excellent framework for problem solving because:
- **Encapsulation**: Bundles data and methods together
- **Inheritance**: Promotes code reuse
- **Polymorphism**: Allows flexible interfaces
- **Abstraction**: Simplifies complex systems

---

## 2. Algorithmic Thinking

### 2.1 Definition and Importance

Algorithmic thinking is the ability to formulate problems in terms of discrete steps and sequences. It involves:

1. **Decomposition**: Breaking complex problems into smaller parts
2. **Pattern Recognition**: Identifying similarities between problems
3. **Abstraction**: Focusing on important information only
4. **Algorithm Design**: Creating step-by-step solutions

### 2.2 Steps in Algorithmic Problem Solving

```
┌─────────────────────────────────────────────────────────┐
│           ALGORITHMIC PROBLEM SOLVING PROCESS           │
├─────────────────────────────────────────────────────────┤
│  1. Problem Understanding                               │
│     → Read carefully, identify inputs and outputs      │
│                                                         │
│  2. Input/Output Analysis                               │
│     → Define data types, constraints, format           │
│                                                         │
│  3. Algorithm Development                               │
│     → Choose appropriate strategy                      │
│                                                         │
│  4. Pseudocode/Flowchart Design                         │
│     → Plan the logic flow                              │
│                                                         │
│  5. Code Implementation                                 │
│     → Write clean, efficient Python code               │
│                                                         │
│  6. Testing and Debugging                               │
│     → Verify with various test cases                   │
│                                                         │
│  7. Optimization                                       │
│     → Improve time and space complexity                │
└─────────────────────────────────────────────────────────┘
```

### 2.3 Time and Space Complexity (Big O Notation)

Understanding complexity helps choose the right strategy:

| Complexity | Name | Example Operations |
|------------|------|---------------------|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search, traversal |
| O(n log n) | Linearithmic | Merge sort, quick sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Permutations |

---

## 3. Core Problem Solving Strategies

### 3.1 Brute Force Approach

**Definition**: Try all possible solutions until finding the correct one.

**When to Use**:
- Small input sizes
- When no better algorithm is obvious
- When simplicity matters more than efficiency

**Example**: Linear Search

```python
def linear_search(arr, target):
    """
    Brute Force: Check each element sequentially
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return index if found
    return -1  # Not found

# Test the function
numbers = [10, 25, 30, 45, 50, 65, 80]
result = linear_search(numbers, 45)
print(f"Element found at index: {result}")
```

### 3.2 Divide and Conquer

**Definition**: Break the problem into smaller subproblems, solve them recursively, and combine the results.

**When to Use**:
- Problems that can be divided into similar subproblems
- Sorting (merge sort, quick sort)
- Searching (binary search)
- Tree operations

**Key Steps**:
1. **Divide**: Split into smaller subproblems
2. **Conquer**: Solve subproblems recursively
3. **Combine**: Merge solutions

**Example**: Merge Sort Implementation

```python
def merge_sort(arr):
    """
    Divide and Conquer: Recursively sort and merge
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Conquer (recursive calls)
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combine (merge sorted halves)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = merge_sort(numbers)
print(f"Sorted array: {sorted_numbers}")
```

### 3.3 Dynamic Programming

**Definition**: Solve complex problems by breaking them into overlapping subproblems and storing their solutions to avoid redundant calculations.

**When to Use**:
- Problems with optimal substructure
- Problems with overlapping subproblems
- Optimization problems (minimization/maximization)

**Two Approaches**:
1. **Memoization (Top-Down)**: Recursive with caching
2. **Tabulation (Bottom-Up)**: Iterative with table filling

**Example**: Fibonacci Sequence

```python
# Method 1: Naive Recursive (Exponential Time)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Method 2: Dynamic Programming - Memoization (Top-Down)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Method 3: Dynamic Programming - Tabulation (Bottom-Up)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Method 4: Space-Optimized DP
def fib_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Test all methods
n = 50
print(f"Fibonacci at position {n}:")
print(f"Optimized DP result: {fib_optimized(n)}")
```

**Example**: Longest Common Subsequence (LCS)

```python
def lcs(str1, str2):
    """
    Dynamic Programming: Find longest common subsequence
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(str1), len(str2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Test
X = "AGGTAB"
Y = "GXTXAYB"
result = lcs(X, Y)
print(f"Length of LCS: {result}")  # Output: 4 (GTAB)
```

### 3.4 Greedy Algorithms

**Definition**: Make locally optimal choices at each step, hoping for a global optimum.

**When to Use**:
- Problems where local optimal leads to global optimal
- Activity selection
- Fractional knapsack
- Huffman coding
- Minimum spanning tree

**Example**: Activity Selection Problem

```python
def activity_selection(activities):
    """
    Greedy: Select maximum number of non-overlapping activities
    Time Complexity: O(n log n)
    """
    # Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[2])
    
    selected = [sorted_activities[0]]
    last_finish = sorted_activities[0][2]
    
    for i in range(1, len(sorted_activities)):
        # Start time >= last finish time
        if sorted_activities[i][1] >= last_finish:
            selected.append(sorted_activities[i])
            last_finish = sorted_activities[i][2]
    
    return selected

# Activities: (name, start_time, end_time)
activities = [
    ("A1", 0, 6),
    ("A2", 3, 4),
    ("A3", 1, 2),
    ("A4", 5, 8),
    ("A5", 5, 9),
    ("A6", 8, 10)
]

result = activity_selection(activities)
print("Selected activities:")
for activity in result:
    print(f"  {activity[0]}: {activity[1]} - {activity[2]}")
```

### 3.5 Backtracking

**Definition**: Build solutions incrementally and abandon solutions that fail to satisfy constraints.

**When to Use**:
- Constraint satisfaction problems
- Puzzle solving (Sudoku, N-Queens)
- Combinatorial problems
- Path finding

**Example**: N-Queens Problem

```python
def solve_n_queens(n):
    """
    Backtracking: Place n queens on n×n chessboard
    so no two attack each other
    Time Complexity: O(n!) - exponential
    """
    result = []
    board = [-1] * n  # board[i] = column position of queen in row i
    
    def is_safe(row, col):
        """Check if placing queen at (row, col) is safe"""
        for prev_row in range(row):
            prev_col = board[prev_row]
            # Check column and diagonals
            if prev_col == col or \
               prev_col == col - (row - prev_row) or \
               prev_col == col + (row - prev_row):
                return False
        return True
    
    def solve(row):
        if row == n:
            # Found valid solution
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1  # Backtrack
    
    solve(0)
    return result

# Solve for 4-Queens
solutions = solve_n_queens(4)
print(f"Number of solutions for 4-Queens: {len(solutions)}")
print("First solution (row-wise column positions):", solutions[0])
```

### 3.6 Recursion vs Iteration

Understanding when to use each approach:

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| **Definition** | Function calls itself | Loop-based execution |
| **Memory** | Uses call stack | Uses loop variables |
| **Speed** | Generally slower | Generally faster |
| **Readability** | Often cleaner for recursive problems | More explicit control |
| **Risk** | Stack overflow for deep recursion | Infinite loop risk |

**Example**: Converting Recursive to Iterative

```python
# Recursive approach
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test
print(f"Factorial (Recursive) 5! = {factorial_recursive(5)}")
print(f"Factorial (Iterative) 5! = {factorial_iterative(5)}")
```

---

## 4. Object-Oriented Problem Solving in Python

### 4.1 Designing Classes for Problem Solving

```python
class ProblemSolver:
    """Base class for problem solvers"""
    
    def __init__(self, name):
        self.name = name
        self.strategy = None
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def solve(self, problem):
        if self.strategy:
            return self.strategy.execute(problem)
        return None

class DivideAndConquerStrategy:
    def execute(self, problem):
        # Implementation
        return "Solved using Divide and Conquer"

class DynamicProgrammingStrategy:
    def execute(self, problem):
        # Implementation
        return "Solved using Dynamic Programming"

# Usage
solver = ProblemSolver("MySolver")
solver.set_strategy(DivideAndConquerStrategy())
print(solver.solve("Sample Problem"))
```

---

## 5. Practice Questions

### 5.1 Multiple Choice Questions (MCQs)

**Question 1**: Which strategy divides a problem into smaller subproblems, solves them recursively, and combines the results?
- A) Greedy Algorithm
- B) Divide and Conquer
- C) Backtracking
- D) Brute Force

**Question 2**: What is the time complexity of binary search?
- A) O(n)
- B) O(n²)
- C) O(log n)
- D) O(1)

**Question 3**: Dynamic Programming is used when a problem has:
- A) Only one optimal solution
- B) Overlapping subproblems and optimal substructure
- C) No recursive nature
- D) Small input size only

**Question 4**: In the Fibonacci sequence using memoization, what prevents redundant calculations?
- A) Loop
- B) Cache/Memo table
- C) Global variables
- D) Classes

**Question 5**: Which algorithmic approach makes locally optimal choices hoping for global optimum?
- A) Divide and Conquer
- B) Dynamic Programming
- C) Greedy Algorithm
- D) Backtracking

**Question 6**: The N-Queens problem is best solved using which approach?
- A) Brute Force
- B) Greedy
- C) Backtracking
- D) Dynamic Programming

**Question 7**: What is the space complexity of merge sort?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

**Question 8**: Which sorting algorithm uses the divide and conquer approach?
- A) Selection Sort
- B) Bubble Sort
- C) Merge Sort
- D) Insertion Sort

**Question 9**: The process of breaking a complex problem into smaller parts is called:
- A) Abstraction
- B) Decomposition
- C) Encapsulation
- D) Inheritance

**Question 10**: What type of problems are best suited for dynamic programming?
- A) Problems with no optimal solution
- B) Problems with overlapping subproblems
- C) Problems requiring user input
- D) Problems with no pattern

### 5.2 Fill in the Blanks

1. The process of building solutions incrementally and abandoning failed attempts is called __________.
2. In Big O notation, O(1) represents __________ complexity.
3. Merge sort has __________ time complexity.
4. The greedy approach makes __________ optimal choices.
5. Fibonacci using naive recursion has __________ time complexity.
6. Activity selection problem uses __________ algorithm.
7. In OOP, bundling data and methods together is called __________.
8. The strategy pattern in OOP allows changing __________ at runtime.
9. Binary search requires a __________ array.
10. Memoization in dynamic programming is also known as __________ top-down approach.

### 5.3 Flashcards

| Term | Definition |
|------|------------|
| **Algorithm** | A finite sequence of well-defined instructions for solving a problem |
| **Time Complexity** | Measure of time required by an algorithm as a function of input size |
| **Space Complexity** | Measure of memory required by an algorithm as a function of input size |
| **Divide and Conquer** | Algorithm design technique that breaks problems into smaller subproblems |
| **Dynamic Programming** | Technique to solve overlapping subproblems by storing solutions |
| **Greedy Algorithm** | Makes locally optimal choices at each step |
| **Backtracking** | Builds solutions incrementally and reverses when constraints fail |
| **Recursion** | Technique where a function calls itself to solve smaller instances |
| **Memoization** | Caching results of expensive function calls |
| **Optimal Substructure** | Property where optimal solution can be constructed from optimal solutions of subproblems |
| **Overlapping Subproblems** | Property where same subproblems are solved multiple times |
| **Brute Force** | Trying all possible solutions exhaustively |
| **Big O Notation** | Mathematical notation describing upper bound of algorithm complexity |
| **Base Case** | Condition that stops recursive calls |
| **Abstract Data Type** | A model for data structures with defined operations |

---

## 6. Key Takeaways

1. **Problem Solving is Fundamental**: Essential for programming interviews, software development, and advanced computer science topics.

2. **Choose the Right Strategy**:
   - **Brute Force**: Small inputs, simplicity priority
   - **Divide and Conquer**: Sortable data, searching
   - **Dynamic Programming**: Optimization with overlapping subproblems
   - **Greedy**: Locally optimal leads to global optimal
   - **Backtracking**: Constraint satisfaction, puzzles

3. **Complexity Analysis Matters**: Always consider time and space complexity when designing solutions.

4. **OOP Enhances Problem Solving**: Design patterns like Strategy, Factory, and Observer facilitate modular and maintainable solutions.

5. **Practice is Essential**: Regular coding practice on platforms like LeetCode, HackerRank improves problem-solving skills.

6. **Real-World Applications**: These strategies are used in AI, data science, game development, networking, and enterprise software.

7. **Delhi University Syllabus Alignment**: This content covers topics essential for BCA, BSc (H) Computer Science, and MCA programs under NEP 2024 UGCF.

---

## 7. References and Further Reading

- **Textbooks**:
  - "Introduction to Algorithms" by Cormen, Leiserson, Rivest, Stein
  - "Python Data Structures and Algorithms" by Benjamin Baka
  - "Problem Solving with Algorithms and Data Structures" by Miller and Ranum

- **Online Resources**:
  - GeeksforGeeks (Python Algorithms)
  - LeetCode Practice Problems
  - HackerRank Problem Solving

- **Delivery Unit Code**: This study material aligns with the Object-Oriented Programming Python course under Delhi University NEP 2024 UGCF curriculum.

---

*Prepared for BSc (Hons) Computer Science, Delhi University - NEP 2024 UGCF*