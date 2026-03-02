# IoT System Management with NETCONF-YANG

=====================================

### Overview

NETCONF-YANG is a standardized framework for managing IoT device configurations, monitoring operational state, and ensuring consistency across large device fleets. NETCONF (RFC 6241) provides the protocol for secure, session-based device configuration, while YANG (RFC 6020) defines the data modeling language that structures the data NETCONF operates on.

### Key Points

- **NETCONF Four-Layer Architecture:** Transport (SSH mandatory), Messages (XML-based RPC), Operations (get-config, edit-config, etc.), and Content (configuration/state data).
- **Core NETCONF Operations:** get-config, edit-config, copy-config, delete-config, lock/unlock, get, close-session, and commit.
- **YANG Data Constructs:** leaf (single value), leaf-list (ordered sequence), container (grouping), list (keyed entries), and choice (alternative branches).
- **config true vs config false:** YANG distinguishes writable configuration parameters from read-only operational state data.
- **Transaction Support:** NETCONF supports atomic commit/rollback, preventing inconsistent device states.
- **Five-Step IoT Workflow:** Device discovery (hello exchange), configuration deployment (edit-config), monitoring (get), automated response, and maintenance (rollback-capable updates).
- **RESTCONF (RFC 8040):** An HTTP-based RESTful alternative that reuses the same YANG data models.
- **SNMP Limitations:** Weak security, flat MIBs, no transaction support, and limited configuration capability compared to NETCONF-YANG.

### Important Concepts

- YANG defines the "what" (data structure) and NETCONF provides the "how" (operations and transport)
- NETCONF-YANG architecture includes management application, NETCONF controller, YANG model repository, configuration database, and IoT devices
- NETCONF vs SNMP: SSH vs community strings, hierarchical YANG vs flat MIBs, XML vs BER/ASN.1
- Resource-constrained sensors may need lightweight proxies or gateways for NETCONF support

### Notes

- For exams, be prepared to compare NETCONF-YANG with SNMP across security, configuration, and data modeling dimensions.
- Know the four NETCONF layers, YANG constructs, and the five-step management workflow.
- Be able to draw the NETCONF-YANG IoT architecture diagram showing all key components.
