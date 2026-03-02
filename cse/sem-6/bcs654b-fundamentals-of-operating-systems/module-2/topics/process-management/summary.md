# Process Management - Summary

## Key Definitions and Concepts

- **Process**: Program in execution (PC, registers, variables)
- **PCB**: Process Control Block (PID, state, registers, scheduling info)
- **Thread**: Lightweight process sharing same address space
- **Context Switch**: Saving/Restoring PCB when switching processes
- **Scheduling Criteria**:
  - CPU Utilization = (CPU busy time/Total time) × 100
  - Turnaround Time = Completion Time - Arrival Time
  - Waiting Time = Turnaround Time - Burst Time
  - Response Time = First Run Time - Arrival Time

## Important Formulas and Theorems

```markdown
1. Throughput = Number of processes completed/Time unit
2. Average Waiting Time = (Σ Waiting Times)/Number of processes
3. Scheduling Algorithm Metrics:
   - FCFS: Non-preemptive, convoy effect
   - SJF: Optimal waiting time (non-implementable)
   - Round Robin: Time quantum (TQ) dependent performance
   - Priority: Starvation problem
```

## Key Points

- Process states: New → Ready ↔ Running → Waiting → Terminated
- PCB contains all execution context (state, PC, open files)
- Scheduling queues: Job, Ready, Device
- Thread benefits: Responsiveness, resource sharing, economy
- Multithreading models:
  - Many-to-One (N:1): Multiple user threads → 1 kernel thread
  - One-to-One (1:1): Each user thread → kernel thread
  - Many-to-Many (M:N): Balances parallelism and efficiency
- Common thread libraries: POSIX Pthreads, Windows API, Java Threads
- Operations on processes: Creation (fork()), Termination (exit()), Communication (pipes)

## Common Mistakes to Avoid

1. Confusing program (static) vs process (dynamic instance)
2. Assuming ready→waiting transition (only running→waiting allowed)
3. Forgetting PCB components (must include memory limits, I/O status)
4. Mixing preemptive (RR) vs non-preemptive (FCFS) scheduling

## Revision Tips

1. Practice scheduling algorithms with arrival time tables
2. Draw state diagrams with ALL possible transitions
3. Compare thread models using tables:
   | Model | Pros | Cons |
   |------------|-----------------------|----------------------|
   | Many-to-One| Low OS overhead | No true parallelism |
   | One-to-One | True concurrency | High resource usage |
   | Many-to-Many| Balanced performance | Complex management |
4. Memorize PCB structure using acronym MRS (Memory, Registers, State)
