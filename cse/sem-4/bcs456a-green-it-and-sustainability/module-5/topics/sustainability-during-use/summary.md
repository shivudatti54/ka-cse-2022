# Sustainability During Use - Summary

## Key Definitions and Concepts

- **Sustainability During Use**: Practices and technologies that minimize environmental impact of IT systems during their operational lifecycle
- **Dynamic Voltage and Frequency Scaling (DVFS)**: CPU technique that reduces voltage and clock speed during low workloads to save energy
- **ACPI (Advanced Configuration and Power Interface)**: Standard enabling OS control of hardware power states (C-states for sleep, P-states for performance)
- **Virtualization**: Technology running multiple virtual machines on single physical hardware to improve utilization
- **PUE (Power Usage Effectiveness)**: Ratio of total facility energy to IT equipment energy; lower is better
- **Energy Star**: International certification for energy-efficient electronic equipment
- **EPEAT**: Environmental rating system for electronic products based on 51 criteria
- **Hot/Cold Aisle Containment**: Data center cooling technique preventing air mixing

## Important Formulas and Theorems

- **PUE = Total Facility Energy / IT Equipment Energy**
- **CPU Power Consumption ∝ Frequency × Voltage²** (explains why DVFS is so effective)
- **Energy Savings % = (Original Energy - New Energy) / Original Energy × 100**
- **Server Consolidation Ratio = Physical Servers / Virtual Servers**
- **Annual Energy (kWh) = Power (kW) × Hours per Year**

## Key Points

- The use phase often accounts for the largest portion of IT systems' environmental impact over their lifetime
- Virtualization can improve server utilization from 5-15% to 60-80%, reducing physical server count and energy consumption
- Modern green data centers achieve PUE values of 1.1-1.4 compared to 2.0-3.0 for older facilities
- DVFS saves significant energy because power consumption is proportional to the square of voltage
- ACPI defines multiple sleep states: S3 (suspend-to-RAM) and S4 (hibernate) are most common for energy savings
- Energy Star certified products consume 20-30% less energy than standard products
- Green software development focuses on algorithmic efficiency, reduced computational overhead, and power-aware coding
- Sleep modes can reduce laptop power consumption by over 50% during idle periods

## Common Mistakes to Avoid

- Confusing PUE values: Remember lower PUE is better (closer to 1.0 indicates efficiency)
- Misunderstanding C-states vs P-states: C-states are sleep/idle states, P-states are performance/throttling states
- Forgetting virtualization overhead: Virtual machines consume approximately 10% additional overhead for hypervisor operations
- Overlooking cooling energy: Data center cooling can consume 30-40% of total facility energy
- Assuming energy savings are linear: Power management benefits depend heavily on actual utilization patterns

## Revision Tips

- Practice calculating PUE with different scenarios to fully understand the metric
- Memorize the relationship between CPU voltage, frequency, and power consumption
- Remember the typical server utilization rates before and after virtualization
- Review Energy Star and EPEAT certification criteria as they frequently appear in exams
- Focus on understanding practical applications rather than just definitions
- Practice solving numerical problems involving energy consumption and savings calculations
