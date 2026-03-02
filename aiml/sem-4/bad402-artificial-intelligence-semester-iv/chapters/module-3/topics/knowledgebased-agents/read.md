# Introduction to Knowledge-Based Agents

Knowledge-based agents are a type of intelligent agent that uses knowledge to make decisions and take actions. These agents are designed to operate in environments where the current state is not completely observable, and the agent needs to reason about the current state based on its knowledge.

## Key Concepts

- **Knowledge**: The agent's understanding of the environment, including its current state and the rules that govern its behavior.
- **Reasoning**: The process of drawing conclusions from the agent's knowledge to make decisions.
- **Inference**: The process of deriving new knowledge from existing knowledge.

## Types of Knowledge-Based Agents

There are several types of knowledge-based agents, including:

- **Simple Reflex Agents**: These agents react to the current state of the environment without considering future consequences.
- **Model-Based Reflex Agents**: These agents maintain an internal model of the environment and use it to make decisions.
- **Goal-Based Agents**: These agents have specific goals and use their knowledge to achieve them.
- **Utility-Based Agents**: These agents make decisions based on a utility function that estimates the desirability of each action.

## Example: The Wumpus World

The Wumpus world is a classic example of a knowledge-based agent environment. The agent is placed in a grid world with a Wumpus (a monster) and gold. The agent's goal is to find the gold and avoid the Wumpus. The agent has a limited view of the environment and must use its knowledge to navigate and make decisions.

```
  +-------+-------+-------+
  |       |       |       |
  |  A  |  B  |  C  |
  |       |       |       |
  +-------+-------+-------+
  |       |       |       |
  |  D  |  E  |  F  |
  |       |       |       |
  +-------+-------+-------+
  |       |       |       |
  |  G  |  H  |  I  |
  |       |       |       |
  +-------+-------+-------+
```

## Heuristic Functions

Heuristic functions are used to estimate the distance from the current state to the goal state. These functions are used to guide the search and make decisions.

| Heuristic Function   | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| Manhattan Distance   | The sum of the horizontal and vertical distances between two points.         |
| Euclidean Distance   | The straight-line distance between two points.                               |
| Admissible Heuristic | A heuristic function that never overestimates the true distance to the goal. |

## Reasoning Patterns in Propositional Logic

Propositional logic is a branch of logic that deals with statements that can be either true or false. There are several reasoning patterns in propositional logic, including:

- **Modus Ponens**: If P implies Q, and P is true, then Q is true.
- **Modus Tollens**: If P implies Q, and Q is false, then P is false.

## Exam Tips

- Make sure to understand the different types of knowledge-based agents and their characteristics.
- Practice using heuristic functions to estimate distances and make decisions.
- Review the reasoning patterns in propositional logic and be able to apply them to solve problems.
