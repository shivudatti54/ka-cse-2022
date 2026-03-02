# ICT Technical Measures for Green IT and Sustainability - Summary

## Key Definitions and Concepts

- **ICT Technical Measures**: Systematic approaches and technologies designed to minimize environmental footprint of IT infrastructure
- **Green IT**: Practice of using technology resources efficiently while minimizing environmental impact
- **PUE (Power Usage Effectiveness)**: Metric measuring data center energy efficiency; PUE = Total Facility Energy / IT Equipment Energy
- **Virtualization**: Technology allowing multiple virtual machines to run on single physical hardware
- **DVFS (Dynamic Voltage and Frequency Scaling)**: Processor technique reducing power by lowering voltage/frequency during low workload
- **LCA (Lifecycle Assessment)**: Evaluation of environmental impacts across all product lifecycle stages
- **Energy-Efficient Ethernet (EEE)**: Network standard reducing power during idle periods

## Important Formulas and Theorems

- **PUE Calculation**: PUE = Total Facility Energy (kW) / IT Equipment Energy (kW)
- **Energy Savings from Virtualization**: (Original Servers × Original Power) - (New Servers × New Power × Utilization)
- **Annual Energy**: Power (kW) × Hours per Year (8760)
- **Carbon Footprint**: Energy Consumption (kWh) × Carbon Emission Factor (kg CO2/kWh)

## Key Points

1. Server virtualization can improve utilization rates from 5-15% to 60-80%, dramatically reducing hardware requirements.

2. Hot aisle/cold aisle containment is a critical data center cooling technique that significantly improves efficiency.

3. SSDs consume 50-70% less power than traditional HDDs due to absence of moving parts.

4. Ideal PUE is 1.0; modern optimized data centers achieve PUE between 1.1 and 1.4.

5. Green coding practices include algorithm optimization, lazy loading, efficient caching, and reducing network calls.

6. Energy Star certification requires computers to consume less than 50W in sleep mode.

7. Lifecycle Assessment covers five stages: raw material extraction, manufacturing, transportation, use, and end-of-life.

8. Cloud computing enables better resource utilization through multi-tenant pooling compared to individual deployments.

## Common Mistakes to Avoid

1. **Confusing PUE direction**: Remember - lower PUE is better; PUE of 1.2 is more efficient than 1.5.

2. **Ignoring idle power consumption**: Servers consume 60-70% of peak power even when idle; virtualization addresses this.

3. **Overlooking cooling costs**: For every 1W of IT power, 0.5-1W is needed for cooling in traditional data centers.

4. **Forgetting software impact**: Software inefficiency can cause 20-30% higher energy consumption than necessary.

## Revision Tips

1. Practice PUE calculations with different scenarios to master the formula.

2. Remember the three main virtualization benefits: consolidation, utilization improvement, and cooling reduction.

3. Review the five stages of Lifecycle Assessment for e-waste questions.

4. Understand the relationship between power management features and energy savings.

5. Focus on the difference between sleep mode, hibernation, and shutdown power consumption levels.
