# Performance and Capacity - Summary

## Key Definitions and Concepts

- **Performance**: The measure of how well a system responds to user requests, typically measured through response time, throughput, and resource utilization
- **Capacity**: The maximum workload a system can handle while maintaining acceptable performance levels
- **Response Time**: Time elapsed between user request initiation and system response completion
- **Throughput**: Number of transactions or operations processed per unit time (TPS, RPS)
- **Utilization**: Percentage of time a resource is actively processing (CPU, memory, disk, network)
- **Latency**: Delay before data transfer begins following an instruction
- **Availability**: Percentage of time system is operational (expressed in "nines")
- **Bottleneck**: Component limiting overall system performance due to resource constraints
- **Scalability**: System's ability to handle increased workload through resource addition

## Important Formulas and Theorems

- **CPU Utilization**: (Busy Time / Total Time) × 100%
- **Throughput**: Completed Transactions / Time Period
- **95th Percentile Response Time**: Mean + 1.645 × Standard Deviation (normal distribution)
- **Availability**: (Total Time - Downtime) / Total Time × 100%
- **Capacity Growth Projection**: Current Capacity × (1 + Growth Rate)^n periods

## Key Points

- Performance and capacity are interdependent - adequate capacity doesn't guarantee optimal performance
- The capacity planning lifecycle consists of four phases: Monitoring, Analysis, Modeling, and Implementation
- Vertical scaling adds resources to existing machines; horizontal scaling adds more machines
- Performance baselines represent normal operating conditions and are essential for anomaly detection
- Capacity triggers (typically 75-80% utilization) indicate when expansion becomes necessary
- Workload characterization (interactive, batch, hybrid) affects capacity planning decisions
- SLA compliance often requires 95th or 99th percentile measurements, not just averages
- Bottleneck analysis should systematically evaluate CPU, memory, disk I/O, and network

## Common Mistakes to Avoid

- Confusing performance (how well) with capacity (how much) in exam answers
- Using average response time alone for SLA compliance - always check percentiles
- Ignoring standard deviation when analyzing response time distributions
- Planning capacity only for average load without considering peak loads
- Forgetting that different workload types have different resource requirements

## Revision Tips

1. Practice calculating utilization, throughput, and percentile response times with sample data
2. Memorize the four phases of the capacity planning lifecycle in order
3. Remember that 95th percentile uses 1.645 multiplier for normal distribution calculations
4. Review the differences between vertical and horizontal scaling with examples
5. Focus on understanding bottleneck identification - the component with highest utilization limits the system
6. Know that typical capacity trigger threshold is 75-80% utilization for planning purposes
7. Review SLA compliance calculations and understand how to determine required improvements
