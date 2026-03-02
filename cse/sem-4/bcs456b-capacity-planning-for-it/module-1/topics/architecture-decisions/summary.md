# Architecture Decisions in IT Capacity Planning - Summary

## Key Definitions and Concepts

- **Architecture Decisions:** Strategic choices defining IT infrastructure structure, deployment, and management to meet business demands
- **Monolithic Architecture:** Single deployable unit containing all application components; challenging to scale granularly
- **Microservices Architecture:** Loosely coupled, independently deployable services enabling fine-grained scaling
- **Vertical Scaling (Scale-Up):** Adding more resources (CPU, RAM) to existing servers
- **Horizontal Scaling (Scale-Out):** Adding more server instances to handle increased load
- **Auto-Scaling:** Automatic resource adjustment based on predefined metrics
- **TCO (Total Cost of Ownership):** Complete cost analysis including acquisition, operation, and maintenance

## Important Formulas and Concepts

- **Scalability Formula:** Throughput = (Number of Servers) × (Throughput per Server) × (Efficiency Factor)
- **Auto-scaling Condition:** Scale out when metric > upper threshold; scale in when metric < lower threshold
- **TCO Calculation:** Initial Capital Cost + (Annual Operating Cost × Years) - Residual Value

## Key Points

1. Architecture decisions directly impact capacity requirements, performance characteristics, and total cost of ownership of IT systems

2. Microservices enable horizontal scaling with finer granularity compared to monolithic architectures

3. Cloud deployment offers elasticity and pay-as-you-go pricing, ideal for variable workloads

4. Hybrid cloud combines on-premises control with cloud scalability for burst capacity and disaster recovery

5. Vertical scaling has physical and cost limits; horizontal scaling provides nearly unlimited scalability for cloud-native applications

6. Auto-scaling enables cost-efficient resource utilization by adjusting capacity based on demand

7. Technology selection must consider workload characteristics: CPU-intensive, memory-intensive, or I/O-intensive

## Common Mistakes to Avoid

- Selecting architecture based only on initial cost without considering TCO over system lifetime
- Choosing microservices when application simplicity would suffice, adding unnecessary complexity
- Over-provisioning for peak capacity instead of implementing elastic scaling solutions
- Ignoring network latency and data transfer costs in cloud architecture decisions

## Revision Tips

1. Practice comparing at least 3 architectural options for given scenarios, focusing on scalability and cost implications

2. Remember the key advantage of each model: monoliths (simplicity), microservices (granular scaling), cloud (elasticity), hybrid (flexibility)

3. Review the university's previous exam questions on architecture decisions to understand the expected answer depth and format

4. Create a decision matrix template for comparing architecture options with criteria: Cost, Scalability, Complexity, Implementation Time, Operational Overhead
