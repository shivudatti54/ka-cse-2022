# The Wumpus World - Summary

## Key Definitions and Concepts

- **Wumpus World**: A 4×4 grid-based AI problem where an agent navigates to find gold while avoiding pits and a Wumpus monster.
- **Percept**: Sensory information received by the agent - Stench (adjacent Wumpus), Breeze (adjacent pit), Glitter (gold in room), Bump (wall hit), Scream (Wumpus killed).
- **Action**: Operations the agent can perform - Move, Turn Left, Turn Right, Shoot, Grab, Climb.
- **Safe Room (OK)**: A room confirmed to have neither pit nor Wumpus.
- **Propositional Logic Representation**: Using symbols like P(i,j) for pit, W(i,j) for Wumpus, B(i,j) for breeze, S(i,j) for stench.

## Important Formulas and Theorems

- **Breeze Rule**: B(i,j) ⇒ ∃ adjacent P (breeze implies adjacent pit)
- **Stench Rule**: S(i,j) ⇒ ∃ adjacent W (stench implies adjacent Wumpus)
- **Safe Room**: OK(i,j) ⇔ ¬P(i,j) ∧ ¬W(i,j)
- **No Percept Safe Rule**: ¬B(i,j) ∧ ¬S(i,j) ⇒ adjacent rooms are safe
- **Performance Score**: +1000 (gold out), -1000 (death), -1 per action, -10 (arrow used)

## Key Points

- Agent starts at [1,1] facing right with one arrow
- Adjacency is orthogonal (up, down, left, right) - NOT diagonal
- Pits and Wumpus can be in any location except [1,1]
- Logical inference builds knowledge incrementally
- Agent must reason about unvisited rooms using percept information
- Goal is to get gold and climb out with maximum score

## Common Mistakes to Avoid

- Confusing diagonal rooms as adjacent (common error in exams)
- Forgetting that [1,1] is guaranteed safe (no pit, no Wumpus)
- Not remembering that arrow can only be fired in the facing direction
- Assuming pits/Wumpus can be in the starting room
- Confusing stench with Wumpus presence (stench means adjacent, not in same room)

## Revision Tips

1. Memorize the percept-action table: Stench→Wumpus nearby, Breeze→Pit nearby, Glitter→Gold here, Bump→Wall, Scream→Wumpus dead.

2. Practice drawing the 4×4 grid and marking safe/dangerous rooms based on sample percept sequences.

3. Solve at least 3-4 reasoning problems similar to Examples 1, 2, and 3 in the main content.

4. Remember: No percept at a location means all adjacent squares are safe.
