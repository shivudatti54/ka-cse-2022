# **Theory of Computation Revision Notes**

### Deterministic Finite Automata (DFA)

- **Definition:** A DFA is a 6-tuple M = (Q, Σ, δ, q0, F, q_accept)
  - Q: set of states
  - Σ: alphabet
  - δ: transition function
  - q0: initial state
  - F: set of accepting states
  - q_accept: final state
- **Properties:**
  - Deterministic: for each input, there is exactly one next state
  - Finite: number of states is finite
  - Accepting: if input string is accepted, final state is reached
- **Formulas:**
  - DFA acceptance condition: if input string is accepted, final state is reached
  - Regular expression: L(M) = {x ∈ Σ\* | δ(q0, x) ∈ F}
- **Theorems:**
  - Pumping Lemma for DFAs: if string is accepted, it can be pumped to create new strings accepted by M

### Nondeterministic Finite Automata (NFA)

- **Definition:** An NFA is a 7-tuple N = (Q, Σ, δ, q0, F, q_accept, δ_accept)
  - Q: set of states
  - Σ: alphabet
  - δ: transition function
  - q0: initial state
  - F: set of accepting states
  - q_accept: final state
  - δ_accept: set of accepting transitions
- **Properties:**
  - Nondeterministic: for each input, multiple next states are possible
  - Finite: number of states is finite
  - Accepting: if input string is accepted, final state is reached
- **Formulas:**
  - NFA acceptance condition: if input string is accepted, final state is reached or accepting transition is reached
  - Regular expression: L(N) = {x ∈ Σ\* | ∃q0, δ(0, x) ∈ F or δ(0, x) ∈ δ_accept}

### Application: Text Search

- **Text Search Problem:** find all occurrences of a pattern string in a text string
- **DFA Solution:** use DFA to find all accepting paths in the NFA representing the text search pattern
- **NFA Solution:** use NFA to find all accepting states in the DFA representing the text search pattern

### Finite Automata with Epsilon-Transitions

- **Definition:** An NFA with epsilon-transitions is a 7-tuple N = (Q, Σ, δ, q0, F, q_accept, δ_accept)
  - Q: set of states
  - Σ: alphabet
  - δ: transition function
  - q0: initial state
  - F: set of accepting states
  - q_accept: final state
  - δ_accept: set of accepting transitions
- **Properties:**
  - Epsilon-transitions: ε ∈ Σ, δ(q, ε) = q'
  - Nondeterministic: for each input, multiple next states are possible
  - Finite: number of states is finite
  - Accepting: if input string is accepted, final state is reached or accepting transition is reached
- **Formulas:**
  - NFA acceptance condition: if input string is accepted, final state is reached or accepting transition is reached
  - Regular expression: L(N) = {x ∈ Σ\* | ∃q0, δ(0, x) ∈ F or δ(0, x) ∈ δ_accept}
