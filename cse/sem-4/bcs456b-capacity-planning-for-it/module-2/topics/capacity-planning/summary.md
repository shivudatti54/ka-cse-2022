# Capacity Planning in IT Infrastructure - Summary

## Key Definitions and Concepts

- **Capacity:** The maximum amount of work an IT resource or system can handle within a specified time period, measured in throughput (work per unit time).

- **Capacity Planning:** Strategic activity of predicting future capacity requirements based on business growth, trends, and historical data.

- **Capacity Management:** Operational function that monitors and optimizes existing capacity utilization on a day-to-day basis.

- **Workload:** The amount of work processed by an IT system, characterized as CPU-bound, I/O-bound, memory-bound, or network-bound.

## Important Formulas and Theorems

- **Storage Growth:** Future Capacity = Current Capacity × (1 + Growth Rate)^n where n is number of periods

- **Server Requirements:** Servers Required = Total Concurrent Users ÷ Users per Server

- **Memory Calculation:** Total Memory = Concurrent Users × Memory per User

- **Network Bandwidth:** Bandwidth (Mbps) = (Requests per Minute × Size per Request × 8) ÷ 60 × Peak Factor × Overhead Factor

## Key Points

- Capacity planning ensures IT infrastructure meets current and future business requirements while optimizing costs.

- Four main capacity types: Processing (MIPS/TPS), Storage (Bytes), Network (bps), and Memory (Bytes).

- Capacity planning is strategic and long-term; capacity management is operational and short-term.

- Workload characterization determines the bottleneck type and influences planning strategy.

- Always include 20-30% buffer for redundancy and unexpected growth in capacity calculations.

- Performance baselines establish normal operation reference points for effective planning.

- The capacity planning lifecycle operates at three levels: business, service, and resource.

## Common Mistakes to Avoid

1. Planning exactly at 100% utilization without any buffer, leading to immediate performance issues during peak loads.

2. Confusing capacity planning with capacity management—remember the strategic vs operational distinction.

3. Using inappropriate growth models (linear instead of exponential for storage data).

4. Ignoring the three levels of capacity planning and treating all planning activities the same.

5. Overlooking workload characteristics—failing to identify whether workloads are CPU, I/O, memory, or network bound.

## Revision Tips

1. Practice numerical problems on server, storage, and network capacity calculations multiple times.

2. Create a comparison table differentiating capacity planning vs capacity management, and all four workload types.

3. Memorize the three levels of capacity planning lifecycle and their purposes.

4. Review the formula for compound growth calculation as it applies to storage capacity planning.

5. Focus on understanding the practical application rather than just memorizing definitions—university exams emphasize problem-solving.
