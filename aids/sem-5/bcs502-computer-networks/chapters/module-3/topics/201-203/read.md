# \*\*20.1 Network Layer Services

The network layer is the fourth layer of the OSI model and is responsible for providing various services to ensure reliable and efficient communication between devices on different networks.

### Key Functions of Network Layer Services

- **Routing**: The network layer is responsible for routing packets between different networks. It uses routing tables to forward packets to their final destination.
- **Fragmentation**: When a packet is larger than the maximum size of a network segment, the network layer breaks it into smaller fragments and reassembles them at the receiving end.
- **Error Detection and Correction**: The network layer uses error detection and correction mechanisms such as checksums and CRCs to ensure that packets are delivered error-free.
- **Multiplexing and Demultiplexing**: The network layer multiplexes multiple data streams onto a single communication channel and demultiplexes them at the receiving end.

### Network Layer Protocols

- **IP** (Internet Protocol): IP is the primary protocol used for routing packets between different networks. It assigns a unique IP address to each device on a network.
- **ICMP** (Internet Control Message Protocol): ICMP is used for error-reporting and diagnostic functions at the network layer.
- **IGMP** (Internet Group Management Protocol): IGMP is used for multicasting, which allows multiple devices to receive a single packet.

# \*\*20.2 Packet Switching

Packet switching is a technique used by the network layer to transmit data in small packets between devices on different networks.

### Key Features of Packet Switching

- **Packetization**: Data is broken into small packets, each with a header that contains control information.
- **Switching**: Packets are routed between devices based on their destination addresses.
- **Store-and-Forward**: Packets are stored in a buffer until they are processed by the next device in the path.

### Advantages of Packet Switching

- **Efficient Use of Resources**: Packet switching allows for efficient use of network resources, as each packet is transmitted independently.
- **Flexibility**: Packet switching enables devices to communicate with each other using different protocols.

# \*\*20.3 IPv4 Address and IPv4 Datagram

### IPv4 Address

- **Definition**: IPv4 addresses are 32-bit addresses used to identify devices on a network.
- **Format**: IPv4 addresses are formatted as a dotted decimal number (e.g., 192.168.1.1).
- **Address Classes**: IPv4 addresses are divided into five address classes (A, B, C, D, and E).

### IPv4 Datagram

- **Definition**: IPv4 datagrams are packets of data transmitted between devices on a network using IPv4.
- **Format**: IPv4 datagrams consist of a header and a payload.
- **Header Components**: The IPv4 header includes source and destination addresses, sequence numbers, and a checksum.

### IPv4 Datagram Structure

| Field                  | Format  | Description                                        |
| ---------------------- | ------- | -------------------------------------------------- |
| Version                | 4 bits  | Version of the IP protocol                         |
| Header Length          | 4 bits  | Length of the IP header in 32-bit words            |
| DSCP/ECN               | 6 bits  | Differentiated services code point/ecn             |
| Total Length           | 16 bits | Total length of the datagram in octets             |
| Identification         | 16 bits | Identification number of the datagram              |
| Flags                  | 3 bits  | Flag bits (DF, MF, MF=1)                           |
| Fragment Offset        | 13 bits | Fragment offset from the beginning of the datagram |
| TTL                    | 8 bits  | Time to live of the datagram                       |
| Protocol               | 8 bits  | Protocol used to forward the datagram              |
| Checksum               | 16 bits | Checksum of the datagram header and payload        |
| Source IP Address      | 32 bits | Source IP address of the datagram                  |
| Destination IP Address | 32 bits | Destination IP address of the datagram             |
