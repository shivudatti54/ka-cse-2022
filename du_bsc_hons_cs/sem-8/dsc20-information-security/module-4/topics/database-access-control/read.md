# Database Access Control

## Introduction

Database Access Control is a fundamental pillar of information security that governs who can access what data within a database system and what operations they can perform. In an era where organizations handle massive amounts of sensitive data—from customer information to financial records and intellectual property—implementing robust access control mechanisms is not merely a best practice but a legal and ethical necessity. The University of Delhi's Computer Science curriculum recognizes this importance, equipping students with comprehensive knowledge of access control models, implementation strategies, and security best practices.

Database access control operates at the intersection of authentication, authorization, and auditing. While authentication verifies the identity of users attempting to connect to the database, authorization determines what permissions they receive once authenticated. This separation of concerns ensures that even authenticated users cannot access data beyond their authorized scope. For instance, a customer service representative at a bank may be authenticated to the database system but authorized only to view customer account balances—not to modify them or access transaction histories of other customers.

The evolution of database access control reflects the broader trajectory of information security—from simple username-password combinations to sophisticated multi-layered security frameworks. Modern database management systems (DBMS) like Oracle, PostgreSQL, MySQL, and SQL Server incorporate robust access control mechanisms that security professionals must thoroughly understand to protect organizational assets effectively.

## Key Concepts

### Authentication in Database Systems

Authentication is the first line of defense in database security, verifying the identity of users or processes attempting to access the database. Database systems support multiple authentication mechanisms:

**Password-Based Authentication:** The most common method where users provide a username and password combination. Modern DBMS enforce password policies requiring complexity, periodic changes, and account lockout after failed attempts.

**Integrated/Windows Authentication:** Used in enterprise environments where the operating system's credentials are used for database access. For example, SQL Server's Windows Authentication uses Kerberos protocol.

**Certificate-Based Authentication:** Uses digital certificates for identity verification, providing stronger security than passwords. This method is prevalent in high-security environments.

**Multi-Factor Authentication (MFA):** Combines two or more authentication factors—something you know (password), something you have (token), and something you are (biometric).

### Authorization and Access Control Models

Once authenticated, users receive permissions determining their access rights. Several models govern this authorization process:

**Discretionary Access Control (DAC):** In DAC, the owner of an object (table, view, or database) has discretion over who can access it and what privileges they receive. The owner can grant or revoke permissions to other users. SQL's GRANT and REVOKE statements implement DAC. While flexible, DAC has a limitation: once a user receives permission, they can propagate it to others, making it difficult to enforce strict control.

Example: If user Alice creates a table "Employees," she can grant SELECT privilege on this table to user Bob. Bob can further grant this privilege to Charlie, potentially creating an uncontrolled distribution of access rights.

**Mandatory Access Control (MAC):** In MAC, the system determines access based on security labels assigned to both users (clearance levels) and objects (classification levels). Users can only access objects if their clearance meets or exceeds the object's classification. This model is primarily used in government and military applications where data classification is paramount.

Security labels typically include levels like Top Secret, Secret, Confidential, and Unclassified. A user with "Secret" clearance cannot access "Top Secret" documents regardless of who owns them.

**Role-Based Access Control (RBAC):** RBAC has become the predominant model in modern database systems. Instead of directly assigning permissions to users, permissions are assigned to roles, and users are assigned to roles. This approach simplifies administration significantly. For instance, instead of granting SELECT permission on the "Orders" table to 50 different sales employees, an administrator creates a "Salesperson" role with that permission and assigns all 50 users to this role.

RBAC concepts include:
- **Roles:** Named collections of privileges (e.g., Database Administrator, Analyst, Clerk)
- **Users:** Individual accounts that can be assigned to multiple roles
- **Permissions:** The ability to perform specific operations (SELECT, INSERT, UPDATE, DELETE)
- **Sessions:** A user's connection during which they activate assigned roles

**Attribute-Based Access Control (ABAC):** The newest model, ABAC, makes access decisions based on user attributes, resource attributes, environmental conditions, and action attributes. For example, access to a file might depend on the user's department, the file's sensitivity level, the time of access, and the device being used. This fine-grained control is highly flexible but complex to implement.

### Database Privileges and SQL Commands

SQL provides specific commands for managing access control:

**GRANT Statement:** Assigns privileges to users or roles.

```sql
GRANT SELECT, INSERT ON Employees TO user123;
GRANT ALL PRIVILEGES ON Accounts TO finance_team;
GRANT SELECT ON Orders TO analyst_role;
```

**REVOKE Statement:** Removes previously granted privileges.

```sql
REVOKE INSERT ON Employees FROM user123;
REVOKE ALL PRIVILEges ON Accounts FROM finance_team;
```

**WITH GRANT OPTION:** Allows the recipient to propagate the granted privileges to others.

```sql
GRANT SELECT ON Products TO manager WITH GRANT OPTION;
```

### Object-Level Security

Database objects require specific security considerations:

**Tables:** The most fundamental security unit. Permissions can be granted at the table level controlling who can read, modify, or delete data.

**Views:** Virtual tables that can serve as security mechanisms by presenting only a subset of data. For example, a view showing only non-sensitive customer information can be granted to general staff while the underlying table remains protected.

**Stored Procedures:** Can encapsulate business logic and limit direct table access. Users execute procedures but never directly access the underlying tables.

**Columns:** Some DBMS allow column-level permissions, restricting access to specific columns within a table.

### Row-Level Security (RLS)

Row-Level Security extends access control to individual rows within a table. This is particularly useful in multi-tenant applications where different customers should only see their own data. PostgreSQL, SQL Server, and Oracle support RLS policies that filter rows based on the current user's context.

### Audit Trails

Comprehensive access control includes auditing—recording who accessed what data and when. Database audit logs capture:
- Login attempts (successful and failed)
- SQL statements executed
- Data modifications
- Schema changes
- Permission modifications

These logs are critical for forensic analysis and compliance with regulations like GDPR and HIPAA.

## Examples

### Example 1: Implementing RBAC in a University Database

Consider a university database system with students, faculty, and administrators. The RBAC implementation would be:

**Step 1: Create Roles**
```sql
CREATE ROLE student_role;
CREATE ROLE faculty_role;
CREATE ROLE administrator_role;
```

**Step 2: Assign Privileges to Roles**
```sql
-- Students can view their own grades and courses
GRANT SELECT ON Enrollments TO student_role;
GRANT SELECT ON Courses TO student_role;

-- Faculty can view and update grades for their courses
GRANT SELECT, UPDATE ON Enrollments TO faculty_role;
GRANT SELECT ON Courses TO faculty_role;

-- Administrators have full access
GRANT ALL PRIVILEGES ON ALL TABLES TO administrator_role;
```

**Step 3: Assign Users to Roles**
```sql
GRANT student_role TO 'student_12345';
GRANT faculty_role TO 'prof_kumar';
GRANT administrator_role TO 'admin_du';
```

This approach allows easy modification of permissions by changing role definitions rather than updating each user individually.

### Example 2: Using Views for Security

A company has an "Employees" table with sensitive salary information. Regular HR staff should only see non-salary employee details.

```sql
-- Create view without salary column
CREATE VIEW Employee_Public AS
SELECT Employee_ID, Name, Department, Position, Hire_Date
FROM Employees;

-- Grant access to view, not underlying table
GRANT SELECT ON Employee_Public TO hr_clerks;

-- Only HR managers get access to salary data
GRANT SELECT ON Employees TO hr_managers;
```

Now, if a clerk tries to access salary data directly:
```sql
SELECT * FROM Employees;  -- Will fail/return no rows based on privileges
SELECT * FROM Employee_Public;  -- Will succeed, showing non-sensitive data
```

### Example 3: Managing Privileges with REVOKE and Grant Option

Scenario: Manager Alice grants a privilege to Bob with grant option, but later needs to revoke it.

```sql
-- Alice grants permission to Bob
GRANT SELECT ON Projects TO bob WITH GRANT OPTION;

-- Bob grants to Charlie
GRANT SELECT ON Projects TO charlie;

-- Alice revokes Bob's permission
REVOKE SELECT ON Projects FROM bob;

-- What happens to Charlie's permission?
-- In standard SQL, CASCADE ensures Charlie also loses access
-- This prevents unauthorized permission propagation
REVOKE SELECT ON Projects FROM bob CASCADE;
```

## Exam Tips

1. **Understand the Difference Between DAC and MAC:** DAC is owner-controlled (flexible but less secure), while MAC is system-enforced based on security labels (rigid but highly secure). Remember that DAC allows users to propagate permissions, MAC does not.

2. **RBAC is the Industry Standard:** For exam questions, when asked to design a database security system, default to RBAC unless specified otherwise. Emphasize roles, privileges, and user-role assignments in your answer.

3. **SQL Commands are Frequently Tested:** Memorize the syntax for GRANT, REVOKE, and understand the WITH GRANT OPTION implications. Know how to grant specific privileges (SELECT, INSERT, UPDATE, DELETE, ALL) to users and roles.

4. **Views as Security Mechanisms:** Understand how views can restrict access to specific columns or rows. This is a common exam question—explaining how views provide an additional security layer.

5. **Remember the Principle of Least Privilege:** Users should be granted only the minimum privileges necessary to perform their job functions. This principle is fundamental in access control design.

6. **Authentication vs. Authorization:** Don't confuse these terms. Authentication verifies identity (who you are), while authorization determines permissions (what you can do). Both are essential but distinct components of access control.

7. **Audit Trails are Essential for Security:** Understand that access control isn't complete without logging and auditing. Audit trails enable detection of security breaches and support compliance requirements.

8. **Row-Level Security is Emerging:** With cloud databases and multi-tenant applications, RLS is increasingly important. Understand its basic concept—even if the specific SQL syntax isn't required.