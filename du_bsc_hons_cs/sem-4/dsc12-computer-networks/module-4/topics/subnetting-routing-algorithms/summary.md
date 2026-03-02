# Subnetting & Routing Algorithms

## Introduction
Subnetting and routing algorithms are fundamental concepts in computer networking that enable efficient IP address management and optimal packet forwarding across networks. These topics form a core part of the Delhi University BSc (Hons) Computer Science syllabus under the NEP 2024 UGCF framework.

---

## 1. Subnetting

### Definition & Purpose
- **Subnetting** divides a large network into smaller logical sub-networks (subnets)
- Improves security, reduces broadcast domain size, and optimizes IP address allocation
- Enables hierarchical network design

### Key Components
- **IP Address Classes**: Class A, B, C (based on default subnet masks)
- **Subnet Mask**: 32-bit number separating network and host portions
- **CIDR (Classless Inter-Domain Routing)**: Notation like /24, /26 representing subnet bits
- **Default Gateway**: Router interface connecting subnet to other networks

### Subnetting Concepts
- **Fixed-Length Subnet Mask (FLSM)**: All subnets use same mask size
- **Variable-Length Subnet Mask (VLSM)**: Subnets of different sizes for efficient utilization
- **Network Address**: First IP (all host bits = 0)
- **Broadcast Address**: Last IP (all host bits = 1)
- **Usable Hosts**: 2ⁿ - 2 (where n = host bits)

### Calculation Formula
```
Number of subnets = 2^(subnet bits)
Number of hosts per subnet = 2^(host bits) - 2
```

---

## 2. Routing Algorithms

### Classification

**Static Routing**
- Manually configured routes
- Suitable for small networks
- No routing overhead, more secure

**Dynamic Routing**
- Automatically learns routes from other routers
- Adapts to network changes
- Protocols: RIP, OSPF, EIGRP, BGP

### Types of Dynamic Routing Algorithms

| Algorithm | Type | Metric | Convergence | Scalability |
|-----------|------|--------|-------------|-------------|
| **RIP** | Distance Vector | Hop Count | Slow | Small networks |
| **IGRP** | Distance Vector | Bandwidth, Delay | Medium | Medium networks |
| **OSPF** | Link State | Cost | Fast | Large networks |
| **EIGRP** | Hybrid | Bandwidth, Delay, Load | Fast | Large networks |
| **BGP** | Path Vector | Path Attributes | Slow | Internet backbone |

### Key Routing Concepts
- **Routing Metric**: Value used to determine optimal path (hop count, bandwidth, delay)
- **Administrative Distance**: Trustworthiness of routing information source
- **Convergence Time**: Time for all routers to agree on network topology
- **Routing Loop**: Problem where packets bounce between routers indefinitely
- **Split Horizon**: Prevents routing loops by not advertising routes back to source
- **TTL (Time to Live)**: Prevents infinite packet circulation

---

## Conclusion
Subnetting provides efficient IP address management through logical network division, while routing algorithms ensure optimal packet delivery across interconnected networks. Understanding subnetting calculations and routing protocol characteristics is essential for network design and troubleshooting—key skills for any computer science professional. Mastery of VLSM, CIDR notation, and routing metrics aligns with the Delhi University syllabus requirements for practical networking knowledge.

---

*Reference: Delhi University BSc (Hons) CS NEP 2024 UGCF Syllabus – Computer Networks Unit*