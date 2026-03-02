# Summary: Sequential Circuits

Sequential circuits differ from combinational circuits in that their output depends on both current inputs and stored state information, giving them memory. This module covered:

1. **Fundamental Concepts**: Sequential circuits use feedback from memory elements (flip-flops) to store state, with outputs described by next-state equations ($Q_{next} = \delta(Q, X)$) and output equations.

2. **Flip-Flops**: Four primary types—SR, JK, D, and T—each with unique characteristic equations:

- SR: $Q_{next} = S + \bar{R}Q$
- JK: $Q_{next} = J\bar{Q} + \bar{K}Q$
- D: $Q_{next} = D$
- T: $Q_{next} = T \oplus Q$

3. **Timing Analysis**: Critical constraints include setup time, hold time, and propagation delay. Maximum clock frequency: $f_{max} \leq 1/(t_p + t_{su})$

4. **State Machines**: Moore machines output based on state only ($Y = \lambda(Q)$); Mealy machines output based on state and inputs ($Y = \lambda(Q, X)$)

5. **Design Methodology**: Specification → State Diagram → State Table → State Reduction → State Encoding → Flip-Flop Selection → Equation Derivation → Circuit Implementation

6. **Applications**: Sequential circuits enable counters, registers, shift registers, and finite state machines essential for digital computation and control systems.
