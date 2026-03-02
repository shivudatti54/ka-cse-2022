# Direct Effects of Sustainability During Use - Summary

## Key Definitions and Concepts

- **Direct Effects:** Environmental impacts occurring during the operational/use phase of IT systems, primarily through energy consumption
- **Green IT:** The study and practice of using computing resources efficiently while minimizing environmental impact
- **ACPI States:** Advanced Configuration and Power Interface defines power states from S0 (working) to S5 (soft off)
- **PUE (Power Usage Effectiveness):** Data center efficiency metric = Total Facility Energy / IT Equipment Energy (ideal: 1.0)
- **Virtualization:** Technology allowing multiple virtual machines to run on reduced physical hardware

## Important Formulas and Theorems

- **PUE Calculation:** PUE = Total Facility Energy ÷ IT Equipment Energy
- **DCiE:** (1 ÷ PUE) × 100 (expressed as percentage)
- **Energy Consumption:** Power (kW) × Time (hours) = Energy (kWh)
- **Carbon Footprint:** Energy (kWh) × Grid Emission Factor (kg CO2/kWh) = CO2 Emissions
- **Energy Savings Percentage:** ((Before - After) ÷ Before) × 100

## Key Points

1. The use phase accounts for 50-80% of IT equipment's total carbon footprint, making it the most significant phase for sustainability interventions.

2. ACPI power states (S0-S5) provide systematic approaches to reducing power consumption: S0 is full power, S3 is standby/suspend to RAM, and S5 is soft off.

3. Server virtualization can achieve 50-80% energy reduction by improving utilization rates from typical 15% to 60%+ and enabling dynamic power management.

4. ENERGY STAR certification focuses on energy efficiency during use, while EPEAT provides broader environmental assessment.

5. Software algorithmic efficiency has greater impact on energy consumption than hardware optimization—aO(n) algorithm will almost always outperform O(n²) regardless of hardware.

6. Cloud computing improves resource utilization through multi-tenancy and dynamic scaling but concentrates energy use in data centers with varying carbon intensities.

7. The Green Grid metrics (PUE, DCiE, CUE, WUE) provide standardized ways to measure and compare data center sustainability performance.

8. Simple power management configurations on end-user devices can achieve 70-80% energy reduction through strategic use of sleep states.

## Common Mistakes to Avoid

1. **Confusing direct and indirect effects:** Direct effects occur during use (energy consumption), while indirect effects include manufacturing supply chain and end-of-life disposal.

2. **Ignoring idle power consumption:** Many devices consume significant power even when not actively performing tasks—always consider idle and sleep power in calculations.

3. **Overlooking software efficiency:** Hardware-focused approaches without considering algorithmic efficiency often yield minimal improvements compared to software optimization.

4. **Misunderstanding PUE:** Remember that PUE greater than 1.0 is normal; lower values indicate better efficiency, with 1.1-1.4 representing modern efficient data centers.

## Revision Tips

1. Create a comparison table of ACPI states (S0-S5) with power consumption levels and use cases.

2. Practice PUE and energy savings calculations with different scenarios to build confidence.

3. Memorize the key Green Grid metrics and their formulas before the exam.

4. Review real-world examples of virtualization implementations and their documented energy savings.

5. Focus on understanding the relationship between software efficiency and energy consumption—this connects programming knowledge to sustainability concepts.
