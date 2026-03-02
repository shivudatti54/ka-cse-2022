# Security Concepts, Threats, and Attacks

## Introduction

In today's interconnected digital landscape, information security has become a fundamental concern for organizations, governments, and individuals alike. The exponential growth of the internet, cloud computing, and mobile technologies has transformed how we store, process, and transmit sensitive information. According to the annual reports from cybersecurity agencies worldwide, the number and sophistication of cyber attacks have increased dramatically over the past decade, causing billions of dollars in damages and compromising millions of records.

Information security encompasses the practices, policies, and technologies designed to protect information assets from unauthorized access, use, disclosure, disruption, modification, or destruction. For students pursuing Computer Science at the University of Delhi, understanding the fundamental concepts of security, along with the various threats and attack vectors, forms the cornerstone of building secure systems and applications. This knowledge is not merely theoretical—it is essential for any professional working in software development, system administration, or cybersecurity.

This module introduces the core security concepts embodied in the CIA Triad, explores the taxonomy of security threats, and examines the various attack methodologies employed by malicious actors. Through this understanding, you will be equipped to identify vulnerabilities in systems and implement appropriate countermeasures.

## Key Concepts

### The CIA Triad

The foundation of information security rests upon three fundamental principles, collectively known as the CIA Triad:

**Confidentiality** ensures that information is accessible only to authorized individuals and remains private. This principle governs access controls, encryption, and data classification systems. Confidentiality breaches occur when sensitive information—such as personal identities, financial records, or trade secrets—is exposed to unauthorized parties. Techniques to maintain confidentiality include encryption algorithms (AES, RSA), access control lists (ACLs), steganography, and proper data handling procedures.

**Integrity** guarantees that information remains accurate, complete, and unaltered throughout its lifecycle. Unauthorized modifications to data—whether accidental or intentional—compromise integrity. Digital signatures, checksums, hash functions (SHA-256, MD5), and version control systems help ensure data integrity. For instance, when you download software, the provider often publishes a hash value; you can verify the downloaded file's integrity by comparing hash values.

**Availability** ensures that authorized users have uninterrupted access to information and associated resources when needed. Denial of Service (DoS) attacks, hardware failures, and natural disasters threaten availability. Redundancy, fault-tolerant systems, backup procedures, and robust network infrastructure help maintain availability.

### Additional Security Concepts

**Authentication** is the process of verifying the identity of a user, system, or entity before granting access to resources. Common authentication methods include passwords, biometrics, smart cards, security tokens, and multi-factor authentication (MFA). For example, when you log into your university portal with your roll number and password, the system authenticates your identity.

**Authorization** determines what an authenticated user is permitted to do—specifically, what resources they can access and what operations they can perform. Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC) are common authorization models. After authentication, authorization ensures you can only access your own marksheet, not other students' records.

**Non-repudiation** provides assurance that a parties cannot deny their actions or transactions. Digital signatures and audit logs provide non-repudiation. In legal contexts, a digitally signed contract ensures neither party can claim they didn't sign it.

**Accountability** ensures that every action can be traced back to the responsible entity through audit trails and logging mechanisms.

## Threat Taxonomy

A threat represents any potential occurrence that could harm an information system by exploiting vulnerabilities. Threats can be categorized in multiple ways:

### By Source

**External Threats** originate from outside the organization—hackers, cybercriminals, competitors, and foreign governments. These threats often exploit technical vulnerabilities in network infrastructure, web applications, or operating systems.

**Internal Threats** come from within the organization—disgruntled employees, careless staff, or contractors with privileged access. Studies indicate that internal threats account for a significant percentage of security incidents, as insiders often have legitimate access to sensitive resources.

### By Intent

**Malicious Threats** involve deliberate actions to cause harm, including malware, phishing, ransomware, and espionage.

**Accidental Threats** result from human error, system failures, or natural disasters—unintentional data deletion, accidental publication of confidential information, or hardware failure.

### Common Threat Categories

**Malware** (Malicious Software) encompasses viruses, worms, trojans, ransomware, spyware, and botnets. A **virus** attaches itself to legitimate programs and spreads when executed. A **worm** replicates independently across networks without user intervention. A **trojan** masquerades as legitimate software while performing malicious actions. **Ransomware** encrypts victim data and demands payment for decryption keys—attacks like WannaCry caused global damage in 2017.

**Phishing** involves fraudulent communications, typically emails appearing from trustworthy sources, designed to steal credentials or install malware. Spear phishing targets specific individuals, while whaling targets executives.

**Social Engineering** exploits human psychology rather than technical vulnerabilities. Pretexting involves creating a fabricated scenario, baiting offers enticing rewards, and tailgating involves following authorized personnel into restricted areas.

**Denial of Service (DoS) and Distributed Denial of Service (DDoS)** attacks overwhelm target systems with traffic, rendering them unavailable to legitimate users. DDoS attacks leverage botnets—networks of compromised computers—to amplify the attack volume.

**Man-in-the-Middle (MITM)** attacks intercept communications between two parties to eavesdrop or modify traffic. Common on unsecured Wi-Fi networks, attackers position themselves between the user and the intended destination.

**SQL Injection** exploits vulnerabilities in web applications that use unsanitized user input in database queries. Attackers can extract, modify, or delete database contents.

**Zero-Day Exploits** target previously unknown vulnerabilities for which no patch exists—the "zero-day" refers to the zero days between vulnerability discovery and patch release.

## Attack Classification

### Passive vs Active Attacks

**Passive Attacks** involve eavesdropping on communications without altering data. Examples include traffic analysis, wiretapping, and shoulder surfing. Passive attacks are difficult to detect because they don't modify system behavior or leave obvious traces.

**Active Attacks** involve modifying data, disrupting services, or gaining unauthorized access. Examples include DoS attacks, malware installation, and data modification. Active attacks are more easily detectable but cause greater damage.

### Insider vs Outsider Attacks

**Insider Attacks** originate from individuals within the organization with legitimate access—employees, contractors, or partners. These attacks are particularly dangerous because insiders understand the organization's systems and security measures.

**Outsider Attacks** come from external threat actors—hackers, criminal organizations, or nation-state actors—typically targeting public-facing systems.

### Attack Vectors and Surfaces

An **attack vector** is the method or pathway an attacker uses to access a target system. Common vectors include email attachments, malicious websites, infected software, USB drives, and network vulnerabilities.

The **attack surface** represents the total sum of all entry points (vectors) that an attacker can exploit. Reducing the attack surface—through network segmentation, disabling unnecessary services, and implementing firewalls—strengthens security posture.

### Security Attack Lifecycle

Most attacks follow a recognizable pattern:

1. **Reconnaissance**: Gathering information about the target through public sources, scanning, and social engineering.
2. **Scanning**: Identifying vulnerabilities in target systems using automated tools.
3. **Gaining Access**: Exploiting vulnerabilities to enter the system.
4. **Maintaining Access**: Establishing persistent presence through backdoors or malware.
5. **Covering Tracks**: Removing evidence of the attack to avoid detection.
6. **Exfiltration**: Stealing data or causing damage before exiting.

Understanding this lifecycle helps security professionals detect and respond to attacks at various stages.

## Examples

### Example 1: Phishing Attack Analysis

Consider a student receiving an email appearing to be from the university library, claiming their membership will expire and requesting credential verification through a provided link.

**Step-by-Step Analysis:**
1. **Recognition**: The email creates urgency ("will expire") and requests sensitive information.
2. **Verification**: The student should check the sender's email address—universityofficial@library-du.com (fake) vs. library@du.ac.in (genuine).
3. **Investigation**: Hovering over the link reveals it points to a suspicious domain, not the university's actual website.
4. **Proper Response**: Report the email to IT security, delete it, and never click suspicious links.

This example demonstrates how social engineering exploits trust and urgency to compromise credentials.

### Example 2: SQL Injection Demonstration

A vulnerable login form might construct queries like:
```
SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
```

If an attacker enters `' OR '1'='1` as the username, the query becomes:
```
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = ''
```

Since '1'='1' is always true, the attacker gains unauthorized access without valid credentials.

**Countermeasures**: Use parameterized queries (prepared statements), input validation, and principle of least privilege for database accounts.

### Example 3: DDoS Attack Impact

During a DDoS attack on a university's online examination portal:
1. Attackers flood the server with thousands of requests from botnets
2. Server resources become exhausted handling malicious traffic
3. Legitimate students cannot access the portal for their exams
4. The university experiences reputational damage and operational disruption

**Countermeasures**: Traffic scrubbing services, rate limiting, content delivery networks (CDNs), and incident response planning.

## Exam Tips

1. **Remember the CIA Triad** - This forms the foundation of information security and appears frequently in exams. Be able to explain each component with examples.

2. **Differentiate between threats, vulnerabilities, and attacks** - A vulnerability is a weakness, a threat is potential harm exploiting that vulnerability, and an attack is the actual exploitation.

3. **Know the difference between authentication and authorization** - Authentication verifies identity (who you are); authorization determines permissions (what you can do).

4. **Understand passive vs active attacks** - Passive attacks only observe; active attacks modify data or systems.

5. **Recognize common attack names and their characteristics** - Phishing, MITM, SQL Injection, DoS/DDoS, malware types.

6. **Explain the attack lifecycle** - Reconnaissance → Scanning → Gaining Access → Maintaining Access → Covering Tracks → Exfiltration.

7. **Apply security concepts to real scenarios** - Exam questions often present scenarios where you must identify the relevant threat type and suggest countermeasures.