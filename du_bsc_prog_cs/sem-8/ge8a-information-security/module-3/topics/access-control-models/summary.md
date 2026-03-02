# Access Control Models
## Ge8A Information Security - BSc Physical Science (CS), Delhi University (NEP 2024)

### Introduction
Access Control is a fundamental concept in information security that regulates who can access resources within a computer system. It ensures confidentiality, integrity, and availability of data by defining policies for resource access. The three primary models—DAC, MAC, and RBAC—form the backbone of modern security frameworks.

### Key Concepts

- **Subject**: Entity requesting access (users, processes)
- **Object**: Resource being accessed (files, databases, systems)
- **Permission**: Specific rights granted (read, write, execute)
- **Authentication**: Verifying identity of the subject
- **Authorization**: Determining access rights after authentication

### Main Access Control Models

1. **Discretionary Access Control (DAC)**
   - Owner of the resource has full control over permissions
   - Access is granted based on user's identity and ownership
   - Flexible but less secure; users can inadvertently grant unauthorized access
   - Example: File permissions in Windows/Linux

2. **Mandatory Access Control (MAC)**
   - System enforces access based on security labels/clearances
   - Users cannot change permissions; governed by security policies
   - Highly secure, used in military and government applications
   - Based on classification levels (Top Secret, Secret, Confidential, Public)

3. **Role-Based Access Control (RBAC)**
   - Access is assigned based on roles within an organization
   - Users are assigned roles; roles are assigned permissions
   - Simplifies administration; easier to manage than DAC
   - Example: Admin, Manager, Employee roles in enterprise systems

4. **Attribute-Based Access Control (ABAC)**
   - Access decisions based on user attributes, resource attributes, and environmental conditions
   - More dynamic and granular than RBAC
   - Used in cloud computing and modern web applications

### Comparison Table

| Model    | Owner Control | Security Level | Management Complexity |
|----------|---------------|----------------|----------------------|
| DAC      | High          | Low            | Low                  |
| MAC      | None          | High           | High                 |
| RBAC     | Medium        | Medium         | Medium               |

### Conclusion
Understanding access control models is essential for designing secure systems. While DAC offers flexibility, MAC provides maximum security for sensitive environments. RBAC balances both, making it widely adopted in organizations. For exam preparation, remember that Delhi University emphasizes the practical implementation and differences between these models in real-world security scenarios.