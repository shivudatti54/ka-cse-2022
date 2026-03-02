# Algorithms for Planning as State Space Search

## Introduction

Planning in artificial intelligence refers to the task of generating a sequence of actions that transforms an initial state into a desired goal state. Viewing planning as state space search provides a formal framework where problem-solving becomes a graph traversal problem. In this perspective, states represent world configurations, actions represent transitions between states, and the solution is a path from the initial state to a goal state.

The state space search approach to planning is fundamental to classical AI planning. It allows us to leverage well-established search algorithms to solve planning problems. This approach is particularly effective for planning domains where the environment is fully observable, deterministic, and static. Understanding these algorithms is crucial for CSE students as they form the foundation for more advanced planning techniques used in robotics, automated scheduling, and intelligent agent systems.

This topic explores both forward (progression) and backward (regression) state space search, examines various search strategies, and discusses heuristics that make planning efficient. We will also examine partial-order planning and planning graphs, which represent significant advancements in the field of AI planning.

## Key Concepts

### 1. Planning Problem Definition

A classical planning problem can be defined as a tuple (P, A, I, G) where:

- P is the set of propositions (state variables)
- A is the set of actions with preconditions and effects
- I is the initial state
- G is the goal state

Each state in the state space is a set of propositions that are true in that state. Actions are applicable only when their preconditions are satisfied, and applying an action produces a new state with the specified effects.

### 2. Forward State Space Search (Progression)

Forward state space search starts from the initial state and applies actions to progress toward the goal. The algorithm treats the planning problem as a graph search problem:

```
function FORWARD-SEARCH(problem):
 frontier = priority queue with initial state
 explored = empty set

 while frontier is not empty:
 state = pop from frontier with highest priority

 if state satisfies goal:
 return SOLUTION(state)

 add state to explored

 for each action applicable in state:
 next_state = RESULT(state, action)
 if next_state not in explored and not in frontier:
 add next_state to frontier

 return failure
```

The main advantage of forward search is its naturalness—we move from what we have toward what we want. However, it can be inefficient as it explores many states that are not relevant to the goal.

### 3. Backward State Space Search (Regression)

Backward search, also called regression, starts from the goal state and works backward to find the initial state. At each step, we find actions that would lead to the current state and compute their predecessors:

```
function BACKWARD-SEARCH(problem):
 frontier = queue with goal state
 explored = empty set

 while frontier is not empty:
 state = pop from frontier

 if state is subset of initial state:
 return SOLUTION(state)

 add state to explored

 for each action relevant to state:
 predecessor = REGRESS(action, state)
 if predecessor not in explored:
 add predecessor to frontier

 return failure
```

Backward search is often more efficient because it focuses on states that are relevant to achieving the goal. However, computing predecessors can be complex, especially with negative effects in actions.

### 4. Heuristics for Planning

Heuristics are essential for making state space search efficient. Several domain-independent heuristics have been developed:

**Delete List Relaxation**: Ignore negative effects of actions. The heuristic counts the number of unsatisfied goal propositions and estimates the cost as the maximum number of steps needed to achieve any goal proposition.

**Additive Heuristics**: Assume goals are independent and sum the costs of achieving each goal individually. This is admissible but may underestimate true cost.

**Max Heuristics**: Take the maximum cost among subgoals rather than the sum. This is also admissible.

**Set-Level Heuristics**: Treat the problem as achieving a set of propositions rather than a sequence, providing a more accurate estimate.

### 5. Partial-Order Planning

Partial-order planning (POP) represents a significant departure from total-order state space search. Instead of constructing a linear sequence of states, POP builds a partial order among actions:

- Start action has initial state as its effects
- Finish action has goal state as its preconditions
- Causal links ensure that action effects satisfy preconditions of other actions
- Temporal constraints specify ordering requirements

POP is more flexible than state-space search because it doesn't commit to a specific ordering until necessary. This makes it more efficient in many domains.

### 6. Planning Graphs

A planning graph is a directed graph that encodes constraints between propositions and actions over multiple levels. It consists of alternating proposition levels and action levels:

- **Proposition levels (S₀, S₁, S₂, ...)**: All propositions true at that level
- **Action levels (A₀, A₁, A₂, ...)**: All actions whose preconditions are satisfied at the previous proposition level

Planning graphs provide two key benefits:

1. **Mutex links**: Indicate incompatible propositions or actions that cannot co-occur
2. **Leveled ground truth**: Can be used to compute admissible heuristics

The Graphplan algorithm uses planning graphs to efficiently search for solutions.

## Examples

### Example 1: Simple Block World Planning

Consider a blocks world problem:

- Initial state: On(A, Table), On(B, Table), On(C, A), Clear(B), Clear(C)
- Goal: On(A, B), On(B, C)

**Forward Search Progression:**

1. Initial: {On(A,T), On(B,T), On(C,A), Clear(B), Clear(C)}
2. Apply Stack(C,A): Remove On(C,A), Add On(C,Table), Clear(A), Clear(C)
3. Apply Stack(B,A): Remove On(B,T), Add On(B,A), Clear(B)
4. Apply Stack(C,B): Remove On(C,T), Add On(C,B), Clear(C)

This shows how forward search systematically builds toward the goal state.

### Example 2: Computing Delete List Relaxation Heuristic

Given a planning problem with goal {G1, G2} and actions:

- Action A1: Precondition {P1}, Effect {G1, ¬P1}
- Action A2: Precondition {P2}, Effect {G2, ¬P2}

The delete list relaxation heuristic ignores negative effects, treating the problem as achieving positive goals independently. If achieving G1 costs 2 steps and G2 costs 3 steps, the heuristic returns max(2,3) = 3 (for max heuristic) or 2+3=5 (for additive heuristic).

### Example 3: Partial-Order Planning

Using POP for the blocks world:

1. Create Start (effects: initial state propositions) and Finish (preconditions: goal propositions)
2. Find open precondition: On(A,B) needs Stack(A,B) action
3. Stack(A,B) needs Clear(A) and Clear(B)—currently Clear(B) satisfied, Clear(A) needs Unstack(C,A)
4. Establish causal links and ordering constraints
5. Continue until all preconditions are satisfied

POP allows flexibility in the order of actions while ensuring constraints are met.

## Exam Tips

1. **Understand the difference between forward and backward search**: Forward search is goal-directed but may explore irrelevant states; backward search focuses on goal-relevant states but regression computation can be complex.

2. **Remember the planning problem tuple**: (P, A, I, G) is fundamental—know what each component represents.

3. **Heuristics are crucial for efficiency**: Delete list relaxation is the most common approach; understand how it works by ignoring negative effects.

4. **POP vs State-Space Search**: Partial-order planning doesn't commit to order early, making it more flexible but harder to implement than total-order approaches.

5. **Planning graphs provide leveled information**: Know that proposition and action levels alternate, and mutex links indicate incompatibility.

6. **Graphplan algorithm**: Understand how it uses planning graphs to efficiently extract solutions without exhaustive search.

7. **Admissible vs inadmissible heuristics**: Max and additive heuristics are admissible (never overestimate), making them useful for A\* search.

8. **Know when to apply each approach**: Forward search for simple problems; backward search when goal is specific and actions have simple preconditions; POP for problems with flexible ordering.
