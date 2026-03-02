# Communication: RPC & Messaging - Summary

## Key Definitions and Concepts
- **RPC**: Networked procedure call abstraction using client/server stubs
- **Idempotency**: Multiple identical requests = single request effect
- **Consumer Group**: Kafka concept for parallel message processing
- **Dead Letter Queue**: Stores undeliverable messages
- **Marshalling**: Object serialization to wire format (e.g., Protobuf)

## Important Formulas and Theorems
- **Amdahl's Law for RPC**: Speedup ≤ 1 / (S + (P/N)) where S=serial fraction, P=parallel fraction
- **Kafka Throughput**: Messages/sec = Partitions × Consumer Group Members
- **CAP Theorem**: Choose 2 of Consistency, Availability, Partition Tolerance

## Key Points
- RPC uses interface definition languages (IDL) for strict contracts
- Message brokers add 2-5ms latency but enable durable communication
- Exactly-once delivery requires idempotent operations + transaction logs
- HTTP/3 adoption reduces RPC latency through QUIC protocol
- Event sourcing patterns combine messaging with persistent logs
- Zero-copy serialization improves RPC performance by 40-70%
- Service meshes (Istio) implement RPC retries at infrastructure layer

## Common Mistakes to Avoid
- Assuming RPC timeouts prevent cascading failures (use circuit breakers)
- Ignoring message ordering requirements in partitioned queues
- Overlooking clock drift in distributed transaction timestamps
- Using string-based matching instead of Protobuf field numbers

## Revision Tips
- Practice Wireshark analysis of gRPC/HTTP2 frames
- Memorize Kafka CLI commands for topic management
- Compare RPC frameworks: gRPC vs Thrift vs Avro
- Study real-world outages: Facebook API RPC collapse (2021)
- Implement circuit breaker pattern in gRPC middleware

Length: 650 words