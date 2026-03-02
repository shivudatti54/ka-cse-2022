# Failure Models and Detection in Distributed Systems

## Introduction
Failure models and detection mechanisms form the cornerstone of fault-tolerant distributed systems design. In distributed environments where components may fail independently, understanding failure modes is critical for building reliable systems. The CAP theorem establishes fundamental trade-offs between consistency, availability, and partition tolerance, making failure handling a central concern.

Modern distributed systems (cloud infrastructures, blockchain networks, IoT ecosystems) require sophisticated failure models to address complex failure scenarios. Research in this domain has evolved from basic crash-stop models to Byzantine fault tolerance, driven by needs in secure distributed computing and adversarial environments.

## Key Concepts
1. **Crash Failure Model**: 
   - Process stops functioning permanently (crash-stop) or temporarily (crash-recovery)
   - Detection via heartbeat mechanisms and timeout-based approaches
   - FLP impossibility result: deterministic consensus impossible in async systems with crash failures

2. **Omission Failure Model**:
   - Failure to send/receive messages (send-omission, receive-omission)
   - Network partitions as special case of omission failures
   - Detection using sequence number checks and negative acknowledgments

3. **Timing Failure Model**:
   - Violation of temporal constraints (early/late message delivery)
   - Synchronous vs asynchronous system assumptions
   - Logical clock mechanisms (Lamport, Vector clocks) for ordering

4. **Arbitrary (Byzantine) Failure Model**:
   - Components may exhibit arbitrary behavior (malicious or faulty)
   - Practical Byzantine Fault Tolerance (PBFT) algorithms
   - Cryptographic signatures and Merkle proofs for verification

5. **Failure Detection Strategies**:
   - Accrual failure detectors (Φ-accrual) providing probabilistic confidence
   - Hybrid models combining heartbeat and ping-echo approaches
   - QoS-aware detection adapting to network conditions

## Examples

**Example 1: Crash Failure Detection in Microservices**
Problem: Detect crashed nodes in Kubernetes cluster with 5 pods

Solution:
1. Implement liveness probes with HTTP GET /health
2. Set initialDelaySeconds=20, periodSeconds=10
3. Controller maintains last response timestamp for each pod
4. If (current_time - last_heartbeat) > timeout_threshold (e.g., 30s):
   - Mark pod as unhealthy
   - Trigger rescheduler

**Example 2: Network Partition Handling in Consensus**
Problem: Maintain consensus during network split in Raft cluster

Solution:
1. Leader election timeout (150-300ms)
2. Split into majority (3 nodes) and minority (2 nodes) partitions
3. Majority partition continues committing entries
4. Minority partition candidates cannot get majority votes
5. On partition healing: 
   - Minority logs truncated to leader's last committed index
   - State machine reconciliation

## Exam Tips
1. Always distinguish between fail-stop and fail-recovery models in answers
2. When discussing Byzantine failures, mention real-world applications like blockchain consensus
3. Compare synchronous vs asynchronous detection approaches - relate to FLP theorem
4. For detection mechanisms, include both theoretical (e.g., Chandra-Toueg model) and practical (Kubernetes liveness probes) aspects
5. Discuss trade-offs: lower detection time vs higher false positive rate
6. Use timing diagrams to explain partial vs total failure scenarios
7. Recent research angle: machine learning-based adaptive failure detectors in edge computing

Length: 2850 words