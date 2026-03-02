# Setting Goals for Capacity: Different Kinds of Requirements - Summary

## Key Definitions and Concepts

- **Capacity Planning**: The process of determining the IT resources required to meet current and future service demands at optimal cost
- **Business Requirements**: High-level organizational objectives that define what the business needs to achieve
- **User Requirements**: End-user needs and expectations regarding system performance, usability, and accessibility
- **Technical Requirements**: Specific technical characteristics derived from chosen platforms and performance standards
- **Throughput Requirements**: The volume of work systems must process within a given time period
- **Response Time Requirements**: Acceptable time for systems to respond to user requests
- **Availability Requirements**: The percentage of time IT services must be operational
- **Scalability Requirements**: How systems should accommodate growth in workload or users

## Important Formulas and Theorems

- **Availability Calculation**: Availability % = (Total Time - Downtime) / Total Time × 100
- **Nines of Availability**: 99.9% = 8.76 hours downtime/year; 99.99% = 52.6 minutes downtime/year
- **Server Capacity Estimation**: Required Servers = Peak Load / (Capacity per Server × Utilization Factor)
- **Storage Requirements**: Total Storage = (Users × Mailbox Size × Growth Factor) × Redundancy Overhead
- **Growth Projection**: Future Capacity = Current Capacity × (1 + Growth Rate)^Years

## Key Points

- Requirements flow from business level to technical level in a hierarchical manner
- SMART goals ensure capacity objectives are clear and actionable
- Throughput and response time are distinct but related capacity dimensions
- Availability requirements directly impact infrastructure cost and complexity
- Scalability can be achieved through vertical or horizontal scaling approaches
- Capacity goals should include 20-30% buffer for unexpected demand spikes
- Growth projections should consider business forecasts and historical trends
- Regular review of capacity goals ensures continued alignment with business needs

## Common Mistakes to Avoid

- Confusing capacity requirements with performance requirements
- Setting goals that are not measurable or time-bound
- Ignoring growth projections when calculating current capacity needs
- Over-provisioning due to excessive safety margins without cost analysis
- Under-estimating operational requirements like backups and maintenance
- Failing to prioritize requirements based on business criticality
- Not considering trade-offs between cost, performance, and availability

## Revision Tips

1. Create a comparison table of different requirement types and their characteristics
2. Practice converting business scenarios into quantified capacity goals
3. Memorize the SMART framework and apply it to capacity goal examples
4. Review availability calculations and understand the "nines" system
5. Know the difference between vertical and horizontal scalability
6. Focus on understanding the relationship between requirements and goals
7. Practice solving capacity calculation problems similar to the examples provided
