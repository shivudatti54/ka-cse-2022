# Quick and Dirty Math in IT Capacity Planning

## Introduction

Capacity planning is a critical function in IT infrastructure management that ensures sufficient resources are available to meet current and future workload demands. While sophisticated analytical tools and complex modeling techniques exist for precise capacity predictions, there is often a need for rapid, approximate calculations that can provide immediate insights without requiring extensive data collection or specialized software. This is where "Quick and Dirty Math" comes into play—a practical approach to capacity estimation that uses simple mathematical techniques to derive reasonable answers quickly.

The term "quick and dirty math" refers to back-of-the-envelope calculations or rough order of magnitude (ROM) estimates that IT professionals use for initial capacity assessments, quick feasibility checks, or when detailed data is unavailable. These techniques are particularly valuable during early project phases, budget discussions, or when making quick decisions about resource allocation. While they may not provide the precision of detailed analytical models, they offer substantial value by enabling rapid decision-making and providing reasonable estimates that can guide further investigation.

In the context of the university's Capacity Planning curriculum, understanding quick estimation techniques is essential for every IT professional. These methods complement formal capacity planning methodologies by providing quick sanity checks and preliminary estimates that help identify potential issues before investing in detailed analysis. This module introduces the fundamental mathematical approaches used for quick capacity calculations in IT environments, covering estimation techniques, simple queuing concepts, and practical shortcuts commonly used in industry.

## Key Concepts

### 1. The Power of 10 Approach

One of the most valuable quick estimation techniques is the "Power of 10" or "10x rule" approach. This method recognizes that in IT systems, small changes in parameters often result in exponential changes in resource requirements. When capacity planning, if you cannot precisely calculate the answer, estimating within an order of magnitude (factor of 10) is often sufficient for initial decision-making.

The power of 10 approach works because IT systems typically exhibit non-linear behavior. For example, adding users to a system may not simply require proportional additional resources—cache hit rates, contention for shared resources, and threshold effects can cause resource requirements to grow much faster than linearly. By thinking in orders of magnitude, capacity planners can quickly determine whether proposed solutions are feasible without getting bogged down in precise calculations.

### 2. Little's Law and Simple Queuing Estimates

Little's Law is a fundamental principle in queuing theory that provides a simple relationship between three key metrics: average number of customers in the system (L), average arrival rate (λ), and average time a customer spends in the system (W). The formula is expressed as:

**L = λ × W**

In IT capacity planning, this translates directly to understanding system performance. For example, if a web server receives 100 requests per second (arrival rate) and each request takes 0.5 seconds to process (response time), then on average, there are 50 concurrent requests being processed by the system. This simple relationship helps estimate required queue depths, buffer sizes, and thread counts.

### 3. Utilization and Response Time Relationships

A critical concept in quick capacity math is understanding the relationship between resource utilization and response time. Using the simple queuing approximation, when utilization (ρ) approaches 100%, response times increase dramatically. The approximate relationship is:

**Response Time Factor = 1 / (1 - ρ)**

This means if a system is operating at 50% utilization, response time is approximately twice the service time. At 80% utilization, response time becomes 5 times the service time. At 90% utilization, it becomes 10 times. This exponential relationship illustrates why keeping system utilization below certain thresholds is crucial for maintaining acceptable performance.

### 4. 80/20 Rule for Capacity Estimation

The Pareto principle, or 80/20 rule, is frequently applicable in IT capacity planning. Typically, 80% of system load comes from 20% of users or transactions. Similarly, 80% of resource consumption may be caused by 20% of applications. This heuristic helps in quick capacity assessments by focusing attention on the critical subset of users or workloads that matter most.

### 5. Linear Extrapolation and Scaling Factors

When detailed data is unavailable, linear extrapolation provides a simple method for capacity estimation. If you know that a certain configuration handles a specific load, you can estimate capacity for larger or smaller configurations using scaling factors. However, it's crucial to recognize that linear scaling often breaks down—systems may not scale perfectly due to shared resources, contention points, or architectural limitations.

### 6. Rules of Thumb for Common IT Components

Several widely-used rules of thumb exist for quick capacity estimates:

- **CPU Estimation**: One CPU core can typically handle approximately 200-500 HTTP requests per second for simple web applications, though this varies significantly based on application complexity.
- **Memory Estimation**: A rough guideline is 1-2 GB of RAM per 100 concurrent users for typical web applications, plus additional memory for the operating system and database caches.
- **Disk I/O**: A standard disk drive (7200 RPM) can handle approximately 100-150 IOPS, while SSD drives can handle 10,000-100,000+ IOPS depending on the model.
- **Network Bandwidth**: A 1 Gbps network interface can theoretically handle approximately 800 Mbps of practical throughput, accounting for protocol overhead.

### 7. The "Three Numbers" Quick Test

Experienced capacity planners often use a simple sanity check based on three key numbers: the peak concurrent users, the average request size, and the available bandwidth. Multiplying these gives a quick estimate of whether the network infrastructure is adequate. For example, 1000 concurrent users each downloading 1 MB of data at peak would require approximately 8 Gbps of network capacity—clearly exceeding a single 1 Gbps link.

## Examples

### Example 1: Quick Web Server Capacity Estimate

**Problem**: Estimate how many web servers are needed to handle 10,000 concurrent users, assuming each user generates 2 requests per minute, and each request requires 100ms of CPU time on a single core.

**Solution Using Quick Math**:

Step 1: Calculate total requests per second

- 10,000 users × 2 requests/minute = 20,000 requests/minute
- 20,000 / 60 = approximately 333 requests per second

Step 2: Calculate CPU cores needed

- Each request takes 100ms = 0.1 seconds of CPU time
- For 333 requests/second: 333 × 0.1 = 33.3 CPU-seconds per second
- This means we need approximately 33-34 CPU cores to handle this load at 100% utilization

Step 3: Apply utilization factor

- We should not run at 100% utilization; target 70% utilization
- 34 / 0.7 = approximately 48-50 cores needed

Step 4: Estimate servers

- If each server has 8 cores: 50 / 8 = 6.25, round up to 7 servers
- Add redundancy: 7 × 1.5 = approximately 10-11 servers

**Answer**: Approximately 10-11 web servers with 8 cores each would be needed for this load.

### Example 2: Database Connection Pool Sizing

**Problem**: An application has 500 concurrent users, each user think time is 5 seconds, and average database query time is 200ms. Determine appropriate connection pool size.

**Solution Using Little's Law**:

Step 1: Calculate effective request rate

- With 5-second think time, each user makes 1 request every 5 seconds
- Request rate = 500 users / 5 seconds = 100 requests per second

Step 2: Apply Little's Law

- L = λ × W (where W = response time)
- L = 100 requests/sec × 0.2 seconds = 20 connections needed

Step 3: Add safety margin

- Account for variance: 20 × 1.5 = 30 connections
- Typical practice suggests 30-40 connections for this workload

**Answer**: A connection pool of 30-40 database connections would be appropriate.

### Example 3: Storage Capacity Quick Estimate

**Problem**: Estimate storage requirements for a video streaming service with 100,000 users, where each user stores an average of 50 videos in their playlist, each video averages 500 MB.

**Solution**:

Step 1: Calculate total storage for user data

- 100,000 users × 50 videos × 500 MB
- = 100,000 × 25,000 MB
- = 2,500,000,000 MB = 2.5 PB

Step 2: Apply 80/20 rule (not all videos are unique)

- Assume only 20% are unique content (rest are duplicates)
- Unique content: 2.5 PB × 0.2 = 0.5 PB

Step 3: Add overhead for redundancy and growth

- RAID/backup overhead: 0.5 × 1.5 = 0.75 PB
- Growth margin (20%): 0.75 × 1.2 = 0.9 PB

**Answer**: Approximately 0.9-1 PB of storage would be needed.

## Exam Tips

1. **Memorize Little's Law**: L = λ × W is one of the most frequently tested formulas in capacity planning exams. Understand how to rearrange it to solve for any variable.

2. **Know the Utilization-Response Time Relationship**: Remember that response time increases exponentially as utilization approaches 100%. At 90% utilization, response time is 10 times the service time.

3. **Apply Order of Magnitude Thinking**: When exact calculations aren't possible, use powers of 10 to provide reasonable estimates. This demonstrates understanding of system behavior.

4. **Practice Unit Conversions**: Be comfortable converting between seconds, milliseconds, requests per second, and other common units used in capacity calculations.

5. **Understand When Quick Math Is Appropriate**: Quick estimation techniques are useful for initial estimates and sanity checks but not for final capacity decisions requiring precision.

6. **Remember the 80/20 Rule**: This heuristic frequently appears in exam questions and helps simplify complex capacity problems by focusing on the critical 20% of users or workloads.

7. **Include Safety Margins**: Always apply appropriate safety factors (typically 1.5x to 2x) when making capacity recommendations to account for unexpected loads and growth.
