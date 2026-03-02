# Module 2: Data Link Layer Protocols

## Introduction

The Data Link Layer (DLL) is the second layer in the OSI model and is crucial for ensuring reliable point-to-point and point-to-multipoint data transfer across a physical network. It acts as an interface between the physical layer (raw bitstream) and the higher network layers (packets). Its primary responsibility is to take packets from the Network Layer and encapsulate them into **frames** for transmission, handling errors, flow control, and access to the shared medium. This module explores the core protocols that govern these functions.

## Core Concepts & Protocols

The data link layer is primarily concerned with three key functions, each managed by specific types of protocols:

### 1. Framing

Framing is the process of encapsulating a network layer packet with a header and trailer to form a frame. The header contains control information like source and destination addresses, while the trailer typically contains error detection bits.

*   **Example:** A common method is **Byte Stuffing** (or character stuffing). If the designated flag sequence `FLAG` is `01111110`, and this pattern appears in the data, the sender *stuffs* (adds) an extra escape byte (e.g., `ESC`) before it. The receiver removes this `ESC` byte, ensuring the flag is only recognized as a frame delimiter.

### 2. Flow Control

Flow control mechanisms regulate the rate of data transmission between a sender and a receiver to prevent the fast sender from overwhelming the slow receiver. Two fundamental protocols are used:

#### a) Stop-and-Wait ARQ (Automatic Repeat Request)

This is the simplest protocol. The sender transmits a single frame and then waits for an acknowledgment (ACK) from the receiver before sending the next frame. If an ACK is not received within a timeout period, the sender retransmits the frame.

*   **Advantage:** Simple to implement.
*   **Disadvantage:** Highly inefficient, as the channel is idle while waiting for the ACK, leading to low link utilization.

#### b) Sliding Window Protocol

This protocol allows the sender to transmit multiple frames before needing an ACK. The "window" represents a set of sequence numbers the sender can use. As ACKs are received, the window "slides" forward.

*   **Go-Back-N ARQ:** The sender can have up to `N` unacknowledged frames. If a frame is lost or damaged, the receiver discards all subsequent frames, and the sender must retransmit *all* frames starting from the lost one.
*   **Selective Repeat ARQ:** A more efficient method where the receiver individually acknowledges correctly received frames and can buffer out-of-order frames. The sender only retransmits the specific frames that are lost or corrupted. This requires a more complex receiver design.

### 3. Error Control

Error control ensures the integrity of data transferred. It involves:
*   **Error Detection:** Using techniques like **Cyclic Redundancy Check (CRC)**. The sender performs a calculation on the frame's bits to generate a CRC remainder, which is appended to the trailer. The receiver performs the same calculation; if the result doesn't match, the frame contains an error and is discarded.
*   **Error Correction:** Achieved through retransmission (ARQ). When a frame is lost or found to be in error, the receiver requests retransmission by sending a **Negative Acknowledgement (NAK)** or by not sending an ACK, triggering the sender's timeout mechanism.

## Summary of Key Points

| Concept | Protocol/Technique | Primary Function | Key Characteristic |
| :--- | :--- | :--- | :--- |
| **Framing** | Byte Stuffing, Bit Stuffing | Encapsulate packets into frames with delimiters. | Ensures receiver can identify frame boundaries. |
| **Flow Control** | Stop-and-Wait ARQ | Regulate data flow to prevent receiver overflow. | Simple but inefficient; only one frame at a time. |
| | Sliding Window (Go-Back-N) | Allow multiple unacknowledged frames. | More efficient but retransmits all frames after error. |
| | Sliding Window (Selective Repeat) | Allow multiple unacknowledged frames. | Most efficient; only retransmits specific erroneous frames. |
| **Error Control** | CRC (Error Detection) | Detect errors in transmitted frames. | Appends a checksum to the frame trailer. |
| | ARQ (Error Correction) | Recover from errors via retransmission. | Uses ACKs, NAKs, and timeouts for reliability. |

**In essence,** data link layer protocols work in tandem to provide reliable, efficient, and orderly communication over a single link. Understanding the trade-offs between simplicity (Stop-and-Wait) and efficiency (Sliding Window) is fundamental for network engineers.