# Capacity Planning in IT Infrastructure

## Table of Contents

- [Capacity Planning in IT Infrastructure](#capacity-planning-in-it-infrastructure)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Capacity](#definition-of-capacity)
  - [Types of Capacity in IT Systems](#types-of-capacity-in-it-systems)
  - [Capacity Planning vs Capacity Management](#capacity-planning-vs-capacity-management)
  - [Capacity Planning Lifecycle](#capacity-planning-lifecycle)
  - [Workload Characterization](#workload-characterization)
  - [Capacity Planning Techniques](#capacity-planning-techniques)
  - [Baseline and Benchmarking](#baseline-and-benchmarking)
- [Examples](#examples)
  - [Example 1: Web Server Capacity Planning](#example-1-web-server-capacity-planning)
  - [Example 2: Database Storage Capacity Calculation](#example-2-database-storage-capacity-calculation)
  - [Example 3: Network Bandwidth Planning](#example-3-network-bandwidth-planning)
- [Exam Tips](#exam-tips)

## Introduction

Capacity planning is a critical function in IT service management that ensures an organization's technology infrastructure can meet current and future business requirements. In the context of the university's curriculum, capacity planning represents one of the fundamental pillars of IT service management alongside availability planning, continuity planning, and service level management.

The importance of capacity planning cannot be overstated in modern enterprise environments. As businesses become increasingly digital and dependent on technology, the need to properly size IT resources—servers, storage, network bandwidth, and processing power—becomes essential for maintaining service quality while controlling costs. Poor capacity planning leads to either under-provisioning, which causes service degradation and business loss, or over-provisioning, which results in unnecessary capital expenditure and operational waste.

This module focuses on understanding capacity as a core concept, exploring various types of capacities in IT systems, and examining the methodologies used to measure, analyze, and plan for capacity requirements. The knowledge gained from this topic is directly applicable to real-world scenarios where IT professionals must make informed decisions about infrastructure investments and resource allocation.

## Key Concepts

### Definition of Capacity

Capacity refers to the maximum amount of work that an IT resource or system can handle within a specified time period. In IT infrastructure context, capacity is measured in terms of throughput—the volume of work a system can process per unit of time. For example, a server's processing capacity might be measured in transactions per second (TPS), while storage capacity is measured in bytes (GB, TB, PB).

The concept of capacity extends beyond simple physical limits. It encompasses the overall capability of IT components to deliver services effectively. Understanding capacity requires analyzing both the theoretical maximum (raw capacity) and the practical effective capacity considering real-world constraints like maintenance windows, redundancy requirements, and peak load handling.

### Types of Capacity in IT Systems

**Processing Capacity:** This relates to the computational capability of servers and CPUs. Processing capacity is typically measured in millions of instructions per second (MIPS), floating-point operations per second (FLOPS), or more practically in transactions per second for database systems. Modern multi-core processors have complicated traditional capacity calculations, as processing capacity now depends on the number of cores, clock speed, and the application's ability to utilize parallel processing.

**Storage Capacity:** This refers to the amount of data that can be stored in disk drives, solid-state drives, and backup media. Storage capacity planning must consider not just current data volumes but also growth rates, retention requirements, and backup storage needs. The distinction between raw storage (physical disk capacity) and usable storage (after RAID overhead, formatting, and reserved space) is crucial for accurate planning.

**Network Capacity:** Network bandwidth determines how much data can be transmitted between systems. Capacity planning for networks must account for peak traffic loads, growth trends, and quality of service requirements. Network capacity is measured in bits per second (bps) and encompasses local area networks (LAN), wide area networks (WAN), and internet connectivity.

**Memory Capacity:** RAM capacity directly impacts a system's ability to handle concurrent users and process large datasets efficiently. Memory capacity planning requires understanding application memory requirements, operating system needs, and caching behaviors. Insufficient memory leads to excessive paging, severely degrading performance.

### Capacity Planning vs Capacity Management

While these terms are often used interchangeably, they represent distinct but related concepts in IT service management.

Capacity Planning is the strategic activity of predicting future capacity requirements and planning accordingly. It involves forecasting based on business growth projections, technology trends, and historical data. Capacity planning typically considers time horizons of months to years and focuses on major infrastructure changes.

Capacity Management is the operational function that monitors and optimizes the use of existing capacity on a day-to-day basis. It involves continuous monitoring, tuning, and minor adjustments to ensure resources are utilized efficiently. Capacity management operates on shorter timeframes—daily, weekly, or monthly.

### Capacity Planning Lifecycle

The capacity planning lifecycle consists of several interconnected phases:

**Business Capacity Planning:** This top-level activity translates business requirements into IT capacity needs. It involves understanding business growth plans, new service launches, seasonal variations, and strategic initiatives that will impact IT demand.

**Service Capacity Planning:** This focuses on individual IT services and their capacity requirements. Service capacity planning ensures each service has adequate resources to meet its service level agreements (SLAs) and performance targets.

**Resource Capacity Planning:** This detailed level examines specific infrastructure components—servers, storage arrays, network devices—and determines their required specifications and quantities.

### Workload Characterization

Understanding workload characteristics is fundamental to effective capacity planning. Workloads can be categorized in several ways:

**CPU-Bound Workloads:** Applications that primarily consume processor resources. Scientific simulations, encryption operations, and certain database queries fall into this category. Planning for CPU-bound workloads requires focusing on processor speed, core count, and instruction-level parallelism.

**I/O-Bound Workloads:** Applications that spend significant time waiting for disk or network operations. Database systems with complex queries, file servers, and streaming applications are typically I/O-bound. Planning requires attention to storage subsystem performance, including disk type, RAID configuration, and caching strategies.

**Memory-Bound Workloads:** Applications that require large amounts of RAM. In-memory databases, big data processing frameworks, and applications with large caches fall into this category. Capacity planning must ensure adequate RAM to avoid costly disk paging.

**Network-Bound Workloads:** Applications limited by network bandwidth. Video streaming, large data transfers, and distributed applications often fall into this category. Planning focuses on network infrastructure bandwidth and latency.

### Capacity Planning Techniques

**Trend Analysis:** This technique uses historical data to identify patterns and project future requirements. Linear regression, moving averages, and exponential smoothing are common statistical methods used in trend analysis. The accuracy of trend analysis depends heavily on data quality and the stability of underlying patterns.

**Benchmarking:** This approach uses standardized tests to establish baseline performance and compare different system configurations. Benchmarks provide reference points for capacity planning but must be applied carefully, as real-world workloads often differ significantly from benchmark workloads.

**Modeling and Simulation:** Mathematical models represent system behavior and allow planners to simulate various scenarios without actually implementing them. Queuing theory models, for example, can predict response times and queue lengths under different load conditions.

**Threshold-Based Planning:** This approach establishes utilization thresholds (such as 70% CPU utilization) and triggers capacity additions when thresholds are exceeded. While simple to implement, threshold-based planning is reactive and may result in delayed responses to capacity needs.

### Baseline and Benchmarking

Establishing performance baselines is essential for capacity planning. A baseline represents the normal, expected performance level under typical operating conditions. Baselines are established through continuous monitoring over a representative period and serve as reference points for detecting anomalies and planning improvements.

Benchmarking complements baseline establishment by providing standardized performance measurements. Common benchmarks include SPEC CPU for processor performance, TPC-C for database transaction processing, and SPECpower_ssj2008 for server power efficiency. When using benchmarks, it's important to select benchmarks that closely match the actual workload characteristics.

## Examples

### Example 1: Web Server Capacity Planning

**Problem:** A company expects its e-commerce website to handle 10,000 concurrent users during peak season, with each user session requiring approximately 2 MB of memory and generating 5 requests per minute. Currently, each web server can handle 500 concurrent users. Determine the number of web servers required and total memory needed.

**Solution:**

Step 1: Calculate required servers

- Current capacity per server = 500 concurrent users
- Required concurrent users = 10,000
- Required servers = 10,000 ÷ 500 = 20 servers

Step 2: Calculate memory requirements

- Memory per user session = 2 MB
- Total concurrent users = 10,000
- Total memory = 10,000 × 2 MB = 20,000 MB = approximately 20 GB per server

Step 3: Include buffer for redundancy

- With 20% buffer: 20 × 1.2 = 24 servers
- Total memory with buffer: 24 × 20 GB = 480 GB

**Answer:** Minimum 24 web servers with 20 GB RAM each (480 GB total) to handle the projected load with redundancy.

### Example 2: Database Storage Capacity Calculation

**Problem:** A database currently stores 500 GB of data with a monthly growth rate of 10%. The organization requires 3 years of retention and wants to maintain 30% spare capacity for performance. Calculate the required storage capacity.

**Solution:**

Step 1: Calculate data growth over 3 years

- Month 1: 500 GB × 1.10 = 550 GB
- After 36 months: 500 × (1.10)^36 = 500 × 35.95 = 17,975 GB

Step 2: Calculate required capacity with buffer

- Required storage = 17,975 GB × 1.30 (30% spare) = 23,367.5 GB

Step 3: Convert to practical units

- 23,367.5 GB ≈ 23.4 TB

**Answer:** Approximately 24 TB of storage capacity should be provisioned to meet 3-year requirements with appropriate buffer.

### Example 3: Network Bandwidth Planning

**Problem:** An enterprise application has 1,000 users. Each user generates on average 10 network requests per minute, with each request averaging 50 KB in size. Calculate the required network bandwidth in Mbps, assuming a peak factor of 3× and 20% overhead.

**Solution:**

Step 1: Calculate average bandwidth requirement

- Total requests per minute = 1,000 × 10 = 10,000 requests
- Data per minute = 10,000 × 50 KB = 500,000 KB = approximately 488 MB
- Bandwidth in MB/min = 488 MB ÷ 60 = 8.13 MB/s
- In Mbps: 8.13 × 8 = 65 Mbps

Step 2: Apply peak factor

- Peak bandwidth = 65 × 3 = 195 Mbps

Step 3: Add overhead

- With 20% overhead: 195 × 1.20 = 234 Mbps

**Answer:** Approximately 250 Mbps network bandwidth is required to handle peak traffic with overhead.

## Exam Tips

1. **Understand the Difference:** Remember that capacity planning is about future needs (strategic), while capacity management is about current utilization (operational). This distinction frequently appears in exam questions.

2. **Know the Types:** Be familiar with all types of capacity—processing, storage, network, and memory—and their respective measurement units. university exams often test understanding of which capacity type applies to different scenarios.

3. **Workload Characterization is Key:** Always identify whether a workload is CPU-bound, I/O-bound, memory-bound, or network-bound before planning capacity. This determines where bottlenecks will occur.

4. **Buffer and Redundancy:** Always include safety margins (typically 20-30%) in capacity calculations for redundancy and unexpected growth. Never plan exactly at 100% utilization.

5. **Formulas Matter:** Memorize key formulas for throughput calculation, storage growth projection using compound growth rate, and network bandwidth calculations.

6. **Lifecycle Phases:** Remember the three levels of capacity planning—business capacity planning, service capacity planning, and resource capacity planning—from strategic to tactical.

7. **Baseline Importance:** Understand that baselines represent normal operations and are essential for detecting anomalies and planning improvements. Never skip baseline establishment in capacity planning processes.

8. **Time Horizons:** Capacity planning typically considers longer timeframes (months to years) compared to capacity management (daily to weekly monitoring).

9. **Growth Projections:** When calculating future capacity needs, use appropriate growth models. Compound growth (exponential) is common for storage and data-intensive applications.

10. **Real-World Application:** Many exam questions present scenarios requiring you to calculate required resources given user counts, request rates, and resource consumption per user. Practice such problems thoroughly.
