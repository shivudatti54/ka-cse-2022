# Planning Graphs

## Introduction

Planning is a fundamental area in Artificial Intelligence that deals with the problem of finding a sequence of actions that achieves a given goal from an initial state. Traditional planning approaches like state-space search and partial-order planning face significant challenges when dealing with complex problems involving many variables and interactions. Planning graphs were introduced as a powerful intermediate representation that provides a more efficient approach to solving planning problems by incrementally building a leveled graph that captures the progression of states and actions.

The Planning Graph approach, most notably implemented in the GraphPlan algorithm, offers a different paradigm from conventional planning search methods. Instead of searching through the entire state space, GraphPlan builds a directed bipartite graph alternating between proposition levels (representing states) and action levels (representing possible actions). This structure allows for efficient reasoning about mutex (mutually exclusive) relationships between propositions and actions, enabling pruning of the search space and faster solution extraction.

Planning graphs are particularly important in modern AI because they address the representational and computational challenges of classical planning. They provide a compact representation of the planning problem that can be analyzed to determine whether a solution exists and to extract such a solution efficiently. This approach has influenced many subsequent planning algorithms and remains a fundamental concept in AI education, including the syllabus for Artificial Intelligence.

## Key Concepts

### Structure of a Planning Graph

A planning graph consists of alternating levels of propositions (literals) and actions. The graph begins with an initial proposition level (P0) containing the initial state literals, followed by an action level (A1) containing all ground actions whose preconditions are satisfied in the previous proposition level, then another proposition level (P1) containing all propositions that could be true after executing actions from the previous level, and so on.

Each proposition level contains literals that could potentially be true at that point in the plan, along with mutex links indicating which pairs of propositions cannot be true simultaneously. Similarly, each action level contains actions that could be executed, along with mutex links indicating which pairs of actions cannot be executed together. The mutex relationships are crucial for pruning the search space effectively.

### Mutex Links

Mutex (mutual exclusion) links are used to denote incompatibility between propositions or actions. Two propositions are mutually exclusive (mutex) at a given level if they cannot both hold simultaneously in any valid state. This typically occurs when one proposition is the negation of another, or when they are produced by mutually exclusive actions.

Two actions are mutex at a given level if they cannot be executed together in any valid plan reaching that level. Actions can be mutex due to several reasons: conflicting effects (one deletes what the other adds), interference (one deletes a precondition of the other), or competing needs (their preconditions are mutex at the previous proposition level).

### GraphPlan Algorithm

The GraphPlan algorithm works in two main phases. In the first phase, called expansion, the planning graph is built level by level. Starting from the initial state, the algorithm adds an action level containing all applicable actions (those whose preconditions are satisfied in the current proposition level), then adds the next proposition level containing all effects of those actions. This process continues until either the goal appears in a proposition level without mutex relations, or the graph stabilizes (no new propositions can be added).

In the second phase, called extraction, the algorithm searches backward from the goal level to find a valid plan. If the goal appears in a proposition level without mutex constraints, the algorithm attempts to select actions from the previous action level that achieve the goal and do not have mutex relationships. This backward search continues until reaching the initial state.

### Solution Extraction

Extracting a solution from the planning graph involves a backtracking search that works backward from the goal. At each level, the algorithm selects a set of actions that achieve the current subgoals without having mutex relationships with each other. The selected actions must also not have mutex relationships with the actions already chosen for subsequent levels in the plan.

If the backward search fails at a particular level, GraphPlan backtracks and tries alternative action selections. If no valid plan can be found at a given level, the algorithm may expand the planning graph further to the next level and try again. This iterative approach continues until either a valid plan is found or the algorithm determines that no solution exists.

### Time Complexity and Performance

The time complexity of GraphPlan depends on the number of propositions, actions, and the length of the solution plan. The space complexity is polynomial in the size of the planning graph. GraphPlan performs well on problems with finite solution lengths and reasonable numbers of propositions and actions, making it suitable for many classical planning problems.

## Examples

### Example 1: Simple Block World Problem

Consider a simple planning problem with three blocks (A, B, C) on a table. Initially, A is on B, B is on C, and C is on the table. The goal is to have A on B and B on C (stacked as A-B-C).

Initial state: {On(A,B), On(B,C), On(C,Table), Clear(A), Clear(Table)}
Goal: {On(A,B), On(B,C)}

Actions available:

- UNSTACK(x,y): Preconditions: On(x,y), Clear(x) | Effects: On(x,Table), Clear(y), Holding(x)
- STACK(x,y): Preconditions: Holding(x), Clear(y) | Effects: On(x,y), Clear(x), Not(Holding(x))
- PICKUP(x): Preconditions: On(x,Table), Clear(x) | Effects: Holding(x), Not(On(x,Table)), Not(Clear(x))
- PUTDOWN(x): Preconditions: Holding(x) | Effects: On(x,Table), Clear(x), Not(Holding(x))

Building the planning graph:

- P0: Initial propositions
- A1: Actions applicable (PICKUP(A), PICKUP(B), PICKUP(C), PUTDOWN(A), PUTDOWN(B), PUTDOWN(C))
- P1: Propositions after A1
- Continue until goal propositions appear without mutex

The solution plan would involve: UNSTACK(A,B), PUTDOWN(A), UNSTACK(B,C), STACK(B,C), PICKUP(A), STACK(A,B)

### Example 2: Two-Robot Delivery Problem

Consider a domain where two robots must deliver objects. Initial state: Robot1 at location A with object X, Robot2 at location B, goal is object X at location C.

Actions:

- move(r, from, to): robot moves between locations
- pick(r, obj, loc): robot picks up object
- drop(r, obj, loc): robot drops object

At each level, the planning graph captures which robots can perform which actions based on their locations and what they are holding. Mutex links would prevent both robots from holding the same object or being at the same location if that's a constraint.

## Exam Tips

1. **Understand the bipartite structure**: Remember that planning graphs alternate between proposition levels and action levels, starting and ending with propositions.

2. **Know mutex conditions**: Be able to identify when propositions or actions are mutually exclusive—negations, conflicting effects, interference, and competing preconditions.

3. **GraphPlan algorithm steps**: Remember the two-phase approach of expansion (building the graph) and extraction (searching backward for solutions).

4. **Termination conditions**: Know when GraphPlan terminates—either goal achieved or graph stabilizes (no new propositions added).

5. **Solution extraction process**: Understand the backward search mechanism and how it selects non-mutex actions to achieve subgoals.

6. **Advantages over state-space search**: Planning graphs provide more efficient pruning through mutex relationships and avoid redundant computation.

7. **Limitations**: GraphPlan cannot handle partial observability, uncertain outcomes, or continuous time—these are important limitations to remember for exam questions comparing planning approaches.

8. **Relationship with other planners**: Be prepared to compare planning graphs with state-space planning, partial-order planning, and heuristic-based planners.
