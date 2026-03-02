# Point-to-Point Protocol (PPP)


## Table of Contents

- [Point-to-Point Protocol (PPP)](#point-to-point-protocol-ppp)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [PPP Frame Structure](#ppp-frame-structure)
  - [PPP Phases and Operation](#ppp-phases-and-operation)
  - [Link Control Protocol (LCP)](#link-control-protocol-lcp)
  - [Authentication Protocols](#authentication-protocols)
  - [Network Control Programs (NCP)](#network-control-programs-ncp)
  - [PPPoE (PPP over Ethernet)](#pppoe-ppp-over-ethernet)
  - [Multilink PPP](#multilink-ppp)
- [Examples](#examples)
  - [Example 1: PPP Frame Analysis](#example-1-ppp-frame-analysis)
  - [Example 2: CHAP Authentication Walkthrough](#example-2-chap-authentication-walkthrough)
  - [Example 3: IPCP Address Negotiation](#example-3-ipcp-address-negotiation)
- [Exam Tips](#exam-tips)

## Introduction

Point-to-Point Protocol (PPP) is a crucial data link layer protocol defined by RFC 1334 and later expanded in RFC 1331 and RFC 1332. It serves as a standard method for establishing a direct connection between two network nodes over serial cables, dial-up telephone lines, and other point-to-point links. PPP became the de facto standard for point-to-point serial communication because it addresses several limitations of the earlier HDLC (High-Level Data Link Control) protocol and provides enhanced features for network configuration and authentication.

The significance of PPP in modern networking cannot be overstated. It forms the foundation for various (broadband) access methods including PPP over Ethernet (PPPoE) and PPP over ATM (PPPoA), which are extensively used by Internet Service Providers (ISPs) for customer connections. Additionally, PPP serves as the underlying protocol for many virtual private network (VPN) implementations and is essential for understanding how remote access connections are established and managed in enterprise networks.

Unlike its predecessor protocols, PPP provides a comprehensive framework that encompasses link establishment, link testing, authentication, and network layer protocol configuration. This modular approach, achieved through a family of supporting protocols called Network Control Programs (NCPs), makes PPP extremely versatile and extensible. The protocol operates at the data link layer of the OSI model and is responsible for encapsulating network layer packets and transmitting them across the physical connection.

## Key Concepts

### PPP Frame Structure

The PPP frame format is designed to be versatile and compatible with various physical layer specifications. Each frame begins and ends with a flag byte (0x7E), which serves as a delimiter for synchronization. The frame structure includes several critical fields that enable reliable data transmission and protocol negotiation.

The **Address field** in PPP is always set to 0xFF (All Stations address), indicating that the frame is destined for all stations on the point-to-point link. Unlike HDLC where the address field could be used to identify specific stations, PPP uses this field consistently because there are only two endpoints on a point-to-point link, eliminating the need for addressing. The **Control field** is typically set to 0x03, representing Unnumbered Information (UI) frames, which means no sequence numbering is used in PPP's basic operation.

The **Protocol field** is a two-byte field that identifies the type of data contained in the Information field. This field is crucial for multiplexing different protocols over the same link. Protocol values in the range 0xCxxx indicate Network Layer protocols, where 0x0021 represents IPv4, 0x002D indicates IPv6, and 0x002B represents IPX. Values in the range 0x8xxx indicate Link Control Protocol (LCP) or Authentication protocols, with 0xC021 representing LCP, 0xC023 representing Password Authentication Protocol (PAP), and 0xC223 representing Challenge Handshake Authentication Protocol (CHAP).

### PPP Phases and Operation

PPP operates through a series of distinct phases that govern the lifecycle of a connection. Understanding these phases is essential for troubleshooting and implementing PPP-based solutions. The protocol progresses through five main phases: Link Dead, Link Establishment, Authentication, Network Layer Protocol Configuration, and Link Termination.

**Phase 1: Link Dead** represents the initial state where no physical connection exists or the physical layer is down. This phase occurs when the carrier detect signal is not present or when the physical layer is otherwise unavailable. When the physical connection is established, PPP automatically transitions to the Link Establishment phase.

**Phase 2: Link Establishment** involves the exchange of Link Control Protocol (LCP) packets to configure and test the data link. During this phase, the endpoints negotiate various link parameters including Maximum Receive Unit (MRU) size, compression options, and error detection settings. The LCP packet types used include Configure-Request, Configure-Ack, Configure-Nak, and Configure-Reject, which implement a reliable negotiation mechanism.

**Phase 3: Authentication** is an optional phase that occurs after successful link establishment. If either end requests authentication, the protocol enters this phase to verify the identity of the connecting entity. The two main authentication protocols supported by PPP are PAP (Password Authentication Protocol) and CHAP (Challenge Handshake Authentication Protocol). Authentication failure typically results in link termination.

**Phase 4: Network Layer Protocol Configuration** involves the exchange of Network Control Program (NCP) packets to configure one or more network layer protocols. For IPv4, this is accomplished through IPCP (Internet Protocol Control Protocol), which negotiates IP address assignment, DNS server addresses, and other IP-related parameters. This phase allows dynamic address allocation, which is crucial for dial-up Internet connections.

**Phase 5: Link Termination** occurs when either party decides to close the connection, when authentication fails, or when the physical layer connection is lost. LCP packets (Terminate-Request and Terminate-Ack) are exchanged to gracefully close the link.

### Link Control Protocol (LCP)

LCP is the foundation of PPP's link management capabilities. It provides essential functions for establishing, maintaining, and terminating point-to-point connections. LCP operates by exchanging various packet types, each serving a specific purpose in link management.

**Link Configuration** involves negotiating options that both ends must follow. Common configuration options include MRU (Maximum Receive Unit), which specifies the maximum packet size each end can receive; asynchronous control character map (ACCM), which defines which control characters should be escaped; and protocol field compression, which allows reducing the two-byte protocol field to one byte when appropriate.

**Link Testing** includes the Echo-Request and Echo-Reply packets used to test the link quality. These packets help verify that the link is operational and can be used to measure round-trip time and packet loss. The Link Quality Report (LQR) mechanism provides statistics about link reliability, though it is less commonly implemented than echo testing.

**Link Monitoring** is performed continuously during the connection lifetime to ensure the link remains operational. If excessive errors are detected or if keepalive packets are not received within the configured timeout, the link may be terminated.

### Authentication Protocols

**Password Authentication Protocol (PAP)** is the simpler of the two authentication methods but provides significantly less security. In PAP, the client sends a username and password in plaintext to the authenticator, who then verifies the credentials against a database. The vulnerabilities of PAP include the exposure of passwords in clear text during transmission and the vulnerability to replay attacks where an attacker captures and retransmits valid authentication sequences.

**Challenge Handshake Authentication Protocol (CHAP)** provides stronger security by using a challenge-response mechanism that never transmits passwords over the link. During CHAP authentication, the authenticator sends a random challenge to the peer, who must compute a response using a shared secret (password) and a one-way hash function (typically MD5). The authenticator then verifies the response without ever learning the actual password. CHAP provides protection against replay attacks because the challenge is randomly generated for each authentication attempt.

### Network Control Programs (NCP)

NCPs are a family of protocols responsible for negotiating network layer parameters. Each network layer protocol has a corresponding NCP. For IPv4, IPCP (Internet Protocol Control Protocol) handles address negotiation, while for IPv6, IPv6CP performs similar functions. For other protocols like IPX or AppleTalk, corresponding NCPs handle their specific configuration needs.

**IPCP Negotiation** is particularly important for dial-up Internet access. During IPCP negotiation, the ISP's access server typically assigns a dynamic IP address to the client through the IPCP Configure-Request/Configure-Ack exchange. Additional options that can be negotiated include primary and secondary DNS server addresses, primary and secondary WINS server addresses (for Microsoft networks), and IP compression options.

### PPPoE (PPP over Ethernet)

PPPoE combines PPP with Ethernet to provide authentication and address assignment capabilities over Ethernet networks. It is extensively used by DSL Internet service providers who require the accounting and authentication features of PPP but need to operate over Ethernet-based access networks. PPPoE encapsulates PPP frames inside Ethernet frames and adds a PPPoE Session ID to maintain the session. The protocol includes a Discovery phase for session establishment and a Session phase for data transfer, making it essential knowledge for understanding modern broadband access.

### Multilink PPP

Multilink PPP (MP or MLPPP) provides load balancing and redundancy by aggregating multiple physical links into a single logical link. This is particularly useful for bonding multiple dial-up connections or combining multiple physical WAN connections. MLPPP fragments packets and distributes the fragments across the component links, reassembling them at the receiving end. The protocol requires a Short Sequence Number Header for tracking fragments and uses a Multilink Maximum Received Reconstructed Unit (MRRU) option during negotiation.

## Examples

### Example 1: PPP Frame Analysis

Consider a PPP frame received on a serial interface with the following hex dump: 7E FF 03 C0 21 05 02 00 0A 7E. Let us analyze this frame step by step.

**Step 1: Identify the Flag bytes**
The frame begins and ends with 0x7E, which is the standard PPP flag byte indicating the start and end of a frame.

**Step 2: Analyze the Address and Control fields**
The bytes 0xFF and 0x03 follow the opening flag. 0xFF is the PPP broadcast address, and 0x03 indicates an Unnumbered Information (UI) frame with the P/F bit set to 0. These are the standard values for PPP frames.

**Step 3: Examine the Protocol field**
The bytes 0xC0 0x21 represent the Protocol field. Converting this to decimal gives 0xC021, which is the LCP (Link Control Protocol) protocol identifier. This indicates that the Information field contains an LCP packet.

**Step 4: Interpret the LCP packet**
The remaining bytes 0x05 0x02 0x00 0x0A constitute the LCP packet. The first byte (0x05) is the LCP packet type, indicating a Code-Reject packet. The second byte (0x02) is the Identifier field. Bytes 0x00 0x0A represent the Length field (10 bytes in decimal), indicating the total LCP packet length.

This frame represents a Code-Reject message from one PPP endpoint, indicating that it received an LCP packet with an unrecognized code.

### Example 2: CHAP Authentication Walkthrough

Suppose a client with username "client1" and password "secret123" initiates a CHAP authentication with an authenticator server. Let's trace the complete authentication exchange.

**Step 1: Server sends Challenge**
The server initiates CHAP by sending a Challenge packet to the client. The Challenge contains:

- Challenge Value: A random 16-byte value, for example: 0x4A 0x8B 0x3C 0x92 ... (random bytes)
- Name: Server's identifier, e.g., "AuthServer"

**Step 2: Client computes Response**
The client computes the CHAP response using the formula:
Response = MD5(Challenge ID + Password + Challenge Value)

For our example, if the Challenge ID is 0x05:
Input to MD5 = 0x05 + "secret123" + 0x4A 0x8B 0x3C 0x92 ...
This produces a 16-byte hash, for example: 0x2D 0x7A 0x91 0xE3 ... (the actual hash depends on the random challenge)

**Step 3: Client sends Response**
The client sends a Response packet containing:

- Response Value: The computed 16-byte hash
- Name: "client1"

**Step 4: Server verifies Response**
The server, having "secret123" stored locally, performs the same MD5 calculation. If the computed hash matches the received Response Value, authentication succeeds. The server then sends a Success packet. If not, it sends a Failure packet.

This example illustrates why CHAP is more secure than PAP: the password "secret123" is never transmitted over the network.

### Example 3: IPCP Address Negotiation

Consider a PPP client connecting to an ISP. During IPCP negotiation, the client sends a Configure-Request for IP address 0.0.0.0 (requesting address assignment), and the ISP responds. Let us trace the exchange:

**Step 1: Client sends Configure-Request**
The client sends IPCP Configure-Request with the following options:

- IP Address: 0.0.0.0 (indicating request for address assignment)
- Primary DNS: 0.0.0.0 (requesting DNS address)
- IP Compression Protocol: 0x0047 (Van Jacobson compression)

**Step 2: Server sends Configure-Nak**
The server does not accept 0.0.0.0 as a valid address and responds with Configure-Nak, offering:

- IP Address: 192.168.100.45 (the address being assigned)
- Primary DNS: 8.8.8.8 (Google's public DNS)
- IP Compression Protocol: 0x0047 (accepted)

**Step 3: Client sends Configure-Request**
The client accepts the offered values and sends a new Configure-Request:

- IP Address: 192.168.100.45
- Primary DNS: 8.8.8.8
- IP Compression Protocol: 0x0047

**Step 4: Server sends Configure-Ack**
The server acknowledges all options by sending Configure-Ack. IPCP negotiation is now complete, and the client has IP address 192.168.100.45 configured with DNS server 8.8.8.8.

This is the typical address negotiation process used by dial-up and some DSL Internet connections.

## Exam Tips

1. **Remember PPP Frame Format**: The standard PPP frame format is Flag (0x7E) - Address (0xFF) - Control (0x03) - Protocol - Information - FCS - Flag (0x7E). This is frequently asked in examinations.

2. **Difference between PAP and CHAP**: PAP transmits passwords in plaintext and is vulnerable to replay attacks, while CHAP uses challenge-response and never transmits passwords, making it more secure. Remember that CHAP uses MD5 hashing.

3. **PPP Phases Sequence**: The correct order is Link Dead → Link Establishment (LCP) → Authentication (optional) → Network Layer Protocol Configuration (NCP) → Link Termination. Do not skip any phase in the sequence.

4. **Protocol Field Values**: Remember key protocol field values: 0x0021 (IPv4), 0x002B (IPX), 0xC021 (LCP), 0xC023 (PAP), 0xC223 (CHAP). These are commonly asked in multiple-choice questions.

5. **LCP Functions**: LCP handles link establishment, link testing (Echo-Request/Echo-Reply), link monitoring, and link termination. It does not handle network layer protocol configuration—that is the job of NCPs.

6. **IPCP Purpose**: IPCP (Internet Protocol Control Protocol) is responsible for assigning dynamic IP addresses to PPP clients and negotiating DNS server addresses. It operates at the network layer but is considered part of PPP's control protocols.

7. **PPPoE Application**: PPPoE combines PPP with Ethernet and is primarily used by DSL service providers for authentication and session management over broadband connections. It uses a Discovery phase and a Session phase.

8. **Multilink PPP Purpose**: Multilink PPP aggregates multiple physical links into a single logical link for load balancing and increased bandwidth. It requires the MRRU (Multilink Maximum Received Reconstructed Unit) option to be negotiated.

9. **PPP vs HDLC**: Unlike HDLC, PPP requires an explicit Address field (always 0xFF) and uses a two-byte Protocol field. HDLC uses one-byte address and control fields by default.

10. **State Transitions**: Understand that transitions between phases are triggered by specific events—physical layer up triggers transition to Link Establishment, successful LCP triggers authentication (if requested), successful authentication triggers NCP phase, and Terminate-Request triggers link termination.
