# Cloud Computing - Summary

## Key Definitions and Concepts

- **Cloud Computing**: A model for enabling on-demand network access to a shared pool of configurable computing resources that can be rapidly provisioned and released with minimal management effort.

- **NIST Five Characteristics**: On-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service.

- **Multi-tenancy**: Multiple customers sharing the same physical infrastructure while maintaining isolation between workloads.

- **Virtualization**: Technology that creates virtual versions of hardware platforms, storage devices, and network resources.

## Important Formulas and Theorems

- **Cloud Cost Formula**: Total Cloud Cost = Compute Cost + Storage Cost + Data Transfer Cost + Additional Services

- **Right-sizing**: Matching instance types to actual workload requirements for cost optimization

- **Auto-scaling Rules**: Scale out threshold (typically 70-80% CPU), Scale in threshold (typically 20-30% CPU)

## Key Points

1. **Service Models**: IaaS (infrastructure - AWS EC2), PaaS (platform - Azure App Service), SaaS (software - Microsoft 365)

2. **Deployment Models**: Public (shared resources), Private (single organization), Hybrid (combination), Community (shared by specific groups)

3. **Benefits**: Cost savings, scalability, elasticity, high availability, disaster recovery, global infrastructure

4. **Challenges**: Data security, vendor lock-in, compliance, latency, loss of control over infrastructure

5. **Shared Responsibility**: Security responsibilities vary by service model - IaaS requires more user management than SaaS

6. **Capacity Planning**: Cloud enables right-sizing, auto-scaling, and pay-as-you-go pricing eliminating over-provisioning

7. **Major Providers**: AWS, Microsoft Azure, Google Cloud Platform (GCP), IBM Cloud

## Common Mistakes to Avoid

- Confusing service models with deployment models (they are different concepts)
- Assuming cloud is always cheaper (without proper planning, costs can exceed on-premises)
- Believing cloud removes all management responsibilities (varies significantly by service model)
- Ignoring data privacy and compliance requirements when selecting cloud services

## Revision Tips

1. Create a comparison table of IaaS, PaaS, and SaaS with examples, management responsibilities, and use cases.

2. Practice drawing the cloud architecture diagram showing the relationship between physical, virtualization, and service layers.

3. Remember that in exams, cloud computing questions often test understanding of fundamental concepts rather than technical implementation details.

4. Focus on how cloud computing addresses traditional IT challenges like capacity planning, cost management, and scalability.
