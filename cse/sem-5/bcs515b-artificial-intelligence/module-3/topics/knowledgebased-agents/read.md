# Knowledge-Based Agents

## Introduction

Knowledge-Based Agents are fundamental entities in Artificial Intelligence that utilize knowledge representation and reasoning to make intelligent decisions. Unlike simple reflex agents that respond directly to stimuli based on condition-action rules, knowledge-based agents maintain an internal knowledge base (KB) of facts about the world and use logical reasoning to determine appropriate actions. This approach allows agents to handle complex, dynamic environments where pre-defined responses are insufficient.

The study of knowledge-based agents is crucial in AI because they form the foundation for many advanced systems including expert systems, planning systems, and natural language understanding applications. In the context of 's Artificial Intelligence curriculum, understanding knowledge-based agents provides students with essential insights into how machines can represent, manipulate, and reason with knowledge - a cornerstone of intelligent behavior. The Wumpus World environment serves as an excellent benchmark problem for understanding these agents, as it presents a miniature world that captures all essential challenges of reasoning under uncertainty.

## Key Concepts

### Knowledge-Based Agent Architecture

A knowledge-based agent consists of three main components:

1. **Knowledge Base (KB)**: A collection of sentences in a knowledge representation language that express facts about the world. The KB stores both background knowledge (general rules) and observed facts (percepts).

2. **Inference Engine**: The component that derives new facts from existing knowledge using logical reasoning. It applies inference rules to the KB to answer queries and add new sentences.

3. **Agent Program**: Connects percepts to actions by maintaining the KB, updating it with new percepts, and querying the KB to determine the best action.

The agent operates in a cycle: receive percept → add to KB → query KB for action → execute action → repeat.

### The Wumpus World

The Wumpus World is a classic AI problem used to illustrate knowledge-based reasoning. It consists of:

- **Environment**: A 4×4 grid of rooms (cells)
- **Agent**: Starts at position [1,1] facing right
- **Wumpus**: A dangerous creature that kills the agent if entered; located in one random cell
- **Pits**: Bottomless pits that kill the agent if entered; scattered in the grid
- **Gold**: The agent's goal - to grab the gold and return safely
- **Percepts**: The agent receives sensory information:
- Stench (adjacent to Wumpus)
- Breeze (adjacent to Pit)
- Glitter (gold in current cell)
- Bump (when hitting a wall)
- Scream (when Wumpus is killed)

### Knowledge Representation

**Propositional Logic** is used for representing facts in the Wumpus World:

- **Atomic sentences**: Basic propositions like P(1,2) meaning "Pit at (1,2)"
- **Complex sentences**: Using logical connectives (¬, ∧, ∨, ⇒, ⇔)
- **Horn clauses**: Sentences with at most one positive literal (useful for efficient reasoning)

**Key Propositions for Wumpus World**:

- B(i,j): Breeze at (i,j)
- S(i,j): Stench at (i,j)
- P(i,j): Pit at (i,j)
- W(i,j): Wumpus at (i,j)
- G(i,j): Gold at (i,j)

### Logical Reasoning

**Modus Ponens**: If P ⇒ Q is known and P is true, then Q can be inferred.

**Universal Instantiation**: If ∀x P(x) is true, then P(c) is true for any constant c.

**Forward Chaining**: Start from known facts and apply inference rules repeatedly until the goal is reached.

**Backward Chaining**: Start from the goal and work backwards to find supporting facts.

### Knowledge Representation Languages

**Syntax**: Defines valid sentences in the language
**Semantics**: Defines the meaning of sentences (truth conditions)
**Entailment**: KB ⊨ α means α follows necessarily from KB
**Inference**: KB ⊢ α means α can be derived from KB via inference rules

## Examples

### Example 1: Reasoning about Pits

**Problem**: The agent at [1,1] perceives "Breeze" at position [1,1]. What can the agent infer?

**Solution**:

**Step 1**: Identify the rule

- Rule: B(i,j) ⇒ ∃ neighboring cell (P(p,q))
- In English: "If there's a breeze at [i,j], then there's a pit in one of the adjacent cells"

**Step 2**: Analyze the current position

- [1,1] has two adjacent cells: [1,2] and [2,1]
- Agent knows: B(1,1) is TRUE

**Step 3**: Apply Modus Ponens

- From B(1,1) ⇒ (P(1,2) ∨ P(2,1))
- And B(1,1) is TRUE
- Therefore: P(1,2) ∨ P(2,1) is TRUE

**Step 4**: What the agent CANNOT conclude yet

- Cannot determine exactly which cell has the pit
- Cannot conclude that either cell definitely has a pit

### Example 2: Safe Cell Identification

**Problem**: Agent moves to [1,2] and perceives "Stench" but NO "Breeze". What does the agent conclude?

**Solution**:

**Step 1**: Percepts at [1,2]

- S(1,2) = TRUE (Stench present)
- B(1,2) = FALSE (No breeze)

**Step 2**: Apply logical reasoning for stench

- From S(1,2): Wumpus must be in adjacent cell
- Adjacent cells to [1,2]: [1,1], [2,2], [1,3]
- Already know [1,1] has no Wumpus (agent visited safely)
- So: W(1,3) ∨ W(2,2) must be TRUE

**Step 3**: Apply logical reasoning for no breeze

- From ¬B(1,2): No pit in adjacent cells
- Adjacent cells: [1,1], [2,2], [1,3]
- Therefore: ¬P(1,1) ∧ ¬P(1,3) ∧ ¬P(2,2) must all be TRUE

**Step 4**: Conclusion

- [2,2] is now safe (no pit from breeze analysis)
- Agent can confidently move to [2,2]

### Example 3: Knowledge Base Construction

**Problem**: Write KB sentences for the Wumpus world rule "Pits cause breezes in adjacent squares"

**Solution**:

**Step 1**: Define the implication rule

- B(i,j) ⇔ (P(i-1,j) ∨ P(i+1,j) ∨ P(i,j-1) ∨ P(i,j+1))
- This is a biconditional: breeze IF AND ONLY IF adjacent pit exists

**Step 2**: Break into two directions

1. B(i,j) ⇒ (P(i-1,j) ∨ P(i+1,j) ∨ P(i,j-1) ∨ P(i,j+1))
2. (P(i-1,j) ∨ P(i+1,j) ∨ P(i,j-1) ∨ P(i,j+1)) ⇒ B(i,j)

**Step 3**: Apply for specific locations

- B(1,1) ⇒ (P(1,2) ∨ P(2,1))
- B(1,2) ⇒ (P(1,1) ∨ P(1,3) ∨ P(2,2))

**Step 4**: Handling boundary conditions

- For [1,1], only valid adjacent cells are [1,2] and [2,1]
- The rule automatically handles this since out-of-bounds cells are implicitly FALSE

## Exam Tips

1. **Remember the agent cycle**: Percept → Update KB → Query KB → Execute Action → Repeat. This sequence is fundamental and frequently tested.

2. **Know Wumpus World percepts**: Stench = Wumpus nearby, Breeze = Pit nearby, Glitter = Gold, Bump = Wall, Scream = Wumpus killed.

3. **Understand the difference between entails (⊨) and infers (⊢)**: Entailment is semantic (truth-based), inference is syntactic (rule-based). If KB is complete and sound, then ⊢ implies ⊨.

4. **Apply Modus Ponens correctly**: From P ⇒ Q and P, infer Q. This is the most common inference rule used in knowledge-based systems.

5. **Remember Horn Clauses**: Sentences with at most one positive literal enable efficient forward chaining. Expert systems often use Horn clause form.

6. **Safe cell reasoning**: A cell is safe if it cannot contain a Wumpus or Pit. Use negation of percepts to prove safety.

7. **Vocabulary matters**: Study terms like atomic sentences, complex sentences, propositional logic, inference engine, and knowledge base thoroughly.

8. **Understand the knowledge representation requirements**: Syntax (valid sentences), Semantics (meaning/truth), Entailment (logical consequence), and Inference (derivation methods).
