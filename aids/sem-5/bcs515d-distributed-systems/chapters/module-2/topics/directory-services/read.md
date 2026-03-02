# Directory Services

## 1. Introduction to Directory Services

Directory Services represent a critical component in distributed systems, providing a specialized form of **name service** designed for managing and accessing information about various resources in a network. While traditional name services (like DNS) primarily map human-readable names to network addresses, directory services offer a more sophisticated approach by storing **attributes** about objects and supporting complex **search queries**.

A directory service acts as a centralized repository for information about users, computers, printers, services, and other network resources. It provides a structured, hierarchical framework for organizing, retrieving, and managing this data, enabling efficient resource discovery and access control in distributed environments.

## 2. Key Concepts and Terminology

### 2.1. Directory Information Base (DIB)

The DIB is the actual database that stores all the directory entries. Each entry represents an object in the directory (e.g., a user, a printer) and consists of a collection of attributes.

### 2.2. Directory Entry

A single record in the DIB. It is composed of a set of **attributes**, each with a type and one or more values.

```
+-----------------------+
|   Directory Entry     |
| (e.g., User: John Doe)|
+-----------------------+
| Attribute: cn         |
| Value: John Doe       |
+-----------------------+
| Attribute: mail       |
| Value: jdoe@email.com |
+-----------------------+
| Attribute: employeeID |
| Value: 12345          |
+-----------------------+
```

### 2.3. Attribute

A characteristic of an object. It has a type (e.g., `telephoneNumber`) and associated values (e.g., `+1-555-0101`).

### 2.4. Distinguished Name (DN)

A unique identifier for an entry within the directory hierarchy. It is constructed by combining the Relative Distinguished Name (RDN) of the entry with the DNs of its parent entries.

Example DN: `cn=John Doe,ou=Engineering,dc=example,dc=com`

### 2.5. Schema

The set of rules that defines the structure of the DIB, including which object classes and attribute types are allowed, and how they relate to each other.

## 3. Comparison with Name Services

It's crucial to understand how directory services differ from and complement basic name services like the Domain Name System (DNS).

| Feature              | Name Service (e.g., DNS)              | Directory Service (e.g., LDAP)                    |
| :------------------- | :------------------------------------ | :------------------------------------------------ |
| **Primary Function** | Name-to-address resolution            | Attribute-based information storage and retrieval |
| **Data Model**       | Flat or hierarchical namespaces       | Hierarchical, object-oriented data model          |
| **Query Type**       | Simple lookup (name → IP)             | Complex search and filter operations              |
| **Data Structure**   | Simple records (e.g., A, MX records)  | Rich entries with multiple attributes             |
| **Update Frequency** | Relatively low (mostly read-oriented) | Higher (frequent reads and writes)                |
| **Typical Use Case** | Finding a website's IP address        | Finding all printers on the 3rd floor             |

## 4. The Lightweight Directory Access Protocol (LDAP)

LDAP is the predominant protocol used to access directory services. It was developed as a lighter-weight alternative to the X.500 Directory Access Protocol (DAP).

### 4.1. LDAP Operations

LDAP defines a set of operations for interacting with the directory:

- **Bind (Authentication):** Establishes a session and authenticates a client.
- **Search:** Looks for and retrieves directory entries based on a search filter.
- **Compare:** Tests if a named entry contains a given attribute value.
- **Add:** Inserts a new entry into the directory.
- **Delete:** Removes an entry.
- **Modify:** Changes the attributes of an entry.
- **Unbind:** Terminates a session.

### 4.2. LDAP Data Interchange Format (LDIF)

LDIF is a standard text format for representing LDAP directory entries and data changes.

```
dn: cn=John Doe,ou=users,dc=acme,dc=com
objectClass: inetOrgPerson
cn: John Doe
sn: Doe
mail: j.doe@acme.com
telephoneNumber: +1 555 123 4567
```

## 5. Architecture of Directory Services

Directory services typically follow a client-server model.

### 5.1. DSA (Directory System Agent)

The server component that provides access to the DIB. It processes client requests and manages the directory data.

```
+---------+    LDAP Request    +-----+
| LDAP    | -----------------> |     |
| Client  |                    | DSA |
|         | <----------------- |     |
+---------+    LDAP Response   +-----+
```

### 5.2. Replication and Distribution

To ensure high availability, performance, and fault tolerance, directory data is often replicated across multiple servers. Changes made to one replica are propagated to others.

```
         +-----------------+
         |  Master DSA     |
         | (Read/Write)    |
         +-----------------+
              /    \
             /      \
            /        \
+-----------------+  +-----------------+
|  Replica DSA 1  |  |  Replica DSA 2  |
| (Read-Only)     |  | (Read-Only)     |
+-----------------+  +-----------------+
```

### 5.3. Referrals

If a DSA does not hold the requested information, it may return a **referral** to the client, pointing it to another DSA that might have the data.

```
Client asks DSA-A for entry in partition B
         |
         v
DSA-A returns a referral: "ldap://dsa-b.acme.com"
         |
         v
Client connects to DSA-B and re-issues the request
```

## 6. Implementation: Active Directory and OpenLDAP

### 6.1. Microsoft Active Directory (AD)

AD is a comprehensive directory service for Windows domain networks. It uses LDAP for communication, Kerberos for authentication, and a multi-master replication model. Its schema is extensible, allowing integration with other applications.

### 6.2. OpenLDAP

An open-source implementation of an LDAP directory server. It is highly configurable and widely used on Unix/Linux systems for managing user accounts, groups, and other system information.

## 7. Use Cases and Applications

- **Centralized Authentication:** Logging into computers and applications using a single set of credentials (Single Sign-On - SSO).
- **Resource Discovery:** Finding network resources like printers and file shares based on their properties (e.g., location, color capability).
- **Address Books:** Storing and looking up contact information for users within an organization.
- **Authorization and Policy Management:** Storing user permissions and group memberships to control access to resources.

## 8. Exam Tips

1.  **Differentiate DNS and Directory Services:** Be prepared to clearly explain the functional differences using a table. DNS is for simple name resolution; LDAP is for complex, attribute-based queries.
2.  **Understand LDAP Operations:** Memorize the core LDAP operations (Bind, Search, Add, Modify, Delete) and what they do. You will likely be asked to match an operation to a scenario.
3.  **Draw and Explain the Hierarchy:** Practice drawing a simple directory information tree (DIT) and writing the Distinguished Name (DN) for an entry within it. Understand what an RDN is.
4.  **Know the Benefits of Replication:** Be able to discuss why replicating directory servers is crucial for performance, scalability, and availability in a distributed system.
5.  **Explain a Referral:** Understand the concept of a referral—why a server would send one and what the client must do next. This is a key mechanism for linking distributed directory services.
