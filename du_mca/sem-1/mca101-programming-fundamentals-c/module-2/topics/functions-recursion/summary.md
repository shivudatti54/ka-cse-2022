# Functions and Recursion in C - Summary

## Key Definitions and Concepts

- **Function:** A self-contained block of code that performs a specific task and promotes code reusability and modularity.
- **Function Prototype:** A declaration that specifies the function's name, return type, and parameter list.
- **Actual Parameters:** Variables or values passed to a function at the call site.
- **Formal Parameters:** Variables declared in the function definition that receive values from actual parameters.
- **Call by Value:** Parameter passing method where a copy of the argument is passed; original values remain unchanged.
- **Call by Reference:** Parameter passing method where the address of the argument is passed, allowing modification of original values.
- **Recursion:** A programming technique where a function calls itself to solve a problem by breaking it into smaller sub-problems.
- **Base Case:** The terminating condition in recursion that stops further recursive calls.
- **Stack Frame (Activation Record):** Memory allocated on the stack when a function is called, containing return address, local variables, and parameters.

## Important Formulas and Theorems

- **Factorial:** n! = n × (n-1)!, with base case 0! = 1! = 1
- **Fibonacci:** F(n) = F(n-1) + F(n-2), with F(0) = 0, F(1) = 1
- **Binary Search Recurrence:** T(n) = T(n/2) + O(1), resulting in O(log n) time complexity
- **Recursion Time Complexity:** For T(n) = T(n-1) + O(1), complexity is O(n)

## Key Points

- Every C program must have a `main()` function as the entry point.
- Functions can be categorized into four types based on parameters and return values.
- C uses call by value by default; call by reference requires using pointers.
- Recursion requires a well-defined base case to prevent infinite loops.
- Each recursive call creates a new stack frame, consuming stack memory.
- Tail recursion can be optimized by compilers to use constant stack space.
- The naive recursive Fibonacci has exponential time complexity O(2^n).
- Binary search using recursion has O(log n) time complexity.
- Iterative solutions are often more efficient than recursive solutions in terms of memory usage.

## Common Mistakes to Avoid

1. **Forgetting the base case:** This causes infinite recursion and stack overflow, crashing the program.
2. **Confusing call by value with call by reference:** Remember that simple parameter passing in C does not modify the original variables.
3. **Not updating the recursive parameter:** The recursive call must move toward the base case; otherwise, infinite recursion occurs.
4. **Ignoring stack overflow:** For large inputs, recursion may exhaust stack memory; consider iterative alternatives.

## Revision Tips

1. Practice tracing recursive functions by drawing the call stack manually.
2. Write both iterative and recursive versions of common problems to understand the differences.
3. Memorize the standard recursive patterns: factorial, Fibonacci, binary search, and array operations.
4. Focus on identifying the base case first when solving recursive problems.
5. Review past DU exam questions on functions and recursion to understand the question pattern and difficulty level.