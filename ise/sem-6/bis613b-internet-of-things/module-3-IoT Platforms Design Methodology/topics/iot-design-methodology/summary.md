# IoT Design Methodology

=====================================

### Overview

IoT Design Methodology provides a systematic seven-step framework for developing IoT solutions, guiding developers from concept to deployment. It addresses the unique intersection of hardware, software, networking, and data analytics that distinguishes IoT from traditional software development.

### Key Points

- **Step 1 - Purpose and Requirements:** Define the system purpose, stakeholders, functional requirements (what the system does), and non-functional requirements (scalability, availability, security)
- **Step 2 - Process Specification:** Describe system behavior abstractly using Data Flow Diagrams (DFDs) showing how data flows and events trigger actions
- **Step 3 - Domain Model:** Identify key entities, their properties, and relationships using UML class diagrams
- **Step 4 - Information Model:** Define data structure, format, schema, metadata, and semantics for data exchanged between components
- **Step 5 - Service Specification:** Define software services such as Device Service, Data Ingestion, Storage, Analytics, and API services
- **Step 6 - IoT Level Specification:** Choose the deployment complexity level (Level 1 through Level 6) based on device count and processing architecture
- **Step 7 - Functional View:** Translate abstract specifications into concrete hardware, protocols, cloud platforms, and databases
- **IoT Levels:** Level 1 (single device, local) to Level 6 (large-scale cloud-based WAN), with Level 4 introducing fog/edge nodes

### Important Concepts

- Domain Model focuses on entities and relationships; Information Model focuses on data structure and semantics
- IoT Levels 1-6 classification based on device count, storage location, and analytics capabilities
- Service-Oriented Architecture (SOA) and Microservices patterns for service design
- Common protocols: MQTT, CoAP, HTTP; Common platforms: AWS IoT Core, Azure IoT Hub

### Notes

- Memorize all seven steps in order: Purpose, Process, Domain, Information, Service, Level, Functional View
- Be prepared to apply the methodology to a given scenario by walking through each step
- Know the difference between Domain Model (entities) and Information Model (data schemas) as this is a frequently tested distinction
