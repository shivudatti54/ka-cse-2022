# Setting Goals for Capacity: Different Kinds of Requirements

## Table of Contents

- [Setting Goals for Capacity: Different Kinds of Requirements](#setting-goals-for-capacity-different-kinds-of-requirements)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Understanding Requirements in Capacity Planning](#understanding-requirements-in-capacity-planning)
  - [Types of Capacity Requirements](#types-of-capacity-requirements)
  - [Setting SMART Capacity Goals](#setting-smart-capacity-goals)
  - [Relationship Between Requirements and Capacity Goals](#relationship-between-requirements-and-capacity-goals)
- [Examples](#examples)
  - [Example 1: E-Commerce Platform Capacity Goals](#example-1-e-commerce-platform-capacity-goals)
  - [Example 2: Corporate Email System Requirements](#example-2-corporate-email-system-requirements)
  - [Example 3: Database Server Capacity Planning](#example-3-database-server-capacity-planning)
- [Exam Tips](#exam-tips)

## Introduction

Capacity planning is a critical function in information technology management that ensures IT resources are appropriately sized to meet current and future business demands. Setting goals for capacity involves understanding the various types of requirements that an IT infrastructure must satisfy and establishing measurable objectives that align with organizational objectives. Without clearly defined capacity goals, organizations risk either over-provisioning (leading to unnecessary costs) or under-provisioning (resulting in poor performance and service degradation).

In the context of IT service management, capacity planning encompasses the proactive management of technical infrastructure, applications, and supporting services to ensure they deliver the required performance levels at optimal cost. The process of setting capacity goals requires a thorough understanding of business requirements, user expectations, technical constraints, and cost considerations. This topic explores the different kinds of requirements that drive capacity planning decisions and provides guidance on establishing effective capacity goals for IT services.

The importance of proper capacity goal setting cannot be overstated in modern organizations where IT has become integral to business operations. Whether it's ensuring adequate server resources for e-commerce platforms during peak seasons or maintaining response times for customer-facing applications, capacity goals form the foundation of reliable IT service delivery. This module examines the various categories of requirements and their role in shaping capacity planning strategies.

## Key Concepts

### Understanding Requirements in Capacity Planning

Requirements in capacity planning refer to the documented needs and expectations that the IT infrastructure must fulfill. These requirements serve as the basis for determining the type, amount, and configuration of IT resources required. Requirements can be categorized into several types, each playing a distinct role in capacity planning decisions.

**Business Requirements** represent the high-level objectives and needs of the organization. These requirements are derived from organizational strategies, market conditions, regulatory obligations, and operational needs. Business requirements define what the organization aims to achieve and provide the context for more detailed technical requirements. For example, a business requirement might be "support business growth of 20% annually" or "ensure 99.9% system availability for critical applications." Business requirements are typically expressed in business terms and focus on outcomes rather than technical solutions.

**User Requirements** describe the needs and expectations of the end-users who interact with IT systems and services. These requirements capture how users perceive system performance, availability, and usability. User requirements are often captured through user surveys, interviews, and analysis of user behavior patterns. Examples include response time expectations, concurrent user support requirements, and accessibility needs. Understanding user requirements is essential for designing IT services that deliver positive user experiences.

**Technical Requirements** specify the technical characteristics and constraints that IT systems must meet. These requirements are derived from the chosen technology platforms, integration needs, security considerations, and performance benchmarks. Technical requirements include specifications such as processor speed, memory capacity, storage throughput, network bandwidth, and database performance parameters. Technical requirements must be measurable and testable to ensure compliance.

**Operational Requirements** address the day-to-day operational needs of IT service delivery. These include requirements for system backups, maintenance windows, monitoring capabilities, and support procedures. Operational requirements ensure that IT services can be managed effectively throughout their lifecycle and that appropriate support mechanisms are in place.

### Types of Capacity Requirements

**Throughput Requirements** define the volume of work that systems must process within a given time period. Throughput is typically measured in transactions per second, requests per minute, or operations per hour depending on the system type. Setting throughput requirements involves analyzing current workload patterns and projecting future growth based on business forecasts. For instance, an e-commerce platform might require the capacity to handle 10,000 orders per hour during peak shopping seasons.

**Response Time Requirements** specify the acceptable time taken by systems to respond to user requests. Response time requirements are critical for user satisfaction and productivity. Different types of transactions may have different response time expectations. Real-time systems might require response times in milliseconds, while batch processing jobs might have requirements measured in hours. Response time requirements should consider both average and peak load conditions.

**Availability Requirements** define the percentage of time that IT services must be operational and accessible to users. Availability is typically expressed as a percentage of total operating time, such as 99.9% (three nines) or 99.99% (four nines). Each additional level of availability represents exponentially higher infrastructure requirements and costs. Availability requirements must consider both planned downtime (for maintenance) and unplanned downtime (from failures).

**Scalability Requirements** specify how the system should accommodate growth in workload or users. Scalability requirements define whether growth should be handled through vertical scaling (adding more power to existing resources) or horizontal scaling (adding more resources). These requirements also specify the expected scaling factors and the time frame over which scaling should occur.

**Storage Requirements** define the amount of data storage capacity needed to support current operations and future growth. Storage requirements consider not only the raw data volume but also overhead for file systems, redundancy, backups, and growth margin. With the proliferation of unstructured data from sources like logs, media files, and analytics data, storage requirements have become increasingly important.

### Setting SMART Capacity Goals

Effective capacity goals should follow the SMART framework: Specific, Measurable, Achievable, Relevant, and Time-bound. This approach ensures that capacity goals are clear, actionable, and aligned with organizational objectives.

**Specific Goals** clearly define what needs to be achieved without ambiguity. Instead of saying "improve system performance," a specific goal would be "reduce average response time for customer transactions to under 2 seconds."

**Measurable Goals** include quantitative criteria that allow progress to be tracked and success to be evaluated. Measurements might include CPU utilization percentages, memory usage limits, transaction throughput rates, or response time thresholds.

**Achievable Goals** are realistic given available resources, technology, and budget constraints. Setting unachievable goals leads to frustration and demotivation, while too easily achievable goals may not drive necessary improvements.

**Relevant Goals** align with broader business objectives and priorities. Capacity goals should support the organization's strategic initiatives and deliver value to customers and stakeholders.

**Time-bound Goals** specify when results should be achieved, creating urgency and enabling progress monitoring. For example, "achieve 99.95% availability by Q4 2024."

### Relationship Between Requirements and Capacity Goals

Capacity goals bridge the gap between requirements and actual resource provisioning. Requirements provide the "what" (what needs to be achieved), while capacity goals define the "how much" and "when." The process of translating requirements into capacity goals involves:

1. **Analyzing requirements** to understand the underlying needs and priorities
2. **Quantifying requirements** by assigning numerical values where possible
3. **Prioritizing requirements** based on business criticality and impact
4. **Establishing thresholds** that define acceptable performance levels
5. **Defining metrics** to measure compliance with capacity goals

## Examples

### Example 1: E-Commerce Platform Capacity Goals

Consider an e-commerce company preparing for holiday shopping season. Based on business analysis, the company projects a 40% increase in traffic compared to the previous year.

**Current System Baseline:**

- Average daily visits: 50,000
- Peak hourly visits: 8,000
- Average response time: 1.5 seconds
- Current server capacity: 4 application servers with 16GB RAM each

**Business Requirements Analysis:**

- Must handle 70,000 daily visits (40% growth)
- Must maintain response time under 2 seconds during peak hours
- System availability during holiday season: 99.9%

**Capacity Goals Setting:**

_Throughput Goal:_ Support 11,200 peak hourly visits (40% increase from 8,000)

_Response Time Goal:_ Maintain average response time ≤2 seconds at 150% of average load

_Availability Goal:_ Achieve 99.9% availability during the holiday period (November-December)

_Scalability Goal:_ Implement auto-scaling to add 2 additional servers when CPU utilization exceeds 70%

_Storage Goal:_ Ensure 50% growth margin in database storage capacity before holiday season

**Calculation for Server Capacity:**

- Current peak: 8,000 visits/hour with 4 servers = 2,000 visits/server/hour
- Target peak: 11,200 visits/hour
- Required servers: 11,200 ÷ 2,000 = 5.6, round up to 6 servers
- With scalability buffer: 8 servers (including 2 for auto-scaling)

### Example 2: Corporate Email System Requirements

A medium-sized organization with 2,500 employees is upgrading its email infrastructure.

**Gathered Requirements:**

- Each user has average mailbox size of 2GB
- Users send approximately 50 emails per day with average size of 100KB
- 10% of users access email simultaneously during peak hours
- Email must be accessible within 3 seconds on average
- System must support disaster recovery with 4-hour recovery time objective

**Translating to Capacity Goals:**

_Storage Capacity Goal:_

- Current storage: 2,500 × 2GB = 5TB
- Growth factor: 20% annual growth
- 3-year storage requirement: 5TB × 1.2³ = 8.64TB
- With 30% overhead for redundancy: 11.2TB minimum

_Concurrent User Goal:_

- Peak concurrent users: 2,500 × 10% = 250 users
- Design capacity: Support 300 concurrent users (20% buffer)

_Performance Goal:_

- Average response time: ≤3 seconds
- 95th percentile response time: ≤5 seconds
- Search operations: ≤10 seconds for inbox searches

_Availability Goal:_

- Planned availability: 99.95% (approximately 4.38 hours annual downtime)
- Include maintenance windows in availability calculation

### Example 3: Database Server Capacity Planning

A financial application requires database capacity planning for transaction processing.

**Requirements Identified:**

- Process 5,000 transactions per second during business hours
- Support 500 concurrent database connections
- Ensure transaction processing latency under 50 milliseconds
- Maintain data integrity with zero tolerance for data loss

**Capacity Goals:**

_Throughput Goal:_ Process 5,000 TPS with capability to burst to 7,500 TPS for 15-minute intervals

_Connection Goal:_ Support 500 concurrent connections with connection pooling efficiency of 80%

_Latency Goal:_ Average transaction latency ≤50ms at 80% load; ≤100ms at peak load

_Redundancy Goal:_ Implement database clustering with automatic failover and zero data loss configuration

**Resource Calculation:**

- Assuming 500 TPS per core with modern processors, need: 5,000 ÷ 500 = 10 cores minimum
- With 30% headroom: 13 cores
- Memory: 500 connections × 2MB per connection = 1GB minimum, plus 8GB for buffer cache
- Total memory: 16GB recommended

## Exam Tips

1. **Understand the requirement hierarchy**: Remember that business requirements drive user requirements, which in turn inform technical requirements. This cascading relationship is important for exam questions on requirement analysis.

2. **Know the difference between capacity and performance requirements**: Capacity requirements deal with "how much" (throughput, storage, users), while performance requirements deal with "how fast" (response time, latency). Don't confuse these in exam answers.

3. **Remember SMART criteria for goals**: When answering questions about setting capacity goals, always mention that effective goals should be Specific, Measurable, Achievable, Relevant, and Time-bound.

4. **Be familiar with availability calculations**: Know how to calculate availability percentages and understand what each "nine" represents. For example, 99.9% equals approximately 8.76 hours of annual downtime.

5. **Understand scalability types**: Know the difference between vertical scaling (adding resources to existing nodes) and horizontal scaling (adding more nodes), and when each is appropriate.

6. **Capacity vs. performance trade-offs**: Recognize that capacity planning often involves trade-offs between cost, performance, and availability. Exam questions may ask you to balance these factors.

7. **Requirement prioritization**: In capacity planning, not all requirements have equal importance. Understand how to prioritize based on business criticality and impact.

8. **Buffer and growth margins**: Always include appropriate buffer capacity and growth margins in capacity calculations. A common approach is to add 20-30% above current requirements.
