# Distributed Intrusion Detection in Cloud Computing

Distributed Intrusion Detection Systems (DIDS) are essential for cloud security due to the distributed, dynamic, and multi-tenant nature of cloud environments. Traditional centralized IDS fails in the cloud because there's no single network choke point, VMs migrate dynamically, east-west traffic between co-resident VMs is invisible to perimeter defenses, and attackers operating from compromised internal VMs evade perimeter-based detection.

DIDS employs a hierarchical architecture with multiple coordinated Intrusion Detection Agents (IDAs) deployed across different layers: Host-based IDS (HIDS) inside guest VMs monitoring OS-level events, hypervisor-based IDS providing visibility into guest VMs without being inside them, and Network-based IDS (NIDS) at virtual switches or physical perimeters. These agents use signature-based detection for known threats and anomaly-based detection to identify deviations from normal behavior. A Global Intrusion Detection Manager (GIDM) correlates data from all agents to identify attacks spanning multiple VMs or hosts.

## Key Takeaways

- DIDS addresses cloud-specific challenges like VM mobility, east-west traffic invisibility, and multi-tenancy
- Architecture includes multiple agent types (HIDS, hypervisor-based, NIDS) reporting to a central correlator
- Signature-based detection catches known attacks while anomaly-based detection identifies novel threats
- Key challenges include data collection overhead, correlation complexity, scalability, and agent security
