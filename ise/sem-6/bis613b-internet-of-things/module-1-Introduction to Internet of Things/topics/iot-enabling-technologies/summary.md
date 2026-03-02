# IoT Enabling Technologies

=====================================

### Overview

IoT is not a single technology but a convergence of several enabling technologies that work together to facilitate device connectivity, data processing, communication, and security. These technologies form the backbone of any IoT deployment.

### Key Points

- **Wireless Sensor Networks (WSNs):** Foundation for data acquisition, consisting of distributed sensor nodes and a gateway/sink node that aggregates data.
- **Identification Technologies:** RFID and EPC provide unique identity to physical objects for tracking and management without line-of-sight requirements.
- **Short-Range Protocols:** BLE (low power, wearables), Zigbee (mesh networking, home automation), Wi-Fi (high data rate, high power), Z-Wave (home automation).
- **LPWAN Protocols:** LoRaWAN (long range, low power, smart cities) and NB-IoT/LTE-M (cellular-based, licensed spectrum, high reliability).
- **Embedded Systems:** Dedicated low-power computing systems (MCUs like ESP32, MPUs like Raspberry Pi) integrated into IoT devices.
- **Cloud Computing:** Provides scalable computing (IaaS, PaaS, SaaS) for storing and processing massive IoT data streams.
- **Big Data Analytics:** Processes IoT data characterized by Volume, Velocity, and Variety using platforms like Hadoop and Spark.
- **Security Technologies:** Includes cryptography (AES), secure protocols (TLS/SSL), device authentication, and hardware security modules.

### Important Concepts

- Protocol comparison: BLE vs Zigbee vs Wi-Fi vs LoRaWAN vs NB-IoT (range, power, data rate trade-offs)
- WSN architecture: sensor nodes communicating through a gateway/sink node to the cloud
- Cloud service models: IaaS, PaaS, SaaS and their roles in IoT
- Middleware for interoperability between disparate devices and protocols
- Three Vs of Big Data: Volume, Velocity, Variety

### Notes

- Power consumption is the most critical trade-off factor when choosing communication protocols -- always discuss this in exam answers.
- Be prepared to compare protocols in table format: range, power consumption, data rate, and key applications.
- Always mention security implications when discussing any IoT enabling technology.
