# **Study Material: Implementing Sliding Window Protocol in Data Link Layer**

## **Introduction**

The Sliding Window protocol is a popular technique used in the data link layer to manage data transfer over a shared medium with a limited bandwidth. In this study material, we will explore the concept of Sliding Window protocol, its advantages and disadvantages, and implement a program to demonstrate its functionality.

## **What is Sliding Window Protocol?**

The Sliding Window protocol is a control protocol used in data link layer to manage data transfer between two devices, typically a sender and a receiver, over a shared medium. The protocol uses a sliding window approach to divide the data into smaller chunks, called segments, and transmit them one by one.

## **Key Concepts**

- **Window size**: The maximum number of segments that can be transmitted by the sender in a single transmission.
- **Sliding window**: The range of segments that are currently being transmitted by the sender.
- **Acknowledgment**: A message sent by the receiver to acknowledge the receipt of a segment.
- **Retransmission**: The retransmission of a segment that was not received by the receiver.

## **How Sliding Window Protocol Works**

The Sliding Window protocol works as follows:

1.  The sender and receiver agree on a window size.
2.  The sender divides the data into segments and transmits them one by one.
3.  The receiver acknowledges the receipt of each segment.
4.  If a segment is lost or corrupted, the sender retransmits it.
5.  The receiver acknowledges the receipt of the retransmitted segment.

## **Advantages and Disadvantages**

Advantages:

- **Efficient use of bandwidth**: The Sliding Window protocol allows for efficient use of bandwidth by dividing the data into smaller chunks.
- **Reduced retransmissions**: The protocol reduces retransmissions by allowing the sender to retransmit lost or corrupted segments.

Disadvantages:

- **Increased complexity**: The Sliding Window protocol adds complexity to the data transfer process.
- **Dependence on acknowledgment**: The protocol depends on acknowledgment from the receiver, which can lead to delays.

## **Implementing Sliding Window Protocol**

Below is a simple Python program to demonstrate the Sliding Window protocol:

```python
import time

class SlidingWindowProtocol:
    def __init__(self, window_size):
        self.window_size = window_size
        self.window = []
        self.send_index = 0
        self.receive_index = 0

    def send_segment(self, data):
        if self.send_index < len(self.window):
            self.window[self.send_index] = data
            print(f"Segment sent: {data}")
            self.send_index += 1
        else:
            print("Window is full. Waiting for acknowledgment.")

    def receive_segment(self, segment):
        if segment == self.window[self.receive_index]:
            print(f"Segment received: {segment}")
            self.receive_index += 1
        else:
            print("Segment not received correctly.")

    def retransmit_segment(self, segment):
        self.send_segment(segment)

def main():
    window_size = 3
    protocol = SlidingWindowProtocol(window_size)

    # Data to be sent
    data = "Hello World!"

    # Divide data into segments
    segments = [data[i:i + window_size] for i in range(0, len(data), window_size)]

    # Simulate data transmission
    for i, segment in enumerate(segments):
        # Simulate sender's delay
        time.sleep(1)
        protocol.send_segment(segment)

        # Simulate receiver's delay
        time.sleep(1)
        protocol.receive_segment(segment)

        # Simulate packet loss
        if i == 2:
            # Simulate packet loss
            print("Packet lost. Retransmitting...")
            protocol.retransmit_segment(segment)

if __name__ == "__main__":
    main()
```

## **Explanation**

The program demonstrates the Sliding Window protocol by simulating a data transmission between a sender and a receiver. The sender divides the data into segments and transmits them one by one using a sliding window approach. The receiver acknowledges the receipt of each segment, and the sender retransmits segments that were not received correctly.

## **Key Takeaways**

- The Sliding Window protocol is a control protocol used in data link layer to manage data transfer between two devices.
- The protocol uses a sliding window approach to divide the data into smaller chunks and transmit them one by one.
- The protocol requires acknowledgment from the receiver to ensure reliable data transfer.

## **Conclusion**

In conclusion, the Sliding Window protocol is an efficient technique used in data link layer to manage data transfer over a shared medium. The program demonstrates the implementation of the protocol and highlights its advantages and disadvantages.
