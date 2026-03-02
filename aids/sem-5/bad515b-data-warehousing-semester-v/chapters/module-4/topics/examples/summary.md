# Examples of Dimensional Modelling - Summary

## Key Definitions and Concepts

- **Dimensional Modelling**: A technique for organizing data in a data warehouse that optimizes for query performance and business user understanding.
- **Star Schema**: A dimensional model with a central fact table surrounded by denormalized dimension tables, forming a star-like structure.
- **Fact Table**: The central table containing measurable business metrics (facts) and foreign keys to dimension tables.
- **Dimension Table**: Contains descriptive attributes used for filtering, grouping, and labeling data in reports.
- **Surrogate Key**: A system-generated unique identifier for each dimension record, preferred over natural keys.
- **Grain**: The level of detail in the fact table; defines what each row represents.
- **Slowly Changing Dimension (SCD)**: Techniques for handling changes in dimension attribute values over time.

## Important Formulas and Techniques

- Four-Step Design Process: Business Process → Grain → Dimensions → Facts
- SCD Type 1: UPDATE existing record (no history)
- SCD Type 2: INSERT new record with effective dates (full history)
- SCD Type 3: UPDATE current record and add new column (partial history)
- Fact Types: Additive (sum across all dimensions), Semi-additive (sum across some dimensions), Non-additive (ratios, percentages)

## Key Points

- Always identify the business process and define grain before designing dimensions.
- Fact tables contain numeric measurements; dimension tables contain descriptive attributes.
- Date dimension is universal and essential for every data warehouse.
- Surrogate keys are mandatory in dimension tables for tracking history.
- Star schema is preferred for query performance despite data redundancy.
- Snowflake schema normalizes dimension tables, reducing redundancy but increasing query complexity.
- Conformed dimensions can be shared across multiple business processes.
- Type 2 SCD is most common for tracking historical changes in dimension attributes.

## Common Mistakes to Avoid

- Confusing facts (measurable metrics) with dimensions (descriptive attributes).
- Using natural keys instead of surrogate keys in dimension tables.
- Defining grain too coarsely or too finely for the business requirements.
- Forgetting to include the date dimension in the design.
- Applying snowflake normalization when star schema would perform better.
- Not considering how dimension changes will be handled (SCD).

## Revision Tips

- Practice designing star schemas by identifying the four essential elements: business process, grain, dimensions, and facts.
- Memorize the standard questions: What happened? (Fact), When? (Date), Where? (Location), Who? (Customer), What? (Product).
- Review SQL queries against star schemas to understand join patterns.
- Study SCD types with concrete examples of when each should be applied.
- Compare star vs snowflake schema advantages and trade-offs.