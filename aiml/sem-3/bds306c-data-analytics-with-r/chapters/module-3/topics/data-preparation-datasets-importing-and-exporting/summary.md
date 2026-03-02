# **Data Preparation Datasets, Importing and Exporting files, Accessing Databases, Data Cleaning and Transformation**

### Chapter 3.1: Datasets

- **Definition:** A collection of data, typically in a structured format, used for analysis or other purposes.
- **Types of Datasets:**
  - **Census data:** Data collected from the population.
  - **Survey data:** Data collected through questionnaires or interviews.
  - **Experimental data:** Data collected from controlled experiments.
- **Importance:** Quality of the dataset affects the accuracy of the analysis.

### Chapter 3.2: Importing and Exporting Files

- **Importing Files:**
  - **CSV (Comma Separated Values):** Common format for datasets.
  - **Excel Files:** Can be imported into R using `read.csv()` and `read.xlsx()`.
  - **SPSS Files:** Can be imported into R using `read.spss()`.
- **Exporting Files:**
  - **CSV (Comma Separated Values):** Can be exported using `write.csv()`.
  - **Excel Files:** Can be exported using `write.xlsx()`.

### Chapter 3.3: Accessing Databases

- **Types of Databases:**
  - **Relational databases:** Store data in tables with defined relationships.
  - **NoSQL databases:** Store data in flexible, semi-structured formats.
- **Accessing Databases:**
  - **RDBMS (Relational Database Management System):** Can be accessed using `RMySQL`, `RPostgreSQL`, etc.
  - **Cloud databases:** Can be accessed using `RAmazon`, `RGoogleCloud`, etc.

### Chapter 3.4: Data Cleaning and Transformation

- **Data Cleaning:**
  - **Handling missing values:** Using `complete.cases()`, `na.omit()`, etc.
  - **Handling duplicates:** Using `duplicated()`, `unique()`, etc.
- **Data Transformation:**
  - **Data normalization:** Using `scale()`, `standardize()`, etc.
  - **Data aggregation:** Using `group_by()`, `summarise()`, etc.

### Important Formulas, Definitions, and Theorems

- **Mean:** $\bar{x} = \frac{\sum x_i}{n}$
- **Standard Deviation:** $\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}$
- **Correlation Coefficient:** $r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \sqrt{\sum (y_i - \bar{y})^2}}$

### Key Points

- Data quality affects analysis accuracy.
- Understanding dataset types and sources is crucial.
- Proper file handling is essential.
- Data cleaning and transformation are critical steps.
- Familiarity with database systems and access methods is necessary.
