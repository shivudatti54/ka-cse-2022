# Linear and Binary Recursion - Summary

## Key Definitions and Concepts
- **Recursion**: A programming technique where a function calls itself to solve smaller instances of the same problem
- **Base Case**: The condition that terminates recursion; without it, infinite recursion occurs
- **Recursive Case**: The part where the function calls itself with a smaller or simpler subproblem
- **Linear Recursion**: Recursion with exactly one recursive call in each recursive case
- **Binary Recursion**: Recursion with two recursive calls in each recursive case
- **Recursion Tree**: A visual representation showing all recursive calls and their relationships

## Important Formulas and Theorems
- **Linear Recursion Time Complexity**: O(n) typically
- **Binary Recursion Time Complexity**: O(2^n) without optimization, O(log n) with divide-and-conquer
- **Space Complexity**: O(n) for both types - equals maximum recursion depth
- **Fibonacci**: T(n) = T(n-1) + T(n-2) + O(1), solving to O(2^n)
- **Binary Search**: T(n) = T(n/2) + O(1), solving to O(log n)

## Key Points
- Every recursive function MUST have a base case to prevent infinite recursion
- Linear recursion processes data in a single direction (typically left-to-right or top-to-bottom)
- Binary recursion divides problem into two equal subproblems - fundamental to divide-and-conquer
- The call stack grows with each recursive call and shrinks when base cases are reached
- Recursion trees help visualize complex recursive executions
- Binary recursion without memoization has exponential time complexity due to overlapping subproblems
- Binary search exemplifies efficient binary recursion with O(log n) complexity
- Iterative solutions often use less memory than recursive ones
- Tail recursion can be optimized by some compilers to use constant space

## Common Mistakes to Avoid
1. **Forgetting the base case**: This causes stack overflow and infinite recursion
2. **Incorrect base case**: Using wrong termination condition leads to wrong answers
3. **Not reducing problem size**: Each recursive call must move toward the base case
4. **Ignoring overlapping subproblems**: In binary recursion like Fibonacci, same values are computed repeatedly
5. **Confusing return values**: Not properly handling what each recursive call should return

## Revision Tips
1. Practice tracing recursive functions by hand - this builds intuition
2. Draw recursion trees for at least 3-4 levels to understand execution flow
3. Memorize the complexity analysis formulas as they're frequently asked in exams
4. Solve at least 5 problems each of linear and binary recursion types
5. Compare recursive and iterative solutions side-by-side to understand trade-offs