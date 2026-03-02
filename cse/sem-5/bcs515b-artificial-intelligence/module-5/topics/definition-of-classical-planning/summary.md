# Classical Planning - Summary

## Key Definitions and Concepts

- **Classical Planning**: A subfield of AI dealing with finding action sequences to achieve goals from initial states, assuming a fully observable, deterministic, and static world
- **Planning Problem**: Formally defined as P = (Σ, s₀, G), where Σ is the planning domain, s₀ is the initial state, and G is the goal condition
- **State**: A complete description of the world at a point in time, represented as a set of ground atoms (facts)
- **Action**: Has preconditions (requirements for applicability) and effects (changes to the world)
- **Transition Function (δ)**: Maps states and actions to new states: δ: S × A → S
- **Plan**: A sequence of actions [a₁, a₂, ..., aₙ] that transforms s₀ to a goal state

## Important Formulas and Theorems

- **Planning Problem**: P = (Σ, s₀, G)
- **Transition Function**: δ(s, a) = s' (deterministic successor state)
- **Plan Validity**: A plan π is valid if applicability holds at each step and goal G is satisfied in the final state
- **Action Schema**: Action(Name, Parameters, Preconditions, Effects)

## Key Points

- Classical planning assumes: full observability, determinism, and static world
- Actions are applicable only when their preconditions are satisfied in the current state
- Effects can be positive (add literals) or negative (delete literals)
- PDDL is the standard language for representing planning problems
- Plan execution is distinct from plan generation
- Classical planning is PSPACE-complete in general
- Goal regression is a backward planning technique
- States must be fully specified (no hidden information)

## Common Mistakes to Avoid

- Confusing preconditions with effects - preconditions must be true BEFORE action execution
- Forgetting that actions can have both positive and negative effects
- Assuming partial observability (it doesn't apply to classical planning)
- Not checking action applicability at each step when validating a plan
- Confusing the planning domain (general rules) with the planning problem (specific instance)

## Revision Tips

1. Practice writing action schemas with correct preconditions and effects for simple scenarios
2. Work through multiple planning examples to understand state transitions
3. Memorize the formal definition and three assumptions of classical planning
4. Review PDDL syntax for both domain and problem definitions
5. Practice validating given plans by checking applicability and goal satisfaction
6. Understand the difference between forward (progression) and backward (regression) planning
