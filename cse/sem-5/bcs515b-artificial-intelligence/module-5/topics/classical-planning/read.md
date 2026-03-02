# Classical Planning

## Introduction

Classical Planning is a fundamental area in Artificial Intelligence that deals with the problem of generating a sequence of actions to achieve a specific goal from an initial state. It forms the backbone of many automated planning systems used in robotics, game playing, automated tutoring systems, and logistics optimization. The classical planning paradigm assumes a fully observable, deterministic, and static environment with explicit representations of states and actions.

In the context of 's AI curriculum, classical planning represents a significant shift from problem-solving techniques like search algorithms to a more structured approach where the planner explicitly reasons about actions and their effects on the world. Unlike incremental problem solvers, classical planning systems maintain a declarative representation of states, goals, and actions, making them more modular and easier to modify. The planning domain definition language (PDDL) emerged as a standard formalism for describing planning problems, enabling researchers to compare different planning algorithms on common benchmarks.

The importance of classical planning in modern AI cannot be overstated. It provides the theoretical foundation for understanding more complex planning paradigms including probabilistic planning, temporal planning, and hierarchical planning. Understanding classical planning helps students grasp essential concepts like state representation, action schemas, goal testing, and plan execution that are crucial for advanced AI applications.

## Key Concepts

### 1. Planning Problem Definition

A classical planning problem can be formally defined as a tuple (S, A, I, G, γ) where:

- S represents the finite set of all possible states
- A represents the set of all possible actions
- I ∈ S is the initial state
- G ⊆ S represents the goal state or condition
- γ: S × A → S is the transition function (deterministic)

The planner must find a sequence of actions (a₁, a₂, ..., an) such that applying these actions from the initial state I leads to a state s that satisfies the goal condition G.

### 2. STRIPS Planning

STRIPS (Stanford Research Institute Problem Solver) was one of the earliest and most influential planning formalisms. It represents actions using three components:

- **Preconditions**: A set of conditions that must be true before the action can be executed
- **Add List (Effects)**: A set of conditions that become true after executing the action
- **Delete List**: A set of conditions that become false after executing the action

For example, the action "Pickup(X)" in a blocks world might have:

- Preconditions: HandEmpty ∧ Clear(X)
- Add List: Holding(X)
- Delete List: HandEmpty, Clear(X)

### 3. Planning as State-Space Search

Classical planning can be viewed as a search problem in two ways:

**Forward State-Space Search (Progression)**: Start from the initial state and apply actions to generate successor states until reaching a goal state. This approach is complete but can be inefficient for large state spaces.

**Backward State-Space Search (Regression)**: Start from the goal state and work backwards to find actions that could lead to the initial state. This is often more efficient because the branching factor is typically smaller near the goal.

### 4. Partial-Order Planning (POP)

Partial-order planning represents a significant advancement where the planner does not commit to a total ordering of actions unnecessarily. Instead, it maintains a set of actions with ordering constraints and resolves open preconditions through a process called "plan refinement."

The key components of POP include:

- **Start action**: Has no preconditions and initial state conditions as effects
- **Finish action**: Has goal conditions as preconditions and no effects
- **Open precondition**: A precondition of some action not yet achieved by any other action's effects
- **Flaw selection**: Choosing which open precondition to address next
- **Resolvers**: Actions that can potentially satisfy the selected open precondition

### 5. Planning Graph and Graphplan

Planning graphs provide an efficient data structure for solving planning problems. A planning graph consists of alternating layers of propositions (literals) and actions:

- **Proposition layers**: Contain literals that could be true at that level
- **Action layers**: Contain actions whose preconditions are satisfied in the previous proposition layer

The key advantage of planning graphs is that they provide polynomial-time reachability heuristics and can detect when no solution exists.

### 6. Heuristics in Planning

Various heuristics have been developed to improve planning efficiency:

- **Delete-list relaxation**: Ignore delete effects when calculating heuristic values, making the relaxed problem easier to solve
- **Subgoal independence**: Assume subgoals are independent and sum their individual costs
- **Pattern database**: Precompute heuristic values for patterns extracted from the problem

### 7. Planning Domain Definition Language (PDDL)

PDDL has become the standard language for describing planning problems. It separates the domain definition (actions and their effects) from the specific problem instance (objects, initial state, and goal):

```
Domain: Blocks-World
Predicates: (?x - block)
 (on-table ?x)
 (holding ?x)
 (clear ?x)

Action: STACK
 Parameters: ?x ?y - block
 Precondition: (holding ?x) ∧ (clear ?y)
 Effect: (handempty) ∧ (on ?x ?y) ∧ (clear ?x) ∧ (not (holding ?x)) ∧ (not (clear ?y))
```

## Examples

### Example 1: Blocks World Planning Problem

**Problem**: We have three blocks (A, B, C) on a table. Initially: A on B, B on table, C on table. Goal: A on table, B on C, C on table.

**Initial State**: {On(A,B), OnTable(B), OnTable(C), Clear(A), Clear(C), HandEmpty}
**Goal State**: {OnTable(A), On(B,C), OnTable(C), Clear(A), Clear(B)}

**Solution using STRIPS-style actions**:

1. **UNSTACK(A, B)**:

- Preconditions: {On(A,B), Clear(A), HandEmpty}
- Add: {Holding(A), Clear(B)}
- Delete: {On(A,B), HandEmpty}

2. **PUTDOWN(A)**:

- Preconditions: {Holding(A)}
- Add: {OnTable(A), Clear(A), HandEmpty}
- Delete: {Holding(A)}

3. **UNSTACK(B, table)** is not needed as B is already on table.

4. **STACK(B, C)**:

- Preconditions: {Holding(B), Clear(C)}
- Add: {On(B,C), Clear(B), HandEmpty}
- Delete: {Holding(B), Clear(C)}

**Final Plan**: [UNSTACK(A,B), PUTDOWN(A), STACK(B,C)]

### Example 2: Forward State-Space Search

Consider a simple planning problem with two variables:

- Initial state: {¬a, ¬b}
- Goal state: {a, b}
- Actions available:
- Action1: Preconditions: {}, Effects: {a}
- Action2: Preconditions: {a}, Effects: {b}

**Search Process**:

- Start: {¬a, ¬b} - Not goal
- Apply Action1: {a, ¬b} - Not goal
- Apply Action2: {a, b} - Goal achieved!

**Plan**: [Action1, Action2]

### Example 3: Partial-Order Planning

**Problem**: Goal is to have both A on table and B on table from initial state where A is on B.

**Initial State**: {On(A,B), OnTable(B), Clear(A), HandEmpty}
**Goal**: {OnTable(A), OnTable(B)}

**POP Steps**:

1. Start with Start and Finish actions
2. Finish has preconditions: OnTable(A) ∧ OnTable(B)
3. Open precondition: OnTable(A)

- Add UNSTACK(A,B) which provides OnTable(A) as effect

4. UNSTACK requires HandEmpty (already have) and Clear(A) (already have)
5. Open precondition: OnTable(B) is already satisfied in initial state
6. Final Plan: UNSTACK(A,B) with no ordering constraints on Start

## Exam Tips

1. **Know the formal definition**: Remember that a planning problem is a tuple (S, A, I, G, γ) and be able to explain each component clearly in exams.

2. **STRIPS representation**: Practice writing STRIPS-style action representations with preconditions, add list, and delete list for simple problems.

3. **Forward vs Backward search**: Understand when each approach is more efficient—forward search works well when branching factor is small near start, backward when goal is simpler than initial state.

4. **POP advantages**: Remember that partial-order planning is more flexible than total-order planning and can find solutions with fewer steps by not imposing unnecessary ordering.

5. **Planning graph structure**: Know that planning graphs contain alternating proposition and action layers, and they provide polynomial-time heuristic estimates.

6. **PDDL understanding**: Be familiar with the basic structure of PDDL domain and problem definitions, including predicates, actions, and parameters.

7. **Heuristic functions**: Understand delete-list relaxation heuristic and why it's admissible (never overestimates actual cost).

8. **Goal regression**: Be able to perform backward chaining—given a goal and an action, determine what must be true before the action for the goal to hold afterward.
