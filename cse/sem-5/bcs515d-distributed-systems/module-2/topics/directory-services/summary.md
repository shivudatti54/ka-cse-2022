# Directory Services - Summary

## Key Definitions and Concepts

- **Directory Service**: A specialized database optimized for storing and retrieving information about network objects (users, computers, printers) in a hierarchical structure
- **DIT (Directory Information Tree)**: The hierarchical tree structure that organizes all directory entries from root to leaf nodes
- **DN (Distinguished Name)**: A unique identifier for a directory entry, consisting of the full path from root to the entry (e.g., uid=user,ou=people,dc=domain,dc=com)
- **RDN (Relative Distinguished Name)**: The component of DN at a single level in the hierarchy
- **LDAP (Lightweight Directory Access Protocol)**: The standard protocol for accessing and managing directory services
- **Object Class**: Defines a category of objects and specifies mandatory and optional attributes
- **Schema**: The collection of rules defining object classes, attributes, and their relationships

## Important Formulas and Theorems

No specific formulas apply to this topic as it is conceptual in nature. Key relationships include:

- **DN Composition**: DN = RDN1 + RDN2 + ... + RDNn (from leaf to root)
- **LDAP Search Scope**: 0 = base, 1 = one level, 2 = subtree

## Key Points

- Directory services are read-optimized databases designed for frequent lookups rather than transaction processing
- LDAP is the de facto standard protocol, derived from but simpler than X.500
- Entries in a directory follow a hierarchical tree structure (DIT) with the root at the top
- Object classes define what attributes entries can contain, with mandatory and optional attributes
- Active Directory is Microsoft's enterprise directory service implementation extending LDAP
- Directory services provide centralized authentication, authorization, and resource discovery
- Replication ensures high availability through master-slave or multi-master configurations
- Common LDAP operations include Bind, Search, Add, Delete, Modify, and Compare

## Common Mistakes to Avoid

- Confusing DN with RDN (DN is the complete path, RDN is one level)
- Thinking directory services can replace databases (they complement each other)
- Assuming LDAP always uses encryption (port 389 can be unencrypted; use port 636 or STARTTLS for security)
- Forgetting that directory services are optimized for reads, not frequent writes
- Confusing DNS with directory services (DNS is for name-to-address resolution only)

## Revision Tips

- Draw the DIT structure to understand hierarchical relationships
- Memorize the seven LDAP operations and their purposes
- Remember key differences between directory services and relational databases
- Review sample LDAP search queries to understand filtering syntax
- Practice explaining how user authentication works through LDAP step-by-step
- Focus on understanding the real-world applications in enterprise networks
