# Knowledge-Based Agents - Summary

## Key Definitions and Concepts

- **Knowledge-Based Agent**: An AI agent that uses a knowledge base of facts and logical inference to decide actions rather than simple condition-action rules.
- **Knowledge Base (KB)**: A collection of sentences in a knowledge representation language expressing facts about the world.
- **Inference Engine**: Component that derives new facts from the KB using logical inference rules.
- **Wumpus World**: A classic AI benchmark problem - a 4×4 grid with Wumpus, pits, gold, where the agent must navigate safely.
- **Entailment (KB ⊨ α)**: Semantic relationship where α is necessarily true whenever KB is true.
- **Inference (KB ⊢ α)**: Syntactic process of deriving α from KB using inference rules.
- **Horn Clause**: A clause with at most one positive literal, enabling efficient forward chaining.

## Important Formulas and Theorems

- **Modus Ponens**: From P ⇒ Q and P, infer Q
- **Universal Instantiation**: From ∀x P(x), infer P(c) for any constant c
- **Wumpus Percept Rules**:
  - Breeze at (i,j) ⇔ Pit in adjacent cell
  - Stench at (i,j) ⇔ Wumpus in adjacent cell
  - Glitter ⇔ Gold in current cell

## Key Points

- Knowledge-based agents maintain an internal KB and use inference rather than just reflexes.
- The agent cycle: Percept → Add to KB → Query KB → Execute Action → Repeat.
- Wumpus World tests reasoning under partial observability.
- Stench indicates adjacent Wumpus; Breeze indicates adjacent Pit.
- Logical reasoning allows agents to deduce safe paths.
- A cell is safe if it can be proven (through negation) to have no hazards.
- Propositional logic provides the formal foundation for knowledge representation.

## Common Mistakes to Avoid

- Confusing "entailment" with "inference" - they are different concepts (semantic vs syntactic).
- Forgetting that the agent starts at [1,1] and can only move to adjacent cells.
- Assuming percepts directly identify hazards rather than their proximity.
- Not considering boundary conditions when applying rules at grid edges.

## Revision Tips

- Practice drawing the Wumpus World grid and marking percepts.
- Memorize the five percept types and their meanings.
- Re-derive safe cell conclusions using logical rules.
- Review the agent cycle diagram until it becomes automatic.
- Solve at least 3-4 Wumpus World reasoning problems before the exam.
