# Network Management: SNMP

## Introduction
Simple Network Management Protocol (SNMP) forms the backbone of modern network management systems. As networks grow in complexity, SNMP provides a standardized framework for monitoring network devices, detecting faults, and managing configurations. Developed in 1988, SNMP has evolved through three major versions, becoming essential for managing routers, switches, servers, and IoT devices in enterprise environments.

In DU's MCA curriculum, understanding SNMP is crucial for implementing network monitoring solutions and troubleshooting large-scale infrastructures. With 75% of enterprise networks using SNMP for device management, this protocol remains vital for IT operations. The protocol's client-server architecture using Manager/Agent model enables efficient data collection from distributed network elements.

## Key Concepts
1. **SNMP Components**:
   - **Manager**: Central system collecting data (e.g., SolarWinds, PRTG)
   - **Agent**: Software running on managed devices (Cisco IOS, Linux SNMPd)
   - **MIB (Management Information Base)**: Hierarchical database storing device parameters as OIDs (Object Identifiers)
   - **OID Structure**: Dot notation (e.g., 1.3.6.1.2.1.1.5 for sysName)

2. **Protocol Versions**:
   - **SNMPv1**: Basic GET/SET operations with community strings (plaintext)
   - **SNMPv2c**: Bulk operations and improved error handling
   - **SNMPv3**: USM (User Security Model) with authentication and encryption

3. **PDU Types**:
   - GET: Retrieve single value
   - GETNEXT: Tree traversal
   - SET: Modify device parameters
   - TRAP/INFORM: Asynchronous alerts

4. **Security Models**:
   - Community-based (v1/v2c)
   - User-based (v3) with authPriv (SHA/AES) security levels

## Examples
**Example 1: Retrieving Interface Status**
```bash
# Using net-snmp CLI tools
snmpget -v2c -c public 192.168.1.1 1.3.6.1.2.1.2.2.1.8.1
```
*Output:* IF-MIB::ifOperStatus.1 = up(1)

**Example 2: Configuring SNMPv3 Agent**
```cisco
Router(config)# snmp-server group Admin v3 auth
Router(config)# snmp-server user Alice Admin v3 auth SHA myauthpass
```

**Example 3: Trap Configuration for Link Down**
```xml
<!-- In Net-SNMP snmpd.conf -->
authtrapenable 1
trap2sink 10.0.0.5 TRAPCOMMUNITY
```

## Exam Tips
1. Always mention OID structure (ISO→org→dod→internet→mgmt→mib-2→system)
2. Compare SNMPv2c vs v3 security mechanisms in detail
3. Remember TRAP is unacknowledged; INFORM requires confirmation
4. MIB walks use GETNEXT for hierarchical data retrieval
5. Community strings act as weak passwords in v1/v2c
6. Real-world application: Bandwidth monitoring via IF-MIB
7. Know RFC numbers: 1157 (v1), 3416 (v3)