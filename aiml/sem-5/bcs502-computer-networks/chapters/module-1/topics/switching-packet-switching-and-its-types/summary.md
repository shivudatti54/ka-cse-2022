# Switching: Packet Switching and its types

=====================================================

## Overview

---

- Switching is a method of routing data packets between nodes in a computer network.
- It is a type of packet switching.

## Packet Switching

---

- A packet is a small data unit that is transmitted independently.
- Packet switching is a technique where packets are transmitted through a network, routed through intermediate nodes to reach their destination.
- Key characteristics:
  - Packets are assigned unique addresses (source and destination).
  - Packets are transmitted independently, and their order is not guaranteed.

## Types of Packet Switching

---

- **Store-and-Forward Switching**
  - Packets are stored in a buffer before being forwarded to the next hop.
  - Prevents packet loss and ensures delivery.
- **Cut-Through Switching**
  - Packets are forwarded without buffering, without error detection.
  - Increases network speed but increases error rate.
- **Virtual Circuit Switching**
  - Establishes a virtual circuit between two nodes before data transmission.
  - Guarantees packet delivery and prevents errors.
- **Cell Switching**
  - Divides data into cells and assigns a cell header to each cell.
  - Used in ATM (Asynchronous Transfer Mode) networks.

## Theorems and Formulas

---

- **Theorem:**

  The packet switching capacity of a network is given by:

  C = λ / (∑μk)

  where:
  - C = packet switching capacity
  - λ = arrival rate
  - ∑μk = sum of service rates

- **Formula:**

  The packet loss rate (PL) is given by:

  PL = λ / (μ \* (1 - P))

  where:
  - PL = packet loss rate
  - λ = arrival rate
  - μ = service rate
  - P = probability of packet loss

## Key Terms

---

- **Packet**: a small data unit that is transmitted independently.
- **Switch**: a node that forwards packets to their destination.
- **Buffer**: a temporary storage area for packets.
- **Virtual Circuit**: a logical connection between two nodes that is established before data transmission.
