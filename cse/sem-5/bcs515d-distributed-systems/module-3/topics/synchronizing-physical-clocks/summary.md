# Synchronizing Physical Clocks - Summary

## Key Definitions and Concepts

- **Physical Clocks**: Real-time clocks that provide absolute time reference based on UTC (Coordinated Universal Time), typically implemented using crystal oscillators.

- **Clock Drift**: The phenomenon where physical clocks run at slightly different rates due to oscillator imperfections, measured in parts per million (ppm).

- **Internal Synchronization**: Clock synchronization where nodes in a distributed system agree with each other.

- **External Synchronization**: Clock synchronization where nodes agree with an authoritative external time source like UTC.

- **Round-Trip Time (RTT)**: The total time taken for a message to travel from sender to receiver and back.

## Important Formulas and Theorems

- **Cristian's Algorithm Offset**: Clock offset = Server time + (RTT/2) - Client receive time

- **NTP Offset Formula**: Offset = ((T2 - T1) + (T3 - T4)) / 2, where T1 is originate, T2 is receive, T3 is transmit, and T4 is destination timestamp.

- **NTP Delay Formula**: Delay = (T4 - T1) - (T3 - T2)

- **Berkeley Algorithm Average**: Average time = (Sum of all client times) / Number of clients

## Key Points

1. Physical clocks in distributed systems cannot remain perfectly synchronized due to clock drift caused by oscillator imperfections and variable network delays.

2. Cristian's algorithm uses a centralized time server and estimates one-way delay as half the round-trip time, making it simple but dependent on symmetric network conditions.

3. The Berkeley algorithm takes a decentralized approach by computing a consensus average time, making it robust against individual clock failures but requiring more message exchanges.

4. Network Time Protocol (NTP) is the industry standard for Internet clock synchronization, organized hierarchically with Stratum 1 servers connected to authoritative time sources.

5. Clock monotonicity is crucial for applications requiring temporal ordering, and gradual adjustments (clock slewing) are preferred over sudden jumps (clock stepping).

6. The accuracy of clock synchronization varies: Cristian's achieves seconds-level, NTP achieves milliseconds on LANs and tens of milliseconds across the Internet.

7. NTP filters multiple time sources and uses sophisticated algorithms to reject erroneous time values and maintain accurate synchronization.

## Common Mistakes to Avoid

1. Confusing internal synchronization (agreement between system clocks) with external synchronization (agreement with UTC).

2. Assuming symmetric network delays when using Cristian's algorithm—this is an approximation that introduces errors.

3. Thinking that clock synchronization is a one-time activity—clocks must be periodically resynchronized due to drift.

4. Believing that setting the clock backward is always safe—this violates monotonicity and can cause serious issues in applications.

## Revision Tips

1. Practice calculating clock offsets using both Cristian's algorithm and NTP formulas with sample timestamp values.

2. Remember the key distinguishing feature: Cristian uses a server with accurate time, while Berkeley computes consensus without requiring an accurate coordinator.

3. Review the stratum hierarchy in NTP: Stratum 0 → Stratum 1 → Stratum 2 → and so on.

4. Understand why gradual clock adjustment (slewing) is preferred over sudden changes (stepping) in production systems.
