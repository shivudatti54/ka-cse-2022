# Mixed Definitions in IT Capacity Planning - Summary

## Key Definitions and Concepts

- **Capacity**: Maximum sustainable throughput a system can handle (transactions per second, users supported, data transfer rates)
- **Performance**: How well a system executes functions, measured by response time and throughput
- **Throughput**: Rate of work completion, expressed as units processed per time unit
- **Response Time**: Elapsed time from request initiation to complete response receipt
- **Utilization**: Percentage of available capacity currently in use; critical threshold is 80-90%
- **Service Demand**: Total resource time required to complete one unit of work
- **Bottleneck**: Resource with highest utilization limiting overall system throughput
- **Scalability**: System's ability to handle increased workload through additional resources

## Important Formulas and Theorems

- **Utilization (ρ) = Arrival Rate (λ) / Service Rate (μ)**
- **Response Time = Service Time / (1 - Utilization)** (for simple queueing models)
- **Minimum Servers = (Arrival Rate × Service Time) / Target Utilization**
- **Growth Projection**: Future Capacity = Current Capacity × (1 + Growth Rate)^Years

## Key Points

- Capacity planning ensures IT resources meet current and future business demands
- High utilization (>80-90%) causes exponential response time increases due to queueing effects
- Bottleneck identification is critical—improving non-bottleneck resources doesn't improve overall performance
- Horizontal scalability (scaling out) adds more nodes; vertical scalability (scaling up) adds more power to existing nodes
- Workload characterization (types, arrival patterns, service demands) is fundamental to accurate capacity planning
- SLA defines contractual performance commitments; SLO provides internal safety margins
- Think time impacts concurrency—longer think times allow more users at same utilization
- Capacity growth rates should be projected from historical data combined with business forecasts

## Common Mistakes to Avoid

- Confusing capacity (how much work) with performance (how fast work completes)
- Assuming linear performance degradation with increased load—actually, degradation is exponential near capacity limits
- Neglecting to identify the bottleneck resource before planning upgrades
- Ignoring workload characteristics and assuming uniform resource demands

## Revision Tips

1. Create a vocabulary list with definitions for all key terms—exam questions often test precise terminology understanding
2. Practice calculating utilization from arrival rates and service times
3. Remember that bottleneck resources constrain entire system throughput regardless of other component capacities
4. Focus on the non-linear relationship between utilization and response time as a critical concept
5. Review how different scalability approaches (horizontal vs vertical) apply to different infrastructure scenarios
