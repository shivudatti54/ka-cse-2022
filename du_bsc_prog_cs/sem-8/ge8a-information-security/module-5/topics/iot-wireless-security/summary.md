# IoT Wireless Security - Summary

## Key Definitions and Concepts

- **Internet of Things (IoT):** Network of physical devices embedded with sensors, software, and connectivity enabling data collection and exchange
- **Perception Layer:** Bottom layer of IoT architecture with sensors and actuators for data acquisition
- **Network Layer:** Communication infrastructure connecting IoT devices to processing systems
- **Firmware:** Software embedded in device hardware controlling device functionality
- **OTA Updates:** Over-the-air mechanisms for remotely updating device firmware

## Important Formulas and Theorems

- AES-128/256 encryption: Standard symmetric encryption used in Zigbee, BLE, and WiFi
- TLS 1.3: Transport layer security protocol for secure communications
- X.509 Certificates: Digital certificates for device authentication
- Elliptic Curve Cryptography (ECC): Lightweight asymmetric cryptography suitable for constrained IoT devices

## Key Points

- IoT wireless protocols operate across various frequency bands: 2.4 GHz (WiFi, Zigbee, BLE), sub-GHz (LoRaWAN), and 800-900 MHz (Z-Wave)

- Major security challenges include resource constraints, heterogeneous device ecosystems, legacy unpatched devices, physical accessibility, and manufacturer default configurations

- Critical attack vectors: eavesdropping, replay attacks, MITM attacks, DoS/DDoS attacks, and firmware exploitation

- The Mirai botnet (2016) exploited default credentials in IoT devices to compromise 600,000+ devices, demonstrating the scale of IoT vulnerability

- Security frameworks include: secure device onboarding, network segmentation using VLANs, strong encryption (AES-256), and cryptographically signed OTA updates

- BLE vulnerabilities include legacy pairing methods susceptible to man-in-the-middle attacks and BLE Sniffing attacks

- Defense-in-depth strategy combines network security, device authentication, encryption, and continuous monitoring

## Common Mistakes to Avoid

- Assuming all IoT devices support the same security protocols—they vary significantly based on manufacturer and protocol

- Overlooking physical security; attackers can extract keys and firmware from physically accessible devices

- Neglecting the importance of unique, non-default credentials for each device

- Assuming encryption alone is sufficient—key management and secure implementation are equally critical

- Ignoring the need for regular firmware updates and patches

## Revision Tips

1. Create a comparative table of IoT protocols covering frequency, data rate, range, power consumption, and security features

2. Practice explaining attack scenarios step-by-step, as exam questions often require describing attack methodologies

3. Review the Mirai botnet case study thoroughly—it frequently appears in examinations

4. Focus on the relationship between resource constraints and security implementation challenges in IoT

5. Memorize recommended security measures and be prepared to suggest solutions for given IoT deployment scenarios