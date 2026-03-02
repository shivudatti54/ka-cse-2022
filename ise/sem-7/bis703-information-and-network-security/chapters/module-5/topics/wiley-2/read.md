Of course. Here is a comprehensive educational note on the requested topic, formatted for  engineering students.

# Module 5: Intrusion Detection and Prevention Systems (IDPS)

**Subject:** Information and Network Security
**Module:** Module 5 (10 hours)
**Topic:** Wiley 2 (Intrusion Detection Systems)

---

## 1. Introduction

In an ideal world, network security measures like firewalls and encryption would be sufficient to stop all attacks. However, the reality is that determined attackers can bypass these defenses. An **Intrusion Detection System (IDS)** and its proactive counterpart, an **Intrusion Prevention System (IPS)**, are essential security mechanisms that act as a "burglar alarm" and "security guard" for a network. They monitor system and network activities for malicious actions or policy violations, providing a critical layer of defense-in-depth.

## 2. Core Concepts Explained

### What is an Intrusion?
An intrusion is any unauthorized activity that can compromise the confidentiality, integrity, or availability (CIA triad) of a computer system or network. This includes activities like malware infections, unauthorized access attempts, and denial-of-service attacks.

### Intrusion Detection System (IDS)
An IDS is a monitoring system that detects suspicious activity and generates alerts. It is primarily a **passive** system; it watches, analyzes, and reports but does not take direct action to stop the threat.

**Key Characteristics:**
*   **Passive Monitoring:** Deployed out-of-band, analyzing copies of network traffic.
*   **Alert-Centric:** Notifies security administrators of potential incidents.
*   **No Impact on Traffic:** Since it's passive, it does not introduce latency or block packets.

### Intrusion Prevention System (IPS)
An IPS builds upon IDS functionality but is an **active** system. It is placed in-line (directly in the network path) and can automatically take action to block or prevent detected threats.

**Key Characteristics:**
*   **Active Prevention:** Deployed in-line, analyzing real-time traffic.
*   **Action-Centric:** Can drop malicious packets, reset connections, or block source IP addresses.
*   **Potential for Impact:** Being in-line, a poorly configured IPS can block legitimate traffic (false positive) and affect network performance.

## 3. Detection Methodologies

IDS/IPS can be classified based on how they detect intrusions:

### 1. Signature-Based Detection (Misuse Detection)
This method relies on a database of known attack patterns or signatures, much like an antivirus program.

*   **How it works:** It compares network packets or system logs against a database of predefined signatures.
*   **Example Signature:** `alert tcp any any -> 192.168.1.10 80 (content:"/etc/passwd"; msg:"Apache root access attempt";)`
    *   This Snort rule alerts on any TCP traffic destined for the web server on port 80 containing the string "/etc/passwd".
*   **Advantage:** Very effective at detecting known attacks with low false positives.
*   **Disadvantage:** Cannot detect zero-day attacks or novel threats for which a signature does not yet exist.

### 2. Anomaly-Based Detection
This method uses a baseline of "normal" system or network behavior. Any activity that significantly deviates from this baseline is flagged as a potential intrusion.

*   **How it works:** The system learns normal behavior (e.g., typical bandwidth usage, login times, protocols used) during a training period. Subsequent activities are compared against this profile.
*   **Example:** A user who typically logs in from Bangalore between 9 AM and 5 PM suddenly attempts to log in at 3 AM from a foreign country. This would be flagged as an anomaly.
*   **Advantage:** Can detect previously unknown attacks (zero-day) and insider threats.
*   **Disadvantage:** Higher rate of false positives, as normal behavior can sometimes be unusual (e.g., a user downloading a large legal file).

### 3. Stateful Protocol Analysis
This advanced method understands the state of a protocol conversation (like TCP handshakes) and can identify sequences of commands that are not permitted by the protocol standard, even if each individual packet looks normal.

## 4. Types of IDPS Based on Deployment

*   **Network-Based IDPS (NIDS/NIPS):** Monitors traffic on entire network segments. It is typically deployed at strategic points like network borders. (e.g., Snort, Suricata).
*   **Host-Based IDPS (HIDS/HIPS):** Installed on individual hosts (servers, workstations). It monitors activities on that specific host, such as file access, system calls, and logs. (e.g., OSSEC, Wazuh).
*   **Wireless IDPS (WIDS/WIPS):** Specialized in monitoring wireless network traffic for rogue access points and malicious behavior.

## 5. Key Points and Summary

| Aspect | Intrusion Detection System (IDS) | Intrusion Prevention System (IPS) |
| :--- | :--- | :--- |
| **Primary Function** | Monitoring and Alerting | **Prevention** and Blocking |
| **Deployment** | Out-of-band (Passive) | **In-line** (Active) |
| **Impact on Traffic** | None | Can introduce latency; can block traffic |
| **Response** | Generates alerts for admin review | **Automatically** takes action (drop, reset, block) |

**Summary:**
*   **IDS** is a detective control. It is best for monitoring and forensic analysis without risking disruption to legitimate business traffic.
*   **IPS** is a preventative control. It is essential for automatically stopping known threats but must be carefully tuned to avoid blocking legitimate users (false positives).
*   Both systems use **signature-based** (for known threats) and **anomaly-based** (for unknown threats) detection methods.
*   A modern security operations center (SOC) will deploy a combination of **NIDS/NIPS** for network-wide coverage and **HIDS/HIPS** for critical endpoint protection, creating a robust, layered defense strategy.