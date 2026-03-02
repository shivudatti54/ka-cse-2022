# OS Security in Cloud Computing

## Overview

Operating System security in cloud environments refers to hardening and protecting both Host OS (running on physical server) and Guest OS (running inside each Virtual Machine). The OS layer sits between application and hypervisor/hardware, making it a prime attack target; a compromised OS exposes all applications, data, and services running on it.

## Key Points

- **Host OS Critical Importance**: Has highest privilege level after hypervisor, can access all VMs, virtual disks, and memory; compromise allows control of all tenant VMs on that physical server
- **Host OS Hardening**: Minimal installation (only essential packages), dedicated purpose (only hypervisor and management tools), disable unused services (SSH, USB ports, kernel modules), Mandatory Access Controls (SELinux enforcing, AppArmor), file system integrity monitoring (AIDE, Tripwire), Secure Boot (UEFI)
- **Host OS Patch Management**: Apply security patches promptly using automated tools (WSUS, yum-cron, unattended-upgrades), test in staging before production, schedule maintenance windows for reboots
- **Guest OS Security**: Customer responsibility in IaaS shared responsibility model; hardening includes removing unnecessary services, strong authentication (SSH keys), OS-level firewall configuration (iptables, Windows Firewall), endpoint protection (antivirus, HIDS), least privilege user accounts
- **Guest OS Patching**: Customer-managed using automated tools (AWS Systems Manager Patch Manager, Azure Update Management), immutable infrastructure pattern (deploy new VMs from updated images, destroy old ones), monitor with vulnerability scanners (Qualys, Nessus, AWS Inspector)
- **OS Vulnerabilities**: Privilege escalation, kernel exploits, misconfigured permissions, unpatched software, default credentials
- **Cloud-Specific Risks**: Shared kernel (containers share host kernel - exploit affects ALL containers), management OS exposure (Dom0 in Xen has direct hypervisor access), side-channel attacks (Spectre/Meltdown exploit CPU behavior leaking data across VM boundaries)

## Important Concepts

- Access control models: DAC (traditional Unix file permissions, flexible but misconfiguration-prone), MAC (system-enforced policies with SELinux/AppArmor, essential for high-security), RBAC (role-based access in management consoles)
- Process isolation mechanisms: Virtual memory (separate address spaces), Namespaces (isolate PID, network, mount, user - foundation of containers), Cgroups (control CPU, memory, I/O per process group - prevent resource exhaustion)
- Logging and auditing: auditd/Windows Event Log, centralized log collection to SIEM (CloudWatch, Azure Monitor, Splunk), tamper-proof write-once storage
- Immutable infrastructure as modern patching approach: replace entire VMs instead of patching live systems for consistency and security

## Notes

- In IaaS shared responsibility model: customer secures Guest OS, provider secures Host OS and hypervisor
- Understand Host OS compromise is more severe than Guest OS compromise (affects all tenant VMs)
- Know MAC vs. DAC difference and why MAC (SELinux/AppArmor) is preferred in cloud environments
- Immutable infrastructure is modern cloud approach to patching - replace instead of patch
- Side-channel attacks (Spectre/Meltdown) exploit shared hardware affecting OS security in multi-tenant cloud
- Remember namespaces and cgroups as Linux kernel features enabling container isolation
