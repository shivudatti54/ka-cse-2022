# Simple Network Management Protocol (SNMP)

=====================================

### Overview

SNMP is an application-layer protocol based on a manager-agent model that enables network administrators to monitor, manage, and control network devices remotely using a standardized set of operations and a structured Management Information Base (MIB).

### Key Points

- **Architecture Components:** SNMP Manager (NMS), SNMP Agent (on managed device), Managed Device, Management Information Base (MIB), and Object Identifiers (OIDs).
- **Core Operations:** GET (retrieve value), GETNEXT (traverse table), SET (modify value), RESPONSE (reply to requests), and TRAP (asynchronous event notification from agent to manager).
- **Advanced Operations:** GETBULK (bulk data retrieval, SNMPv2c+) and INFORM (acknowledged notification, SNMPv2c+).
- **SNMP Versions:** v1 uses plaintext community strings (insecure); v2c adds GETBULK/INFORM but still uses community strings; v3 adds authentication (SHA), encryption (AES), and access control via USM.
- **IoT Application:** Monitoring sensor data via GET, fault management via TRAPs, remote configuration via SET, and performance tracking on gateways.
- **MIB and OIDs:** Every managed object is accessed via a globally unique OID organized in a hierarchical tree structure; custom MIBs are developed for IoT-specific data.
- **SNMP vs. NETCONF-YANG:** SNMP is simpler and lightweight (UDP-based), suited for basic monitoring; NETCONF-YANG is richer with full CRUD operations, transaction support, and stronger security.

### Important Concepts

- Manager-Agent model is the foundation of SNMP architecture
- TRAPs are asynchronous and unacknowledged; INFORMs are acknowledged
- SNMPv3 is mandatory for secure IoT deployments
- MIB is the "map" that translates OIDs into human-readable object descriptions

### Notes

- For exams, memorize all PDU types (GET, GETNEXT, GETBULK, SET, RESPONSE, TRAP, INFORM) and which SNMP versions introduced them.
- The security difference between v1/v2c (community strings) and v3 (USM with authentication and encryption) is a frequently tested topic.
- SNMP is preferred for constrained IoT devices due to its lightweight nature, while NETCONF-YANG is used for complex configuration on capable devices.
