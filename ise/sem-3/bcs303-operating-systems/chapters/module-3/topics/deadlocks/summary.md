# Deadlocks - Summary

## Key Definitions and Concepts

A DEADLOCK is a state where two or more processes are permanently blocked, each waiting for resources held by others. The four Coffman conditions necessary for deadlock are mutual exclusion, hold and wait, no preemption, and circular wait. A SAFE STATE exists when there is at least one execution sequence that allows all processes to complete without deadlock. The RESOURCE ALLOCATION GRAPH is a directed graph with process and resource nodes showing request and assignment edges.

## Important Formulas and Theorems

Need = Maximum Demand - Allocation
Work = Available (working vector)
Safety Check: Need(i) ≤ Work for some process i
Banker's Algorithm Safety: Find sequence where all processes can complete
Resource Request Grant Condition: Request ≤ Need AND Request ≤ Available

## Key Points

- Deadlock involves processes holding resources while waiting for additional resources
- All four Coffman conditions must hold simultaneously for deadlock to occur
- Prevention eliminates one Coffman condition; avoidance uses advance information
- The Banker's Algorithm ensures safe state before granting resource requests
- Detection allows deadlocks but recovers after identification
- Resource allocation graph cycles indicate potential deadlock with single instances
- Circular wait can be prevented by imposing total resource ordering
- Process termination and resource preemption are common recovery strategies

## Common Mistakes to Avoid

Students often confuse deadlock prevention with deadlock avoidance. Prevention removes one Coffman condition at design time, while avoidance dynamically checks safety before allocation. Another common error is assuming that any cycle in the resource allocation graph guarantees deadlock; cycles only indicate potential deadlock with single resource instances. Many students also forget that the Banker's Algorithm requires knowledge of maximum resource needs in advance.

## Revision Tips

Practice at least three full problems of the Banker's Algorithm including safety checks and resource request processing. Draw resource allocation graphs for various scenarios and identify cycles. Memorize the four Coffman conditions and think about how each prevention strategy eliminates one condition. Review the difference between safe and unsafe states, remembering that unsafe states may or may not lead to deadlock.