# **Computer Networks**

### Topic: Packets Dropped

#### Introduction

In computer networks, packets are the basic units of data that are transmitted between devices. When these packets travel through a network, they can be affected by various factors that can cause them to be lost or dropped. In this topic, we will discuss what packets dropped mean, the causes of packet loss, and the impact on network performance.

#### What are Packets Dropped?

Packets dropped refer to the packets that are lost or discarded during transmission due to various reasons. These packets are never received by the destination device and are considered as lost packets.

#### Causes of Packet Loss

Packet loss can occur due to various reasons, including:

- **Physical Layer Issues**
  - Radio frequency interference (RFI)
  - Electromagnetic interference (EMI)
  - Cable damage or cuts
  - Network congestion
- **Data Link Layer Issues**
  - Collisions
  - Errors in MAC addresses
  - Frame errors
- **Network Layer Issues**
  - Routing errors
  - Packet fragmentation
  - IP address conflicts
- **Transport Layer Issues**
  - Congestion
  - Connection termination
  - Errors in TCP or UDP headers

#### Types of Packet Loss

There are two types of packet loss:

- **Duplicate Packets**: Packets that are received multiple times, but are not necessary for the data to be reconstructed.
- **Lost Packets**: Packets that are not received by the destination device.

#### Impact on Network Performance

Packet loss can have a significant impact on network performance, including:

- **Decreased Throughput**: Packet loss can reduce the amount of data that is transmitted, resulting in decreased throughput.
- **Increased Latency**: Packet loss can cause a delay in the transmission of data, resulting in increased latency.
- **Reduced Quality of Service**: Packet loss can lead to reduced quality of service, including decreased reliability and increased jitter.

#### Example

Suppose we have a network with two nodes, A and B, that are connected through a wireless link. Node A sends a packet of data to node B, but due to radio frequency interference, the packet is dropped. Node B does not receive the packet and sends an acknowledgement (ACK) back to node A. Node A assumes that the packet was delivered successfully and continues to send more packets. However, due to the packet loss, some of the subsequent packets may also be lost, leading to a decrease in throughput and increased latency.

#### Key Concepts

- **Packet loss**: The loss of packets during transmission.
- **Causes of packet loss**: Physical layer issues, data link layer issues, network layer issues, and transport layer issues.
- **Types of packet loss**: Duplicate packets and lost packets.
- **Impact on network performance**: Decreased throughput, increased latency, and reduced quality of service.

#### Review Questions

1. What is packet loss?
2. What are the causes of packet loss?
3. What are the types of packet loss?
4. How does packet loss affect network performance?
5. Can you give an example of packet loss in a network?

#### Practice Exercises

1. Explain how packet loss can occur due to physical layer issues.
2. Describe the impact of packet loss on network performance.
3. Design a network that minimizes packet loss due to physical layer issues.

Note: This is a comprehensive study material for the topic "And find the number of packets dropped" in computer networks. It covers the definition, causes, types, and impact of packet loss, as well as key concepts and review questions. The practice exercises are designed to test the understanding of the topic.
