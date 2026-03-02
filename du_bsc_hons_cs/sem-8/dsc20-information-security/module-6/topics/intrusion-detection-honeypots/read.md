# Intrusion Detection Honeypots

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In the contemporary digital landscape, cybersecurity has become a paramount concern for organizations, governments, and individuals alike. The proliferation of interconnected devices, cloud computing, and digital services has exponentially expanded the attack surface available to malicious actors. According to the 2023 Global Cybersecurity Index, India witnessed a 95% increase in cyberattacks compared to the previous year, highlighting the urgent need for sophisticated defensive mechanisms.

**Intrusion Detection Systems (IDS)** and **Honeypots** represent two of the most critical components in a comprehensive cybersecurity strategy. While traditional security measures like firewalls and antivirus software act as the first line of defense, IDS and honeypots provide deeper visibility into network traffic and attacker behavior.

For students pursuing BSc (Hons) Computer Science under the NEP 2024 UGCF framework at Delhi University, understanding these concepts is essential not only for academic success but also for building a successful career in cybersecurity. This study material provides comprehensive coverage of intrusion detection, honeypots, and related concepts with practical examples and application-oriented questions.

---

## 2. Intrusion Detection Systems (IDS)

### 2.1 Definition and Purpose

An **Intrusion Detection System (IDS)** is a security tool designed to monitor network traffic or system activities for malicious behavior or policy violations. Unlike preventive controls (like firewalls), IDS is primarily a **detective control** that identifies ongoing or completed attacks without actively blocking them (that function is performed by IPS).

The primary objectives of an IDS are:

1. **Detection**: Identify suspicious patterns indicating potential attacks
2. **Alerting**: Notify security administrators of detected threats
3. **Logging**: Record relevant information for forensic analysis
4. **Reporting**: Generate reports for compliance and auditing purposes

### 2.2 IDS vs. IPS: Understanding the Distinction

A common source of confusion in cybersecurity is the distinction between IDS and IPS. While both are related to intrusion detection, their functions differ significantly:

| Feature | IDS (Intrusion Detection System) | IPS (Intrusion Prevention System) |
|---------|----------------------------------|-----------------------------------|
| **Primary Function** | Detects and alerts about threats | Detects, alerts, and actively blocks threats |
| **Placement** | Monitors traffic passively (tap/mirror port) | Inline with traffic flow |
| **Response** | Passive (sends alerts) | Active (drops packets, terminates connections) |
| **Latency** | Minimal (no interference) | Potential for latency |
| **Risk** | False positives don't impact traffic | False positives can block legitimate traffic |
| **Use Case** | Monitoring and forensics | Real-time protection |

**Delhi University Examination Perspective**: Students must understand that while IDS "listens" to traffic like a network sniffer, IPS sits "in-line" and can actively prevent attacks. This distinction frequently appears in exam questions.

### 2.3 Types of Intrusion Detection Systems

#### 2.3.1 Network-Based IDS (NIDS)

A **Network-Based IDS (NIDS)** monitors network traffic across an entire network segment. It analyzes packets flowing through the network for signs of malicious activity.

**Characteristics**:
- Monitors traffic at the network level
- Can analyze traffic between different network segments
- Examples: Snort, Suricata, Bro/Zeek
- Advantages: Can detect distributed attacks, doesn't require installation on individual hosts
- Disadvantages: Cannot decrypt encrypted traffic, may miss attacks targeting specific hosts

#### 2.3.2 Host-Based IDS (HIDS)

A **Host-Based IDS (HIDS)** operates on individual computers or servers, monitoring system calls, file system changes, and system logs.

**Characteristics**:
- Monitors activity on a specific host
- Can detect rootkits, unauthorized file modifications, and privilege escalation
- Examples: OSSEC, Tripwire, AIDE
- Advantages: Can analyze encrypted traffic within the host, detects local attacks
- Disadvantages: Resource-intensive on monitored systems, may be disabled by attackers

### 2.4 Detection Methodologies

#### 2.4.1 Signature-Based Detection

**Signature-based detection** (also known as knowledge-based or pattern matching) identifies known attack patterns by comparing network traffic or system events against a database of predefined signatures (attack patterns).

**How It Works**:
1. Security analysts create or obtain signatures representing known attacks
2. The IDS compares incoming traffic against the signature database
3. When a match is found, an alert is generated

**Advantages**:
- High accuracy for known attacks
- Low false positive rate when signatures are well-crafted
- Easy to understand and maintain

**Disadvantages**:
- Cannot detect zero-day attacks (new, unknown attacks)
- Requires regular signature updates
- Attackers can modify signatures slightly to evade detection (polymorphic attacks)

**Example Snort Rule (Signature-Based)**:
```bash
# Snort rule to detect ICMP ping sweep
alert icmp any any -> $HOME_NET any (msg:"ET SCAN ICMP Ping"; 
itype:8; classtype:attempted-recon; sid:1000001; rev:1;)

# Snort rule to detect potential SSH brute force
alert tcp any any -> $HOME_NET 22 (msg:"Potential SSH Brute Force"; 
flow:to_server,established; content:"SSH-"; nocase; 
threshold:type both, track by_src, count 5, seconds 60; 
classtype:attempted-admin; sid:1000002; rev:1;)
```

#### 2.4.2 Anomaly-Based Detection

**Anomaly-based detection** establishes a baseline of normal system or network behavior and flags significant deviations from this baseline as potential threats.

**How It Works**:
1. The system learns "normal" behavior during a training period
2. Statistical models or machine learning algorithms establish thresholds
3. Deviations from normal behavior trigger alerts

**Advantages**:
- Can detect zero-day attacks and unknown threats
- Doesn't require prior knowledge of specific attack signatures
- Can identify new variants of known attacks

**Disadvantages**:
- Higher false positive rates due to legitimate behavior changes
- Training period may miss periodic legitimate activities
- Resource-intensive compared to signature-based detection
- Sophisticated attackers can slowly modify behavior to evade detection

**Practical Example**:
Consider a web server that typically receives 1000 requests per hour. An anomaly-based IDS might flag the server as suspicious if it suddenly receives 50,000 requests in an hour (indicating a potential DDoS attack) or if it starts receiving unusual types of requests at unusual times.

#### 2.4.3 Stateful Protocol Analysis

**Stateful protocol analysis** examines network traffic by comparing observed events against predetermined profiles of generally accepted definitions of benign protocol activity for each protocol state.

**Example**: In a properly formed HTTP session, the server should respond to a GET request with a 200 OK status. A stateful analyzer would flag responses like "500 Internal Server Error" appearing frequently as potentially suspicious.

---

## 3. Honeypots: Deception Technology

### 3.1 Definition and Concept

A **honeypot** is a decoy system, application, or network designed to attract, detect, and study attacker behavior. Unlike production systems that serve legitimate business purposes, honeypots exist solely to be probed, attacked, and compromised—providing valuable intelligence without risking actual assets.

The fundamental principle behind honeypots is **deception**: by creating attractive but fake targets, security teams can:

1. Detect attackers who evade traditional security controls
2. Gather intelligence about attack techniques and tools
3. Collect evidence for forensic analysis and prosecution
4. Waste attacker time and resources

### 3.2 Types of Honeypots

#### 3.2.1 By Interaction Level

**Low-Interaction Honeypots**:
- Simulate limited services (typically through emulators)
- Limited attack surface, low risk of compromise
- Easy to deploy and maintain
- Examples: Honeyd, Kippo (SSH honeypot), Dionaea
- Use Case: Basic threat detection, collecting malware samples

**Medium-Interaction Honeypots**:
- Provide more realistic responses than low-interaction
- Simulate specific services more convincingly
- Can collect more detailed attack information
- Examples: Cowrie, Glastopf, HoneyTrap

**High-Interaction Honeypots**:
- Real operating systems and applications (not emulated)
- Full attack surface, allows complete attack chains
- Highest information gathering potential
- Higher risk (requires careful isolation)
- Examples: Modern honeynets, physical systems in sandboxes
- Use Case: Advanced threat research, APT detection

#### 3.2.2 By Purpose

**Research Honeypots**:
- Used primarily for academic research and threat intelligence
- Focus on understanding attacker methodologies
- Collect comprehensive data for analysis
- No specific organizational protection mandate

**Production Honeypots**:
- Deployed alongside production systems
- Support defensive operations by detecting attackers
- Typically lower interaction to minimize risk
- Provide early warning of attacks

#### 3.2.3 By Deployment

**Pure Honeypot**:
- Standalone system with no production value
- Entirely deceptive, no legitimate traffic should exist
- Any connection is immediately suspicious

**Malware Collector**:
- Specifically designed to collect malware samples
- May expose vulnerabilities to attract exploits
- Connected to threat intelligence platforms

### 3.3 Practical Example: Deploying a Low-Interaction SSH Honeypot

**Cowrie** is a popular medium to high-interaction SSH and Telnet honeypot designed to log brute force attacks and the shell interaction performed by the attacker.

**Installation Example (Ubuntu)**:
```bash
# Install required dependencies
sudo apt-get install git python3-virtualenv libssl-dev libffi-dev python3-dev

# Clone Cowrie repository
git clone https://github.com/cowrie/cowrie.git
cd cowrie

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Cowrie
pip install --upgrade pip
pip install -r requirements.txt

# Configure Cowrie
cp etc/cowrie.cfg.dist etc/cowrie.cfg

# Edit configuration (example)
# In etc/cowrie.cfg, set hostname and other parameters

# Run Cowrie
bin/cowrie start
```

**Sample Log Output**:
```
2024-01-15T10:23:45.123456+0000 [cowrie.ssh.factory] New connection: 
10.0.0.50 (router.external.example.com) 
[algorithm: ecdh-sha2-nistp256]

2024-01-15T10:23:47.234567+0000 [cowrie.ssh.factory] 
Login attempt [root/123456] succeeded

2024-01-15T10:23:50.345678+0000 [cowrie.core.output] 
cmd: ls -la

2024-01-15T10:24:05.456789+0000 [cowrie.core.output] 
cmd: uname -a
Linux honeypot 5.4.0-generic #1 SMP x86_64 GNU/Linux
```

### 3.4 Honeynets: Networks of Honeypots

A **honeynet** is a network of two or more honeypots designed to simulate a realistic network environment. The concept was pioneered by Project Honeynet and has become a standard for deception technology.

**Key Components of a Honeynet**:
1. **Honeywall**: A gateway that bridges the honeynet to the production network, monitoring all traffic
2. **Multiple Honeypots**: Various systems with different configurations and vulnerabilities
3. **Data Control**: Mechanisms to prevent the honeynet from being used to attack external systems
4. **Data Capture**: Tools to record attacker activities (keystrokes, screenshots, network traffic)

**Honeywall Implementation (Snort Inline)**:
```bash
# Example honeywall configuration with iptables
# Allow inbound to honeypots
iptables -A FORWARD -i eth0 -d 192.168.1.0/24 -j ACCEPT

# Log all traffic for analysis
iptables -A FORWARD -i eth0 -d 192.168.1.0/24 -j LOG 
--log-prefix "HONEYNET_TRAFFIC: "

# Rate limiting to prevent DoS
iptables -A FORWARD -m limit --limit 10/min -j LOG
```

---

## 4. Deployment Strategies

### 4.1 Strategic Placement

Effective honeypot deployment requires careful consideration of network topology:

1. **DMZ Placement**: Deploy honeypots in the demilitarized zone to detect external attackers
2. **Internal Network**: Place honeypots internally to detect insider threats
3. **Data Center**: Position honeypots near critical assets to detect lateral movement
4. **Cloud Environments**: Deploy honeypots in cloud VPCs to monitor cloud-specific threats

### 4.2 Production vs. Research Deployment

| Aspect | Production Deployment | Research Deployment |
|--------|----------------------|---------------------|
| **Objective** | Detect attackers, protect real assets | Study attacker behavior, gather intelligence |
| **Complexity** | Lower to medium | High |
| **Interaction Level** | Low to medium | High |
| **Risk Tolerance** | Very low | Medium to high |
| **Maintenance** | Regular updates | Continuous monitoring |
| **Data Usage** | Operational security | Research, threat intelligence |

---

## 5. Evasion Techniques and Countermeasures

Understanding how attackers evade detection is crucial for building effective security systems.

### 5.1 Common Evasion Techniques

**1. Fragmentation**: Splitting attack payloads across multiple packets to evade signature detection
```bash
# Example: Fragmented TCP packet attack
# Attacker sends TCP segments in unusual order
# to confuse IDS pattern matching
```

**2. Protocol Evasion**: Using non-standard protocols or protocol violations to bypass controls

**3. Encryption**: Encrypting malicious payloads so IDS cannot inspect content

**4. Polymorphic Attacks**: Changing attack signatures while maintaining malicious functionality

**5. Timing Attacks**: Slowing down attacks to evade rate-based detection

### 5.2 Countermeasures

Modern IDS and honeypot systems implement various countermeasures:

1. **Defragmentation**: Reassembling fragmented packets before analysis
2. **Deep Packet Inspection**: Analyzing payload content regardless of encryption (using man-in-the-middle or endpoint detection)
3. **Behavioral Analysis**: Looking for malicious patterns rather than specific signatures
4. **Machine Learning**: Adapting to new attack variations

---

## 6. Practical Example: Snort IDS Configuration

**Snort** is the most widely deployed open-source IDS/IPS globally. Below is a comprehensive example:

### 6.1 Basic Snort Configuration

```bash
# snort.conf - Basic configuration

# Define HOME_NET (the network to protect)
ipvar HOME_NET 192.168.1.0/24

# Define external networks
ipvar EXTERNAL_NET !$HOME_NET

# Configure preprocessors
preprocessor frag3_global: max_frags 65536
preprocessor frag3_engine: policy first detect_anomalies

preprocessor stream5_global: max_tcp 8192, track_tcp yes
preprocessor stream5_tcp: policy first

preprocessor http_inspect: global iis_unicode_map unicode.map 1252
preprocessor http_inspect_server: server default \
    profile all ports { 80 443 8080 }

# Enable output plugins
output unified2: filename snort.log, limit 128

# Include rule files
include /etc/snort/rules/community.rules
include /etc/snort/rules/local.rules
```

### 6.2 Custom Rules for Honeypot Integration

```bash
# Detect connections to known honeypot IPs (threat intelligence)
alert ip $EXTERNAL_NET any -> [192.168.1.100,192.168.1.101] any 
(msg:"HONEPOT Connection Detected"; 
classtype:trojan-activity; sid:1000003; rev:1;)

# Detect port scans from honeypot connections
alert tcp $HOME_NET any -> $EXTERNAL_NET any 
(msg:"Outbound connection from honeypot IP"; 
flow:from_host,established; 
classtype:attempted-recon; sid:1000004; rev:1;)

# Detect brute force attempts
alert tcp $EXTERNAL_NET any -> $HOME_NET 22 
(msg:"SSH Brute Force Attempt"; 
flow:to_server,established; 
content:"SSH-"; nocase; 
threshold:type threshold, track by_src, count 5, seconds 60; 
classtype:attempted-admin; sid:1000005; rev:1;)
```

---

## 7. Assessment Questions

### 7.1 Multiple Choice Questions (Advanced Level)

1. **Scenario**: An organization deploys a honeypot that emulates a vulnerable Windows Server 2019 with SMB enabled. After one week, logs show multiple failed authentication attempts followed by successful login using the credentials "Administrator:Password123". The attacker then executed PowerShell commands to enumerate network resources.

   **Question**: What type of honeypot was MOST likely deployed, and what is the PRIMARY concern with this deployment?
   
   a) Low-interaction honeypot; risk of attacker pivot to production systems
   b) High-interaction honeypot; risk of attacker pivot to production systems
   c) Medium-interaction honeypot; risk of data exfiltration
   d) Research honeypot; high maintenance overhead

2. **Question**: Which of the following statements about IDS and IPS is CORRECT?

   a) IDS can drop malicious packets while IPS can only alert
   b) IDS requires inline placement while IPS uses passive monitoring
   c) IDS generates alerts without blocking traffic
   d) IPS cannot be deployed in NAT environments

3. **Question**: An anomaly-based IDS has been deployed in your network. During the training phase, a legitimate batch job runs every night at 2 AM. After deployment, legitimate batch jobs generate alerts. What is the MOST appropriate solution?

   a) Disable the anomaly-based detection
   b) Include the batch job in the training data and retrain
   c) Switch entirely to signature-based detection
   d) Adjust the threshold to only alert on critical anomalies

### 7.2 Scenario-Based Application Questions

**Question 1 (15 marks)**

XYZ University manages a student network with approximately 5,000 devices. The security team has noticed an increase in port scanning activities originating from within the network. The current firewall and antivirus solutions have not been able to identify the source.

As a security consultant, propose a deployment strategy that includes:
- Placement of honeypots in the network
- Selection of appropriate honeypot types
- Integration with existing security infrastructure
- Legal considerations for deploying honeypots on campus

**Question 2 (10 marks)**

Given the following Snort rule:

```bash
alert tcp $EXTERNAL_NET any -> $HOME_NET 22 
(msg:"SSH Brute Force"; flow:to_server,established; 
content:"SSH-"; nocase; threshold:type both, track by_src, 
count 5, seconds 30; classtype:attempted-admin; sid:1000001;)
```

Explain:
- What attack this rule detects
- How the threshold option works
- One way an attacker could evade this detection
- One limitation of this signature-based approach

**Question 3 (10 marks)**

Compare and contrast signature-based and anomaly-based intrusion detection. In a financial services organization handling sensitive customer data, recommend which approach (or combination) would be more effective and justify your recommendation.

---

## 8. Key Takeaways

1. **IDS vs IPS**: IDS detects and alerts but doesn't block traffic (passive monitoring), while IPS actively blocks threats (inline deployment). Understanding this distinction is fundamental to network security architecture.

2. **Detection Methods**: Signature-based detection is effective for known threats but cannot detect zero-day attacks. Anomaly-based detection can identify unknown threats but may generate more false positives.

3. **Honeypots are Deception Technology**: They serve as attractive decoys to detect, deflect, and study attackers. The level of interaction (low, medium, high) determines both the information gathered and the risk involved.

4. **Honeynets Extend Honeypot Value**: By deploying multiple interconnected honeypots, organizations can create realistic environments that encourage attackers to reveal more sophisticated techniques.

5. **Deployment Strategy Matters**: Strategic placement of honeypots (DMZ, internal network, cloud) determines what threats they can detect. Production honeypots prioritize security, while research honeypots prioritize information gathering.

6. **Evasion is Real**: Sophisticated attackers use fragmentation, encryption, and timing variations to evade detection. Modern security solutions must combine multiple detection methodologies.

7. **Practical Tools**: Snort remains the industry-standard open-source IDS, with extensive rule-writing capabilities. Understanding Snort rules is essential for both exam success and practical security work.

8. **Legal and Ethical Considerations**: Deploying honeypots involves legal implications, especially regarding entrapment and data collection. Organizations must have clear policies and, in some jurisdictions, may need explicit authorization.

---

*Study Material prepared for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*
*Topic: Intrusion Detection Honeypots — Information Security*