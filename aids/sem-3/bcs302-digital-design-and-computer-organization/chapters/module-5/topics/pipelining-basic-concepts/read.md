# Pipeline Basics

## What is Pipelining?

Technique to overlap instruction execution. Like assembly line - multiple instructions in different stages simultaneously.

## 5-Stage MIPS Pipeline

| Stage | Name               | Action                             |
| ----- | ------------------ | ---------------------------------- |
| IF    | Instruction Fetch  | Read instruction from memory       |
| ID    | Instruction Decode | Decode opcode, read registers      |
| EX    | Execute            | ALU operation, address calculation |
| MEM   | Memory Access      | Load/Store memory access           |
| WB    | Write Back         | Write result to register           |

## Pipeline Execution

```
Time →  1   2   3   4   5   6   7   8   9
I1:    IF  ID  EX MEM  WB
I2:        IF  ID  EX MEM  WB
I3:            IF  ID  EX MEM  WB
I4:                IF  ID  EX MEM  WB
I5:                    IF  ID  EX MEM  WB
```

## Performance Metrics

**Without pipelining:**

- Time = n × k × τ (n instructions, k stages, τ cycle time)

**With pipelining:**

- Time = (k + n - 1) × τ

**Speedup:**

```
Speedup = n × k / (k + n - 1)
```

For large n: Speedup ≈ k (number of stages)

**CPI (Cycles Per Instruction):**

- Ideal pipelined CPI = 1
- Actual CPI = 1 + stall cycles
