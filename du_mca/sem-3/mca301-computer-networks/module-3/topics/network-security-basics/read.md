# Network Security Basics

## Introduction
Network security forms the cornerstone of modern digital infrastructure protection. With increasing cyber threats targeting organizations (15% YoY growth in India according to CERT-In 2023), understanding security fundamentals is critical for MCA graduates. The primary objectives of network security - Confidentiality, Integrity, and Availability (CIA triad) - ensure authorized access, data accuracy, and system reliability.

Modern networks face sophisticated threats like ransomware (WannaCry impacted 200,000+ systems globally), phishing (74% of Indian organizations targeted in 2022), and DDoS attacks. The financial sector alone reported 13% of total cyber incidents in India (2023 RBI report). This makes security protocols like encryption, firewalls, and intrusion detection systems essential components of network architecture.

## Key Concepts
1. **Cryptography**: 
   - Symmetric Encryption (AES-256): Single key for encryption/decryption
   - Asymmetric Encryption (RSA 2048): Public/private key pairs
   - Digital Signatures: SHA-256 with RSA for message authentication

2. **Access Control**:
   - AAA Framework (Authentication, Authorization, Accounting)
   - RADIUS/TACACS+ for network access management
   - Role-Based Access Control (RBAC)

3. **Network Defense Mechanisms**:
   - Firewalls: Stateful inspection vs Packet filtering
   - IDS/IPS: Signature-based vs Anomaly-based detection
   - VPN Technologies: IPsec (Transport/Tunnel modes), SSL/TLS

4. **Threat Mitigation**:
   - DDoS Protection: Rate limiting, Anycast DNS
   - Malware Defense: Sandboxing, Heuristic analysis
   - Social Engineering Prevention: SPF/DKIM/DMARC for email security

## Examples

**1. AES-256 Encryption Process**
```
Plaintext: "DU_MCA_2024"
Key: 256-bit randomly generated key

Steps:
1. Key Expansion: Create 14 round keys from original
2. Initial Round: AddRoundKey
3. 14 Main Rounds:
   - SubBytes (S-box substitution)
   - ShiftRows 
   - MixColumns
   - AddRoundKey
4. Final Round (without MixColumns)
Ciphertext: 1a3f...c9b2 (128-bit block)
```

**2. Firewall Rule Implementation**
```bash
# Allow HTTPS traffic from specific IP range
iptables -A INPUT -p tcp --dport 443 -s 192.168.1.0/24 -j ACCEPT

# Block SSH brute-force attacks
iptables -A INPUT -p tcp --dport 22 -m recent --name SSH --set
iptables -A INPUT -p tcp --dport 22 -m recent --name SSH --update --seconds 60 --hitcount 5 -j DROP
```

**3. VPN Setup with OpenVPN**
```config
# Server Configuration
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh2048.pem
server 10.8.0.0 255.255.255.0
push "redirect-gateway def1 bypass-dhcp"
tls-auth ta.key 0
cipher AES-256-CBC
```

## Exam Tips
1. Always mention CIA triad when asked about security objectives
2. Differentiate clearly between IDS (detection) and IPS (prevention)
3. For encryption questions, specify key sizes (AES-256 vs RSA-2048)
4. Remember firewall types: Packet Filtering (Layer 3), Stateful (Layer 4), Application (Layer 7)
5. In case studies, link threats to mitigation techniques (e.g., DDoS → Cloudflare)
6. Understand PKI hierarchy: Root CA → Intermediate CA → End Entity
7. Use OSI model references: SSL/TLS at Layer 5, IPsec at Layer 3