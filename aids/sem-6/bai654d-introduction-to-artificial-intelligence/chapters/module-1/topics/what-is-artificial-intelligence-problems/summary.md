# What is Artificial Intelligence? Problems - Summary

## Key Definitions and Concepts

- **Artificial Intelligence**: The simulation of human intelligence processes by machines, encompassing learning, reasoning, problem-solving, perception, and language understanding.

- **Well-defined Problems**: Problems with clearly specified initial states, goal states, operators, and path costs—solvable through formal algorithms.

- **Ill-defined Problems**: Problems lacking complete formal specifications, requiring additional context, common sense reasoning, or learning approaches.

- **Problem Space**: The complete set of all possible states reachable from the initial state through any sequence of legal operator applications.

- **State Space**: A formal graph representation of the problem space where nodes represent states and edges represent operator transitions.

## Important Formulas and Theorems

- **Problem Formulation Model**: Any AI problem requires defining (Initial State, Goal State, Operators, Path Cost)

- **State Space Size**: For problems with branching factor b and depth d, maximum states = b^d (though many states may be unreachable)

## Key Points

1. AI can be viewed from two perspectives: systems that think like humans and systems that act intelligently.

2. The four components of problem formulation are fundamental to representing any AI problem systematically.

3. Well-defined problems permit algorithmic solution; ill-defined problems require heuristic or learning-based approaches.

4. Problem space represents the conceptual landscape; state space provides its mathematical formalization.

5. Toy problems serve educational purposes; real-world problems drive practical applications.

6. Operator definition must include preconditions (when applicable) and costs (for optimal solutions).

7. The goal test determines whether a state is a goal state—it may check for exact match or goal condition satisfaction.

8. Understanding problem structure is essential for selecting appropriate search strategies.

## Common Mistakes to Avoid

1. Confusing problem space with state space—they are related but distinct concepts.

2. Forgetting that operators may have preconditions limiting their applicability.

3. Overlooking path cost when problems ask for optimal solutions.

4. Assuming all AI problems are well-defined—many real-world problems are ill-defined.

5. Defining goal states only as single configurations when goal conditions are often more general.

## Revision Tips

1. Practice formulating various word problems using the four-component model until it becomes automatic.

2. Draw state space diagrams for simple problems like 8-puzzle or water jug to visualize search concepts.

3. Create comparison tables distinguishing well-defined from ill-defined problems with concrete examples.

4. Review how problem formulation directly influences search algorithm selection in subsequent topics.

5. Solve multiple toy problems manually to build intuition about state transitions and path costs.