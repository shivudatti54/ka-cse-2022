# Pipelining Basic Concepts - Summary

## Key Definitions and Concepts

- **Pipelining**: An architectural technique that divides instruction execution into multiple stages, allowing multiple instructions to be processed simultaneously at different pipeline stages.

- **Pipeline Stage**: One of the discrete steps in instruction processing, such as fetch, decode, execute, memory access, or write-back.

- **Pipeline Register**: Hardware registers placed between pipeline stages to hold intermediate results and control information.

- **Pipeline Hazard**: A condition that prevents the ideal continuous flow of instructions through the pipeline, categorized as structural, data, or control hazards.

- **Throughput**: The number of instructions completed per unit time, which pipelining improves; measured in instructions per cycle (IPC).

- **Latency**: The total time required to execute a single instruction from start to finish.

## Important Formulas and Theorems

- **Ideal Speedup**: k (number of pipeline stages) for large number of instructions
- **Actual Speedup**: n × Clock cycle / (n + k - 1) × Clock cycle, where n = instructions, k = stages
- **Effective CPI**: 1 + (Stall frequency × Stall penalty)
- **Pipeline Efficiency**: (Actual speedup / Number of stages) × 100%

## Key Points

1. Pipelining improves throughput (instructions per clock cycle) but does not reduce the execution time of a single instruction (latency).

2. The classic five-stage pipeline consists of IF, ID, EX, MEM, and WB stages.

3. Structural hazards occur due to insufficient hardware resources; resolved by duplicating resources or careful design.

4. Data hazards occur when instructions depend on results from previous instructions: RAW (true dependency), WAR, and WAW (name dependencies).

5. Control hazards arise from branch instructions; mitigated through branch prediction, delay slots, and pipeline flushing.

6. Data forwarding (bypassing) allows ALU results to be forwarded directly to subsequent instructions without waiting for register write-back.

7. Pipeline clock cycle time is determined by the slowest stage plus register setup time.

8. During pipeline fill (first k-1 cycles) and drain (last k-1 cycles), full throughput is not achieved.

9. Cache memory is critical for pipeline performance as it reduces memory access time for instruction fetch and data memory operations.

## Common Mistakes to Avoid

1. Confusing throughput with latency—pipelining increases throughput, not speed of individual instructions.

2. Forgetting that pipeline hazards cause actual performance to be less than ideal speedup.

3. Assuming RAW hazards can always be resolved without stalls—forwarding has limitations.

4. Not considering that branch mispredictions cause pipeline flushes, wasting several cycles of work.

5. Ignoring the fact that pipeline registers add latency to each instruction's path through the processor.

## Revision Tips

1. Draw timing diagrams for a 5-stage pipeline with and without hazards to visualize instruction overlap.

2. Practice calculating speedup, CPI, and efficiency for different pipeline configurations and stall scenarios.

3. Memorize the five pipeline stages and what happens in each stage for different instruction types (R-type, load, store, branch).

4. Review the relationship between pipelining and cache memory—cache misses cause pipeline stalls.

5. Solve previous years' DU exam questions on pipelining to understand the exam pattern and important topics.