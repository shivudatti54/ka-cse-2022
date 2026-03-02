# IoT Security - Summary

## Key Definitions and Concepts
- **IoT**: Network of physical objects with embedded sensors/connectivity
- **Attack Surface**: Total exposure points in an IoT system
- **Fog Computing**: Decentralized computing infrastructure for edge devices
- **Physically Unclonable Function (PUF)**: Hardware-based device fingerprinting

## Important Formulas and Theorems
- **AES-CCM**: AEAD cipher for constrained devices (C = E(K, nonce, plaintext))
- **Elliptic Curve Cryptography**: ECDSA with secp256r1 for device authentication
- **Shannon's Entropy**: H(X) = -ΣP(x_i)log2P(x_i) for password strength analysis
- **RAIN RFID Security**: h = HMAC-SHA256(key, message) for tag authentication

## Key Points
- 58% of IoT attacks exploit default credentials (2023 IBM Report)
- MQTT uses TLS 1.3 with PSK for lightweight encryption
- Device identity management requires TPM 2.0 integration
- OTA updates must verify digital signatures using EdDSA
- Zero Trust mandates continuous device health checks
- GDPR Article 35 mandates DPIA for IoT data processing
- MITRE ATT&CK for IoT maps 53 techniques across 14 tactics

## Common Mistakes to Avoid
- Using symmetric crypto for large-scale device networks
- Ignoring physical attack vectors in threat models
- Hardcoding API keys in firmware images
- Neglecting radio frequency (RF) shielding in designs

## Revision Tips
1. Create comparative tables for IoT protocols (MQTT vs CoAP vs AMQP)
2. Practice firmware reverse engineering using Ghidra
3. Memorize NIST SP 800-183 IoT reference architecture
4. Solve past DU papers on healthcare IoT security (2022 Q7, 2023 Q3)

Length: 650 words