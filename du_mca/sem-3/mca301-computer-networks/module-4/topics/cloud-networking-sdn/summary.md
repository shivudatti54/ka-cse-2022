# Cloud Networking and SDN - Summary

## Key Definitions and Concepts

- **Software Defined Networking (SDN):** A network architecture that separates the control plane from the data plane, enabling centralized network management and programmatic control through software applications.

- **Control Plane:** The network intelligence layer that makes forwarding decisions; in SDN, this resides in a centralized controller rather than individual network devices.

- **Data Plane:** The network layer that performs packet forwarding based on flow rules; in SDN, this consists of simple OpenFlow-enabled switches.

- **OpenFlow:** The standard southbound protocol for communication between SDN controllers and network switches, defining flow table structure and message types.

- **Flow Entry:** An OpenFlow table entry containing match fields, instructions, and counters that define how packets should be processed.

- **Network Virtualization:** Technology that creates multiple isolated virtual networks on shared physical infrastructure (VXLAN, NVGRE).

- **NFV (Network Functions Virtualization):** Virtualizing network services like firewalls and load balancers to run on standard servers rather than dedicated hardware.

- **VPC (Virtual Private Cloud):** An isolated virtual network environment provided by cloud service providers.

## Important Formulas and Theorems

- **OpenFlow Message Types:** packet-in, packet-out, flow-mod, port-status, error—each serves specific functions in controller-switch communication.

- **Flow Matching Process:** Packet arrives → Extract headers → Search flow tables in priority order → Apply first matching entry's instructions → Update counters.

- **SDN Architecture Layers:** Infrastructure Layer (Data Plane) → Control Layer (SDN Controller) → Application Layer (Network Applications).

## Key Points

1. SDN decouples control plane from data plane, unlike traditional networking where both reside in each device.

2. The SDN controller maintains global network visibility and programs flow rules on switches via southbound protocols like OpenFlow.

3. OpenFlow flow entries contain match fields, instructions, and counters for packet processing and monitoring.

4. Popular SDN controllers include Ryu (Python), OpenDaylight (Java), ONOS (distributed), and Floodlight (Java).

5. VXLAN extends VLAN capabilities by supporting up to 16 million virtual networks compared to VLAN's 4096 limit.

6. NFV virtualizes network functions (firewalls, load balancers) while SDN controls the network fabric—they work together but solve different problems.

7. Cloud networking leverages SDN principles to provide on-demand, scalable network resources including VPCs, VPN connections, and load balancers.

8. SDN enables network automation, vendor independence, and faster innovation cycles compared to traditional hardware-centric networking.

## Common Mistakes to Avoid

- Confusing SDN with NFV—they are complementary but distinct technologies addressing different networking challenges.

- Believing SDN eliminates all network hardware; SDN replaces control plane software but still requires physical switches for data forwarding.

- Overlooking controller scalability and security as important design considerations in SDN deployments.

- Assuming OpenFlow is the only southbound protocol—others like NETCONF, OVSDB, and P4 also exist.

## Revision Tips

1. Draw and label the SDN architecture diagram showing all three layers and API connections until you can reproduce it from memory.

2. Create a comparison table between traditional networking and SDN covering 5-6 key dimensions (control, scalability, vendor dependency, configuration complexity, innovation speed).

3. Practice explaining OpenFlow flow processing step-by-step for packet-in scenarios.

4. Review cloud networking concepts through hands-on practice with free tier services from AWS, Azure, or GCP if available.

5. Focus on understanding why SDN was introduced (to solve traditional networking limitations) rather than just memorizing features.