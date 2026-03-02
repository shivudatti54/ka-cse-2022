# Data Center Design and Interconnection Networks

## Overview

Modern cloud computing is powered by massive, globally distributed data centers that form the physical foundation of cloud platforms. Data center design, architecture, and interconnection networks directly dictate cloud's core promises: scalability, reliability, performance, and cost-efficiency, providing the tangible infrastructure upon which virtualized cloud services are delivered.

## Key Points

- **Scalability and Elasticity**: Designed for massive horizontal scaling using thousands of standardized commodity servers rather than few powerful servers; allows incremental, cost-effective capacity addition
- **Reliability and High Availability**: Redundancy at every level - power (multiple grids, generators, UPS), networking (multiple fiber paths, redundant switches), cooling (N+1 or 2N systems); eliminates single points of failure (SPOF)
- **Power Usage Effectiveness (PUE)**: Key efficiency metric = Total facility power / IT equipment power; ideal PUE is 1.0; modern cloud datacenters achieve 1.1-1.4 through advanced cooling and efficient power distribution
- **Traditional Three-Tier Network**: Hierarchical model with Core (backbone) → Aggregation (consolidates connections) → Access (ToR switches); drawback is east-west traffic must travel up to core and back causing latency
- **Modern Spine-Leaf Architecture**: Two-tier Clos network where every leaf switch connects to every spine switch; non-blocking fabric with any server communicating through single hop (leaf-spine-leaf) for predictable low latency
- **Spine-Leaf Scalability**: Add more leaf switches for capacity, more spine switches for bandwidth; enables linear pay-as-you-grow scaling with multiple equal-cost paths between leaf switches
- **Software-Defined Networking (SDN)**: Decouples control plane (centralized SDN controller) from data plane (commodity switches); benefits include automation, agility for dynamic policy changes, and traffic optimization
- **Inter-Data Center Networks**: High-speed fiber-optic WANs connect data centers; enables global load balancing, data replication/backup across regions, and CDNs at edge locations

## Important Concepts

- Key datacenter components: Server Racks (compute nodes), Top-of-Rack (ToR) Switch (first network layer), Power Distribution Units (PDUs), Computer Room Air Conditioning (CRAC)
- Design principles: Scalability, Reliability, Efficiency/Sustainability, Security/Compliance, Manageability/Automation
- Spine-leaf advantages over three-tier: Non-blocking fabric, predictable latency, linear scalability, redundancy, cost-effective using commodity switches
- Virtualization enables Software-Defined Data Centers (SDDC) where compute, storage, networking delivered as automated, policy-driven services
- Global cloud fabric requires WAN interconnectivity, global load balancing, data replication, and CDN edge locations

## Notes

- Focus on understanding why spine-leaf is superior for east-west traffic (predictable latency, scalability)
- Know PUE metric definition and typical values (ideal 1.0, modern 1.1-1.4, importance for cloud providers)
- Understand SDN core concept: separation of control and data planes with benefits (automation, agility)
- Remember datacenter components and how physical layer relates to logical network design
- Connect datacenter design to higher-level concepts: enables IaaS/PaaS/SaaS delivery
- Be able to compare three-tier vs. spine-leaf architectures in tabular format
- Understand virtualization's role in increasing utilization from 10-15% to 60-80% or higher
