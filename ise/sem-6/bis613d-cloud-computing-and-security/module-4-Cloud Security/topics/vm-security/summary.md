# VM Security in Cloud Computing

## Overview

Virtual Machines are fundamental cloud computing building blocks - isolated software-based computer emulations running own OS and applications on shared physical hardware. VM security focuses on protecting VMs from attacks, ensuring strong isolation between co-resident VMs, and securing the hypervisor that manages them; a breach can have cascading consequences affecting every VM on the physical host.

## Key Points

- **Hypervisor Types**: Type 1 (Bare-Metal) runs directly on hardware with smaller attack surface, more secure (VMware ESXi, Xen, KVM, Hyper-V); Type 2 (Hosted) runs as application on host OS with larger attack surface (VirtualBox, VMware Workstation)
- **Hypervisor Hardening**: Minimize Trusted Computing Base (TCB), secure management interface on isolated network with certificate-based auth and MFA, apply patches promptly (hypervisor vulnerabilities affect all VMs), enable audit logging for administrative actions, follow CIS Benchmarks
- **VM Isolation**: Most critical security property with CPU isolation (Intel VT-x, AMD-V separate execution contexts), Memory isolation (hypervisor prevents cross-VM memory access), I/O isolation (Intel VT-d, SR-IOV), Network isolation (vSwitch, VLANs)
- **VM Escape**: Most severe virtualization attack where attacker inside Guest VM exploits hypervisor vulnerability to break out and gain host/other VM access; example CVE-2015-3456 (VENOM) virtual floppy disk vulnerability
- **VM Sprawl**: Uncontrolled proliferation of created but never decommissioned VMs; security risk from unpatched, unmonitored VMs with sensitive data or stale credentials; mitigate with lifecycle management, automated expiration, regular audits
- **VM Image Security**: Golden images must use trusted sources, be pre-hardened/patched/stripped of secrets, regularly scanned for vulnerabilities/malware/credentials, stored immutably (read-only), never contain embedded secrets (inject at boot using cloud-init, Key Vault, Secrets Manager)
- **Live Migration Security**: Moving running VM between hosts transfers memory contents over network; encrypt migration traffic (VMware vMotion encryption, KVM TLS), restrict to dedicated management network

## Important Concepts

- Virtualization stack layers from bottom: Physical Hardware → Hypervisor (VMM) → Virtual Hardware (vCPU, vRAM, vNIC) → Guest OS → Guest VM
- VM escape exploits virtual hardware emulation bugs (virtual network card, display) to execute code at hypervisor privilege level for full host control
- Snapshot security: Snapshots contain sensitive data (encryption keys, session tokens, passwords in memory); must encrypt snapshot storage, control access with IAM, delete old snapshots regularly
- VM security best practices: Micro-segmentation (SDN fine-grained policies limiting lateral movement), network monitoring (IDS/IPS for east-west traffic), resource limits (prevent DoS), disable unnecessary virtual hardware, encrypt virtual disks

## Notes

- Type 1 hypervisors preferred in cloud for smaller Trusted Computing Base (TCB) and higher security
- VM Escape is most critical VM attack - know how it works (exploiting virtual hardware emulation) and impact
- Understand VM sprawl risks and mitigation strategies (lifecycle management, automated expiration)
- Image security: know golden image concept and why secrets should never be embedded (inject at boot time)
- Be able to list isolation mechanisms: CPU (VT-x), Memory (hypervisor-managed), I/O (VT-d), Network (vSwitch)
- Live migration and snapshots expose sensitive data if not encrypted - frequently tested topic
