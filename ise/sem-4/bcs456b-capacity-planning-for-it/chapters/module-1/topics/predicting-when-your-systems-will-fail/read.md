# Module 1: Capacity Planning for IT

## Topic: Predicting When Your Systems Will Fail

### Introduction

For an engineering student, a "system failure" might conjure images of a crashed server or a blue screen. However, in the context of IT capacity planning, a "failure" is more often a performance failure—a state where a system becomes so slow or unresponsive that it can no longer serve its intended function adequately, even if it hasn't technically crashed. Predicting these failures is not about crystal balls; it's a disciplined engineering process of measuring, modeling, and forecasting. It is a critical proactive strategy to ensure service availability, optimize costs, and plan for future growth.

### Core Concepts: The Path to Prediction

Predicting system failure hinges on understanding the relationship between **demand** (load) and **capacity** (supply). The goal is to identify the **saturation point**—the moment when demand exceeds available capacity, leading to a rapid degradation in performance.

#### 1. Key Performance Indicators (KPIs) / Metrics

You cannot predict what you do not measure. The first step is to identify and monitor the right metrics. These typically fall into two categories:

- **Resource Utilization Metrics:** Measure how much of a specific resource is being used.
  - **CPU Utilization (%):** The percentage of time the processor is busy. Consistently high levels (e.g., >80-90%) indicate potential bottleneck.
  - **Memory Utilization (%):** The percentage of RAM in use. High utilization can lead to swapping to disk, which drastically slows down performance.
  - **Disk I/O (IOPS, Throughput):** Measures read/write operations per second and data transfer rate. High latency here can stall entire systems.
  - **Network Bandwidth (Mbps/Gbps):** The volume of data moving across the network. Saturation causes packet loss and delays.

- **Application Performance Metrics:** Measure the experience from a user's perspective.
  - **Response Time:** The time taken to complete a user transaction (e.g., page load time). A steep increase is a key failure indicator.
  - **Throughput:** The number of transactions or requests processed per second. A dropping throughput under increasing load often signifies a failing system.
  - **Error Rate:** The percentage of requests that result in errors. A rising error rate is a direct signal of failure.

#### 2. Trend Analysis and Forecasting

Once metrics are collected over time, you can analyze trends to forecast future behavior.

- **Linear Growth:** If user numbers are growing at a steady rate (e.g., 10% per month), you can extrapolate the trend to predict when resource consumption will hit a critical threshold.
- **Seasonal Patterns:** Many systems have predictable peaks (e.g., e-commerce during holidays, university portals during exam registration). Forecasting involves identifying these patterns and planning capacity for the next peak.

#### 3. Load Testing and Modeling

Trend analysis is based on history. To predict behavior under unprecedented load, engineers use **load testing**.

- **Concept:** Use tools (e.g., JMeter, LoadRunner) to simulate real-world load on a system in a test environment.
- **Goal:** To intentionally find the breaking point. You gradually increase the simulated user load while monitoring KPIs. The test answers crucial questions:
  - At what number of concurrent users does response time exceed acceptable limits?
  - Which component (CPU, Database, Disk) fails first?
  - What is the maximum throughput the system can handle?

This process creates a predictive model: "Our current web server can handle 1,000 concurrent users before response time exceeds 2 seconds."

### Example: Predicting Failure for a University Exam Portal

**Scenario:** 's exam results portal historically sees a 10x surge in traffic on result day. Last year, with 50,000 simultaneous users, the average response time was 5 seconds (unacceptably slow). CPU utilization was at 98%.

**Prediction Analysis:**

1.  **Metric:** CPU Utilization and Response Time are the key failure indicators.
2.  **Trend:** Student registrations are growing at 5% per year. This year, expect ~52,500 simultaneous users.
3.  **Modeling:** Based on last year's data, the system failed at 50k users. A linear scaling model might suggest that 52.5k users would increase response time further and push utilization to 100%, causing a complete bottleneck.
4.  **Prediction & Action:** The system **will fail** under the projected load. This prediction triggers action: the IT team must scale up (more powerful servers) or scale out (add more servers behind a load balancer) **before** the next results are published.

### Key Points / Summary

- **Failure Definition:** In capacity planning, failure is primarily a **performance failure** (unacceptable slowness), not just a system crash.
- **Foundation is Measurement:** Prediction is impossible without continuously monitoring the right **KPIs** (CPU, Memory, Response Time, Throughput).
- **Trend Analysis:** Use historical data to forecast future demand based on **linear growth** and **seasonal patterns**.
- **Load Testing:** Proactively **simulate load** in a test environment to find the exact breaking point of your system and build a predictive model.
- **Goal:** The ultimate aim is to **proactively identify** future bottlenecks and address them **before** they impact users, ensuring reliability and planning cost-effective upgrades.
