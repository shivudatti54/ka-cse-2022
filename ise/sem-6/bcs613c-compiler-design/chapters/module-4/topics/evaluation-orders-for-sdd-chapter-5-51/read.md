# **Evaluation Orders for SDD Chapter 5: 5.1**

## **Introduction**

In the context of LR parsing, evaluation orders refer to the sequence of actions taken to evaluate the SDD (Shift-Reduce-Decision) table. The SDD table is a crucial data structure used in LR parsing to determine the next action to take during the parsing process. In this section, we will delve into the concept of evaluation orders and their significance in LR parsing.

## **What is an SDD Table?**

An SDD table is a two-dimensional table used in LR parsing to store the possible next actions from a given state. The table has three columns:

- **Shift**: The action to take when a terminal symbol is shifted onto the stack.
- **Reduce**: The action to take when a non-terminal symbol is reduced to a terminal symbol.
- **Decision**: The action to take when a non-terminal symbol can be replaced by a non-terminal symbol.

## **Evaluation Orders**

An evaluation order is a sequence of actions taken to evaluate the SDD table. The evaluation order is determined by the following steps:

1.  **Start**: Begin with the initial state and the start symbol.
2.  **Shift**: If the current state has a shift action, shift the terminal symbol onto the stack.
3.  **Reduce**: If the current state has a reduce action, reduce the non-terminal symbol to a terminal symbol.
4.  **Decision**: If the current state has a decision action, decide which non-terminal symbol to replace.
5.  **Repeat**: Repeat steps 2-4 until the stack is empty or the parsing is complete.

## **Types of Evaluation Orders**

There are two types of evaluation orders:

- **Linear Evaluation Order**: This type of evaluation order is linear, meaning that each state is visited only once.
- **Non-Linear Evaluation Order**: This type of evaluation order is non-linear, meaning that some states may be visited multiple times.

## **Example**

Suppose we have a grammar with the following SDD table:

| State | Shift | Reduce | Decision |
| ----- | ----- | ------ | -------- |
| A     |       |        | A        |
| B     |       | B      | B        |
| C     |       |        | C        |

The initial state is A, and the start symbol is S. The evaluation order can be determined as follows:

1.  Start: A
2.  Shift: Shift the terminal symbol onto the stack (A → A 'a')
3.  Reduce: Reduce the non-terminal symbol A to a terminal symbol (A → a)
4.  Decision: Decide which non-terminal symbol to replace (B → B)
5.  Repeat: Repeat steps 2-4 until the stack is empty or the parsing is complete.

## **Code Example**

Here is a code example in Python that demonstrates the evaluation order for a simple grammar:

```python
class SDDTable:
    def __init__(self, states, terminals, non_terminals):
        self.states = states
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.table = [[None for _ in range(len(states))] for _ in range(len(states))]

    def set_shift(self, state, symbol):
        # Set the shift action
        self.table[state][symbol] = 'shift'

    def set_reduce(self, state, symbol):
        # Set the reduce action
        self.table[state][symbol] = 'reduce'

    def set_decision(self, state, symbol):
        # Set the decision action
        self.table[state][symbol] = 'decision'

    def evaluate(self, start_state, start_symbol):
        # Evaluate the SDD table
        stack = []
        current_state = start_state

        while True:
            # Shift
            if self.table[current_state][start_symbol] == 'shift':
                stack.append(start_symbol)
                current_state = 0
            # Reduce
            elif self.table[current_state][start_symbol] == 'reduce':
                # Find the reduce symbol
                reduce_symbol = None
                for state in self.table:
                    if state[0] == start_symbol and state[1] == 'reduce':
                        reduce_symbol = state[2]
                        break

                # Update the stack
                stack.append(reduce_symbol)
                current_state = reduce_symbol
            # Decision
            elif self.table[current_state][start_symbol] == 'decision':
                # Find the decision symbol
                decision_symbol = None
                for state in self.table:
                    if state[0] == current_state and state[1] == start_symbol:
                        decision_symbol = state[2]
                        break

                # Update the current state
                current_state = decision_symbol

            # Check for completion
            if not stack:
                break

        return stack

# Create the SDD table
states = ['A', 'B', 'C']
terminals = ['a', 'b']
non_terminals = ['S', 'A', 'B', 'C']

table = SDDTable(states, terminals, non_terminals)

# Set the actions
table.set_shift(0, 'a')
table.set_reduce(1, 'S')
table.set_decision(2, 'a')

# Evaluate the SDD table
start_state = 0
start_symbol = 'S'
result = table.evaluate(start_state, start_symbol)

print(result)  # [S, a]
```

This code example demonstrates how to create an SDD table, set the actions, and evaluate the table using a linear evaluation order.
