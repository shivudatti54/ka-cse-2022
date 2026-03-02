# Cloud Networking & SDN

## Introduction
Cloud Networking and Software-Defined Networking (SDN) represent paradigm shifts in network architecture. Cloud networking enables dynamic resource allocation through virtualization, while SDN decouples control plane from data plane for centralized management. These technologies form the backbone of modern cloud services (AWS, Azure), 5G networks, and IoT ecosystems.

The importance lies in addressing traditional networking limitations: static configurations, vendor lock-in, and inefficient resource utilization. For DU MCA students, mastering these concepts is crucial for careers in cloud architecture, DevOps, and network automation. The global SDN market is projected to reach $32.7B by 2025 (MarketsandMarkets), highlighting industry demand.

## Key Concepts
1. **SDN Architecture**:
   - **Control Plane**: Centralized controller (e.g., OpenDaylight) using protocols like OpenFlow
   - **Data Plane**: Programmable switches (P4 language)
   - **Northbound APIs**: REST APIs for application integration
   - **Southbound APIs**: OpenFlow, NETCONF for device communication

2. **Cloud Networking Components**:
   - Virtual Private Cloud (VPC)
   - Load Balancers (ALB/NLB)
   - Content Delivery Networks (CloudFront, Akamai)
   - Network Function Virtualization (NFV)

3. **Overlay vs Underlay Networks**:
   - Underlay: Physical infrastructure (BGP, OSPF)
   - Overlay: Virtual networks (VXLAN, GRE tunnels)

4. **Network Automation**:
   - Infrastructure as Code (Terraform)
   - Configuration Management (Ansible)
   - CI/CD Pipelines for network updates

## Examples
**Example 1: AWS VPC Setup with Terraform**
```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  tags = { Name = "du-mca-vpc" }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "ap-south-1a"
}
```
*Solution*: This Terraform code creates a VPC with public subnet in Mumbai region, demonstrating Infrastructure as Code for cloud networking.

**Example 2: SDN Traffic Engineering**
Problem: Prioritize video traffic in campus network.
Solution:
1. Create OpenFlow rule in ONOS controller:
```bash
flow-mod cmd=add,table=0 eth_type=0x800,ip_proto=17,udp_dst=5004 priority=60000 apply:output=2
```
2. Set QoS policy for UDP port 5004 (RTP)
3. Verify with sFlow-RT analytics

## Exam Tips
1. Memorize SDN architecture layers with examples (Northbound: REST, Southbound: OpenFlow)
2. Understand VXLAN header structure (24-bit VNI vs VLAN's 12-bit)
3. Practice BGP configuration for cloud interconnects
4. Study CAPEX vs OPEX benefits in cloud networking case studies
5. Know NFV use cases: virtual firewalls, SD-WAN
6. Compare OpenStack Neutron vs AWS VPC architectures
7. Prepare flow tables diagrams for OpenFlow-based questions