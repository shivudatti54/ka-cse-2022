# Agents and Environment - Summary

## Key Definitions and Concepts

- **Agent**: An entity that perceives its environment through sensors and acts upon it through actuators
- **Agent Function**: Mathematical mapping from percept histories to actions
- **Rational Agent**: One that selects actions to maximize expected performance measure
- **PEAS**: Framework for task environment specification (Performance measure, Environment, Actuators, Sensors)

## Important Formulas and Theorems

- Agent Function: f: P\* → A (percept sequence to action mapping)
- Rationality depends on: Performance measure, Percept sequence, Prior knowledge, Available actions, Learning capabilities
- Environment complexity directly impacts agent architecture complexity

## Key Points

- The agent function describes ideal behavior; the agent program implements it
- Simple reflex agents work only in fully observable, deterministic environments
- Model-based agents maintain internal state to handle partial observability
- Goal-based agents consider future consequences; utility-based agents prefer better outcomes
- Partially observable environments require agents with memory/state
- Deterministic environments have predictable outcomes; stochastic environments involve uncertainty
- Static environments don't change during agent deliberation; dynamic environments do
- Multi-agent environments involve cooperation, competition, or both
- Learning agents improve through feedback from a critic component
- Real-world applications typically involve partially observable, stochastic, sequential, dynamic environments

## Common Mistakes to Avoid

- Confusing agent function (specification) with agent program (implementation)
- Assuming rational agents make perfect decisions (rationality ≠ omniscience)
- Choosing complex agent types for simple environments unnecessarily
- Ignoring environment properties when designing agent architectures
- Forgetting that partial observability requires internal state/memory

## Revision Tips

1. Always start by defining PEAS for any agent problem
2. Match environment properties to appropriate agent type
3. Practice drawing the agent-environment interaction diagram
4. Memorize the six environment property classifications
5. Remember: Complex environments need sophisticated agents; simple environments allow simple solutions
