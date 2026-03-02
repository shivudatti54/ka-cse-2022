# **And Find the Number of Packets Dropped**

### Key Definitions

- **Packet**: a small unit of data transmitted over a network.
- **Packet Loss**: the number of packets that are not received by a destination.
- **Error**: a modification to a packet that makes it unusable by the destination.

### Key Formulas

- **Packet Loss Rate (PLR)**: PLR = (Number of packets dropped / Total number of packets transmitted) \* 100
- **Bit Error Rate (BER)**: BER = (Number of errors / Total number of bits transmitted) \* 100

### Key Theorems

- **Poisson Distribution**: used to model packet loss in a network. It assumes that packet loss is independent and identically distributed.

### Key Points

- **Types of packet loss**:
  - **Dropped packets**: packets that are not received by the destination.
  - **Corrupted packets**: packets that are received but contain errors.
  - **Duplicate packets**: packets that are received multiple times.
- **Causes of packet loss**:
  - **Link failure**: physical damage to the network connection.
  - **Buffer overflow**: when a network interface buffer is full.
  - **Network congestion**: when too many packets are transmitted at once.
- **Measuring packet loss**:
  - **Peak packet loss**: the highest packet loss rate during a given time period.
  - **Average packet loss**: the average packet loss rate over a given time period.
