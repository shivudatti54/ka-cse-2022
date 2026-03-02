# Types of Penetration Tests

## Introduction
Penetration testing (pentesting) is a simulated cyberattack against a computer system, network, or web application to identify security vulnerabilities that could be exploited by malicious actors. A critical first step in any penetration testing engagement is understanding and selecting the appropriate type of test. The choice depends on the client's goals, the scope of the engagement, the rules of engagement, and the specific assets being tested. This module explores the various classifications of penetration tests, providing a foundational understanding essential for any cybersecurity professional.

## Classification by Knowledge Level
One of the primary ways to categorize penetration tests is based on the amount of information provided to the testing team before the engagement begins.

### 1. Black-Box Testing
In a black-box test, the penetration tester is given no prior knowledge of the internal structure, design, or implementation of the target system. The tester approaches the target just as an external attacker would, with only publicly available information.

**Characteristics:**
*   **Knowledge Level:** Zero internal knowledge.
*   **Simulates:** An external, unprivileged attacker.
*   **Time/Cost:** Often more time-consuming and expensive due to the required reconnaissance phase.
*   **Focus:** Overall external security posture, security processes, and incident response.

```
+---------------------+      +---------------------+      +---------------------+
|   Tester with no    |----->|   Reconnaissance    |----->|   Exploitation &    |
|  internal knowledge |      |   (OSINT, Scanning)  |      |     Reporting       |
+---------------------+      +---------------------+      +---------------------+
```

**Example:** A tester is hired to assess the security of `example.com`. They are only given the company name and must discover all web assets, network ranges, and potential entry points from scratch.

### 2. White-Box Testing
A white-box test (also known as clear-box or structural testing) is the polar opposite. The tester is provided with complete knowledge of the target environment, including network diagrams, source code, credentials, and system architecture.

**Characteristics:**
*   **Knowledge Level:** Full internal knowledge.
*   **Simulates:** An internal threat actor or a highly privileged external attacker who has already breached the perimeter.
*   **Time/Cost:** More efficient and less costly as it eliminates the need for extensive reconnaissance.
*   **Focus:** Identifying deep, complex vulnerabilities that are hard to find without internal knowledge.

```
+---------------------+      +---------------------+      +---------------------+
| Tester with full    |----->|   Code Review &     |----->|  Targeted Exploit   |
| internal knowledge  |      |   Architecture      |      |   Development &     |
| (Diagrams, Code)    |      |     Analysis        |      |     Reporting       |
+---------------------+      +---------------------+      +---------------------+
```

**Example:** A developer provides a tester with the full source code of a web application and credentials for a test environment to find logical flaws and business logic vulnerabilities.

### 3. Grey-Box Testing
Grey-box testing strikes a balance between black-box and white-box. Testers are provided with partial knowledge of the target, such as low-privilege user credentials or a basic network diagram.

**Characteristics:**
*   **Knowledge Level:** Limited internal knowledge.
*   **Simulates:** An attacker who has gained a foothold inside the network (e.g., through a phishing attack) or an insider threat with standard user privileges.
*   **Time/Cost:** Offers a good balance of realism and efficiency.
*   **Focus:** Privilege escalation, lateral movement, and the security of internal systems.

**Example:** A tester is given a set of employee-level login credentials for the corporate network to assess what an attacker could do after a successful initial breach.

*Table: Comparison of Knowledge-Based Test Types*
| Aspect | Black-Box | Grey-Box | White-Box |
| :--- | :--- | :--- | :--- |
| **Tester Knowledge** | None | Partial | Full |
| **Realism** | High (external threat) | Medium (post-breach) | Low (focused audit) |
| **Time Efficiency** | Low | Medium | High |
| **Primary Focus** | Perimeter security, processes | Lateral movement, internal security | Code flaws, architectural issues |
| **Cost** | High | Medium | Low |

## Classification by Target Environment
Penetration tests can also be defined by the specific environment or technology being assessed.

### 1. Network Services Penetration Test
This is one of the most common types of tests. It focuses on identifying vulnerabilities in network infrastructure, including servers, workstations, network devices (routers, switches, firewalls), and network services.

**Sub-types include:**
*   **Internal Network Test:** Conducted from inside the network, simulating an insider threat.
*   **External Network Test:** Conducted from outside the network, targeting public-facing IP addresses.

**Common Tools:** Nmap, Nessus, Metasploit, Burp Suite (for web services on networks).

### 2. Web Application Penetration Test
This test focuses exclusively on web applications, APIs (REST, SOAP, GraphQL), and web services. It aims to find vulnerabilities like those listed in the OWASP Top 10.

**Key Areas:** Injection flaws (SQLi, OS Command), Broken Access Control, Cryptographic failures, Security misconfigurations.

**Common Tools:** Burp Suite Professional, OWASP ZAP, browser developer tools.

### 3. Wireless Network Penetration Test
This assessment targets wireless (Wi-Fi) networks. The tester attempts to identify weak encryption (WEP, WPA), weak passwords, rogue access points, and misconfigurations to gain unauthorized access to the wireless network.

**Common Tools:** Aircrack-ng suite, Kismet, Wireshark.

### 4. Social Engineering Penetration Test
This test assesses the human element of security. It involves manipulating individuals into breaking security procedures, such as revealing passwords or granting physical access.

**Common Vectors:**
*   **Phishing Emails:** Deceptive emails tricking users into clicking links or opening attachments.
*   **Vishing:** Voice phishing over the phone.
*   **Smishing:** SMS phishing.
*   **Physical Tailgating:** Following an authorized person into a restricted area.

### 5. Physical Penetration Test
Testers attempt to circumvent physical security controls to gain access to buildings, servers rooms, or workstations to plant devices or extract data. This often combines with social engineering.

**Common Targets:** Locks, badge readers, security guards, cameras.

### 6. Cloud Penetration Test
With the rise of cloud computing (IaaS, PaaS, SaaS), this test focuses on misconfigurations and vulnerabilities specific to cloud environments like AWS, Azure, and Google Cloud Platform.

**Key Focus:** Storage bucket permissions, IAM roles and policies, virtual machine security groups, managed service configurations.

**Important Note:** Cloud providers have specific rules of engagement that must be followed before testing their platforms.

*Table: Comparison of Environment-Based Test Types*
| Test Type | Primary Target | Key Vulnerabilities Sought | Common Tools |
| :--- | :--- | :--- | :--- |
| **Network Services** | Servers, Firewalls, Services | Missing patches, open ports, weak protocols | Nmap, Nessus, Metasploit |
| **Web Application** | Web Apps, APIs | OWASP Top 10 (e.g., SQLi, XSS) | Burp Suite, OWASP ZAP |
| **Wireless** | Wi-Fi Networks | Weak encryption, weak passwords | Aircrack-ng, Kismet |
| **Social Engineering** | People & Processes | Susceptibility to deception | Gophish, SET (Social-Engineer Toolkit) |
| **Physical** | Buildings & Access Controls | Lock bypass, tailgating | Lock picks, disguised devices |
| **Cloud** | Cloud Infrastructure & Services | Misconfigured S3 buckets, overly permissive IAM | Pacu, ScoutSuite, Cloud-specific CLIs |

## Other Specialized Test Types

### 1. Blind and Double-Blind Testing
*   **Blind Test:** A type of black-box test where the organization's security team is aware that a test is being conducted. This tests their ability to detect and respond to an attack.
*   **Double-Blind Test (Red Team Exercise):** The ultimate test of security posture. The security team (Blue Team) has **no prior knowledge** that a test is occurring. This simulates a real-world attack most accurately and tests both defensive technology and human processes (e.g., IR plan).

### 2. Automated vs. Manual Testing
*   **Automated Testing:** Uses tools to scan for known vulnerabilities quickly. Great for covering large attack surfaces but prone to false positives/negatives.
*   **Manual Testing:** Involves a skilled human tester who can think creatively, chain vulnerabilities together, and find complex business logic flaws that tools miss. Essential for a thorough assessment.

A robust penetration test will almost always involve a combination of both automated and manual techniques.

## Choosing the Right Test
The choice of test depends on the **Goals and Objectives** defined during the scoping phase.
*   **Regulatory Compliance (e.g., PCI DSS):** Often mandates both internal and external network tests, plus web app tests.
*   **Testing a new Web Application:** A white-box web app test is ideal before launch.
*   **Testing overall defensive capabilities:** A double-blind red team exercise is most comprehensive.
*   **Limited Budget/Time:** A grey-box test can provide the most value for money.

## Exam Tips
1.  **Memorize the Core Three:** Be able to define, compare, and contrast Black, White, and Grey-Box tests. Understand their simulative value and resource implications.
2.  **Know Your Environments:** Be prepared to suggest the most appropriate type of test (e.g., network, web, wireless) based on a given scenario.
3.  **Double-Blind is Key:** Remember that a Double-Blind test is synonymous with a Red Team exercise and is the best measure of an organization's real-world defensive readiness.
4.  **Tool Association:** While not required to list every tool, be familiar with the common tool categories associated with each test type (e.g., Burp Suite for web apps).
5.  **The Human Factor:** Never underestimate the importance of Social Engineering tests; humans are often the weakest link in the security chain.