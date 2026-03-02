# Controlled Access Protocols in Data Communication

## Introduction

In computer networks, when multiple devices share a common communication channel, there arises a critical challenge: how to regulate access to the medium to prevent data collisions and ensure efficient data transmission. This problem is addressed by Media Access Control (MAC) protocols at the Data Link Layer. Controlled access protocols represent a fundamental category of MAC protocols where nodes must obtain explicit permission before transmitting data on the shared medium.

Unlike random access protocols (such as ALOHA or CSMA) where stations transmit freely and deal with collisions afterward, controlled access protocols coordinate transmissions through a systematic approach. This coordination ensures that only one station transmits at a time, completely eliminating collisions on the channel. Controlled access methods are particularly valuable in environments where reliability and predictable latency are critical, such as in industrial control systems, legacy local area networks, and certain wireless applications.

The importance of controlled access protocols in 's Computer Networks syllabus cannot be overstated. These protocols form the backbone of traditional Ethernet implementations and token-ring networks, demonstrating how orderly access to shared resources can be achieved through proper synchronization. Understanding these protocols prepares students to appreciate modern network design principles and the trade-offs between complexity, efficiency, and reliability in communication systems.

## Key Concepts

### Overview of Access Methods

Data communication networks that use a shared transmission medium require protocols to manage access and prevent simultaneous transmissions that would result in collisions. Access methods are broadly categorized into three main types: random access, controlled access, and channelization. Controlled access methods differ from random access in that they provide an orderly mechanism where stations take turns transmitting, rather than competing for the channel randomly.

The fundamental characteristic of all controlled access protocols is that a station must receive permission (either explicitly or implicitly) before it can transmit data. This permission-based approach eliminates the possibility of collisions entirely, making the channel utilization highly predictable, though potentially less efficient under light load conditions compared to random access methods.

### Types of Controlled Access Protocols

**1. Reservation**

In reservation-based protocols, the shared channel is divided into two distinct periods: a reservation period and a data transmission period. During the reservation period, all stations that need to transmit data send brief reservation signals to claim a slot in the upcoming data transmission period. The data channel is then divided into time slots, with each reserved slot assigned to a specific station.

The process works as follows: First, the system announces the beginning of a reservation period. Stations that have data to send transmit their reservation during this period. These reservations are collected by all stations (creating a reservation table). During the subsequent data transmission period, each station transmits in its assigned time slot. This method is particularly effective in scenarios where data traffic is predictable and frame sizes are relatively constant.

A key advantage of reservation protocols is that they can guarantee quality of service for real-time applications. However, they suffer from overhead associated with the reservation process, and if a station reserves a slot but has no data to send, that slot remains unused, leading to inefficiency.

**2. Polling**

Polling is a master-slave controlled access protocol where one designated station (the primary or controller) systematically grants permission to other stations (secondaries) to transmit data. The controller maintains a polling list and visits each station in a predetermined sequence, asking each one if it has data to send.

The polling operation involves two main commands: SELECT (S) and POLL (P). When the controller wants to send data to a secondary station, it sends a SELECT frame. When the controller wants to allow a secondary to transmit, it sends a POLL frame. The polled station, upon receiving the POLL, either transmits data if it has any queued, or sends a NULL frame (or "no data" response) if it has nothing to send.

Polling protocols are commonly used in environments where a central controller makes sense, such as in certain wireless networks (like IEEE 802.11's point coordination function) and legacy IBM SNA networks. The primary advantages include deterministic behavior and the ability to prioritize certain stations. However, the protocol introduces latency as the controller must poll each station in sequence, and the failure of the controller brings down the entire network.

**3. Token Passing**

Token passing is perhaps the most elegant controlled access protocol. In this method, a special frame called a "token" circulates among all stations connected to the network. The token is a control frame that grants the holder the exclusive right to transmit data. A station can only transmit when it possesses the token, and upon completing its transmission (or after a maximum holding time), it must pass the token to the next station.

Token passing networks, such as Token Ring (IEEE 802.5) and Token Bus (IEEE 802.4), operate on the principle of logical ring topology. Each station knows its predecessor and successor in the ring. When a station receives the token, it checks if the token is addressed to it. If so, and if it has data to transmit, it seizes the token, changes it to a data frame, appends its message, and sends it around the ring. The data frame travels through each station until it reaches its destination, which copies the data and marks the frame as "seen." The frame continues to the sender, which then verifies successful transmission and releases a new token.

The token passing method offers several advantages: guaranteed access (no starvation), predictable latency (if the number of stations is known), and excellent efficiency under heavy load conditions. However, token passing has some drawbacks: the complexity of token management, the possibility of token loss (which requires recovery procedures), and the overhead of token circulation.

### Comparison of Controlled Access Methods

| Protocol      | Topology | Collision | Latency     | Efficiency (Heavy Load) | Complexity |
| ------------- | -------- | --------- | ----------- | ----------------------- | ---------- |
| Reservation   | Star/Bus | None      | Variable    | Good                    | Moderate   |
| Polling       | Star     | None      | Predictable | Moderate                | Low        |
| Token Passing | Ring     | None      | Predictable | Very Good               | High       |

## Examples

### Example 1: Understanding Token Passing Operation

**Problem:** In a token ring network with 4 stations (A, B, C, and D) arranged in a logical ring (A→B→C→D→A), Station A has 3 frames to send, Station B has 1 frame, and Stations C and D have none. Describe the token passing operation for one complete cycle.

**Solution:**

1. Initially, assume Station A holds the token and has data to transmit.

2. **Step 1:** Station A (holding token) sends its first data frame. The frame contains the destination address and data payload. The token is consumed (transformed into a data frame).

3. **Step 2:** The data frame circulates through the ring. Station B sees the frame but does not match its address, so it passes it on. Station C and Station D do the same.

4. **Step 3:** The frame reaches Station A (the sender). Since it was marked as "seen" by the destination (which would have been indicated), Station A now knows the transmission was successful. It releases a new token.

5. **Step 4:** The token circulates to Station B. Station B has 1 frame to send, so it captures the token and transmits its data frame.

6. **Step 5:** The token circulates to Station C. Station C has no data, so it immediately passes the token to Station D.

7. **Step 6:** Station D passes the token back to Station A, completing one cycle. Station A still has 2 more frames, so it will transmit those in subsequent cycles.

**Key Point:** In each cycle, every station gets exactly one opportunity to transmit (if it has data), ensuring fairness and preventing starvation.

### Example 2: Polling Protocol Analysis

**Problem:** A polling system has one controller and 5 slave stations. The polling overhead (time to send POLL command) is 1 ms, and each station takes 2 ms to respond if it has data to send. If the probability that any station has data to send is 0.3, calculate the average time to poll all 5 stations.

**Solution:**

**Given:**

- Number of stations = 5
- Polling overhead per station = 1 ms
- Data transmission time (if station has data) = 2 ms
- Probability of data at each station = 0.3

**Calculation:**

For each station:

- Expected time = Polling overhead + (Probability × Data transmission time)
- Expected time = 1 ms + (0.3 × 2 ms) = 1 + 0.6 = 1.6 ms

For 5 stations:

- Total average time = 5 × 1.6 ms = 8 ms

**Answer:** The average time to poll all 5 stations is 8 milliseconds.

### Example 3: Reservation Protocol Calculation

**Problem:** A reservation-based system has a frame structure where each frame consists of a 100-slot reservation period and a 2 ms data transmission period. Each reservation slot is 0.1 ms, and each data slot is 0.5 ms. If there are 10 stations, calculate:
(a) Total time for one frame
(b) Efficiency of the system assuming all stations have data to send

**Solution:**

**(a) Total time for one frame:**

- Reservation period = 100 slots × 0.1 ms = 10 ms
- Data transmission period = 2 ms (given)
- Total frame time = 10 + 2 = 12 ms

**(b) Efficiency calculation:**

- If all 10 stations have data, they use 10 of the 100 available reservation slots
- Data slots used = 10 slots × 0.5 ms = 5 ms
- Total useful time (data transmission) = 5 ms
- Efficiency = Useful time / Total frame time = 5 / 12 ≈ 41.67%

**Note:** With only 10 stations using 100 slots, the efficiency is low. The system would be more efficient if the number of reservation slots matched the number of active stations more closely.

## Exam Tips

1. **Understand the fundamental difference:** Controlled access protocols require permission before transmission, unlike random access protocols where stations transmit freely and handle collisions afterward.

2. **Memorize the three types:** Reservation, Polling, and Token Passing are the three main controlled access protocols. Be able to explain each one with a diagram.

3. **Token passing is collision-free:** Remember that token passing guarantees no collisions because only the station holding the token can transmit. This is a key advantage over CSMA/CD.

4. **Polling uses SELECT and POLL commands:** In polling protocols, the controller sends SELECT to send data to a secondary, and POLL to request data from a secondary.

5. **Reservation divides time into periods:** Remember that reservation protocols have two distinct periods - the reservation period and the data transmission period.

6. **Token Ring vs Token Bus:** Token Ring (IEEE 802.5) uses a physical ring topology, while Token Bus (IEEE 802.4) uses a bus topology but implements logical ring for token passing.

7. **Token recovery is crucial:** In token passing networks, if the token is lost (due to noise or station failure), a token recovery procedure must be initiated. This is an important operational consideration.

8. **Compare efficiency:** Under heavy load conditions, token passing has the best efficiency among controlled access methods because there is no polling overhead during data transmission.

9. **Real-world applications:** Token Ring (IBM) and early Ethernet variants (using token bus) are practical examples of controlled access implementations. Modern Wi-Fi uses CSMA/CA (a random access variant).

10. ** frequently asks:** Previous question papers show emphasis on drawing and explaining the operation of token passing and polling mechanisms. Practice these diagrams thoroughly.
