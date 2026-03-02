# Inter-Cloud Resource Management

## Overview

Inter-cloud computing (cloud federation or cloud bursting) refers to distributing cloud computing services across multiple cloud environments, enabling seamless resource, data, and application sharing between different platforms. This approach overcomes single-provider limitations like resource constraints, vendor lock-in, geographical restrictions, and service outages.

## Key Points

- **Cloud Federation**: Formal agreement between cloud providers to share resources while maintaining autonomy, extending capabilities by borrowing resources during peak demand
- **Cloud Bursting**: Application runs in private cloud but "bursts" into public cloud when demand spikes, requiring seamless integration between environments
- **Broker-Based Architecture**: Cloud broker acts as intermediary for service discovery, SLA negotiation, resource allocation, and monitoring across multiple providers
- **Peer-to-Peer Architecture**: Cloud providers directly interact to share resources without central broker; requires standardized protocols and interfaces
- **Resource Discovery Module**: Identifies available resources across platforms by monitoring availability, maintaining catalogs, and updating status in real-time
- **Resource Selection and Allocation**: Determines optimal provider based on cost, performance, geography, security/compliance, and provider reputation
- **Standard Protocols**: OCCI (RESTful protocol for managing cloud resources), CDMI (Cloud Data Management Interface), CIMI (Cloud Infrastructure Management Interface)
- **Scheduling Strategies**: Cost-Aware (minimize cost), Performance-Oriented (maximize throughput/minimize latency), Energy-Efficient (reduce consumption), Hybrid (multi-criteria)

## Important Concepts

- Hybrid architecture combines broker-based and peer-to-peer models for flexibility in cloud interactions
- Security and identity management uses federated identity, cross-cloud encryption, and consistent security policies
- Challenges include interoperability (proprietary APIs), security/privacy (compliance), performance variability (network latency), vendor lock-in, and complex management
- Real-world implementations: Kubernetes Federation, Apache Mesos with DC/OS, Cloud Management Platforms (RightScale, Scalr, Morpheus)
- Future trends: Serverless cross-cloud functions, AI-driven resource optimization, blockchain for resource exchange, edge cloud integration

## Notes

- Understand differences between cloud bursting (temporary spillover), cloud federation (formal resource sharing), and multi-cloud strategies
- Focus on challenges especially interoperability and security - frequently tested topics
- Be familiar with architectural models (broker-based, peer-to-peer, hybrid) and their trade-offs
- Remember key protocols: OCCI, CDMI, CIMI that enable inter-cloud communication
- Practice explaining real-world scenarios like e-commerce peak demand handling with cloud bursting
- Compare scheduling strategies and know when each is appropriate (cost vs. performance vs. energy)
