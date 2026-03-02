# Runtime Energy Consumption Basics - Summary

## Key Definitions and Concepts

- **Runtime Energy Consumption**: The electrical energy consumed by a system during software execution, measured in Joules (J) or Watt-hours (Wh).

- **Dynamic Power**: Power consumed during active computation due to transistor switching, proportional to the square of voltage (P ∝ V²).

- **Static Power**: Power consumed due to leakage current even when the processor is idle, becoming more significant with smaller transistor sizes.

- **Power States**: C-states (CPU idle), P-states (performance), and S-states (system sleep) manage energy consumption at different levels.

## Important Formulas and Theorems

- **Energy Equation**: E = P × t (Energy = Power × Time)

- **Dynamic Power**: P_dynamic = α × C × V² × f (switching activity × capacitance × voltage² × frequency)

- **Static Power**: P_static = I_leak × V (leakage current × voltage)

- **Energy-Delay Product (EDP)**: EDP = E × t (balances energy efficiency with performance)

## Key Points

- Runtime energy consumption is a critical component of Green IT initiatives, contributing significantly to carbon emissions.

- Voltage scaling provides quadratic power reduction, making it the most effective energy optimization technique.

- Algorithm choice directly impacts energy consumption - efficient algorithms reduce execution time and total energy use.

- Power management states allow systems to reduce energy consumption during idle or low-activity periods.

- Software optimization (code efficiency, data structures, I/O reduction) can significantly lower runtime energy consumption.

- The ICT sector accounts for 2-4% of global carbon emissions, emphasizing the importance of energy-conscious computing.

- Performance per Watt is the standard metric for evaluating energy-efficient computing systems.

## Common Mistakes to Avoid

- Confusing power (Watts) with energy (Joules) - power is rate of energy consumption, not total consumption.

- Ignoring static power consumption in modern nanometer-scale processors where leakage current is significant.

- Assuming that lower power always means better - performance trade-offs must be considered using metrics like EDP.

- Overlooking the energy consumption of peripheral devices (displays, storage, network) in total system energy calculations.

## Revision Tips

- Memorize the fundamental E = P × t equation and understand how each variable affects the result.

- Practice calculating energy consumption for different processor configurations and algorithms.

- Review power state hierarchies (C-states, P-states, S-states) as they are commonly tested in exams.

- Understand the quadratic relationship between voltage and power - this is crucial for energy optimization questions.

- Remember that green software design focuses on both algorithmic efficiency and runtime power management.
