# Logical Design of IoT

=====================================

### Overview

The logical design of IoT defines the abstract representation of system entities, information flow, and component interactions without specifying physical implementation. It focuses on communication protocols, application logic, data formats, and functional blocks that form the blueprint of an IoT solution.

### Key Points

- **Device and Sensing Block:** Sensors detect physical properties, actuators perform actions, and MCUs/MPUs process data and manage communication.
- **Communication Block:** Handles data transfer using D2D (Bluetooth, Zigbee), D2G (Wi-Fi, LoRaWAN), and G2C (Ethernet, Cellular) protocols; gateways act as bridges.
- **Data Storage and Processing Block:** Cloud/backend handles data ingestion, storage (SQL/NoSQL), and processing (real-time for alerts, batch for trend analysis).
- **Application and Interface Block:** Delivers value via dashboards, mobile apps, APIs, and business logic rules.
- **MQTT Protocol:** Lightweight publish-subscribe messaging with three roles -- Publisher (sensor), Subscriber (app), and Broker (server routing messages).
- **Communication Models:** Request-Response (HTTP), Publish-Subscribe (MQTT), Push-Pull, Exclusive Pair (WebSockets).
- **Information Modeling:** YANG data modeling language standardizes data structure and semantics for interoperability.

### Important Concepts

- Four functional blocks: Device/Sensing, Communication, Data Storage/Processing, Application/Interface
- MQTT architecture: Publisher sends to a topic on a Broker, Subscriber receives from that topic
- Logical design answers "how the system operates" vs physical design answers "what devices are used"
- IoT Levels 1-6 classify systems by complexity, node count, and cloud involvement
- Protocol selection depends on range, data rate, and power consumption trade-offs

### Notes

- Describe logical design as a data flow in exam answers: sensed, transmitted, processed, presented to user.
- MQTT (publisher, subscriber, broker roles) is one of the most frequently examined IoT topics.
- Always justify protocol choices by citing range, power, and data rate characteristics relevant to the application.
