# Clocks in Distributed Systems

## Introduction

Time is a fundamental concept in computing systems, but distributed systems present unique challenges when it comes to time and clock management. Unlike single-machine systems where a single clock governs all operations, distributed systems consist of multiple autonomous computers, each with its own local clock. These independent clocks rarely keep perfect time, leading to clock drift and synchronization challenges that can significantly impact system behavior and correctness.

The importance of clocks in distributed systems extends far beyond simply knowing the current time. Many critical operations depend on accurate time ordering of events, including transaction processing, deadlock detection, cache coherence protocols, and debugging distributed applications. When events occur across multiple machines, establishing a consistent temporal order becomes essential for maintaining system invariants and ensuring correct operation.

This module explores the fundamental challenges of time in distributed systems, examining both physical clocks that attempt to track real-world time and logical clocks that provide alternative ordering mechanisms. Understanding these concepts is crucial for designing and implementing reliable distributed algorithms that depend on temporal properties.

## Key Concepts

### Physical Clocks and Clock Drift

Physical clocks in computers are typically implemented using crystal oscillators that generate periodic interrupts. These hardware clocks maintain a counter that increments on each interrupt, representing elapsed time since some reference point. The frequency of this oscillation determines the clock's precision, with modern systems typically using clocks with frequencies between 1 MHz and 100 MHz.

**Clock drift** refers to the phenomenon where a clock's rate of time progression deviates from the ideal rate. Every physical clock experiences drift due to manufacturing variations, temperature changes, voltage fluctuations, and aging of components. Drift is typically measured in parts per million (ppm), where a drift of 100 ppm means the clock gains or loses 100 microseconds per second. Typical computer clocks drift between 10 and 100 ppm, resulting in potential errors of several seconds per day.

**Clock skew** is the difference between the readings of two clocks at the same instant. Clock skew can be positive or negative, indicating whether one clock leads or lags another. In distributed systems, clock skew between machines can range from milliseconds in local networks to potentially much larger values in wide-area systems.

### Clock Synchronization Requirements

Clock synchronization in distributed systems aims to ensure that processes maintain sufficiently accurate representations of real time. The requirements for synchronization accuracy vary depending on the application. Some systems require millisecond-level accuracy, while others may tolerate larger discrepancies. The fundamental challenge stems from the impossibility of perfectly synchronizing clocks in asynchronous systems where message delivery times are unpredictable.

Several factors complicate clock synchronization: the non-zero time required for messages to travel between machines, the variable latency of network communications, the inaccuracy of local clock oscillators, and the computational overhead of synchronization protocols. Despite these challenges, various algorithms have been developed to achieve acceptable synchronization in practice.

### Network Time Protocol (NTP)

NTP is the most widely used protocol for clock synchronization on the Internet. Operating in a hierarchical client-server manner, NTP organizes time servers into strata, where Stratum 1 servers are directly connected to authoritative time sources such as atomic clocks or GPS receivers. Lower strata servers synchronize with higher stratum servers, creating a distributed synchronization infrastructure.

NTP uses a sophisticated algorithm that measures round-trip delay and offset between client and server. The protocol performs multiple exchanges to filter out erroneous measurements and converge on accurate time estimates. Typical NTP synchronization achieves accuracy within 10 milliseconds on wide-area networks and within 1 millisecond on local networks. NTP operates continuously, adjusting the local clock gradually through small frequency adjustments (slewing) to avoid discontinuities that could affect running applications.

### Cristian's Algorithm

Cristian's algorithm, proposed by Flaviu Cristian in 1989, provides a simple approach to clock synchronization in client-server systems. The algorithm operates as follows: the client sends a request to the time server, which responds with its current time. The client then sets its clock to the server's time plus half the round-trip time, assuming symmetric communication delays.

The algorithm makes several assumptions: the server's clock is trustworthy, the message delay is predictable, and the round-trip time can be approximated as twice the one-way delay. Cristian's algorithm is particularly suitable for systems where a single time server is available and network delays are relatively small. Its simplicity makes it easy to implement, but it lacks the robustness of more sophisticated approaches.

### Berkeley Algorithm

The Berkeley algorithm, developed at the University of California Berkeley, takes a different approach by having a time daemon actively gather clock readings from other machines, compute a consensus time, and distribute corrections back to all participants. Unlike NTP and Cristian's algorithm, which synchronize with an external time source, Berkeley achieves internal synchronization among a group of machines.

The algorithm works by having the daemon poll each machine for its clock value, calculating the average (possibly weighted by accuracy estimates), and then instructing each machine to advance or retard its clock by a calculated amount. This approach handles missing machines gracefully and can work even when no external time source is available. The Berkeley algorithm is particularly useful in isolated networks where external time references are unavailable.

### Clock Synchronization in Practice

Modern operating systems provide various mechanisms for clock management. The `gettimeofday()` system call in Unix-like systems returns the current time with microsecond precision, though actual accuracy depends on synchronization status. Windows provides similar functionality through the `GetSystemTime()` API. Virtualized environments present additional challenges, as virtual machines may experience inconsistent time progression due to virtualization overhead.

Cloud computing platforms often provide time synchronization services. Amazon Web Services uses the Amazon Time Sync Service, providing highly accurate time via NTP endpoints in each region. Google Cloud Platform offers the Google Public NTP service. These services typically achieve sub-millisecond accuracy relative to UTC, suitable for most distributed applications.

## Examples

### Example 1: Calculating Clock Drift Impact

Consider a distributed database system where transactions are timestamped using local clocks. If two servers have a clock skew of 50 milliseconds and each server processes transactions independently, a transaction timestamped at T on Server A might appear to occur after a transaction timestamped at T+40ms on Server B, even though they occurred concurrently. This can lead to incorrect transaction ordering and violate serializability guarantees.

**Solution**: The system must either synchronize clocks frequently enough to keep skew below acceptable thresholds (less than half the minimum transaction timestamp interval) or use logical timestamps (Lamport clocks) that guarantee correct ordering regardless of physical time differences.

### Example 2: NTP Round-Trip Calculation

Suppose a client sends a request to an NTP server at time T1 (according to the client's clock). The server receives the request at Ts (server time), sends a response, and the client receives it at T4 (client time). The server's response includes Ts and the time it sent the response (T3). The client calculates:

- Round-trip delay = (T4 - T1) - (T3 - Ts)
- Clock offset = ((T3 - Ts) + (T4 - T1)) / 2

If the round-trip delay is 20ms and the server's timestamp indicates it sent the response at T3 = 1000ms (server time), and the client receives it at T4 = 1012ms (client time), then:
- Offset = ((1000 - 995) + (1012 - 1000)) / 2 = (5 + 12) / 2 = 8.5ms

The client would adjust its clock forward by 8.5ms to synchronize with the server.

### Example 3: Cristian's Algorithm in Practice

A client needs to synchronize its clock with a time server. The client sends a request at client time 10:00:00.000 (T1). The server receives the request at 10:00:00.100 (server time) and immediately responds with the time 10:00:00.100. The client receives the response at 10:00:00.120 (T4).

The round-trip time is 120ms, so the one-way delay is approximately 60ms. The client sets its clock to: server time + one-way delay = 10:00:00.100 + 0.060 = 10:00:00.160.

However, if the actual one-way delay was 80ms (asymmetric path), the true server time when the client received the response was 10:00:00.180, meaning the client's clock is now 20ms ahead of the server. This demonstrates the fundamental limitation of Cristian's algorithm when network paths are asymmetric.

## Exam Tips

1. **Distinguish between clock drift and clock skew**: Clock drift is the rate error of a single clock over time, while clock skew is the instantaneous difference between two clocks at a specific moment.

2. **Understand the assumptions of each synchronization algorithm**: Cristian's algorithm assumes symmetric network delays, while the Berkeley algorithm does not require an external time source.

3. **Remember that physical clock synchronization is impossible in asynchronous systems**: This is a fundamental result—you cannot achieve perfect synchronization due to unpredictable message delays.

4. **NTP stratification**: Remember that Stratum 1 servers connect directly to authoritative time sources, and each subsequent stratum synchronizes with the previous one.

5. **Practical accuracy ranges**: NTP typically achieves millisecond accuracy on LANs and 10-100ms on WANs. This is sufficient for many applications but not for real-time control systems.

6. **Clock adjustment methods**: Systems can adjust clocks through slewing (gradual rate adjustment) or stepping (discontinuous jumps). NTP prefers slewing to avoid disrupting running applications.

7. **Logical clocks as an alternative**: When physical clock synchronization is impossible or insufficient, logical clocks (Lamport clocks) provide ordering guarantees that may be sufficient for application requirements.