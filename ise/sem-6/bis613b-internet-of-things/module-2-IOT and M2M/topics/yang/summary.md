# YANG (Yet Another Next Generation)

=====================================

### Overview

YANG (RFC 6020) is a data modeling language used to define the structure, constraints, and semantics of configuration and state data for network devices, serving as the standard data modeling companion to the NETCONF protocol for IoT management.

### Key Points

- **Purpose:** Models both configuration data (writable settings) and operational state data (read-only status) manipulated by NETCONF, acting as a contract between devices and management systems.
- **Core Data Types:** Leaf (single value), Leaf-list (sequence of values), Container (hierarchy of nodes), List (sequence of entries), and Choice (select one of several alternatives).
- **Human-Readable:** YANG models are significantly easier to understand and write compared to SNMP MIBs, reducing development and maintenance effort.
- **Validation and Constraints:** Enforces data integrity by defining types, ranges, mandatory fields, and default values directly in the model, preventing invalid configurations.
- **Extensibility:** New device capabilities can be added through modular YANG modules without breaking existing models.
- **Configuration vs. State:** Uses "config true" for writable configuration parameters and "config false" for read-only operational state data like sensor readings and battery levels.
- **Protocol Integration:** Primarily used with NETCONF but also compatible with RESTCONF (HTTP-based) for flexible management interfaces.

### Important Concepts

- YANG models serve as contracts defining what data a device exposes and accepts
- Module structure includes namespace, prefix, organization, revision, containers, and leaves
- YANG replaces the older SMI/MIB approach used in SNMP with a more modern, flexible framework
- RESTCONF uses the same YANG models but over HTTP/REST instead of NETCONF/SSH

### Notes

- For exams, know the five core YANG data types (leaf, leaf-list, container, list, choice) and be able to explain each with an example.
- Understand the distinction between configuration data and state data in YANG models -- this is frequently tested.
- YANG is tightly coupled with NETCONF; always discuss them together when explaining modern IoT network management.
