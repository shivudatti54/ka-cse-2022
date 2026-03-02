# Container Orchestration with Kubernetes - Summary

## Key Definitions and Concepts
- **Pod**: Smallest execution unit with shared storage/network
- **Deployment**: Manages replicated application Pods with update strategies
- **Service**: Network abstraction for Pod access
- **CRD**: Custom Resource Definition for extending Kubernetes API
- **Operator**: Kubernetes-native application controller

## Important Formulas and Theorems
- Desired State = Current State (Declarative Model)
- HPA Scaling: `desiredReplicas = ceil(currentReplicas * (currentMetricValue / desiredMetricValue))`
- Raft Consensus: Leader election and log replication for etcd

## Key Points
- Kubernetes uses declarative configuration via YAML manifests
- Control Plane components: API Server, etcd, Scheduler, Controller Manager
- Services enable loose coupling between microservices
- Persistent Volumes abstract storage from underlying infrastructure
- Network Policies implement zero-trust security models
- Operators automate complex application management
- Kubelet manages node-level operations and Pod lifecycle

## Common Mistakes to Avoid
- Forgetting resource requests/limits leading to node overcommit
- Misconfiguring liveness/readiness probes causing cascading failures
- Using default namespaces instead of creating environment-specific ones
- Ignoring PodDisruptionBudgets during cluster maintenance

## Revision Tips
- Practice creating Pods/Deployments/Services from scratch
- Use `kubectl explain` to understand API fields
- Set up minikube cluster for hands-on experimentation
- Study Kubernetes failure stories from production environments