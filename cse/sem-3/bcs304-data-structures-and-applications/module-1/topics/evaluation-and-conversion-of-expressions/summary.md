# Evaluation and Conversion of Expressions

## Overview

Arithmetic expressions can be written in three different notations: infix, prefix, and postfix. Understanding how to convert between these notations and evaluate them using stacks is a fundamental topic in data structures. Computers prefer postfix notation as it is unambiguous and easy to evaluate using a stack.

## Key Points

- Infix notation is the standard mathematical notation used by humans, but it requires parentheses and precedence rules to avoid ambiguity.
- Prefix notation places the operator before its operands, while postfix notation places the operator after its operands.
- Postfix notation is preferred by computers as it is unambiguous and easy to evaluate using a stack.
- The infix-to-postfix conversion algorithm uses a stack to hold operators temporarily while scanning the infix expression from left to right.
- The postfix expression evaluation algorithm uses a stack of operands to evaluate the expression.

## Important Definitions

- **Infix notation**: a notation where the operator is placed between its operands.
- **Prefix notation**: a notation where the operator is placed before its operands.
- **Postfix notation**: a notation where the operator is placed after its operands.
- **Precedence**: the order in which operators are evaluated when there are multiple operators in an expression.

## Key Formulas / Syntax

- Infix-to-postfix conversion algorithm:
  1. Create an empty stack for operators and an empty output string.
  2. Scan the infix expression from left to right, one token at a time.
  3. For each token, apply the conversion rules.
- Postfix expression evaluation algorithm:
  1. Create an empty stack for operands.
  2. Scan the postfix expression from left to right, one token at a time.
  3. For each token, apply the evaluation rules.

## Comparisons

| Notation | Operator Position | Example (A + B) |
| -------- | ----------------- | --------------- |
| Infix    | Between operands  | A + B           |
| Prefix   | Before operands   | + A B           |
| Postfix  | After operands    | A B +           |

## Exam Tips

- Memorize the infix-to-postfix conversion algorithm and practice tracing it with at least 3-4 examples.
- Always show the complete trace table with columns: Token, Action, Stack, Output.
- When evaluating postfix, remember: first pop = right operand, second pop = left operand.
- Know the precedence table by heart: `^` > `* / %` > `+ -`.
- Practice these specific expressions as they frequently appear: `A + B * C - D`, `(A + B) * (C - D)`, and `A * (B + C) / D`.
