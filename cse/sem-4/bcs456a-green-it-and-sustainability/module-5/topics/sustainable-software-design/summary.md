# Sustainable Software Design - Summary

## Key Definitions and Concepts

- **Sustainable Software Design**: Creating software applications that minimize environmental impact while maintaining functionality and performance
- **Green Computing**: The practice of designing and using computing resources efficiently
- **Carbon Awareness**: Scheduling computational tasks during periods of lower carbon intensity
- **Energy Efficiency**: Achieving desired outcomes with minimal energy consumption
- **Green Coding**: Writing code that optimizes computational resources and reduces energy usage

## Important Formulas and Metrics

- **Power Usage Effectiveness (PUE)** = Total Facility Energy / IT Equipment Energy
- **Energy per Transaction** = Total Energy Consumed / Number of Transactions
- **Carbon Intensity** = CO2 Emissions per Computational Unit
- **Time Complexity Impact**: O(n²) → O(n) reduces energy consumption by 50%+

## Key Points

1. ICT sector contributes 2-4% of global carbon emissions, making software sustainability critical

2. The four pillars of sustainable software are: energy efficiency, hardware efficiency, carbon awareness, and lifecycle sustainability

3. Algorithmic optimization—reducing time complexity—directly decreases CPU energy consumption

4. Lazy loading reduces initial data transfer by 60-80%, significantly lowering network energy usage

5. Database-level filtering is more efficient than application-level processing

6. Cloud computing enables right-sizing, virtualization, and geographic distribution for better resource utilization

7. Sustainable software design aligns with SDG 9 (Innovation) and SDG 13 (Climate Action)

8. Hardware efficiency involves matching computational needs to appropriate hardware specifications

## Common Mistakes to Avoid

1. **Ignoring algorithmic complexity**: Choosing O(n²) solutions over O(n) without justification increases energy consumption significantly

2. **Loading unnecessary data**: Fetching all records instead of using WHERE clauses wastes network bandwidth and processing energy

3. **Neglecting lazy loading**: Loading all resources immediately causes unnecessary energy consumption

4. **Forgetting hardware impact**: Inefficient software shortens hardware lifespan, increasing e-waste

## Revision Tips

1. Practice analyzing code snippets for time complexity and energy implications

2. Remember the four principles of sustainable software design for exam questions

3. Understand lazy loading, caching, and database optimization as key sustainable techniques

4. Know the relationship between algorithmic efficiency and energy consumption

5. Review how cloud computing features (virtualization, multi-tenancy) contribute to sustainability
