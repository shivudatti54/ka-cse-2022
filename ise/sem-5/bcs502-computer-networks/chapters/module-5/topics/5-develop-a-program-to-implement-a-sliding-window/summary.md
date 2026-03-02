# **Sliding Window Protocol in Data Link Layer**

### Key Points

- **Definition:** A sliding window protocol is a control protocol used in the data link layer to manage data transfer between two nodes in a network.
- **Goal:** To maximize data transfer rate by minimizing the amount of control data sent.
- **Formula:** Window size (W) = Maximum transmission unit (MTU) / Round-trip time (RTT)
- **Key concepts:**
  - **Window size:** The maximum amount of data that can be sent in a single transmission.
  - **Round-trip time (RTT):** The time it takes for a packet to travel from the sender to the receiver and back.
  - **Sliding window:** A window of available bandwidth that moves forward in time as the data transfer continues.

### Important Formulas and Theorems

- **Maximizing data transfer rate:** W = MTU / RTT
- **Sliding window update:** When the sender receives an acknowledgement (ACK), it slides the window forward by W packets.

### Program Implementation

- **Sender:**
  - Initialize window size (W)
  - Send data in segments of size W
  - Receive ACKs and update window size
- **Receiver:**
  - Receive data segments
  - Send ACKs for received data
  - Slide window forward after receiving ACK

### Important Definitions

- **Maximum transmission unit (MTU):** The maximum size of a packet that can be transmitted in a network.
- **Acknowledgement (ACK):** A message sent by the receiver to acknowledge receipt of data.

### Theorems

- **Sliding window protocol theorem:** The sliding window protocol maximizes data transfer rate by minimizing control data.
