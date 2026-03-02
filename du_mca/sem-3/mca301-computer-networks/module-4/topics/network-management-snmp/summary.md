# Network Management: SNMP - Summary

## Key Definitions and Concepts
- **SNMP**: Application-layer protocol for managing IP network devices
- **MIB**: Virtual database containing managed objects in ASN.1 format
- **Trap**: Unsolicited notification from agent to manager
- **Community String**: Plaintext password in SNMPv1/v2c

## Important Formulas and Theorems
- OID Notation: 1.3.6.1.2.1 (iso.org.dod.internet.mgmt.mib-2)
- SNMP Ports: UDP 161 (Agent), UDP 162 (Manager)
- Version Features Matrix: v3 = v2c + authentication + encryption

## Key Points
- SNMPv3 uses USM (User Security Model) and VACM (View Access Control Model)
- MIBs are compiled into agent software using ASN.1 compiler
- GETBULK operation in v2c reduces PDUs for large data requests
- SNMP walk = Sequence of GETNEXT operations
- Enterprise-specific MIBs start at OID 1.3.6.1.4.1
- INFORM-PDU requires acknowledgment; TRAP doesn't
- Security Levels: noAuthNoPriv → authNoPriv → authPriv

## Common Mistakes to Avoid
- Using SNMPv1 in modern networks (security risk)
- Confusing OID numerical notation with symbolic names
- Forgetting UDP port differences for traps vs queries
- Misconfiguring SNMPv3 security levels
- Ignoring access control views in VACM

## Revision Tips
1. Practice OID navigation using SNMPwalk CLI tool
2. Create comparison charts for SNMP versions
3. Memorize key MIB-2 OIDs: system(1), interfaces(2), ip(4)
4. Use Wireshark to analyze SNMP packet structure
5. Review RFC 3414 for SNMPv3 security framework