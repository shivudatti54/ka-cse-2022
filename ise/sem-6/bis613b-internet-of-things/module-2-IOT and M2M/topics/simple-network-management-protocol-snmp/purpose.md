# Learning Purpose: Simple Network Management Protocol (SNMP)

**1. Why this topic matters**
SNMP is one of the most widely deployed network management protocols and serves as the foundational approach to monitoring and managing IoT devices and network equipment. Understanding SNMP's architecture, operations, and limitations is essential for managing IoT deployments and for appreciating why modern alternatives like NETCONF-YANG were developed.

**2. What you will learn**
You will learn the SNMP architecture comprising Manager, Agent, and Management Information Base (MIB) components. You will understand SNMP operations (GET, SET, GETBULK, TRAP), how Object Identifiers (OIDs) are used to access device data, and the differences between SNMP versions (v1, v2c, v3) with particular attention to the security improvements in SNMPv3.

**3. How it connects to other topics**
SNMP directly addresses the IoT systems management needs identified earlier in Module 2. It contrasts with NETCONF-YANG, which overcomes SNMP's limitations for configuration management, and both are relevant to the network operator requirements topic. The monitoring concepts from SNMP are applied practically in Module 4 when managing Raspberry Pi-based IoT systems.

**4. Real-world relevance**
SNMP is used globally to monitor network infrastructure, server health, and IoT gateways. ISPs use SNMP to track bandwidth utilization across thousands of routers, while industrial IoT deployments use SNMP traps to receive immediate alerts when equipment sensors report abnormal conditions, enabling rapid response to potential failures.
