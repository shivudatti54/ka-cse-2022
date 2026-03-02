# Discretionary Role-Based Access Control (DRBAC)

## Introduction

Access Control is the cornerstone of information security, forming the first line of defense in protecting sensitive data and system resources from unauthorized access. In the context of enterprise information systems, particularly those handling confidential or personal data, implementing robust access control mechanisms is not merely a technical requirement but a legal and ethical obligation. The University of Delhi's Computer Science curriculum recognizes this importance, dedicating significant attention to understanding various access control models that form the backbone of secure computing environments.

Discretionary Role-Based Access Control (DRBAC) represents a sophisticated hybrid approach that combines the flexibility of discretionary access control with the administrative efficiency of role-based systems. Unlike traditional models where access decisions rest solely with owners (discretionary) or are enforced by the system based on security labels (mandatory), DRBAC introduces a middle ground where administrators can define roles and permissions while still allowing certain discretionary privileges to role holders. This model has gained significant traction in modern organizations because it balances security requirements with operational flexibility, making it particularly suitable for dynamic business environments where job responsibilities change frequently and the principle of least privilege must be maintained.

Understanding DRBAC is essential for computer science students because it reflects real-world access control implementations in organizations ranging from healthcare systems (handling Patient Health Information under HIPAA) to banking systems (protecting customer financial data) to university administration systems (managing student records). The model's relevance extends to cloud computing environments, enterprise resource planning systems, and government applications, making it a critical topic for professional practice in India's rapidly digitizing economy.

## Key Concepts

### Fundamentals of Access Control

Access Control encompasses three fundamental elements: subjects, objects, and permissions. **Subjects** are active entities that request access to resources—typically users, processes, or programs running on behalf of users. **Objects** (or resources) are passive entities containing or receiving information, including files, databases, directories, printers, and network services. **Permissions** (or privileges) define the type of access a subject can have to an object, commonly categorized as read, write, execute, delete, or create.

The access control process involves three core functions: identification (presenting a claimed identity), authentication (verifying that identity), and authorization (determining what an authenticated user can do). DRBAC specifically addresses the authorization phase, determining access rights based on roles rather than individual identities or mandatory security classifications.

### Discretionary Access Control (DAC)

Discretionary Access Control is a model where the owner of a resource has complete control over who can access it and what they can do with it. The term "discretionary" refers to the owner's discretion in granting, revoking, or transferring access rights. In DAC systems, each object has an owner (typically the creator), and only the owner can specify access policies for that object.

DAC provides flexibility and intuitive ownership semantics but has significant limitations in large organizations. The owner-centric model makes it difficult to enforce consistent security policies across the enterprise. Additionally, when employees leave or change positions, access rights may not be properly revoked, creating security gaps. The propagation of access rights (when an authorized user shares access with others) makes it challenging to maintain the principle of least privilege.

### Role-Based Access Control (RBAC)

Role-Based Access Control (RBAC) shifts the focus from individual users to organizational roles. In RBAC, permissions are associated with roles rather than individual users. Users are assigned to roles based on their job functions, and roles are granted permissions based on the principle of least privilege—giving only the minimum access necessary to perform job duties.

RBAC offers several administrative advantages: simplified permission management (permissions change only when role responsibilities change), easy auditing (what can a role do?), support for separation of duties (preventing fraud by requiring multiple roles for sensitive operations), and reduced administrative overhead in large organizations. The widely cited RBAC96 model by Sandhu et al. defines four components: core RBAC, role hierarchies, static separation of duties, and dynamic separation of duties.

### Discretionary Role-Based Access Control (DRBAC)

DRBAC extends traditional RBAC by incorporating discretionary elements that allow role holders to exercise some discretion in access decisions. This hybrid approach addresses scenarios where strict role-based permissions are too rigid for certain business processes while maintaining the organizational structure benefits of RBAC.

In DRBAC, role holders may have the discretion to:
- Grant limited access to subordinates or colleagues based on need
- Delegate specific tasks without administrative intervention
- Temporarily share access during absences
- Make exceptions for emergency situations

For example, in a hospital information system, a senior doctor (holding the "Senior Doctor" role) might have discretion to grant temporary read access to a patient's records to a medical student assisting in treatment. Similarly, in a corporate environment, a project manager might delegate certain document access to team members for the duration of a project.

### Role Hierarchy and Permission Inheritance

Role hierarchies in DRBAC establish parent-child relationships between roles, where child roles inherit permissions from parent roles. This creates a natural structure reflecting organizational reporting relationships—a "Team Leader" role might inherit all permissions of "Team Member" plus additional permissions for approval and supervision.

However, DRBAC introduces constraints on this inheritance to maintain security. Not all permissions are automatically inherited; sensitive permissions require explicit assignment. Administrators can define which permissions are inheritable and which require explicit discretionary grants, preventing excessive privilege accumulation.

### Separation of Duties

Separation of Duties (SoD) is a fundamental security principle that prevents any single individual from having enough authority to complete a critical transaction alone. DRBAC implements SoD through two mechanisms:

**Static Separation of Duties (SSoD):** Specifies that a user cannot be assigned to certain mutually exclusive roles simultaneously. For example, in a financial system, the same person cannot hold both the "Accounts Payable" and "Accounts Receivable" roles to prevent embezzlement.

**Dynamic Separation of Duties (DSSoD):** Allows a user to be authorized for multiple roles but restricts them from exercising all roles simultaneously in a single session. A user might have both "Purchase Requestor" and "Purchase Approver" roles but must activate only one at a time, with the system logging which role is active.

## Examples

### Example 1: University Examination System

Consider a University Examination Management System with the following DRBAC structure:

**Roles Defined:**
- Examination Controller (highest authority)
- Head Examiner (manages specific exams)
- Invigilator (conducts exams)
- Faculty Member (evaluates answer scripts)
- Student (views results)

**Scenario:** Dr. Sharma, holding the "Head Examiner" role for the Computer Science end-semester examination, needs to delegate script evaluation to Prof. Mehta (who already has the "Faculty Member" role) and Prof. Khan (another "Faculty Member").

**Discretionary Action:** Dr. Sharma uses her discretionary privilege to assign Prof. Mehta and Prof. Khan to the specific question paper evaluation task. The system records:
- Delegator: Dr. Sharma (Head Examiner role)
- Delegatees: Prof. Mehta, Prof. Khan
- Permission: Evaluate Answer Scripts (specific to Paper CS-401)
- Duration: 7 days (until evaluation deadline)
- Constraint: Read-only access to answer scripts

This demonstrates how DRBAC allows task-specific delegation while maintaining role-based structure.

### Example 2: Healthcare Information System

In a multi-specialty hospital, the "Senior Resident" role has discretionary privileges to grant emergency access:

**Role Permissions (standard):**
- Read patient records (all departments)
- Write to patient records (own department)

**Discretionary Permissions:**
- Grant emergency read access to any patient record (for 24 hours)
- Must document reason for access in audit log

**Scenario:** A patient in the Emergency Ward requires consultation from a Cardiology Senior Resident. The ER Senior Resident uses discretionary privilege to grant the Cardiology resident temporary read access to the emergency case file. The system logs:
- Access granted by: ER-SR-001
- Access granted to: Cardio-SR-003
- Patient ID: P-2024-1847
- Reason: "Emergency cardiac consultation required"
- Auto-expire: 24 hours

This example illustrates DRBAC balancing security (time-limited, logged access) with operational flexibility (enabling emergency care).

### Example 3: Banking Transaction System

A modern banking core banking system implements DRBAC for transaction approval workflows:

**Roles:**
- Relationship Manager (RM)
- Branch Manager (BM)
- Credit Officer (CO)
- Compliance Officer (Compliance)

**Scenario:** A loan application requires approval based on amount:

| Transaction Value | Required Roles |
|-------------------|----------------|
| Up to ₹5 lakhs | Credit Officer alone |
| ₹5-50 lakhs | Credit Officer + Branch Manager |
| Above ₹50 lakhs | Credit Officer + Branch Manager + Compliance Officer |

The DRBAC implementation enforces SSoD—the same person cannot be both Credit Officer and Branch Manager. For transactions above ₹50 lakhs, the system enforces DSSoD, requiring the BM and Compliance Officer to be different individuals logging in from different terminals.

**Discretionary Element:** The Branch Manager can use discretionary privilege to temporarily elevate a Senior Credit Officer's limit to ₹75 lakhs for a specific high-value priority customer, but this requires:
- Written justification
- Automatic notification to Compliance
- Audit trail creation
- Auto-revocation after 48 hours

## Exam Tips

1. **Understand the Distinction:** Clearly differentiate between DAC (owner-controlled), MAC (system-controlled based on classifications), and RBAC (role-controlled). DRBAC is a hybrid combining RBAC structure with discretionary elements.

2. **Know the Core Components:** Remember the RBAC96 model components—core RBAC, role hierarchies, static SoD, and dynamic SoD. These are frequently tested in DU examinations.

3. **Principle of Least Privilege:** This is fundamental to RBAC and DRBAC—always emphasize that users should have only the minimum access necessary to perform their job functions.

4. **Administrative vs. Discretionary Permissions:** In DRBAC, distinguish between administrative permissions (managed by administrators) and discretionary permissions (exercised by role holders within defined bounds).

5. **Separation of Duties Examples:** Be prepared to give examples of SSoD and DSSoD in real systems—the purchase/approval example is particularly common in exams.

6. **Advantages Over Traditional Models:** DRBAC offers simplified administration, better scalability, easier compliance auditing, and supports least privilege more effectively than pure DAC.

7. **Audit and Accountability:** Remember that DRBAC systems maintain comprehensive audit logs—every discretionary access grant must be logged with timestamp, grantor, grantee, reason, and expiration.

8. **Current Relevance:** Connect the topic to contemporary applications—cloud computing, microservices architecture, and zero-trust security models all rely on access control principles.