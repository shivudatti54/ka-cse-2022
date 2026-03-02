# **Computer Networks Revision Notes: Protocol**

### Introduction

- A protocol is a set of rules that governs the format and exchange of data between devices on a network.
- Protocols ensure that data is transmitted and received correctly, regardless of the devices or networks involved.

### Network Models

- **OSI Model**
  - 7 layers:
    1. Physical (PHY)
    2. Data Link (DLL)
    3. Network (NL)
    4. Transport (TP)
    5. Session (SS)
    6. Presentation (PP)
    7. Application (AP)
  - Each layer has a specific function and interacts with other layers to ensure data exchange.
- **TCP/IP Model**
  - 4 layers:
    1. Network Access
    2. Internet
    3. Transport
    4. Application
  - Simple and more commonly used than OSI model

### Network Protocols

- **TCP (Transmission Control Protocol)**
  - Ensures reliable data transfer between devices.
  - Connection-oriented, meaning a connection is established before data is sent.
  - Uses sequence numbers to ensure data is received in the correct order.
- **UDP (User Datagram Protocol)**
  - Ensures efficient data transfer between devices.
  - Connectionless, meaning no connection is established before data is sent.
  - Does not guarantee delivery or order of data.
- **HTTP (Hypertext Transfer Protocol)**
  - Used for transferring data over the web.
  - Ensures data is delivered in a format that can be interpreted by web browsers.

### Important Formulas and Definitions

- **Packet Sniffing**: The process of intercepting and analyzing network traffic.
- **IP (Internet Protocol) Address**: A unique address assigned to each device on a network.
- **MAC (Media Access Control) Address**: A unique address assigned to each device on a network.
- **IP Address Subnetting**: The process of dividing an IP address into smaller subnets.

### Theorems

- **Store and Forward**: The process of storing received data at a node until it is forwarded to its next destination.
- **Cut-through**: The process of forwarding data as soon as it is received, without storing it in a buffer.

This summary should provide a concise overview of the key points for the topic "Textbook: Ch" in Computer Networks.
