# Network Function Virtualization (NFV) - Summary

## Key Definitions and Concepts

- **NFV (Network Function Virtualization):** Virtualizing network functions (firewalls, load balancers, routers) onto standard commercial hardware instead of proprietary appliances
- **NFVI (Network Function Virtualization Infrastructure):** Combined hardware and software resources forming the virtualization platform
- **VNF (Virtualized Network Function):** Software implementation of a network function running on NFVI
- **MANO (Management and Orchestration):** Framework for managing VNF lifecycle including VIM, VNFM, and NFVO
- **SFC (Service Function Chaining):** Ordered sequence of network functions through which traffic flows
- **VNFD (VNF Descriptor):** Declarative specification of a VNF's requirements
- **NSD (Network Service Descriptor):** Specification defining a network service composed of multiple VNFs

## Important Formulas and Theorems

- NFV reduces CapEx by 60-70% compared to traditional hardware deployments
- VNF scaling can be vertical (adding resources) or horizontal (adding instances)
- Service chain latency increases with each VNF hop in the forwarding graph

## Key Points

1. ETSI established the NFV architectural framework in 2012, defining NFVI, VNF, and MANO as core components

2. NFVI provides compute, storage, and network resources; VNFs are the virtualized network services; MANO orchestrates the entire lifecycle

3. MANO consists of three sub-components: VIM (resource management), VNFM (VNF lifecycle), and NFVO (service orchestration)

4. NFV enables hardware independence, dynamic scaling, elastic resource allocation, and faster service deployment

5. Service Function Chaining (SFC) uses NSH (Network Service Header) to steer traffic through specific VNFs regardless of physical topology

6. Performance optimization techniques include DPDK (kernel bypass), SR-IOV (direct device assignment), CPU pinning, and huge pages

7. Container-based VNFs (CNF) are emerging as lightweight alternatives to VM-based VNFs

8. NFV is fundamental to 5G core network architecture enabling network slicing and edge computing

## Common Mistakes to Avoid

- Confusing NFV with SDN - NFV virtualizes functions while SDN controls the network
- Treating all VNFs the same - some require bare-metal access for performance
- Ignoring MANO - the orchestration layer is critical for NFV operation
- Underestimating network complexity in service chaining - latency increases with each hop

## Revision Tips

1. Draw and label the ETSI NFV architecture diagram from memory

2. Memorize the three MANO components and their specific responsibilities

3. Practice explaining a complete NFV deployment with a real-world example like virtual firewall

4. Understand how SFC works and be able to trace packet flow through a service chain

5. Review current NFV research trends - 5G, edge computing, and container-native functions are hot topics