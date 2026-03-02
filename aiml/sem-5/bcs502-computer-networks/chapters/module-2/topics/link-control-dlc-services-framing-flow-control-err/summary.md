# Link Control

### Introduction

- Link control refers to the process of managing data transmission over a single communication link.
- It ensures the reliable transfer of data between devices.

### DLC Services

- **Framing**: Adding headers and trailers to data packets to identify the start and end of the frame.
- **Flow Control**: Preventing network congestion by regulating the amount of data sent at one time.
- **Error Control**: Detecting and correcting errors that occur during data transmission.

### Connectionless and Connection-Oriented

- **Connectionless**: No established connection between devices; data is sent independently.
- **Connection-Oriented**: Establishes a connection before data transmission; guarantees reliable delivery.

### Data Link Layer Protocols

- **HDLC (High-Level Data Link Control)**: Used for connection-oriented data transfer.
- **SDLC (Synchronous Data Link Control)**: Used for connection-oriented data transfer.

### Important Formulas and Definitions

- **Error Detection**: Used to detect errors in data transmission.
  - **Cyclic Redundancy Check (CRC)**: A mathematical formula to detect errors.
  - **Parity Check**: A method to detect errors using odd or even numbers of 1s.
- **Error Correction**: Used to correct errors in data transmission.
  - **Block Coding**: A method to encode data into blocks to correct errors.
  - **Cyclic Codes**: A type of block code used for error correction.

### Theorems

- **Hadamard Code**: A type of cyclic code used for error correction.
- **Shannon-Hartley Theorem**: A theorem that relates the bandwidth of a communication channel to the data transmission rate.

### Key Points

- Link control is essential for reliable data transfer over a single communication link.
- DLC services include framing, flow control, and error control.
- Connectionless and connection-oriented protocols ensure reliable data transfer.
- HDLC and SDLC are two popular data link layer protocols.
- Error detection and correction techniques, such as CRC and parity check, are used to ensure reliable data transmission.
