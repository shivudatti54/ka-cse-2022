# Clocks in Distributed Systems - Summary

## Key Definitions

- **Clock Drift**: The rate at which a clock deviates from true time, typically measured in parts per million (ppm)

- **Clock Skew**: The instantaneous difference between the readings of two clocks at the same physical moment

- **Clock Synchronization**: The process of ensuring that multiple clocks in a distributed system maintain sufficiently close agreement with each other or with an authoritative time source

- **Physical Clocks**: Hardware-based clocks that track real-world time, typically implemented using crystal oscillators

- **Time Protocol (NTP)**: A widely-used protocol for synchronizing clocks over IP networks, organized in a hierarchical stratum structure

## Important Formulas

- **Cristian's Algorithm Clock Setting**: 
  `Client_Time = Server_Time + (Round_Trip_Time / 2)`

- **NTP Offset Calculation**:
  `Offset = ((T3 - T1) + (T4 - T2)) / 2`
  where T1, T2 are client send/receive times and T3, T4 are server send/receive times

- **Clock Drift Rate**:
  `Drift (ppm) = (|Measured_Time - Expected_Time| / Expected_Time) × 10⁶`

## Key Points

1. All physical clocks experience drift due to hardware imperfections, making synchronization necessary in distributed systems

2. Perfect clock synchronization is impossible in asynchronous distributed systems due to unpredictable message delivery times

3. NTP is the Internet standard for clock synchronization, achieving millisecond accuracy on LANs through a hierarchical stratum structure

4. Cristian's algorithm provides simple client-server synchronization but assumes symmetric network delays

5. The Berkeley algorithm achieves internal synchronization among a group without requiring an external time source

6. Clock adjustments should preferably use slewing (gradual rate changes) rather than stepping (sudden jumps) to avoid disrupting applications

7. Virtualized and cloud environments present additional synchronization challenges due to time acceleration or pausing of virtual machines

8. For applications requiring strict event ordering, logical clocks (Lamport clocks) may be more appropriate than physical clocks

## Common Mistakes

1. **Confusing drift with skew**: Drift is a rate error over time, while skew is an instantaneous difference between two clocks at a point in time

2. **Assuming perfect synchronization is achievable**: Students often forget that synchronization is always approximate due to network delays

3. **Ignoring asymmetric delays**: Cristian's algorithm and some NTP modes assume roughly symmetric network paths, which may not hold in practice

4. **Overestimating NTP accuracy**: While NTP is accurate, it typically achieves milliseconds (not microseconds) accuracy even on good network conditions

5. **Applying wrong synchronization approach**: Using physical clocks when logical ordering is all that's required, or vice versa, can lead to unnecessary complexity or incorrect behavior