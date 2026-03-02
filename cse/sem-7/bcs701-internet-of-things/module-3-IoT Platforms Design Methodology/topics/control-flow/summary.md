# Control Flow in Python for IoT - Summary

## Key Definitions

- **Control Flow**: The order in which statements, instructions, and function calls are executed in a program.
- **Conditional Statement**: A programming construct that executes different code paths based on boolean conditions (if-elif-else).
- **Iteration**: The repetitive execution of a code block using loops (for, while).
- **Loop Control Statement**: Statements that modify loop execution (break terminates, continue skips iteration, pass is placeholder).
- **Exception Handling**: Mechanism to handle runtime errors gracefully using try-except-finally blocks.
- **State Machine**: A computational model that transitions between discrete states based on conditions, implementable using match-case.

## Important Formulas

- **Time Complexity for Sequential Processing**: O(n) for processing n sensor readings
- **Time Complexity for Nested Loops**: O(m × n) for m sensors over n time periods
- **Loop Iteration Count**: For `range(n)`, exactly n iterations execute

## Key Points

1. Python uses indentation to define code blocks within control structures, unlike brace-based languages.

2. Conditional statements in Python evaluate conditions sequentially; the first True condition executes and subsequent conditions are skipped.

3. For loops iterate over sequences and are ideal for known iteration counts; while loops continue until a condition becomes false.

4. The break statement terminates the entire loop, while continue skips only the current iteration.

5. Match-case (Python 3.10+) provides pattern matching useful for implementing device state machines and message handling.

6. Exception handling with try-except-finally ensures IoT systems handle sensor failures gracefully without crashing.

7. Nested control structures enable complex multi-sensor decision making but increase code complexity.

8. In IoT contexts, common falsy values include 0 (sensor readings), None (sensor failure), and empty collections.

9. The finally block executes regardless of exceptions, essential for resource cleanup in IoT applications.

10. Time complexity analysis helps optimize IoT code for real-time constraints on resource-constrained devices.

## Common Mistakes

1. **Confusing break and continue**: Students often use break when continue is needed, terminating entire loops instead of skipping individual iterations.

2. **Missing indentation**: Python requires consistent indentation; errors here cause syntax failures or incorrect program behavior.

3. **Catching exceptions in wrong order**: Catching general Exception before specific ones prevents proper error handling; always catch specific exceptions first.

4. **Off-by-one errors in range()**: Remember that range(n) generates 0 to n-1, not 1 to n; common in sensor array indexing.

5. **Not handling None values**: IoT sensors frequently return None on failure; failing to check for None before processing causes runtime errors.