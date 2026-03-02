# Link Control: DLC Services

### Key Points

- **Framing**: Adding a header and trailer to data frames to identify frame boundaries and synchronization.
  - Frame format: `Preamble + Data + Footer`
  - Bit rate: 1/4 of the transmission rate (1 bit reserved for synchronization)
- **Flow Control**: Regulating data transfer to prevent network congestion.
  - Windowing: sender sends data in fixed-size segments (window) until receiver acknowledges sending a frame.
  - Window size: `w = (MTU - 16) / (8 * transmission rate)`
- **Error Control**: Detecting and correcting errors in transmitted data.
  - **Cyclic Redundancy Check (CRC)**: calculates a checksum of received frames and compares it to the original checksum.
  - **Parity bits**: adds an extra bit to each frame for error detection.
- **Connectionless and Connection-Oriented**:
  - Connectionless: no handshake, sender sends frames without receiver acknowledgement.
  - Connection-Oriented: establishes a connection before data transfer, sender and receiver exchange handshakes.
- **Data Link Layer Protocols**:
  - Ethernet: CSMA/CD, CSMA/PRAM
  - PPP (Point-to-Point Protocol): frames data in 512-byte segments, adds error-checking codes.
  - HDLC (High-Level Data-Link Control): frames data in packets, adds error-checking codes.
- **High-Level Data Link (HDLC) Protocol**:
  - Establishes connection between devices.
  - Frames data in packets, adds error-checking codes.
  - Uses 16-bit sequence numbers to detect errors.

### Important Formulas and Definitions

- **MTU (Maximum Transmission Unit)**: maximum size of a frame or packet.
- **CRC (Cyclic Redundancy Check)**: `C(x) = \sum_{i=0}^{n-1} g_i x_i`, where `g_i` is a polynomial.
- **Parity bits**: `P(x) = \sum_{i=0}^{n-1} p_i x_i`, where `p_i` is a bit.

### Theorems

- **Hadamard's Inequality**: `||\sum_{i=0}^{n-1} a_i x_i|| \leq \sqrt{\sum_{i=0}^{n-1} a_i^2} \cdot ||x||`
- **Error-Correcting Capacity**: `R = \frac{1}{1 + \frac{E_b}{N_0}}`, where `E_b` is the average energy per bit and `N_0` is the noise power spectral density.
