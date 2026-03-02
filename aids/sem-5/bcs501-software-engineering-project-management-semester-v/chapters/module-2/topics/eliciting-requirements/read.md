# Security Requirements Engineering

## Introduction to Security Requirements Engineering

Security Requirements Engineering (SRE) is the systematic process of identifying, documenting, and managing security requirements throughout the Software Development Life Cycle (SDLC). It represents a proactive approach to building secure software by "shifting security left" – addressing security concerns early in the development process rather than as an afterthought.

Traditional software requirements focus on functionality, performance, and usability, but often neglect security aspects. SRE bridges this gap by integrating security considerations directly into the requirements phase, ensuring that security is built into the foundation of the application rather than bolted on later.

```
Traditional SDLC vs. Secure SDLC with SRE

Traditional: Requirements → Design → Implementation → Testing → Deployment
             (Security often addressed here →)           ↑

Secure SDLC: Security Requirements → Secure Design → Secure Implementation → Security Testing → Secure Deployment
             ↑                                                                                ↑
        Security built-in                                                             Security validated
```

## Importance of Security Requirements

Security requirements serve several critical functions in the development process:

1. **Foundation for secure design**: They provide the basis for architectural decisions and design patterns
2. **Guidance for developers**: Clear requirements help developers implement security controls correctly
3. **Basis for testing**: Security tests validate whether requirements have been met
4. **Compliance alignment**: Help meet regulatory and standards requirements (GDPR, HIPAA, PCI-DSS)
5. **Risk management**: Identify and address security risks before implementation

Without well-defined security requirements, development teams may:
- Implement inconsistent security controls
- Overlook critical security features
- Waste resources on unnecessary security measures
- Create vulnerabilities that are expensive to fix later

## Types of Security Requirements

Security requirements can be categorized into several types:

### Functional Security Requirements
These specify security-related functions the system must perform:

- Authentication mechanisms (multi-factor, biometric)
- Authorization controls (role-based access control)
- Audit logging capabilities
- Encryption of sensitive data
- Input validation routines

### Non-Functional Security Requirements
These specify quality attributes related to security:

- Availability (resistance to DoS attacks)
- Confidentiality (protection from unauthorized disclosure)
- Integrity (protection from unauthorized modification)
- Accountability (ability to trace actions to users)
- Reliability (resistance to failure under attack)

### Constraints and Policies
These include organizational or regulatory requirements:

- Password complexity policies
- Data retention periods
- Compliance requirements (PCI-DSS, HIPAA)
- Privacy protections (GDPR)

## The Security Requirements Engineering Process

The SRE process typically follows these stages:

### 1. Asset Identification
Identify what needs protection:
- Data assets (PII, financial data, intellectual property)
- System assets (servers, databases, network infrastructure)
- Business processes (critical operations, revenue streams)

```
Asset Identification Process

Business Context → [Identify Critical Assets] → [Classify Assets] → [Determine Protection Needs]
       ↑                                                        ↓
Regulatory Requirements                                  Security Requirements
```

### 2. Threat Identification
Use techniques like threat modeling to identify potential threats:
- STRIDE methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- Attack tree analysis
- Abuse cases

### 3. Vulnerability Analysis
Identify weaknesses that could be exploited:
- Architectural vulnerabilities
- Design flaws
- Implementation weaknesses

### 4. Security Requirement Elicitation
Gather security requirements from various sources:
- Stakeholder interviews
- Regulatory requirements
- Security standards (OWASP, NIST, ISO 27001)
- Historical incident data
- Industry best practices

### 5. Requirement Specification
Document requirements clearly and unambiguously:
- Use consistent templates
- Include rationale and priority
- Specify verification methods

### 6. Validation and Verification
Ensure requirements are complete, consistent, and testable:
- Requirements reviews
- Traceability matrices
- Test case development

## Elicitation Techniques

Several techniques can be used to elicit security requirements:

### 1. Abuse Cases
Develop scenarios describing how the system could be misused:

```
Example Abuse Case Template:

Title: Unauthorized access to admin functions
Actor: Malicious user
Preconditions: User has standard privileges
Main Scenario:
1. User attempts to access admin URL directly
2. System checks permissions
3. System blocks access and logs attempt
Postconditions: Access denied, event logged
```

### 2. Security Use Cases
Extend regular use cases with security considerations:

```
Regular Use Case: "User logs into system"
Security Use Case: "User logs into system with secure authentication"
Extensions:
- System validates input against injection attacks
- System implements account lockout after 5 failed attempts
- System uses secure session management
```

### 3. Threat Modeling
Systematic approach to identifying and addressing threats:

```
Threat Modeling Process:

[Diagram System] → [Identify Threats] → [Mitigate Threats] → [Validate]
      ↑                   ↓                    ↓
Assets & Trust Boundaries          Security Requirements
```

### 4. Security Requirements Workshops
Structured sessions with stakeholders to identify requirements:

```
Workshop Structure:
- Introduction to security concepts
- Asset identification exercise
- Threat brainstorming session
- Requirement prioritization
```

### 5. Compliance Analysis
Review regulatory and standards requirements:
- GDPR: Data protection, privacy by design
- PCI-DSS: Payment card security
- HIPAA: Healthcare information protection
- ISO 27001: Information security management

## Documenting Security Requirements

Effective documentation is crucial for security requirements. Use consistent templates:

### Security Requirement Template

```
ID: SR-001
Type: Functional/Non-functional/Constraint
Description: The system shall [security function]
Rationale: [Why this requirement is important]
Source: [Regulation, standard, or threat]
Priority: High/Medium/Low
Verification: [How to test this requirement]
Dependencies: [Other requirements this depends on]
```

### Requirements Traceability Matrix

| Requirement ID | Source          | Design Element     | Test Case     | Status    |
|----------------|-----------------|--------------------|---------------|-----------|
| SR-001         | OWASP ASVS L1   | AuthController     | TC-AUTH-01    | Implemented|
| SR-002         | PCI-DSS Req 3.4 | EncryptionService  | TC-ENC-02     | In Progress|
| SR-003         | GDPR Art. 32    | AuditLogger        | TC-AUD-01     | Verified   |

## Common Security Requirements Categories

### Authentication Requirements
- Multi-factor authentication for administrative access
- Password complexity rules (minimum length, character types)
- Account lockout after failed attempts
- Secure password recovery mechanisms
- Session timeout after period of inactivity

### Authorization Requirements
- Role-based access control implementation
- Principle of least privilege enforcement
- Separation of duties for critical functions
- Access review processes

### Data Protection Requirements
- Encryption of sensitive data at rest (AES-256)
- Encryption of data in transit (TLS 1.2+)
- Proper key management practices
- Data sanitization before disposal

### Input Validation Requirements
- Validation of all input sources (forms, APIs, files)
- Context-specific output encoding
- Protection against common injection attacks (SQLi, XSS)
- File upload restrictions (type, size, content scanning)

### Logging and Monitoring Requirements
- Audit trails for security-relevant events
- Log protection against tampering
- Regular log review processes
- Alerting for suspicious activities

### Error Handling Requirements
- Generic error messages to users
- Detailed error logging for administrators
- No sensitive information in error responses
- Graceful failure under attack conditions

## Integrating Security Requirements with DevSecOps

Security requirements play a crucial role in DevSecOps integration:

### Automated Requirements Validation
- Security requirements as code
- Automated compliance checking
- Continuous validation through CI/CD pipelines

### Security Requirements in User Stories

```
As a [role], I want [feature] so that [benefit]
Security Considerations:
- [Security requirement 1]
- [Security requirement 2]
Acceptance Criteria:
- [Functional acceptance criterion]
- [Security acceptance criterion]
```

### Example: Secure Login User Story

```
As a user, I want to log in securely so that I can access my account
Security Considerations:
- Password must be hashed with bcrypt
- Implement account lockout after 5 failed attempts
- Use HTTPS for all authentication requests
Acceptance Criteria:
- System rejects weak passwords (<12 characters)
- System locks account after 5 failed login attempts
- Login page only accessible via HTTPS
```

## Challenges in Security Requirements Engineering

### 1. Balancing Security and Usability
Overly restrictive security requirements can impact user experience:
- Solution: Involve UX designers in security discussions
- Implement security controls transparently where possible

### 2. Changing Threat Landscape
New threats emerge constantly:
- Solution: Regular requirement reviews and updates
- Monitor threat intelligence sources

### 3. Resource Constraints
Limited time and budget for security:
- Solution: Risk-based prioritization
- Focus on high-impact requirements first

### 4. Lack of Security Expertise
Development teams may lack security knowledge:
- Solution: Security training and awareness
- Engage security specialists early

### 5. Requirement Ambiguity
Vague requirements lead to inconsistent implementation:
- Solution: Clear, testable requirement specifications
- Examples and implementation guidance

## Best Practices for Security Requirements Engineering

1. **Start early**: Integrate security from the beginning of the SDLC
2. **Involve stakeholders**: Include security, development, operations, and business representatives
3. **Use standards**: Leverage established frameworks (OWASP ASVS, NIST SP 800-53)
4. **Prioritize based on risk**: Focus on requirements that address the highest risks
5. **Make requirements testable**: Ensure each requirement can be verified
6. **Maintain traceability**: Link requirements to design, implementation, and testing
7. **Review and update regularly**: Adapt to changing threats and business needs

## Tools for Security Requirements Management

| Tool Type | Examples | Purpose |
|-----------|----------|---------|
| Requirements Management | JIRA, DOORS, Modern Requirements | Documenting and tracking requirements |
| Threat Modeling | Microsoft Threat Modeling Tool, OWASP Threat Dragon | Identifying security requirements |
| Security Standards | OWASP ASVS, NIST CSF, ISO 27002 | Requirement checklists and templates |
| Compliance Management | RSA Archer, MetricStream, StandardFusion | Mapping requirements to regulations |

## Exam Tips

1. **Understand the different types** of security requirements (functional, non-functional, constraints)
2. **Remember key elicitation techniques** like abuse cases, threat modeling, and security use cases
3. **Know the common requirement categories** (authentication, authorization, data protection, etc.)
4. **Practice writing clear, testable requirements** using standard templates
5. **Understand how security requirements integrate** with DevSecOps and agile methodologies
6. **Be familiar with major security standards** (OWASP ASVS, NIST, ISO) as requirement sources
7. **Recognize common challenges** and how to address them in real-world scenarios