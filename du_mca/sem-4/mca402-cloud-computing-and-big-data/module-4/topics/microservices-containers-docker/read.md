# Microservices, Containers & Docker

## Introduction
Microservices architecture represents a paradigm shift in software development, breaking applications into small, independent services communicating via APIs. This approach enables continuous delivery/deployment, scalability, and technological heterogeneity. Containers provide lightweight virtualization by packaging applications with dependencies, while Docker emerged as the de facto standard for containerization.

The combination addresses critical cloud computing challenges:  
1. **Resource Efficiency**: Containers share host OS kernel vs full virtualization  
2. **DevOps Enablement**: Docker's "build once, run anywhere" philosophy streamlines CI/CD  
3. **Cloud-Native Design**: Microservices align perfectly with cloud elasticity and distributed systems  

Industry adoption spans Netflix (9,000+ microservices), Amazon, and Spotify. For Big Data systems, this architecture enables scalable processing pipelines and real-time analytics.

## Key Concepts
**Microservices Characteristics**  
- Service Decoupling: Each service owns its database and business logic  
- Bounded Context: Domain-driven design principles  
- Fault Isolation: Circuit breakers prevent cascading failures  
- Polyglot Persistence: Mix SQL/NoSQL databases as needed  

**Container Fundamentals**  
- Linux Namespaces: PID, network, mount namespace isolation  
- Control Groups (cgroups): Resource limits for CPU/memory  
- Union File Systems: Layered image construction  
- OCI Standards: Runtime and image specifications  

**Docker Ecosystem**  
- Docker Engine: Client-server architecture with containerd runtime  
- Dockerfile: Declarative image build instructions  
- Docker Compose: Multi-container application management  
- Docker Swarm: Native clustering and orchestration  
- Registry: Docker Hub and private image repositories  

**Orchestration**  
- Service Discovery: Consul, etcd  
- Load Balancing: NGINX, Traefik  
- Monitoring: Prometheus, Grafana dashboards  

## Examples

**1. Containerizing Python Microservice**  
```dockerfile
# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```
Build and run:  
```bash
docker build -t user-service .
docker run -d -p 5000:5000 --name user_svc user-service
```

**2. Microservices Communication**  
```python
# Order service (FastAPI)
@app.get("/orders/{user_id}")
async def get_orders(user_id: int):
    user_data = requests.get(f"http://user-service:5000/users/{user_id}")
    # Process order data with user info
```

**3. Docker Compose Setup**  
```yaml
version: '3.8'
services:
  redis:
    image: redis:alpine
    ports: ["6379:6379"]
  web:
    build: .
    ports: ["5000:5000"]
    depends_on: ["redis"]
```

## Exam Tips
1. Always contrast monolithic vs microservices architectures - mention scalability, deployment, and fault tolerance  
2. Understand Docker's layered filesystem - base image → intermediate layers → writable container layer  
3. Memorize essential commands: `docker build`, `docker-compose up`, `docker swarm init`  
4. Explain sidecar pattern in microservices - auxiliary containers for logging/monitoring  
5. Know Kubernetes vs Docker Swarm differences: complexity vs simplicity, community support  
6. Describe container networking models: bridge, host, overlay  
7. Discuss security aspects: image scanning, least privilege principle, secrets management