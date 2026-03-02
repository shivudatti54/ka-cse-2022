# IoT Platforms Design Methodology

=====================================

### Overview

IoT Platforms Design Methodology extends the core IoT design methodology by focusing on platform-level decisions including the seven-step framework, IoT levels, and the role of Python in IoT development. It provides the blueprint for choosing appropriate platforms, protocols, and tools for deployment.

### Key Points

- **Seven-Step Framework:** Purpose/Requirements, Process Specification, Domain Model, Information Model, Service Specification, IoT Level Specification, and Functional View Specification
- **Functional View Details:** Specifies physical devices (Raspberry Pi, ESP32), communication protocols (MQTT, HTTP, LoRaWAN), cloud platforms, databases, and visualization tools
- **IoT Level Selection:** Critical architectural decision ranging from Level 1 (single local device) to Level 6 (global cloud-based WAN system)
- **Level 4 Significance:** Introduces fog/edge computing nodes for local pre-processing before cloud transmission
- **Python in IoT:** Used for device programming (MicroPython), gateway logic, cloud services (AWS Lambda, Flask), and data analytics (Pandas, NumPy)
- **Service Design Patterns:** SOA and Microservices patterns for building Device, Ingestion, Storage, Analytics, and API services
- **Weather Monitoring Case Study:** Demonstrates applying all seven steps using ESP32 sensors, Raspberry Pi gateway, MQTT protocol, and AWS cloud services

### Important Concepts

- Platform selection based on IoT level requirements (edge vs cloud processing)
- Data Flow Diagrams for abstract process specification
- Difference between Domain Model (entities/relationships) and Information Model (data schema/semantics)
- Common IoT protocols: MQTT for telemetry, HTTP for REST APIs, LoRaWAN for long-range

### Notes

- Be able to identify the correct IoT Level (1-6) for any given system description
- For exam scenarios, walk through each of the seven steps logically when asked to design an IoT system
- Python serves at every layer: device (MicroPython), gateway (scripts), cloud (serverless functions), and analytics
