# Pipelining: Basic Concepts

## Introduction

Pipelining is one of the most fundamental techniques used in modern computer processors to improve instruction throughput and overall system performance. In the context of the Basic Processing Unit, pipelining allows the processor to work on multiple instructions simultaneously by overlapping their execution stages, much like an assembly line in a factory. While a single instruction takes the same amount of time to execute, the pipeline enables the processor to complete one instruction per clock cycle after the pipeline is full, resulting in a significant improvement in computational throughput.

The concept of pipelining becomes particularly important when considering the execution of a complete instruction, which we have studied involves multiple stages: fetching the instruction from memory, decoding it, executing the operation, and storing the result. Without pipelining, each of these stages must complete entirely before the next instruction can begin, leaving most of the processor's hardware idle at any given time. Pipelining addresses this inefficiency by dividing the processor into separate stages, each capable of working on a different instruction simultaneously.

In this topic, we will explore the fundamental concepts of pipelining, including pipeline structure, speedup calculations, hazards that can limit performance, and the critical role that cache memory plays in making pipelines effective. Understanding these concepts is essential for comprehending how modern processors achieve the performance levels required by contemporary computing applications.

## Key Concepts

### What is a Pipelined Processor?

A pipeline in a processor is a series of processing stages, where each stage completes a portion of the instruction execution task. The output of one stage becomes the input to the next stage, allowing multiple instructions to be in various stages of execution simultaneously. The classic RISC pipeline, often called the five-stage pipeline, consists of the following stages: Instruction Fetch (IF), Instruction Decode (ID), Execute (EX), Memory Access (MEM), and Write Back (WB).

Consider a non-pipelined processor that takes 100 nanoseconds to execute one instruction. This processor can complete 10 million instructions per second. Now consider a pipelined version where each of the five stages takes 20 nanoseconds. The first instruction still takes 100 nanoseconds to complete (5 × 20 ns), but once the pipeline is full, a new instruction completes every 20 nanoseconds. This processor can now complete 50 million instructions per second, representing a fivefold improvement in throughput.

### Pipeline Registers

Pipeline registers are essential components that separate the different stages of a pipeline. These registers store the intermediate results and control signals between stages, ensuring that each stage has the necessary information to complete its portion of the instruction. In the five-stage pipeline, there would typically be pipeline registers between IF/ID, ID/EX, EX/MEM, and MEM/WB stages.

The placement of pipeline registers introduces a small delay in the signal propagation, known as register delay. This delay must be factored into the clock cycle time of the pipelined processor. However, the performance gains from parallelism far outweigh this overhead in most practical scenarios. Pipeline registers also help maintain instruction order and ensure that instructions do not interfere with each other in incorrect ways.

### Speedup and Efficiency

The theoretical speedup of a pipeline with N stages over a non-pipelined processor is N times, assuming ideal conditions with no hazards or stalls. This is because the pipeline allows N instructions to be processed simultaneously, each in a different stage. However, several factors limit the actual speedup achievable in real processors.

The actual speedup can be calculated using the formula: Speedup = (Execution time without pipeline) / (Execution time with pipeline). For a pipeline with k stages, where each stage takes time t, the time to execute n instructions without pipelining is n × k × t. With pipelining, the time is k × t + (n - 1) × t. Therefore, the speedup approaches k as n becomes large, but never exceeds k due to the initial pipeline fill time.

Pipeline efficiency measures how effectively the pipeline is being used. It is calculated as the actual speedup divided by the number of stages. An efficiency of 1 (or 100%) would mean perfect utilization of all pipeline stages, which is rarely achieved in practice due to hazards and other limitations.

### Pipeline Hazards

Pipeline hazards are situations that prevent the next instruction in the instruction stream from executing in the proper clock cycle. There are three main types of hazards: structural hazards, data hazards, and control hazards.

Structural hazards occur when the processor hardware cannot support all combinations of instructions in the pipeline simultaneously. This typically happens when two instructions need the same hardware resource at the same time. For example, if the processor has only one memory port, both instruction fetch and data access cannot happen in the same cycle. Structural hazards can be resolved by adding duplicate hardware resources or by careful scheduling of instructions.

Data hazards occur when instructions depend on the results of previous instructions that are still in the pipeline. There are three types of data hazards: Read After Write (RAW), Write After Read (WAR), and Write After Write (WAW). RAW hazards, also called true data dependencies, are the most common and occur when an instruction needs to read a value that a previous instruction has not yet written. WAR and WAW hazards are more common in out-of-order execution processors and are less likely in simple in-order pipelines.

Control hazards, also known as branch hazards, occur due to branches and other instructions that change the program counter. When a branch is decoded and found to be taken, the instructions that were fetched after the branch are incorrect and must be discarded. This creates bubbles in the pipeline and reduces performance. Branch prediction techniques are used to mitigate control hazards.

### Role of Cache Memory in Pipelines

Cache memory plays a CRITICAL role in pipeline performance. Without fast memory access, the pipeline stages that require memory access (particularly IF and MEM stages) would become bottlenecks, causing the pipeline to stall frequently. The inclusion of cache memory between the processor and main memory significantly reduces memory access latency.

Instruction cache (I-cache) stores frequently executed instructions close to the processor, allowing fast instruction fetches without waiting for main memory access. Similarly, data cache (D-cache) enables quick reads and writes of data operands. In a pipelined processor, cache hits can often be serviced in a single clock cycle, allowing the pipeline to operate at full speed. Cache misses, however, can cause significant delays as the processor may need to wait for data to be fetched from main memory, which can take dozens of clock cycles.

The principle of locality, both temporal and spatial, makes caches effective. Temporal locality suggests that recently accessed instructions and data are likely to be accessed again, while spatial locality indicates that nearby instructions and data are likely to be needed soon. These characteristics align perfectly with pipeline operation, as pipeline stages typically work on sequential instructions and related data.

## Examples

### Example 1: Calculating Pipeline Speedup

Consider a non-pipelined processor that takes 200 nanoseconds to complete one instruction. Design a five-stage pipeline where each stage takes 45 nanoseconds. Calculate the theoretical speedup for executing 100 instructions.

**Solution:**

For non-pipelined processor:
Time for 100 instructions = 100 × 200 ns = 20,000 ns

For pipelined processor:
Pipeline fill time = 5 × 45 ns = 225 ns
Time for remaining 99 instructions = 99 × 45 ns = 4,455 ns
Total time = 225 + 4,455 = 4,680 ns

Speedup = 20,000 / 4,680 ≈ 4.27

The speedup is less than 5 (the number of stages) because of the pipeline fill overhead. As the number of instructions increases, the speedup approaches 5.

### Example 2: Identifying Data Hazards

Consider the following instruction sequence:
```
I1: ADD R1, R2, R3      // R1 = R2 + R3
I2: SUB R4, R1, R5      // R4 = R1 - R5
I3: AND R6, R4, R7      // R6 = R4 & R7
```

Identify the data hazards in this sequence for a five-stage pipeline.

**Solution:**

I1 writes to R1 in the WB stage.
I2 reads R1 in the ID stage and writes R4 in WB stage.
I3 reads R4 in ID stage.

RAW Hazard between I1 and I2: I2 needs the value of R1 that I1 produces. In a five-stage pipeline, I1 writes in stage 5 (WB), while I2 reads in stage 2 (ID). Without forwarding, there is a 3-cycle stall.

RAW Hazard between I2 and I3: I3 needs the value of R4 that I2 produces. Similarly, without forwarding, I3 must wait until I2 completes its WB stage.

These hazards can be resolved through data forwarding (sending results directly from EX/MEM or MEM/WB stages to earlier stages) or by compiler scheduling.

### Example 3: Pipeline Stall due to Cache Miss

In a pipeline with 5 stages, assume the following:
- Cache hit takes 1 cycle
- Cache miss takes 20 cycles to service
- Cache miss rate for instruction fetch is 2%
- Each instruction requires 1 instruction fetch

Calculate the average CPI (Cycles Per Instruction) and determine the performance impact.

**Solution:**

Average cycles per instruction fetch = (0.98 × 1) + (0.02 × 20) = 0.98 + 0.40 = 1.38 cycles

Since instruction fetch is part of the IF stage, the average CPI is 1.38.

If the processor had perfect memory with 1 cycle per access, CPI would be 1.0.

The performance degradation = (1.38 - 1.0) / 1.0 × 100% = 38%

This demonstrates why cache memory is CRITICAL for pipeline performance. Even a 2% miss rate causes significant performance degradation.

## Exam Tips

FOR DU SEMESTER EXAMS, REMEMBER THE FOLLOWING KEY POINTS:

1. UNDERSTAND THE BASIC IDEA: Pipelining overlaps instruction execution stages to improve throughput. Know that it does NOT reduce instruction latency but INCREASES throughput.

2. SPEEDUP FORMULA: Remember that theoretical maximum speedup equals the number of pipeline stages. Actual speedup is always less due to hazards and pipeline fill time.

3. HAZARD TYPES: Be able to clearly distinguish between structural, data, and control hazards. Know that data hazards are the most common and can be resolved through forwarding and compiler scheduling.

4. CACHE IMPORTANCE: Cache memory is ESSENTIAL for pipeline performance. Know that without caches, pipeline stalls would occur frequently, eliminating most performance benefits.

5. DRAW THE PIPELINE DIAGRAM: Practice drawing instruction-time diagrams for both non-pipelined and pipelined execution. This helps visualize how instructions overlap.

6. CPI CALCULATIONS: Be prepared to calculate average CPI considering cache miss rates and branch penalties. The formula: Average CPI = Base CPI + (Miss rate × Miss penalty).

7. SOLVE NUMERICAL PROBLEMS: DU exams frequently include numerical problems on speedup calculations, hazard identification, and pipeline timing. Practice these thoroughly.