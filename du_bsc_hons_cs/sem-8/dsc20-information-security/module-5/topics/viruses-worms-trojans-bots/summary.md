# Viruses, Worms, Trojans, and Bots - Summary

## Key Definitions and Concepts

- **Malware**: Malicious software designed to damage, disrupt, or gain unauthorized access to computer systems
- **Virus**: Malware that requires a host file and human intervention to spread; attaches to legitimate programs
- **Worm**: Self-replicating malware that spreads autonomously across networks without host files or human action
- **Trojan**: Malware disguised as legitimate software that deceives users into installation; does not replicate itself
- **Bot**: Compromised computer controlled remotely by an attacker; operates as part of a botnet
- **Botnet**: Network of compromised computers (zombies) coordinated by a command-and-control server
- **Payload**: The malicious component of malware that performs harmful actions
- **Command-and-Control (C2)**: Server infrastructure used by attackers to communicate with and control compromised systems

## Important Formulas and Theorems

This topic is primarily conceptual rather than formula-based. Key theoretical frameworks include:

- **Malware Classification**: Based on propagation method (self-replicating vs. non-replicating), host dependency (dependent vs. independent), and delivery mechanism (network vs. file-based)
- **Infection Chain**: Initial compromise → establishment → propagation → payload execution → exfiltration/impact

## Key Points

1. **Viruses** need human action (opening files) to spread; worms spread automatically through vulnerabilities
2. **Trojans** rely on social engineering and deception, unlike technical exploitation used by viruses/worms
3. **Worms** can cause rapid, massive infections (WannaCry infected 200,000+ systems in days)
4. **Bots** transform computers into zombies for coordinated attacks like DDoS
5. **Botnets** can contain millions of compromised devices (Mirai had 600,000+ IoT devices)
6. **Polymorphic viruses** change their code to evade antivirus detection
7. **Macro viruses** embed in documents and activate when files are opened
8. **RATs (Remote Access Trojans)** create backdoors for unauthorized remote control

## Common Mistakes to Avoid

1. Confusing viruses with worms—remember viruses need hosts, worms don't
2. Assuming Trojans self-replicate—they spread only through deception
3. Overlooking the human element in Trojan infections—user action is always required
4. Underestimating IoT botnets—security cameras, routers are common targets
5. Ignoring patch management—most worm attacks exploit known vulnerabilities

## Revision Tips

1. Create comparison tables differentiating all four malware types by propagation, dependency, and purpose
2. Memorize at least one real-world example for each malware type
3. Focus on the "why" behind each characteristic—understand the attacker's objectives
4. Practice explaining malware concepts in simple terms—this helps in exam explanations
5. Review recent cybersecurity incidents to connect theoretical concepts with real-world relevance
6. Understand the complete attack lifecycle from initial infection to impact