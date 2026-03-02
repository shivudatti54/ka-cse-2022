# Deployment in IT Infrastructure - Summary

## Key Definitions and Concepts

- **Deployment**: The process of making software applications available for use in production environments
- **Blue-Green Deployment**: Maintains two identical environments for instant rollback capability
- **Canary Deployment**: Gradually rolls out changes to a small subset of users before full deployment
- **Rolling Deployment**: Updates instances incrementally across the infrastructure
- **Feature Flags**: Runtime configuration toggles that control feature availability without code deployment
- **CI/CD Pipeline**: Automated pipeline for continuous integration, delivery, and deployment
- **Infrastructure as Code (IaC)**: Managing infrastructure through machine-readable configuration files

## Important Formulas and Theorems

- **Blue-Green Capacity**: Total infrastructure during deployment = 2 × production capacity
- **Rolling Deployment Capacity**: During deployment with N-1 instances, capacity = (N-1)/N of total
- **Canary Load Calculation**: Initial canary load = total users × canary percentage
- **Container Density**: Containers per host = Available resources / Container resource requests

## Key Points

- Deployment strategy choice directly impacts infrastructure capacity requirements and costs
- Blue-green deployments require temporary doubling of infrastructure but provide instant rollback
- Canary deployments minimize risk by limiting exposure to new versions while monitoring performance
- Rolling deployments are resource-efficient but complicate rollback procedures
- Containerization enables higher deployment density and efficient resource utilization
- Automated deployment pipelines reduce human error and ensure consistency
- Integration with auto-scaling is essential for handling capacity variations during deployment
- Rollback mechanisms must be designed before deployment to minimize service disruption

## Common Mistakes to Avoid

- Failing to calculate temporary capacity requirements for blue-green deployments
- Not monitoring resource utilization during canary releases, leading to performance degradation
- Ignoring rollback complexity when choosing rolling deployment strategies
- Underestimating container orchestration overhead in capacity calculations

## Revision Tips

- Practice calculating infrastructure requirements for each deployment strategy
- Memorize the trade-offs between deployment strategies: speed, risk, resource usage, rollback time
- Review how containerization and orchestration tools impact capacity planning
- Focus on understanding real-world scenarios where each deployment strategy is appropriate
