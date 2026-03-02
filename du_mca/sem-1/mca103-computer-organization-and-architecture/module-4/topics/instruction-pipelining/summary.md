# Instruction Pipelining - Summary

## Key Definitions and Concepts

- **Instruction Pipelining**: A technique that overlaps the execution of multiple instructions by dividing execution into discrete stages, allowing one instruction to complete per clock cycle.
- **Pipeline Stage**: One of k distinct phases of instruction execution (IF, ID, EX, MEM, WB in classic RISC pipeline).
- **Pipeline Hazard**: A condition that prevents ideal pipeline operation; classified as structural, data, or control hazards.
- **Throughput**: Number of instructions completed per clock cycle; ideally 1 in a pipelined processor.
- **Latency**: Number of clock cycles required to execute a single instruction from start to finish.

## Important Formulas and Theorems

- **Maximum Speedup**: S(max) = k, where k is the number of pipeline stages
- **Actual Speedup**: S = (n × k) / (n + k - 1), where n is instruction count
- **Throughput**: 1 instruction per clock cycle (ideal)
- **Efficiency**: E = n / (n + k - 1)
- **Branch Penalty**: Number of stages between instruction fetch and branch resolution
- **Average Branch Penalty**: (1 - Prediction Accuracy) × Branch Penalty

## Key Points

- Pipelining improves throughput (instructions per cycle) but not individual instruction latency
- Five-stage RISC pipeline (IF, ID, EX, MEM, WB) achieves near-ideal speedup of 5x for large instruction sequences
- Data hazards (RAW) require actual computation results; WAR/WAW are register reuse conflicts
- Forwarding resolves most RAW hazards without stalling by routing results directly between pipeline stages
- Control hazards cause 2-3 cycle penalties in typical pipelines; branch prediction mitigates this
- Modern processors use 10-19 stage deep pipelines for higher clock frequencies
- Superscalar and out-of-order execution build upon basic pipelining concepts
- Pipeline flush (discarding speculatively executed instructions) occurs on branch misprediction

## Common Mistakes to Avoid

- Confusing throughput with latency: pipeline increases throughput, not individual instruction speed
- Thinking pipeline stages reduce total work: they merely overlap work that must still be done
- Forgetting that RAW is the only true data dependency in sequential execution; WAR/WAW are artificial
- Incorrectly calculating speedup by using clock cycle time instead of cycle count
- Assuming more pipeline stages always improves performance—deeper pipelines increase hazard penalties

## Revision Tips

1. Draw 5-cycle pipeline timing diagrams for at least 5 instructions to visualize overlap and identify hazards
2. Memorize the three hazard types and one-sentence explanation for each
3. Practice calculating speedup for various values of n (instruction count) and k (stages)
4. Understand forwarding: which pipeline registers connect to which stages for ALU operations
5. Review branch prediction concepts: why static prediction fails, how dynamic prediction improves accuracy
6. Connect to real processors: Intel Core i7 uses 14-19 stages; ARM Cortex processors use varying depths
7. Solve numerical problems from previous DU question papers on pipeline performance and hazard resolution