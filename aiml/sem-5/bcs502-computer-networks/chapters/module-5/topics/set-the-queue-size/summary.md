# Set the Queue Size

## Computer Networks Module

### Key Points

- **Queue Size**: The maximum number of packets allowed to be stored in a buffer before it is discarded.
- **Types of Queue Sizes**:
  - **Dynamic Queue Size**: Adjusts based on network traffic and demand.
  - **Static Queue Size**: Fixed and not adjusted by the network.
- **Importance of Queue Size**:
  - Reduces packet loss and retransmission.
  - Ensures fair allocation of bandwidth.
  - Improves network performance and efficiency.

### Formulas and Definitions

- **Packet Loss**: The number of packets lost due to congestion or other network issues.
- **Queue Size Formula**: $Q = \lambda \times \frac{1}{\mu}$
  - $Q$: Queue Size
  - $\lambda$: Arrival Rate
  - $\mu$: Service Rate
- **Little's Law**: $L = \lambda \times \frac{1}{\mu}$
  - $L$: Average System Load
  - $\lambda$: Arrival Rate
  - $\mu$: Service Rate

### Theorems

- **M/M/1 Queue Theory**: A simple model for analyzing queue sizes in networks.
- **M/D/1 Queue Theory**: A variation of the M/M/1 model with deterministic service times.

### Revision Tips

- Understand the concept of queue size and its impact on network performance.
- Familiarize yourself with formulas and definitions related to queue sizes.
- Apply Little's Law to analyze system loads in networks.
