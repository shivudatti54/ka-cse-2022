# Functions & Recursion

## Introduction
Functions are fundamental building blocks in programming that enable code modularity and reusability. A function is a self-contained block of code that performs a specific task, accepting inputs through parameters and returning outputs. In professional software development, functions help manage complexity through abstraction and separation of concerns.

Recursion is a powerful technique where a function calls itself directly or indirectly to solve problems that can be broken into smaller, identical sub-problems. While iterative solutions use loops, recursive approaches often provide elegant solutions for problems like tree traversals, mathematical sequences, and divide-and-conquer algorithms. However, improper use can lead to stack overflows and performance issues.

The importance of mastering recursion lies in its prevalence in advanced algorithms (DFS, backtracking) and functional programming paradigms. DU's MCA program emphasizes this concept as it forms the basis for understanding computational complexity and memory management in recursive systems.

## Key Concepts
1. **Function Anatomy**:
   - Declaration: `return_type function_name(parameters)`
   - Parameters (formal vs actual)
   - Return statement and type matching
   - Scope: Local vs Global variables

2. **Recursion Fundamentals**:
   - Base Case: Termination condition preventing infinite loops
   - Recursive Case: Problem decomposition
   - Call Stack: LIFO structure managing function calls
   - Stack Frames: Activation records storing function state

3. **Tail Recursion**:
   - Special case where recursive call is last operation
   - Enables compiler optimization (equivalent to iteration)
   - Example: `return factorial(n-1, n*accumulator)`

4. **Memory Considerations**:
   - Space Complexity: O(n) for linear recursion vs O(1) for iteration
   - Stack Overflow Risk: Default stack size ~1MB (~10^4 calls depth)

5. **Recursive Problem Patterns**:
   - Direct vs Indirect Recursion
   - Tree Recursion (multiple recursive calls)
   - Mutual Recursion (functions calling each other)

## Examples

**Example 1: Factorial Calculation**
```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n-1)
```
**Step-by-Step Execution**:
factorial(3) 
→ 3 * factorial(2)
→ 3 * (2 * factorial(1))
→ 3 * (2 * (1 * factorial(0)))
→ 3 * (2 * (1 * 1)) = 6

**Example 2: Fibonacci Sequence**
```c
int fib(int n) {
    if(n <= 1) return n;
    return fib(n-1) + fib(n-2);
}
```
**Call Tree for fib(4)**:
```
       fib(4)
       /    \
    fib(3)  fib(2)
    /  \     /   \
 fib(2)fib(1)fib(1)fib(0)
 /  \
fib(1)fib(0)
```

**Example 3: Directory Traversal (Pseudocode)**
```
function list_files(directory):
    for entry in directory:
        if entry is file:
            print(entry)
        else:
            list_files(entry)  # Recursive call
```

## Exam Tips
1. **Base Case Identification**: Always verify termination condition first
2. **Tracing Practice**: Draw call trees for small n values (n=3-5)
3. **Tail Recursion Detection**: Check if recursive call is last operation
4. **Space Analysis**: Count maximum simultaneous stack frames
5. **Iterative Conversion**: Replace recursion with stack data structure
6. **Edge Cases**: Handle n=0, negative numbers, empty data structures
7. **Memoization**: Suggest optimization for overlapping subproblems