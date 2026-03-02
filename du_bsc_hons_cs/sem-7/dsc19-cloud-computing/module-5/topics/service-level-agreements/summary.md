# Service Level Agreements (SLAs) in Cloud Computing - Summary

## Key Definitions and Concepts

- **Service Level Agreement (SLA)**: A formal contract between a cloud provider and customer defining expected service standards, measurable metrics, and remedies for failures.
- **Availability**: The percentage of time a service is operational, calculated as (Total Time - Downtime) / Total Time × 100%
- **Service Credits**: Compensation (typically bill credits) provided to customers when SLA commitments are not met
- **Shared Responsibility Model**: Division of security and availability duties between cloud provider (infrastructure) and customer (data, applications)

## Important Formulas and Theorems

- **Availability Formula**: Availability % = (Total Time - Downtime) / Total Time × 100%
- **Downtime Calculation**: Downtime = Total Time × (1 - Availability %)
- **Downtime Limits by Tier**:
  - 99% (one nine): 87.6 hours/year
  - 99.9% (three nines): 8.76 hours/year
  - 99.99% (four nines): 52.6 minutes/year
  - 99.999% (five nines): 5.26 minutes/year

## Key Points

1. SLAs are legally binding agreements that set measurable performance standards for cloud services
2. Different cloud services have different SLAs—always check service-specific agreements
3. Multi-AZ deployments typically guarantee 99.99% availability vs 99.9% for single-AZ
4. Service credits are the primary remedy for SLA violations, not cash refunds
5. Common exclusions from SLAs include force majeure, scheduled maintenance, and customer-caused issues
6. The shared responsibility model means providers guarantee infrastructure, not application-level availability
7. AWS, Azure, and GCP all have distinct SLA structures and service credit policies
8. Achieving "five nines" (99.999%) requires comprehensive architectural design beyond just infrastructure SLAs

## Common Mistakes to Avoid

1. **Assuming uniform SLAs**: Never assume all services have the same SLA—each service must be evaluated separately
2. **Ignoring exclusions**: Many students overlook SLA exclusions, which significantly limit actual coverage
3. **Confusing availability with reliability**: Availability is uptime percentage; reliability is mean time between failures (MTBF)
4. **Forgetting customer responsibilities**: Under shared responsibility, customers are responsible for applications, data, and access management
5. **Not accounting for maintenance windows**: Scheduled maintenance can cause downtime even when within SLA terms

## Revision Tips

1. Practice numerical problems on downtime calculations using the availability formula
2. Create a comparison table of AWS, Azure, and GCP SLA offerings for common services
3. Memorize the "nines" and their corresponding downtime allowances
4. Review real SLA documents from major cloud providers to understand actual terminology
5. Understand the difference between infrastructure SLA and application-level availability requirements
6. Focus on the shared responsibility model—it's frequently tested in DU exams