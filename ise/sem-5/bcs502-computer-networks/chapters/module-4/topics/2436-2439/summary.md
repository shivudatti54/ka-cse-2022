# **Revision Notes: 24.3.6-24.3.9 - Introduction to Transport Layer**

## **Introduction**

- The Transport Layer is the fourth layer of the OSI model and provides reliable data transfer between devices.
- It ensures error-free, ordered, and sequential delivery of data between senders and receivers.

## **24.3.6: Transport Layer Protocols**

- **TCP (Transmission Control Protocol)**:
  - Connection-oriented protocol
  - Ensures reliable, error-free data transfer
  - Uses ACK (acknowledgment) packets to confirm data receipt
  - Uses sequence numbers to maintain data order
  - Windowing mechanism to control data transfer rate
- **UDP (User Datagram Protocol)**:
  - Connectionless protocol
  - Fast data transfer with no guarantee of delivery or order
  - Uses ports to identify data sender and receiver

## **24.3.7: Transport Layer Functions**

- **Segmentation and Reassembly**:
  - Breaking down data into smaller segments
  - Reassembling segments at the receiving end
- **Error Detection and Correction**:
  - Using checksums to detect errors
  - Using forward error correction (FEC) to correct errors

## **24.3.8: Transport Layer Metrics**

- **Throughput**:
  - Measured as the amount of data transferred per unit time
- **Delay**:
  - Measured as the time it takes for data to travel from sender to receiver
- **Jitter**:
  - Measured as the variation in delay

## **24.3.9: Transport Layer Theorems**

- **Pareto's Law**:
  - States that 80% of data is transferred within 20% of the total transfer time
- **Gartner's Law**:
  - States that 80% of problems are caused by 20% of the code

## **Important Formulas and Definitions**

- **Packet Loss**:
  - P = (number of lost packets) / (total number of packets)
- **Throughput**:
  - T = (data transferred) / (time taken)
- **Delay**:
  - D = (time taken) - (time delay)

Note: This summary is a concise revision guide and is not intended to be a comprehensive study guide.
