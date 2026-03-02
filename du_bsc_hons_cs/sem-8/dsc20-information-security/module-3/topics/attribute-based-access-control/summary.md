# Attribute-Based Access Control (ABAC) - Summary

## Key Definitions and Concepts

- **ABAC (Attribute-Based Access Control)**: An access control methodology where authorization is determined by evaluating attributes associated with the subject, object, action, and environment conditions—allowing dynamic, context-aware access decisions.

- **Subject Attributes**: Characteristics of the requesting entity (user ID, role, department, clearance level, location, employment status)

- **Resource Attributes**: Properties of the object being accessed (file classification, owner, data sensitivity, type, metadata)

- **Action Attributes**: The operation being requested (read, write, delete, execute, download)

- **Environment Attributes**: Contextual conditions (time, IP address, device type, network security, threat level)

- **XACML**: eXtensible Access Control Markup Language—the standard XML language for expressing ABAC policies

## Important Formulas and Theorems

- **ABAC Policy Structure**: IF (subject.attributes AND resource.attributes AND action.attributes AND environment.attributes match conditions) THEN (PERMIT/DENY)

- **RBAC as ABAC Subset**: RBAC can be implemented in ABAC by treating "role" as a subject attribute—demonstrating ABAC's expressive power

- **Policy Combining Algorithms**: Multiple policies are evaluated using algorithms like "deny-overrides," "permit-overrides," or "first-applicable"

## Key Points

1. ABAC provides **fine-grained, dynamic access control** compared to role-based static permissions

2. The four pillars of ABAC are **subject, resource, action, and environment attributes**—all must be evaluated for access decisions

3. ABAC **subsumes** DAC, MAC, and RBAC—these can be expressed as special cases within the ABAC framework

4. **Environment attributes** distinguish ABAC from earlier models—enabling time-based, location-based, and device-aware access

5. **XACML** is the industry-standard language for writing ABAC policies and managing request/response protocols

6. ABAC is essential for **cloud computing, IoT, federated identity, and multi-tenant systems** where context varies dynamically

7. Common **real-world implementations** include AWS IAM policies, Azure ABAC, and healthcare EHR systems

8. **Policy management** is critical—conflicting policies can lead to security vulnerabilities; organizations use deny-by-default approaches

## Common Mistakes to Avoid

- Confusing RBAC and ABAC: RBAC uses static role assignments; ABAC evaluates dynamic attributes in real-time

- Forgetting environment attributes: Many students focus only on subject and resource attributes, missing the contextual dimension

- Overlooking policy conflicts: Multiple policies may give conflicting decisions; understanding combining algorithms is essential

- Assuming ABAC is always better: For simple systems, RBAC may be more practical—ABAC introduces complexity that requires proper infrastructure

## Revision Tips

1. Create a comparison table of DAC, MAC, RBAC, and ABAC with columns for granularity, flexibility, administration complexity, and use cases

2. Practice writing ABAC policy statements in both natural language and pseudo-code for common scenarios

3. Remember that "environment" is what makes ABAC uniquely powerful—always consider time, location, and device context

4. Study XACML structure: Target (what requests), Rule (condition + effect), Policy (multiple rules), PolicySet (multiple policies)

5. Connect to exam questions: Be ready to explain why a hospital or bank would choose ABAC over RBAC