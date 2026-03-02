# **21.3.2 Network Layer Services**

### Introduction

The Network Layer is the third layer of the OSI model and is responsible for routing data between networks. It provides several services that enable data to be transmitted efficiently and reliably over a network.

### Network Layer Services

The Network Layer provides the following services:

- **Routing**: The Network Layer is responsible for routing data between networks. It uses routing tables to determine the best path for data to take between networks.
- **Fragmentation**: When a packet is larger than the maximum size allowed by a network, the Network Layer breaks it up into smaller packets called fragments. These fragments are then transmitted over the network and reassembled at the receiving end.
- **Reassembly**: The Network Layer is responsible for reassembling packets that have been fragmented during transmission.
- **Error Detection and Correction**: The Network Layer provides error detection and correction mechanisms to ensure that data is delivered correctly.

### Packet Switching

---

Packet switching is a method of transmitting data over a network where data is broken up into small packets and transmitted independently. Each packet contains the source and destination addresses, as well as error-checking and sequencing information.

### How Packet Switching Works

Here's an example of how packet switching works:

1. A user sends data to a website using a packet-switching network.
2. The data is broken up into small packets and transmitted independently over the network.
3. Each packet contains the source and destination addresses, as well as error-checking and sequencing information.
4. The packets are routed through the network using routing tables.
5. The packets are reassembled at the receiving end in the correct order.

### IPv4 Address

---

An IPv4 address is a 32-bit address that identifies a device on a network. It is used to route data between networks and is the most commonly used address type.

### IPv4 Address Format

The IPv4 address format is as follows:

`xxx.xxx.xxx.xxx`

where `xxx` represents a group of four numbers separated by dots.

### IPv4 Datagram

---

An IPv4 datagram is a single packet of data that is transmitted over a network using the Internet Protocol (IP). It is the basic unit of data transmission over the Internet.

### IPv4 Datagram Format

The IPv4 datagram format is as follows:

| Field           | Length  | Description                             |
| --------------- | ------- | --------------------------------------- |
| Version         | 4 bits  | Version of the IP protocol              |
| Header Length   | 4 bits  | Length of the IP header                 |
| DSCP            | 6 bits  | Differentiated Services Code Point      |
| ECN             | 2 bits  | Explicit Congestion Notification        |
| Total Length    | 16 bits | Total length of the datagram            |
| ID              | 16 bits | Identification number                   |
| Flags           | 3 bits  | Flags that indicate the type of service |
| Fragment Offset | 13 bits | Offset of the first fragment            |
| TTL             | 8 bits  | Time to live                            |
| Protocol        | 8 bits  | Protocol type                           |
| Source IP       | 32 bits | Source IP address                       |
| Destination IP  | 32 bits | Destination IP address                  |

### IPv6 Address

---

An IPv6 address is a 128-bit address that identifies a device on a network. It is used to route data between networks and is the recommended address type for new networks.

### IPv6 Address Format

The IPv6 address format is as follows:

`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

where `x` represents a hexadecimal digit.

### IPv6 Datagram

---

An IPv6 datagram is a single packet of data that is transmitted over a network using the Internet Protocol version 6 (IPv6). It is the basic unit of data transmission over the Internet.

### IPv6 Datagram Format

The IPv6 datagram format is as follows:

| Field          | Length   | Description                |
| -------------- | -------- | -------------------------- |
| Version        | 8 bits   | Version of the IP protocol |
| Header Length  | 4 bits   | Length of the IP header    |
| Traffic Class  | 8 bits   | Traffic class              |
| Flow Label     | 20 bits  | Flow label                 |
| Payload Length | 16 bits  | Length of the payload      |
| Next Header    | 8 bits   | Next header type           |
| Hop Limit      | 8 bits   | Hop limit                  |
| Source IP      | 128 bits | Source IP address          |
| Destination IP | 128 bits | Destination IP address     |

### Comparison of IPv4 and IPv6

---

| Feature        | IPv4              | IPv6                                       |
| -------------- | ----------------- | ------------------------------------------ |
| Address Length | 32 bits           | 128 bits                                   |
| Address Format | `xxx.xxx.xxx.xxx` | `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` |
| Address Space  | Limited           | Much larger                                |
| Header Length  | 20 bits           | 40 bits                                    |
| Security       | Less secure       | More secure                                |
| Mobility       | Less mobile       | More mobile                                |

### Conclusion

---

In conclusion, the Network Layer provides several services that enable data to be transmitted efficiently and reliably over a network. Packet switching is a method of transmitting data over a network where data is broken up into small packets and transmitted independently. IPv4 addresses are 32-bit addresses that identify a device on a network, while IPv6 addresses are 128-bit addresses that identify a device on a network. IPv4 datagrams are single packets of data that are transmitted over a network using the Internet Protocol (IP), while IPv6 datagrams are single packets of data that are transmitted over a network using the Internet Protocol version 6 (IPv6).
