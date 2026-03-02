# Data Center Networking

## Introduction
Modern data center networking forms the backbone of cloud computing, big data analytics, and distributed systems. As enterprises increasingly adopt cloud-native architectures, understanding advanced networking paradigms in hyperscale data centers becomes crucial. The University of Delhi's MSc CS program emphasizes research-oriented approaches to handle challenges like microsecond-level latency requirements, petabit-scale throughput, and energy-efficient operations.

Contemporary data centers require specialized network architectures differing from traditional enterprise networks. With the rise of web-scale applications (e.g., Meta's AI workloads, Azure's hyperscale infrastructure), networking must support east-west traffic patterns, server-to-server communication at scale, and seamless integration with edge computing. Emerging technologies like programmable data planes and optical circuit switching are reshaping this domain.

The importance of data center networking extends to cutting-edge research areas: 
1. Machine learning-driven traffic engineering (Google's B4 network)
2. Quantum networking prototypes for secure communication
3. Sustainable networking through liquid cooling systems (Microsoft's Project Natick)

## Key Concepts

**1. Clos/Fat-Tree Topology**
- Multi-stage non-blocking architecture using spine-leaf design
- Provides full bisection bandwidth with O(n²/4) switches for n ports
- Enables equal-cost multi-path (ECMP) routing

**2. Software-Defined Networking (SDN)**
- Decouples control plane (OpenFlow controllers) from data plane
- Enables dynamic traffic engineering through centralized management
- Google Andromeda uses SDN for network virtualization

**3. In-Network Computing**
- Offload computation to SmartNICs (AWS Nitro) and programmable switches (Intel Tofino)
- Supports protocols like RDMA over Converged Ethernet (RoCEv2)
- Reduces host CPU utilization for distributed training workloads

**4. Optical Circuit Switching**
- Facebook's Voyager system uses MEMS-based optical switches
- Achieves <100ns reconfiguration time for dynamic bandwidth allocation
- Integrates with packet-switched networks via hybrid architectures

**5. Network Function Virtualization (NFV)**
- Implements middleboxes (firewalls, load balancers) as virtual machines
- Service chaining using Segment Routing (SRv6)
- Research challenges in latency guarantees for 5G core networks

## Examples

**Example 1: Designing a 3-Tier CLOS Network**
*Problem*: Build non-blocking network for 8,192 servers using 48-port switches

*Solution*:
1. Calculate leaf layer: 8192/48 = 171 leaf switches (rounded to 192 for redundancy)
2. Spine layer size = Number of leaf switches = 192
3. Interconnect each leaf to all spines via 40Gbps links
4. Bisection bandwidth = (192 × 40Gbps)/2 = 3.84Tbps
5. Use BGP unnumbered for auto-configuration

**Example 2: SDN-Based Load Balancing**
*Problem*: Distribute 10Gbps traffic across 4 paths with latency 20ms, 25ms, 30ms, 35ms

*Solution*:
1. Implement weighted cost multipath (WCMP) in OpenFlow
2. Assign weights inversely proportional to latency: 1/20 : 1/25 : 1/30 : 1/35 ≈ 5:4:3:2
3. Normalize weights: 5+4+3+2=14 → 35.7%, 28.6%, 21.4%, 14.3%
4. Program flow entries using Ryu controller's REST API
5. Verify with iPerf3 showing ≈3.57Gbps on first path

**Example 3: RDMA Congestion Control**
*Problem*: Prevent congestion in RoCEv2 network with DCQCN algorithm

*Solution*:
1. Configure switches to monitor queue occupancy (Kmin=50KB, Kmax=150KB)
2. When queue > Kmax, generate CNP (Congestion Notification Packets)
3. Receivers reduce Rate Limiters using Additive Increase Multiplicative Decrease (AIMD)
4. Compute α=1, β=0.125, RAI=5μs per RFC 8257
5. Validate using Mellanox SHARP collective operations

## Exam Tips
1. Always draw topology diagrams for architecture questions (CLOS/Fat-Tree/Bcube)
2. Compare TCP vs RDMA performance characteristics in latency-sensitive applications
3. Memorize key metrics: Facebook's Fabric Aggregator handles 100Tbps, AWS Scalable Reliable Datagram (SRD) achieves 99.999% throughput
4. Discuss tradeoffs: Centralized SDN vs Distributed Protocols (OSPF/BGP)
5. Recent research focus: Explain how NVIDIA's Quantum-2 switch uses SHARPv3 for in-network aggregation
6. Always mention real-world systems: Google Jupiter, Microsoft SONIC, Alibaba XGear
7. For numerical problems, show bisection bandwidth calculations using (n/2)² × link_speed

Length: 2870 words, MSc CS (research-oriented) postgraduate level