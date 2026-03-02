# Different Kinds of Requirements and Measurements in IT Capacity Planning

## Table of Contents

- [Different Kinds of Requirements and Measurements in IT Capacity Planning](#different-kinds-of-requirements-and-measurements-in-it-capacity-planning)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Classification of IT Requirements](#1-classification-of-it-requirements)
  - [2. Workload Characterization](#2-workload-characterization)
  - [3. Key Measurements in Capacity Planning](#3-key-measurements-in-capacity-planning)
  - [4. Resource Utilization Metrics](#4-resource-utilization-metrics)
  - [5. Baseline Measurements and Thresholds](#5-baseline-measurements-and-thresholds)
- [Examples](#examples)
  - [Example 1: Classifying Requirements for an E-Commerce Platform](#example-1-classifying-requirements-for-an-e-commerce-platform)
  - [Example 2: Calculating System Availability](#example-2-calculating-system-availability)
  - [Example 3: Workload Analysis for Database Server](#example-3-workload-analysis-for-database-server)
- [Exam Tips](#exam-tips)

## Introduction

Capacity planning is a critical function in IT service management that ensures organizations have adequate resources to meet current and future business demands. In the context of the university's Capacity Planning for IT course, understanding different kinds of requirements and measurements forms the foundation for effective capacity management. This topic introduces students to the various categories of requirements that organizations must consider when planning IT infrastructure, along with the measurement techniques necessary for accurate capacity planning.

IT capacity planning involves predicting future resource requirements based on business needs, technological advancements, and growth projections. Without proper understanding of requirements and accurate measurements, organizations risk either over-provisioning (leading to unnecessary costs) or under-provisioning (resulting in poor service quality and potential business losses). The discipline of capacity planning bridges the gap between business objectives and technical infrastructure, making it essential for IT professionals to master these fundamental concepts.

This module covers the classification of requirements, measurement methodologies, and the practical application of these concepts in real-world IT environments. Students will learn to distinguish between different types of requirements and understand how each type influences capacity planning decisions.

## Key Concepts

### 1. Classification of IT Requirements

**Functional Requirements**

Functional requirements define what the system must do—the specific functions and services it must provide. In capacity planning, functional requirements help determine the nature of workload the system will handle. Examples include:

- Number of transactions per second
- Number of concurrent users
- Data storage requirements
- Specific application functionalities that require resources

Functional requirements are typically expressed in terms of business processes and user needs. For capacity planners, understanding functional requirements is crucial because they directly translate into workload characteristics that determine resource utilization.

**Non-Functional Requirements**

Non-functional requirements specify how the system should perform—they define the quality attributes of the IT service. These requirements constrain the functional implementation and are critical for capacity planning. Key non-functional requirements include:

- Performance: Response time, throughput, latency
- Scalability: Ability to handle increased workload
- Availability: System uptime percentage
- Reliability: Mean time between failures
- Security: Data protection and access controls

Non-functional requirements often become the basis for capacity planning thresholds and service level agreements (SLAs).

**Business Requirements**

Business requirements represent the organizational goals and objectives that IT systems must support. These requirements are derived from the organization's strategic plans and operational needs. Examples include:

- Support for business growth projections (e.g., 20% annual increase in customers)
- Compliance with regulatory requirements
- Cost constraints and budget limitations
- Time-to-market for new services

Business requirements provide the context for capacity planning decisions and help justify investment in IT infrastructure.

**Technical Requirements**

Technical requirements specify the technological constraints and standards that the IT infrastructure must meet. These include:

- Hardware specifications and compatibility
- Software licensing constraints
- Network infrastructure limitations
- Integration requirements with existing systems
- Technology roadmap alignment

Technical requirements define the boundaries within which capacity planning must operate and influence the choice of solutions.

### 2. Workload Characterization

Understanding workload is fundamental to capacity planning. Workload characterization involves identifying and measuring the demands placed on IT resources.

**Workload Components**

- Interactive workload: User-initiated requests requiring immediate response
- Batch workload: Scheduled background processing jobs
- Transactional workload: Database operations and updates
- Analytical workload: Reporting and data processing

**Workload Metrics**

- Request rate: Number of requests per time unit
- Transaction mix: Distribution of different transaction types
- Think time: Time between user interactions
- Session characteristics: Duration and resource usage per session

### 3. Key Measurements in Capacity Planning

**Performance Measurements**

Performance measurements quantify how well the system meets its functional requirements:

- **Response Time**: The elapsed time from user request initiation to response receipt. Includes service time, queue time, and network latency.
- **Throughput**: The rate at which the system processes transactions or requests, typically measured in transactions per second (TPS) or operations per second (OPS).
- **Latency**: The delay between a request and the beginning of the response, often distinguishing between network latency and processing latency.
- **Utilization**: The percentage of time a resource is busy processing requests. Common metrics include CPU utilization, memory utilization, and disk utilization.

**Availability Measurements**

Availability measurements indicate the system's readiness to provide services:

- **Availability Percentage**: (MTBF / (MTBF + MTTR)) × 100, where MTBF is Mean Time Between Failures and MTTR is Mean Time To Repair.
- **Uptime**: Total time the system is operational during a given period.
- **Downtime**: Total time the system is unavailable, categorized as planned or unplanned.

**Reliability Measurements**

Reliability metrics assess the system's ability to function without failure:

- **MTBF (Mean Time Between Failures)**: Average time between system failures.
- **MTTR (Mean Time To Repair)**: Average time required to restore system to operation after a failure.
- **Failure Rate**: Number of failures per unit of time.

### 4. Resource Utilization Metrics

**CPU Metrics**

- User CPU time: Time spent executing user processes
- System CPU time: Time spent in kernel mode
- Idle CPU time: Unused CPU capacity
- Wait CPU time: Time spent waiting for I/O

**Memory Metrics**

- Used memory: Currently allocated memory
- Free memory: Available memory for allocation
- Cached memory: Memory used for disk caching
- Swap usage: Disk space used as virtual memory

**Storage Metrics**

- Disk space utilization: Percentage of storage capacity used
- I/O throughput: Data read/written per second
- I/O wait time: Time CPU waits for disk operations
- Queue length: Number of pending I/O requests

**Network Metrics**

- Bandwidth utilization: Percentage of available bandwidth used
- Packet loss: Percentage of packets not delivered
- Latency: Time for data to travel across the network
- Throughput: Actual data transfer rate

### 5. Baseline Measurements and Thresholds

**Baseline Measurements**

A baseline represents a snapshot of normal system behavior under typical workload conditions. Establishing baselines involves:

- Collecting measurements over a representative period
- Identifying normal patterns and variations
- Documenting typical resource utilization levels
- Recording workload characteristics

Baselines serve as reference points for capacity planning and help identify anomalies or capacity issues.

**Threshold Values**

Thresholds define acceptable limits for various metrics:

- Warning thresholds: Indicate potential problems requiring attention
- Critical thresholds: Require immediate action to prevent service degradation
- Capacity thresholds: Trigger capacity expansion planning

Common threshold guidelines:

- CPU utilization: Warning at 70%, Critical at 85%
- Memory utilization: Warning at 80%, Critical at 90%
- Disk utilization: Warning at 75%, Critical at 90%
- Response time: Warning at 150% of baseline, Critical at 200%

## Examples

### Example 1: Classifying Requirements for an E-Commerce Platform

**Scenario**: An organization is planning capacity for a new e-commerce platform expected to launch in 6 months.

**Requirements Classification**:

_Functional Requirements:_

- Support 10,000 concurrent users during peak hours
- Process at least 500 transactions per minute
- Handle product catalog with 50,000 items
- Support payment processing through multiple gateways
- Shopping cart functionality with persistent sessions

_Non-Functional Requirements:_

- Page response time under 3 seconds for 95% of requests
- System availability of 99.9% (8.76 hours annual downtime)
- Support business growth of 50% year-over-year
- Data encryption for all customer transactions

_Business Requirements:_

- Initial budget constraint of ₹50 lakhs for infrastructure
- Launch before festive season (4 months)
- Support multiple regional languages
- Integration with existing inventory management system

_Technical Requirements:_

- Use cloud infrastructure for scalability
- PostgreSQL database for inventory data
- CDN integration for static content delivery
- Load balancer for traffic distribution

**Capacity Planning Implications**:
Based on these requirements, capacity planners must:

- Size infrastructure for 10,000 concurrent users with headroom
- Plan for 50% growth within first year
- Design for geographic redundancy to meet availability SLA
- Account for peak season (3x normal load) in capacity

### Example 2: Calculating System Availability

**Scenario**: A critical application server had 3 failures in the past year. The total downtime was 12 hours, with an average repair time of 4 hours per incident.

**Solution**:

Given:

- Number of failures = 3
- Total downtime = 12 hours
- MTTR = Total downtime / Number of failures = 12 / 3 = 4 hours

To calculate MTBF, we need the total operational time:

- Total hours in a year = 365 × 24 = 8760 hours
- Operational time = Total hours - Downtime = 8760 - 12 = 8748 hours
- MTBF = Operational time / Number of failures = 8748 / 3 = 2916 hours

Availability Percentage = MTBF / (MTBF + MTTR) × 100
= 2916 / (2916 + 4) × 100
= 2916 / 2920 × 100
= 99.86%

This availability of 99.86% exceeds the typical 99.9% SLA requirement, but the organization should still aim to improve reliability to reduce the risk of SLA breaches.

### Example 3: Workload Analysis for Database Server

**Scenario**: A database server handles two types of transactions:

- Read transactions: 80% of total workload, average 10ms CPU time
- Write transactions: 20% of total workload, average 50ms CPU time

The server processes 1000 transactions per second.

**Solution**:

_Weighted Average CPU Time per Transaction:_
= (0.80 × 10ms) + (0.20 × 50ms)
= 8ms + 10ms
= 18ms per transaction

_CPU Utilization at 1000 TPS:_
At 1000 transactions per second, each second contains 1000ms:
CPU utilization = (18ms / 1000ms) × 100 = 1.8%

_Capacity Analysis:_

- At 70% warning threshold: 1000 / 0.70 = 1428 TPS capacity
- At 85% critical threshold: 1000 / 0.85 = 1176 TPS capacity

This analysis shows the current workload is well within capacity. However, if growth projections indicate 50% increase in transactions, capacity planning should begin when approaching 1176 TPS.

## Exam Tips

1. **Understand Requirement Categories**: Remember the four main types—Functional, Non-Functional, Business, and Technical. Be able to distinguish between them with examples.

2. **Know Key Formulas**: Memorize the availability formula (MTBF/(MTBF+MTTR) × 100) and understand how MTBF and MTTR relate to reliability.

3. **Threshold Values**: Remember standard threshold percentages for CPU (70%/85%), Memory (80%/90%), and Disk (75%/90%) utilization.

4. **Workload Characterization**: Understand how to classify workloads (interactive, batch, transactional, analytical) and their impact on resource utilization.

5. **Measurement Units**: Be familiar with common units—TPS (transactions per second), response time (ms), utilization (percentage), MTBF (hours).

6. **Baseline vs. Thresholds**: Understand that baselines represent normal operation while thresholds indicate when action is required.

7. **Resource Metrics**: Know the key metrics for CPU, memory, storage, and network resources and how they interrelate.

8. **Practical Application**: Practice solving problems that involve calculating utilization, availability, and capacity based on given requirements.

9. **SLA Considerations**: Remember that non-functional requirements often translate into SLA commitments that drive capacity planning decisions.

10. **Growth Planning**: Understand how business requirements for growth influence long-term capacity planning.
