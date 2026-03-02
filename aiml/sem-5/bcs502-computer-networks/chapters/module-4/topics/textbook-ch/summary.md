# Revision Notes: Transport Layer (Ch)

## Introduction

- The Transport Layer is the fourth layer of the OSI model and is responsible for reliable data transfer between devices.
- It provides error-free, sequential delivery of data between endpoints.
- The Transport Layer uses the Transport Protocol (TCP) and User Datagram Protocol (UDP).

## Transport-Layer Protocols

- **TCP (Transmission Control Protocol)**:
  - Connection-oriented
  - Reliable, sequential delivery of data
  - Error-checking and correction
  - Flow control and congestion control
  - Formula: `R = (s + 1) * (1 + e + h) * (1 + a)` where R = round-trip time, s = signal transmission time, e = error rate, h = overhead, and a = acknowledgement delay
- **UDP (User Datagram Protocol)**:
  - Connectionless
  - Best-effort delivery of data
  - No error-checking or correction
  - Formula: None (as it's a simpler protocol)

## Key Concepts

- **Segmentation**: Breaking down data into smaller packets for transmission.
- **Reassembly**: Reconstructing the original data from the received packets.
- **Flow Control**: Regulating the amount of data sent at one time to prevent network congestion.
- **Congestion Control**: Managing network congestion by regulating the amount of data sent.

## Important Formulas and Definitions

- **Round-Trip Time (R)**: The time it takes for a message to travel from the sender to the receiver and back.
- **Packet Loss**: The loss of a packet during transmission.
- **Error Rate**: The probability of an error occurring during transmission.
- **Segment Size**: The maximum size of a segment.
- **Window Size**: The maximum amount of data that can be sent before receiving an acknowledgement.

## Theorems

- **TCP Congestion Control Theorem**: Regulates the amount of data sent to prevent network congestion.
- **UDP Best-Effort Delivery Theorem**: Provides best-effort delivery of data, but no guarantee of delivery.
