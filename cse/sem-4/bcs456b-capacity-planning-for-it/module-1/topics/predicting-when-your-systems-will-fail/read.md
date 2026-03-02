# Predicting When Your Systems Will Fail

## Table of Contents

- [Predicting When Your Systems Will Fail](#predicting-when-your-systems-will-fail)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Understanding Capacity and Utilization](#understanding-capacity-and-utilization)
  - [The Concept of Thresholds](#the-concept-of-thresholds)
  - [Growth Prediction Models](#growth-prediction-models)
  - [Workload Characterization](#workload-characterization)
  - [Trend Analysis and Forecasting](#trend-analysis-and-forecasting)
  - [The Planning Horizon](#the-planning-horizon)
- [Examples](#examples)
  - [Example 1: Predicting CPU Failure for a Web Server](#example-1-predicting-cpu-failure-for-a-web-server)
  - [Example 2: Using Linear Regression for Storage Planning](#example-2-using-linear-regression-for-storage-planning)
  - [Example 3: Compound Growth Prediction for Database Server](#example-3-compound-growth-prediction-for-database-server)
- [Exam Tips](#exam-tips)

## Introduction

In modern IT infrastructure management, predicting when your systems will fail due to capacity constraints is a critical skill for any IT professional. Capacity planning is not merely about reacting to problems after they occur; it's about proactive forecasting to ensure system availability, performance, and reliability. When systems fail due to resource exhaustion—whether CPU, memory, storage, or network bandwidth—the consequences can be severe, ranging from application downtime to complete business disruption and financial losses.

This topic introduces the fundamental concepts of predicting system failures through capacity planning techniques. We will explore how to measure current system utilization, analyze growth trends, and forecast future resource requirements. Understanding these principles is essential for IT professionals who need to make informed decisions about infrastructure investments, scaling strategies, and maintenance schedules. The goal is to shift from reactive firefighting to proactive management, ensuring that systems remain available and performant as demand grows.

In the context of the university's Capacity Planning for IT course, this module provides the foundation for all subsequent topics. You will learn to use mathematical models and analytical techniques that enable IT departments to justify infrastructure investments to management and plan for sustainable growth.

## Key Concepts

### Understanding Capacity and Utilization

Capacity refers to the maximum workload a system can handle while maintaining acceptable performance levels. Utilization, on the other hand, measures how much of that capacity is currently being used. These two metrics form the basis of all capacity planning analysis. For example, a server with 64 GB of RAM currently using 48 GB has a memory utilization of 75%. When utilization approaches 100%, the system begins to experience performance degradation and eventually fails to process requests.

Key metrics to monitor include:

- **CPU Utilization**: Percentage of processing capacity in use
- **Memory Utilization**: RAM currently allocated versus available
- **Storage Utilization**: Disk space consumed versus total capacity
- **Network Utilization**: Bandwidth consumption as a percentage of available capacity
- **I/O Utilization**: Input/output operations per second compared to maximum throughput

### The Concept of Thresholds

Every system has thresholds—points at which performance degrades or failure occurs. These thresholds are not always at 100% utilization. Many systems begin experiencing issues at 70-80% utilization due to overhead, contention, and the need for headroom. Understanding your system's specific threshold behavior is crucial for accurate failure prediction.

There are three types of thresholds:

1. **Warning Threshold**: At this point, administrators should investigate and potentially take preventive action (typically 70-75% utilization)
2. **Critical Threshold**: Immediate action required; system performance significantly impacted (typically 85-90% utilization)
3. **Failure Threshold**: System can no longer function properly; service disruption inevitable (typically 95-100% utilization)

### Growth Prediction Models

Predicting future resource requirements requires understanding how demand grows over time. Several models help us forecast when systems will reach capacity limits:

**Linear Growth Model**: Assumes constant, steady increase in resource usage over time. This is the simplest model and works well for stable, mature systems with predictable growth patterns.

**Exponential Growth Model**: Assests that resource usage grows by a constant percentage over time. Common in rapidly growing applications or businesses experiencing market expansion.

**Step Function Growth**: Resource usage remains constant until a threshold triggers a sudden increase. This models systems that hit capacity limits and then get upgraded in discrete steps.

**Compound Annual Growth Rate (CAGR)**: A standardized way to express growth over multiple periods. Formula: CAGR = (Ending Value / Beginning Value)^(1/n) - 1, where n is the number of years.

### Workload Characterization

Before predicting failures, you must understand what drives resource consumption. Workload characterization involves identifying:

- **User workload**: Number of concurrent users, session duration, request frequency
- **Transaction workload**: Type and complexity of transactions (read-heavy vs. write-heavy)
- **Batch workload**: Scheduled jobs, data processing loads, backup operations
- **Peak vs. average load**: Understanding the difference between typical and maximum demand

### Trend Analysis and Forecasting

Trend analysis involves examining historical data to identify patterns and project future resource needs. Key techniques include:

**Moving Averages**: Smooth out short-term fluctuations to reveal longer-term trends. A 30-day moving average, for example, calculates the average utilization over the past 30 days to show the underlying trend.

**Linear Regression**: Fits a straight line through historical data points to predict future values. Useful for systems with steady, predictable growth.

**Exponential Smoothing**: Gives more weight to recent data points, making forecasts more responsive to recent trends while still considering historical patterns.

### The Planning Horizon

Capacity planning requires defining a planning horizon—the time period for which you're forecasting. Common planning horizons include:

- **Short-term** (0-3 months): For immediate operational decisions
- **Medium-term** (3-12 months): For budget and procurement planning
- **Long-term** (1-5 years): For strategic infrastructure planning

The appropriate horizon depends on your organization's planning cycles, budget processes, and the lead time required for infrastructure procurement and deployment.

## Examples

### Example 1: Predicting CPU Failure for a Web Server

A web server currently has 50% CPU utilization and is experiencing 10% growth per month. The critical threshold is 85%. When will the server fail?

**Given:**

- Current CPU utilization: 50%
- Monthly growth rate: 10%
- Critical threshold: 85%

**Solution:**

Month 1: 50% × 1.10 = 55%
Month 2: 55% × 1.10 = 60.5%
Month 3: 60.5% × 1.10 = 66.55%
Month 4: 66.55% × 1.10 = 73.21%
Month 5: 73.21% × 1.10 = 80.53%
Month 6: 80.53% × 1.10 = 88.58%

The server will exceed the critical threshold between month 5 and month 6. To maintain a safety margin, you should plan for capacity increase before month 5. If you need 2 months lead time for procurement, action is needed immediately.

### Example 2: Using Linear Regression for Storage Planning

An organization has been tracking storage utilization for the past 6 months:

- Month 1: 400 GB
- Month 2: 440 GB
- Month 3: 490 GB
- Month 4: 530 GB
- Month 5: 590 GB
- Month 6: 640 GB

Current storage capacity is 1 TB (1000 GB). Using linear regression, predict when storage will reach 85% capacity.

**Solution:**

Calculate average monthly growth:
Month 1-6 growth = 640 - 400 = 240 GB over 6 months
Average growth = 240/6 = 40 GB per month

Monthly growth rate = 40/400 = 10% (approximately linear)

Days until 85% capacity:
Capacity at 85% = 1000 × 0.85 = 850 GB
Remaining capacity = 850 - 640 = 210 GB
Time to reach 85% = 210/40 = 5.25 months

So approximately in month 12 (6 + 5.25), storage will reach critical threshold. Planning horizon should begin at least 3-4 months before this.

### Example 3: Compound Growth Prediction for Database Server

A database server's memory utilization has grown from 30% to 45% over the past year. Using CAGR, predict when it will reach 80% if the growth pattern continues.

**Given:**

- Beginning value: 30%
- Ending value: 45%
- Time period: 1 year
- Threshold: 80%

**Solution:**

CAGR = (45/30)^(1/1) - 1 = 1.5 - 1 = 0.5 or 50% annual growth

Monthly growth factor = 1.50^(1/12) = 1.034 (approximately 3.4% monthly)

Month-by-month projection:
Current: 45%
Month 3: 45% × 1.034³ = 49.7%
Month 6: 45% × 1.034⁶ = 55.1%
Month 9: 45% × 1.034⁹ = 61.1%
Month 12: 45% × 1.034¹² = 67.7%
Month 18: 45% × 1.034¹⁸ = 83.2%

The server will reach 80% threshold between month 15 and month 18. With a 3-month procurement lead time, planning should begin in month 12-15.

## Exam Tips

1. **Understand the difference between capacity and utilization**: Capacity is maximum capability; utilization is current usage. This distinction frequently appears in university exams.

2. **Remember threshold levels**: Warning (70-75%), Critical (85-90%), and Failure (95-100%). Know that thresholds vary by system and aren't always at 100%.

3. **Know the growth models**: Linear for steady growth, exponential for percentage-based growth, and step function for discrete capacity jumps. Choose the appropriate model based on the scenario.

4. **Practice CAGR calculations**: This formula appears frequently: CAGR = (Ending Value / Beginning Value)^(1/n) - 1

5. **Include safety margins**: Real-world planning always requires buffer time for procurement, testing, and deployment. Never plan to reach capacity exactly—always have headroom.

6. **Understand planning horizons**: Short-term (0-3 months), medium-term (3-12 months), and long-term (1-5 years) serve different purposes in capacity planning.

7. **Consider workload patterns**: Peak loads, not just averages, determine when systems fail. A system at 60% average but 90% peak may fail during peak hours.

8. **Know moving averages**: This technique smooths data to reveal trends—useful when examining noisy utilization data.
