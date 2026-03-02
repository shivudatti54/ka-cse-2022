# Deployment and Automated Deployment Philosophies - Summary

## Key Definitions and Concepts

- **Deployment**: The process of making software available in a target production environment
- **CI/CD Pipeline**: Automated pipeline that automates the path from code commit to production deployment
- **Infrastructure as Code (IaC)**: Managing infrastructure through configuration files rather than manual processes
- **Idempotent Operations**: Operations that produce the same result regardless of how many times they are executed
- **GitOps**: Using Git as the single source of truth for infrastructure and application configurations

## Important Formulas and Techniques

- **Blue-Green Deployment**: Maintain two identical environments; switch traffic after validation
- **Canary Deployment**: Gradually shift traffic (10% → 30% → 50% → 100%) to detect issues early
- **Rolling Deployment**: Update instances incrementally while maintaining capacity
- **Immutable Infrastructure**: Replace infrastructure components rather than modify them

## Key Points

- Automated deployment eliminates manual errors and ensures consistency
- Deployment strategies balance risk, downtime, and deployment speed
- CI/CD pipelines integrate build, test, and deployment processes
- Containerization (Docker) and orchestration (Kubernetes) are foundational to modern deployment
- Infrastructure as Code enables reproducible, version-controlled environments
- Rollback capabilities are essential for safe deployment practices
- Immutable infrastructure simplifies troubleshooting and enables predictable deployments

## Common Mistakes to Avoid

- Assuming deployment scripts will run only once (not considering idempotency)
- Skipping testing in deployment pipelines leading to production failures
- Not having rollback plans before deploying to production
- Modifying production infrastructure directly instead of through IaC
- Insufficient monitoring during and after deployment

## Revision Tips

1. Create comparison charts for different deployment strategies
2. Practice writing simple Ansible/Terraform configurations for deployment
3. Understand the flow from code commit to production in a typical CI/CD pipeline
4. Review real-world case studies of deployment failures and learnings
5. Memorize key terminology and their practical applications
