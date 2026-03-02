# Python Data Types and Data Structures for IoT

=====================================

### Overview

IoT systems generate massive volumes of heterogeneous data from diverse sensors and devices. Understanding fundamental data types (sensor, actuator, metadata, multimedia) and choosing appropriate data structures (arrays, queues, JSON, Protobuf) is critical for designing efficient and scalable IoT platforms.

### Key Points

- **Data by Source:** Sensor data (numeric measurements), actuator status (boolean/enum), device metadata (key-value pairs), and multimedia data (images, audio)
- **Data by Structure:** Structured (relational tables), semi-structured (JSON, XML, CSV), and unstructured (images, video)
- **Data by Time:** Streaming data (continuous real-time flow) and time-series data (indexed by time, most common in IoT)
- **JSON:** The de facto standard for IoT data interchange; human-readable, lightweight, and language-independent
- **Protocol Buffers (Protobuf):** Binary format by Google; more compact and faster than JSON, ideal for bandwidth-constrained scenarios
- **Data Structures by Layer:** Arrays/Structs on device, Queues for buffering, JSON for transmission, Avro for big data pipelines
- **CSV:** Simple tabular format used for exporting historical time-series data for analysis

### Important Concepts

- JSON vs Protobuf trade-offs: JSON is flexible and readable; Protobuf is compact and fast
- Data flow from sensor node (Array/Buffer/Struct) through gateway to cloud (JSON/Avro) to storage (databases)
- Queues (FIFO) are crucial for decoupling sensor reading tasks from network transmission tasks
- Time-series data is the most common data type in IoT applications

### Notes

- Be prepared to compare JSON and Protobuf and justify choosing one over the other based on a scenario
- Associate data structures with correct IoT architecture layers: device, gateway/fog, cloud, application
- Python dictionaries and lists are the fundamental structures for creating and manipulating JSON-based IoT data
