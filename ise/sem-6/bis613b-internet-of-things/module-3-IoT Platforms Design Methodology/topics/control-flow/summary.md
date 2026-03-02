# Control Flow in IoT Systems

=====================================

### Overview

Control flow in IoT governs the logical sequence of operations across the entire system, from sensor nodes to the cloud and back to actuators. It determines how an IoT system reacts to data, events, and user commands, and is implemented as centralized, decentralized, or hybrid architectures.

### Key Points

- **Centralized Control (Cloud-Centric):** All logic and decisions are made in the cloud; sensors send data to cloud, cloud processes and sends commands back to actuators
- **Decentralized (Edge-Based) Control:** Control logic is placed on local gateways or edge devices for immediate decision-making without cloud dependency
- **Hybrid Control:** Combines edge control for time-critical decisions with cloud control for analytics and long-term optimization
- **Rule Engines:** Control logic is implemented using IF-THEN-ELSE rules that link sensor triggers to actuator actions
- **Centralized Pros/Cons:** High computational power but suffers from latency and internet dependency
- **Edge Pros/Cons:** Ultra-low latency and offline operation but higher cost and complexity at the edge
- **Trigger-Action Programming:** Declarative rules where a trigger condition (sensor data, event, schedule) triggers a specific action

### Important Concepts

- Three control flow paradigms: Centralized, Decentralized (Edge), Hybrid
- Trade-offs between latency, reliability, computational power, and cost
- Rule engines (AWS IoT Rules Engine, Node-RED) for implementing control logic
- Edge computing overcomes latency and connectivity limitations of cloud-centric models

### Notes

- For exam scenarios, be prepared to recommend the appropriate control flow model based on application requirements (e.g., industrial safety needs edge control)
- Hybrid is the most common real-world approach, balancing responsiveness with powerful cloud analytics
- Understand the comparison table: Centralized vs Decentralized vs Hybrid with their respective pros and cons
