# Label Switched Router (LSR)

## Introduction

Label Switched Router (LSR) is a fundamental component in Multi-Protocol Label Switching (MPLS) networks, which represents a significant advancement in packet forwarding technology. Traditional IP routing relies on longest prefix matching at each router, which can be computationally expensive and slow for high-speed networks. LSR introduces a label-based forwarding mechanism that simplifies the forwarding decision process, enabling faster packet processing and more efficient network performance.

In MPLS architecture, LSRs are the devices that perform label switching operations. They operate at layer 2.5 (between the traditional data link layer and network layer), examining the label attached to a packet rather than analyzing the entire IP header at every hop. This approach significantly reduces the processing overhead and enables the implementation of sophisticated traffic engineering capabilities. LSRs form the backbone of service provider networks, enabling the delivery of high-quality services such as VPN, traffic engineering, and quality of service (QoS).

The development of LSR and MPLS was driven by the need for faster forwarding in increasingly complex networks. As internet traffic grew exponentially, traditional routing protocols struggled to keep pace with the demands for speed and efficiency. LSR addresses these challenges by introducing a more streamlined forwarding mechanism that decouples the forwarding decision from the network layer analysis, resulting in improved network performance and flexibility.

## Key Concepts

### Architecture of LSR

An LSR consists of three main functional components: the control plane, the forwarding plane, and the management plane. The control plane is responsible for maintaining routing information and label distribution protocols. It runs traditional routing protocols like OSPF, IS-IS, or BGP to learn network topology and determines label information through protocols such as LDP (Label Distribution Protocol) or RSVP-TE (Resource Reservation Protocol-Traffic Engineering). The forwarding plane, also called the data plane, performs the actual packet forwarding based on label operations. It uses the label information base (LIB) to determine the next hop and performs label push, pop, and swap operations. The management plane handles network configuration, monitoring, and troubleshooting.

### Label Operations

LSR performs three primary label operations: push (insert), swap (replace), and pop (remove). When a packet enters an MPLS domain, the ingress LSR performs a push operation, adding a label stack to the packet. At each intermediate LSR, the label is swapped with a new label corresponding to the next hop in the label-switched path (LSP). At the egress LSR, a pop operation removes the label, and the packet is forwarded based on its original IP header. These operations enable the creation of end-to-end label-switched paths that can traverse multiple LSRs efficiently.

### Label Information Base (LIB)

The Label Information Base is a critical data structure maintained by each LSR. It contains mappings between incoming labels and outgoing labels, along with the corresponding outgoing interface and next-hop information. The LIB is populated through label distribution protocols and is used by the forwarding plane to perform label switching decisions. Each LSR maintains entries for all label bindings it has learned from its neighbors, enabling it to make forwarding decisions quickly without consulting routing tables.

### Label Distribution Protocol (LDP)

LDP is the standard protocol used by LSRs to exchange label binding information. It operates between adjacent LSRs in an MPLS domain, establishing neighbor relationships and sharing label mappings. LDP messages include discovery, adjacency, session, and notification messages. The protocol ensures that all LSRs in the network have consistent label information, enabling proper packet forwarding through label-switched paths. LDP supports both ordered and independent control modes, allowing network operators to choose the label distribution behavior that best suits their network requirements.

### Types of LSR

There are three types of LSR based on their position in the MPLS network: Ingress LSR (Label Edge Router -LER), Intermediate LSR, and Egress LSR. The ingress LSR is responsible for classifying packets and adding the initial label stack. It determines the appropriate LSP for each packet based on factors such as destination address, QoS requirements, or traffic engineering policies. Intermediate LSRs perform label swapping operations, forwarding packets along the established LSP. The egress LSR removes the label and delivers the packet to its final destination using traditional IP forwarding.

### Penultimate Hop Popping

Penultimate Hop Popping (PHP) is an optimization technique in MPLS where the label is removed by the LSR immediately before the egress router rather than by the egress router itself. This approach reduces the processing burden on the egress LSR and improves efficiency. The egress LSR signals the penultimate hop to perform the pop operation by sending a special implicit null label. PHP is particularly beneficial in networks with high traffic volumes, as it reduces the label operations required at the egress point.

## Examples

### Example 1: Basic Label Switching Operation

Consider a simple MPLS network with four LSRs: LSR-A (Ingress), LSR-B (Intermediate), LSR-C (Intermediate), and LSR-D (Egress). A packet needs to travel from source to destination through this network.

Step 1: At LSR-A (Ingress), the packet enters with IP header destination 192.168.1.10. LSR-A performs a lookup in its forwarding table and determines the appropriate LSP. It pushes label 100 onto the packet and forwards it to LSR-B.

Step 2: At LSR-B, the incoming label 100 is looked up in the LIB. The LIB indicates that label 100 should be swapped with label 200 for forwarding toward LSR-C. LSR-B performs the swap operation and forwards the packet.

Step 3: At LSR-C, the incoming label 200 is swapped with label 300 for forwarding to LSR-D. The packet continues along the LSP.

Step 4: At LSR-D (Egress), the incoming label 300 is popped. The packet now contains only the original IP header and is forwarded to the final destination using traditional IP routing.

This example demonstrates how LSRs perform label operations to forward packets efficiently through an MPLS domain without examining the IP header at each hop.

### Example 2: Label Distribution Process

Consider two adjacent LSRs: LSR-X and LSR-Y. They need to establish label bindings for forwarding traffic between them.

Step 1: LSR-X and LSR-Y establish an LDP session using discovery and adjacency messages. They exchange Hello messages to discover each other and establish a TCP connection for reliable communication.

Step 2: Once the session is established, LSR-X assigns a local label (e.g., 500) for the prefix 10.1.1.0/24 and sends a label mapping message to LSR-Y. The mapping message contains the FEC (Forwarding Equivalence Class), which is the IP prefix in this case, and the local label.

Step 3: LSR-Y receives the mapping and stores it in its LIB. LSR-Y assigns its own local label (e.g., 700) for the same FEC and sends its label mapping back to LSR-X.

Step 4: Both LSRs now have complete label binding information. When LSR-X needs to forward packets destined for 10.1.1.0/24 to LSR-Y, it will use label 700. When LSR-Y forwards packets to LSR-X, it will use label 500.

This process ensures that both routers have consistent label information for forwarding packets along the label-switched path.

### Example 3: Traffic Engineering with LSR

In a service provider network, an LSR can be configured to implement traffic engineering by establishing multiple LSPs with different constraints. Consider a network where LSR-P is the ingress router and LSR-Q is the egress router, with multiple paths available through intermediate LSRs.

The network administrator configures two LSPs: one for high-priority traffic (LSP1) and one for best-effort traffic (LSP2). LSP1 is configured to use the path through LSR-R1 (low latency path) with bandwidth reservation. LSP2 uses the path through LSR-R2 (default path) without bandwidth guarantees.

When high-priority traffic arrives at LSR-P, it is classified and assigned to LSP1. The ingress LSR pushes label 1000 (for LSP1) and the packet travels through the reserved path. For regular traffic, label 2000 (for LSP2) is pushed, and the packet follows the default path.

This example illustrates how LSRs enable sophisticated traffic engineering capabilities in MPLS networks, allowing network operators to optimize resource utilization and meet different service level agreements.

## Exam Tips

1. **Remember the three label operations**: Push (adding label at ingress), Swap (replacing label at intermediate LSRs), and Pop (removing label at egress). These are frequently asked in exams.

2. **Understand the difference between LER and LSR**: Label Edge Routers (LER) are at the boundaries of the MPLS domain performing classification and label imposition/removal, while LSRs are the core routers performing label switching.

3. **Know the planes of LSR architecture**: Control plane (routing and label distribution), Forwarding plane (actual packet switching based on labels), and Management plane (configuration and monitoring). Questions often ask about the functions of each plane.

4. **Penultimate Hop Popping (PHP)**: Remember that PHP is an optimization where the penultimate LSR removes the label instead of the egress LSR, reducing processing at the egress router.

5. **LDP functions**: LDP is used for label distribution between LSRs. Know that it establishes sessions, exchanges label bindings, and maintains the Label Information Base (LIB).

6. **LIB vs RIB vs FIB**: Understand the difference between Label Information Base (LIB - stores label mappings), Routing Information Base (RIB - traditional routing table), and Forwarding Information Base (FIB - optimized routing table for forwarding).

7. **Advantages of LSR-based forwarding**: Faster forwarding (label lookup vs IP prefix match), traffic engineering capabilities, QoS support, and VPN support. These are commonly asked as "advantages of MPLS" questions.

8. **Label stack concept**: Remember that MPLS supports a stack of labels, with the top label being used for forwarding. Inner labels are used for hierarchical MPLS or VPNs.

9. **FEC (Forwarding Equivalence Class)**: Understand that packets are grouped into FECs based on characteristics like destination address, service class, or tunnel identifier. All packets in an FEC follow the same LSP.

10. **MPLS position in OSI model**: MPLS operates at layer 2.5, between the data link layer (layer 2) and network layer (layer 3). This is a classic exam question.
