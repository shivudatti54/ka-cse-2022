# Incident Detection and Triage

## Introduction to Incident Detection and Triage

Incident Detection and Triage form the critical first phase of the Incident Handling process within a Security Operations Center (SOC). This phase is about identifying potential security breaches from a sea of data and then systematically prioritizing them for further analysis. Effective detection and triage are paramount; they determine how quickly an organization can respond to a threat, thereby directly impacting the potential damage and cost of a security incident.

This process is not about confirming an incident outright but rather about efficiently filtering out false positives and focusing analyst effort on the most credible and severe threats. It sits at the intersection of technology (SIEM, EDR, network sensors) and human analytical skill.

## Key Concepts in Incident Detection

### 1. What Constitutes an Incident?

An incident is any event that violates an organization's security policies or poses a threat to the confidentiality, integrity, or availability (CIA triad) of its information systems. Common examples include:

- Malware infection
- Unauthorized access or privilege escalation
- Denial-of-Service (DoS) attacks
- Phishing campaigns targeting employees
- Data exfiltration attempts

### 2. Detection Methods

Incidents can be detected through various means, broadly categorized into reactive and proactive methods.

**Reactive Detection:**

- **Alert-Driven:** The most common method. Security tools like SIEM, Intrusion Detection Systems (IDS), Endpoint Detection and Response (EDR), and firewalls generate alerts based on predefined signatures, anomalies, or correlation rules.
  _Example: A SIEM correlation rule triggers an alert when a single user account fails to log in to ten different servers within five minutes._
- **User-Reported:** Incidents reported by employees, customers, or other third parties.
  _Example: An employee receives a phishing email and reports it to the SOC via a dedicated mailbox._

**Proactive Detection:**

- **Threat Hunting:** A hypothesis-driven process where analysts proactively search for threats that have evaded existing automated detection controls. This is covered in more detail in Module 5.
- **Review of Logs and Metrics:** Manually reviewing dashboards, log feeds, or system performance metrics for unusual activity that may not have risen to the level of an alert.

### 3. The Role of the SIEM in Detection

As covered in Module 2, the SIEM is the central nervous system for detection. It aggregates and correlates logs from diverse sources (network devices, servers, applications) to identify malicious patterns.

```
+----------------+    +----------------+    +-----------------------+
|                |    |                |    |                       |
|  Log Sources   |--->|   SIEM Engine  |--->|   Detection &         |
| (FW, EDR, OS)  |    | (Correlation,  |    |   Correlation Rules   |
|                |    |  Normalization)|    |                       |
+----------------+    +----------------+    +-----------------------+
                                                         |
                                                         v
                                                +-------------------+
                                                |                   |
                                                |   Alerts &        |
                                                |   Security Events |
                                                |                   |
                                                +-------------------+
```

## The Triage Process

Triage is the art and science of quickly assessing an alert to determine its validity, severity, and priority. The goal is to answer three fundamental questions:

1.  **Is this a real threat?** (False Positive vs. True Positive)
2.  **How serious is it?** (Severity)
3.  **How urgently should we act?** (Priority)

A structured triage process prevents analyst burnout and ensures critical incidents are handled first.

### Step 1: Initial Alert Assessment

The analyst receives an alert, typically as a ticket in a SOAR or ticketing system. The initial assessment involves:

- **Reviewing Alert Details:** Examining the source IP, destination IP, username, timestamp, and the rule that triggered the alert.
- **Checking Asset Criticality:** Is the target asset a public-facing web server, a database containing PII, or a developer's test machine? Criticality directly impacts severity.
- **Contextual Enrichment:** Using tools to add context. This includes:
  - **IP Reputation:** Checking if the source IP is known to be malicious (e.g., via VirusTotal, AlienVault OTX).
  - **Geolocation:** Is the login attempt originating from a country with no business presence?
  - **User Context:** Is the user a system admin, a regular employee, or a service account? Is the user on vacation?
  - **Threat Intelligence Feeds:** Does the alert signature or indicator of compromise (IoC) match a known threat campaign?

### Step 2: False Positive Identification

A core skill in triage is efficiently identifying false positives. Common causes include:

- **Misconfigured Applications:** Legitimate software behaving unusually.
- **Authorized Activity:** Penetration testing, network scans by IT staff, or automated system processes mistaken for malicious activity.
- **Overly Sensitive Rules:** Correlation rules that need tuning to reduce noise.
- **Benign Software:** Tools like `nmap` or `ping` used by administrators for legitimate purposes.

If an alert is determined to be a false positive, the analyst documents the reason and closes the ticket. This documentation is crucial for tuning detection rules later.

### Step 3: Severity and Priority Assignment

If the alert is deemed a true positive, the analyst must assign a severity and priority level. These are often defined in a formal classification matrix.

**Severity** measures the potential impact of the incident on the organization.
**Priority** determines the order in which the incident will be handled.

| Severity Level | Description                                                                         | Example                                                                    |
| :------------- | :---------------------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **Critical**   | Immediate, material impact on business operations, data loss, or system compromise. | Ransomware encrypting file shares; confirmed data exfiltration.            |
| **High**       | Significant impact likely if not contained. No current material impact.             | Widespread malware infection; successful phishing of a privileged account. |
| **Medium**     | Localized impact on a single system or low-sensitivity data.                        | Isolated malware infection on a non-critical endpoint.                     |
| **Low**        | Minimal impact, often a policy violation without immediate security implications.   | User installing unauthorized but non-malicious software.                   |

Priority is usually a function of Severity and other factors like **scope** (number of systems affected) and **urgency** (is the attack ongoing?).

### Step 4: Initial Documentation and Escalation

The triage phase concludes with initial documentation and handoff. The analyst creates a new incident ticket (or updates the alert ticket) with all gathered information:

- Summary of the event
- Assigned severity/priority
- Initial indicators (IPs, hashes, domains)
- Contextual information gathered
- Recommended next steps

This ticket is then escalated to a Tier 2 or Incident Response analyst for full-scale investigation and containment, as covered in the next part of Module 4.

## Triage Workflow Diagram

The following ASCII flow chart illustrates the logical steps an analyst follows during the triage process.

```
+---------------------+
|                     |
|   Alert Received    |
| (from SIEM/SOAR)    |
|                     |
+----------+----------+
           |
           v
+----------+----------+
|                     |
|  Initial Assessment |   +---------------------------------+
|  & Enrichment       +-->| Check: Source IP, User, Asset, |
|                     |   | Threat Intel, Geolocation      |
+----------+----------+   +---------------------------------+
           |
           v
+----------+----------+
|                     +<---+
|  False Positive?    |    | Yes -> Document & Close Ticket
+----------+----------+    |
           | No            |
           v               |
+----------+----------+    |
|                     |    |
|  Assign Severity    |    |
|  & Priority         |    |
|                     |    |
+----------+----------+    |
           |               |
           v               |
+----------+----------+    |
|                     |    |
|  Document Findings  +----+
|  & Escalate         |
|                     |
+---------------------+
```

## Tools for Effective Triage

- **SIEM:** The primary source of alerts and a tool for log lookup during enrichment.
- **SOAR Platform:** Automates the ticketing, enrichment (via API integrations with threat intel feeds), and escalation processes.
- **Threat Intelligence Platforms:** Provide context on IoCs (e.g., IP reputation, known malware hashes).
- **EDR Tools:** Allow deep inspection of endpoint activity related to an alert (process trees, network connections).
- **Network Analysis Tools:** (e.g., Wireshark, Zeek) for analyzing packet captures related to network-based alerts.

## Exam Tips

- **Understand the Difference:** Be crystal clear on the difference between **Detection** (finding a potential incident) and **Triage** (assessing and prioritizing it). They are distinct but consecutive phases.
- **False Positives are Key:** Expect questions on how to identify and handle false positives. The goal of tuning is to reduce them, not eliminate them entirely (which could lead to false negatives).
- **Severity vs. Priority:** Remember that **Severity** is about impact, and **Priority** is about order of handling. A high-severity incident might not be high priority if it's already been contained automatically.
- **Follow the Process:** For scenario-based questions, mentally walk through the triage steps: receive alert -> enrich with context -> check for false positive -> assign severity/priority -> document/escalate.
- **Know the Tools:** Be prepared to match triage activities (e.g., "checking IP reputation") to the correct tool (e.g., "Threat Intelligence Platform").
