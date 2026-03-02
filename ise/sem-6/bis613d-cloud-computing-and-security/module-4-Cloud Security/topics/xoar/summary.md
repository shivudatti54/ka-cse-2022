# XOAR: Self-Protecting Software

XOAR (eXecuting with Orchestrated Autonomous Resilience) is a self-protecting software approach that addresses security weaknesses in monolithic server applications by decomposing them into smaller, isolated compartments running with minimal privileges. Traditional monolithic applications have large attack surfaces, run with excessive privileges, lack internal isolation, and are difficult to patch, meaning a single vulnerability can compromise the entire application.

XOAR applies privilege separation by breaking applications into multiple compartments (HTTP parser, CGI engine, SSL/TLS handler, logger, config manager), each running as a separate process with its own address space and restricted privileges. The principle of least privilege ensures each compartment receives only the minimum permissions required for its function. Key components include a Compartment Manager orchestrating the decomposed application, a Policy Engine defining access control and communication policies, and Inter-Compartment Communication channels using message passing and controlled system calls. This architecture reduces blast radius so compromising one compartment doesn't grant access to the entire application.

## Key Takeaways

- XOAR decomposes monolithic applications into isolated, least-privilege compartments to limit breach impact
- Core principles are privilege separation (decomposition) and least privilege (minimum permissions)
- Compromising one compartment cannot access capabilities belonging to other isolated compartments
- XOAR provides application-level defense in depth complementing VM, OS, and network security
