# Recursion - Summary

## Key Definitions and Concepts

- RECURSION: A programming technique where a function calls itself to solve a problem by breaking it into smaller sub-problems.
- BASE CASE: The terminating condition in a recursive function that stops further recursive calls and returns a direct result.
- RECURSIVE CASE: The part of a recursive function where the problem is reduced and the function calls itself with modified parameters.
- CALL STACK: A stack data structure that stores information about each active function call, including local variables and return addresses.
- STACK OVERFLOW: An error that occurs when the call stack exceeds its memory limit due to excessive recursive calls.

## Important Formulas and Theorems

- FACTORIAL: n! = n × (n-1)!, with base case 0! = 1
- FIBONACCI: F(n) = F(n-1) + F(n-2), with F(0) = 0, F(1) = 1
- RECURRENCE RELATION: A formula that defines each term of a sequence using preceding terms, fundamental to analyzing recursive algorithms

## Key Points

- EVERY RECURSIVE FUNCTION MUST HAVE A BASE CASE to prevent infinite recursion
- EACH RECURSIVE CALL MUST MOVE TOWARD THE BASE CASE by modifying parameters appropriately
- RECURSION CREATES MULTIPLE STACK FRAMES, consuming O(n) space where n is recursion depth
- TAIL RECURSION has the recursive call as the last statement but C compilers do not optimize it
- TREE RECURSION (like Fibonacci) has EXPONENTIAL TIME COMPLEXITY O(2^n) in naive implementation
- BINARY SEARCH USING RECURSION divides search space by half at each step, achieving O(log n) complexity
- ITERATION is generally MORE MEMORY-EFFICIENT than recursion for simple repetitive tasks

## Common Mistakes to Avoid

- FORGETTING THE BASE CASE: This causes infinite recursion and program crash
- NOT MODIFYING PARAMETERS CORRECTLY: Parameters must change toward the base case in each recursive call
- ASSUMING ALL PROBLEMS NEED RECURSION: Using recursion where iteration suffices wastes memory
- IGNORING STACK LIMITATIONS: Deep recursion (thousands of calls) can overflow the stack in C
- CONFUSING RETURN VALUES: Not properly handling what each recursive call returns and how it's used

## Revision Tips

- PRACTICE TRACING RECURSIVE FUNCTIONS by writing out each call and return value on paper
- MEMORIZE STANDARD PATTERNS: factorial, Fibonacci, sum, reversal, and binary search are exam favorites
- ALWAYS START BY IDENTIFYING THE BASE CASE before writing any recursive function
- COMPARE ITERATIVE AND RECURSIVE SOLUTIONS for the same problem to understand trade-offs
- PRACTICE BINARY SEARCH RECURSION as it combines recursion with a critical searching algorithm