# Packet Switching and Its Types - Summary

## Key Definitions and Concepts

- **Packet Switching**: A communication method where data is broken into small chunks (packets) that are transmitted independently through a network without establishing a dedicated path.

- **Datagram Packet Switching**: A connectionless switching technique where each packet is routed independently with complete destination address information; no prior connection setup is required.

- **Virtual Circuit Packet Switching**: A connection-oriented switching technique where a logical path (virtual circuit) is established before data transfer; all packets follow the same path using a virtual circuit identifier (VCI).

- **VCI (Virtual Circuit Identifier)**: A short identifier used in virtual circuit switching instead of full destination addresses to identify the connection.

## Important Formulas and Theorems

- Packet consists of: Header + Payload (Data) + Trailer (optional)
- Header contains: Source/Destination address, Sequence number, Protocol info, Packet length
- In virtual circuit: Address overhead is reduced (VCI vs full address)
- No specific formulas required for this topic, but understanding the comparison characteristics is essential

## Key Points

- Packet switching enables statistical multiplexing, allowing efficient bandwidth utilization compared to circuit switching.

- Datagram switching (connectionless) is used in IP networks and the Internet; packets may take different paths and arrive out of order.

- Virtual circuit switching (connection-oriented) is used in X.25, Frame Relay, and ATM; requires connection setup but guarantees ordered delivery.

- Virtual circuit switching provides better QoS support due to resource reservation during connection establishment.

- Datagram switching is more resilient to network failures as packets can be dynamically rerouted.

- Virtual circuit switching has higher overhead for connection setup but lower per-packet overhead due to VCI usage.

- The Internet combines both approaches: IP (datagram) at network layer and TCP (virtual circuit-like) at transport layer.

## Common Mistakes to Avoid

- Confusing datagram with connectionless and virtual circuit with connection-oriented - these are synonymous pairs.

- Thinking virtual circuit establishes a physical dedicated path like circuit switching; it is a logical path only.

- Assuming packets always arrive in order in datagram switching - they frequently arrive out of order.

- Forgetting that virtual circuit requires state maintenance in routers, increasing network complexity.

## Revision Tips

- Create a comparison table between datagram and virtual circuit switching covering connection setup, routing, ordering, QoS, failure handling, and examples.

- Remember the key examples: IP/UDP = datagram; X.25/Frame Relay/ATM = virtual circuit.

- Understand why the Internet uses datagram at network layer (resilience, simplicity) but adds reliability at transport layer (TCP).

- Practice explaining the differences verbally, as exam questions often require descriptive answers.
