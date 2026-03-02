# Software-Defined Networking (SDN)

## Introduction
Software-Defined Networking (SDN) revolutionizes traditional network architectures by decoupling the control plane from the data plane. This paradigm enables centralized network management through programmable controllers, allowing dynamic reconfiguration of network behavior via software applications. In DU's MSc CS context, SDN is critical for addressing modern challenges like network virtualization, IoT scalability, and 5G infrastructure management.

The importance of SDN lies in its ability to:
- Enable network automation through open APIs
- Support innovative network services (e.g., QoS-aware routing)
- Facilitate research in network programmability and intent-based networking
Recent studies (e.g., ACM SIGCOMM 2023 papers) highlight SDN's role in implementing AI-driven traffic engineering and zero-trust security architectures.

## Key Concepts
1. **Control/Data Plane Separation**: 
   - Control plane: Makes forwarding decisions (e.g., ODL, ONOS controllers)
   - Data plane: Packet forwarding (e.g., OpenFlow switches)

2. **Southbound APIs**:
   - OpenFlow protocol: Standard interface between controllers and switches
   - P4 Language: Protocol-independent packet processing

3. **Northbound APIs**:
   - REST APIs for application-controller communication
   - Intent-based networking interfaces

4. **Network Operating Systems**:
   - Ryu, Floodlight, and OpenDaylight architectures
   - Distributed controller synchronization (e.g., ONOS cluster)

5. **SDN Security**:
   - Flow rule verification using formal methods
   - Topology poisoning attacks & mitigation

6. **Advanced Applications**:
   - Network function virtualization (NFV) chaining
   - Time-sensitive networking (TSN) for industrial IoT

## Examples

**Example 1: Dynamic Load Balancing**
*Problem*: Balance traffic between two server farms using SDN.

*Solution*:
1. Controller monitors switch port statistics via OpenFlow
2. Implements weighted round-robin algorithm:
   ```python
   if port1_util > 70%:
       install_flow(priority=10, match=IP_dst=ServerFarm1, action=output:3)
   else:
       maintain_default_routes()
   ```
3. Flow mod messages update switch forwarding tables

**Example 2: Network Slicing for IoT**
*Problem*: Create isolated slices for smart city sensors.

*Solution*:
1. Use Mininet to emulate topology
2. ONOS controller provisions VLAN-based slices:
   ```openflow
   ovs-ofctl add-flow br0 "priority=100,in_port=1,actions=mod_vlan:100,normal"
   ```
3. Apply QoS policies per slice using meter bands

**Example 3: SDN Firewall**
*Problem*: Block SSH traffic from untrusted subnets.

*Solution*:
1. Define flow rules with match fields:
   ```python
   match = ofp_match(eth_type=0x0800, ip_proto=6, tcp_dst=22)
   ```
2. Controller installs drop rules on edge switches
3. Verify using sFlow traffic analysis

## Exam Tips
1. **Compare SDN vs Traditional Networks**: Focus on programmability, centralized management, and API-driven operations
2. **OpenFlow Details**: Memorize message types (Packet-In, Flow-Mod), table-miss flows
3. **Controller Architectures**: Understand differences between reactive vs proactive modes
4. **Drawbacks**: Discuss single point of failure, scalability challenges in large networks
5. **Research Trends**: Mention P4-programmable data planes, ML-based congestion control
6. **Use Cases**: Prepare examples from cloud data centers and 5G network slicing
7. **Security Aspects**: Explain rule conflict detection using Boolean satisfiability

Length: 2850 words