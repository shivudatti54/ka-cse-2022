# Performance and Capacity

## Table of Contents

- [Performance and Capacity](#performance-and-capacity)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Performance Metrics and Indicators](#1-performance-metrics-and-indicators)
  - [2. Capacity Planning Fundamentals](#2-capacity-planning-fundamentals)
  - [3. Workload Characterization](#3-workload-characterization)
  - [4. Performance Monitoring and Analysis](#4-performance-monitoring-and-analysis)
  - [5. Performance Tuning and Optimization](#5-performance-tuning-and-optimization)
- [Examples](#examples)
  - [Example 1: Calculating System Utilization and Planning Capacity](#example-1-calculating-system-utilization-and-planning-capacity)
  - [Example 2: Memory Capacity Planning for Database Server](#example-2-memory-capacity-planning-for-database-server)
  - [Example 3: Response Time Analysis and SLA Compliance](#example-3-response-time-analysis-and-sla-compliance)
- [Exam Tips](#exam-tips)

## Introduction

Performance and Capacity are fundamental concepts in IT infrastructure management that directly impact an organization's ability to deliver services efficiently. In the context of Capacity Planning for IT (BCS456B), understanding how to measure, analyze, and optimize system performance is crucial for any IT professional. Performance refers to how well a computer system or network operates in terms of responsiveness, throughput, and resource utilization, while Capacity represents the maximum workload a system can handle while maintaining acceptable performance levels.

Effective capacity planning ensures that IT resources are utilized optimally, costs are controlled, and service level agreements (SLAs) are met. As organizations grow and their IT requirements expand, the ability to predict future capacity needs and proactively address performance bottlenecks becomes a critical competitive advantage. This topic forms the foundation for understanding how to balance system performance with business requirements, making it essential for IT managers, system administrators, and capacity planners.

The relationship between performance and capacity is interdependent: poor performance often indicates capacity constraints, while adequate capacity doesn't always guarantee optimal performance. Therefore, a comprehensive understanding of both concepts is necessary for effective IT service management and planning.

## Key Concepts

### 1. Performance Metrics and Indicators

Performance measurement involves collecting quantitative data about system behavior using various metrics:

- **Response Time**: The elapsed time between a user request and system response. It includes service time, waiting time, and transmission time. Average response time, 90th percentile response time, and peak response time are commonly monitored.

- **Throughput**: The number of transactions or requests processed per unit time. Measured in transactions per second (TPS), requests per second (RPS), or operations per second (OPS). Higher throughput generally indicates better system performance.

- **Utilization**: The percentage of time a resource is busy processing requests. CPU utilization, memory utilization, disk utilization, and network utilization are key indicators. High utilization (>80%) often signals potential bottlenecks.

- **Availability**: The percentage of time a system is operational and accessible. Calculated as (Total Time - Downtime) / Total Time × 100. Typically expressed as "nines" (99.9% = three nines).

- **Latency**: The delay before a transfer of data begins following an instruction. Network latency, disk latency, and application latency are critical measurements.

- **Error Rate**: The frequency of errors occurring in the system, including transaction failures, timeouts, and exceptions.

### 2. Capacity Planning Fundamentals

Capacity Planning is the process of determining the IT infrastructure requirements needed to meet current and future business demands:

- **Baseline Capacity**: The minimum resource capacity required to meet current business needs. Established through monitoring and analysis of historical data.

- **Scalability**: The ability of a system to handle increased workload by adding resources. Vertical scaling (adding power to existing machines) and horizontal scaling (adding more machines) are two approaches.

- **Capacity Triggers**: Predefined thresholds that indicate when capacity expansion becomes necessary. Examples include CPU utilization exceeding 75% for extended periods or disk space falling below 20%.

- **Capacity Planning Lifecycle**: Includes four phases - Monitoring, Analysis, Modeling, and Implementation. This cyclical process ensures continuous optimization.

### 3. Workload Characterization

Understanding the nature of workloads is essential for accurate capacity planning:

- **Workload Types**: Interactive (user-facing), batch (background processing), and hybrid workloads have different resource requirements and performance characteristics.

- **Peak Load vs. Average Load**: Capacity must handle peak loads, but optimizing for peak alone leads to inefficiency. Understanding the load distribution helps in planning.

- **Growth Rate**: The rate at which workload increases over time, typically measured as percentage growth per month or year. Used to predict future capacity requirements.

- **Service Level Agreements (SLAs)**: Contracts defining expected performance levels. Capacity planning must ensure SLA compliance during normal and peak operations.

### 4. Performance Monitoring and Analysis

Continuous monitoring is essential for effective capacity management:

- **Active Monitoring**: Involves synthetic transactions and probes to measure performance from user perspective. Tools include APM (Application Performance Monitoring) solutions.

- **Passive Monitoring**: Collection and analysis of actual transaction data from production systems. Uses agents, SNMP collectors, and log analyzers.

- **Bottleneck Analysis**: The process of identifying constraints that limit system performance. Common bottlenecks include CPU, memory, disk I/O, and network bandwidth.

- **Performance Baselines**: Reference points representing normal system behavior under typical conditions. Used to detect anomalies and plan capacity.

### 5. Performance Tuning and Optimization

Once performance issues are identified, tuning efforts focus on optimization:

- **Resource Optimization**: Adjusting resource allocation, configuring parameters, and optimizing code to improve efficiency.

- **Load Balancing**: Distributing workloads across multiple resources to prevent any single component from becoming a bottleneck.

- **Caching Strategies**: Implementing caches at various levels (database, application, web) to reduce response times and backend load.

- **Queue Management**: Implementing queuing mechanisms to handle burst loads gracefully and prioritize critical transactions.

## Examples

### Example 1: Calculating System Utilization and Planning Capacity

**Problem**: A web server processes an average of 2,400 requests per hour. Each request takes 0.5 seconds of CPU time on average. The server has a single CPU core operating at 100% capacity.

**Solution**:

**Step 1: Calculate current throughput**

- Requests per second = 2,400 / 3,600 = 0.667 requests/second

**Step 2: Calculate CPU seconds per second**

- CPU utilization = 0.667 × 0.5 = 0.333 CPU-seconds/second
- This equals 33.3% CPU utilization

**Step 3: Determine capacity headroom**

- Available capacity = 100% - 33.3% = 66.7%
- Maximum requests with current CPU = 2,400 / 0.333 = 7,207 requests/hour

**Step 4: Plan for 50% growth**

- Expected requests after growth = 2,400 × 1.5 = 3,600 requests/hour
- Required CPU capacity = (3,600 × 0.5) / 3,600 = 0.5 CPU-seconds/second = 50% utilization
- Current capacity can handle this growth with 50% headroom remaining

**Conclusion**: The current server has adequate capacity for 50% growth. However, if growth exceeds 100% (4,800 requests/hour), additional CPU capacity would be needed.

### Example 2: Memory Capacity Planning for Database Server

**Problem**: A database server currently runs with 16GB RAM. Monitoring shows:

- Average memory usage: 12GB (75%)
- Peak memory usage: 14.5GB (90.6%)
- Memory leak suspected: 0.5GB increase per month

Calculate when capacity will be exceeded and recommend action.

**Solution**:

**Step 1: Determine usable memory headroom**

- Usable headroom at peak = 16GB - 14.5GB = 1.5GB
- At current growth rate, days until exhaustion = 1.5GB / (0.5GB/30 days) = 90 days

**Step 2: Calculate memory required in 6 months**

- Expected peak usage in 6 months = 14.5GB + (0.5GB × 6) = 17.5GB
- Required memory for 80% utilization = 17.5GB / 0.8 = 21.875GB

**Step 3: Recommendation**

- Immediate: Schedule memory leak fix within 60 days
- Short-term: Plan upgrade to 32GB RAM before month 4
- Long-term: Implement auto-scaling or optimize queries to reduce memory footprint

### Example 3: Response Time Analysis and SLA Compliance

**Problem**: An e-commerce application must meet SLA: "95% of transactions complete within 3 seconds." Current monitoring data shows:

- Average response time: 1.8 seconds
- Standard deviation: 0.9 seconds
- Distribution: Normal (Gaussian)

Determine if SLA is being met and identify improvement targets.

**Solution**:

**Step 1: Calculate 95th percentile response time**

- For normal distribution, 95th percentile = Mean + 1.645 × Standard Deviation
- 95th percentile = 1.8 + 1.645 × 0.9 = 1.8 + 1.48 = 3.28 seconds

**Step 2: Compare with SLA**

- Current 95th percentile (3.28s) > SLA requirement (3.0s)
- SLA is NOT being met - approximately 2.5% of transactions exceed 3 seconds

**Step 3: Calculate required improvement**

- Target 95th percentile ≤ 3.0 seconds
- Using same standard deviation (0.9s), required mean = 3.0 - 1.645 × 0.9 = 1.52 seconds
- Required improvement = 1.8 - 1.52 = 0.28 seconds (15.6% reduction in average response time)

**Step 4: Recommendations**

- Optimize database queries to reduce average response time by 0.3 seconds
- Consider implementing caching layer
- Add load balancing to distribute traffic more evenly

## Exam Tips

1. **Remember the difference between performance and capacity**: Performance is "how well" the system works (response time, throughput), while capacity is "how much" the system can handle (maximum workload).

2. **Know key formulas**: Average utilization = Busy Time / Total Time; Throughput = Completed Transactions / Time Period; 95th Percentile = Mean + 1.645 × Standard Deviation (for normal distribution).

3. **Understand the capacity planning lifecycle**: The four phases are Monitoring → Analysis → Modeling → Implementation. This is a continuous cyclical process.

4. **Vertical vs. Horizontal Scaling**: Remember vertical scaling adds resources to existing machines (more CPU/RAM), while horizontal scaling adds more machines to the infrastructure.

5. **Common performance metrics to remember**: Response time, throughput, utilization, latency, availability, and error rate. Be able to explain each with an example.

6. **SLA compliance calculations**: When given mean and standard deviation, you can calculate percentile response times using the normal distribution formula for exam problems.

7. **Bottleneck identification**: In capacity planning problems, always check CPU, memory, disk I/O, and network as potential bottlenecks. The component with highest utilization is typically the bottleneck.

8. **Growth rate calculations**: Remember to account for both organic growth (business increase) and synthetic growth (new features/users) when planning future capacity.

9. **Baselines are essential**: Performance baselines represent normal operating conditions and are crucial for detecting anomalies - this frequently appears in exams.

10. **Practice unit conversions**: Common conversions include requests/hour to requests/second (divide by 3600) and percentage utilization calculations.
