# Container Orchestration with Kubernetes

## Introduction
Kubernetes has emerged as the de facto standard for container orchestration in distributed systems, revolutionizing how modern cloud-native applications are deployed and managed. Originally developed from Google's Borg system, Kubernetes provides a platform for automating deployment, scaling, and operations of application containers across clusters of hosts. 

In distributed systems, Kubernetes addresses critical challenges including service discovery, load balancing, storage orchestration, automated rollouts/rollbacks, and self-healing capabilities. Its importance extends to enabling microservices architectures, CI/CD pipelines, and hybrid cloud deployments. For DU MSc CS students, understanding Kubernetes is essential for working with large-scale systems like e-commerce platforms handling 10,000+ QPS or AI/ML workloads requiring dynamic resource allocation.

Recent research directions include Kubernetes' integration with serverless architectures (Knative), service meshes (Istio), and edge computing paradigms. The 2023 Kubernetes Chaos Engineering Report highlights how organizations use chaos mesh frameworks to test system resilience at scale.

## Key Concepts
1. **Pods**: Smallest deployable units containing one/more containers with shared storage/network
2. **Deployments**: Declarative updates for Pods and ReplicaSets with rollout strategies
3. **Services**: Abstract way to expose applications running on Pods (ClusterIP, NodePort, LoadBalancer)
4. **Namespaces**: Virtual clusters within physical clusters for resource isolation
5. **Kubelet**: Primary node agent managing Pod lifecycle and reporting to control plane
6. **Operators**: Kubernetes-native applications using Custom Resource Definitions (CRDs) for complex stateful apps
7. **Horizontal Pod Autoscaler**: Automatically scales number of Pods based on CPU/memory or custom metrics
8. **etcd**: Distributed key-value store maintaining cluster state with Raft consensus algorithm

Advanced concepts include Network Policies (CNI plugins), Persistent Volumes with CSI drivers, and Admission Controllers for security policies. Current research focuses on Kubernetes Federation for multi-cluster management and KubeEdge for edge computing.

## Examples

**Example 1: Deployment with Rolling Updates**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
```
Apply with `kubectl apply -f deployment.yaml`. Kubernetes maintains 3 replicas, updating pods incrementally.

**Example 2: Service Exposure**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: LoadBalancer
  selector:
    app: web
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```
This creates a cloud provider load balancer routing external traffic to Pods with `app: web` label.

**Example 3: Horizontal Pod Autoscaling**
```bash
kubectl autoscale deployment web-app --cpu-percent=50 --min=3 --max=10
```
Kubernetes automatically scales Pods when CPU utilization exceeds 50%, using metrics from Metrics Server.

## Exam Tips
1. Understand YAML manifest structure: Always specify apiVersion, kind, metadata, and spec
2. Differentiate Service types: ClusterIP (internal), NodePort (static port), LoadBalancer (external)
3. Know rollout commands: `kubectl rollout history deployment/web-app`
4. Master troubleshooting flow: Check Pods → Describe Pod → Check Events → Check Logs
5. Remember etcd's role: Only component with persistent storage in control plane
6. RBAC components: Roles, RoleBindings, ClusterRoles, ServiceAccounts
7. StatefulSet vs Deployment: Use StatefulSets for apps requiring stable network IDs/persistent storage