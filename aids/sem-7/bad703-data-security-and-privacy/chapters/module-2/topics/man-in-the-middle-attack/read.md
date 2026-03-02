# Man-in-the-Middle (MitM) Attack

## 1. Introduction

In the realm of data security, ensuring the confidentiality and integrity of communication between two parties is paramount. A **Man-in-the-Middle (MitM) attack** is a fundamental and potent cyber threat where an unauthorized attacker secretly intercepts and potentially alters the communication between two parties who believe they are directly communicating with each other. This attack is a direct assault on the core principles of secure communication: confidentiality, integrity, and authenticity. Understanding MitM attacks is crucial for engineering secure systems and networks.

## 2. Core Concepts

A MitM attack is essentially a form of eavesdropping. The attacker positions themselves between the victim (e.g., a user) and the legitimate entity (e.g., a web server, another user) to relay, capture, and even manipulate the data flowing between them.

The attack typically unfolds in two main phases:

### Phase 1: Interception
The first and most critical step is for the attacker to insert themselves into the communication channel. This is often done by compromising a network component or by tricking the victim's device into sending traffic through the attacker's system. Common interception techniques include:

*   **ARP Spoofing/Poisoning:** The attacker sends forged Address Resolution Protocol (ARP) messages onto a Local Area Network (LAN). This links the attacker's MAC address to the IP address of a legitimate device (like the default gateway/router). All traffic destined for that IP is now mistakenly sent to the attacker.
*   **DNS Spoofing:** The attacker compromises a DNS server or its cache, causing it to return a fraudulent IP address for a domain name. For example, a request for `www.mybank.com` could be redirected to the attacker's server IP instead of the bank's real IP.
*   **Rogue Wi-Fi Access Points:** An attacker sets up a malicious Wi-Fi hotspot with a legitimate-sounding name (e.g., "Free Airport WiFi"). When users connect, all their internet traffic flows through the attacker's machine.

### Phase 2: Decryption (If Traffic is Encrypted)
Once the traffic is intercepted, if it is encrypted (e.g., using HTTPS), the attacker cannot read it without the session keys. To bypass this, attackers often use:

*   **SSL Stripping:** The attacker acts as a "translator" between the victim and the server. They establish an *unencrypted* HTTP connection with the victim while maintaining a proper *encrypted* HTTPS connection with the server. The victim sees the site but is unaware their connection to the attacker is unsecured, allowing the attacker to see all data in plaintext.
*   **Fake Certificates:** The attacker may use a self-signed or stolen digital certificate to impersonate the legitimate website, hoping the user will ignore browser security warnings.

After interception and decryption, the attacker can simply **eavesdrop** (passive attack) on the communication to steal sensitive information like login credentials or credit card numbers. Alternatively, they can **modify** the data in transit (active attack), for instance, altering the destination bank account number in a financial transaction.

## 3. Examples

1.  **Public Wi-Fi Eavesdropping:** A student connects to a free, unsecured coffee shop Wi-Fi. An attacker on the same network uses ARP spoofing to become the "man-in-the-middle." The student then logs into their university portal. The attacker intercepts the HTTP (non-encrypted) session and captures their username and password.

2.  **Session Hijacking in E-Commerce:** A user starts a secure (HTTPS) session on an e-commerce site. An attacker uses DNS spoofing to redirect the user's connection to a malicious server. This server presents a fake certificate, and if the user accepts the warning, the attacker can decrypt the session, steal the user's session cookies, and take over their logged-in account to make fraudulent purchases.

## 4. Key Points & Mitigation Summary

*   **Definition:** A MitM attack involves an attacker secretly relaying and potentially altering communication between two parties who believe they are directly communicating.
*   **Goal:** To steal sensitive data (login credentials, financial info) or manipulate communications for malicious purposes.
*   **Phases:** Interception first, followed by decryption if the traffic is encrypted.
*   **Common Techniques:** ARP Spoofing, DNS Spoofing, and Rogue Wi-Fi access points.

**How to Prevent MitM Attacks:**

*   **Use Strong Encryption:** Always use protocols that provide end-to-end encryption, such as **HTTPS**, **SSL/TLS**, and **VPNs**. This renders intercepted data useless without the decryption key.
*   **Public Key Infrastructure (PKI):** Rely on trusted Certificate Authorities (CAs) to validate website certificates. Pay attention to browser warnings about invalid certificates.
*   **Network Security:** Use secure, encrypted Wi-Fi (WPA2/WPA3) and avoid public, unsecured networks for sensitive tasks. Network administrators can use tools like **Dynamic ARP Inspection (DAI)** and **DHCP Snooping** to prevent ARP spoofing on switches.
*   **User Vigilance:** Be cautious of unsolicited emails/links and always check for the padlock icon (`🔒`) and `https://` in the address bar.
*   **Multi-Factor Authentication (MFA):** Even if credentials are stolen via MitM, MFA can prevent account takeover as the attacker won't have the second factor.