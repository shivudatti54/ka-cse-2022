# Protocol Layering - Summary

## Key Definitions and Concepts

- **Protocol Layering:** A network architecture approach that organizes communication functions into distinct layers, each providing services to the layer above
- **OSI Model:** A seven-layer reference model (Physical, Data Link, Network, Transport, Session, Presentation, Application) developed by ISO
- **TCP/IP Model:** A four-layer model (Network Access, Internet, Transport, Application) that forms the foundation of the Internet
- **Encapsulation:** The process of adding layer-specific headers to data as it moves down through the layers
- **Decapsulation:** The reverse process of removing headers as data moves up through the layers
- **PDU (Protocol Data Unit):** The data unit at each layer with specific names: Data, Segment/Datagram, Packet, Frame, Bits

## Important Formulas and Theorems

- **Port Numbers Range:** 0-65535 (Well-known: 0-1023, Registered: 1024-49151, Dynamic: 49152-65535)
- **MAC Address:** 48-bit address expressed as 12 hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E)
- **IPv4 Address:** 32-bit address, typically represented in dotted-decimal notation (e.g., 192.168.1.1)

## Key Points

1. The OSI model has 7 layers; TCP/IP has 4 layers corresponding to OSI layers
2. Physical Layer transmits raw bits; Data Link Layer provides reliable node-to-node transfer
3. Network Layer handles routing and logical addressing (IP); Transport Layer handles port addressing and end-to-end communication
4. TCP provides reliable, connection-oriented service; UDP provides unreliable, connectionless service
5. Routers operate at Layer 3 (Network), Switches at Layer 2 (Data Link), Hubs at Layer 1 (Physical)
6. Each layer communicates only with adjacent layers through well-defined interfaces
7. Encapsulation adds headers at sender; decapsulation removes headers at receiver
8. Application Layer protocols: HTTP, FTP, SMTP, DNS, Telnet
9. Transport Layer protocols: TCP (port 80 for HTTP, 21 for FTP) and UDP (DNS uses both)
10. The OSI model is a reference model; TCP/IP is the implementation used in practice

## Common Mistakes to Avoid

1. **Confusing PDU names:** Remember segments (Transport), packets (Network), frames (Data Link), and bits (Physical)
2. **Mixing up TCP/IP and OSI layer counts:** TCP/IP has 4 layers, OSI has 7 layers
3. **Thinking routers work at all layers:** Routers primarily work at Layer 3 (Network Layer)
4. **Confusing logical and physical addressing:** IP addresses are logical (configurable); MAC addresses are physical (burned into NIC)
5. **Assuming all protocols use TCP:** Many applications use UDP (e.g., DNS, video streaming, online gaming)

## Revision Tips

1. Use mnemonics to remember OSI layers: "All People Seem To Need Data Processing"
2. Draw the layer diagram and write key protocols next to each layer
3. Practice tracing a web request through all layers to understand encapsulation
4. Create a comparison table between OSI and TCP/IP models
5. Focus on understanding which layer each common protocol belongs to—this frequently appears in exams
