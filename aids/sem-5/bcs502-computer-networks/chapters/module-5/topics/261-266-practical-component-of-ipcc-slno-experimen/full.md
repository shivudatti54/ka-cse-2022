# **26.1-26.6 PRACTICAL COMPONENT OF IPCC Sl.NO Experiments 1 Implement three nodes point – to – point network with duplex links between them**

## **Introduction**

In this practical component, we will implement a three-node point-to-point network with duplex links between them. This experiment will help us understand the concept of point-to-point networks, duplex links, and how they can be used to establish a reliable and efficient communication network.

## **Historical Context**

The concept of point-to-point networks has been around for decades. In the early days of computer networking, point-to-point networks were used to connect two devices directly. With the advent of packet switching, point-to-point networks evolved to use packet-switching protocols such as TCP/IP.

## **Modern Developments**

In modern times, point-to-point networks are still widely used, particularly in applications where reliability and security are paramount. With the advent of wireless technology, point-to-point networks can now be established using wireless links, such as Wi-Fi or cellular networks.

## **Practical Component**

### Experiment Objective

The objective of this experiment is to design and implement a three-node point-to-point network with duplex links between them.

### Requirements

- Three nodes (computers or switches)
- Three duplex links (cables or wireless connections)
- Network devices (routers or hubs)
- Network software (operating system, network protocol)

### Experiment Design

For this experiment, we will use three nodes: Node A, Node B, and Node C. Each node will have a duplex link connecting it to the other two nodes.

## **Diagram Description**

The following diagram shows the three-node point-to-point network with duplex links between them:

```
          +---------------+
          |  Node A    |
          |  (Router)  |
          +---------------+
                  |
                  |
                  v
          +---------------+
          |  Node B    |
          |  (Switch)  |
          +---------------+
                  |
                  |
                  v
          +---------------+
          |  Node C    |
          |  (Router)  |
          +---------------+
```

## **Implementation**

To implement the three-node point-to-point network, we will follow these steps:

1. Connect Node A to Node B using a duplex cable.
2. Connect Node B to Node C using a duplex cable.
3. Configure the network devices (routers and switches) to establish a connection between the nodes.
4. Test the network to ensure that data can be transmitted between the nodes.

## **Duplex Links**

A duplex link is a two-way communication link that allows data to be transmitted in both directions. In a point-to-point network, duplex links are used to establish a connection between two nodes.

## **Types of Duplex Links**

There are two types of duplex links:

- Wired duplex links: These are used to connect nodes using cables or fibers.
- Wireless duplex links: These are used to connect nodes using wireless technology, such as Wi-Fi or cellular networks.

## **Advantages of Duplex Links**

Duplex links offer several advantages, including:

- Reliable communication: Duplex links ensure that data can be transmitted in both directions, reducing the risk of communication errors.
- High-speed transmission: Duplex links can transmit data at high speeds, making them suitable for applications that require fast data transfer.

## **Disadvantages of Duplex Links**

While duplex links offer several advantages, they also have some disadvantages, including:

- Increased cost: Duplex links can be more expensive than single-link connections.
- Complexity: Duplex links can be more complex to set up and maintain than single-link connections.

## **Case Study**

A financial institution uses a three-node point-to-point network with duplex links to connect its servers, switches, and routers. The network is used to transmit financial data securely and efficiently.

## **Applications**

Three-node point-to-point networks with duplex links have several applications, including:

- Financial institutions: Point-to-point networks are used to connect servers, switches, and routers to transmit financial data securely and efficiently.
- Healthcare: Point-to-point networks are used to connect medical devices, such as MRI machines and patient monitoring systems.
- Manufacturing: Point-to-point networks are used to connect machines and devices to transmit production data securely and efficiently.

## **Example Code**

Here is an example code in C++ that demonstrates how to establish a duplex connection between two nodes:

```cpp
#include <iostream>
#include <string>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {
  // Create a socket
  int sock = socket(AF_INET, SOCK_STREAM, 0);
  if (sock < 0) {
    std::cerr << "Error creating socket" << std::endl;
    return 1;
  }

  // Set up the address and port number
  struct sockaddr_in addr;
  addr.sin_family = AF_INET;
  addr.sin_port = htons(8080);
  inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);

  // Connect to the other node
  if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
    std::cerr << "Error connecting to other node" << std::endl;
    return 1;
  }

  // Send data to the other node
  char data[] = "Hello, world!";
  send(sock, data, strlen(data), 0);

  // Receive data from the other node
  char buffer[256];
  recv(sock, buffer, 256, 0);
  std::cout << "Received data: " << buffer << std::endl;

  // Close the socket
  close(sock);
  return 0;
}
```

## **Further Reading**

- "Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall
- "Networking Fundamentals" by Keith P. Bartolomeo
- "Computer Networks: A Systems Approach" by Larry L. Peterson and Bruce S. Davie

I hope this detailed content helps you understand the practical component of IPCC Sl.NO Experiments 1 Implement three nodes point – to – point network with duplex links between them.
