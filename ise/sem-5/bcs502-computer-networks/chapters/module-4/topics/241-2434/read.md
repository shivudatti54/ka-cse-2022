# **24.1-24.3.4: Transport Layer**

## **Introduction**

The Transport Layer is the fourth layer of the OSI model and is responsible for providing reliable data transfer between devices on a network. It ensures that data is delivered in the correct order and that errors are detected and corrected.

## **24.1: Introduction to Transport Layer**

### Definition

The Transport Layer is responsible for providing reliable data transfer between devices on a network.

### Functions

- Provides reliable data transfer between devices
- Ensures that data is delivered in the correct order
- Detects and corrects errors
- Provides flow control to prevent network congestion
- Provides error-free delivery of data

### Examples

- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)

### Key Concepts

- Connection-oriented vs connectionless
- Reliable vs unreliable data transfer
- Flow control and error correction

## **24.2: Transport-Layer Protocols**

### Definition

Transport-Layer protocols are responsible for providing reliable data transfer between devices on a network.

### Types of Transport-Layer Protocols

- **Connection-Oriented Protocols**
  - TCP (Transmission Control Protocol)
  - SAP (Session Assignment Protocol)
- **Connectionless Protocols**
  - UDP (User Datagram Protocol)
  - DCCP (Datagram Congestion Control Protocol)

### Characteristics of Connection-Oriented Protocols

- Establishes a connection before data transfer
- Ensures reliable data transfer
- Provides flow control and error correction

### Characteristics of Connectionless Protocols

- Does not establish a connection before data transfer
- Does not ensure reliable data transfer
- Provides best-effort delivery of data

### Key Concepts

- Handshaking and connection establishment
- Sequence numbers and acknowledgment packets
- Acknowledgment and retransmission

## **24.3: User-Level Transport Protocols**

### Definition

User-Level Transport Protocols are software-based protocols that provide reliable data transfer between applications on different devices.

### Examples

- SCTP (Stream Control Transmission Protocol)
- DCCP (Datagram Congestion Control Protocol)

### Characteristics

- Provide reliable data transfer
- Support multiple streams and connections
- Offer flexibility in error detection and correction

### Key Concepts

- Stream management and multiplexing
- Error detection and correction mechanisms
- Application-level flow control

### 24.3.4: Transport-Layer Security\*\*

---

### Definition

Transport-Layer Security (TLS) is a cryptographic protocol used to secure data transfer between devices on a network.

### How TLS Works

1.  Handshake phase: Establishes a secure connection between the client and server.
2.  Data transfer: Secure data is transferred between the client and server.
3.  Shutdown phase: Terminates the secure connection.

### TLS Components

- **Master Secret**: The shared secret key used for encryption and decryption.
- **Session ID**: A unique identifier for the session.
- **Certificate**: A digital certificate containing the public key and identity information.

### Key Concepts

- Handshake and key exchange
- Encryption and decryption algorithms
- Certificate management and verification
