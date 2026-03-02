# Requirements Gathering Methods for Data Warehousing

## Introduction

For  Semester V Engineering students, understanding how to gather accurate and complete requirements is the most critical first step in building a successful Data Warehouse (DW). A DW is a large, complex system that serves the entire organization. If its design is based on incomplete or incorrect requirements, it will fail to meet business needs, leading to wasted resources and poor decision-making. This module explores the formal methods used to elicit these requirements effectively.

## Core Concepts and Methods

Requirements gathering for a DW is fundamentally different from traditional software systems. The focus shifts from *process* and *function* to *data* and *analysis*. The goal is to understand **what decisions** users need to make and **what information** (data) they need to make them. Here are the primary methods used:

### 1. Interviews

This is the most common and effective technique. It involves one-on-one or small-group sessions with key stakeholders, business analysts, and subject matter experts (SMEs).

*   **How it works:** The DW designer prepares a set of open-ended questions aimed at discovering key performance indicators (KPIs), business rules, desired reports, and unresolved business questions.
*   **Example Questions:**
    *   "What are the top 3 metrics you use to measure the performance of your department?"
    *   "If you could have one new report to help you make better decisions, what would it contain?"
    *   "How do you currently combine sales data with inventory data? What challenges do you face?"
*   **Advantage:** Provides deep, qualitative insight and uncovers hidden requirements.
*   **Challenge:** Time-consuming and requires a skilled interviewer to avoid leading questions.

### 2. Surveys / Questionnaires

These are useful for collecting quantitative information from a large and geographically dispersed group of potential users.

*   **How it works:** A structured set of questions is distributed to a broad audience. Questions are often multiple-choice or based on a rating scale (e.g., "Rate the importance of daily sales reports on a scale of 1-5").
*   **Example:** Surveying all regional sales managers to rank their most needed data dimensions (e.g., by product, by region, by time period).
*   **Advantage:** Reaches a wide audience quickly and cheaply; easy to analyze results statistically.
*   **Challenge:** Lacks depth; cannot explore ambiguous answers or follow up on interesting points in real-time.

### 3. Joint Application Development (JAD) Sessions

JAD sessions are structured, facilitated workshops that bring together all key stakeholders (users, managers, IT staff, sponsors) in a single location for an intensive, focused period.

*   **How it works:** A facilitator guides the group through a predefined agenda to identify, define, prioritize, and agree upon DW requirements. The goal is to achieve consensus quickly and avoid later conflicts.
*   **Example:** A 2-day JAD session with representatives from sales, marketing, and finance to define the exact metrics and calculations for a "Customer Profitability" score.
*   **Advantage:** Speeds up the requirements process, improves communication, and builds a shared sense of ownership.
*   **Challenge:** Requires significant coordination and can be dominated by vocal participants if not well-facilitated.

### 4. Prototyping

This method involves building a small-scale, working model (a prototype) of a part of the DW, such as a sample dashboard or report.

*   **How it works:** Developers create a quick, visual mock-up based on initial assumptions. Users interact with the prototype and provide feedback on what they like, dislike, or need changed.
*   **Example:** Creating a mock-up of an executive dashboard with charts for sales revenue, customer count, and profit margin. Users might see it and realize they also need a chart for "year-over-year growth."
*   **Advantage:** Helps users visualize the final system and articulate requirements they didn't know they had. It clarifies vague requirements effectively.
*   **Challenge:** Can create unrealistic expectations about project timelines if users believe the final system is nearly complete.

### 5. Document Analysis

This technique involves reviewing existing organizational documents to source requirements.

*   **How it works:** The DW team studies existing reports, spreadsheets, forms, and legacy system documentation. These documents are a goldmine of information on current metrics, data sources, and business rules.
*   **Example:** Analyzing a monthly financial report spreadsheet to understand the formulas for calculating "Net Profit" or "Operating Expenses." This directly informs the ETL (Extract, Transform, Load) logic.
*   **Advantage:** Provides concrete, historical examples of data usage. Uncovers formal business rules.
*   **Challenge:** Documents may be outdated or may not reflect how data is *actually* used in practice.

## Key Points & Summary

*   **Foundation for Success:** Requirements gathering is the most crucial phase in DW development. A DW built on poor requirements will fail.
*   **Shift in Focus:** DW requirements focus on **information needs for decision-making**, not on process automation.
*   **Combination of Methods:** No single method is sufficient. A project should combine several techniques (e.g., Interviews + JAD + Document Analysis) for a complete picture.
*   **Stakeholder Involvement:** Continuous engagement with business users and stakeholders is non-negotiable. They are the source of truth for business needs.
*   **Iterative Process:** Requirements are rarely fully known upfront. The process is iterative, and methods like prototyping help refine them over time.

By meticulously applying these methods, engineers can ensure the resulting Data Warehouse is aligned with business strategy and becomes a valuable asset for strategic decision-making.