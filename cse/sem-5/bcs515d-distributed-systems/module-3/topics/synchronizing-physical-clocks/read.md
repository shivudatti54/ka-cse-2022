# Synchronizing Physical Clocks

## Introduction

In distributed systems, physical clocks play a crucial role in maintaining temporal ordering of events and ensuring consistency across multiple machines. Physical clocks, also known as real-time clocks, provide an absolute time reference based on universal time standards like UTC (Coordinated Universal Time). However, due to various factors such as network delays, clock drift, and hardware limitations, maintaining perfect synchronization across all nodes in a distributed system becomes a challenging task.

The importance of clock synchronization in distributed systems cannot be overstated. Applications ranging from financial transactions to distributed databases require precise timing to maintain consistency and ensure correct ordering of operations. When clocks are not synchronized, events may appear to occur in the wrong sequence, leading to data inconsistencies, concurrency issues, and failures in time-critical applications. For instance, in a distributed banking system, if two transactions occur simultaneously on different servers but their clocks are not synchronized, determining which transaction happened first becomes impossible without proper synchronization mechanisms.

This topic covers the fundamental challenges of physical clock synchronization, the algorithms designed to address these challenges, and the practical implementations used in modern distributed systems. We will explore both centralized and decentralized synchronization approaches, including Cristian's algorithm, the Berkeley algorithm, and the Network Time Protocol (NTP), which is widely used on the Internet today.

## Key Concepts

### Clock Drift and Oscillator Imperfections

Physical clocks are typically implemented using crystal oscillators that generate periodic signals. However, no oscillator is perfect, and each crystal oscillates at a slightly different frequency. This phenomenon is known as clock drift. The drift rate is usually measured in parts per million (ppm), where a typical quartz crystal might drift about 10-100 ppm. This means that two clocks initially synchronized perfectly could drift apart by several seconds over a day if left unsynchronized.

The drift rate causes clocks to either run faster (positive drift) or slower (negative drift) than the ideal time. To maintain synchronization, systems must periodically adjust clocks to compensate for this drift. However, sudden large adjustments can cause problems in time-sensitive applications, which is why most synchronization algorithms use gradual adjustments or compensate for accumulated errors over time.

### Clock Synchronization Requirements

For effective clock synchronization in distributed systems, several requirements must be met. First, the clocks must agree on the current time, meaning the difference between any two clocks should be bounded by a small value known as the precision. Second, the clocks should progress forward monotonically, meaning they should never jump backward in time, as this could cause serious issues in applications relying on temporal ordering. Third, the clocks should be accurate, meaning they should be close to the real UTC time, though this requirement varies depending on the application.

The distinction between internal synchronization and external synchronization is important. Internal synchronization ensures that clocks in a distributed system agree with each other, while external synchronization ensures that the clocks agree with an authoritative external time source like UTC. Achieving external synchronization automatically provides internal synchronization, but the reverse is not necessarily true.

### Cristian's Algorithm

Cristian's algorithm, proposed by Flaviu Cristian in 1989, is one of the earliest and simplest clock synchronization algorithms. It uses a centralized approach where a single time server maintains the authoritative time and responds to client requests.

The algorithm works as follows: A client node sends a request to the time server at time T1 (according to the client's local clock). The time server receives the request, immediately reads its accurate time, and sends a reply containing this time value back to the client. The client receives the reply at time T2 (according to the client's local clock). The client then estimates the round-trip time (RTT) as T2 - T1 and assumes that the one-way delay is approximately half of the RTT. The client sets its clock to the server's time plus half the estimated RTT.

The accuracy of Cristian's algorithm depends on the accuracy of the RTT estimation. In networks with highly variable delays, this assumption may not hold well, leading to synchronization errors. The algorithm also has a single point of failure in the time server, which can be addressed by using multiple servers.

### Network Time Protocol (NTP)

Network Time Protocol is the most widely used clock synchronization protocol on the Internet and in modern distributed systems. NTP is a hierarchical protocol organized into strata, where Stratum 1 servers are directly connected to authoritative time sources (like atomic clocks or GPS receivers), Stratum 2 servers synchronize with Stratum 1 servers, and so on.

NTP uses a sophisticated algorithm to achieve synchronization accuracy of typically within milliseconds on local area networks and tens of milliseconds across the Internet. The protocol employs a symmetric mode where peers exchange time messages in both directions, allowing each peer to calculate the offset and delay between its clock and the other's clock. NTP also includes sophisticated algorithms to filter out erroneous time values and select the best sources.

The NTP synchronization process involves multiple rounds of message exchange to improve accuracy and detect incorrect time sources. The protocol maintains a database of associations with various time sources and continuously evaluates their quality to choose the best available time reference.

### The Berkeley Algorithm

The Berkeley algorithm, developed at the University of California, Berkeley, takes a different approach compared to Cristian's algorithm. Instead of having clients simply request the time from a server, the Berkeley algorithm uses a daemon running on a coordinator node that actively queries all machines in the group about their current time values.

In the Berkeley algorithm, the coordinator sends a request to all machines asking for their current time. Each machine replies with its current time value. The coordinator then computes the average of all these time values (excluding its own) and calculates the adjustment needed for each machine. The coordinator sends the adjustment value (either positive or negative) to each machine, which then adjusts its clock accordingly.

One key advantage of the Berkeley algorithm is that it does not assume that the coordinator has the correct time. Instead, it computes a consensus time from the group, making the system more robust against a single faulty clock. The algorithm can also handle situations where some machines have incorrect time values by using averaging techniques that exclude outliers.

### Clock Adjustment Strategies

When synchronizing physical clocks, systems must decide how to apply the correction. There are two main approaches: setting the clock directly to the correct value or gradually adjusting the clock rate over time.

Direct setting, also called clock stepping, simply sets the clock to the correct time. This approach is straightforward but can cause problems in applications that rely on monotonic time progression. If the clock is set backward, applications that have already recorded timestamps might experience inconsistencies.

Gradual adjustment, also called clock slewing, involves speeding up or slowing down the clock rate to gradually converge to the correct time. This approach maintains monotonicity and is preferred in most production systems. Many operating systems provide functions to adjust the system clock gradually, and NTP typically uses this approach for small corrections.

## Examples

### Example 1: Calculating Time Offset Using Cristian's Algorithm

**Problem:** A client node sends a request to a time server at local time 10:00:00.000 (T1). The time server replies with its time as 10:00:00.500. The client receives the reply at local time 10:00:00.520 (T2). Calculate the estimated clock offset and the corrected time that the client should set.

**Solution:**

Step 1: Calculate the round-trip time (RTT)
RTT = T2 - T1 = 10:00:00.520 - 10:00:00.000 = 520 milliseconds

Step 2: Estimate one-way delay
One-way delay = RTT / 2 = 520 / 2 = 260 milliseconds

Step 3: Calculate the clock offset
Clock offset = Server time - Client's estimated arrival time
Server time at sending = 10:00:00.500
Estimated arrival time = Client's send time + one-way delay = 10:00:00.000 + 0.260 = 10:00:00.260
Clock offset = 10:00:00.500 - 10:00:00.260 = 0.240 seconds (240 milliseconds)

Step 4: Calculate the corrected time
Corrected time = Client's receive time + clock offset
Corrected time = 10:00:00.520 + 0.240 = 10:00:00.760 seconds

Therefore, the client should set its clock to 10:00:00.760. The estimated offset is that the client's clock was 240 milliseconds behind the server's clock.

### Example 2: NTP Timestamp Calculation

**Problem:** In an NTP exchange, a client sends a packet with timestamps: Originate Timestamp (T1) = 0xC1A9C5E7.00000000, and receives a reply with Receive Timestamp (T2) = 0xC1A9C5EF.20000000 and Transmit Timestamp (T3) = 0xC1A9C5EF.40000000. The client receives the reply at T4 = 0xC1A9C5F0.10000000. Calculate the round-trip delay and clock offset.

**Solution:**

First, let's convert these hex timestamps to decimal (seconds since NTP epoch):
NTP timestamps are in seconds since January 1, 1900.

T1 = 0xC1A9C5E7 = 3247244007 seconds
T2 = 0xC1A9C5EF = 3247244015 seconds
T3 = 0xC1A9C5EF = 3247244015 seconds
T4 = 0xC1A9C5F0 = 3247244016 seconds

Step 1: Calculate the clock offset
Offset = ((T2 - T1) + (T3 - T4)) / 2
Offset = ((3247244015 - 3247244007) + (3247244015 - 3247244016)) / 2
Offset = (8 + (-1)) / 2 = 7/2 = 3.5 seconds

Step 2: Calculate the round-trip delay
Delay = (T4 - T1) - (T3 - T2)
Delay = (3247244016 - 3247244007) - (3247244015 - 3247244015)
Delay = 9 - 0 = 9 seconds

The offset indicates that the client clock is 3.5 seconds behind the server, and the total round-trip delay is 9 seconds. In practice, NTP performs multiple exchanges and applies filtering to get more accurate results.

### Example 3: Berkeley Algorithm Average Calculation

**Problem:** In a system with three machines (A, B, C) and coordinator node, the coordinator collects the following time readings: Machine A: 10:00:00.000, Machine B: 10:00:00.400, Machine C: 10:00:00.200. The coordinator's own time is 10:00:00.100. Calculate the average time and the adjustments needed for each machine.

**Solution:**

Step 1: Calculate the average time (excluding coordinator)
Average = (A + B + C) / 3
Average = (10:00:00.000 + 10:00:00.400 + 10:00:00.200) / 3
Average = 10:00:00.600 / 3 = 10:00:00.200

Step 2: Calculate the adjustment for each machine
Adjustment = Average - Machine's time

Machine A: Adjustment = 10:00:00.200 - 10:00:00.000 = +0.200 seconds (add 200ms)
Machine B: Adjustment = 10:00:00.200 - 10:00:00.400 = -0.200 seconds (subtract 200ms)
Machine C: Adjustment = 10:00:00.200 - 10:00:00.200 = 0 seconds (no change)

The coordinator would send these adjustment values to each machine. Machine A would advance its clock by 200ms, Machine B would slow down its clock by 200ms, and Machine C would remain unchanged. This brings all three machines to a consensus time of 10:00:00.200.

## Exam Tips

1. **Remember the key difference between Cristian's and Berkeley algorithms**: Cristian's algorithm uses a time server that clients query for the time, while the Berkeley algorithm uses a coordinator that actively polls machines and computes a consensus average time.

2. **NTP Stratum Levels**: Remember that Stratum 0 refers to the actual time source (atomic clock, GPS), Stratum 1 is the primary server directly connected to Stratum 0, and subsequent strata represent increasing network distance from the authoritative source.

3. **Clock Drift Concept**: Understand that physical clocks drift due to oscillator imperfections, measured in parts per million (ppm). This drift necessitates periodic resynchronization.

4. **One-way Delay Estimation**: In Cristian's algorithm, the one-way delay is estimated as half of the round-trip time, assuming symmetric network delays. This is a simplification that may not hold in asymmetric networks.

5. **Internal vs External Synchronization**: Internal synchronization ensures agreement between clocks in a distributed system, while external synchronization ensures agreement with an external time source like UTC.

6. **Clock Adjustment Methods**: Know the difference between clock stepping (direct setting) and clock slewing (gradual rate adjustment). Slewing maintains monotonicity and is preferred in production systems.

7. **Berkeley Algorithm Robustness**: Unlike Cristian's algorithm, the Berkeley algorithm does not require the coordinator to have accurate time—it computes a consensus from the group, making it more robust against a single faulty clock.
