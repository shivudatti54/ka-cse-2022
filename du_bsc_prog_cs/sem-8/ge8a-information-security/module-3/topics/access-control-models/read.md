# Access Control Models

## Comprehensive Study Material for Ge8A Information Security

---

## 1. Introduction

**Access Control** is a fundamental concept in information security that determines who can access what resources in a computing environment and what operations they can perform. It serves as the frontline defense mechanism for protecting sensitive information, ensuring confidentiality, integrity, and availability of resources.

### What is Access Control?

Access Control is a security technique that regulates who or what can view or use resources in a computing environment. It is a core component of the CIA triad (Confidentiality, Integrity, Availability) and forms the backbone of most security architectures.

### Real-World Relevance

In today's digital landscape, access control is everywhere:

- **Banking Systems**: ATM machines use access control to ensure only authorized users can access their accounts
- **Healthcare**: Electronic Health Records (EHR) systems use access control to protect patient data under HIPAA regulations
- **Corporate Networks**: Employees access internal systems based on their roles and clearance levels
- **Cloud Services**: Multi-tenant cloud environments rely heavily on access control to isolate user data
- **Social Media**: Privacy settings control who can see your posts and personal information

---

## 2. Types of Access Control Models

### 2.1 Discretionary Access Control (DAC)

**Definition**: Discretionary Access Control is a model where the owner of a resource has full discretion over who can access it. The owner can grant or revoke access permissions at their will.

#### Key Characteristics

- **Owner-centric**: Resource owners control access to their resources
- **Permission-based**: Users are granted explicit permissions to access objects
- **Flexible**: Easy to implement and modify
- **Less secure**: Owners may inadvertently grant excessive permissions

#### How DAC Works

In DAC, each object (file, directory, device) has an Access Control List (ACL) that specifies which subjects (users, groups) can perform which operations. When a user requests access to a resource, the system checks the ACL to determine whether to grant or deny access.

#### Example: Linux File Permissions

```python
# Understanding DAC in Linux

# In Linux, every file has:
# 1. Owner (user)
# 2. Group
# 3. Permissions for Owner, Group, and Others

# Permission types:
# r = read (4)
# w = write (2)
# x = execute (1)

# Example: chmod 755 file.txt
# Owner: rwx (7 = 4+2+1)
# Group: r-x (5 = 4+0+1)
# Others: r-x (5 = 4+0+1)

# This DAC implementation shows owner has full control
# and can modify permissions using chmod command

class DACPermission:
    def __init__(self, owner, group, permissions):
        self.owner = owner
        self.group = group
        self.permissions = permissions  # Format: "rwxr-x---"
    
    def check_access(self, user, operation):
        """Check if user has required permission"""
        # Simplified DAC logic
        if user == self.owner:
            return self.permissions[1] == 'r' if operation == 'read' else self.permissions[2] == 'w'
        elif user in self.group:
            return self.permissions[4] == 'r' if operation == 'read' else self.permissions[5] == 'w'
        else:
            return self.permissions[7] == 'r' if operation == 'read' else self.permissions[8] == 'w'

# Example usage
file_perm = DACPermission("alice", "developers", "rwxr-x---")
print(file_perm.check_access("alice", "read"))  # True
print(file_perm.check_access("bob", "write"))   # False (not owner, not in group)
```

#### Advantages and Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| Simple to implement | Less secure (relies on owner judgment) |
| Flexible and adaptable | Difficult to enforce organizational policies |
| User-friendly | Permission creep risk |
| Low overhead | No centralized control |

---

### 2.2 Mandatory Access Control (MAC)

**Definition**: Mandatory Access Control is a strict model where the operating system enforces access control based on security labels (classification levels). Users cannot override or modify these controls.

#### Key Characteristics

- **System-enforced**: The OS enforces access rules; users have no control
- **Label-based**: Every subject and object has a security label
- **Hierarchical**: Security levels are typically hierarchical (Top Secret > Secret > Confidential > Unclassified)
- **Most secure**: Provides strong protection for sensitive data

#### Security Labels

In MAC, every subject (user, process) and object (file, device) is assigned a **security label** consisting of:

1. **Classification Level**: Hierarchical ranking (e.g., Top Secret, Secret, Confidential, Unclassified)
2. **Categories**: Non-hierarchical compartments (e.g., Nuclear, Army, Navy)

#### The Bell-LaPadula Model

The Bell-LaPadula model is the foundational model for Mandatory Access Control, focusing on **confidentiality**. It was developed by the US Department of Defense in the 1970s.

##### Core Principles (Simple Security Property and *-Property)

1. **Simple Security Property (No Read Up)**: A subject can only read objects at or below their security clearance level.
   - A "Secret" clearance user cannot read "Top Secret" documents
   
2. **Star Property (No Write Down)**: A subject can only write to objects at or above their security clearance level.
   - A "Secret" clearance user can only write to "Secret" or "Top Secret" files
   - This prevents leaking sensitive information to lower clearance levels

3. **Strong Star Property (No Read/Write Down)**: A subject can simultaneously read and write only to objects at the same security level.

##### Bell-LaPadula Formal Definitions

```
Simple Security Property:
    A subject s can read object o iff:
    1. s dominates o (clearance(s) ≥ classification(o)), OR
    2. o is in the "read" mode access

Star Property:
    A subject s can write to object o iff:
    1. o dominates s (classification(o) ≥ clearance(s)), OR
    2. o is in the "write" mode access
```

#### Example: Government Classification System

```python
# Bell-LaPadula Model Implementation

from enum import IntEnum

class SecurityLevel(IntEnum):
    UNCLASSIFIED = 0
    CONFIDENTIAL = 1
    SECRET = 2
    TOP_SECRET = 3

class Category:
    """Categories (compartments) for MAC"""
    def __init__(self, categories):
        self.categories = set(categories)
    
    def dominates(self, other):
        """Category A dominates Category B if A contains all categories in B"""
        return other.categories.issubset(self.categories)

class SecurityLabel:
    """Security label for Bell-LaPadula model"""
    def __init__(self, level, categories):
        self.level = SecurityLevel(level)
        self.category = Category(categories)
    
    def dominates(self, other):
        """Label A dominates Label B if A's level >= B's level 
        AND A's categories dominate B's categories"""
        return (self.level >= other.level and 
                self.category.dominates(other.category))

class Subject:
    """Subject (user/process) with security clearance"""
    def __init__(self, name, security_label):
        self.name = name
        self.security_label = security_label
    
    def can_read(self, obj):
        """Bell-LaPadula: No Read Up - subject can read objects at or below their level"""
        # Check if object's label is dominated by subject's label
        return self.security_label.dominates(obj.security_label)
    
    def can_write(self, obj):
        """Bell-LaPadula: No Write Down - subject can write to objects at or above their level"""
        # Subject can only write to objects that dominate (or equal) subject's level
        return obj.security_label.dominates(self.security_label)

class Object:
    """Object (file/resource) with security classification"""
    def __init__(self, name, security_label):
        self.name = name
        self.security_label = security_label

# Example Scenario
if __name__ == "__main__":
    # Create users with different clearance levels
    alice = Subject("Alice", SecurityLabel(SecurityLevel.TOP_SECRET, ["Nuclear", "Army"]))
    bob = Subject("Bob", SecurityLabel(SecurityLevel.SECRET, ["Army"]))
    charlie = Subject("Charlie", SecurityLabel(SecurityLevel.CONFIDENTIAL, ["Navy"]))
    
    # Create classified documents
    doc1 = Object("Nuclear_Code", SecurityLabel(SecurityLevel.TOP_SECRET, ["Nuclear"]))
    doc2 = Object("Army_Report", SecurityLabel(SecurityLevel.SECRET, ["Army"]))
    doc3 = Object("Navy_Report", SecurityLabel(SecurityLevel.CONFIDENTIAL, ["Navy"]))
    
    # Test Bell-LaPadula rules
    print("=== Bell-LaPadula Model Tests ===")
    print(f"Alice (Top Secret) reading Nuclear Code: {alice.can_read(doc1)}")  # True
    print(f"Alice (Top Secret) reading Army Report: {alice.can_read(doc2)}")    # True (dominates)
    print(f"Alice (Top Secret) writing to Navy Report: {alice.can_write(doc3)}") # False (write down)
    
    print(f"\nBob (Secret) reading Nuclear Code: {bob.can_read(doc1)}")  # False (read up)
    print(f"Bob (Secret) reading Army Report: {bob.can_read(doc2)}")    # True
    print(f"Bob (Secret) writing to Army Report: {bob.can_write(doc2)}") # True
```

#### Advantages and Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| Very high security | Complex to implement |
| Centralized control | Inflexible |
| Prevents data leakage | Performance overhead |
| Suitable for military/government | Difficult for general business use |

---

### 2.3 Role-Based Access Control (RBAC)

**Definition**: Role-Based Access Control is a model where access permissions are assigned to roles rather than individual users. Users are then assigned to roles based on their job responsibilities.

#### Key Characteristics

- **Role-centric**: Permissions are associated with roles, not individual users
- **Job-function based**: Roles reflect organizational job functions
- **Simplified administration**: Easy to manage through role assignment
- **Supports principle of least privilege**: Users get minimum permissions needed

#### RBAC Terminology

- **Role**: A collection of permissions (e.g., Manager, Employee, Admin)
- **Permission**: An authorization to perform a specific operation
- **User**: An individual who is assigned to roles
- **Session**: A mapping of a user to one or more activated roles

#### How RBAC Works

```
User → Role Assignment → Permissions
                    ↓
            Role Permissions
                    ↓
            Access to Resources
```

#### Example: Corporate RBAC Implementation

```python
# Role-Based Access Control (RBAC) Implementation

from collections import defaultdict

class Permission:
    def __init__(self, resource, action):
        self.resource = resource
        self.action = action  # read, write, delete, execute
    
    def __str__(self):
        return f"{self.action}:{self.resource}"
    
    def __eq__(self, other):
        return self.resource == other.resource and self.action == other.action
    
    def __hash__(self):
        return hash((self.resource, self.action))

class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = set()
    
    def add_permission(self, permission):
        self.permissions.add(permission)
    
    def remove_permission(self, permission):
        self.permissions.discard(permission)
    
    def has_permission(self, resource, action):
        return Permission(resource, action) in self.permissions

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.roles = set()
    
    def assign_role(self, role):
        self.roles.add(role)
    
    def revoke_role(self, role):
        self.roles.discard(role)
    
    def has_permission(self, resource, action):
        """Check if user has permission through any of their roles"""
        for role in self.roles:
            if role.has_permission(resource, action):
                return True
        return False

class RBACSystem:
    def __init__(self):
        self.roles = {}
        self.users = {}
    
    def create_role(self, role_name):
        role = Role(role_name)
        self.roles[role_name] = role
        return role
    
    def create_user(self, user_id, name):
        user = User(user_id, name)
        self.users[user_id] = user
        return user
    
    def grant_permission(self, role_name, resource, action):
        if role_name in self.roles:
            self.roles[role_name].add_permission(Permission(resource, action))
    
    def assign_role(self, user_id, role_name):
        if user_id in self.users and role_name in self.roles:
            self.users[user_id].assign_role(self.roles[role_name])
    
    def check_access(self, user_id, resource, action):
        if user_id in self.users:
            return self.users[user_id].has_permission(resource, action)
        return False

# Example: University Management System
if __name__ == "__main__":
    rbac = RBACSystem()
    
    # Create roles
    admin = rbac.create_role("Admin")
    professor = rbac.create_role("Professor")
    student = rbac.create_role("Student")
    
    # Define permissions for each role
    # Admin: Full access to all resources
    rbac.grant_permission("Admin", "student_records", "read")
    rbac.grant_permission("Admin", "student_records", "write")
    rbac.grant_permission("Admin", "student_records", "delete")
    rbac.grant_permission("Admin", "grades", "read")
    rbac.grant_permission("Admin", "grades", "write")
    
    # Professor: Can read/write grades, read student records
    rbac.grant_permission("Professor", "grades", "read")
    rbac.grant_permission("Professor", "grades", "write")
    rbac.grant_permission("Professor", "student_records", "read")
    
    # Student: Can only read their own grades
    rbac.grant_permission("Student", "my_grades", "read")
    
    # Create users
    alice = rbac.create_user("U001", "Alice")  # Admin
    bob = rbac.create_user("U002", "Bob")      # Professor
    charlie = rbac.create_user("U003", "Charlie")  # Student
    
    # Assign roles
    rbac.assign_role("U001", "Admin")
    rbac.assign_role("U002", "Professor")
    rbac.assign_role("U003", "Student")
    
    # Test access
    print("=== RBAC Access Control Tests ===")
    print(f"Alice (Admin) can delete student records: {rbac.check_access('U001', 'student_records', 'delete')}")  # True
    print(f"Bob (Professor) can write grades: {rbac.check_access('U002', 'grades', 'write')}")  # True
    print(f"Charlie (Student) can read all student records: {rbac.check_access('U003', 'student_records', 'read')}")  # False
    print(f"Charlie (Student) can read own grades: {rbac.check_access('U003', 'my_grades', 'read')}")  # True
```

#### RBAC vs. DAC/MAC

| Feature | DAC | MAC | RBAC |
|---------|-----|-----|------|
| Assignment | Owner-based | System-enforced | Role-based |
| Flexibility | High | Very Low | Medium-High |
| Security Level | Low | Very High | Medium |
| Complexity | Low | Very High | Medium |
| Use Case | General computing | Military/Government | Enterprise applications |

---

### 2.4 Attribute-Based Access Control (ABAC)

**Definition**: Attribute-Based Access Control is an advanced model where access decisions are based on attributes of the subject, resource, action, and environment. It provides fine-grained access control using policies.

#### Key Characteristics

- **Attribute-based**: Uses attributes rather than roles
- **Policy-driven**: Access decisions based on defined policies
- **Very fine-grained**: Can control access at attribute level
- **Dynamic**: Can consider environmental conditions
- **Flexible**: Highly customizable

#### ABAC Attributes

1. **Subject Attributes**: User ID, role, department, clearance level, location
2. **Resource Attributes**: File type, classification, owner, creation date
3. **Action Attributes**: Read, write, delete, execute
4. **Environment Attributes**: Time, location, device type, network security level

#### ABAC Policy Example

```
PERMIT access IF:
    Subject.department = "Finance" AND
    Resource.type = "Financial Document" AND
    Resource.classification ≤ Subject.clearance AND
    Environment.time BETWEEN "09:00" AND "17:00" AND
    Environment.location = "Office"
```

#### Example: ABAC Implementation

```python
# Attribute-Based Access Control (ABAC) Implementation

from datetime import datetime, time
from typing import Dict, Any

class ABACPolicy:
    def __init__(self, name, conditions):
        self.name = name
        self.conditions = conditions
    
    def evaluate(self, subject_attrs, resource_attrs, action, env_attrs):
        """Evaluate if policy grants access"""
        for condition in self.conditions:
            if not condition(subject_attrs, resource_attrs, action, env_attrs):
                return False
        return True

class ABACSystem:
    def __init__(self):
        self.policies = []
    
    def add_policy(self, policy):
        self.policies.append(policy)
    
    def check_access(self, subject_attrs, resource_attrs, action, env_attrs):
        """Check access based on all policies"""
        for policy in self.policies:
            if policy.evaluate(subject_attrs, resource_attrs, action, env_attrs):
                return True
        return False

# Define common conditions
def subject_has_role(role_name):
    return lambda s, r, a, e: s.get('role') == role_name

def subject_in_department(dept):
    return lambda s, r, a, e: s.get('department') == dept

def resource_has_type(res_type):
    return lambda s, r, a, e: r.get('type') == res_type

def resource_classification_below_or_equal(max_class):
    return lambda s, r, a, e: r.get('classification', 0) <= max_class

def action_equals(req_action):
    return lambda s, r, a, e: a == req_action

def environment_during_hours(start, end):
    def check(s, r, a, e):
        current_time = e.get('current_time', time(12, 0))
        return start <= current_time <= end
    return check

def environment_from_office():
    return lambda s, r, a, e: e.get('location') == 'Office'

# Example: Healthcare ABAC System
if __name__ == "__main__":
    abac = ABACSystem()
    
    # Policy 1: Doctors can read patient records during working hours
    doctor_read_policy = ABACPolicy(
        "Doctor Read Access",
        [
            subject_has_role('Doctor'),
            action_equals('read'),
            resource_has_type('patient_record'),
            resource_classification_below_or_equal(3),
            environment_during_hours(time(6, 0), time(22, 0))
        ]
    )
    abac.add_policy(doctor_read_policy)
    
    # Policy 2: Nurses can read patient records anytime from hospital
    nurse_read_policy = ABACPolicy(
        "Nurse Read Access",
        [
            subject_has_role('Nurse'),
            action_equals('read'),
            resource_has_type('patient_record'),
            resource_classification_below_or_equal(2),
        ]
    )
    abac.add_policy(nurse_read_policy)
    
    # Policy 3: Admin can write any record during office hours
    admin_write_policy = ABACPolicy(
        "Admin Write Access",
        [
            subject_has_role('Admin'),
            action_equals('write'),
            environment_during_hours(time(9, 0), time(17, 0)),
            environment_from_office()
        ]
    )
    abac.add_policy(admin_write_policy)
    
    # Test scenarios
    print("=== ABAC Access Control Tests ===")
    
    # Scenario 1: Dr. Smith reading patient record
    doctor_attrs = {'role': 'Doctor', 'department': 'Cardiology', 'id': 'D001'}
    record_attrs = {'type': 'patient_record', 'classification': 2, 'owner': 'Hospital'}
    env_attrs = {'current_time': time(10, 0), 'location': 'Hospital'}
    
    print(f"Dr. Smith reading patient record at 10 AM: {abac.check_access(doctor_attrs, record_attrs, 'read', env_attrs)}")
    
    # Scenario 2: Same doctor at 3 AM
    night_env = {'current_time': time(3, 0), 'location': 'Hospital'}
    print(f"Dr. Smith reading patient record at 3 AM: {abac.check_access(doctor_attrs, record_attrs, 'read', night_env)}")
    
    # Scenario 3: Nurse reading high-classification record
    nurse_attrs = {'role': 'Nurse', 'department': 'Emergency', 'id': 'N001'}
    high_class_record = {'type': 'patient_record', 'classification': 4}
    print(f"Nurse reading top-secret record: {abac.check_access(nurse_attrs, high_class_record, 'read', env_attrs)}")
    
    # Scenario 4: Admin writing from home
    admin_attrs = {'role': 'Admin', 'department': 'IT', 'id': 'A001'}
    home_env = {'current_time': time(14, 0), 'location': 'Home'}
    print(f"Admin writing from home: {abac.check_access(admin_attrs, record_attrs, 'write', home_env)}")
```

#### ABAC vs. RBAC

| Feature | RBAC | ABAC |
|---------|------|------|
| Granularity | Role-level | Attribute-level |
| Flexibility | Moderate | Very High |
| Complexity | Lower | Higher |
| Policy Management | Role-based | Attribute-based |
| Context Awareness | Limited | Full |
| Use Case | Enterprise | Cloud, IoT, Complex systems |

---

## 3. Comparison of Access Control Models

| Aspect | DAC | MAC | RBAC | ABAC |
|--------|-----|-----|------|------|
| **Control Basis** | Owner discretion | System enforcement | Job roles | Multiple attributes |
| **Security Level** | Low | Very High | Medium | High |
| **Complexity** | Low | Very High | Medium | High |
| **Flexibility** | High | Very Low | Medium | Very High |
| **Administration** | Distributed | Centralized | Role-based | Policy-based |
| **Example OS** | Windows, Linux | SE Linux, Trusted Solaris | Oracle DB, SAP | AWS IAM, Azure AD |
| **Best For** | General users | Military/Government | Organizations | Cloud/Web services |

---

## 4. Delhi University Syllabus Context

This topic aligns with **Ge8A Information Security** (BSc Physical Science CS - NEP 2024). Students should understand:

1. **Fundamental concepts** of access control as covered in Module 3/4 of most information security syllabi
2. **Difference between DAC, MAC, RBAC, and ABAC** - this is typically a 5-10 mark question in university exams
3. **Bell-LaPadula model** - crucial for understanding confidentiality in MAC
4. **Practical implementation** - code examples help understand real-world applications

---

## 5. Practice Questions (MCQs)

### Multiple Choice Questions

**Q1. In the Bell-LaPadula model, the "Simple Security Property" states that:**
- a) A subject can write to objects at a lower security level
- b) A subject can read objects at a higher security level
- c) A subject can only read objects at or below their security clearance level
- d) A subject can read and write at any security level

**Q2. Which access control model is best suited for military applications requiring high confidentiality?**
- a) DAC
- b) MAC
- c) RBAC
- d) ABAC

**Q3. In RBAC, permissions are assigned to:**
- a) Individual users
- b) Roles
- c) Objects
- d) Resources

**Q4. The "Star Property" in Bell-LaPadula model is also known as:**
- a) No Read Up
- b) No Write Down
- c) No Read Down
- d) No Write Up

**Q5. Which model uses security labels for enforcing access control?**
- a) DAC
- b) RBAC
- c) MAC
- d) ABAC

**Q6. In ABAC, which of the following is NOT typically used as an attribute?**
- a) User department
- b) Time of access
- c) User password
- d) Resource type

**Q7. DAC stands for:**
- a) Direct Access Control
- b) Discretionary Access Control
- c) Dynamic Access Control
- d) Distributed Access Control

**Q8. Which access control model is most flexible and fine-grained?**
- a) DAC
- b) MAC
- c) RBAC
- d) ABAC

**Q9. In RBAC, a user can be assigned:**
- a) Only one role
- b) Multiple roles
- c) No role
- d) Only system roles

**Q10. The principle of least privilege is best enforced by:**
- a) DAC
- b) MAC
- c) RBAC
- d) All of the above

### Answer Key
1. (c) 2. (b) 3. (b) 4. (b) 5. (c) 6. (c) 7. (b) 8. (d) 9. (b) 10. (c)

---

## 6. Flashcards for Quick Revision

### Term Definitions

| Term | Definition |
|------|------------|
| **Access Control** | Security technique that regulates who can view or use resources |
| **DAC** | Access control model where resource owners determine who can access their resources |
| **MAC** | Strict access control model enforced by the system based on security labels |
| **RBAC** | Access control model where permissions are assigned to roles, not users |
| **ABAC** | Access control model that makes decisions based on multiple attributes |
| **Security Label** | In MAC, a classification level and category assigned to subjects and objects |
| **Bell-LaPadula Model** | A formal model for MAC focusing on confidentiality with "No Read Up" and "No Write Down" rules |
| **Simple Security Property** | "No Read Up" rule - subjects can only read objects at or below their clearance |
| **Star Property** | "No Write Down" rule - subjects can only write to objects at or above their clearance |
| **ACL** | Access Control List - specifies which subjects can access which objects |
| **Role** | In RBAC, a collection of permissions associated with a job function |
| **Principle of Least Privilege** | Users should have minimum permissions needed to perform their job |

### Key Points Summary

- **DAC**: Owner controls; flexible but less secure
- **MAC**: System enforces; uses security labels; highest security
- **RBAC**: Role-based; simplifies administration; best for organizations
- **ABAC**: Attribute-based; most flexible; used in cloud environments

---

## 7. Key Takeaways

1. **Access Control is Fundamental**: It is the cornerstone of information security, determining who can access what resources.

2. **Four Major Models**:
   - **DAC**: Owner-driven, flexible, but less secure
   - **MAC**: System-enforced, uses security labels, highest security for sensitive applications
   - **RBAC**: Role-based, simplifies administration, best for enterprises
   - **ABAC**: Attribute-based, most flexible, ideal for cloud and complex environments

3. **Bell-LaPadula Model** is crucial for understanding MAC:
   - **Simple Security Property**: No Read Up (subjects can only read objects at or below their clearance)
   - **Star Property**: No Write Down (subjects can only write to objects at or above their clearance)
   - This model focuses primarily on **confidentiality**

4. **Choice Depends on Requirements**:
   - Use DAC for general-purpose systems
   - Use MAC for military/government applications
   - Use RBAC for organizational systems
   - Use ABAC for cloud services and IoT

5. **Real-World Applications**: These models are used in operating systems (Linux file permissions), databases, cloud platforms (AWS IAM), healthcare systems, and government classified systems.

6. **For Delhi University Exam**: Focus on understanding differences between models, Bell-LaPadula rules, and being able to explain each model with examples.

---

*Generated for BSc Physical Science (CS) - Ge8A Information Security, NEP 2024*