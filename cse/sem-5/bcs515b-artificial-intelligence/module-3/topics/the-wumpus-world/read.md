# The Wumpus World

## Introduction

The Wumpus World is a classic artificial intelligence problem that serves as an excellent illustration of logical reasoning in AI. It was introduced by Eugene Charniak and Christopher Riesbeck as a benchmark problem for testing AI agents that can reason under uncertainty. The Wumpus World provides a simple yet challenging environment where an agent must navigate through a cave to find gold while avoiding deadly pits and a terrifying creature called the Wumpus.

This problem is particularly significant in the context of 's AI syllabus because it demonstrates how an intelligent agent can use propositional logic to make decisions based on sensory information. The Wumpus World is a fully observable environment from the agent's perspective when it visits a square, but the agent must reason about unobserved squares using logical inference. This makes it an ideal case study for understanding knowledge representation, inference mechanisms, and the design of logic-based agents.

The importance of studying the Wumpus World extends beyond just understanding this particular problem. It serves as a foundation for understanding more complex real-world applications such as autonomous navigation, robotics, and decision-making systems where an agent must work with partial information and make reasoned decisions.

## Key Concepts

### Environment Description

The Wumpus World is a 4×4 grid of rooms (cells) connected by passages. The agent starts in the bottom-left corner (1,1) facing right. The environment contains:

- Exactly one Wumpus (a monster that kills the agent if it enters its room)
- Zero or more pits (holes that cause the agent to fall and die)
- Exactly one piece of gold (the agent's goal)
- The agent can climb out of the cave from the starting position

### Percepts

The agent receives percepts indicating the current state of its environment:

- **Stench**: Smelly if Wumpus is in an adjacent room (not diagonal)
- **Breeze**: Present if a pit is in an adjacent room
- **Glitter**: Present if gold is in the same room
- **Bump**: Received when the agent tries to move into a wall
- **Scream**: Heard if the Wumpus is killed

### Actions

The agent can perform the following actions:

- **Move Forward**: Move to the adjacent room in the direction faced
- **Turn Left**: Rotate 90° counter-clockwise
- **Turn Right**: Rotate 90° clockwise
- **Shoot**: Shoot an arrow in the direction faced (kills Wumpus if hit)
- **Grab**: Pick up gold if in the same room
- **Climb**: Climb out of the cave (only from start location)

### Performance Measure

The agent receives:

- +1000 points for grabbing the gold and climbing out
- -1000 points for falling into a pit or being eaten by Wumpus
- -1 point for each action taken
- -10 points for using an arrow

### Logical Rules

The Wumpus World can be represented using propositional logic with the following symbols:

- P(i,j): Pit in room [i,j]
- W(i,j): Wumpus in room [i,j]
- B(i,j): Breeze in room [i,j]
- S(i,j): Stench in room [i,j]
- G(i,j): Gold in room [i,j]
- OK(i,j): Room [i,j] is safe (no pit, no Wumpus)

Key logical implications:

- B(i,j) ⇒ ∃ adjacent (P)
- S(i,j) ⇒ ∃ adjacent (W)
- OK(i,j) ⇒ ¬P(i,j) ∧ ¬W(i,j)

### Reasoning Process

The agent uses backward chaining and forward chaining to deduce information:

1. From percepts, infer the state of adjacent rooms
2. Build a mental map of safe and dangerous rooms
3. Use logical rules to eliminate possibilities
4. Plan a sequence of actions to reach the goal

## Examples

### Example 1: Initial Reasoning

**Scenario**: Agent starts at [1,1]. Initial percepts show no breeze and no stench.

**Solution**:

- Since there is no breeze at [1,1], there are no pits adjacent to [1,1]
- Since there is no stench at [1,1], there is no Wumpus adjacent to [1,1]
- Therefore, rooms [1,2] and [2,1] are safe (OK squares)
- Agent can safely move to either [1,2] or [2,1]

**Step-by-step**:

1. From initial percept: ¬B(1,1) and ¬S(1,1)
2. Using logical rules: ¬B(1,1) ⇒ ¬P(1,2) ∧ ¬P(2,1)
3. Similarly: ¬S(1,1) ⇒ ¬W(1,2) ∧ ¬W(2,1)
4. Conclusion: OK(1,2) and OK(2,1)

### Example 2: Handling Stench

**Scenario**: Agent moves to [1,2] and detects a stench but no breeze.

**Solution**:

- Stench at [1,2] implies Wumpus is in an adjacent room
- Adjacent rooms are [1,1], [1,3], and [2,2]
- [1,1] is safe (we know no Wumpus there)
- Wumpus must be in either [1,3] or [2,2]
- No breeze means no pits in adjacent rooms

**Step-by-step**:

1. S(1,3) detected ⇒ W(1,3) ∨ W(2,2)
2. ¬W(1,1) known from initial state
3. Cannot determine exact Wumpus location yet
4. Mark [1,3] and [2,2] as potentially dangerous

### Example 3: Safe Navigation

**Scenario**: Agent is at [2,1], detects breeze. What can be inferred?

**Solution**:

- Breeze at [2,1] implies a pit is in an adjacent room
- Adjacent rooms are [1,1], [2,2], and [3,1]
- [1,1] is known to be safe (no pit)
- Pit must be in [2,2] or [3,1]
- Agent should avoid these rooms

**Step-by-step**:

1. B(2,1) ⇒ P(1,1) ∨ P(2,2) ∨ P(3,1)
2. ¬P(1,1) known
3. Therefore: P(2,2) ∨ P(3,1)
4. Mark both rooms as potentially dangerous

## Exam Tips

1. **Remember the percept list**: Stench, Breeze, Glitter, Bump, Scream - this is frequently asked in exams.

2. **Know the logical implications**: Breeze implies adjacent pit, Stench implies adjacent Wumpus.

3. **Understand agent initialization**: Agent starts at [1,1] facing right, has arrow, no gold.

4. **Performance score is crucial**: Remember +1000 for gold out, -1000 for death, -1 per action.

5. **Safe squares**: Room is safe if ¬P ∧ ¬W (no pit and no Wumpus).

6. **Adjacency is orthogonal only**: Diagonal rooms are NOT considered adjacent for percepts.

7. **Arrow usage**: Arrow can only be fired in the direction the agent is facing.

8. **Climb action**: Only works from the starting position [1,1].

9. **Wumpus can be killed**: Shooting the arrow kills Wumpus and produces a scream.

10. **State representation**: Know how to represent knowledge using propositional logic symbols P(i,j), W(i,j), B(i,j), S(i,j).
