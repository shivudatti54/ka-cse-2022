# Packet Switching - Summary

## Key Definitions and Concepts

- **Packet Switching**: A data transmission method where messages are broken into independent packets that are routed separately across the network.

- **Packet**: A discrete data unit containing a header (control information) and payload (application data).

- **Datagram Switching**: Connectionless packet switching where each packet is routed independently with complete destination information.

- **Virtual Circuit Switching**: Connection-oriented packet switching that establishes a logical path before transmission.

- **Store-and-Forward**: Mechanism where each network node receives, stores, and forwards complete packets.

## Important Formulas and Theorems

- **Number of Packets** = ⌈Total Data Size / Maximum Segment Size⌉

- **Transmission Delay (Tt)** = Packet Size (bits) / Bandwidth (bps)

- **End-to-End Delay** = n × Tt + (n-1) × Tp + n × Tproc + Queueing Delay
  - Where n = number of links, Tp = propagation delay, Tproc = processing delay

## Key Points

- Packet switching emerged from ARPANET in the 1960s and forms the foundation of the modern Internet.

- Each packet contains source/destination addresses, sequence numbers, TTL, and error-checking information.

- Packets can travel independently through different routes, enabling load balancing and fault tolerance.

- Datagram (connectionless) is used in IP networks; Virtual Circuit (connection-oriented) is used in Frame Relay and ATM.

- Packet switching offers better resource utilization compared to circuit switching for bursty traffic.

- Store-and-forward introduces latency but enables error checking and congestion management at each node.

- QoS mechanisms like priority queueing and traffic shaping manage performance in packet-switched networks.

- Queueing occurs when packet arrival rate exceeds service rate, potentially causing delays and packet loss.

## Common Mistakes to Avoid

- **Confusing packet and circuit switching**: Remember circuit switching reserves resources upfront; packet switching shares resources dynamically.

- **Forgetting packet headers**: Students often overlook that headers add overhead to the actual data payload.

- **Ignoring reassembly**: Packets arrive out of order in datagram switching; sequence numbers are crucial for reassembly.

- **Misunderstanding store-and-forward**: This mechanism occurs at every router, not just the final destination.

## Revision Tips

1. Create a comparison table between packet switching and circuit switching covering connection setup, resource allocation, delay characteristics, and efficiency.

2. Practice delay calculation problems covering all delay components (transmission, propagation, processing, queueing).

3. Memorize the key fields in a packet header and understand why each field is necessary.

4. Review real-world protocols: IP uses datagram approach; TCP provides reliability over datagram networks.

5. Understand why packet switching is ideal for the Internet: handles diverse traffic, scales well, and provides resilience against failures.
