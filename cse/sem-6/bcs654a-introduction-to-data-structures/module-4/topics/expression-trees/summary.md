# Expression Trees

## Overview

An expression tree represents arithmetic expressions where leaf nodes are operands and internal nodes are operators. Different traversal methods produce different expression notations: inorder gives infix, preorder gives prefix, postorder gives postfix.

## Key Points

- **Leaf Nodes**: Contain operands (numbers or variables)
- **Internal Nodes**: Contain operators (+, -, \*, /, etc.)
- **Inorder Traversal**: Produces infix notation (a + b) requiring parentheses
- **Preorder Traversal**: Produces prefix notation (+ a b) operator before operands
- **Postorder Traversal**: Produces postfix notation (a b +) operands before operator
- **Construction**: Build from postfix/prefix expression using stack
- **Evaluation**: Postorder traversal computes expression value recursively

## Important Concepts

- Expression trees naturally represent operator precedence through structure
- Postfix expression converted to tree by pushing operands, popping for operators
- Evaluation uses postorder: evaluate children, apply operator to results
- Infix notation requires parentheses for correct precedence
- Prefix and postfix notations are unambiguous without parentheses
- Operator as parent with operands as children models computation

## Notes

- Practice converting between expression formats using trees
- Understand how tree structure represents precedence and associativity
- Know algorithm for building tree from postfix expression
- Be able to evaluate expression tree using postorder traversal
- Remember traversal type determines expression notation produced
