# Data Warehouses and Data Marts: An Introduction

For  Engineering Students, Semester V - Data Warehousing, Module 1

## Introduction

In the modern enterprise, data is generated from myriad sources: transactional systems, customer relationship management (CRM) software, social media, sensors, and more. While these Operational Systems (OLTP - Online Transaction Processing) are excellent for day-to-day operations, they are poorly suited for complex analysis and reporting. This is where **Data Warehouses** and **Data Marts** come into play. They form the backbone of Business Intelligence (BI), providing a consolidated, historical, and analysis-ready view of an organization's data.

## Core Concepts

### 1. Data Warehouse (DW)

A Data Warehouse is a **subject-oriented, integrated, time-variant, and non-volatile** collection of data in support of management's decision-making process. This classic definition by Bill Inmon captures its essence:

*   **Subject-Oriented:** Data is organized around key subjects of the business, such as customers, products, sales, or suppliers, rather than specific applications or processes (e.g., invoicing or inventory). This allows for analysis focused on these core entities.
*   **Integrated:** The DW integrates data from multiple, heterogeneous source systems (e.g., Oracle, SQL Server, flat files). During the ETL (Extract, Transform, Load) process, inconsistencies are resolved—data is cleaned, standardized, and transformed into a unified format.
*   **Time-Variant:** Unlike operational systems that primarily store current data, a DW stores historical data. It can contain data from five, ten, or more years, enabling trend analysis, forecasting, and year-over-year comparisons.
*   **Non-Volatile:** Once data is entered into the warehouse, it is not updated or deleted in the traditional sense. New data is appended, but the old data remains, creating a stable historical record. This is crucial for accurate analysis.

**Example:** A university might have separate systems for student registration, course management, and finance. A Data Warehouse would integrate data from all these sources to analyze questions like: "What is the average grade trend for students who took 'Advanced Calculus' before 'Data Structures' over the last five years?"

### 2. Data Mart

A Data Mart is a **subset of a data warehouse** (or a focused, standalone repository) designed to serve the specific needs of a particular department, team, or line of business. It is often seen as a smaller, more agile version of a data warehouse.

*   **Scope:** While a data warehouse is enterprise-wide, a data mart has a limited scope (e.g., a Data Mart for the Finance department, the Marketing team, or the Sales division).
*   **Data:** It contains summarized and detailed data related to a specific subject area.
*   **Advantages:**
    *   **Faster Implementation:** Cheaper and quicker to build as they deal with a smaller dataset.
    *   **Improved Performance:** Queries are faster because they search through less data.
    *   **Departmental Focus:** Tailored to the specific analytical needs of a user group.

**Types of Data Marts:**
*   **Dependent Data Mart:** Populated directly from the enterprise data warehouse. This ensures consistency and a single version of the truth.
*   **Independent Data Mart:** Created directly from operational sources without a data warehouse. This can lead to data silos and inconsistency but is faster to deploy.

**Example:** The Sales department doesn't need all the integrated financial and HR data from the full warehouse. They need a Data Mart focused on sales figures, customer demographics, and product performance to create their quarterly reports and forecasts.

### Relationship Between Data Warehouse and Data Marts

The relationship is often hierarchical. An enterprise builds a central, integrated **Data Warehouse** as the single source of truth. From this large repository, smaller, department-specific **Dependent Data Marts** are created through further summarization and selection. This top-down approach maintains data consistency across the organization.

An alternative bottom-up approach, advocated by Ralph Kimball, involves building individual Data Marts first and then integrating them into a larger data warehouse structure.

## Key Points & Summary

| Feature | Data Warehouse | Data Mart |
| :--- | :--- | :--- |
| **Scope** | Enterprise-wide | Department-specific |
| **Subject** | Multiple subjects | Single, specific subject |
| **Data Source** | Multiple heterogeneous sources | Fewer sources, often a DW |
| **Size** | Large (GBs to TBs to PBs) | Small (MBs to GBs) |
| **Implementation Time** | Months to years | Weeks to months |

*   **Purpose:** Both are used for **Online Analytical Processing (OLAP)**, enabling complex queries, data mining, and decision support, as opposed to OLTP systems designed for transactions.
*   **The Goal:** The ultimate goal of both is to turn raw data into meaningful information for strategic decision-making.
*   **Design Approach:** The enterprise data warehouse serves as the foundational, integrated layer, while data marts provide tailored, accessible data for business users.

**In conclusion,** a Data Warehouse is the central repository for an organization's historical data, designed for enterprise-level analysis. Data Marts are smaller, focused subsets that provide departmental users with quick and easy access to the specific data they need. Together, they form a critical architecture for any robust Business Intelligence strategy.