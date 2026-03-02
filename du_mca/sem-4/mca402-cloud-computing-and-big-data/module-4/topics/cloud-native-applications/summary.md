# Cloud-Native Applications - Summary

## Key Definitions and Concepts

- **Cloud-Native Applications**: Software programs designed specifically to run on cloud infrastructure, utilizing containerization, microservices, and dynamic orchestration to achieve scalability, resilience, and observability.

- **Microservices Architecture**: An architectural style that structures an application as a collection of loosely coupled, independently deployable services communicating via lightweight protocols.

- **Container**: Lightweight, standalone packages containing application code along with all dependencies needed for execution.

- **Kubernetes**: An open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.

- **Serverless Computing**: A cloud computing model where the cloud provider dynamically manages server allocation, with billing based on actual resource consumption.

## Important Formulas and Theorems

- **12-Factor App Methodology**: A set of twelve best practices for building SaaS applications covering codebase, dependencies, configuration, backing services, build/release/run, processes, port binding, concurrency, disposability, dev/prod parity, logs, and admin processes.

- **Auto-scaling Rules**: HPA typically scales based on CPU utilization threshold (70%) or custom metrics, with replica count bounds defined by minReplicas and maxReplicas.

## Key Points

- Cloud-native applications leverage cloud platform capabilities including elasticity, scalability, and automated resource management.

- Containerization (Docker) ensures consistent environments across development, testing, and production.

- Kubernetes provides essential features like service discovery, load balancing, automated rollouts/rollbacks, and self-healing.

- Microservices offer independent scaling and deployment but introduce complexity in distributed system management.

- Serverless computing is ideal for event-driven workloads with variable traffic patterns.

- Cloud-native design patterns (Circuit Breaker, Bulkhead) address resilience challenges in distributed systems.

- GitOps-based CI/CD pipelines automate deployment through Git as the single source of truth.

## Common Mistakes to Avoid

1. **Confusing containerization with virtualization**: Containers share the host OS kernel while virtual machines run complete operating systems.

2. **Over-decomposing microservices**: Creating too many fine-grained services increases operational complexity beyond benefits.

3. **Ignoring state management**: Treating stateless services while overlooking data consistency and persistence requirements.

4. **Neglecting security**: Failing to implement proper network policies, secrets management, and container image scanning.

5. **Not designing for failure**: Ignoring fault tolerance patterns leads to cascading failures in distributed systems.

## Revision Tips

1. Practice writing basic Dockerfiles and Kubernetes YAML configurations—these are frequently asked in practical exams.

2. Create comparison charts: Monolithic vs. Microservices, Synchronous vs. Asynchronous communication, VMs vs. Containers.

3. Review the 12-Factor App methodology thoroughly—know each factor with a one-line explanation.

4. Understand the complete Kubernetes architecture: control plane components, worker node components, and their interactions.

5. Solve previous years' question papers to identify frequently tested concepts and patterns.

6. Implement a mini-project using Docker and Kubernetes to gain hands-on experience with the concepts.