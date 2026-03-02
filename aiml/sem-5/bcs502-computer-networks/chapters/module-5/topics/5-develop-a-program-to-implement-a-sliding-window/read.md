# **5. Develop a Program to Implement a Sliding Window Protocol in the Data Link Layer**

## **Table of Contents**

1. [Introduction](#introduction)
2. [What is Sliding Window Protocol?](#what-is-sliding-window-protocol)
3. [How Sliding Window Protocol Works](#how-sliding-window-protocol-works)
4. [Example Program Implementation](#example-program-implementation)
5. [Key Concepts](#key-concepts)

## **1. Introduction**

The Sliding Window Protocol is a type of flow control mechanism used in data link layer protocols to manage the transmission of data packets between two devices. It is a simple and effective method for preventing network congestion and ensuring reliable data transfer.

## **2. What is Sliding Window Protocol?**

The Sliding Window Protocol is a flow control mechanism that divides the available bandwidth into fixed-size windows and allows devices to send data packets within these windows. The window size is typically fixed, and devices can move the window forward or backward as needed to accommodate changing network conditions.

## **3. How Sliding Window Protocol Works**

Here's a step-by-step explanation of how the Sliding Window Protocol works:

- **Window Establishment**: The sender and receiver agree on a window size and establish the sliding window protocol.
- **Packet Transmission**: The sender sends data packets within the established window size.
- **Window Movement**: If the sender receives an acknowledgement (ACK) for a packet, it moves the window forward and sends the next packet.
- **WindowSize Reduction**: If the sender receives a negative acknowledgement (NACK) or a timeout, it reduces the window size and sends a revised window size to the receiver.
- **Window Movement and Packet Transmission**: The sender continues to send packets within the updated window size.

## **4. Example Program Implementation**

Below is a simple Python program that implements a Sliding Window Protocol:

```python
import socket
import time

# Constants
WINDOW_SIZE = 3
PACKET_SIZE = 1024
BUFFER_SIZE = 1024

class SlidingWindowProtocol:
    def __init__(self, window_size, packet_size):
        self.window_size = window_size
        self.packet_size = packet_size
        self.buffer_size = BUFFER_SIZE
        self.window = bytearray(WINDOW_SIZE * packet_size)

    def send_packet(self, packet):
        # Fill the window with packets
        index = 0
        while index < self.window_size * self.packet_size:
            self.window[index:index + self.packet_size] = packet
            index += self.packet_size
        # Send the window
        return socket.send(self.window)

    def receive_ack(self, ack):
        # Check if the ack is for a packet in the window
        for i, packet in enumerate(self.window):
            if packet == ack:
                # Move the window forward
                return i
        # Return -1 if the ack is not in the window
        return -1

    def receive_nack(self, nack):
        # Reduce the window size
        self.window_size -= 1
        # Send a revised window size to the receiver
        return self.send_packet(self.window_size)

def main():
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the receiver
    sock.connect(("receiver", 12345))

    # Initialize the sliding window protocol
    protocol = SlidingWindowProtocol(WINDOW_SIZE, PACKET_SIZE)

    # Send packets
    for i in range(10):
        packet = bytearray(i * PACKET_SIZE)
        protocol.send_packet(packet)
        time.sleep(1)
        # Receive ack or nack
        ack = sock.recv(1)
        if ack == b'1':
            # Move the window forward
            index = protocol.receive_ack(ack)
            # Send the next packet
            packet = bytearray((i + 1) * PACKET_SIZE)
            protocol.send_packet(packet)
        elif ack == b'0':
            # Move the window backward
            index = protocol.receive_nack(ack)
            # Send the previous packet
            packet = bytearray((i - 1) * PACKET_SIZE if index > 0 else len(packet) * PACKET_SIZE)
            protocol.send_packet(packet)

if __name__ == "__main__":
    main()
```

## **5. Key Concepts**

- **Window Size**: The fixed-size window in which data packets are sent.
- **Packet Size**: The size of each data packet.
- **Buffer Size**: The size of the buffer used to store packets.
- **Acknowledge (ACK)**: A packet sent by the receiver to indicate that a packet is received successfully.
- **Negative Acknowledge (NACK)**: A packet sent by the sender to indicate that a packet is not received successfully.
- **Flow Control**: The process of managing the transmission of data packets to prevent network congestion.
