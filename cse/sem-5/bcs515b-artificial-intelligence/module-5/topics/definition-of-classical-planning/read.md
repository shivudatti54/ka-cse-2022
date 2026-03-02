# Definition of Classical Planning

## Introduction

Classical Planning is a fundamental subfield of Artificial Intelligence that deals with the problem of finding a sequence of actions to achieve a goal from an initial state. It forms the foundation of automated planning and reasoning systems. In classical planning, the world is assumed to be fully observable (the planner has complete knowledge of the world state), deterministic (actions have predictable outcomes), and static (no external events interfere with the plan). This simplified model allows us to focus on the core algorithmic challenges of planning without dealing with uncertainty or incomplete information.

The significance of classical planning in AI cannot be overstated. It serves as the building block for more complex planning paradigms like probabilistic planning, temporal planning, and hierarchical planning. Applications of classical planning range from robotics and autonomous navigation to automated assembly, logistics optimization, and even puzzle solving. Understanding the formal definition of classical planning, its components, and its representations is essential for any computer science engineer, as it provides insights into problem-solving mechanisms that are applicable across various domains of AI.

## Key Concepts

### Formal Definition of Classical Planning

A classical planning problem is formally defined as a tuple P = (Σ, s₀, G), where:

- **Σ** is the planning domain, consisting of a set of states, a set of actions, and a transition function
- **s₀** is the initial state, representing the starting configuration of the world
- **G** is the goal condition, specifying what needs to be achieved

The planner's task is to find a sequence of actions (a plan) that transforms the state from s₀ to a state sₙ that satisfies the goal condition G.

### Components of Classical Planning

**States**: A state is a complete description of the world at a particular point in time. In classical planning, states are typically represented as logical formulas or sets of ground atoms (facts that are true). For example, a state might be represented as {At(Robot, RoomA), Holding(Robot, Box), Clear(Box)}.

**Actions**: Actions describe what the planner can do to change the world. An action is defined by:

- **Preconditions**: The conditions that must be true before the action can be executed
- **Effects**: The changes that occur in the world after the action is executed

Actions are represented using a notation like Action(Name, Parameters, Preconditions, Effects). For example:

- Action(Move(robot, from, to),
  Precondition: At(robot, from),
  Effect: ¬At(robot, from) ∧ At(robot, to))

**Transition Function**: The transition function (or successor state function) defines how states change when actions are applied. It is a mapping from states and actions to states: δ: S × A → S. In deterministic classical planning, applying an action in a state leads to exactly one new state.

**Goal Condition**: The goal is a logical formula that specifies the desired state(s). A state s satisfies goal G if G is true in s. The planning problem is solved when a plan π is found such that applying π to s₀ results in a state sₙ where G holds.

### Planning Domains and Problems

The Planning Domain Definition Language (PDDL) is the standard language for representing classical planning problems. A PDDL description consists of:

- **Domain Definition**: Defines the predicates, types, and action schemas
- **Problem Definition**: Specifies the objects, initial state, and goal

### Solutions to Classical Planning

A solution (plan) to a classical planning problem is a sequence of actions [a₁, a₂, ..., aₙ] such that:

1. The first action a₁ is applicable in s₀ (its preconditions are satisfied)
2. Each subsequent action aᵢ is applicable in the state resulting from previous actions
3. The final state satisfies the goal condition G

Plans can be partial-order (where actions can be executed in different orders) or total-order (a strict sequence). The simplest form is a total-order sequence.

## Examples

### Example 1: The Blocks World Problem

Consider a robot that needs to stack blocks. We have three blocks (A, B, C) on a table.

**Domain:**

- Predicates: On(block, block), OnTable(block), Clear(block), Holding(block)
- Actions: Stack(block, block), Unstack(block, block), Pickup(block), Putdown(block)

**Initial State:**

- OnTable(A), OnTable(B), On(A, B), Clear(A), Clear(C), Empty

**Goal:**

- On(A, B) ∧ On(B, C)

**Solution:**

1. Unstack(A, B) - A is picked up from B
2. Putdown(A) - A is placed on table
3. Pickup(B) - B is picked up
4. Stack(B, C) - B is stacked on C
5. Pickup(A) - A is picked up
6. Stack(A, B) - A is stacked on B

### Example 2: Logistics Planning

A delivery robot needs to transport a package from location A to location B.

**Domain:**

- Predicates: At(obj, loc), In(obj, vehicle), Vehicle(vehicle), Location(loc)
- Actions: Load(obj, vehicle, loc), Unload(obj, vehicle, loc), Drive(vehicle, from, to)

**Initial State:**

- At(Package, A), At(Truck, A), Vehicle(Truck), Location(A), Location(B)

**Goal:**

- At(Package, B)

**Solution:**

1. Load(Package, Truck, A)
2. Drive(Truck, A, B)
3. Unload(Package, Truck, B)

### Example 3: Simple Navigation

A robot must navigate from room R1 to room R4.

**Initial State:**

- At(Robot, R1), Connected(R1, R2), Connected(R2, R3), Connected(R3, R4)

**Goal:**

- At(Robot, R4)

**Actions:**

- Action(Go(from, to), Precondition: At(Robot, from) ∧ Connected(from, to), Effect: At(Robot, to) ∧ ¬At(Robot, from))

**Solution:**

1. Go(R1, R2)
2. Go(R2, R3)
3. Go(R3, R4)

## Exam Tips

1. **Memorize the formal definition**: Remember that a classical planning problem is a tuple P = (Σ, s₀, G) with domain, initial state, and goal.

2. **Understand the assumptions**: Classical planning assumes full observability, determinism, and a static world - know these three assumptions clearly.

3. **Know action representation**: Be able to write actions with preconditions and effects in both formal notation and PDDL format.

4. **Distinguish between planning and execution**: Planning computes the sequence offline; execution applies actions in the world.

5. **Plan validity conditions**: A valid plan must have applicable actions at each step and achieve the goal.

6. **Understand state representation**: States are complete descriptions - know how to represent states as sets of ground atoms.

7. **Be familiar with PDDL**: The Planning Domain Definition Language is the standard representation - understand its basic structure.

8. **Complexity awareness**: Classical planning is PSPACE-complete in the general case - understand the implications of this complexity class.

9. **Goal regression**: This is an important technique for backward planning - understand how to compute what must be true before achieving a goal.

10. **State-space vs. plan-space planning**: Know the two main approaches to searching for plans and their differences.
