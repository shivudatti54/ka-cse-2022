# **20.1-20.3: Network Layer Services, Packet Switching, IPv4 Address, IPv4 Datagram, IPv6**

## **20.1: Network Layer Services**

The network layer is the fifth layer of the OSI model and is responsible for routing data between different networks. It provides services such as connectivity, traffic control, and error detection.

### Connectionless vs Connection-Oriented Services

The network layer provides two types of services:

- **Connectionless services**: These services do not establish a connection between the sender and receiver before data is sent. Anagrams such as UDP (User Datagram Protocol) and ICMP (Internet Control Message Protocol) are examples of connectionless services.
- **Connection-oriented services**: These services establish a connection between the sender and receiver before data is sent. TCP (Transmission Control Protocol) is an example of a connection-oriented service.

### Services Provided by the Network Layer

The network layer provides several services, including:

- **Routing**: The network layer is responsible for routing data between different networks.
- **Network Address Translation (NAT)**: NAT is used to translate IP addresses in a network.
- **Fragmentation and Reassembly**: The network layer breaks down large packets into smaller packets and reassembles them at the receiving end.
- **Error Detection and Correction**: The network layer detects and corrects errors in data transmitted over the network.

## **20.2: Packet Switching**

Packet switching is a technique used by the network layer to transmit data over a network. It involves breaking down data into small packets and transmitting each packet over the network independently.

### How Packet Switching Works

Here's a step-by-step explanation of how packet switching works:

1.  **Packet Creation**: The data is broken down into small packets, and each packet is assigned a header that contains the destination IP address.
2.  **Packet Transmission**: Each packet is transmitted over the network independently.
3.  **Packet Reception**: Each packet is received by a router or switch, which checks the destination IP address.
4.  **Packet Forwarding**: The packet is forwarded to the next hop on the path to the destination.
5.  **Packet Reassembly**: The packets are reassembled at the receiving end into the original data.

### Advantages and Disadvantages of Packet Switching

Advantages:

- **Scalability**: Packet switching allows networks to be scaled up or down as needed.
- **Flexibility**: Packet switching allows for different types of networks to be connected.

Disadvantages:

- **Error Prone**: Packet switching is error-prone, and packets can be lost or corrupted during transmission.
- **Complexity**: Packet switching is complex and requires sophisticated network infrastructure.

## **20.3: IPv4 Address**

An IP address is a unique identifier assigned to each device on a network. IPv4 (Internet Protocol version 4) is the most widely used IP protocol.

### How IPv4 Addresses Work

IPv4 addresses are divided into two parts:

- **Network ID**: This part of the IP address identifies the network to which the device belongs.
- **Host ID**: This part of the IP address identifies the specific device on the network.

IPv4 addresses are represented in dotted decimal notation, with four numbers separated by dots.

### IPv4 Address Classes

IPv4 addresses are classified into five classes:

- **Class A**: Class A addresses are assigned to large networks (up to 16 million hosts).
- **Class B**: Class B addresses are assigned to medium-sized networks (up to 65,536 hosts).
- **Class C**: Class C addresses are assigned to small networks (up to 256 hosts).
- **Class D**: Class D addresses are used for multicast communications.
- **Class E**: Class E addresses are used for experimental communications.

### IPv4 Addressing Example

Here's an example of an IPv4 address:

```
192.168.1.100
```

In this example:

- **192.168.1.** is the network ID.
- **100** is the host ID.

## **Modern Developments: IPv6**

IPv6 (Internet Protocol version 6) is the next-generation IP protocol, designed to replace IPv4.

### IPv6 Addressing

IPv6 addresses are longer and more complex than IPv4 addresses, with a maximum of 128 characters.

IPv6 addresses are represented in hexadecimal notation, with eight groups of four hexadecimal digits separated by colons.

### IPv6 Addressing Example

Here's an example of an IPv6 address:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

In this example:

- **2001:0db8:85a3** is the network ID.
- **0000:0000:8a2e** is the host ID.
- **0370:7334** is the interface ID.

## **Further Reading**

- [RFC 791: Internet Protocol] (https://tools.ietf.org/html/rfc791)
- [RFC 791: Internet Protocol (IP)] (https://www.ietf.org/assignments/iana-registry/texts/ RFC-791.txt)
- [IPv4 Addressing](https://en.wikipedia.org/wiki/IPv4_address)
- [IPv6 Addressing](https://en.wikipedia.org/wiki/IPv6_address)

Note: The above links are subject to change, and the content may not be up-to-date.
