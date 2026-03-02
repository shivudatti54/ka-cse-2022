# Quick and Dirty Math in IT Capacity Planning - Summary

## Key Definitions and Concepts

- **Quick and Dirty Math**: Back-of-the-envelope or rough order of magnitude (ROM) calculations used for rapid capacity estimation without detailed analysis
- **Little's Law**: Fundamental queuing formula L = λ × W, relating average number in system (L), arrival rate (λ), and wait time (W)
- **Utilization (ρ)**: The proportion of time a resource is busy, typically expressed as a decimal or percentage
- **Order of Magnitude**: A factor of 10 used for approximate estimates when precise calculations aren't feasible
- **Pareto Principle (80/20 Rule)**: The observation that approximately 80% of effects come from 20% of causes

## Important Formulas and Theorems

1. **Little's Law**: L = λ × W (Number in system = Arrival rate × Residence time)

2. **Utilization-Response Time Relationship**: Response Time Factor = 1 / (1 - ρ)

- At 50% utilization: response is 2× service time
- At 80% utilization: response is 5× service time
- At 90% utilization: response is 10× service time

3. **Capacity Estimation**: Total Capacity = (Requests per second) × (Service time per request)

4. **Scaling Factor**: New Capacity ≈ Old Capacity × (New Resources / Old Resources)

## Key Points

- Quick estimation techniques provide rapid insights without requiring extensive data collection or specialized tools
- Little's Law is fundamental to understanding system behavior and predicting concurrent user capacity
- Response time grows exponentially as utilization approaches 100%, making high utilization unsustainable
- Order of magnitude thinking (powers of 10) helps determine feasibility when exact answers aren't needed
- The 80/20 rule helps identify critical workloads that contribute most to resource consumption
- Always apply safety margins (typically 1.5x to 2x) when making capacity recommendations
- Quick math is appropriate for initial estimates and sanity checks, but detailed analysis is needed for final decisions

## Common Mistakes to Avoid

1. **Ignoring utilization thresholds**: Running systems at high utilization (>80%) without understanding performance degradation
2. **Linear extrapolation errors**: Assuming systems scale linearly when they often exhibit non-linear behavior
3. **Forgetting safety margins**: Making capacity recommendations without accounting for peak loads and growth
4. **Unit conversion errors**: Mixing milliseconds, seconds, and minutes in calculations

## Revision Tips

1. Practice Little's Law calculations until you can apply them instantly—rearrange the formula for all three variables
2. Memorize key utilization-response time relationships (50%, 80%, 90% utilization impact)
3. Remember standard rules of thumb for CPU, memory, disk I/O, and network capacity
4. Always verify your quick estimates against known system constraints before making recommendations
5. Use the "three numbers" sanity test: concurrent users × request size × response time ≈ resource requirement
