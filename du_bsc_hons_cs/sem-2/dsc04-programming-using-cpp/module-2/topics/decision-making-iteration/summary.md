# Decision Making & Iteration in C++

## Introduction
Decision making and iteration are fundamental control flow structures in C++ that enable programs to make choices and repeat actions. These concepts form the backbone of algorithmic problem-solving and are essential for the Delhi University B.Sc. (Hons) Computer Science (NEP 2024 UGCF) syllabus under the "Programming Using C++" course.

---

## Decision Making Statements

Decision making allows the program to execute specific blocks of code based on certain conditions.

### 1. **if Statement**
- Executes a block only if the condition is true
- Syntax: `if (condition) { statements; }`

### 2. **if-else Statement**
- Provides alternative path when condition is false
- Syntax: `if (condition) { ... } else { ... }`

### 3. **else-if Ladder**
- Checks multiple sequential conditions
- Syntax: `if (cond1) { } else if (cond2) { } else { }`

### 4. **Switch Statement**
- Multiple-choice selection based on constant values
- Uses `case`, `break`, and `default` keywords
- More efficient than else-if for discrete values

### 5. **Conditional/Ternary Operator**
- Shorthand: `condition ? expr1 : expr2`

---

## Iteration (Looping) Statements

Loops enable repetitive execution of code blocks.

### 1. **for Loop**
- Used when number of iterations is known
- Syntax: `for (initialization; condition; increment) { }`
- Ideal for counting and array traversal

### 2. **while Loop**
- Pre-test loop (checks condition before execution)
- Syntax: `while (condition) { statements; }`
- Used when iterations depend on dynamic conditions

### 3. **do-while Loop**
- Post-test loop (executes at least once)
- Syntax: `do { statements; } while (condition);`
- Useful for menu-driven programs

### 4. **Range-based for Loop (C++11)**
- Simplified iteration over containers
- Syntax: `for (auto var : container) { }`

---

## Jump Statements

Control the flow of program execution.

- **break**: Exits the loop or switch immediately
- **continue**: Skips current iteration, proceeds to next
- **return**: Exits function and optionally returns value
- **goto**: Transfers control to labeled statement (avoid usage)

---

## Key Differences

| Aspect | Decision Making | Iteration |
|--------|-----------------|-----------|
| Purpose | Choose between paths | Repeat actions |
| Execution | Once per condition | Multiple times |
| Examples | if, switch, ternary | for, while, do-while |

---

## Common Patterns for Exams

1. **Menu-driven programs**: Use do-while + switch
2. **Pattern printing**: Nested for loops
3. **Summation/Counting**: for loop with accumulators
4. **Input validation**: while loop with condition check

---

## Conclusion
Mastery of decision making and iteration is crucial for problem-solving in C++. These control structures enable programmers to write efficient, dynamic, and logical code. Understanding when to use each structure (if vs switch, for vs while) is key to writing optimized programs, as covered in the Delhi University syllabus for C++ programming.