# NETCONF (Network Configuration Protocol)

=====================================

### Overview

NETCONF (RFC 6241) is an IETF session-based network management protocol that uses XML for data encoding and provides operations to install, manipulate, and delete configurations of network devices, offering a modern and secure alternative to SNMP for IoT management.

### Key Points

- **Four-Layer Architecture:** Transport (SSH mandatory), RPC (request-reply), Operations (get-config, edit-config, etc.), and Content (configuration and state data).
- **Core Operations:** get-config, edit-config, copy-config, delete-config, lock/unlock, get, close-session, and kill-session.
- **Transaction Support:** NETCONF supports atomic configuration changes, preventing inconsistent device states unlike SNMP.
- **Security:** Mandates SSH transport for encrypted and authenticated communication, far stronger than SNMP community strings.
- **YANG Integration:** Uses YANG (RFC 6020) as its data modeling language to define structure, constraints, and semantics of device data.
- **Configuration vs. State Data:** YANG distinguishes between writable configuration data (config true) and read-only operational state data (config false).
- **IoT Suitability:** Addresses heterogeneity, scale, security, complex configurations, and automation needs of IoT environments.

### Important Concepts

- NETCONF is designed for comprehensive configuration management, while SNMP focuses primarily on monitoring
- YANG data types: leaf, leaf-list, container, list, choice
- NETCONF uses XML-based RPC for communication
- RESTCONF is an HTTP-based alternative that uses the same YANG models
- NETCONF serves as the southbound interface in SDN controllers

### Notes

- For exams, be ready to contrast NETCONF-YANG with SNMP on security (SSH vs. community strings), data modeling (YANG vs. MIBs), and transaction support (yes vs. no).
- NETCONF may be too resource-heavy for extremely constrained IoT devices; it is more suited for gateways and capable devices.
- Memorize the core NETCONF operations and the four protocol layers.
