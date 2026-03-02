# Threat Modeling in the Design Phase

## Introduction to Threat Modeling

Threat modeling is a structured approach for identifying, quantifying, and addressing security risks during the design phase of the Software Development Life Cycle (SDLC). It is a proactive security measure, contrasting with reactive approaches like penetration testing that occur later in the development process. By analyzing a system's design before code is written, teams can identify potential security flaws when they are easiest and least expensive to fix.

The core philosophy of threat modeling is to "think like an attacker." Development teams systematically analyze their system designs to anticipate how an adversary might attempt to compromise the system's Confidentiality, Integrity, or Availability (the CIA triad).

## Why Threat Modeling in the Design Phase?

Integrating threat modeling into the design phase offers significant advantages:

- **Cost-Effectiveness:** Fixing a design flaw before any code is written is exponentially cheaper than remediating a vulnerability discovered in production. The later a flaw is found, the higher the cost to fix it.
- **Shift-Left Security:** This practice embodies the "shift-left" principle of DevSecOps, moving security considerations earlier in the SDLC. It builds security in rather than bolting it on.
- **Improved Design Decisions:** The process forces architects and developers to consider security implications upfront, leading to more robust and resilient system architectures.
- **Comprehensive Coverage:** It provides a systematic way to ensure security is considered across all components and data flows, reducing the chance of overlooking critical areas.

## Key Concepts and Terminology

- **Asset:** Anything valuable that needs to be protected (e.g., user data, intellectual property, system resources).
- **Threat:** A potential event or action that could cause harm to an asset by exploiting a vulnerability.
- **Vulnerability:** A weakness or flaw in the system's design, implementation, or operation that could be exploited by a threat.
- **Attack Vector:** The path or means by which an attacker gains access to execute an attack.
- **Threat Agent (or Actor):** The entity (e.g., hacker, script kiddie, insider threat) that initiates the threat.
- **Mitigation:** A security control, countermeasure, or safeguard implemented to reduce the impact or likelihood of a threat.

## The Threat Modeling Process: A Step-by-Step Approach

A common and effective methodology for threat modeling can be broken down into four key steps, often remembered by the acronym **PASTA** (Process for Attack Simulation and Threat Analysis) or the simpler **DREAD** (for risk rating), but we'll use a foundational four-step process.

### Step 1: Decompose the Application

The first step is to gain a deep understanding of the system you are modeling. This involves creating a high-level architectural diagram.

1.  **Identify Assets:** What are you trying to protect? (e.g., customer PII, database, admin credentials).
2.  **Identify Entry Points:** Where can data or commands enter the system? (e.g., login API, file upload endpoint, user input field).
3.  **Identify Trust Levels:** What are the trust boundaries? (e.g., the internet is untrusted, the internal application server is trusted). Data crossing a trust boundary is a critical point for analysis.
4.  **Diagram Data Flow:** Create a Data Flow Diagram (DFD) showing how data moves between external entities, processes, data stores, and trust boundaries.

**Example ASCII Data Flow Diagram (DFD):**

```
    +-------------+      +-----------------+      +---------------+      +-----------+
    |   Internet  |----->|  Web Server    |----->| Application   |----->| Database  |
    | (Untrusted) |<-----| (Trust Boundary)|<-----| Server        |<-----| (Data     |
    +-------------+      +-----------------+      | (Trusted)     |      |  Store)   |
                                                   +---------------+      +-----------+
```

_This simple diagram shows data flowing from an untrusted source (Internet) through a web server (crossing a trust boundary) to trusted internal components. Each arrow represents a data flow and a potential entry point for analysis._

### Step 2: Identify and Analyze Threats

With the system decomposed, you can now systematically identify threats. Several frameworks can guide this process:

- **STRIDE:** Developed by Microsoft, this is the most widely used classification model. It categorizes threats into six types:

  | Threat Type                | Description                                | Security Property Violated |
  | :------------------------- | :----------------------------------------- | :------------------------- |
  | **S**poofing               | Impersonating someone or something else    | Authentication             |
  | **T**ampering              | Modifying data or code                     | Integrity                  |
  | **R**epudiation            | Claiming an action didn't occur            | Non-Repudiation            |
  | **I**nformation Disclosure | Exposing information to unauthorized users | Confidentiality            |
  | **D**enial of Service      | Denying access to valid users              | Availability               |
  | **E**levation of Privilege | Gaining capabilities without authorization | Authorization              |

- **Attack Libraries:** Use pre-defined lists of common attacks, such as the **OWASP Top 10** (e.g., Injection, Broken Authentication) or **CAPEC** (Common Attack Pattern Enumeration and Classification).

**Technique:** Apply the STRIDE model _per element_ in your DFD. For example, ask: "How could an attacker spoof identity at this data flow? How could they tamper with data at this process?"

### Step 3: Mitigate Threats

For each identified threat, determine and document a mitigation strategy.

- **Mitigation Techniques:** Map threats to standard security controls.
  - **Spoofing:** Mitigated by strong authentication (e.g., multi-factor authentication).
  - **Tampering:** Mitigated by integrity controls (e.g., digital signatures, hashes).
  - **Repudiation:** Mitigated by strong logging and audit trails.
  - **Information Disclosure:** Mitigated by encryption (in-transit and at-rest).
  - **Denial of Service:** Mitigated by throttling, rate limiting, and resource management.
  - **Elevation of Privilege:** Mitigated by rigorous authorization checks and the principle of least privilege.

**Prioritization:** Not all threats are created equal. Use a risk rating framework like **DREAD** to prioritize which threats to address first based on their potential **Damage**, **Reproducibility**, **Exploitability**, **Affected users**, and **Discoverability**.

### Step 4: Validate and Document

The final step is to ensure the model is accurate and the findings are properly recorded.

- **Review:** Have the threat model reviewed by other security architects or developers to catch missed threats.
- **Document:** Maintain a living document (often a simple table or a dedicated tool's output) that includes:
  - Threat ID
  - Description
  - Affected Component
  - STRIDE Category
  - Risk Rating (e.g., High/Medium/Low)
  - Mitigation Strategy
  - Owner for mitigation
- **Track:** Integrate the findings into the project's backlog to ensure mitigations are implemented.

## Threat Modeling Methodologies

Several formal methodologies exist beyond the basic four-step process:

- **PASTA:** A seven-stage, risk-centric methodology focused on aligning business objectives with technical requirements.
- **LINDDUN:** Focuses primarily on privacy threats, complementing STRIDE's security focus.
- **Trike:** A methodology focused on risk management and acceptance using a requirements-based approach.
- **VAST:** (Visual, Agile, and Simple Threat Modeling) scales threat modeling across the organization for both infrastructure and software.

## Tools for Threat Modeling

While threat modeling can be done with whiteboards and spreadsheets, dedicated tools can streamline the process.

- **Microsoft Threat Modeling Tool:** A free, STRIDE-based tool that integrates with DFDs and provides automated analysis and reporting.
- **OWASP Threat Dragon:** An open-source, web-based tool that supports both rule-based and manual threat modeling.
- **IriusRisk:** A commercial platform that integrates threat modeling into the CI/CD pipeline.

## Integration with Secure SDLC

Threat modeling is not a one-time activity. It should be integrated into the agile workflow:

- **Sprint 0:** Create an initial threat model for the overall architecture.
- **New Feature/Story:** For any significant new feature or user story, a lightweight threat modeling session should be conducted during grooming or planning.
- **Major Changes:** Revisit the threat model whenever there is a significant change to the architecture or technology stack.

## Example Scenario: Simple Web Login

**1. Decompose:** Assets: User credentials, user data. Entry Point: `/api/login` endpoint. Trust Boundary: Between user's browser (untrusted) and web server (trusted).

**2. Identify Threats (using STRIDE):**

- **Spoofing:** An attacker could brute force or guess passwords.
- **Tampering:** An attacker could modify the login request (e.g., change `isAdmin=false` to `true`).
- **Information Disclosure:** Passwords transmitted in cleartext could be intercepted.
- **Denial of Service:** An attacker could flood the login endpoint with requests.

**3. Mitigate:**

- Enforce strong password policies and implement account lockout.
- Use HTTPS to encrypt the login request, preventing tampering and disclosure.
- Validate and sanitize all input on the server-side.
- Implement rate limiting on the login endpoint.

## Exam Tips

- **Memorize STRIDE:** Be able to recall each letter and what security property it violates. This is a very common exam topic.
- **Understand the "Why":** Be prepared to explain why threat modeling in the design phase is more cost-effective than later stages.
- **Know the Steps:** Be able to list and describe the four fundamental steps of threat modeling (Decompose, Identify, Mitigate, Validate).
- **Differentiate Concepts:** Understand the difference between a threat, a vulnerability, and a risk.
- **Think Practically:** For scenario-based questions, apply the process: identify the entry point, think of a relevant STRIDE category, and suggest a logical mitigation.
