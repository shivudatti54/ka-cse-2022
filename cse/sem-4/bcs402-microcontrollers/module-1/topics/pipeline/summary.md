# Pipeline in ARM Embedded Systems - Summary

## Key Definitions

- **Pipeline**: An implementation technique that overlaps the execution of multiple instructions by dividing processing into discrete stages, each completing in one clock cycle.
- **Pipeline Depth**: The number of stages in a processor's pipeline; determines maximum theoretical speedup and clock frequency capability.
- **Pipeline Hazard**: A condition where the next instruction cannot execute in the ideal pipeline slot due to dependencies or resource conflicts.
- **Data Hazard**: A dependency between instructions where one instruction requires data that another instruction has not yet produced.
- **Control Hazard**: A pipeline stall caused by branch instructions where the correct instruction path is unknown until branch resolution.
- **Structural Hazard**: Inability to execute an instruction due to hardware resource limitations.
- **Pipeline Stall**: Insertion of NOP cycles to resolve hazards when forwarding or prediction cannot eliminate the dependency.
- **Pipeline Flush**: Discarding speculatively executed instructions after a mispredicted branch.

## Important Formulas

- **Ideal Pipeline Speedup**: S = n × N / (n + N - 1) ≈ n, where n = number of pipeline stages, N = number of instructions

- **Actual CPI with Stalls**: CPI = Ideal CPI + (Pipeline stall cycles per instruction)

- **Branch Penalty**: Total cycles = (N × CPI ideal) + (Number of branches × Branch penalty)

- **ARM7 PC Offset**: PC(used in fetch) = Current PC + 8 (for 32-bit ARM instructions)

## Key Points

1. ARM7TDMI uses a 3-stage pipeline (Fetch, Decode, Execute), while ARM9 uses a 5-stage pipeline (adds Memory Access and Write-back stages).

2. The pipeline allows one instruction to complete per cycle once fully loaded, achieving approximately n-times speedup for an n-stage pipeline.

3. Data hazards in ARM are primarily RAW (Read-After-Write) dependencies, which are resolved through forwarding paths and pipeline interlocks.

4. Forwarding routes results directly from pipeline stages to dependent instructions, eliminating the need to wait for register write-back.

5. Branch instructions in ARM cause pipeline flushes; the ARM7 3-stage pipeline has a 2-cycle branch penalty, while ARM9 reduces this through improved handling.

6. ARM's conditional execution feature significantly reduces branch penalties by allowing conditional instructions to execute without branch resolution.

7. Pipeline depth represents a trade-off: deeper pipelines enable higher clock frequencies but increase penalty for mispredicted branches.

8. Real-time embedded systems require careful consideration of pipeline behavior for accurate worst-case execution time (WCET) analysis.

## Common Mistakes

1. Confusing MIPS and ARM pipeline architectures—the ARM7 has 3 stages, not 5; ARM9 has 5 stages, matching MIPS but with different stage functions.

2. Forgetting the PC+8 offset in ARM instructions; the PC used during fetch points 8 bytes ahead, not to the current instruction.

3. Incorrectly calculating pipeline cycles—remember to account for pipeline fill (n cycles) and drain (n-1 cycles), not just N × n.

4. Assuming all hazards require stalling; forwarding can resolve most RAW hazards without any performance penalty in modern ARM processors.

5. Ignoring the difference between taken and not-taken branch penalties in branch prediction scenarios.