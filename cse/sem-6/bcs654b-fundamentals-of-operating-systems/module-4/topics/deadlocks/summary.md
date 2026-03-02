# Deadlocks - Summary

## Key Definitions and Concepts

- **Deadlock**: System state where processes wait indefinitely for resources held by others
- **Coffman Conditions**:
  - _Mutual Exclusion_: Resource non-sharable
  - _Hold & Wait_: Process holds resource while waiting for others
  - _No Preemption_: Resources cannot be forcibly removed
  - _Circular Wait_: Circular chain of processes waiting for resources
- **Handling Strategies**:
  - _Prevention_: Design system to exclude 1+ Coffman conditions
  - _Avoidance_: Use algorithms (Banker's) to predict safe states
  - _Detection_: Periodically check for deadlocks using resource graphs/algorithms
  - _Recovery_: Process termination/resource preemption

## Important Formulas and Theorems

```markdown
1. **Safety Algorithm** (Banker's Algorithm):
   - Let Work = Available
   - Finish[i] = false for all i
   - Find i where Finish[i] = false and Need[i] ≤ Work
   - If no such i exists, system is safe iff all Finish[i] = true

2. Resource Allocation Equations:
   - Max_Need[i] = Allocation[i] + Remaining_Need[i]
   - Available ≥ Request[i] → Grant request (temporarily)
```

## Key Points

1. Deadlocks require **all four Coffman conditions** simultaneously
2. **Prevention methods**:
   - Eliminate Mutual Exclusion (impractical for physical resources)
   - Require full resource allocation upfront (negates Hold & Wait)
3. **Banker's Algorithm** uses:
   - Max matrix (total resources needed)
   - Allocation matrix (currently held)
   - Need matrix (remaining requirements)
4. **Deadlock Avoidance** requires resource ordering and safe sequence verification
5. **Detection Methods**:
   - Single Instance: Use wait-for graphs
   - Multiple Instances: Use Banker's-like detection algorithm
6. **Recovery Options**:
   - Process Termination (abort all/some)
   - Resource Preemption (rollback/starve victim process)
7. Practical systems often use **detection+recovery** due to prevention/avoidance overhead

## Common Mistakes to Avoid

1. Confusing **prevention** (design-time) with **avoidance** (runtime)
2. Assuming deadlocks occur when only 3 Coffman conditions exist
3. Forgetting to update **Available** matrix after temporary resource allocation in Banker's algorithm
4. Missing circular waits in complex resource graphs

## Revision Tips

1. **Memorize Coffman conditions** using acronym "M-H-N-C" (Mutual, Hold, No preemption, Circular)
2. **Practice Banker's Algorithm** with 3+ process examples (common in exams)
3. **Compare strategies** using:
   - Prevention: High overhead but guaranteed safety
   - Avoidance: Flexible but needs advance resource knowledge
   - Detection: Practical but recovery is costly
4. **Draw resource allocation graphs** for detection scenarios - circles for processes, boxes for resources, arrows for allocations/requests
