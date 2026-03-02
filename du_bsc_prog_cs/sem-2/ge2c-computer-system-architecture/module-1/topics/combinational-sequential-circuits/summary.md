# Combinational and Sequential Circuits - Summary

## Key Definitions and Concepts

- **Combinational Circuit**: A digital circuit where output depends only on present inputs with no memory element
- **Sequential Circuit**: A digital circuit where output depends on present inputs and past history (stored state), containing memory elements
- **Flip-Flop**: A bistable circuit that stores one bit of information; fundamental building block of sequential circuits
- **Multiplexer (MUX)**: A combinational circuit that selects one of multiple inputs based on select lines
- **Demultiplexer (DEMUX)**: A combinational circuit that routes one input to one of multiple outputs
- **Encoder**: Converts binary information from 2^n inputs to n outputs
- **Decoder**: Converts n inputs to 2^n outputs

## Important Formulas and Theorems

- **MUX Output**: Y = Σ m(i) · Ii where m(i) is the minterm for select line combination
- **Full Adder Sum**: S = A ⊕ B ⊕ Cin
- **Full Adder Carry**: Cout = AB + Cin(A ⊕ B)
- **JK Flip-Flop Characteristic Equation**: Q(next) = JQ' + K'Q
- **D Flip-Flop Characteristic Equation**: Q(next) = D
- **T Flip-Flop Characteristic Equation**: Q(next) = T ⊕ Q

## Key Points

- Combinational circuits have no memory; sequential circuits store information using flip-flops
- Basic logic gates (AND, OR, NOT) form building blocks for all combinational circuits
- Flip-flops are edge-triggered or level-triggered memory elements
- Synchronous sequential circuits use a common clock; asynchronous circuits respond to input changes
- Counters are classified as ripple (asynchronous) or synchronous based on clock distribution
- Registers store multiple bits; shift registers move data within the register
- Karnaugh maps provide graphical method for Boolean function minimization

## Common Mistakes to Avoid

- Confusing combinational with sequential circuits—remember memory elements define sequential circuits
- Forgetting that JK flip-flop toggles when J=K=1 (not an invalid state like SR)
- Ignoring propagation delays in ripple counters, which cause counting errors at high frequencies
- Incorrectly mapping select lines in multiplexer/demultiplexer problems
- Failing to consider setup and hold times for flip-flops in practical designs

## Revision Tips

1. Practice drawing truth tables for all flip-flop types until they become automatic
2. Solve previous year DU question papers to understand exam patterns and frequently asked topics
3. Focus on timing diagram problems—they appear frequently and test practical understanding
4. Memorize characteristic equations for flip-flops as they help in circuit analysis and design
5. Understand the relationship between state diagrams, state tables, and circuit implementation