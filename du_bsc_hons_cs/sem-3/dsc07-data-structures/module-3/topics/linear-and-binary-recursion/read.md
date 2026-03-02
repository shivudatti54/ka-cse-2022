# Linear and Binary Recursion

## Introduction
Recursion is one of the most fundamental and powerful concepts in computer science and programming. It is a problem-solving technique where a function calls itself to solve smaller instances of the same problem. In the University of Delhi's Data Structures curriculum, understanding recursion is essential because it forms the backbone of many advanced algorithms and data structures like trees, graphs, and sorting algorithms.

Linear and binary recursion represent two distinct patterns of recursive calls that every computer science student must master. Linear recursion involves a single recursive call per function execution, making it the simpler and more straightforward form. Binary recursion, on the other hand, involves two recursive calls in each recursive case, enabling divide-and-conquer strategies. Both patterns have significant applications in real-world computing, from file system navigation to optimization problems.

This topic carries substantial weight in DU examinations, with questions frequently appearing in both internal assessments and end-semester exams. Students often find recursion challenging initially, but with proper understanding of the mechanics and sufficient practice, it becomes an invaluable tool in their algorithmic toolkit.

## Key Concepts

### What is Recursion?
Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem. A recursive function has two essential components:
1. **Base Case (Stopping Condition)**: The condition under which the recursion terminates
2. **Recursive Case**: The part where the function calls itself with a smaller or simpler version of the problem

The general structure follows: solve problem directly if it's simple enough, otherwise break it into similar subproblems and apply recursion to solve them.

### Linear Recursion
Linear recursion occurs when a recursive function makes exactly one recursive call in each recursive case. The computation typically proceeds from the top down, with each call working on a progressively smaller instance of the problem.

The execution forms a linear chain of function calls. Each call reduces the problem size by a fixed amount (typically 1) until reaching the base case. The results then propagate back through the call chain.

**Example - Factorial**:
```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case (linear)
```

### Binary Recursion
Binary recursion occurs when a function makes two recursive calls in each recursive case. This pattern is fundamental to divide-and-conquer algorithms, where a problem is split into two equal or nearly equal subproblems.

**Example - Fibonacci**:
```python
def fibonacci(n):
    if n <= 0:  # Base case
        return 0
    if n == 1:  # Base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Two recursive calls
```

### Recursion vs Iteration
While both recursion and iteration solve problems through repetition, they differ significantly in implementation and resource usage:

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Implementation | Function calls itself | Uses loops (for, while) |
| Memory | Uses call stack | Uses constant memory |
| Base Case | Required for termination | Loop condition |
| Readability | Often more elegant for recursive problems | Often more efficient |

### Stack Frames and Memory
Each recursive call creates a new stack frame containing local variables, return address, and parameters. The stack grows with each call and shrinks as base cases are reached. This is why space complexity equals the maximum depth of the recursion.

### Recursion Tree
A recursion tree provides a visual representation of recursive function execution. For linear recursion, it's a straight line; for binary recursion, it forms a branching tree structure. This tool is invaluable for analyzing time and space complexity.

## Examples

### Example 1: Linear Recursion - Sum of Array Elements
**Problem**: Write a recursive function to find the sum of all elements in an array.

**Solution**:
```python
def sum_array(arr, n):
    # Base case: empty array has sum 0
    if n == 0:
        return 0
    # Recursive case: last element plus sum of remaining elements
    return arr[n-1] + sum_array(arr, n-1)

# Example usage
arr = [1, 2, 3, 4, 5]
result = sum_array(arr, 5)
print(result)  # Output: 15
```

**Step-by-step execution for sum_array([1,2,3,4,5], 5)**:
1. Call: sum_array([1,2,3,4,5], 5) → returns 5 + sum_array([1,2,3,4,5], 4)
2. Call: sum_array([1,2,3,4,5], 4) → returns 4 + sum_array([1,2,3,4,5], 3)
3. Call: sum_array([1,2,3,4,5], 3) → returns 3 + sum_array([1,2,3,4,5], 2)
4. Call: sum_array([1,2,3,4,5], 2) → returns 2 + sum_array([1,2,3,4,5], 1)
5. Call: sum_array([1,2,3,4,5], 1) → returns 1 + sum_array([1,2,3,4,5], 0)
6. Base Case: sum_array([1,2,3,4,5], 0) → returns 0
7. Unwinding: 1+0=1, 2+1=3, 3+3=6, 4+6=10, 5+10=15

**Time Complexity**: O(n), **Space Complexity**: O(n)

### Example 2: Binary Recursion - Fibonacci Sequence
**Problem**: Write a recursive function to find the nth Fibonacci number.

**Solution**:
```python
def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Binary recursive case: two recursive calls
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
result = fibonacci(6)
print(result)  # Output: 8 (sequence: 0,1,1,2,3,5,8)
```

**Execution tree for fibonacci(4)**:
```
fibonacci(4)
├── fibonacci(3)
│   ├── fibonacci(2)
│   │   ├── fibonacci(1) = 1
│   │   └── fibonacci(0) = 0
│   │   └── returns 1
│   └── fibonacci(1) = 1
│   └── returns 2
└── fibonacci(2)
    ├── fibonacci(1) = 1
    └── fibonacci(0) = 0
    └── returns 1
└── returns 3
```

**Time Complexity**: O(2^n) - exponential without optimization
**Space Complexity**: O(n) - maximum depth of recursion tree

### Example 3: Binary Search using Recursion
**Problem**: Implement binary search using recursion to find an element in a sorted array.

**Solution**:
```python
def binary_search(arr, target, low, high):
    # Base case: element not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    # Recursive case: search in left half
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # Recursive case: search in right half
    else:
        return binary_search(arr, target, mid + 1, high)

# Example usage
arr = [2, 3, 4, 10, 40, 50, 60, 70]
target = 10
result = binary_search(arr, target, 0, len(arr)-1)
print(f"Element found at index: {result}")  # Output: Element found at index: 3
```

**Step-by-step search for target=50**:
1. low=0, high=7, mid=3, arr[3]=10 < 50 → Search right half
2. low=4, high=7, mid=5, arr[5]=50 → Found! Return 5

**Time Complexity**: O(log n), **Space Complexity**: O(log n)

## Exam Tips

1. **Identify the Type of Recursion**: Always determine whether the problem requires linear or binary recursion. Linear has one recursive call, binary has two.

2. **Always Identify the Base Case**: In exam questions, the base case is your safety net. Without it, you'll get infinite recursion and zero marks.

3. **Draw the Recursion Tree**: For binary recursion problems, drawing even a small recursion tree helps visualize the problem and avoid mistakes.

4. **Analyze Time and Space Complexity**: DU exams frequently ask for complexity analysis. Remember: linear recursion is typically O(n) time, O(n) space. Binary recursion without optimization is O(2^n), with optimization like binary search it's O(log n).

5. **Trace Through Execution**: When stuck, manually trace through 2-3 iterations to understand the pattern. This often reveals the solution.

6. **Convert to Iteration if Needed**: Some problems that seem recursive can be solved iteratively with better space complexity. Know when to use which.

7. **Remember the Unwinding Phase**: The result doesn't appear immediately. Each recursive call must complete and return before the final answer emerges.

8. **Practice Previous Year Questions**: DU frequently repeats question patterns. Practice problems from past years thoroughly.

9. **Understand Tail Recursion**: Tail recursion occurs when the recursive call is the last operation. Some compilers optimize it to use constant space.

10. **Handle Edge Cases**: Always consider what happens with n=0, n=1, empty arrays, or invalid inputs in your solution.