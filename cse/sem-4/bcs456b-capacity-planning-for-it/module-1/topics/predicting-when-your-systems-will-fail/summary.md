# Predicting When Your Systems Will Fail - Summary

## Key Definitions and Concepts

- **Capacity**: Maximum workload a system can handle while maintaining acceptable performance
- **Utilization**: Percentage of total capacity currently being used (Utilization = Current Usage / Maximum Capacity × 100)
- **Threshold**: Point at which system behavior changes; warning (70-75%), critical (85-90%), failure (95-100%)
- **Workload**: Total computational work submitted to a system, including user requests, transactions, and batch jobs
- **Planning Horizon**: Time period for which capacity forecasts are made (short-term: 0-3 months, medium-term: 3-12 months, long-term: 1-5 years)

## Important Formulas and Theorems

- **CAGR (Compound Annual Growth Rate)**: CAGR = (Ending Value / Beginning Value)^(1/n) - 1
- **Linear Growth**: Future Value = Current Value + (Growth Rate × Time Period)
- **Exponential Growth**: Future Value = Current Value × (1 + Growth Rate)^Time Period
- **Time to Threshold**: Time = (Threshold Value - Current Value) / Average Growth Rate

## Key Points

1. Capacity planning is proactive—not reactive—management of IT infrastructure resources

2. Systems don't fail only at 100% utilization; performance degradation often begins at 70-80% due to contention and overhead

3. Linear growth assumes constant increase; exponential growth assumes percentage-based increase each period

4. Moving averages smooth short-term fluctuations to reveal underlying trends in utilization data

5. Always include procurement lead time in planning—never wait until systems reach capacity to order upgrades

6. Peak utilization matters more than average utilization when predicting failures

7. Different growth models suit different scenarios: linear for mature systems, exponential for rapidly growing applications

8. Safety margins of 20-30% below maximum capacity are industry best practice

## Common Mistakes to Ignore

- Assuming systems fail only at 100% utilization
- Using average utilization without considering peak loads
- Planning to use 100% of capacity before taking action
- Ignoring procurement and deployment lead times
- Applying wrong growth model (e.g., linear for exponentially growing systems)

## Revision Tips

1. Practice calculating CAGR and growth projections with different time periods

2. Memorize the threshold percentages and understand why they matter

3. Work through multiple examples of predicting time-to-failure with varying growth rates

4. Understand when to use linear vs. exponential models based on system characteristics

5. Review the relationship between planning horizon, lead time, and threshold levels
