# Introduction to the Wumpus World

The Wumpus World is a classic problem in the field of Artificial Intelligence (AI), introduced by Stuart Russell and Peter Norvig. It is a simple yet challenging environment that has been used to illustrate various concepts in AI, including knowledge-based agents, logical reasoning, and planning.

## The Wumpus World Environment

The Wumpus World is a 4x4 grid, where an agent (usually called the "hunter") is placed in one of the cells. The environment is partially observable, meaning that the agent can only perceive its immediate surroundings. The grid contains the following elements:

- **Wumpus**: a monster that can kill the agent if it is in the same cell.
- **Pit**: a hazard that can kill the agent if it falls into it.
- **Gold**: a treasure that the agent must collect to win the game.
- **Stench**: a smell that indicates the presence of the Wumpus in a nearby cell.
- **Breeze**: a wind that indicates the presence of a Pit in a nearby cell.

## The Hunter's Goal

The hunter's goal is to collect the gold and return to the starting cell without being killed by the Wumpus or falling into a Pit. The hunter can move in one of four directions (up, down, left, or right) and can also shoot an arrow to kill the Wumpus.

## Knowledge-Based Agents

A knowledge-based agent is an agent that uses knowledge to make decisions. In the Wumpus World, the agent uses its knowledge of the environment to navigate and avoid hazards. The agent's knowledge is represented using logical statements, such as:

- **Wumpus(x, y)**: the Wumpus is in cell (x, y).
- **Pit(x, y)**: there is a Pit in cell (x, y).
- **Gold(x, y)**: there is gold in cell (x, y).
- **Stench(x, y)**: there is a stench in cell (x, y).
- **Breeze(x, y)**: there is a breeze in cell (x, y).

## Inference and Reasoning

The agent uses logical inference and reasoning to update its knowledge and make decisions. For example, if the agent perceives a stench in a cell, it can infer that the Wumpus is in a nearby cell. If the agent perceives a breeze in a cell, it can infer that there is a Pit in a nearby cell.

## Heuristic Functions

Heuristic functions are used to guide the agent's search for a solution. In the Wumpus World, a heuristic function can be used to estimate the distance from the agent's current cell to the gold. The agent can use this heuristic function to choose the next cell to move to.

## Example Walkthrough

Here is an example walkthrough of the Wumpus World:

```
 1 | 2 | 3 | 4
  ---------
5 | H | 7 | 8
  ---------
9 | 10 | 11 | 12
  ---------
13 | 14 | 15 | 16
```

The hunter is in cell 6. The agent perceives a stench in cell 6, which means that the Wumpus is in a nearby cell. The agent can infer that the Wumpus is in cell 5 or cell 7. The agent moves to cell 7 and perceives a breeze, which means that there is a Pit in a nearby cell. The agent can infer that there is a Pit in cell 8 or cell 10.

## Comparison of Informed Search Strategies

The following table compares different informed search strategies that can be used in the Wumpus World:

| Strategy      | Description                                                                          | Advantages                              | Disadvantages                             |
| ------------- | ------------------------------------------------------------------------------------ | --------------------------------------- | ----------------------------------------- |
| Greedy Search | Choose the next cell based on a heuristic function                                   | Fast and efficient                      | May get stuck in local optima             |
| A\* Search    | Choose the next cell based on a heuristic function and the cost of reaching the cell | Guaranteed to find the optimal solution | Can be slow and computationally expensive |
| Hill Climbing | Choose the next cell based on a heuristic function and the current cell's neighbors  | Fast and efficient                      | May get stuck in local optima             |

## Exam Tips

To prepare for an exam on the Wumpus World, make sure to:

- Understand the environment and the hunter's goal
- Know how to represent the environment using logical statements
- Understand how to use inference and reasoning to update the agent's knowledge
- Be familiar with different informed search strategies and their advantages and disadvantages
- Practice solving example problems and walkthroughs
