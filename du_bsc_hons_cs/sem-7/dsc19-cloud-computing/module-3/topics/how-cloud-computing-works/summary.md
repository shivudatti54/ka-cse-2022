# How Cloud Computing Works - Summary

## Key Definitions and Concepts

- **Cloud Computing**: Delivery of computing services (servers, storage, databases, networking, software) over the internet on a pay-as-you-go basis
- **Virtualization**: Technology that creates virtual versions of hardware platforms, storage devices, and network resources
- **Multi-tenancy**: Architecture allowing multiple customers to share cloud resources while maintaining data isolation
- **Elasticity**: Ability to dynamically scale resources up or down based on demand
- **Orchestration**: Automated coordination and management of complex cloud workloads

## Important Formulas and Concepts

- **Service Models**: IaaS (Infrastructure) → PaaS (Platform) → SaaS (Software) — increasing abstraction, decreasing control
- **Deployment Models**: Public, Private, Hybrid, Community — based on access and ownership
- **Five Characteristics**: On-demand self-service, broad network access, resource pooling, rapid elasticity, measured service

## Key Points

1. Cloud architecture consists of physical infrastructure, virtualization layer, resource pooling, and management plane
2. IaaS provides maximum control (virtual machines, OS); PaaS provides development platforms; SaaS provides complete applications
3. Public clouds offer scalability and cost-efficiency; private clouds offer control and security; hybrid combines both advantages
4. Cloud provisioning happens in minutes through automated orchestration, unlike traditional IT which takes weeks
5. Key enabling technologies include virtualization, containers (Docker), Kubernetes, and serverless computing
6. Cloud shifts spending from Capital Expenditure to Operational Expenditure
7. Multi-tenancy enables cost-sharing while maintaining security through isolation

## Common Mistakes to Avoid

- Confusing PaaS with IaaS—PaaS abstracts away the operating system, while IaaS provides virtualized hardware
- Assuming private clouds are always more secure—security depends on implementation, not deployment model
- Overlooking the shared responsibility model—security and management duties are divided between provider and customer

## Revision Tips

1. Draw the cloud service model pyramid (IaaS at base, SaaS at top) to remember the hierarchy
2. Practice explaining cloud concepts to a non-technical person—this tests true understanding
3. Memorize real-world examples (AWS for IaaS, Heroku for PaaS, Netflix for SaaS) as exam questions often use these
4. Review NIST cloud computing definition and the five essential characteristics