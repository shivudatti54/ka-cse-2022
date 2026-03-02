# Wireless Attack Techniques

## Introduction to Wireless Vulnerabilities

Wireless networks have become ubiquitous in modern computing environments, but their convenience comes with significant security challenges. Unlike wired networks where physical access control provides a layer of protection, wireless signals propagate through the air, making them accessible to anyone within range. This chapter explores the various attack techniques that target wireless networks, particularly Wi-Fi networks, and the underlying vulnerabilities that make these attacks possible.

Wireless attacks can be broadly categorized into passive attacks (eavesdropping without altering communications) and active attacks (interacting with or modifying network communications). Understanding these techniques is crucial for implementing effective wireless security measures.

## Wireless Reconnaissance Techniques

### War Driving and War Flying
Attackers often begin with reconnaissance to identify potential targets. War driving involves driving around with a wireless-enabled device to detect and map wireless networks. War flying uses drones equipped with wireless capabilities for the same purpose.

```
+----------------+      +----------------+      +-----------------+
| Attacker with  |      | Wireless       |      | Mapping         |
| Laptop/Device  |----->| Network        |----->| Software        |
| + GPS          | Scan | Discovery      | Log  | (Kismet, etc.)  |
+----------------+      +----------------+      +-----------------+
```

Tools commonly used for wireless reconnaissance include:
- **Kismet**: A wireless network detector, sniffer, and intrusion detection system
- **NetStumbler**: A Windows-based tool for detecting wireless networks
- **inSSIDer**: A wireless network scanner for Windows and macOS
- **Wireshark**: With wireless capabilities for packet capture and analysis

### Network Enumeration
Once networks are discovered, attackers enumerate details about them:
- SSID (Service Set Identifier)
- BSSID (Basic Service Set Identifier/MAC address)
- Signal strength and channel information
- Security protocols in use (Open, WEP, WPA, WPA2, WPA3)
- Connected clients

## Attacks Against Wireless Authentication

### Evil Twin Attack (Rogue Access Point)
An evil twin attack involves setting up a malicious access point with the same SSID as a legitimate network. When users connect to this rogue AP, the attacker can intercept all communications.

```
+---------------+      +----------------+      +-----------------+
| Legitimate    |      | Rogue AP with  |      | User Device     |
| Access Point  |      | Same SSID      |<---->| (connects to    |
| (SSID: CorpNet)|      | (SSID: CorpNet)|      | stronger signal)|
+---------------+      +----------------+      +-----------------+
      ^                                               |
      |                                               |
      +-----------------------------------------------+
                  Legitimate connection attempt
```

### KRACK Attack (Key Reinstallation Attack)
KRACK targets the four-way handshake process in WPA2, exploiting vulnerabilities in the protocol that allow attackers to force nonce reuse, enabling packet decryption and injection.

The four-way handshake process:
1. AP → Client: ANonce (random number)
2. Client → AP: SNonce + MIC (Message Integrity Code)
3. AP → Client: GTK + MIC
4. Client → AP: ACK

KRACK works by blocking the final ACK message, causing the client to reinstall the same encryption key, which can be exploited to decrypt packets.

## Attacks Against Wireless Encryption

### WEP Cracking
Wired Equivalent Privacy (WEP) is fundamentally flawed and easily crackable due to weaknesses in the RC4 encryption algorithm and initialization vector (IV) implementation.

**Weaknesses in WEP:**
- Short 24-bit IVs that eventually repeat
- Weak key scheduling in RC4
- Integrity check value (ICV) based on CRC-32, which is cryptographically insecure
- Authentication challenges that can be captured and replayed

**Tools for WEP cracking:**
- Aircrack-ng suite
- Wifite
- Fern WiFi Cracker

The process typically involves:
1. Monitoring network traffic to capture IVs
2. Using statistical attacks to recover the key
3. Sometimes using packet injection to accelerate IV collection

### WPA/WPA2 PSK Cracking
While more secure than WEP, WPA/WPA2 with pre-shared keys (PSK) is vulnerable to offline dictionary attacks against the captured four-way handshake.

```
+----------------+      +----------------+      +-----------------+
| Capture Four-  |      | Use Dictionary |      | Success if      |
| Way Handshake  |----->| Attack with    |----->| Password is in  |
| with Airodump  |      | Hashcat or     |      | Wordlist        |
+----------------+      +----------------+      +-----------------+
```

The attack process:
1. Capture the four-way handshake (can force deauthentication to trigger reauthentication)
2. Use a tool like Aircrack-ng or Hashcat to perform a dictionary attack
3. Success depends on password complexity and the quality of the wordlist

## Denial of Service Attacks

### Deauthentication Attacks
Deauthentication attacks send spoofed deauth frames to disconnect clients from an access point. Since 802.11 management frames are unencrypted and unauthenticated, this attack is simple to execute.

```
+---------------+      +-----------------+
| Attacker      |      | Client          |
| sends spoofed |----->| receives        |
| deauth frame  |      | deauth frame    |
| from AP MAC   |      | and disconnects |
+---------------+      +-----------------+
```

**Tools for deauthentication:**
- Aireplay-ng (`aireplay-ng --deauth`)
- MDK3
- MDK4

### Beacon Flood Attack
This attack floods the area with fake access point beacons, making it difficult for legitimate clients to find and connect to real networks. It can also be used to hide rogue access points among numerous fake ones.

### RF Jamming
Physical layer attacks using specialized equipment to transmit noise on wireless frequencies, effectively blocking all communications on affected channels.

## Advanced Attack Techniques

### Man-in-the-Middle Attacks
Once an attacker has positioned themselves between a client and the network (through evil twin or other means), they can intercept and potentially modify communications.

```
+----------+      +-------------+      +----------+
| Client   |      | Attacker    |      | Legit AP |
| Traffic  |----->| intercepts  |----->| or       |
|          |      | and relays  |      | Internet |
+----------+      +-------------+      +----------+
```

Tools for MITM attacks:
- Ettercap
- SSLstrip (for HTTPS downgrading)
- BetterCAP

### Wi-Fi Pineapple Attacks
The Wi-Fi Pineapple is a specialized device created by Hak5 that automates many wireless attacks, particularly those involving rogue access points and client-side attacks.

### WPS Attacks
Wi-Fi Protected Setup (WPS) was designed to simplify network setup but contains serious vulnerabilities. The PIN authentication method can be brute-forced because:
- The 8-digit PIN is effectively only 11,000 possibilities due to checksum
- The AP reveals whether the first 4 digits and second 4 digits are correct separately

**Tools for WPS attacks:**
- Reaver
- Bully
- Wifite (automated)

## Enterprise Network Attacks

### EAP Downgrade Attacks
Attacks against enterprise networks that use 802.1X/EAP authentication may attempt to downgrade the authentication method to weaker versions.

### RADIUS Attacks
Targeting the RADIUS server itself or attempting to intercept communications between the AP and RADIUS server.

## Comparison of Wireless Attack Techniques

| Attack Type | Target Protocol | Difficulty | Impact | Tools |
|-------------|-----------------|------------|--------|-------|
| WEP Cracking | WEP | Easy | High | Aircrack-ng, Wifite |
| WPA PSK Cracking | WPA/WPA2-PSK | Medium | High | Hashcat, Aircrack-ng |
| KRACK | WPA2 | Medium | Medium | Custom scripts |
| Evil Twin | Any | Medium | High | Airbase-ng, Hostapd |
| Deauthentication | Any | Easy | Medium | Aireplay-ng, MDK3 |
| WPS PIN Attack | WPS | Easy | High | Reaver, Bully |

## Protection and Detection Strategies

### Defensive Measures
- Use WPA3 whenever possible
- For WPA2, use strong passwords (15+ characters, complexity)
- Disable WPS on all access points
- Use enterprise authentication (802.1X) instead of PSK
- Implement wireless intrusion detection/prevention systems (WIDS/WIPS)
- Regularly monitor for rogue access points
- Use certificate-based authentication where possible

### Detection Techniques
- Monitor for deauthentication floods
- Detect multiple APs with the same SSID/BSSID
- Identify unusual signal patterns
- Use RF fingerprinting to identify authorized devices
- Monitor for authentication anomalies

## Exam Tips

1. **Focus on protocol weaknesses**: Understand why WEP is broken and the specific vulnerabilities in WPA2 that KRACK exploits.
2. **Know the tools**: Be familiar with the main wireless security tools (Aircrack-ng suite, Wifite, Reaver) and what each is used for.
3. **Understand the process**: For common attacks like WPA cracking, know the step-by-step process from reconnaissance to key recovery.
4. **Differentiate attack types**: Be able to distinguish between passive attacks (eavesdropping) and active attacks (injection, deauthentication).
5. **Remember defense strategies**: For each attack technique, know the appropriate defensive measures.
6. **Practice with scenarios**: Be prepared to analyze attack scenarios and identify what type of attack is occurring and how to defend against it.