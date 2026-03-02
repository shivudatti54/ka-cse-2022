# Representation Revisited - Summary

## Key Definitions

- **Knowledge Representation**: The study of how to encode knowledge in a formal language that AI systems can use to reason about the world.
- **Expressivity**: The ability of a representation language to capture all necessary truths about a domain.
- **Procedural Knowledge**: Knowledge encoded as procedures or algorithms (knowing how).
- **Declarative Knowledge**: Knowledge encoded as statements in a formal language (knowing that).
- **Frame Problem**: The challenge of representing what does not change when actions are performed.
- **Situation Calculus**: A formalism for representing dynamic worlds using situations, actions, and fluents.
- **Successor State Axioms**: Axioms specifying what is true in the situation resulting from an action.

## Important Formulas

- Successor state axiom pattern: `F(do(a,s)) ↔ (Effect_a ∨ (F(s) ∧ ¬Changed_a))`
- Frame axiom inference: If fluent F is not affected by action a, then `F(do(a,s)) ↔ F(s)`
- First-order universal quantification: `∀x: P(x)` represents "for all x, P is true"
- First-order existential quantification: `∃x: P(x)` represents "there exists an x such that P is true"

## Key Points

1. Good representations balance expressivity, computational tractability, ease of acquisition, clarity, modularity, and perspicuity.

2. The representation spectrum progresses from ground atomic facts through propositional logic to first-order logic, description logics, and ontologies.

3. Declarative representations are preferred in AI because they are easier to verify, debug, and modify than purely procedural encodings.

4. Representation and reasoning are inseparable—the choice of representation directly determines reasoning complexity.

5. The frame problem is solved in situation calculus using successor state axioms that explicitly characterize changes while implicitly preserving other facts.

6. First-order logic enables compact representation of general rules that would require enumeration in propositional logic.

7. Modern AI systems often combine declarative knowledge bases with procedural attachments for efficiency.

8. Ontologies provide shared vocabularies enabling logical inference across different knowledge bases and systems.

## Common Mistakes

1. Confusing propositional and first-order logic—propositional logic cannot express "all" or "some" quantifiers concisely.

2. Ignoring computational complexity—choosing highly expressive representations without considering inference tractability.

3. Overlooking the frame problem when representing dynamic worlds—failing to specify what changes and what persists.

4. Treating representation as separate from reasoning—they must be designed together.

5. Using overly complex representations when simpler ones suffice—adding unnecessary expressivity increases computational cost.