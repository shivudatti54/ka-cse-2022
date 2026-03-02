# Applications of Stacks

## Introduction

A stack is a fundamental linear data structure that follows the **Last-In, First-Out (LIFO)** principle. This means the last element added to the stack is the first one to be removed. While understanding the operations (Push, Pop) and implementations (using arrays or linked lists) of a stack is crucial, its true power is revealed in its diverse applications across computer science. This module explores the most common and important real-world applications of stacks.

## 1. Expression Evaluation

One of the most classic applications of a stack is in the evaluation of arithmetic expressions. Computers need a way to unambiguously parse and compute expressions written by humans. Stacks are instrumental in converting expressions into forms that are easier for machines to evaluate and in performing the evaluation itself.

### 1.1. Infix, Prefix, and Postfix Notation

- **Infix Notation:** This is the standard notation we use daily, where the operator is placed _between_ the operands (e.g., `A + B`). It requires knowledge of operator precedence and parentheses to define the order of evaluation.
- **Prefix (Polish) Notation:** The operator is placed _before_ the operands (e.g., `+ A B`). It requires no parentheses and is evaluated from right to left.
- **Postfix (Reverse Polish) Notation:** The operator is placed _after_ the operands (e.g., `A B +`). It requires no parentheses and is evaluated from left to right. This notation is ideally suited for stack-based evaluation.

**Comparison of Notations**
| Notation | Example Expression | Operator Position | Parentheses Needed? | Evaluation Direction |
| :--- | :--- | :--- | :--- | :--- |
| Infix | `(A + B) * C` | Between operands | Yes | Requires precedence rules |
| Prefix | `* + A B C` | Before operands | No | Right to Left |
| Postfix | `A B + C *` | After operands | No | Left to Right |

### 1.2. Conversion from Infix to Postfix

The algorithm to convert an infix expression to a postfix expression uses a stack to keep track of operators.

**Algorithm Steps:**

1.  Initialize an empty stack for operators and an empty string for the output.
2.  Scan the infix expression from left to right.
3.  If the scanned character is an operand (letter or digit), add it to the output string.
4.  If the scanned character is an opening parenthesis `(`, push it onto the stack.
5.  If the scanned character is a closing parenthesis `)`, pop from the stack and add to the output string until an opening parenthesis is encountered. Pop and discard the opening parenthesis.
6.  If the scanned character is an operator:
    - While the stack is not empty, the top has an operator of greater or equal precedence, and the top is not an opening parenthesis, pop the operator from the stack and add it to the output.
    - Push the current scanned operator onto the stack.
7.  After the entire expression is scanned, pop all remaining operators from the stack and add them to the output.

**Example: Convert `(A + B) * C` to Postfix**

| Symbol | Action        | Stack (top->bottom) | Output String |
| :----- | :------------ | :------------------ | :------------ |
| `(`    | Push `(`      | `(`                 | ``            |
| `A`    | Add to output | `(`                 | `A`           |
| `+`    | Push `+`      | `( +`               | `A`           |
| `B`    | Add to output | `( +`               | `A B`         |
| `)`    | Pop until `(` | ``                  | `A B +`       |
| `*`    | Push `*`      | `*`                 | `A B +`       |
| `C`    | Add to output | `*`                 | `A B + C`     |
| End    | Pop all       | ``                  | `A B + C *`   |

**Final Postfix Expression:** `A B + C *`

### 1.3. Evaluation of Postfix Expression

Postfix evaluation is straightforward with a stack. The algorithm requires a stack for operands.

**Algorithm Steps:**

1.  Initialize an empty stack for operands.
2.  Scan the postfix expression from left to right.
3.  If the scanned element is an operand, push it onto the stack.
4.  If the scanned element is an operator, pop the top two operands from the stack. Apply the operator to them (note: the first popped element is `operand2`, the second is `operand1`). Push the result back onto the stack.
5.  After the entire expression is scanned, the stack will contain exactly one element, which is the final result.

**Example: Evaluate `5 3 2 * +` (which is `5 + (3 * 2)` in infix)**

| Symbol | Action                                                            | Stack (top->bottom) |
| :----- | :---------------------------------------------------------------- | :------------------ |
| `5`    | Push `5`                                                          | `5`                 |
| `3`    | Push `3`                                                          | `5, 3`              |
| `2`    | Push `2`                                                          | `5, 3, 2`           |
| `*`    | Pop `2` (op2), Pop `3` (op1)<br>Compute `3 * 2 = 6`<br>Push `6`   | `5, 6`              |
| `+`    | Pop `6` (op2), Pop `5` (op1)<br>Compute `5 + 6 = 11`<br>Push `11` | `11`                |

**Final Result:** `11`

## 2. Function Call Management

This is perhaps the most fundamental application of stacks, deeply integrated into how programming languages work. Whenever a function is called, an **activation record** (or stack frame) is created. This record contains the function's parameters, local variables, return address, and other bookkeeping information. The system stack (or call stack) is used to manage these records.

**How it works:**

1.  **Calling a function:** The current function's state (return address, etc.) is pushed onto the call stack. A new stack frame for the called function is created and pushed on top.
2.  **Returning from a function:** The top stack frame (the currently executing function) is popped from the stack. The return address stored in the previous frame is used to resume execution of the caller function.

```
CALL STACK DIAGRAM:

main() {
    var x = 5;     | Stack Frame for main()
    funcA(x);       |-----------------------------
}                   | x = 5                     |
                    | Return Address: (line 4)   |
                    |============================|
funcA(int a) {      | Stack Frame for funcA()    |
    var b = 10;     |----------------------------|
    funcB(b);       | a = 5                      |
}                   | b = 10                     |
                    | Return Address: (line 11)  |
                    |============================|
funcB(int c) {      | Stack Frame for funcB()    |
    print(c);       |----------------------------|
} // returns        | c = 10                     |
                    | Return Address: (line 9)   |
                    `----------------------------'
```

_Figure: The call stack during the execution of `funcB`. The LIFO nature perfectly manages the nested function calls and returns._

## 3. Backtracking Algorithms

Backtracking is a problem-solving technique that involves building a solution incrementally and abandoning a path ("backtracking") as soon as it is determined to be invalid. A stack is the natural data structure to remember the path taken and the choices made at each step, allowing the algorithm to backtrack to a previous state.

**Common Example: The Maze Problem**

- **Problem:** Find a path from the start to the end of a maze.
- **Stack Use:** Each explored position is pushed onto the stack. When a dead end is reached (no valid moves), the algorithm backtracks by popping the current position from the stack, returning to the previous junction to try a different path.

```
ASCII MAZE EXAMPLE:

S: Start, E: End, #: Wall, .: Path

S . # # #
# . . . #
# # . # #
# # . . E
# # # # .

STACK TRACE (positions as (row, col)):
Push (0,0) -> Start
Push (0,1) -> Move Right
Push (1,1) -> Move Down (from (0,1))
Push (1,2) -> Move Right
Push (1,3) -> Move Right
Push (1,4) -> Move Right -> Dead End!
Pop() -> Back to (1,3)
Pop() -> Back to (1,2)
Push (2,2) -> Move Down -> Path continues...
... eventually leading to E.
```

## 4. Depth-First Search (DFS) in Graphs

DFS is a fundamental graph traversal algorithm that explores as far as possible along a branch before backtracking. This "go deep first" behavior is perfectly implemented using a stack.

**Algorithm Steps:**

1.  Start from a source node, mark it visited, and push it onto the stack.
2.  While the stack is not empty:
    a. Pop the top node.
    b. For each unvisited adjacent node of the popped node:
    _ Mark it as visited.
    _ Push it onto the stack.

This process ensures that the most recently discovered node is explored next (LIFO), leading to the depth-first exploration.

## 5. Undo/Redo Mechanism

The undo and redo features in applications like text editors, graphic design software, and IDEs are classic examples of stack applications.

- **Undo Stack:** Every action performed by the user (e.g., typing text, drawing a shape) is recorded as a command object and pushed onto an _undo stack_.
- **Undo:** When the user triggers undo, the top command is popped from the undo stack and its `undo()` method is executed, reverting the state. This command is then pushed onto a _redo stack_.
- **Redo:** When the user triggers redo, the top command is popped from the redo stack and its `execute()` method is run again. This command is pushed back onto the undo stack.

This two-stack system (one for undo, one for redo) provides a clean and efficient way to manage state history.

## 6. Browser History

The back and forward buttons in a web browser function similarly to undo/redo.

- **Back Stack:** As you navigate to new pages, each URL is pushed onto a _back stack_.
- **Back Button:** Clicking "back" pops the current page from the back stack and pushes it onto a _forward stack_, then navigates to the new top of the back stack.
- **Forward Button:** Clicking "forward" pops a page from the forward stack and pushes it back onto the back stack, then navigates to that page.

## 7. Other Applications

- **Syntax Parsing:** Compilers use stacks to check for balanced symbols (e.g., parentheses `()`, braces `{}`, brackets `[]`) in source code.
- **String Reversal:** Pushing each character of a string onto a stack and then popping them all off will reverse the string.
- **Iterative Solutions for Recursive Problems:** Any recursive algorithm (e.g., Tower of Hanoi) can be implemented iteratively using a stack to simulate the function call stack.

## Exam Tips

1.  **Focus on Conversions:** Be thoroughly prepared to dry-run the infix-to-postfix conversion and postfix evaluation algorithms. These are common questions.
2.  **Understand the LIFO Principle:** For any application question, always explain _why_ the LIFO property is a good fit for the problem (e.g., the last function called is the first to return; the last action is the first to undo).
3.  **Draw Diagrams:** For questions on the call stack or DFS, a simple diagram showing the stack's state at various points can earn you full marks.
4.  **Compare and Contrast:** Be ready to explain the difference between infix, prefix, and postfix notations and why postfix is easier to evaluate.
5.  **Think in Code:** While implementations might not be asked directly, understanding how you would use a stack's `push` and `pop` operations to solve a problem (like backtracking) demonstrates deep knowledge.
