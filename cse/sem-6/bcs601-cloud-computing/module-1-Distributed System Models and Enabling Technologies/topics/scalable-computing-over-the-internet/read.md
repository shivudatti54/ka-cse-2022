# Scalable Computing Over the Internet

## 1. Introduction and Formal Definitions

Scalable computing denotes the capacity of a computing system to accommodate growing workloads while maintaining acceptable performance metrics. Formally, **scalability** refers to the ability of a system to handle increasing quantities of work, or its capability to be enlarged to accommodate that growth, without proportional degradation in performance. The formal definition encompasses two primary dimensions: **load scalability** (the system's ability to handle increased load by adding resources) and **generational scalability** (the system's ability to support newer and more powerful resources without redesign).

The exponential growth of internet users (exceeding 5 billion globally) and data generation (estimated at 463 exabytes daily) has rendered scalable computing over the internet indispensable for modern applications. This paradigm enables organizations to provision computing resources dynamically, aligning capacity with demand while optimizing cost structures.

## 2. Theoretical Models of Scalability

### 2.1 Amdahl's Law

Amdahl's Law provides a fundamental theoretical bound on the maximum speedup achievable through parallel processing. The law states that the theoretical speedup in latency of the execution of a program is limited by the sequential portion of the program.

**Formal Statement:** If $P$ represents the proportion of a program that can be parallelized and $(1-P)$ represents the sequential portion, then the maximum speedup $S$ achievable with $N$ processors is:

$$S(N) = \frac{1}{(1-P) + \frac{P}{N}}$$

**Proof:**
Let $T_1$ denote the execution time on a single processor. The sequential portion requires time $(1-P)T_1$. The parallel portion, distributed across $N$ processors, requires time $\frac{P \cdot T_1}{N}$. Therefore:

$$T_N = (1-P)T_1 + \frac{P \cdot T_1}{N} = T_1\left[(1-P) + \frac{P}{N}\right]$$

The speedup factor $S(N) = \frac{T_1}{T_N}$ yields the stated formula.

**Implication:** As $N \to \infty$, the maximum speedup approaches $\frac{1}{1-P}$, establishing a fundamental ceiling independent of processor count. For instance, with $P = 0.95$ (95% parallelizable), maximum speedup is limited to 20x regardless of processor availability.

### 2.2 Gustafson's Law

Gustafson's Law addresses a limitation in Amdahl's Law by considering scaled problems rather than fixed problems. It demonstrates that with sufficiently large problem sizes, nearly linear speedup is achievable.

**Formal Statement:**
$$S(N) = (1-P) + N \cdot P$$

where $P$ represents the parallel fraction and $N$ denotes processor count.

**Contrast with Amdahl's Law:** While Amdahl's Law assumes fixed problem size, Gustafson's Law assumes fixed execution time, allowing problem size to scale with available resources. This model better represents real-world scenarios where larger datasets necessitate increased computational capacity.

## 3. Scalability Dimensions and Trade-offs

### 3.1 Vertical Scaling (Scale-Up)

Vertical scaling involves augmenting resources (CPU cores, RAM, storage I/O) within a single node. The performance improvement follows the relationship:

$$Performance_{new} = Performance_{old} \times \frac{Resource_{new}}{Resource_{old}} \times Efficiency_{factor}$$

**Advantages:**
- **Architectural Simplicity:** Single-node architecture eliminates distributed system complexities
- **Application Transparency:** No code modification required; existing monolithic applications function unchanged
- **Consistent Performance:** Shared memory eliminates network latency overhead

**Disadvantages:**
- **Physical Limits:** Moore's Law diminishing returns and hardware ceilings
- **Single Point of Failure:** Node failure incapacitates entire service
- **Cost Escalation:** Hardware costs increase non-linearly; enterprise-grade components command premium pricing
- **Theoretical Bound:** Subject to Amdahl's Law constraints

### 3.2 Horizontal Scaling (Scale-Out)

Horizontal scaling adds nodes to the system, distributing load across multiple servers.

**Performance Model:**
$$Throughput_N = Throughput_1 \times N \times Efficiency(N)$$

where $Efficiency(N)$ accounts for coordination overhead decreasing with $N$.

**Advantages:**
- **Theoretical Unboundedness:** Linear scalability approaching $O(N)$ for embarrassingly parallel workloads
- **Fault Tolerance:** Redundant nodes ensure continued operation during failures
- **Cost Efficiency:** Commodity hardware reduces per-unit computational cost

**Disadvantages:**
- **Architectural Complexity:** Requires distributed system design patterns
- **Network Latency:** Inter-node communication introduces $O(\log N)$ or $O(N)$ overhead
- **Consistency Challenges:** CAP theorem implications necessitate trade-off decisions
- **Management Overhead:** Orchestration, monitoring, and deployment complexity

## 4. CAP Theorem and Consistency Trade-offs

Brewer's CAP Theorem states that a distributed data store cannot simultaneously provide all three guarantees: **Consistency** (all nodes see identical data), **Availability** (every request receives response), and **Partition Tolerance** (system continues operation despite network failures).

**Formal Statement:**
$$CAP \equiv \text{At most two of three properties can be simultaneously guaranteed}$$

**Implications for Scalable Systems:**

| Primary Guarantee | System Characteristics | Use Cases |
|-------------------|----------------------|-----------|
| CA (no partitions) | Traditional RDBMS | Banking, transactional systems |
| CP (consistency) | ZooKeeper, etcd | Distributed coordination, inventory |
| AP (availability) | Cassandra, DynamoDB | Social media, analytics |

**Consistency Models in Distributed Systems:**

1. **Strong Consistency:** All reads see most recent write (Linearizability)
2. **Eventual Consistency:** Writes propagate asynchronously; convergence guaranteed
3. **Causal Consistency:** Causally related operations maintain order
4. **Read Your Writes Consistency:** Author sees own writes immediately

## 5. Load Balancing Algorithms

Load balancers distribute incoming traffic across multiple servers using various algorithms:

### 5.1 Round Robin (RR)
- **Description:** Requests distributed sequentially across servers
- **Complexity:** $O(N)$ per request
- **Suitability:** Homogeneous server populations with equal capacity

### 5.2 Weighted Round Robin (WRR)
- **Description:** Server weights $w_i$ determine request allocation proportion
- **Complexity:** $O(N)$ per request
- **Formula:** Server $i$ receives $\frac{w_i}{\sum w_j}$ fraction of requests

### 5.3 Least Connections (LC)
- **Description:** Request routed to server with fewest active connections
- **Complexity:** $O(\log N)$ with min-heap implementation
- **Suitability:** Variable request processing times

### 5.4 Weighted Least Connections (WLC)
- **Description:** Considers both active connections and server weight
- **Complexity:** $O(\log N)$
- **Selection:** Server minimizing $\frac{active\_connections}{weight}$

### 5.5 IP Hash
- **Description:** Consistent hashing based on source IP
- **Complexity:** $O(1)$ lookup
- **Suitability:** Session persistence requirements

## 6. Enabling Technologies

### 6.1 Virtualization
Hypervisors (Type-1: VMware ESXi; Type-2: VirtualBox) enable multiple virtual machines on physical hardware, providing **resource isolation** and **multitenancy**. Live migration capabilities ensure zero-downtime scaling.

### 6.2 Container Orchestration
Kubernetes provides automated deployment, scaling, and management of containerized applications through:
- **Pod scheduling** with resource quotas
- **Horizontal Pod Autoscaler (HPA)** triggering scale events based on CPU/memory metrics
- **Service discovery** enabling dynamic scaling

### 6.3 Distributed Storage
- **HDFS:** Block-based replication (default: 3x) across DataNodes
- **Object Storage:** Amazon S3, Google Cloud Storage with eventual consistency
- **NoSQL Databases:** MongoDB (document), Cassandra (wide-column) with tunable consistency

## 7. Cloud Service Models

| Model | Management Level | Examples | Scalability |
|-------|------------------|----------|-------------|
| IaaS | Infrastructure only | AWS EC2, GCP Compute | User-managed auto-scaling |
| PaaS | Platform | Heroku, Azure App Service | Built-in scaling |
| SaaS | Fully managed | Salesforce, Office 365 | Provider-managed |

## 8. Challenges in Scalable Internet Computing

1. **Network Latency:** Speed of light limitations; $RTT = 2 \times \frac{distance}{c}$ (approximately 1ms per 200km)
2. **Data Consistency:** Distributed transactions impose $2PC$ coordination overhead
3. **Security Surface:** Expanded attack vectors in distributed environments
4. **Cost Optimization:** Right-sizing resources requires sophisticated monitoring
5. **Operational Complexity:** Distributed debugging and tracing challenges

## 9. Hard-Level Multiple Choice Questions

### Question 1
A web application processes 10,000 requests per second with an average response time of 50ms. The application runs on 20 identical servers, each handling 500 requests/second. The development team proposes adding 10 more servers. Calculate the theoretical maximum improvement in throughput if the application exhibits 85% parallelizable workload.

(A) 1.33x improvement
(B) 1.5x improvement
(C) 1.85x improvement
(D) 2.0x improvement

**Answer: (B) 1.5x improvement**

**Explanation:** Using Amdahl's Law with $P = 0.85$ and $N_{old} = 20$, $N_{new} = 30$:
- Original speedup potential: $S_{max} = \frac{1}{1-0.85} = \frac{1}{0.15} = 6.67x$
- With 30 processors: $S(30) = \frac{1}{0.15 + \frac{0.85}{30}} = \frac{1}{0.15 + 0.0283} = \frac{1}{0.1783} = 5.6x$
- Improvement ratio: $\frac{5.6x}{3.76x} \approx 1.5x$

### Question 2
A distributed system requires strong consistency for financial transactions but must handle 100,000 concurrent users globally. According to CAP theorem, which architectural decision addresses this requirement?

(A) Deploy across multiple datacenters in different geographic regions
(B) Implement read-replicas in each region with asynchronous replication
(C) Single-region deployment with synchronous cross-zone replication
(D) Use eventual consistency with conflict resolution

**Answer: (C) Single-region deployment with synchronous cross-zone replication**

**Explanation:** Strong consistency requires CA (no partitions). Single-region deployment with synchronous replication within the region ensures consistency and availability within the region. Geographic distribution would introduce partitions, forcing a CP (consistency + partition tolerance) choice. Options B and D sacrifice strong consistency, while A introduces partitions.

### Question 3
A load balancer uses weighted least connections algorithm. Server A has weight 4 with 8 active connections; Server B has weight 2 with 3 active connections. To which server should the next request be routed?

(A) Server A
(B) Server B
(C) Both equally likely
(D) Cannot be determined

**Answer: (B) Server B**

**Explanation:** WLC selects the server minimizing $\frac{active\_connections}{weight}$:
- Server A: $\frac{8}{4} = 2.0$
- Server B: $\frac{3}{2} = 1.5$

Server B has the lower metric (1.5 < 2.0), so the next request routes to Server B despite having fewer absolute connections.

### Question 4
Given a program with 20% sequential code, calculate the maximum speedup achievable using 64 processors according to Amdahl's Law.

(A) 4.21x
(B) 4.85x
(C) 5.00x
(D) 64x

**Answer: (B) 4.85x**

**Explanation:** With $P = 0.80$ (parallelizable portion) and $N = 64$:
$$S(64) = \frac{1}{(1-0.80) + \frac{0.80}{64}} = \frac{1}{0.20 + 0.0125} = \frac{1}{0.2125} \approx 4.85x$$

This demonstrates that despite 64 processors, Amdahl's Law limits speedup to approximately 5x due to the 20% sequential bottleneck.