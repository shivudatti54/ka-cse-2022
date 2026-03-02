# Cloud-IoT Security

## Introduction
Cloud-IoT security addresses the unique challenges of securing interconnected IoT devices and cloud infrastructure. As IoT deployments grow exponentially (projected 29 billion devices by 2030), their integration with cloud platforms creates complex attack surfaces. The 2021 Colonial Pipeline ransomware attack demonstrated how IoT vulnerabilities in industrial control systems can cascade into critical infrastructure failures through cloud connections.

This domain combines traditional cybersecurity with edge computing challenges, requiring solutions for device heterogeneity, massive data flows, and real-time processing. Recent research focuses on zero-trust architectures and AI-driven anomaly detection in IoT-cloud ecosystems. For DU students, understanding these paradigms is crucial given India's Smart Cities Mission and growing IoT adoption in healthcare (projected ₹14,207 crore market by 2026).

## Key Concepts
1. **Threat Landscape**: 
   - Device-level attacks (physical tampering, side-channel attacks)
   - Network vulnerabilities (MQTT/CoAP protocol exploits)
   - Cloud-side risks (API hijacking, storage breaches)
   - Advanced Persistent Threats (APTs) targeting IoT-cloud data pipelines

2. **Security Models**:
   - Fog-based authentication (using lightweight cryptographic primitives like ECC)
   - Secure Element (SE) hardware for IoT devices
   - Confidential Computing in cloud (Intel SGX, AMD SEV)

3. **Data Protection**:
   - Homomorphic Encryption for cloud processing
   - Differential Privacy in IoT data aggregation
   - Blockchain-based audit trails (Hyperledger Fabric implementations)

4. **Emerging Paradigms**:
   - Post-quantum cryptography for IoT-cloud systems
   - Federated learning for distributed anomaly detection
   - MITRE ATT&CK for IoT framework analysis

## Examples

**Example 1: Smart Home System Breach**
*Scenario*: A Zigbee-based smart lock system sends encrypted data to AWS IoT Core. Attackers intercept OTA firmware updates.

*Solution*:
1. Implement mutual TLS authentication between devices and cloud
2. Use hash-based signature (SPHINCS+) for firmware verification
3. Deploy AWS IoT Device Defender for continuous monitoring
4. Establish rollback protection using versioned S3 buckets

**Example 2: Healthcare IoT Data Leakage**
*Scenario*: Wearable ECG monitors transmit patient data to Azure. Malicious actors exploit CoAP protocol to access sensitive PHI.

*Solution*:
1. Apply AES-256-GCM encryption at device level
2. Implement OAuth 2.0 Device Flow for Azure AD authentication
3. Use Azure Confidential Computing for data processing
4. Deploy network segmentation with software-defined perimeter

## Exam Tips
1. Focus on NIST SP 800-160 Vol 2 guidelines for IoT security
2. Understand certificate-based authentication in LoRaWAN networks
3. Be prepared to compare TLS 1.3 vs MQTT-SN for constrained devices
4. Study GDPR implications for EU data processed in Indian clouds
5. Analyze case studies like Mirai botnet DDoS attacks
6. Know the role of TPM 2.0 in cloud-attestation workflows
7. Review recent papers on neural cryptography for IoT key exchange

Length: 2800 words, MSc CS (research-oriented) postgraduate level