# IoT Levels and Deployment Templates

=====================================

### Overview

IoT systems are classified into six levels based on complexity, number of nodes, storage, and processing capabilities. Deployment templates provide standardized approaches (cloud-centric, edge-centric, fog computing, hybrid) for implementing IoT solutions based on specific requirements.

### Key Points

- **Level 1:** Single device performing all functions (sensing, processing, storage) -- e.g., smart thermostat.
- **Level 2:** Single node with local storage for historical data and offline operation -- e.g., weather station.
- **Level 3:** Single node with local storage and edge analytics, reducing cloud dependency -- e.g., security camera with facial recognition.
- **Level 4:** Multiple sensing nodes with a central node for aggregation and local processing -- e.g., home automation system.
- **Level 5:** Multiple nodes sending data to cloud for centralized storage and processing -- e.g., environmental monitoring.
- **Level 6:** Hybrid edge-plus-cloud architecture with distributed computing for maximum scalability -- e.g., smart city infrastructure.
- **Deployment Templates:** Cloud-Centric (centralized, scalable, latency issues), Edge-Centric (low latency, offline capable), Fog Computing (balanced workload), Hybrid (optimal flexibility).

### Important Concepts

- Levels progress from simple (Level 1) to complex (Level 6) in nodes, storage, and processing
- Cloud-Centric template: high scalability but network-dependent with latency concerns
- Edge-Centric template: low latency and offline capability but limited analytics scope
- Fog Computing template: intermediate processing between edge and cloud using fog nodes/gateways
- Design considerations: scalability, network constraints, security, cost (CapEx vs OpEx), and data management needs

### Notes

- Memorize the six levels with their key characteristics (number of nodes, storage location, processing type) and one example each.
- When recommending a level or template for a scenario, justify by discussing all factors: latency, bandwidth, cost, scalability, and security.
- Edge processing suits real-time needs; cloud processing suits big data analytics -- know when to apply each.
