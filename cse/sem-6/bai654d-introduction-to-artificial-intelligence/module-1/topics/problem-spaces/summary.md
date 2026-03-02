# Problems and Problem Spaces

## Overview

Problem spaces (state spaces) form the foundational framework for AI problem-solving by representing all possible states reachable from an initial state through legal actions. Understanding problem space characteristics helps select appropriate search strategies and evaluate solution complexity.

## Key Points

- **Initial State**: The starting configuration before any actions are taken
- **Goal State**: The desired outcome that signifies problem completion
- **Actions/Operators**: Legal moves that transform one state into another state
- **Path Cost**: Function assigning costs to sequences of actions, enabling optimal solution finding
- **State Space Graph**: Nodes represent states, edges represent state transitions through actions
- **Branching Factor**: Average number of successor states generated from any state, impacts search complexity
- **Problem Formulation**: Systematic process of defining initial state, goal, actions, and costs for computational solving

## Important Concepts

- Problem spaces can be represented as graphs or trees depending on whether states can be revisited
- Well-defined problems have clear components (8-puzzle) versus ill-defined problems with ambiguous elements
- Water Jug problem illustrates state space representation with actions like fill, empty, and pour
- Different problem types require different search strategies based on space characteristics

## Notes

- Always identify all four components when analyzing a problem scenario
- Draw state space diagrams for visualization even when not explicitly required
- Practice classic problems like 8-puzzle and missionaries-cannibals for formulation skills
- Consider constraints that reduce the problem space and affect solution strategies
- Distinguish between finding any solution versus finding the optimal solution
