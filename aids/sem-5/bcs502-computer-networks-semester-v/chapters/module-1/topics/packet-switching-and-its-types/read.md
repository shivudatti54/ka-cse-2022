# Packet Switching and Types

## Introduction

Packet switching is a method of transmitting data over a network by breaking it down into small packets and routing each packet independently. This technique is used in many modern communication networks, including the Internet.

## Key Concepts

### Packet Switching

Packet switching is a connectionless communication method, meaning that there is no dedicated connection established between the sender and receiver before data is transmitted. Instead, each packet is routed through the network based on its destination address.

### Packet Structure

A packet typically consists of two parts:

- **Header**: contains control information, such as source and destination addresses, packet length, and sequence number.
- **Payload**: contains the actual data being transmitted.

## Types of Packet Switching

There are two main types of packet switching:

### 1. Connection-Oriented Packet Switching

In connection-oriented packet switching, a virtual circuit is established between the sender and receiver before data is transmitted. This virtual circuit is used to route all packets between the two endpoints.

Example:

```
+---------------+
|  Sender   |
+---------------+
       |
       |  Establish Virtual Circuit
       v
+---------------+
|  Router 1  |
+---------------+
       |
       |  Route Packets
       v
+---------------+
|  Router 2  |
+---------------+
       |
       |  Route Packets
       v
+---------------+
|  Receiver  |
+---------------+
```

### 2. Connectionless Packet Switching

In connectionless packet switching, each packet is routed independently based on its destination address. There is no virtual circuit established between the sender and receiver.

Example:

```
+---------------+
|  Sender   |
+---------------+
       |
       |  Send Packet 1
       v
+---------------+
|  Router 1  |
+---------------+
       |
       |  Route Packet 1
       v
+---------------+
|  Router 2  |
+---------------+
       |
       |  Route Packet 1
       v
+---------------+
|  Receiver  |
+---------------+
       |
       |  Send Packet 2
       v
+---------------+
|  Router 3  |
+---------------+
       |
       |  Route Packet 2
       v
+---------------+
|  Receiver  |
+---------------+
```

## Comparison of Connection-Oriented and Connectionless Packet Switching

|                     | Connection-Oriented                                                             | Connectionless                                                         |
| ------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Virtual Circuit** | Established before data transmission                                            | Not established                                                        |
| **Packet Routing**  | Packets routed through virtual circuit                                          | Packets routed independently                                           |
| **Reliability**     | More reliable, as packets are routed through established circuit                | Less reliable, as packets may be lost or corrupted during transmission |
| **Efficiency**      | Less efficient, as virtual circuit must be established before data transmission | More efficient, as packets can be transmitted immediately              |

## Exam Tips

- Understand the key concepts of packet switching, including packet structure and types of packet switching.
- Be able to explain the differences between connection-oriented and connectionless packet switching.
- Practice drawing diagrams to illustrate packet switching concepts.
