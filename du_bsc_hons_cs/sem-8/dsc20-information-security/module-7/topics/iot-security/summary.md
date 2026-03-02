# IoT Security - Summary

## Key Definitions and Concepts

- **Internet of Things (IoT)**: Network of physical objects embedded with sensors, software, and connectivity to exchange data with other devices over the internet.
- **Perception Layer**: Physical layer with sensors and actuators that interact with the physical world; vulnerable to physical tampering and data injection.
- **Network Layer**: Communication layer transmitting data via protocols like Wi-Fi, Zigbee, and MQTT; susceptible to eavesdropping and man-in-the-middle attacks.
- **Application Layer**: Service layer providing user interfaces and data processing; faces threats from insecure APIs and weak authentication.
- **Defense in Depth**: Security strategy implementing multiple layers of protection so that if one fails, others still provide security.

## Important Formulas and Theorems

- **OWASP IoT Top 10**: Standard list of most critical IoT security vulnerabilities (weak passwords, insecure services, ecosystem interfaces, update mechanisms, outdated components, privacy issues, insecure data transfer, device management, insecure defaults, physical hardening).
- **DTLS**: Datagram Transport Layer Security—adaptation of TLS for unreliable, datagram-based IoT communication protocols.
- **Secure Boot**: Cryptographic process verifying firmware integrity before execution to prevent malicious code injection.

## Key Points

- IoT devices face unique security challenges due to limited computational resources, heterogeneous nature, massive scale, and physical accessibility.
- The three-layer architecture (perception, network, application) helps identify security requirements at different system levels.
- Default credentials and hardcoded passwords remain the leading cause of IoT breaches (e.g., Mirai botnet).
- Network segmentation is essential to isolate IoT devices from critical business and personal systems.
- TLS/DTLS provides encryption for data in transit; AES-128/256 secures data at rest.
- MQTT over TLS (port 8883) is the recommended secure implementation for lightweight IoT messaging.
- Privacy-by-design principles—data minimization, informed consent, and user control—are critical for IoT compliance with regulations like GDPR.
- Regular firmware updates and secure OTA (Over-The-Air) mechanisms are necessary to patch vulnerabilities throughout the device lifecycle.

## Common Mistakes to Avoid

- Assuming traditional IT security solutions directly apply to resource-constrained IoT devices without considering computational limitations.
- Ignoring physical security—attackers can exploit physical access to devices to extract credentials, modify firmware, or inject malicious data.
- Failing to change default credentials is the single most common security misconfiguration in IoT deployments.
- Overlooking the supply chain—security must be considered from device manufacturing through deployment and decommissioning.

## Revision Tips

1. **Diagram Practice**: Draw and label the three-layer IoT architecture with security controls at each layer—examiners appreciate visual representations.
2. **Case Study Analysis**: Remember the Mirai botnet incident as a canonical example of default credential exploitation.
3. **Protocol Comparison**: Create a table comparing TLS vs. DTLS, MQTT plaintext vs. MQTT over TLS, noting trade-offs for constrained devices.
4. **Scenario-based Thinking**: For any security question, systematically identify assets, threats, vulnerabilities, and countermeasures before proposing solutions.
5. **Terminology**: Ensure precise use of terms—distinguish between authentication (verifying identity) and authorization (granting permissions), and between encryption at rest vs. in transit.