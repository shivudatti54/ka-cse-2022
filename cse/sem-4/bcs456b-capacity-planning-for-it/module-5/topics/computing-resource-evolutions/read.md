# Computing Resource Evolutions

## Table of Contents

- [Computing Resource Evolutions](#computing-resource-evolutions)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Mainframe Computing Era (1950s-1970s)](#mainframe-computing-era-1950s-1970s)
  - [Client-Server Computing (1980s-1990s)](#client-server-computing-1980s-1990s)
  - [Distributed Computing (1990s-2000s)](#distributed-computing-1990s-2000s)
  - [Grid Computing (1990s-2000s)](#grid-computing-1990s-2000s)
  - [Cloud Computing (2007-Present)](#cloud-computing-2007-present)
  - [Edge Computing (2015-Present)](#edge-computing-2015-present)
  - [Modern Hybrid and Multi-Cloud Environments](#modern-hybrid-and-multi-cloud-environments)
- [Examples](#examples)
  - [Example 1: Capacity Planning Evolution for an E-Commerce Platform](#example-1-capacity-planning-evolution-for-an-e-commerce-platform)
  - [Example 2: Calculating Cost Savings from Elastic Computing](#example-2-calculating-cost-savings-from-elastic-computing)
  - [Example 3: Edge Computing Capacity Planning](#example-3-edge-computing-capacity-planning)
- [Exam Tips](#exam-tips)

## Introduction

Computing resource evolution represents one of the most transformative journeys in the history of technology, fundamentally reshaping how organizations approach IT infrastructure and capacity planning. From the massive mainframes of the 1950s to today's sophisticated cloud-native architectures, the landscape of computing has undergone radical changes that continue to accelerate at an unprecedented pace. Understanding this evolution is crucial for IT professionals and students alike, as it provides the foundation for making informed decisions about resource allocation, scalability, and future-proofing organizational infrastructure.

The significance of computing resource evolution extends far beyond historical curiosity. In the context of capacity planning, understanding how computing resources have evolved helps organizations anticipate future needs, optimize current infrastructure, and avoid costly over-provisioning or dangerous under-provisioning. Modern IT environments combine multiple generations of computing paradigms—mainframes still process critical banking transactions, cloud services handle web-scale workloads, and edge devices process IoT data in real-time. This heterogeneity makes understanding the evolutionary path essential for effective capacity management.

This module examines the major paradigms in computing resource evolution, from centralized mainframes through distributed computing, grid computing, cloud computing, and emerging edge computing models. Each paradigm brought new approaches to capacity planning, with distinct advantages, limitations, and planning considerations that remain relevant in modern hybrid environments.

## Key Concepts

### Mainframe Computing Era (1950s-1970s)

The mainframe era marked the beginning of commercial computing, characterized by centralized processing power housed in massive, expensive machines. IBM's System/360 family, introduced in 1964, established the paradigm of centralized computing where a single powerful machine served entire organizations. Capacity planning in this era focused on sizing a single system to meet peak processing requirements, with little consideration for horizontal scaling.

Mainframes offered exceptional reliability and throughput for batch processing workloads, but their cost-prohibitive nature meant only large organizations could afford them. Capacity planning involved careful analysis of transaction volumes, batch window requirements, and growth projections. The planning horizon was typically long—organizations would provision for 3-5 years of growth, leading to significant over-provisioning during the early life of the system.

### Client-Server Computing (1980s-1990s)

The emergence of personal computers and local area networks in the 1980s gave birth to client-server computing, fundamentally decentralizing processing power. In this paradigm, client machines handled user interface and presentation logic while servers managed data and business logic. This distribution of computing resources created new capacity planning challenges—the focus shifted from sizing a single mainframe to balancing loads across multiple servers.

Client-server architectures introduced the concept of tiered computing, with separate database servers, application servers, and web servers. Capacity planning now required understanding the communication patterns between tiers, anticipating bottlenecks at each layer, and planning for independent scaling of individual components. The emergence of three-tier architectures in the 1990s further complicated planning, as organizations needed to predict load distribution across presentation, business logic, and data access layers.

### Distributed Computing (1990s-2000s)

Distributed computing emerged as a solution to the scalability limitations of client-server architectures. This paradigm spread computational tasks across multiple interconnected machines, treating a network of computers as a single unified system. Technologies like CORBA, DCOM, and later web services enabled communication between distributed components, while load balancers distributed requests across server pools.

Capacity planning in distributed environments introduced new metrics: network latency, data consistency trade-offs, and fault tolerance requirements. Organizations moved from capacity planning for individual machines to capacity planning for entire systems. The rise of web-scale applications during the dot-com boom highlighted the importance of horizontal scalability—the ability to add more machines to handle increased load. This era saw the development of techniques like session persistence, distributed caching, and database replication, all requiring careful capacity planning consideration.

### Grid Computing (1990s-2000s)

Grid computing represented an early approach to aggregating distributed computing resources for collective problem-solving. Inspired by electrical power grids, grid computing aimed to share computing resources across organizational boundaries, creating virtual supercomputers from idle desktop machines and underutilized servers. The Globus Toolkit became a foundational technology for grid deployments.

In capacity planning terms, grid computing introduced the concept of resource virtualization at a macro scale. Rather than planning for dedicated capacity, organizations could draw upon shared pools of computing resources. However, the heterogeneous nature of grid resources and the complexity of coordinating work across administrative domains made deterministic capacity planning extremely challenging. Grid computing found success primarily in scientific and research applications with embarrassingly parallel workloads.

### Cloud Computing (2007-Present)

Cloud computing represents the most significant paradigm shift in computing history, fundamentally transforming how organizations procure and manage IT resources. By virtualizing computing resources and delivering them as metered services over networks, cloud computing eliminated the need for organizations to own and manage underlying infrastructure. The NIST definition identifies cloud computing through five essential characteristics: on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service.

Cloud computing revolutionized capacity planning by introducing the concept of elastic scaling—resources that automatically adjust to match demand. Capacity planning in cloud environments shifted from static provisioning to dynamic resource management. Organizations gained the ability to scale horizontally in minutes rather than months, paying only for consumed resources. This transformation required new planning approaches, including workload characterization, cost modeling, performance baselining, and auto-scaling configuration.

The three primary cloud service models—Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS)—each shifted capacity planning responsibilities differently. IaaS requires planning for compute, storage, and network resources; PaaS abstracts infrastructure planning while requiring application-level capacity planning; SaaS eliminates infrastructure planning entirely, shifting focus to consumption monitoring and vendor management.

### Edge Computing (2015-Present)

Edge computing represents the latest evolution, bringing computation and data storage closer to data sources. By processing information at the network edge rather than in centralized cloud data centers, edge computing addresses latency, bandwidth, and data sovereignty concerns for IoT, autonomous systems, and real-time applications. The growth of 5G networks accelerates edge adoption by enabling high-bandwidth, low-latency connectivity.

Capacity planning for edge computing introduces new considerations: distributed resource pools, intermittent connectivity, hierarchical architectures, and integration between edge and cloud components. Organizations must plan for thousands of edge locations versus handfuls of data centers, requiring automated management and orchestration. The edge-cloud continuum creates hybrid capacity planning challenges, determining which workloads run at the edge, which in cloud, and how data moves between them.

### Modern Hybrid and Multi-Cloud Environments

Contemporary IT environments typically combine multiple computing paradigms, creating hybrid architectures that require sophisticated capacity planning. A typical enterprise might run legacy applications on mainframes, core database workloads on private cloud infrastructure, customer-facing applications in public cloud, and IoT processing at the edge. This heterogeneity creates complex capacity planning challenges requiring unified visibility across environments.

Multi-cloud strategies—distributing workloads across multiple cloud providers—add another layer of complexity. Capacity planners must understand the unique characteristics, pricing models, and capabilities of each provider while planning for workload portability and avoiding vendor lock-in.

## Examples

### Example 1: Capacity Planning Evolution for an E-Commerce Platform

Consider the capacity planning journey of a growing e-commerce company over two decades:

**Year 2000 (Client-Server Era):** The company operated a single physical server running both web application and database. Peak season capacity planning involved purchasing hardware sized for 3x average traffic, resulting in significant underutilization during most of the year. The company provisioned for 10,000 concurrent users on a server costing ₹50 lakhs.

**Year 2010 (Distributed/Cloud Era):** After migrating to a three-tier architecture with load balancers, the company could distribute load across multiple application servers. Using cloud infrastructure, they provisioned 5 servers during normal operations and auto-scaled to 20 servers during peak seasons. Annual infrastructure cost reduced to ₹20 lakhs while handling 50,000 concurrent users.

**Year 2020 (Cloud-Native Era):** Containerized microservices deployed on Kubernetes enable fine-grained scaling. The company uses serverless functions for spike processing, managed databases with automatic scaling, and edge caching for global content delivery. They handle 500,000 concurrent users with infrastructure costs directly proportional to revenue, achieving 60% cost reduction compared to traditional provisioning.

This evolution demonstrates how computing paradigms enabled increasingly sophisticated capacity planning, moving from static over-provisioning to dynamic, demand-responsive resource allocation.

### Example 2: Calculating Cost Savings from Elastic Computing

An organization currently runs a batch processing workload on dedicated servers that operate at only 30% average utilization. The workload requires 20 servers running 8 hours daily, 5 days per week.

**Traditional Dedicated Infrastructure:**

- Server cost: ₹5 lakhs each (amortized over 3 years)
- Annual cost: 20 servers × ₹5 lakhs = ₹1 crore
- Utilization: 30% (240 hours/month used out of 720 available)

**Cloud Elastic Model:**

- On-demand instances: 20 servers for 8 hours daily = 160 instance-hours/week
- Monthly: approximately 640 instance-hours
- Cloud cost: ₹100 per instance-hour
- Monthly cost: 640 × ₹100 = ₹64,000
- Annual cost: ₹7.68 lakhs

**Annual Savings:** ₹1 crore - ₹7.68 lakhs = ₹92.32 lakhs (92% reduction)

This example illustrates why cloud computing transformed capacity planning—the organization pays only for utilized capacity rather than owning underutilized infrastructure.

### Example 3: Edge Computing Capacity Planning

A smart city project requires real-time processing of traffic camera data from 1,000 intersections. Each camera generates 2 MB of data per minute, requiring video analytics processing.

**Centralized Cloud Approach:**

- Total data: 1,000 cameras × 2 MB/minute = 2 GB/minute
- Cloud bandwidth required: 2 GB/minute = 33 MB/second
- Cloud processing cost at ₹10/GB: 2 GB/minute × 60 × 24 × 30 = 86,400 GB/month
- Monthly cost: 86,400 × ₹10 = ₹8.64 lakhs
- Latency: 50-100 milliseconds round-trip to cloud data center

**Edge Computing Approach:**

- Edge node at each of 10 zones (100 cameras per zone)
- Each edge node processes local data, sends only alerts (1% of raw data)
- Edge infrastructure: 10 servers × ₹2 lakhs = ₹20 lakhs (one-time)
- Cloud bandwidth for alerts: 864 GB/month
- Monthly cloud cost: 864 × ₹10 = ₹8,640
- Latency: 5-10 milliseconds

**Analysis:** After initial deployment, monthly costs reduce from ₹8.64 lakhs to ₹8,640 (99.9% reduction), while improving response time tenfold. Edge computing proves cost-effective when data volumes are high and latency is critical.

## Exam Tips

1. **Understand Paradigm Characteristics:** For exam questions, clearly differentiate between computing paradigms—know the era, key characteristics, and capacity planning implications of each paradigm from mainframes to edge computing.

2. **Cloud Computing Benefits:** Be prepared to explain how cloud computing transformed capacity planning through elastic scaling, pay-as-you-go pricing, and elimination of upfront capital expenditure.

3. **Service Models Matter:** Understand the differences between IaaS, PaaS, and SaaS—know which capacity planning responsibilities shift to the cloud provider versus remaining with the organization in each model.

4. **Edge Computing Justification:** Be able to explain scenarios where edge computing is preferable to cloud computing, focusing on latency, bandwidth, and data sovereignty requirements.

5. **Hybrid Complexity:** Recognize that modern enterprises operate hybrid environments combining multiple paradigms, requiring integrated capacity planning approaches.

6. **Evolution Drivers:** Understand the business and technological drivers behind each computing evolution—cost reduction, scalability requirements, latency needs, and business agility.

7. **Capacity Planning Metrics:** Know key metrics for each paradigm—utilization rates in mainframes, tier distribution in client-server, elasticity in cloud computing, and latency in edge computing.

8. **Cost Modeling:** Be prepared to calculate or compare infrastructure costs across different computing models, understanding both capital expenditure and operational expenditure implications.
