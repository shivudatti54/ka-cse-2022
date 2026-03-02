# **24.3.6-24.3.9: Transport Layer Fundamentals**

### 24.3.6: Introduction to Transport Layer

The Transport Layer is the fourth layer of the OSI model and is responsible for ensuring reliable data transfer between devices over a network.

**Definition:** The Transport Layer provides a reliable connection between devices, ensuring that data is delivered in the correct order and without duplication or loss.

**Functions:**

- Provides a connection-oriented or connectionless service
- Ensures reliable data transfer
- Provides error detection and correction
- Provides flow control and congestion control

**Example:**

When you send an email, the Transport Layer ensures that the email is received by the recipient's server without any errors or loss of data.

### 24.3.7: Transport-Layer Protocols - Introduction

Transport-Layer protocols are used to implement the functions of the Transport Layer. There are two main types of Transport-Layer protocols:

- **Connection-Oriented (CO) protocols:** Establish a connection before data is sent
- **Connectionless (CL) protocols:** Do not establish a connection before data is sent

**Types of Transport-Layer Protocols:**

- **TCP (Transmission Control Protocol):** A CO protocol that provides reliable data transfer
- **UDP (User Datagram Protocol):** A CL protocol that provides best-effort delivery
- **SCTP (Stream Control Transmission Protocol):** A CO protocol that provides reliable data transfer and multiplexing

**Key Characteristics:**

- **Reliable data transfer:** Ensures that data is delivered in the correct order and without duplication or loss
- **Error detection and correction:** Detects and corrects errors in data transmission
- **Flow control and congestion control:** Regulates the amount of data sent by a device to prevent network congestion

### 24.3.8: Connectionless Transport-Layer Protocols

Connectionless Transport-Layer protocols do not establish a connection before data is sent.

**Characteristics:**

- **No connection establishment:** No connection is established before data is sent
- **Best-effort delivery:** Data is delivered in the best possible manner, but no guarantee is provided
- **Error detection:** Errors in data transmission are detected, but not corrected

**Examples:**

- **UDP:** A connectionless protocol that provides best-effort delivery
- **ICMP (Internet Control Message Protocol):** A connectionless protocol that provides error detection and correction

### 24.3.9: Connectionless vs. Connection-Oriented Transport-Layer Protocols

Connectionless Transport-Layer protocols and connection-oriented protocols have different characteristics.

**Comparison:**

|                              | Connectionless Protocols                          | Connection-Oriented Protocols                     |
| ---------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| **Connection establishment** | No connection establishment                       | Establishes a connection before data is sent      |
| **Error detection**          | Detects errors, but not corrected                 | Detects and corrects errors                       |
| **Flow control**             | Regulates data sent, but no guarantee is provided | Regulates data sent to prevent network congestion |
| **Reliability**              | Provides best-effort delivery                     | Provides reliable data transfer                   |

In conclusion, the Transport Layer is responsible for ensuring reliable data transfer between devices over a network. Both connectionless and connection-oriented protocols have different characteristics, and the choice of protocol depends on the specific application or service.
