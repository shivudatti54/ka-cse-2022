# Virtualization and Cloud Computing - Summary

## Key Definitions and Concepts

- **Virtualization**: Creating software-based representations of physical computing resources (servers, storage, networks) to enable multiple virtual machines on a single physical host
- **Hypervisor**: Software layer that enables virtualization by allocating physical resources to virtual machines; Type 1 runs directly on hardware, Type 2 runs on host operating systems
- **Cloud Computing**: Delivery of computing services (servers, storage, databases, networking, software) over the internet on a pay-as-you-go basis
- **IaaS (Infrastructure as a Service)**: Cloud service model providing virtualized computing resources (VMs, storage, networks)
- **PaaS (Platform as a Service)**: Cloud service model providing complete development and deployment environments
- **SaaS (Software as a Service)**: Cloud service model delivering software applications over the internet

## Important Formulas and Theorems

- **Consolidation Ratio** = Number of Physical Servers ÷ Number of Virtual Machines (typical: 10:1)
- **Resource Utilization** = (Used Resources ÷ Total Available Resources) × 100
- **VM Density** = Total Virtual Machines ÷ Total Physical Hosts
- **Instance Capacity** = Peak Requests per Minute ÷ Requests Handled per Instance
- **Auto-Scale Capacity** = ceil(Maximum Expected Load ÷ Capacity per Instance)

## Key Points

- Virtualization improves server utilization from 5-15% to 60-80%, dramatically reducing hardware costs
- Type 1 hypervisors (VMware ESXi, Hyper-V) are used in enterprise data centers; Type 2 (VirtualBox, VMware Workstation) for development/testing
- Cloud computing offers three service models with shifting responsibility: IaaS (user manages OS/app), PaaS (user manages app), SaaS (provider manages everything)
- Auto-scaling enables dynamic resource adjustment based on demand, improving both performance and cost efficiency
- Hybrid cloud combines private cloud for sensitive workloads with public cloud for elastic burst capacity
- Right-sizing virtual machines and instances is critical for cost optimization in cloud environments

## Common Mistakes to Avoid

- Confusing Type 1 and Type 2 hypervisors or their use cases; remember Type 1 is bare-metal for production
- Misunderstanding the division of responsibility in IaaS, PaaS, and SaaS models
- Setting auto-scaling thresholds too low, causing frequent scaling events (thrashing)
- Over-provisioning cloud resources "just to be safe," negating the cost benefits of cloud computing
- Ignoring network latency considerations when designing distributed or hybrid cloud architectures

## Revision Tips

- Create a comparison table of IaaS, PaaS, and SaaS covering examples, responsibilities, and use cases
- Memorize the consolidation ratio formula and typical values (10:1) for quick exam calculations
- Review real-world examples of cloud providers (AWS, Azure, GCP) and their service offerings
- Practice calculating required instances for auto-scaling configurations
- Understand the advantages and limitations of each cloud deployment model (public, private, hybrid)
