# Pipelining: Basic Concepts - Summary

## Key Definitions and Concepts

- PIPELINING: A technique that overlaps the execution of multiple instructions by dividing the processor into separate stages, improving throughput without reducing instruction latency.

- PIPELINE STAGES: The classic five-stage pipeline includes Instruction Fetch (IF), Instruction Decode (ID), Execute (EX), Memory Access (MEM), and Write Back (WB).

- PIPELINE REGISTERS: Hardware elements placed between stages that store intermediate results and control signals, enabling sequential instruction processing.

- PIPELINE HAZARDS: Conditions that prevent instructions from executing in the proper cycle; classified as structural, data, or control hazards.

## Important Formulas and Theorems

- Theoretical Speedup = Number of pipeline stages (k)

- Actual Speedup = (n × k × t) / (k × t + (n-1) × t), where n = number of instructions, k = stages, t = stage time

- Average CPI = Base CPI + (Miss rate × Miss penalty)

- Pipeline Efficiency = Actual Speedup / Number of stages

## Key Points

- PIPELINING INCREASES THROUGHPUT but not individual instruction speed; the first instruction still takes k cycles to complete.

- Five-stage pipeline achieves one instruction completion per cycle after initial fill period.

- Data hazards (RAW) are the most common and can be resolved through forwarding paths from EX/MEM and MEM/WB stages.

- Control hazards from branches cause pipeline bubbles; branch prediction and delay slots are mitigation techniques.

- CACHE MEMORY IS CRITICAL: Without fast caches, pipeline would stall frequently, negating performance benefits.

- Register delay from pipeline registers adds to clock cycle time but is offset by parallelism gains.

- Practical processors use deeper pipelines (10-20 stages) in modern CPUs to achieve higher clock frequencies.

## Common Mistakes to Avoid

- CONFUSING LATENCY AND THROUGHPUT: Remember that pipelining improves throughput (instructions per second), not the time to execute a single instruction.

- IGNORING PIPELINE FILL TIME: Speedup calculation must account for the initial k cycles needed to fill the pipeline.

- OVERLOOKING CACHE IMPACT: Many students focus only on pipeline hazards and forget that memory access time fundamentally limits pipeline performance.

- MISIDENTIFYING HAZARD TYPES: Structural hazards involve resource conflicts, data hazards involve instruction dependencies, and control hazards involve branch outcomes.

## Revision Tips

- PRACTICE DRAWING pipeline timing diagrams for at least 3-4 instructions to visualize overlap and stalls.

- MEMORIZE the three hazard types and their solutions: structural (add hardware), data (forwarding/scheduling), control (prediction).

- SOLVE AT LEAST 5 numerical problems on speedup and CPI calculations before the exam.

- UNDERSTAND why cache is essential: relate it to the MEM stage and memory access bottleneck in pipelines.