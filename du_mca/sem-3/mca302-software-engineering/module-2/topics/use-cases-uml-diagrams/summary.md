# Use Cases and UML Diagrams - Summary

## Key Definitions and Concepts

- **Use Case**: A description of system behavior from a user's perspective, capturing functional requirements without revealing internal implementation.
- **Actor**: An external entity (person, system, or device) that interacts with the system being modeled.
- **UML (Unified Modeling Language)**: A standardized visual language for visualizing, specifying, constructing, and documenting software-intensive systems.
- **Class Diagram**: A structural diagram showing classes, their attributes, operations, and relationships.
- **Sequence Diagram**: A behavioral diagram illustrating object interactions arranged in time sequence.
- **Activity Diagram**: A behavioral diagram modeling workflow and parallel processes.
- **State Machine Diagram**: A behavioral diagram showing states and transitions of an object over its lifetime.

## Important Formulas and Theorems

- **Multiplicity Notation**: `0..1` (optional), `0..*` (zero to many), `1` (exactly one), `1..*` (one to many)
- **Visibility Symbols**: `+` (public), `-` (private), `#` (protected), `~` (package)
- **Relationship Cardinality**: One-to-One, One-to-Many, Many-to-Many represented through multiplicity

## Key Points

- Use Case modeling focuses on "what" the system does, not "how" it does it.
- `<<include>>` represents mandatory reusable behavior; `<<extend>>` represents optional/exceptional behavior.
- Structural diagrams show static structure; behavioral diagrams show dynamic behavior.
- Aggregation (hollow diamond) implies independent lifecycle; Composition (filled diamond) implies dependent lifecycle.
- Sequence diagrams are essential for understanding object communication and method invocation order.
- Activity diagrams support parallel processing through fork and join nodes.
- UML 2.5 is the current industry standard with 14 diagram types.

## Common Mistakes to Avoid

1. Confusing `<<include>>` with `<<extend>>` relationships in Use Case diagrams
2. Mixing up Aggregation and Composition relationships in Class diagrams
3. Incorrectly using visibility symbols or omitting them entirely
4. Drawing Sequence diagrams without proper activation bars showing execution time
5. Using bidirectional associations without considering real-world directionality

## Revision Tips

1. Practice drawing all major diagram types by hand—examiners expect clean, properly-notated diagrams.
2. Memorize the 14 UML 2.5 diagram types and their categories (structural vs. behavioral).
3. Work through real-world scenarios like ATM, Library, and Shopping systems repeatedly.
4. Focus on understanding when to use each relationship type—this is frequently tested.
5. Review previous DU question papers to understand the exam pattern and important topics.