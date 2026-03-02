# **Classical Planning Revision Notes**

### Definition of Classical Planning

- Classical planning is a problem-solving approach that focuses on finding an efficient sequence of actions to achieve a goal.
- It assumes that the environment is deterministic and that actions have no side effects.

### Algorithms for Planning as State-Space Search

- **Forward Chaining Algorithm**:
  - Works by starting with the goal state and applying reverse actions to reach the initial state.
  - Uses a forward-chaining search strategy.
- **Backward Chaining Algorithm** (also known as **Recursive Backtracking**):
  - Works by starting with the initial state and applying forward actions to reach the goal state.
  - Uses a backward-chaining search strategy.

### Planning Graphs

- A **planning graph** is a graph that represents the planning problem.
- The graph consists of:
  - **Nodes**: representing states, actions, and goals.
  - **Edges**: representing the relationships between nodes (e.g., "firing" an action).
- A planning graph can be constructed by:
  - Adding nodes for each state and goal.
  - Adding edges for each action and its preconditions.

### Important Formulas and Definitions

- **Plan**: a sequence of actions that transforms the initial state into the goal state.
- **Plan Space**: the set of all possible plans.
- **Plan Complexity**: the number of actions in a plan.
- **Plan Length**: the number of steps required to achieve the goal.

### Important Theorems

- **The Planning Space Theorem**: states that there is a finite planning space if there are only a finite number of states and actions.
- **The Planning Complexity Theorem**: states that there is a finite planning complexity if there are only a finite number of states and actions.

### Chapter Summaries

- **Chapter 9-9.4**: introduces the forward and backward chaining algorithms for planning.
- **Chapter 9.5**: discusses the planning graph data structure.
- **Chapter 10-10**: covers advanced topics in classical planning, including planning under uncertainty and planning in dynamic environments.

### Key Concepts to Remember

- Classical planning is a problem-solving approach that focuses on finding an efficient sequence of actions to achieve a goal.
- Forward and backward chaining algorithms are used for planning as state-space search.
- Planning graphs are used to represent the planning problem.
- Plan complexity and plan length are important metrics in planning.
