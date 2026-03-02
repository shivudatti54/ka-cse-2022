# Different Kinds of Requirements and Measurements - Summary

## Key Definitions and Concepts

- **Functional Requirements**: What the system must do—specific functions, services, and operations the system must support.
- **Non-Functional Requirements**: Quality attributes defining how the system performs—performance, scalability, availability, reliability, and security.
- **Business Requirements**: Organizational goals and objectives that IT systems must support, including growth projections and budget constraints.
- **Technical Requirements**: Technological specifications and standards that constrain the IT infrastructure.
- **Workload Characterization**: Process of identifying and measuring demands placed on IT resources.
- **Baseline**: Reference measurement of normal system behavior under typical conditions.
- **Threshold**: Predefined limit that triggers alert or action when exceeded.

## Important Formulas and Theorems

- **Availability Percentage** = MTBF / (MTBF + MTTR) × 100
- **MTBF** = Total Operational Time / Number of Failures
- **MTTR** = Total Downtime / Number of Failures
- **Weighted Average** = Σ(weight_i × value_i) for mixed workloads

## Key Points

- Capacity planning requires understanding all four requirement types to make informed infrastructure decisions.
- Non-functional requirements often become the basis for SLA commitments and threshold definitions.
- Baseline measurements are essential reference points for identifying capacity issues.
- Standard warning thresholds: CPU at 70%, Memory at 80%, Disk at 75%.
- Standard critical thresholds: CPU at 85%, Memory at 90%, Disk at 90%.
- Workload characterization helps predict resource needs for different transaction types.
- Business growth requirements directly influence long-term capacity planning.
- Availability requirements determine redundancy and fault tolerance design.
- Performance measurements (response time, throughput) must align with business service levels.
- Regular measurement collection establishes patterns for accurate forecasting.

## Common Mistakes to Avoid

- Confusing functional requirements with non-functional requirements—functional describes "what," non-functional describes "how well."
- Setting thresholds too high or too low without considering business impact and normal variation.
- Using single-point measurements instead of averaging over representative time periods.
- Ignoring growth projections when establishing baseline capacity.
- Treating all workloads identically—batch and interactive workloads have different characteristics.
- Overlooking technical requirements that may constrain capacity options.

## Revision Tips

1. Create a comparison table distinguishing the four requirement types with examples.
2. Practice calculating availability using different MTBF and MTTR scenarios.
3. Remember threshold percentages: 70%/80%/85%/90%—associate each with specific resources.
4. Understand that requirements cascade—business requirements drive non-functional requirements, which drive technical requirements.
5. Review real-world case studies of capacity planning failures caused by inadequate requirement analysis.
