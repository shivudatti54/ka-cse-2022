# Use-Case Approach - Summary

## Key Definitions and Concepts

- **Use Case**: A description of system behavior from a user's perspective that captures a complete flow of events to achieve a specific goal
- **Actor**: An external entity (person, system, or device) that interacts with the system; represents a role, not a specific individual
- **Use Case Diagram**: UML graphical representation showing actors, use cases, and their relationships within a system boundary
- **Include Relationship**: Used when one use case incorporates another use case's behavior (reusable common functionality)
- **Extend Relationship**: Used when one use case adds behavior to another under specific conditions (optional/exceptional cases)

## Important Formulas and Theorems

- Use case relationships follow UML notation: include (<<include>>), extend (<<extend>>), generalization (solid arrow)
- A well-formed use case must have: unique name, defined actors, preconditions, postconditions, basic flow, and alternative flows
- Preconditions + Basic Flow + Postconditions = Complete Use Case Description

## Key Points

- Use cases focus on "what" the system does, not "how" it does it
- Actors are always external to the system being modeled
- Include is mandatory behavior reuse; Extend is optional behavior addition
- Use case diagrams provide high-level view; use case descriptions provide detailed behavior
- Primary actors initiate use cases; secondary actors provide services to the system
- Alternative flows handle errors, exceptions, and variations from the basic path
- Use cases trace directly to test cases, enabling verification and validation

## Common Mistakes to Avoid

- Confusing actors with users (actors are roles, not individuals)
- Using include instead of extend or vice versa—remember: include = mandatory, extend = optional
- Writing use cases that describe system internals rather than user-visible behavior
- Forgetting preconditions and postconditions—they are essential for defining system state
- Creating use cases that are too detailed (specifying UI elements) or too vague (lacking flow)

## Revision Tips

1. Practice drawing use case diagrams for familiar systems like library management, online booking, or banking systems
2. Memorize the difference between include and extend relationships with examples
3. Review the fully dressed use case format and practice writing at least 2-3 complete use case descriptions
4. Understand that exam questions often ask you to identify errors in given use case descriptions
5. Focus on preconditions and postconditions—they are frequently tested in DU exams