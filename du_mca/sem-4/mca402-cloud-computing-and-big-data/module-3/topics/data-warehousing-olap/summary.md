# Data Warehousing and OLAP - Summary

## Key Definitions and Concepts

- **Data Warehouse**: A subject-oriented, integrated, time-variant, and non-volatile collection of data supporting management decision-making (Bill Inmon, 1992)

- **OLAP (Online Analytical Processing)**: Technology enabling complex analytical queries against large multidimensional datasets for business intelligence

- **Data Mart**: A departmental subset of a data warehouse focused on specific business functions

- **ETL**: Extract, Transform, Load - the process of moving data from source systems to the warehouse

- **Fact Table**: Central table in dimensional modeling containing measurable quantitative data (measures)

- **Dimension Table**: Tables containing descriptive attributes providing context to facts

## Important Formulas and Concepts

- **Data Cube**: n-dimensional representation of data with dimensions and measures
- **Star Schema**: Denormalized design with central fact table and denormalized dimension tables
- **Snowflake Schema**: Normalized extension of star schema with normalized dimension tables
- **OLAP Operations**: Roll-up (aggregation), Drill-down (detailing), Slice (1D selection), Dice (multi-dimensional selection), Pivot (rotation)

## Key Points

- Data warehouses differ from operational databases in being subject-oriented, integrated, time-variant, and non-volatile
- OLAP systems handle complex queries on historical data; OLTP handles day-to-day transactions
- Star schema provides better query performance due to fewer joins; snowflake reduces storage through normalization
- MOLAP stores data multidimensionally (fast but limited scale); ROLAP uses relational databases (scalable but slower)
- Modern cloud data warehouses (Snowflake, Redshift, BigQuery) offer elastic scaling and pay-per-use pricing

## Common Mistakes to Avoid

1. Confusing data warehouse with operational databases - warehouses are for analysis, not transactions
2. Selecting snowflake schema for simple queries where star schema would perform better
3. Neglecting data quality during ETL - garbage in, garbage out applies strongly to warehouses
4. Overlooking the importance of dimension hierarchies needed for roll-up and drill-down operations

## Revision Tips

1. Practice drawing star schemas and identifying fact/dimension tables from business scenarios
2. Memorize the four characteristics of data warehouse and write them in exam answers
3. Create a table comparing OLTP vs OLAP and MOLAP vs ROLAP vs HOLAP for quick reference
4. Solve previous year DU question papers focusing on schema design and OLAP operation identification
5. Visualize data cube operations with diagrams - they are frequently asked in visual form