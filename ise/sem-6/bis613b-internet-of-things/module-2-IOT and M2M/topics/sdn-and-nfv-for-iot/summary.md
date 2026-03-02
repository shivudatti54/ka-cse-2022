# SDN and NFV for IoT

=====================================

### Overview

Software-Defined Networking (SDN) separates the network control plane from the data plane for centralized programmability, while Network Functions Virtualization (NFV) decouples network functions from proprietary hardware to run as software on standard servers -- together they provide flexible, scalable, and cost-effective infrastructure for IoT.

### Key Points

- **SDN Architecture:** Three layers -- Application Layer (business apps), Control Layer (SDN Controller, the "brain"), and Infrastructure Layer (switches/routers). Connected via Northbound API (apps to controller) and Southbound API (controller to switches, e.g., OpenFlow).
- **SDN Benefits for IoT:** Centralized management and automation of millions of devices, dynamic traffic engineering, enhanced security through anomaly detection, and network slicing for different IoT applications.
- **NFV Core Concept:** Replaces proprietary hardware appliances with Virtual Network Functions (VNFs) running on COTS (Commercial Off-The-Shelf) servers.
- **NFV Benefits for IoT:** Reduced CAPEX/OPEX, elastic scalability, flexible deployment of functions at the network edge, and service chaining for automated data processing pipelines.
- **SDN + NFV Synergy:** SDN provides intelligent connectivity and traffic steering; NFV provides agile virtualized services. SDN controllers can orchestrate both network paths and VNF lifecycle.
- **Network Slicing:** A single physical network is partitioned into multiple virtual networks, each tailored for specific IoT applications (e.g., low-latency robotics vs. bulk sensor data).

### Important Concepts

- SDN separates control and forwarding planes; NFV virtualizes network functions
- OpenFlow is the key Southbound API protocol in SDN
- VNFs can be instantiated, scaled, and terminated on demand
- Service chaining routes IoT data through a sequence of VNFs (filtering, encryption, analytics)

### Notes

- For exams, clearly distinguish SDN (network programmability) from NFV (function virtualization) and explain their synergy.
- The centralized SDN controller is a single point of failure and a high-value attack target -- always mention this challenge.
- Be prepared to draw the three-layer SDN architecture diagram with APIs labeled.
