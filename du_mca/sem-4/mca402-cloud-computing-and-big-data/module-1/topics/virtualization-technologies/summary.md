# Virtualization Technologies - Summary

## Key Definitions and Concepts

- **Virtualization**: Technology that creates software-based representations of physical computing resources, enabling multiple virtual machines to run on a single physical server
- **Hypervisor (VMM)**: Software layer that abstracts physical hardware and manages virtual machines; categorized as Type 1 (bare-metal) or Type 2 (hosted)
- **Virtual Machine (VM)**: An isolated software container with its own operating system and applications, running on virtualized hardware
- **Containerization**: OS-level virtualization where containers share the host kernel but maintain isolated user spaces
- **Live Migration**: Moving a running VM from one physical host to another without service interruption
- **VM Snapshot**: Captures complete VM state at a specific point in time for backup and recovery
- **Server Consolidation**: Combining multiple underutilized physical servers into fewer virtual servers

## Important Formulas and Theorems

- **Resource Utilization Improvement**: (1 - Current Utilization) × Number of Servers = Potential Consolidation Ratio
- **TCO Reduction**: (Physical Servers Cost - Virtualized Infrastructure Cost) / Physical Servers Cost × 100
- **Container Memory Efficiency**: Container Memory = Application Memory Only (no OS overhead)
- **VM Memory Requirement**: VM Memory = Guest OS + Application Memory + Hypervisor Overhead

## Key Points

- Virtualization originated in IBM's CP-67 in the 1960s and is now fundamental to cloud computing
- Type 1 hypervisors (ESXi, Hyper-V, KVM) run directly on hardware for production environments; Type 2 (VirtualBox, VMware Workstation) run on host OS for development/testing
- Hardware virtualization virtualizes the physical resources; containerization virtualizes the operating system
- Server consolidation can reduce hardware costs by 50-70% while improving resource utilization from 10-15% to 60-80%
- Live migration enables zero-downtime maintenance and dynamic load balancing
- Containers offer faster startup (seconds vs. minutes), lower overhead, and better resource efficiency than VMs
- Virtualization enables five essential cloud characteristics: on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service

## Common Mistakes to Avoid

- Confusing Type 1 and Type 2 hypervisors—remember bare-metal vs. hosted distinction
- Treating containers and VMs as identical—containers share OS kernel, VMs have separate OS
- Ignoring security considerations—hypervisor vulnerabilities affect all VMs on a host
- Overlooking VM sprawl—untracked VMs become security and licensing risks
- Underestimating performance overhead—virtualization adds 2-5% CPU and memory overhead

## Revision Tips

1. Create a comparison table between Type 1 and Type 2 hypervisors with examples, pros, and cons
2. Memorize 3-4 real-world examples: VMware ESXi (enterprise), KVM (cloud providers), VirtualBox (development), Docker (containers)
3. Practice explaining how virtualization enables each of the five cloud characteristics
4. Review case studies on server consolidation to understand cost-benefit analysis
5. Focus on differences between VMs and containers—this is the most exam-frequently asked concept