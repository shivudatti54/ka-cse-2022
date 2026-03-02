# OS Security in Cloud Computing


## Table of Contents

- [OS Security in Cloud Computing](#os-security-in-cloud-computing)
- [Introduction](#introduction)
- [Host Operating System Security](#host-operating-system-security)
  - [Why Host OS Security is Critical](#why-host-os-security-is-critical)
  - [Host OS Hardening Strategies](#host-os-hardening-strategies)
  - [Patch Management for Host OS](#patch-management-for-host-os)
- [Guest Operating System Security](#guest-operating-system-security)
  - [Guest OS Hardening](#guest-os-hardening)
  - [Guest OS Patching](#guest-os-patching)
- [OS-Level Vulnerabilities in Cloud](#os-level-vulnerabilities-in-cloud)
  - [Common OS Vulnerabilities](#common-os-vulnerabilities)
  - [OS Vulnerabilities Unique to Cloud](#os-vulnerabilities-unique-to-cloud)
- [OS Security Mechanisms](#os-security-mechanisms)
  - [Access Control Models](#access-control-models)
  - [Process Isolation](#process-isolation)
  - [Logging and Auditing](#logging-and-auditing)
- [Key Points / Summary](#key-points--summary)
- [Exam Tips](#exam-tips)
  - [Comparison of Access Control Models](#comparison-of-access-control-models)
  - [Real-World Example: Implementing OS Security in a Cloud Environment](#real-world-example-implementing-os-security-in-a-cloud-environment)

## Introduction

In cloud computing environments, Operating System (OS) security refers to the hardening and protection of both the **Host OS** (the OS running on the physical server) and the **Guest OS** (the OS running inside each Virtual Machine). The OS is a critical layer in the cloud security stack — it sits between the application layer and the hypervisor/hardware, making it a prime target for attackers. A compromised OS can expose all applications, data, and services running on top of it. Cloud environments amplify OS security challenges because a single physical host runs multiple tenant workloads. The Host OS (or Management OS) has direct access to the hypervisor and all VMs, making its security paramount.

## Host Operating System Security

The Host OS is the operating system installed directly on the physical server. In Type 2 hypervisors, it runs the hypervisor as an application. Even in Type 1 (bare-metal) deployments, there is often a management domain (e.g., Xen's Dom0) that functions as a management OS.

### Why Host OS Security is Critical

- The Host OS has the **highest privilege level** after the hypervisor — it can access all VMs, virtual disks, and memory.
- A compromised Host OS allows an attacker to **control all tenant VMs** on that physical server.
- The Host OS runs management tools, APIs, and agents that are high-value targets.

### Host OS Hardening Strategies

| Strategy                            | Description                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Minimal Installation**            | Install only essential packages and services. Remove unnecessary software (GUI, compilers, dev tools) to reduce attack surface. |
| **Dedicated Purpose**               | The Host OS should run ONLY the hypervisor and management tools — no web servers, file sharing, or other services.              |
| **Disable Unused Services**         | Turn off SSH if not needed, disable USB ports, remove unnecessary kernel modules.                                               |
| **Mandatory Access Controls (MAC)** | Use SELinux (enforcing mode) or AppArmor to confine processes to their required permissions.                                    |
| **File System Integrity**           | Use tools like AIDE or Tripwire to detect unauthorized changes to critical OS files.                                            |
| **Secure Boot**                     | Enable UEFI Secure Boot to ensure only signed, trusted OS code loads during startup.                                            |

### Patch Management for Host OS

- Apply security patches **promptly** — unpatched OS is the most common attack vector.
- Use automated patch management tools (e.g., WSUS for Windows, yum-cron/unattended-upgrades for Linux).
- Test patches in a staging environment before applying to production hosts.
- Schedule maintenance windows for patches that require reboots.

## Guest Operating System Security

The Guest OS runs inside each VM and is the tenant's responsibility under the **shared responsibility model** (in IaaS). The cloud provider secures the infrastructure; the customer secures the Guest OS and everything above it.

### Guest OS Hardening

- **Remove Unnecessary Services:** Disable services not required by the application (e.g., print spooler, FTP server).
- **Strong Authentication:** Enforce complex passwords, disable default accounts, and implement SSH key-based authentication.
- **Firewall Configuration:** Configure the OS-level firewall (iptables/nftables on Linux, Windows Firewall) to allow only required traffic.
- **Endpoint Protection:** Install antivirus/anti-malware and host-based intrusion detection (HIDS).
- **User Account Management:** Follow the principle of least privilege — no unnecessary root/admin access.

### Guest OS Patching

In cloud environments, Guest OS patching is the **customer's responsibility**:

- Automate patching with tools like AWS Systems Manager Patch Manager, Azure Update Management.
- Use **immutable infrastructure** patterns: instead of patching live VMs, deploy new VMs from updated golden images and destroy old ones.
- Monitor for unpatched VMs using vulnerability scanners (e.g., Qualys, Nessus, AWS Inspector).

## OS-Level Vulnerabilities in Cloud

### Common OS Vulnerabilities

1. **Privilege Escalation:** An attacker with low-privilege access exploits an OS bug to gain root/admin access. This is especially dangerous on the Host OS.
2. **Kernel Exploits:** Vulnerabilities in the OS kernel can allow attackers to bypass all security controls.
3. **Misconfigured Permissions:** Overly permissive file permissions or sudoers configuration can expose sensitive data.
4. **Unpatched Software:** Known CVEs in OS components that remain unpatched.
5. **Default Credentials:** Default passwords on system accounts or services.

### OS Vulnerabilities Unique to Cloud

- **Shared Kernel (Containers):** In container environments (Docker, Kubernetes), all containers share the host kernel. A kernel exploit affects ALL containers on that host.
- **Management OS Exposure:** The management OS (Dom0 in Xen) has direct hypervisor access. Compromising it is equivalent to compromising the hypervisor.
- **Side-Channel Attacks:** OS-level vulnerabilities like Spectre and Meltdown exploit CPU behavior and can leak data across VM boundaries through the shared OS/hardware.

## OS Security Mechanisms

### Access Control Models

- **Discretionary Access Control (DAC):** Traditional Unix file permissions (owner/group/others). Users control access to their own resources. Flexible but prone to misconfiguration.
- **Mandatory Access Control (MAC):** System-enforced policies that override DAC. SELinux and AppArmor implement MAC. Essential for high-security cloud environments.
- **Role-Based Access Control (RBAC):** Access based on roles rather than individual identity. Commonly used in cloud management consoles.

### Process Isolation

The OS provides process isolation to prevent one process from accessing another's memory or resources:

- **Virtual Memory:** Each process has its own address space.
- **Namespaces (Linux):** Isolate process groups (PID, network, mount, user namespaces). Foundation of container isolation.
- **Cgroups (Linux):** Control resource allocation (CPU, memory, I/O) per process group. Prevents resource exhaustion attacks.

### Logging and Auditing

- **auditd (Linux) / Windows Event Log:** Record system events, file access, authentication attempts.
- **Centralized Log Collection:** Ship OS logs to a SIEM (e.g., CloudWatch, Azure Monitor, Splunk) for correlation and alerting.
- **Tamper-Proof Logs:** Store logs in write-once storage to prevent attackers from covering their tracks.

## Key Points / Summary

- OS security covers both the **Host OS** (provider's domain in many cases) and the **Guest OS** (customer's responsibility in IaaS).
- The Host OS has the **highest privilege level** — its compromise affects all tenant VMs on that host.
- Key hardening strategies: minimal installation, dedicated purpose, MAC (SELinux/AppArmor), secure boot, patch management.
- Guest OS security follows standard hardening plus cloud-specific practices (immutable infrastructure, automated patching).
- Cloud-specific OS risks include shared kernel attacks, management OS exposure, and side-channel attacks (Spectre/Meltdown).
- Access control models (DAC, MAC, RBAC), process isolation (namespaces, cgroups), and centralized logging are essential OS security mechanisms.

## Exam Tips

1. **Shared Responsibility:** Know that in IaaS, the customer is responsible for Guest OS security; the provider secures the Host OS and hypervisor.
2. **Host OS vs Guest OS:** Be able to explain why Host OS compromise is more severe than Guest OS compromise.
3. **MAC vs DAC:** Understand the difference and why MAC (SELinux/AppArmor) is preferred in cloud environments.
4. **Immutable Infrastructure:** Know this as a modern approach to patching in cloud — replace instead of patch.
5. **Side-Channel Attacks:** Understand how Spectre/Meltdown exploit shared hardware and affect OS security in multi-tenant cloud.

### Comparison of Access Control Models

| Model | Description                  | Advantages                                                   | Disadvantages                                                              |
| ----- | ---------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------- |
| DAC   | Discretionary Access Control | Flexible, easy to implement                                  | Prone to misconfiguration, vulnerable to privilege escalation              |
| MAC   | Mandatory Access Control     | Enforces system-wide policies, prevents privilege escalation | Complex to implement, may limit user flexibility                           |
| RBAC  | Role-Based Access Control    | Simplifies access management, reduces administrative burden  | May not be suitable for all environments, requires careful role definition |

### Real-World Example: Implementing OS Security in a Cloud Environment

A company migrates its web application to a cloud provider, using a shared responsibility model. The provider secures the Host OS and hypervisor, while the company is responsible for securing the Guest OS.

To harden the Guest OS, the company:

- Removes unnecessary services and packages
- Configures the OS-level firewall to allow only required traffic
- Implements SSH key-based authentication and disables default accounts
- Installs antivirus/anti-malware and host-based intrusion detection (HIDS)
- Uses automated patch management tools to keep the OS up-to-date

Additionally, the company uses immutable infrastructure patterns to deploy new VMs from updated golden images, ensuring that all VMs are running with the latest security patches.

By implementing these OS security measures, the company reduces the risk of compromise and ensures the confidentiality, integrity, and availability of its web application in the cloud environment.
