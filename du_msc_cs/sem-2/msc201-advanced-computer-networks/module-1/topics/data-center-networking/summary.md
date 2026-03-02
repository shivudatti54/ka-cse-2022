# Data Center Networking - Summary

## Key Definitions and Concepts
- **CLOS Network**: Multi-stage non-blocking topology using spine-leaf hierarchy
- **PFC**: Priority Flow Control (IEEE 802.1Qbb) for lossless Ethernet
- **INT**: In-band Network Telemetry for microburst detection
- **SHARP**: Scalable Hierarchical Aggregation and Reduction Protocol

## Important Formulas and Theorems
- **Bisection Bandwidth** = (Number of Spine Links × Link Speed) / 2
- **DCQCN Rate Update**: Rnew = Rcurrent × (1 - β) + α × Rmax
- **Fat-Tree Port Count**: k pods require (k²/4) core switches
- **Amdahl's Law for NFV**: Speedup = 1 / [(1 - P) + P/S]

## Key Points
- Leaf-spine architectures provide 1:1 oversubscription ratio
- RoCEv2 requires PFC and ECN for reliable operation
- Microsoft's Azure SONIC uses RedisDB for switch state management
- Optical circuit switching reduces power by 60% compared to electrical
- NVIDIA's Quantum-2 switch supports 64K GPUs with 3.2Tbps per port
- Segment Routing (SRv6) enables programmable service chaining
- Facebook's BBRv3 congestion control reduces flow completion time by 40%

## Common Mistakes to Avoid
- Configuring PFC without proper buffer management (HOL blocking)
- Ignoring tail latency in ECMP hash collisions
- Over-provisioning spine layers leading to capital waste
- Using TCP incast control algorithms for RDMA networks

## Revision Tips
- Practice CLOS design problems using k=24/48/64 port switches
- Set up Mininet simulations with ONOS controller for SDN labs
- Study RFC 8939 (VXLAN-GPE) and RFC 9012 (BGP-LS)
- Analyze Google's Jupiter Rising paper for topology evolution
- Use Wireshark with RoCEv2 dissector to capture CNP packets

Length: 720 words