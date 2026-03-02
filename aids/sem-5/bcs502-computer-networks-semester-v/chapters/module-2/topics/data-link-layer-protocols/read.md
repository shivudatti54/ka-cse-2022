# Data Link Layer Protocols (CN - Semester V, Module 2)

## Introduction

The Data Link Layer (DLL) is the second layer in the OSI model and is crucial for reliable point-to-point and point-to-multipoint communication across a network. Its primary responsibility is to take a raw transmission facility (the Physical Layer) and transform it into a line that appears free of transmission errors to the network layer above it. This is achieved through **Data Link Layer Protocols**, which define the rules for framing, error control, flow control, and access control on a shared medium.

## Core Concepts

The key functions managed by data link layer protocols are:

### 1. Framing
The DLL encapsulates network layer datagrams into **frames** by adding a header and a trailer. This process allows the receiver to identify the start and end of a frame. Common framing methods include:
*   **Character Counting:** Uses a field in the header to specify the number of characters in the frame.
*   **Flag Bytes with Byte Stuffing:** Uses special bytes (like `FLAG = 0x7E`) to delimit the frame. If the flag byte appears in the data, a special escape byte (`ESC = 0x7D`) is inserted before it.
*   **Bit Stuffing:** The physical bit pattern of the delimiter flag (e.g., `01111110`) is used. The sender inserts ("stuffs") an extra `0` bit after any sequence of five consecutive `1`s in the data. The receiver removes this extra `0`, ensuring the flag sequence is unique.

**Example:** In bit stuffing, data `01111111` would be transmitted as `011111011` to avoid being mistaken for a flag.

### 2. Error Control
Errors introduced during transmission must be detected and often corrected. Protocols achieve this through:
*   **Error Detection:** Techniques like **Parity Check**, **Checksum**, and, most commonly, **Cyclic Redundancy Check (CRC)** are used. CRC appends a redundant checksum to the frame trailer, allowing the receiver to detect errors with very high probability.
*   **Error Correction:** Using methods like **Automatic Repeat Request (ARQ)**, where the receiver sends an acknowledgment (ACK) for correctly received frames or a negative acknowledgment (NAK) for erroneous ones. The sender retransmits frames that are not acknowledged.

### 3. Flow Control
This mechanism prevents a fast sender from overwhelming a slow receiver. It regulates the amount of data the sender can transmit before waiting for acknowledgment.
*   **Stop-and-Wait ARQ:** The simplest protocol. The sender transmits one frame and then waits for an ACK before sending the next.
*   **Sliding Window Protocol:** Allows multiple frames to be in transit simultaneously. The window size dictates the maximum number of unacknowledged frames. This is far more efficient for high-latency links. Protocols like **Go-Back-N** and **Selective Repeat** are implementations of this concept.

### 4. Access Control (for Shared Media)
When multiple devices share a common broadcast channel (e.g., in LANs), the Media Access Control (MAC) sub-layer determines who gets to transmit next.
*   **Contention-based (Random Access):** Protocols like **ALOHA** and **CSMA/CD** (used in classic Ethernet) allow stations to transmit anytime. They rely on collision detection and random back-off times to resolve conflicts.
*   **Controlled Access:** Protocols like **Token Passing** grant transmission rights in a controlled, deterministic manner, preventing collisions entirely.

## Key Data Link Protocols

*   **HDLC (High-Level Data Link Control):** A bit-oriented, synchronous protocol that is the basis for many others. It uses bit stuffing and supports both point-to-point and multipoint configurations.
*   **PPP (Point-to-Point Protocol):** A simple, byte-oriented protocol widely used for direct connections between two nodes (e.g., dial-up internet). It provides framing, error detection, and authentication.
*   **Ethernet (IEEE 802.3):** The dominant LAN protocol. It defines the MAC sub-layer protocol (CSMA/CD for half-duplex) and framing format for wired networks.

---

## Key Points / Summary

*   **Purpose:** The Data Link Layer provides reliable, error-free communication over the physical link between two directly connected nodes.
*   **Main Functions:** The core duties are **Framing**, **Error Control**, **Flow Control**, and for LANs, **Access Control**.
*   **Framing:** Methods like bit/byte stuffing are used to delineate frames on a bit stream.
*   **Error Control:** Relies on detection mechanisms (like CRC) and correction mechanisms (like ARQ).
*   **Flow Control:** Manages data flow to prevent receiver overload, using protocols like Stop-and-Wait or the more efficient Sliding Window.
*   **Protocol Examples:** HDLC, PPP, and Ethernet are fundamental protocols that implement these concepts for different network environments.
*   **MAC Sublayer:** Specifically handles how devices on a shared medium gain access to transmit data.