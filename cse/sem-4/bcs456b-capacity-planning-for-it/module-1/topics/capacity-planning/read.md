# Capacity Planning

## Table of Contents

- [Capacity Planning](#capacity-planning)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Definition and Scope of Capacity Planning](#1-definition-and-scope-of-capacity-planning)
  - [2. Types of Capacity Planning](#2-types-of-capacity-planning)
  - [3. Capacity Planning Process](#3-capacity-planning-process)
  - [4. Key Metrics in Capacity Planning](#4-key-metrics-in-capacity-planning)
  - [5. Capacity Planning Models](#5-capacity-planning-models)
  - [6. Capacity Planning versus Performance Tuning](#6-capacity-planning-versus-performance-tuning)
  - [7. Three Levels of Capacity Planning](#7-three-levels-of-capacity-planning)
- [Examples](#examples)
  - [Example 1: Web Server Capacity Planning](#example-1-web-server-capacity-planning)
  - [Example 2: Database Storage Capacity Planning](#example-2-database-storage-capacity-planning)
  - [Example 3: Network Bandwidth Capacity Planning](#example-3-network-bandwidth-capacity-planning)
- [Exam Tips](#exam-tips)

## Introduction

Capacity planning is a critical process in information technology infrastructure management that ensures an organization has the right amount of computing resources to meet current and future business demands. In the context of the university's Computer Science and Engineering curriculum, capacity planning represents one of the most important aspects of IT service management, directly impacting system performance, cost efficiency, and business continuity.

The primary objective of capacity planning is to match IT resources with business requirements in the most cost-effective manner. This involves forecasting future workload demands, analyzing current resource utilization, and making informed decisions about hardware upgrades, software licensing, and infrastructure investments. As businesses grow and technology evolves, the demand for IT resources continues to increase exponentially, making capacity planning an essential function for any modern organization.

In today's digital era, where organizations rely heavily on IT systems for their core operations, inadequate capacity planning can lead to severe consequences including system crashes, poor user experience, lost revenue, and damaged reputation. Conversely, over-provisioning results in unnecessary capital expenditure and operational costs. Therefore, achieving the right balance between under-utilization and over-utilization is the cornerstone of effective capacity planning.

## Key Concepts

### 1. Definition and Scope of Capacity Planning

Capacity planning encompasses the process of determining the IT infrastructure requirements needed to meet current and future workload demands. The scope includes various computing resources such as CPU processing power, memory (RAM), storage capacity, network bandwidth, and software licenses. The goal is to provide sufficient resources to meet service level agreements (SLAs) while minimizing costs.

### 2. Types of Capacity Planning

**Resource Capacity Planning**: This focuses on individual computing resources including processors, memory, storage devices, and network components. Resource capacity planning ensures that each component has adequate capacity to handle its assigned workload.

**Business Capacity Planning**: This type aligns IT capacity with business objectives and customer requirements. It translates business needs into technical requirements and ensures that IT investments support organizational goals.

**Service Capacity Planning**: This approach focuses on the capacity of entire IT services rather than individual components. It considers end-to-end service delivery and ensures that services meet defined performance standards.

### 3. Capacity Planning Process

The capacity planning process typically involves four major phases:

**Workload Characterization**: This initial phase involves identifying and classifying all workloads that the system must support. Workloads are categorized based on their characteristics such as CPU-intensive, I/O-intensive, or memory-intensive. Understanding workload patterns helps in accurate capacity forecasting.

**Performance Monitoring and Data Collection**: Continuous monitoring of system performance is essential for capacity planning. Key metrics include CPU utilization, memory usage, disk I/O rates, network throughput, and application response times. This data forms the foundation for capacity analysis.

**Capacity Analysis and Forecasting**: Using historical data and trend analysis, capacity analysts predict future resource requirements. Various mathematical models and forecasting techniques are employed to estimate growth patterns and peak demand periods.

**Capacity Planning Decisions**: Based on analysis results, organizations make decisions about resource procurement, upgrades, or optimization. This may involve hardware upgrades, cloud migration, load balancing implementation, or application optimization.

### 4. Key Metrics in Capacity Planning

Understanding and measuring appropriate metrics is crucial for effective capacity planning:

- **Utilization**: The percentage of available resource capacity being used
- **Throughput**: The number of transactions or requests processed per unit time
- **Response Time**: The time taken to respond to user requests
- **Availability**: The percentage of time the system is operational
- **Queue Length**: The number of requests waiting for processing
- **Saturation Point**: The resource level beyond which performance degrades significantly

### 5. Capacity Planning Models

**Linear Scaling Model**: Assumes that resources scale linearly with workload. Simple to implement but may not accurately represent complex systems.

**Queueing Theory Model**: Uses mathematical queueing theory to predict system performance under different loads. Provides more accurate predictions for systems with waiting times.

**Analytical Model**: Uses mathematical formulas and simulations to analyze system behavior. Suitable for complex distributed systems.

**Trend Analysis Model**: Uses historical data to project future requirements based on growth trends.

### 6. Capacity Planning versus Performance Tuning

It is important to distinguish between capacity planning and performance tuning:

- **Capacity Planning**: Addresses "how much" resource is needed
- **Performance Tuning**: Addresses "how efficiently" resources are being used
- Both are complementary and should be performed together for optimal results

### 7. Three Levels of Capacity Planning

**Tactical Capacity Planning**: Short-term planning covering days to months, focusing on immediate resource needs and optimization

**Strategic Capacity Planning**: Long-term planning covering months to years, focusing on major infrastructure decisions and investments

**Operational Capacity Planning**: Day-to-day planning focusing on real-time resource allocation and load balancing

## Examples

### Example 1: Web Server Capacity Planning

**Problem**: A company currently operates a web server handling 10,000 requests per day with 70% CPU utilization and 60% memory utilization. The business expects 50% growth in traffic over the next year. Determine whether the current server can handle the projected load or if upgrades are necessary.

**Solution**:

**Step 1: Current Load Analysis**

- Current requests per day: 10,000
- Expected growth: 50%
- Projected requests: 10,000 × 1.5 = 15,000 requests per day

**Step 2: Resource Utilization Projection**

- If utilization scales linearly:
- Projected CPU utilization: 70% × 1.5 = 105%
- Projected memory utilization: 60% × 1.5 = 90%

**Step 3: Analysis and Recommendation**

- CPU utilization exceeding 100% indicates the current server will be insufficient
- Memory utilization at 90% is acceptable but leaves little headroom
- Recommendation: Upgrade server CPU or add additional server for load balancing

**Step 4: Capacity Requirement Calculation**

- To handle 15,000 requests with 70% target utilization:
- Required CPU capacity: Current CPU × (15,000/10,000) × (70%/70%) = 1.5 times current
- Recommended: Either upgrade to 1.5× faster CPU or deploy two servers

### Example 2: Database Storage Capacity Planning

**Problem**: A database currently stores 500 GB of data with a growth rate of 20% per year. The current storage system has 1 TB capacity with 50% utilization. Calculate when storage capacity will be exhausted and determine the appropriate upgrade timing.

**Solution**:

**Step 1: Current Status Analysis**

- Current data: 500 GB
- Available capacity: 1 TB × (1 - 0.50) = 500 GB
- Annual growth rate: 20%

**Step 2: Year-by-Year Projection**

| Year | Data Size (GB) | Utilization | Available (GB)   |
| ---- | -------------- | ----------- | ---------------- |
| 0    | 500            | 50%         | 500              |
| 1    | 600            | 60%         | 400              |
| 2    | 720            | 72%         | 280              |
| 3    | 864            | 86.4%       | 136              |
| 4    | 1036.8         | 103.68%     | -36.8 (exceeded) |

**Step 3: Recommendation**

- Storage will be exhausted between year 3 and year 4
- Best practice: Procure additional storage when utilization reaches 80% (approximately 2 years)
- Recommended action: Add storage capacity in year 2 to ensure continuous operation

### Example 3: Network Bandwidth Capacity Planning

**Problem**: An organization's network currently handles 100 Mbps average traffic with peak usage of 180 Mbps. The link capacity is 200 Mbps. If traffic grows at 30% annually, determine when network upgrades will be required.

**Solution**:

**Step 1: Current Analysis**

- Average traffic: 100 Mbps (50% utilization)
- Peak traffic: 180 Mbps (90% utilization)
- Link capacity: 200 Mbps

**Step 2: Growth Projection**

| Year | Avg Traffic (Mbps) | Peak Traffic (Mbps) | Peak Utilization |
| ---- | ------------------ | ------------------- | ---------------- |
| 0    | 100                | 180                 | 90%              |
| 1    | 130                | 234                 | 117% (exceeded)  |
| 2    | 169                | 304.2               | 152%             |

**Step 3: Analysis**

- Peak traffic exceeds capacity in year 1
- Even average traffic exceeds capacity by year 2

**Step 4: Recommendations**

- Short-term (immediate): Implement traffic shaping and QoS to manage peak loads
- Medium-term (within 6 months): Upgrade to 500 Mbps or 1 Gbps link
- Consider implementing load balancing across multiple links
- Monitor traffic patterns to refine future predictions

## Exam Tips

1. **Understand the Capacity Planning Lifecycle**: Remember the four phases - Workload Characterization, Monitoring, Analysis, and Decision Making. This is frequently asked in exams.

2. **Differentiate Between Capacity Planning Types**: Be clear about resource, business, and service capacity planning and their specific purposes.

3. **Know Key Metrics**: Memorize utilization, throughput, response time, availability, queue length, and saturation point as they form the basis of capacity analysis.

4. **Linear vs. Non-linear Scaling**: Understand that in real-world scenarios, scaling is often non-linear due to bottlenecks and system overhead.

5. **Formula for Capacity Forecasting**: Remember the basic formula: Future Capacity = Current Capacity × (Future Workload / Current Workload) × Safety Factor

6. **Distinguish Capacity Planning from Performance Tuning**: This is a common exam question - capacity planning addresses resource quantity while performance tuning addresses resource efficiency.

7. **Three Levels of Planning**: Remember tactical (short-term), strategic (long-term), and operational (day-to-day) capacity planning.

8. **Importance of Workload Characterization**: Know that accurate capacity planning begins with properly understanding and classifying workloads.

9. **Queueing Theory Basics**: Understand basic concepts like arrival rate, service rate, and queue length as they relate to capacity planning.

10. **Cost-Balance Principle**: The goal of capacity planning is to balance under-utilization (wasted cost) with over-utilization (performance degradation).

11. **Know When to Upgrade**: The 80% utilization rule states that upgrades should be planned when resource utilization reaches approximately 80% to allow for growth and peak demands.

12. **Cloud Computing Impact**: Understand how cloud computing has transformed capacity planning by enabling elastic resources and on-demand scaling.
