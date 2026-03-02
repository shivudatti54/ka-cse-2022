# **Introduction to Transport Layer**

### 24.3.6: Connection-Oriented Transport (COT)

**Definition:** Connection-Oriented Transport (COT) is a transport-layer protocol that establishes a connection between a sender and a receiver before data is sent. This connection is maintained throughout the transmission of data.

**Key Characteristics:**

- Establishes a connection before data transmission
- Connection is maintained throughout transmission
- Guarantees reliable, error-free delivery of data
- Uses a sequence number to track data packets

**How COT Works:**

1.  The sender initiates the connection by sending a connection request to the receiver.
2.  The receiver accepts the connection request and responds with a connection acknowledgement.
3.  Once the connection is established, the sender and receiver can start sending data to each other.
4.  The sender breaks the connection after data transmission is complete.

**Example:**

Suppose we want to send a file from a sender machine to a receiver machine using COT. The process would be:

1.  The sender initiates the connection by sending a connection request to the receiver.
2.  The receiver accepts the connection request and responds with a connection acknowledgement.
3.  The sender breaks the connection after transmitting the file.

### 24.3.7: Connectionless Transport (CCL)

**Definition:** Connectionless Transport (CCL) is a transport-layer protocol that does not establish a connection before data transmission. Instead, each data packet is sent independently and does not guarantee reliable delivery.

**Key Characteristics:**

- No connection establishment before data transmission
- No connection maintenance during transmission
- No guarantee of reliable, error-free delivery of data
- Uses sequence numbers to track individual data packets

**How CCL Works:**

1.  The sender sends a data packet to the receiver without establishing a connection.
2.  The receiver receives the data packet and acknowledges its receipt.
3.  The sender breaks the connection after transmitting a single data packet.

**Example:**

Suppose we want to send a series of email messages from a sender machine to a receiver machine using CCL. The process would be:

1.  The sender sends an email message to the receiver without establishing a connection.
2.  The receiver receives the email message and acknowledges its receipt.
3.  The sender breaks the connection after transmitting a single email message.

### 24.3.8: Transport Layer Protocols

**Definition:** Transport layer protocols are used to provide reliable data transfer between devices on a network.

**Types of Transport Layer Protocols:**

- **Connection-Oriented Transport (COT):** Establishes a connection before data transmission and guarantees reliable, error-free delivery of data.
- **Connectionless Transport (CCL):** Does not establish a connection before data transmission and does not guarantee reliable, error-free delivery of data.

**Key Protocols:**

- **TCP (Transmission Control Protocol):** A COT protocol that guarantees reliable, error-free delivery of data.
- **UDP (User Datagram Protocol):** A CCL protocol that does not guarantee reliable, error-free delivery of data.

### 24.3.9: Transport Layer Functions

**Definition:** Transport layer functions are used to provide reliable data transfer between devices on a network.

**Key Functions:**

- **Segmentation and Reassembly:** Breaks data into smaller segments and reassembles them at the receiving end.
- **Error Detection and Correction:** Detects and corrects errors in data packets.
- **Flow Control:** Regulates the amount of data sent by a device to prevent network congestion.

**Key Protocols:**

- **TCP:** Provides segmentation and reassembly, error detection and correction, and flow control.
- **UDP:** Provides segmentation and reassembly, but does not provide error detection and correction or flow control.
