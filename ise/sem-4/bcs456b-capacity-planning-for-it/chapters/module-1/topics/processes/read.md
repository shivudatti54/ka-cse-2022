# SOC Processes and Workflows

## Introduction to SOC Processes

A Security Operations Center (SOC) is not merely a collection of tools and personnel; it is a process-driven entity. The effectiveness of a SOC is determined by the maturity, efficiency, and consistency of its processes and workflows. These structured procedures ensure that security events are handled predictably, effectively, and in a repeatable manner, transforming raw data and potential chaos into managed, mitigated risk.

Processes define _what_ needs to be done, while workflows define _how_ and _by whom_ it is done. They are the central nervous system of the SOC, connecting its various components—people, technology, and intelligence—into a cohesive, responsive unit.

## Core SOC Processes

The core processes of a SOC can be categorized into a continuous cycle, often aligned with the NIST Incident Response Lifecycle (NIST SP 800-61). The key processes are:

### 1. Monitoring and Alerting

This is the 24/7 foundational process where the SOC maintains vigilance over the organization's networks and systems.

- **Purpose:** To collect, aggregate, and analyze log data from various sources (e.g., firewalls, IDS/IPS, endpoints, servers) to identify potential security incidents.
- **Key Activities:**
  - **Log Collection:** Ingesting logs from all critical assets into the SIEM.
  - **Event Correlation:** Using SIEM rules to connect related events from different sources that individually might be benign but together indicate malicious activity.
  - **Alert Generation:** Creating alerts based on correlation rules, threat intelligence feeds, and anomaly detection.
- **Workflow:** Automated and continuous. Analysts monitor dashboards and alert queues.

```
+---------------+    Raw Logs    +-----------+    Correlated    +-------------+
| Log Sources   |--------------->|   SIEM    |---------------->|   Alerts    |
| (Firewalls,   |    (e.g., Syslog)| (Correlation |    Events     |   Queue     |
| Servers, etc.)|                 |  Engine)   |                 |             |
+---------------+                 +-----------+                 +-------------+
```

### 2. Triage and Analysis

Once an alert is generated, it must be quickly assessed to determine its validity and criticality.

- **Purpose:** To filter out false positives and prioritize genuine incidents for further investigation.
- **Key Activities:**
  - **Initial Triage:** A Tier 1 analyst reviews the alert's details (source IP, destination IP, type of activity, timestamp) against known baselines and threat intelligence (e.g., Is the IP known to be malicious?).
  - **Priority Assignment:** Incidents are categorized based on impact and urgency. A common model is:
    | Priority Level | Impact | Urgency | Example |
    | :--- | :--- | :--- | :--- |
    | **P1/Critical** | Severe damage to systems/data | Immediate response | Ransomware execution, Active data exfiltration |
    | **P2/High** | Significant impact | Response within hours | Malware infection, Unauthorized access |
    | **P3/Medium** | Limited impact | Response within days | Policy violation, Scanning from unknown source |
    | **P4/Low** | Minimal to no impact | Response as resources allow | False positive, Benign anomaly |
  - **Initial Investigation:** Gathering additional context (e.g., enriching IPs with threat feeds, checking user account status).

### 3. Incident Response and Escalation

This process involves the coordinated effort to contain, eradicate, and recover from a confirmed security incident.

- **Purpose:** To mitigate the impact of an incident and restore normal operations securely.
- **Key Activities:**
  - **Containment:** Taking short-term and long-term actions to limit damage. This could involve isolating a network segment, blocking a malicious IP at the firewall, or disabling a user account.
  - **Eradication:** Removing the root cause of the incident, such as deleting malware, patching a vulnerability, or removing a threat actor's access.
  - **Recovery:** Restoring affected systems and services to operational status, ensuring they are no longer compromised.
  - **Escalation:** If the incident is complex or severe (P1/P2), it is escalated from Tier 1 to Tier 2 or Tier 3 analysts and often involves notifying other teams like IT, Legal, and Communications.

```
+-------------+    Confirmed    +-----------------+    Escalation    +---------------+
| Alert Queue |---------------->| Triage & Analysis|---------------->| Tier 2 / Tier 3|
|             |    Incident     |  (Tier 1)       |    (if needed)   |  Analysts     |
+-------------+                 +-----------------+                  +---------------+
                                                                           |
                                                                           | Contain/Eradicate/Recover
                                                                           v
                                                                   +-----------------+
                                                                   |   Resolution    |
                                                                   +-----------------+
```

### 4. Threat Hunting

A proactive process that moves beyond reacting to alerts.

- **Purpose:** To proactively and iteratively search through networks and datasets to detect advanced threats that evade existing automated detection tools.
- **Key Activities:**
  - **Hypothesis Formation:** Developing ideas about adversary TTPs (Tactics, Techniques, and Procedures) based on threat intelligence, vulnerability data, or internal analytics.
  - **Investigation:** Using advanced tools (EDR, network analysis) to search for evidence supporting or refuting the hypothesis.
  - **Resolution:** If a threat is found, it initiates the incident response process. If not, the findings are used to refine baselines and improve detection capabilities.

### 5. Reporting and Feedback

The闭环 (closed-loop) process that ensures continuous improvement.

- **Purpose:** To document actions taken, communicate status to stakeholders, and refine SOC processes based on lessons learned.
- **Key Activities:**
  - **Incident Documentation:** Recording all steps taken during an incident in a ticketing system (e.g., Jira, ServiceNow) for audit trails and knowledge sharing.
  - **Post-Incident Review (PIR):** Conducting a meeting after major incidents to discuss what went well, what didn't, and how to improve. This is also known as a "lessons learned" meeting.
  - **Metrics Reporting:** Generating reports on SOC performance (e.g., Mean Time to Detect (MTTD), Mean Time to Respond (MTTR), number of incidents handled) for management.

## Key SOC Workflows

Workflows are the detailed, step-by-step playbooks that analysts follow for specific scenarios.

### 1. Alert Triage Workflow

```
1.  Alert appears in SOC queue.
2.  Analyst opens a new incident ticket.
3.  Analyst reviews alert details (SIEM, raw logs).
4.  Checks threat intelligence for IoC context.
5.  Is the alert a true positive?
    -> No: Classify as false positive, document reason, close ticket.
    -> Yes: Proceed to step 6.
6.  Determine impact and assign priority (P1-P4).
7.  Perform initial containment if possible (e.g., block IP).
8.  If within skillset, investigate further.
9.  If not, escalate to higher tier with detailed notes.
```

### 2. Phishing Email Investigation Workflow

```
1.  Receive reported phishing email from user.
2.  Analyze email headers to identify source and authenticity.
3.  Examine links and attachments in a sandboxed environment.
4.  Check sender and URL reputation with threat intelligence.
5.  If malicious, request block of sender and URLs via email security tool.
6.  Search SIEM/email logs for other recipients of the same email.
7.  Notify all recipients and provide guidance.
8.  Document actions and update threat intelligence feeds.
```

### 3. Malware Infection Workflow

```
1.  Confirm malware alert from EDR/AV.
2.  Isolate the infected host from the network.
3.  Determine malware type and capabilities.
4.  Identify initial infection vector (e.g., phishing, exploit).
5.  Scope the incident: Identify other potentially infected hosts.
6.  Eradicate malware (delete files, kill processes).
7.  Patch the vulnerability that allowed infection.
8.  Return host to service after clean-up.
9.  Conduct PIR to prevent recurrence.
```

## Integration with Other Teams

SOC workflows do not exist in a vacuum. Effective SOCs are integrated with other organizational units:

- **IT Operations:** For implementing containment measures (e.g., isolating a server) and recovery.
- **Network Team:** For implementing network-based blocks and providing specialized netflow data.
- **Legal & Compliance:** For guidance on data breach notification laws and evidence handling.
- **Public Relations/Communications:** For managing external messaging in the event of a public incident.

## Exam Tips

- **Memorize the NIST IR Lifecycle Phases:** Preparation, Detection & Analysis, Containment Eradication & Recovery, and Post-Incident Activity. Be able to map SOC processes to these phases.
- **Understand Triage:** The goal of triage is **prioritization**, not full resolution. Know how to use impact vs. urgency to assign priority levels.
- **Workflows vs. Processes:** A **process** is the high-level objective (e.g., "handle an incident"). A **workflow** is the detailed, step-by-step procedure for a specific scenario (e.g., "phishing workflow").
- **Know the Key Metrics:** MTTD and MTTR are critical for measuring SOC process efficiency. Be prepared to define them.
- **Think Proactively vs. Reactively:** Threat hunting is the primary _proactive_ process. All others are primarily _reactive_ (responding to alerts or events).
