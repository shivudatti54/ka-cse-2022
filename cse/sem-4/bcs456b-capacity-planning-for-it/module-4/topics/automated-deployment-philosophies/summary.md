# Automated Deployment Philosophies - Summary

## Key Definitions and Concepts

- **Automated Deployment**: The process of automatically moving software through environments (development → staging → production) without manual intervention
- **CI/CD**: Continuous Integration automatically integrates and tests code changes; Continuous Deployment automatically deploys validated changes to production
- **Infrastructure as Code (IaC)**: Managing infrastructure through machine-readable configuration files rather than manual processes
- **Deployment Strategy**: A systematic approach to releasing new software versions to production environments

## Important Formulas and Techniques

- **Blue-Green Deployment**: Requires 200% of baseline infrastructure capacity during switchover; provides instant rollback
- **Canary Deployment**: Starts with 5-10% traffic to new version, gradually increases based on monitoring metrics
- **Rolling Deployment**: Updates one instance or batch at a time; maintains partial capacity throughout
- **Kubernetes Autoscaling**: Monitors CPU/memory usage and automatically adjusts replica counts (HPA) or resource limits (VPA)

## Key Points

1. Automated deployment reduces human error, increases deployment frequency, and enables faster feedback loops
2. CI/CD pipelines form the backbone of modern deployment automation with multiple quality gates
3. Blue-green deployment provides zero-downtime but requires double infrastructure resources
4. Canary deployment minimizes risk by gradually routing traffic to new versions
5. IaC enables version-controlled, testable, and repeatable infrastructure provisioning
6. Container orchestration (Kubernetes) provides built-in autoscaling and self-healing capabilities
7. Deployment strategies must align with capacity planning to ensure sufficient resources during transitions
8. Automated rollback mechanisms are essential for maintaining availability during deployment failures
9. Configuration management tools ensure consistency across all environments
10. Security scanning should be integrated into CI/CD pipelines (DevSecOps approach)

## Common Mistakes to Avoid

1. **Ignoring capacity requirements during deployment**: Not accounting for temporary capacity increases during blue-green or canary deployments
2. **Skipping automated testing**: Manual testing bottlenecks negate the benefits of automated deployment
3. **No rollback plan**: Deploying without automated rollback capabilities leads to extended downtime during failures
4. **Inconsistent environments**: Failing to use IaC can cause configuration drift between environments

## Revision Tips

1. Create a comparison table of deployment strategies with pros, cons, and use cases
2. Practice drawing the CI/CD pipeline flow and label each stage
3. Remember that capacity planning and automated deployment are interdependent—scaling affects deployment options
4. Review Kubernetes autoscaling concepts as they frequently appear in capacity planning contexts
5. Focus on understanding when to apply each deployment strategy based on application criticality and resource constraints
