# Cloud Capacity Planning - Summary

## Key Definitions and Concepts

- **Cloud Capacity Planning**: The process of predicting and provisioning appropriate computing resources in cloud environments to meet performance requirements while optimizing costs.

- **IaaS/PaaS/SaaS**: Three cloud service models where capacity planning responsibilities vary from full control (IaaS) to provider-managed (SaaS).

- **Vertical Scaling**: Upgrading existing resource capacity (more CPU/RAM); simple but has limits and requires downtime.

- **Horizontal Scaling**: Adding more resource instances; preferred in cloud for near-unlimited scalability and fault tolerance.

- **Auto-Scaling**: Automatically adjusting resource capacity based on demand using metrics, schedules, or predictions.

- **Rightsizing**: Matching instance sizes to actual workload requirements to eliminate over-provisioning.

## Important Formulas and Theorems

- **Instance Count**: Required Instances = Total Workload / (Capacity per Instance × Utilization Factor)
- **Storage Capacity**: Total Storage = (Data Size × Growth Factor) + Buffer for overheads
- **Bandwidth**: Required Bandwidth = (Page Views × Data per View) / Time Period
- **Cost Savings**: Savings = (On-Demand Price - Reserved/Spot Price) × Usage Duration

## Key Points

- Cloud capacity planning differs from traditional on-premise planning due to on-demand resource allocation and pay-as-you-go pricing.

- Horizontal scaling is preferred over vertical scaling in cloud environments for better fault tolerance and cost efficiency.

- Auto-scaling can be triggered by metrics (CPU, memory), schedules, or predictive analytics.

- Reserved instances offer 30-70% discounts for predictable baseline workloads; spot instances offer up to 90% discounts for fault-tolerant batch jobs.

- Rightsizing involves analyzing usage data and adjusting instance types to match actual requirements.

- Multi-cloud strategies help avoid vendor lock-in but increase complexity in capacity management.

- Key monitoring metrics include CPU utilization, memory usage, network throughput, storage I/O, and application response times.

- Capacity planning is an iterative process requiring continuous monitoring and adjustment.

## Common Mistakes to Avoid

- Over-provisioning resources "just to be safe" leads to unnecessary costs in cloud environments.

- Ignoring auto-scaling configuration results in either performance issues during peaks or wasted resources during low usage.

- Not considering data transfer costs between cloud regions or between cloud and on-premise environments.

- Failing to implement redundancy and high availability in capacity planning, leading to single points of failure.

## Revision Tips

- Focus on understanding the difference between scaling approaches and when to apply each.

- Remember the three auto-scaling types and their appropriate use cases.

- Practice calculating resource requirements from workload scenarios as seen in examples.

- Review cost optimization strategies and their applicability to different workload types.

- Know the key metrics used in cloud capacity monitoring and planning decisions.
