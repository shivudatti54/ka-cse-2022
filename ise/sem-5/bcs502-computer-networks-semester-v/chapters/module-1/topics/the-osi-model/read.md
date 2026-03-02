# OSI Reference Model

## Overview

Open Systems Interconnection model - 7 layers defining network communication.

## The 7 Layers (Top to Bottom)

### Layer 7: Application

- User interface to network
- Protocols: HTTP, FTP, SMTP, DNS, SNMP
- Data unit: Data

### Layer 6: Presentation

- Data translation, encryption, compression
- Formats: JPEG, MPEG, ASCII, SSL/TLS
- Data unit: Data

### Layer 5: Session

- Session establishment, maintenance, termination
- Manages dialogs, synchronization
- Protocols: NetBIOS, RPC
- Data unit: Data

### Layer 4: Transport

- End-to-end delivery, reliability
- Protocols: TCP (reliable), UDP (unreliable)
- Data unit: **Segment**

### Layer 3: Network

- Logical addressing, routing
- Protocols: IP, ICMP, OSPF, BGP
- Devices: Router
- Data unit: **Packet**

### Layer 2: Data Link

- Physical addressing, framing, error detection
- Protocols: Ethernet, PPP, MAC
- Devices: Switch, Bridge
- Data unit: **Frame**

### Layer 1: Physical

- Physical transmission of bits
- Media: Cables, wireless
- Devices: Hub, Repeater
- Data unit: **Bits**

## Mnemonic

**Top-down: "All People Seem To Need Data Processing"**

- Application, Presentation, Session, Transport, Network, Data Link, Physical

**Bottom-up: "Please Do Not Throw Sausage Pizza Away"**

- Physical, Data Link, Network, Transport, Session, Presentation, Application

## Encapsulation

Data flows down, each layer adds header:

```
Application data
→ [Transport header + Data] = Segment
→ [Network header + Segment] = Packet
→ [Frame header + Packet + Frame trailer] = Frame
→ Bits on wire
```

## Layer Comparison

| Layer | PDU     | Address | Devices |
| ----- | ------- | ------- | ------- |
| 7-5   | Data    | -       | Gateway |
| 4     | Segment | Port    | -       |
| 3     | Packet  | IP      | Router  |
| 2     | Frame   | MAC     | Switch  |
| 1     | Bits    | -       | Hub     |
