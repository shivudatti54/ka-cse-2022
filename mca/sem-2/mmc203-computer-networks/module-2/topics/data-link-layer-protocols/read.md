# Data Link Layer Protocols


## Table of Contents

- [Data Link Layer Protocols](#data-link-layer-protocols)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Framing in Data Link Layer](#1-framing-in-data-link-layer)
  - [2. Flow Control Protocols](#2-flow-control-protocols)
  - [3. Error Detection and Correction](#3-error-detection-and-correction)
  - [4. Data Link Layer Protocols](#4-data-link-layer-protocols)
- [Examples](#examples)
  - [Example 1: Bit Stuffing Problem](#example-1-bit-stuffing-problem)
  - [Example 2: Hamming Code Calculation](#example-2-hamming-code-calculation)
  - [Example 3: Stop-and-Wait Efficiency Calculation](#example-3-stop-and-wait-efficiency-calculation)
- [Exam Tips](#exam-tips)

## Introduction

The Data Link Layer is the second layer in the OSI (Open Systems Interconnection) model, functioning as the protocol layer that transfers data between two directly connected nodes on a network. While the Physical layer deals with the actual transmission of raw bits over the communication channel, the Data Link Layer provides node-to-node communication, framing data into manageable packets, and implementing error detection and flow control mechanisms. This layer serves as the backbone of reliable network communication, ensuring that data transferred from the Network layer is properly formatted, protected against errors, and delivered in an orderly fashion.

In the context of 's Computer Science and Engineering curriculum, understanding Data Link Layer protocols is fundamental for several reasons. First, these protocols form the foundation upon which higher-layer networking concepts are built. Second, many interview questions for IT companies (including service-based companies like TCS, Infosys, and product-based companies like Cisco, Juniper) include topics from this layer. Third, practical networking troubleshooting often requires understanding how frames are encapsulated, transmitted, and checked for errors. The protocols discussed in this module—including framing techniques, flow control mechanisms, and error detection/correction methods—are essential knowledge for any computer science engineer.

## Key Concepts

### 1. Framing in Data Link Layer

The Data Link Layer receives packets from the Network layer and encapsulates them into **frames**. Framing provides synchronization between the sender and receiver, identifies the beginning and end of each frame, and allows error detection at the frame level. There are two primary methods for framing: character-oriented framing and bit-oriented framing.

**Character-Oriented Framing:** This method uses special characters to delimit frames. The most common approach is byte stuffing (or character stuffing), where a special escape character (ESC) is used to distinguish between data and control characters. For example, if the flag character (such as DLE STX for start and DLE ETX for end) appears in the data, it is stuffed with an escape character. The receiver then removes the stuffed characters to recover the original data. This method is suitable for text-based communication but is less efficient for binary data.

**Bit-Oriented Framing:** In bit-oriented framing, frames are delimited by a specific bit pattern (typically 01111110). The technique of **bit stuffing** is used where the sender inserts an extra '0' after every five consecutive '1's in the data. When the receiver encounters five consecutive '1's followed by a '0', it removes the '0' to restore the original data. This method is more flexible and can handle any type of data, making it the preferred approach in modern protocols like HDLC (High-Level Data Link Control).

### 2. Flow Control Protocols

Flow control ensures that the sender does not overwhelm the receiver with data faster than it can process. Two primary flow control mechanisms are implemented at the Data Link Layer.

**Stop-and-Wait Protocol:** In this simplest flow control method, the sender transmits a single frame and waits for an acknowledgment (ACK) from the receiver before sending the next frame. If the ACK is received, the sender proceeds with the next frame; if a timeout occurs (or a Negative Acknowledgment NAK is received), the sender retransmits the current frame. While simple to implement, this protocol has very low channel utilization, especially when the propagation delay is large relative to the transmission time. The efficiency of Stop-and-Wait is given by: Efficiency = 1 / (1 + 2a), where a = propagation time / transmission time.

**Sliding Window Protocol:** This protocol allows multiple frames to be in transit simultaneously, significantly improving throughput. The "window" represents the range of frame sequence numbers that the sender can use without receiving acknowledgments. The window has a sender side (allowing unacknowledged frames) and a receiver side (specifying acceptable frame numbers). Each ACK can be cumulative (acknowledging multiple frames) or selective (acknowledging specific frames). The Go-Back-N ARQ (Automatic Repeat reQuest) and Selective Repeat ARQ are two implementations of the sliding window protocol. In Go-Back-N, if a frame is lost, all subsequent frames are retransmitted. In Selective Repeat, only the lost frame is retransmitted, requiring additional buffer management at the receiver.

### 3. Error Detection and Correction

Errors can occur during transmission due to noise, interference, or signal attenuation. The Data Link Layer implements various techniques to detect and sometimes correct these errors.

**Parity Checking:** Single-bit parity adds a parity bit to make the total number of 1s either even (even parity) or odd (odd parity). While simple, it can only detect odd numbers of bit errors and cannot correct them. Two-dimensional parity extends this concept by organizing data into rows and columns, providing better error detection capability.

**Cyclic Redundancy Check (CRC):** CRC is a powerful polynomial code used extensively in data networks. The sender performs polynomial division of the data bits by a predetermined generator polynomial, resulting in a remainder that becomes the CRC code. The receiver performs the same division and compares the remainder. If they match, the frame is assumed error-free; otherwise, an error is detected. CRC can detect all single-bit errors, burst errors up to the degree of the polynomial, and has a very high probability of detecting multiple errors.

**Hamming Code:** This is an error-correcting code that can correct single-bit errors and detect double-bit errors. Hamming codes use redundant bits (parity bits) placed at specific positions in the data word. The number of parity bits (r) required for a data word of length (m) is determined by the inequality: 2^r ≥ m + r + 1. When a bit error occurs, the receiver calculates which bit is in error by checking the parity bits and can flip the erroneous bit to correct it.

### 4. Data Link Layer Protocols

**HDLC (High-Level Data Link Control):** HDLC is a bit-oriented, synchronous protocol that provides reliable synchronous serial communication. It supports both point-to-point and point-to-multipoint configurations. HDLC defines three types of stations: Primary (controls the link), Secondary (operates under primary's control), and Combined (can be both). It uses three frame types: Information frames (I-frames) for data transfer, Supervisory frames (S-frames) for flow and error control, and Unnumbered frames (U-frames) for link management. HDLC operates in three modes: Normal Response Mode (NRM), Asynchronous Balanced Mode (ABM), and Asynchronous Response Mode (ARM).

**PPP (Point-to-Point Protocol):** PPP is a Data Link Layer protocol used for establishing direct connections between two nodes. It is commonly used for dial-up internet connections and for connecting routers over serial links. PPP consists of three main components: Link Control Protocol (LCP) for establishing, configuring, and testing the data link connection; Network Control Protocols (NCPs) for configuring and managing different network layer protocols; and a framing method for encapsulating datagrams. PPP supports error detection, authentication (through PAP and CHAP protocols), and compression. Unlike HDLC, PPP is byte-oriented and uses byte stuffing for framing.

## Examples

### Example 1: Bit Stuffing Problem

**Problem:** Apply bit stuffing to the following data stream: 011011111011111101

**Solution:**

Bit stuffing rule: Insert a '0' after every five consecutive '1's.

1. Start scanning the data from left to right
2. 011011111011111101

- First occurrence of five consecutive 1s: 11111 (positions 5-9)
- After this, insert a '0': 011011111**0**01111101

3. Continue scanning after the inserted bit

- Now we have: 011011111001111101
- Next five consecutive 1s: 11111 (positions 9-13)
- After this, insert another '0': 0110111110011111**0**01

**Final stuffed data:** 01101111100111110101

The receiver will reverse this process by removing each '0' that follows five consecutive '1's.

### Example 2: Hamming Code Calculation

**Problem:** Encode the 8-bit data word 10101010 using Hamming code with even parity.

**Solution:**

Step 1: Determine number of parity bits (r)
For m = 8 data bits: 2^r ≥ 8 + r + 1
2^3 = 8 ≥ 9 (false)
2^4 = 16 ≥ 13 (true)
Therefore, we need r = 4 parity bits.

Step 2: Position the bits
Hamming code positions: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
Parity bits at positions: 1, 2, 4, 8 (powers of 2)
Data bits at remaining positions: 3, 5, 6, 7, 9, 10, 11, 12

Position: 1 2 3 4 5 6 7 8 9 10 11 12
Type: P P D P D D D P D D D D
Data: 1 0 1 0 1 0 1 0 1 0

Step 3: Calculate parity bits (even parity)

- P1 (position 1): covers positions 1,3,5,7,9,11
  Bits: P1, 1, 1, 0, 1, 0 → Need P1=1 to make total 1s even
- P2 (position 2): covers positions 2,3,6,7,10,11
  Bits: P2, 1, 0, 0, 0, 0 → Need P2=1 (1+1=2, even)
- P4 (position 4): covers positions 4,5,6,7,12
  Bits: P4, 1, 0, 1, 0 → Need P4=0 (1+1=0=even)
- P8 (position 8): covers positions 8,9,10,11,12
  Bits: P8, 0, 1, 0, 0 → Need P8=1 (1+1=2, even)

Step 4: Final encoded word
Position: 1 2 3 4 5 6 7 8 9 10 11 12
Data: 1 1 0 0 1 0 1 1 0 1 0

**Hamming code: 110010110101**

### Example 3: Stop-and-Wait Efficiency Calculation

**Problem:** Calculate the channel efficiency of a Stop-and-Wait protocol given that the propagation delay is 20 ms and the frame transmission time is 2 ms.

**Solution:**

Given: Propagation time (Tp) = 20 ms, Transmission time (Tt) = 2 ms

For Stop-and-Wait protocol:
Efficiency = Tt / (Tt + 2 × Tp)

Efficiency = 2 / (2 + 2 × 20)
Efficiency = 2 / (2 + 40)
Efficiency = 2 / 42
Efficiency = 0.0476 or approximately 4.76%

This very low efficiency demonstrates why Stop-and-Wait is impractical for networks with high propagation delays. In satellite communications (where propagation delay is around 270 ms), the efficiency would be even worse, making sliding window protocols essential.

## Exam Tips

1. **Remember the bit stuffing rule:** Always insert a '0' after five consecutive '1's in the data. The receiver removes the '0' after five '1's to recover original data.

2. **Difference between HDLC and PPP:** HDLC is bit-oriented and primarily used for synchronous connections; PPP is byte-oriented and commonly used for dial-up and serial connections.

3. **Hamming code formula:** Remember 2^r ≥ m + r + 1 for determining the number of parity bits needed. This is frequently asked in exams.

4. **Stop-and-Wait efficiency formula:** Efficiency = 1 / (1 + 2a), where a = Tp/Tt. Understand that high propagation delay drastically reduces efficiency.

5. **CRC polynomial properties:** A good CRC generator should have a degree at least equal to the maximum burst error length to be detected, plus one.

6. **Frame types in HDLC:** I-frames carry user data, S-frames handle flow/error control (RR, RNR, REJ), and U-frames manage link establishment (SNRM, SABM, DISC).

7. **Flow control vs Error control:** Flow control prevents the receiver from being overwhelmed, while error control deals with detecting and retransmitting corrupted frames.

8. **Sliding window advantages:** Remember that sliding window protocols achieve much higher efficiency than Stop-and-Wait, especially when the bandwidth-delay product is large.
