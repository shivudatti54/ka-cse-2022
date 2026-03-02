# Security Design Principles

## Introduction
Security Design Principles are fundamental guidelines that help in creating secure information systems. These principles form the foundation of secure system architecture and are essential for protecting data and resources from unauthorized access, modification, or destruction. For BSc CS students at Delhi University (NEP 2024), understanding these principles is crucial for designing and implementing secure computing solutions.

## Key Security Design Principles

### 1. Principle of Least Privilege
- Users and processes should be granted only the minimum access rights necessary to complete their tasks
- Reduces potential damage from accidental or malicious actions
- Applies to user accounts, processes, and programs

### 2. Defense in Depth
- Multiple layers of security controls should be implemented
- If one layer fails, other layers provide protection
- Includes physical, technical, and administrative controls

### 3. Fail Secure (Fail Safe)
- Systems should fail in a secure manner
- When errors occur, access should be denied by default
- Prevents unauthorized access during system failures

### 4. Separation of Duties
- Critical tasks should be divided among different individuals
- Prevents single point of failure and fraud
- Ensures no one person has complete control over a sensitive operation

### 5. Economy of Mechanism
- Keep security mechanisms simple and straightforward
- Complex mechanisms are harder to analyze and more prone to vulnerabilities
- Simpler designs are easier to test and verify

### 6. Open Design (Kerckhoffs's Principle)
- Security should rely on key secrecy, not design secrecy
- System design can be public without compromising security
- Security through obscurity is insufficient

### 7. Complete Mediation
- Every access request must be checked against access control mechanisms
- Prevents bypassing of security controls
- Ensures consistent enforcement of access policies

### 8. Least Common Mechanism
- Minimize shared resources between users/processes
- Reduces potential information leakage channels
- Limits covert timing and storage channels

### 9. Psychological Acceptability
- Security mechanisms should not unnecessarily impede users
- User-friendly interfaces encourage compliance
- Security should be transparent to legitimate users

## Application in System Design
These principles guide security architecture decisions in:
- Software development lifecycle
- Network security design
- Operating system configuration
- Database management systems

They help identify potential threats, minimize vulnerabilities, and establish robust security policies.

## Conclusion
Security Design Principles provide a systematic framework for building secure information systems. By applying these principles, security professionals can create systems that are resilient against attacks and minimize potential damage from security breaches. For exam purposes, remember that these principles work together—their combined implementation provides comprehensive security coverage.

---
*Reference: Delhi University BSc (H) CS Syllabus, NEP 2024 - Information Security Unit*