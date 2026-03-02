# Sliding Window Protocol

### Overview

- Implement a sliding window protocol in the data link layer to manage data transfer efficiently.
- The protocol is used in connectionless protocols like Ethernet and PPP.

### Key Points

- **Sliding Window Protocol:**
  - A connection-oriented protocol that uses a sliding window to control data transfer.
  - The sender and receiver agree on a window size, which determines the amount of data that can be sent at once.
- **Windowing Parameters:**
  - **Window Size (w):** The maximum amount of data that can be sent at once.
  - **Acknowledgement (ACK) Window:** The window in which the receiver acknowledges received data.
- **Flow Control:**
  - Prevents network congestion by controlling the amount of data sent.
  - Ensures reliable data transfer by detecting errors and retransmitting data if necessary.
- **Theorem:**
  - **Theorem:** If the sender sends data at a rate of x packets per second and the window size is w, then the effective transmission rate is min(x, w) packets per second.

### Important Formulas

- **Effective Transmission Rate:** min(x, w)
- **Window Update:** w = min(w, x)

### Definitions

- **Flow Control:** A mechanism to prevent network congestion by controlling the amount of data sent.
- **Sliding Window:** A technique used in connectionless protocols to manage data transfer efficiently.

### Notes

- The sliding window protocol is used in connection-oriented protocols like TCP (Transmission Control Protocol).
- The window size and acknowledgement window are used to control data transfer and ensure reliable data transfer.
