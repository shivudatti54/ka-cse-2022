# Malicious Software Types

## Comprehensive Study Material for BSc (Hons) Computer Science — Information Security

---

## 1. Introduction

**Malicious software**, commonly abbreviated as **malware**, refers to any software designed to infiltrate, damage, or gain unauthorized access to computer systems without the owner's informed consent. In today's interconnected digital landscape, malware represents one of the most significant threats to information security, affecting individuals, corporations, governments, and critical infrastructure worldwide.

### Real-World Relevance

The proliferation of malware has reached alarming proportions. According to cybersecurity reports, over **450,000 new malware samples** are discovered daily. High-profile incidents such as the **WannaCry ransomware attack (2017)**, which affected over 200,000 computers across 150 countries including India's national crime records database, demonstrate the devastating real-world impact of malicious software. The **NotPetya attack** caused an estimated $10 billion in damages globally, making it one of the most costly cyberattacks in history.

For students pursuing **BSc (Hons) Computer Science under NEP 2024 UGCF at Delhi University**, understanding malware types is essential not only for academic success but also for future careers in cybersecurity, ethical hacking, and system administration. This topic forms a core component of the Information Security syllabus and is fundamental to comprehending how cyber threats evolve and how to defend against them.

---

## 2. Classification of Malware

Malware can be classified based on several criteria:

| Classification Basis | Types |
|---------------------|-------|
| **Propagation Method** | Virus, Worm, Trojan, Bot |
| **Payload/Behavior** | Ransomware, Keylogger, Rootkit, Cryptominer |
| **Target System** | Desktop, Mobile, Network-based |
| **Visibility** | Fileless, Stealth, Obfuscated |

Understanding these classifications helps security professionals identify, analyze, and mitigate different types of threats effectively.

---

## 3. Types of Malicious Software

### 3.1 Computer Viruses

A **computer virus** is a malicious code that attaches itself to legitimate programs or files, requiring user action (such as opening an infected file) to propagate. Unlike worms, viruses cannot spread autonomously.

**Characteristics:**
- Requires a host program
- Activates when the host program runs
- Can corrupt or delete data
- Spreads through file sharing, email attachments, and removable media

**Example:** The **CIH (Chernobyl) virus** (1998) would overwrite the master boot record and corrupt BIOS chips, rendering computers unusable.

### 3.2 Computer Worms

A **worm** is a self-replicating malware that spreads across networks without requiring human intervention or a host program. Worms exploit vulnerabilities in operating systems or applications to spread autonomously.

**Characteristics:**
- Does not require a host program
- Exploits network vulnerabilities
- Can consume bandwidth and slow networks
- Often includes malicious payloads

**Example:** The **Morris Worm (1988)** infected approximately 6,000 computers (about 10% of the early internet), demonstrating the destructive potential of self-replicating code.

### 3.3 Trojan Horses (Trojans)

A **Trojan horse** masquerades as legitimate software to deceive users into installing it. Unlike viruses and worms, Trojans do not self-replicate but create backdoors for attackers.

**Characteristics:**
- Disguised as legitimate applications
- Does not self-replicate
- Creates backdoors for remote access
- Can steal data, install additional malware, or provide remote control

**Example:** The **Emotet Trojan** (originally a banking Trojan) evolved into a major malware distribution platform, causing millions of dollars in damages globally.

### 3.4 Ransomware

**Ransomware** encrypts the victim's files or locks their system, demanding payment (typically cryptocurrency) for decryption or restoration. It has become one of the most profitable and widespread malware types.

**Characteristics:**
- Encrypts files using strong cryptography
- Displays ransom notes with payment instructions
- Often exfiltrates data before encryption (double extortion)
- Targets individuals, businesses, and governments

**Real-World Example:** The **WannaCry attack** exploited a Windows SMB vulnerability (EternalBlue) to spread globally, affecting the UK's National Health Service (NHS), India's police departments, and hundreds of organizations worldwide.

### 3.5 Rootkits

A **rootkit** is designed to provide continued privileged access (root-level) while concealing its presence from detection. Rootkits modify the operating system to hide their activities.

**Characteristics:**
- Operates at kernel or system level
- Modifies OS functions to hide presence
- Difficult to detect and remove
- Can maintain persistent access

**Example:** The **Sony BMG rootkit scandal (2005)** installed copy protection software that also acted as a rootkit, secretly collecting user data and creating security vulnerabilities.

### 3.6 Keyloggers

A **keylogger** (keystroke logger) records every keystroke made on a compromised system, capturing sensitive information such as passwords, credit card numbers, and personal messages.

**Characteristics:**
- Can be hardware or software-based
- Captures keystrokes continuously
- Stores or transmits logged data to attackers
- Often used in identity theft and corporate espionage

**Real-World Incident:** Keyloggers have been used in numerous banking fraud cases to capture customer credentials, leading to significant financial losses in India's banking sector.

### 3.7 Adware and Spyware

**Adware** automatically displays or downloads advertising material, often through intrusive pop-ups. **Spyware** monitors user activity and collects information without consent.

**Characteristics of Adware:**
- Generates revenue through advertisements
- May track browsing habits
- Often bundled with legitimate software

**Characteristics of Spyware:**
- Monitors system activity
- Collects personal information
- Difficult to detect due to stealthy operation

### 3.8 Botnets

A **botnet** is a network of compromised computers (bots or zombies) controlled remotely by an attacker (botmaster). Botnets are used for various malicious activities including DDoS attacks, spam distribution, and cryptocurrency mining.

**Characteristics:**
- Coordinated network of infected machines
- Controlled via command-and-control (C2) servers
- Can consist of millions of devices
- Used for distributed denial-of-service (DDoS) attacks

**Example:** The **Mirai botnet (2016)** infected IoT devices and launched massive DDoS attacks, including one that disrupted major websites like Twitter, Netflix, and Reddit.

### 3.9 Advanced Persistent Threats (APTs)

An **Advanced Persistent Threat** is a prolonged, targeted cyberattack in which an intruder gains network access and remains undetected for extended periods. APTs are typically state-sponsored and target high-value assets.

**Characteristics:**
- Long-term presence in a network
- Highly sophisticated and targeted
- Often involves multiple attack stages
- Targets sensitive government or corporate data

**Real-World Examples:**
- **Stuxnet (2010):** Targeted Iran's nuclear enrichment centrifuges
- **APT29 (Cozy Bear):** Linked to Russian intelligence, involved in SolarWinds supply chain attack

### 3.10 Cryptominers (Cryptojacking)

**Cryptominers** secretly use a victim's computational resources to mine cryptocurrency. This can significantly degrade system performance and increase energy costs.

**Characteristics:**
- Consumes CPU/GPU resources
- Often delivered via malicious websites or software
- Can operate as standalone malware or within other malware
- Difficult to detect due to minimal visible activity

---

## 4. Code Examples

Understanding malware behavior through code examples helps security professionals develop effective detection and mitigation strategies. The following examples are for **educational and defensive purposes only**.

### 4.1 Simple Keylogger (Python) — For Defensive Understanding

```python
import keyboard
import smtplib
from email.mime.text import MIMEText
import time

class EducationalKeylogger:
    """
    This code is for educational purposes only to understand
    how keyloggers function for defensive security development.
    """
    
    def __init__(self):
        self.log = []
        self.email_interval = 60  # seconds
        
    def on_key_event(self, event):
        """Record keystroke events"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {event.name}"
        self.log.append(log_entry)
        print(f"Key logged: {event.name}")  # For demo purposes
        
    def start_logging(self):
        """Start keyboard monitoring"""
        keyboard.on_release(self.on_key_event)
        print("Keylogger initialized. Press ESC to stop.")
        keyboard.wait('esc')
        
    def get_log(self):
        """Retrieve captured keystrokes"""
        return "\n".join(self.log)

# Defensive note: This demonstrates why input validation,
# endpoint protection, and user awareness are critical
```

**Defensive Measures:**
- Use endpoint detection and response (EDR) solutions
- Implement keystroke encryption
- Monitor system calls for suspicious behavior

### 4.2 Simulating Worm Propagation Concept — For Academic Study

```python
"""
Academic simulation of network worm propagation dynamics.
For understanding epidemiological models in cybersecurity.
"""

import random
import networkx as nx
from collections import deque

class WormPropagationSimulation:
    """
    Demonstrates how worms spread through networks.
    Used for developing containment strategies.
    """
    
    def __init__(self, network, infection_probability=0.3):
        self.network = network
        self.infection_probability = infection_probability
        self.infected_nodes = set()
        self.quarantined_nodes = set()
        
    def infect_patient_zero(self, initial_node):
        """Infect the first node"""
        self.infected_nodes.add(initial_node)
        print(f"Patient Zero infected: Node {initial_node}")
        
    def simulate_spread(self):
        """Simulate worm propagation step by step"""
        newly_infected = set()
        
        for node in self.infected_nodes:
            # Get neighbors (potential targets)
            neighbors = list(self.network.neighbors(node))
            
            for neighbor in neighbors:
                if (neighbor not in self.infected_nodes and 
                    neighbor not in self.quarantined_nodes):
                    # Probabilistic infection
                    if random.random() < self.infection_probability:
                        newly_infected.add(neighbor)
        
        # Update infected set
        self.infected_nodes.update(newly_infected)
        return len(newly_infected)

# This simulation helps security professionals understand
# propagation patterns and design better containment strategies

# Defensive applications:
# - Network segmentation
# - Rapid patching
# - Intrusion detection systems
```

---

## 5. Detection and Prevention Strategies

Understanding malware types is incomplete without knowing how to defend against them:

| Malware Type | Detection Methods | Prevention Strategies |
|-------------|-------------------|----------------------|
| Viruses | Signature-based AV, Heuristics | Avoid suspicious attachments, Keep software updated |
| Worms | Network monitoring, IDS/IPS | Patch vulnerabilities, Firewall configuration |
| Trojans | Behavior analysis, Sandbox | Download from trusted sources, Least privilege |
| Ransomware | File integrity monitoring, Backup verification | Regular backups, Email filtering |
| Rootkits | Memory forensics, Rootkit detectors | Secure boot, Minimal trust |
| Keyloggers | Process monitoring, Hardware inspection | Virtual keyboards, Password managers |
| Botnets | Network traffic analysis, C2 detection | Botnet detection tools |
| APTs | SIEM, Threat hunting, Log analysis | Defense-in-depth, Threat intelligence |

---

## 6. Key Takeaways

1. **Malware Diversity:** Malicious software encompasses numerous types—viruses, worms, Trojans, ransomware, rootkits, keyloggers, botnets, APTs, and cryptominers—each with distinct propagation methods and payloads.

2. **Evolution of Threats:** Malware has evolved from simple pranks to sophisticated, state-sponsored attacks. Modern threats like ransomware and APTs cause billions in damages globally.

3. **Propagation Mechanisms:** Understanding how different malware spreads is crucial—viruses need hosts, worms propagate autonomously, Trojans deceive, and botnets coordinate attacks.

4. **Defense-in-Depth:** No single solution prevents all malware. A multi-layered approach including preventive controls, detection mechanisms, and incident response is essential.

5. **Ethical Responsibility:** Knowledge of malware should be used for defensive purposes. Creating or distributing malware is illegal and unethical.

6. **Real-World Impact:** India has witnessed significant malware attacks, including the 2017 WannaCry incident affecting Indian systems. Awareness and preparedness are critical.

7. **Academic Foundation:** This topic forms a core component of Delhi University's BSc (Hons) Computer Science syllabus under Information Security, preparing students for careers in cybersecurity.

---

## 7. Multiple Choice Questions (University-Level)

### Question 1
**Which type of malware can spread autonomously without requiring a host program or user intervention?**

A) Virus  
B) Trojan  
C) Worm  
D) Keylogger  

**Answer:** C) Worm  
**Explanation:** Worms are self-replicating malware that can spread across networks independently, unlike viruses (which require a host) and Trojans/Keyloggers (which require user installation).

---

### Question 2
**What distinguishes ransomware from other malware types?**

A) It steals credentials  
B) It encrypts files and demands payment  
C) It creates botnets  
D) It displays advertisements  

**Answer:** B) It encrypts files and demands payment  
**Explanation:** Ransomware specifically encrypts victim files and demands a ransom for decryption, as seen in the WannaCry and NotPetya attacks.

---

### Question 3
**Which malware is specifically designed to hide its presence and provide continued privileged access?**

A) Adware  
B) Rootkit  
C) Spyware  
D) Worm  

**Answer:** B) Rootkit  
**Explanation:** Rootkits modify operating system functions to hide their presence and maintain root-level access to compromised systems.

---

### Question 4
**In the context of APTs (Advanced Persistent Threats), what does the term "Persistence" refer to?**

A) The ability to replicate quickly  
B) Long-term unauthorized access to a network  
C) Encryption of all files  
D) Continuous advertising display  

**Answer:** B) Long-term unauthorized access to a network  
**Explanation:** APTs maintain prolonged, stealthy access to targeted networks, often remaining undetected for months or years while exfiltrating data.

---

### Question 5
**What is the primary purpose of a keylogger?**

A) To slow down system performance  
B) To capture keystrokes and steal information  
C) To spread through networks  
D) To encrypt files  

**Answer:** B) To capture keystrokes and steal information  
**Explanation:** Keyloggers record every keystroke to capture sensitive information like passwords, credit card numbers, and personal communications.

---

### Question 6
**Which malware type was responsible for the 2016 Mirai botnet attack that affected major websites?**

A) Ransomware  
B) Botnet  
C) Rootkit  
D) Adware  

**Answer:** B) Botnet  
**Explanation:** Mirai created a botnet by infecting IoT devices, which was then used to launch massive DDoS attacks against major internet services.

---

### Question 7
**What is the primary characteristic of a Trojan horse compared to viruses and worms?**

A) It self-replicates  
B) It requires a host program  
C) It disguises itself as legitimate software  
D) It spreads through email  

**Answer:** C) It disguises itself as legitimate software  
**Explanation:** Trojans masquerade as legitimate applications to deceive users into installing them, unlike self-replicating viruses/worms.

---

### Question 8
**Double extortion in ransomware attacks refers to:**

A) Demanding payment twice  
B) Encrypting data and threatening to leak it  
C) Targeting two different organizations  
D) Using two encryption algorithms  

**Answer:** B) Encrypting data and threatening to leak it  
**Explanation:** Double extortion involves both encrypting victim data and threatening to publish stolen data if ransom is not paid.

---

### Question 9
**Which of the following is NOT a characteristic of Advanced Persistent Threats (APTs)?**

A) State-sponsored attackers  
B) Short-term attacks  
C) Sophisticated techniques  
D) Targeted at high-value assets  

**Answer:** B) Short-term attacks  
**Explanation:** APTs are characterized by long-term, persistent attacks typically sponsored by nation-states targeting sensitive information.

---

### Question 10
**The EternalBlue exploit, used by the WannaCry ransomware, targeted which protocol?**

A) HTTP  
B) FTP  
C) SMB  
D) SSH  

**Answer:** C) SMB  
**Explanation:** EternalBlue exploited a vulnerability in Microsoft's Server Message Block (SMB) protocol, enabling WannaCry to spread rapidly across networks.

---

## 8. Flashcards for Quick Revision

| Term | Definition |
|------|------------|
| **Malware** | Malicious software designed to damage, disrupt, or gain unauthorized access to computer systems |
| **Virus** | Malware that attaches to legitimate programs and requires user action to spread |
| **Worm** | Self-replicating malware that spreads autonomously across networks |
| **Trojan** | Malware disguised as legitimate software that creates backdoors for attackers |
| **Ransomware** | Malware that encrypts files and demands payment for decryption |
| **Rootkit** | Malware that hides its presence and provides continued privileged system access |
| **Keylogger** | Software that records keystrokes to steal sensitive information |
| **Botnet** | Network of compromised computers controlled by an attacker for malicious activities |
| **APT** | Advanced Persistent Threat — prolonged, targeted attack typically by nation-states |
| **Cryptominer** | Malware that uses system resources to mine cryptocurrency without authorization |

---

## References

1. Stallings, W. (2021). *Network Security Essentials: Applications and Standards*. Pearson Education.
2. Kumar, S. & Singh, R. (2023). *Cybersecurity: A Comprehensive Approach*. Delhi University Press.
3. Europol. (2023). *Internet Organised Crime Threat Assessment (IOCTA)*.
4. NIST Special Publication 800-83: Guide to Malware Incident Prevention and Handling.
5. Cisco. (2024). *Cybersecurity Report — Threat Landscape*.
6. Delhi University, NEP 2024 UGCF Syllabus — Information Security.

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*